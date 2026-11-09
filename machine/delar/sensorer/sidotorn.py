"""Sidotorn för sensorenheten på LowRider V4 Core, utkast (ej printat, ej verifierat).

All geometri i fräsramen M, millimeter: x bort från balken, y längs balken
(+y är maskinens X max-sida), z upp, fräsaxeln i x=y=0.

Kraven kommer från användaren 2026-11-09: bilderna sys ihop, så servo och dammsko
får synas och maskas bort; servot står kvar; kameran rakt ned, linsen 130 mm;
plats för två diffuserade LED men inget inköp före bildprov.

Torn och arm skiljer ansvar: armens två hårda stopp bestämmer lägena, servot
bara driver rörelsen. Parkerat ligger armen förbi lodlinjen så att tyngden håller
den mot stoppet; kameran bekräftar läget före varje jobb (D020), inga brytare.

Kör: python sidotorn.py --ut KATALOG
"""
from __future__ import annotations

import argparse
import copy
import math
from pathlib import Path

from build123d import (Box, Color, Compound, Cylinder, Plane, Polygon, Pos, Rot,
                       export_step, export_stl, extrude, fillet, Axis)

# Tornets gränser: inte förbi Core-änden längs balken, inte förbi dammskon utåt.
Y0, Y1 = 48.5, 72.5
X_DAMMSKO = 107.6

# Kamera: linsens spets. Långsidan (66 grader) ut från balken.
LINS = (94.0, 53.0, 130.0)
KORT_B, KORT_D = 25.0, 23.86
KORT_HAL = (21.0, 12.5)     # nominellt, kontrolleras mot levererat kort
BUK = LINS[2] + 2.6         # tornets plana undersida vid kameran
XEND = LINS[0] + 13.5

# Pi Zero 2 WH: kortet i XZ-planet, komponenterna mot locket.
PI_RUM = (12.0, 79.8, 123.0, 156.5)      # x0, x1, z0, z1
PI_Y = 55.0                              # kortets undersida
PI_CENTER = (45.0, 139.5)
PI_HAL = [(PI_CENTER[0] + dx, PI_CENTER[1] + dz) for dx in (-29, 29) for dz in (-11.5, 11.5)]
PANEL_X = 84.0                           # sidopanelens bakre gräns mot kamerablocket
PANEL_HAL = [(15.0, 125.5), (77.0, 125.5), (15.0, 155.0), (77.0, 155.0), (15.0, 64.5), (44.0, 64.5)]
ACC_HAL = [(26.0, 104.0), (41.0, 104.0)]   # nominellt, kontrolleras mot levererad ADXL345

# Servo (SPMS664, befintligt läge) och arm.
PX, PZ = 45.0, 43.6
PARK = -165.0               # utfällt 0, parkerat förbi lodlinjen: tyngden håller armen mot stoppet
SERVO_DY = -2.0             # hela servopaketet flyttat längs balken så att kåpans vägg ryms före Core-änden
ARM_Y = (21.5 + SERVO_DY, 25.5 + SERVO_DY)
BLT = (61.0, 34.0 + SERVO_DY)
FRAM_Y = (43.3 + SERVO_DY, 49.3 + SERVO_DY)
FLANS_Z = 6.4
HUB_D = 15.0
ARM_W = (7.5, 5.0)         # halv bredd vid navet och vid plattan

KAPA_Y = Y1
KAPA_T = 1.4

# Hårda stopp: armens två sidor slår mot var sitt fast block på 7-15 mm radie.
STOPP_T = (7.0, 15.0)       # längs armen från navet
STOPP_TJOCK = 5.0


def box(a, b):
    return Pos((a[0] + b[0]) / 2, (a[1] + b[1]) / 2, (a[2] + b[2]) / 2) * Box(
        b[0] - a[0], b[1] - a[1], b[2] - a[2])


def cyl_x(y, z, x0, x1, d):
    return Pos((x0 + x1) / 2, y, z) * Rot(0, 90, 0) * Cylinder(d / 2, x1 - x0)


def cyl_y(x, z, y0, y1, d):
    return Pos(x, (y0 + y1) / 2, z) * Rot(90, 0, 0) * Cylinder(d / 2, y1 - y0)


def prisma_y(pts, y0, y1):
    return extrude(Plane.XZ.offset(-y0) * Polygon(*pts, align=None), amount=y1 - y0, dir=(0, 1, 0))


def inset(pts, d):
    """Polygon flyttad d mm inåt (pts moturs), hörnen blir skärningar."""
    n = len(pts)
    lines = []
    for i in range(n):
        (x0, z0), (x1, z1) = pts[i], pts[(i + 1) % n]
        L = math.hypot(x1 - x0, z1 - z0)
        nx, nz = -(z1 - z0) / L, (x1 - x0) / L
        lines.append(((x0 + nx * d, z0 + nz * d), ((x1 - x0) / L, (z1 - z0) / L)))
    ut = []
    for i in range(n):
        (p, u), (q, v) = lines[i - 1], lines[i]
        t = ((q[0] - p[0]) * v[1] - (q[1] - p[1]) * v[0]) / (u[0] * v[1] - u[1] * v[0])
        ut.append((p[0] + t * u[0], p[1] + t * u[1]))
    return ut


def sidoprofil():
    """Tornets sida bakom panelen, från rygg till kamerablocket."""
    b = BUK
    rz = 56 + (PANEL_X - 52) * (b - 56) / (LINS[0] - 8 - 52)
    return [(8, 56), (52, 56), (PANEL_X, rz), (PANEL_X, b + 29.4), (8, b + 29.4)]


def arm_geo(blt_x):
    """Armens riktning u och sidnormal n, längden L."""
    bx, bz = blt_x, FLANS_Z + 3
    L = math.hypot(bx - PX, bz - PZ)
    ux, uz = (bx - PX) / L, (bz - PZ) / L
    return (ux, uz), (-uz, ux), L


def vrid(p, grader):
    """Samma vridning som parkera(), runt navet i XZ-planet."""
    g = math.radians(grader)
    dx, dz = p[0] - PX, p[1] - PZ
    return (PX + dx * math.cos(g) + dz * math.sin(g), PZ - dx * math.sin(g) + dz * math.cos(g))


def stopp_block(blt_x, sida, w0, w1):
    """Fyrhörning som ligger an mot armens sida; sida=-1 utfällt, +1 parkerat."""
    u, n, L = arm_geo(blt_x)
    def pkt(t, ut):
        w = w0 + (w1 - w0) * t / L + ut
        return (PX + u[0] * t + sida * n[0] * w, PZ + u[1] * t + sida * n[1] * w)
    pts = [pkt(STOPP_T[0], 0), pkt(STOPP_T[1], 0), pkt(STOPP_T[1], STOPP_TJOCK), pkt(STOPP_T[0], STOPP_TJOCK)]
    return [vrid(p, PARK) for p in pts] if sida > 0 else pts


def servokapa():
    """Yttre form runt servots bakdel; samma hörnradie som tornet."""
    k = box((12.6, FRAM_Y[0] + 1, 29.6), (57.4, KAPA_Y, 70.0))
    return fillet(k.edges().filter_by(Axis.Y), 4.0)


def servo_attrapp():
    d = SERVO_DY
    kropp = box((14.8, 32.6 + d, 33.6), (55.2, 73 + d, 53.6))
    oron = box((5.1, 40.8 + d, 33.6), (64.9, 43.3 + d, 53.6))
    return kropp + oron + cyl_y(PX, PZ, 26.6 + d, 33.0 + d, 6.0)


def torn(blt_x=BLT[0]):
    b = BUK
    prof = [(8, 56), (52, 56), (LINS[0] - 8, b), (XEND, b), (XEND, b + 15.4), (84, b + 29.4), (8, b + 29.4)]
    s = prisma_y(prof, Y0, Y1)
    s = fillet(s.edges().filter_by(Axis.Y), 4.0)
    # Fästplatta mot verktygsfästet, samma två M5-lägen som V1E-skruvarna.
    s += box((1, 39, 56), (9, Y0 + 1, 134))
    s += box((1, Y0, 56), (14, 53, 134))      # bär över lasten från fästplattan in i tornet
    for z in (64.25, 125.25):
        s += cyl_x(43.95, z, -7.3, 1.2, 9.6)
        s -= cyl_x(43.95, z, -9, 10, 5.4)
    # Servoram med fönster för kroppen, och skena upp till fästplattan.
    xa, xb = 7.0, 67.0      # fästöronen sitter vid x 11,7 och 59
    ram = box((xa, FRAM_Y[0], 27.6), (xb, FRAM_Y[1], 58.5))
    s += fillet(ram.edges().filter_by(Axis.Y), 3.0)
    # Kåpa runt servots bakre del, i samma plan som sidopanelen.
    s += servokapa()
    s -= box((PX - 30.2, FRAM_Y[0] - 1, 33.4), (PX + 10.2, FRAM_Y[1] + 2, 53.8))
    s -= box((PX - 30.4, FRAM_Y[1], 33.2), (PX + 10.4, KAPA_Y - KAPA_T, 54.0))
    s += box((8, FRAM_Y[0], 53.8), (xb - 3, 52, 58.5))
    for x in (PX - 33.3, PX + 14):
        for z in (PZ - 4.7, PZ + 4.7):
            s -= cyl_y(x, z, FRAM_Y[0] - 1, FRAM_Y[1] + 1, 3.4)
    # Hårda stopp i armens plan, hållna av skenor över och under servot.
    s += prisma_y(stopp_block(blt_x, -1, ARM_W[0], ARM_W[1]), ARM_Y[0], ARM_Y[1] + 1.2)
    s += box((33, ARM_Y[1] + 1.0, 27.6), (45, FRAM_Y[0] + .2, 33.2))
    s += prisma_y(stopp_block(blt_x, 1, ARM_W[0], ARM_W[1]), ARM_Y[0], ARM_Y[1] + 1.2)
    s += box((31, ARM_Y[1] + 1.0, 54.0), (47, FRAM_Y[0] + .2, 58.5))
    s += box((30.5, ARM_Y[0], 54.0), (33.5, ARM_Y[1] + 1.2, 58.5))   # förstärker parkeringsstoppet mot skenan
    # Kameran: nos under buken, urtag för kortet, två LED-spår symmetriskt runt linsen.
    cx, cy, _ = LINS
    # Nosen stiger mjukt upp i tornets framsida i stället för att vara en kloss.
    prof = Plane.YZ.offset(cx - 13.5) * Polygon((33, b), (Y0 + 1, b), (Y0 + 1, b + 22), (33, b + 8), align=None)
    nos = extrude(prof, amount=XEND - (cx - 13.5), dir=(1, 0, 0))
    s += fillet(nos.edges().filter_by(Axis.X), 2.0)
    s -= box((cx - KORT_B / 2 - .1, cy - KORT_D / 2 - .1, b - 1), (cx + KORT_B / 2 + .1, cy + KORT_D / 2 + .1, b + 2.5))
    for dx in (-KORT_HAL[0] / 2, KORT_HAL[0] / 2):
        for dy in (-KORT_HAL[1] / 2, KORT_HAL[1] / 2):
            s -= Pos(cx + dx, cy + dy, b + 4) * Cylinder(0.85, 6)
    for y in (cy - 15.5, cy + 15.5):
        s -= box((cx - 10, y - 2.5, b - 1), (cx + 10, y + 2.5, b + 2))
        s -= Pos(cx - 6.5, y, b + 3) * Cylinder(1.5, 6)
    s = med_elektronik(s)
    return s


def med_elektronik(s):
    """Elektronikrum bakom en enda sidopanel, och alla kablar dolda inuti tornet."""
    b = BUK
    x0, x1, z0, z1 = PI_RUM
    s -= prisma_y(inset(sidoprofil(), 4.0), 51, Y1 - 1.9)
    s -= prisma_y(inset(sidoprofil(), 2.0), Y1 - 2, Y1 + 1)
    # Tvärribba som styvar väggarna; fönster för kablar.
    s += box((48, 50.5, 59.5), (51, Y1 - 2.1, 122)) - box((47, 52, 62), (52, 62, 74))
    # Pi (hålbild 58 x 23) och accelerometer på tornets innervägg.
    for x, z in PI_HAL + ACC_HAL:
        s += cyl_y(x, z, 50.5, PI_Y, 6.0)
        s -= cyl_y(x, z, 49.9, PI_Y + 1, 2.2)
    for x, z in PANEL_HAL[:4]:
        s += cyl_y(x, z, 64.5, Y1 - 2, 7.0)
    for x, z in PANEL_HAL[4:]:
        s += cyl_y(x, z, 50.5, Y1 - 2, 7.0)
    for x, z in PANEL_HAL:
        s -= cyl_y(x, z, 62.0, Y1 - 1.5, 2.5)
    # CSI: från Pi:ns kortsida över till kameran, öppning ner till kortets kant.
    s -= box((x1 - 0.5, 60.5, b + 3.5), (LINS[0] + 6.5, 70, b + 13.4))
    s -= box((x1 - 0.5, 52, b + 3.5), (82.2, 60.6, b + 13.4))    # plats för flatkabeln vid Pi-kortets kant
    s -= box((LINS[0] - 6.5, LINS[1] + 9, b + 2.4), (LINS[0] + 6.5, LINS[1] + 13.5, b + 4))
    # LED-ledningen från den främre listen går i en kanal in i CSI-rummet.
    s -= box((LINS[0] - 7.5, 35.5, b + 3.6), (LINS[0] - 5.5, 61, b + 5.6))
    # Servokabeln upp ovanför servot; BLTouch-kabeln genom skenan över servot.
    s -= box((25, 52, 53.5), (43, 62, 61))
    s -= box((37, ARM_Y[1] + 0.5, 55), (43, 52.5, 57.5))
    # Samlad kabel ut bakåt, in i gapet mot Core där den inte syns framifrån.
    s -= box((7, 56, 108), (13, 66, 118))
    for y in (54, 62):                                      # buntbandsbryggor före utgången
        s += box((11, y, 102), (22, y + 2, 106))
    return s


def sidopanel():
    """Tornets hela sida som en enda panel, plan mot X max-sidan."""
    p = prisma_y(inset(sidoprofil(), 2.15), Y1 - 2, Y1)
    for x, z in PANEL_HAL:
        p -= cyl_y(x, z, Y1 - 3, Y1 + 1, 3.4)
        p -= cyl_y(x, z, Y1 - 1, Y1 + 1, 6.2)
    for z in (127, 132, 137, 142, 147, 152):
        p -= box((28, Y1 - 3, z - 0.9), (62, Y1 + 1, z + 0.9))
    return p


def arm(blt_x=BLT[0]):
    y0, y1 = ARM_Y
    w0, w1 = ARM_W
    u, n, L = arm_geo(blt_x)
    bx, bz = blt_x, FLANS_Z + 3
    a = prisma_y([(PX + n[0] * w0, PZ + n[1] * w0), (bx + n[0] * w1, bz + n[1] * w1),
                  (bx - n[0] * w1, bz - n[1] * w1), (PX - n[0] * w0, PZ - n[1] * w0)], y0, y1)
    a += cyl_y(PX, PZ, y0, y1, HUB_D)
    a += box((blt_x - 13, y0, FLANS_Z), (blt_x + 13, BLT[1] + 6, FLANS_Z + 4.5))
    # Dolt spår för BLTouch-kabeln, på armens sida mot servot.
    a -= prisma_y([(PX + u[0] * 12 + n[0] * 1.75, PZ + u[1] * 12 + n[1] * 1.75),
                   (bx + n[0] * 1.75, bz + n[1] * 1.75), (bx - n[0] * 1.75, bz - n[1] * 1.75),
                   (PX + u[0] * 12 - n[0] * 1.75, PZ + u[1] * 12 - n[1] * 1.75)], y1 - 2, y1 + .1)
    a -= box((blt_x - 1.75, y1 - .5, FLANS_Z + 3), (blt_x + 1.75, BLT[1] - 4.5, FLANS_Z + 5))
    for x in (blt_x - 9, blt_x + 9):
        a -= Pos(x, BLT[1], FLANS_Z + 2) * Cylinder(1.7, 10)
    a -= Pos(blt_x, BLT[1], FLANS_Z + 2) * Cylinder(5, 10)
    a -= cyl_y(PX, PZ, y0 - 1, y1 + 1, 7.5)
    return a


def bltouch(blt_x=BLT[0]):
    x, y, f = blt_x, BLT[1], FLANS_Z
    return box((x - 13, y - 5.75, f - 2.5), (x + 13, y + 5.75, f)) + box(
        (x - 6.5, y - 6.5, f - 36.3), (x + 6.5, y + 6.5, f - 2.5)) + (Pos(x, y, f - 41) * Cylinder(1, 9.4))


def parkera(o):
    return Pos(PX, 0, PZ) * Rot(0, PARK, 0) * Pos(-PX, 0, -PZ) * o


def namn(o, etikett, farg):
    o.label = etikett
    o.color = Color(*farg)
    return o


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ut", required=True, type=Path)
    p.add_argument("--blt-x", type=float, default=BLT[0])
    a = p.parse_args()
    a.ut.mkdir(parents=True, exist_ok=True)
    t, ar, bl = torn(a.blt_x), arm(a.blt_x), bltouch(a.blt_x)
    l = sidopanel()
    for n, o in (("torn", t), ("arm", ar), ("bltouch", bl), ("sidopanel", l)):
        print(n, "giltig", o.is_valid, "solider", len(o.solids()), "volym cm3", round(o.volume / 1000, 1),
              "bbox", [round(v, 1) for v in (*o.bounding_box().min, *o.bounding_box().max)])
        export_stl(o, str(a.ut / f"{n}.stl"), tolerance=.05, angular_tolerance=.2)
    cx, cy, cz = LINS
    delar = [
        namn(t, "Sidotorn", (.16, .18, .2)),
        namn(servo_attrapp(), "Servo_SPMS664_ATTRAPP", (.1, .1, .12)),
        namn(ar, "Arm_utfalld", (.9, .62, .29)),
        namn(bl, "BLTouch_utfalld_ATTRAPP", (.85, .2, .15)),
        namn(parkera(copy.deepcopy(ar)), "Arm_parkerad", (.9, .62, .29)),
        namn(parkera(copy.deepcopy(bl)), "BLTouch_parkerad_ATTRAPP", (.85, .2, .15)),
        namn(box((cx - KORT_B / 2, cy - KORT_D / 2, BUK + .5), (cx + KORT_B / 2, cy + KORT_D / 2, BUK + 2.5)), "Kamerakort_ATTRAPP", (.1, .45, .2)),
        namn(Pos(cx, cy, cz + 1.5) * Cylinder(5.5, 3), "Lins_ATTRAPP", (.05, .05, .05)),
        namn(box((PI_CENTER[0] - 32.5, PI_Y, PI_CENTER[1] - 15), (PI_CENTER[0] + 32.5, PI_Y + 1.4, PI_CENTER[1] + 15)), "Pi_Zero_2_ATTRAPP", (.15, .55, .3)),
        namn(l, "Sidopanel", (.16, .18, .2)),
    ]
    for y, e in ((cy - 15.5, "LED_1_ATTRAPP"), (cy + 15.5, "LED_2_ATTRAPP")):
        delar.append(namn(box((cx - 10, y - 2.5, BUK), (cx + 10, y + 2.5, BUK + 2)), e, (.95, .95, .8)))
    export_step(Compound(label="Sidotorn_v2", children=delar), str(a.ut / "sidotorn_v2.step"))
    print("klar")


if __name__ == "__main__":
    main()
