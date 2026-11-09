"""Sidotorn för sensorenheten på LowRider V4 Core, utkast (ej printat, ej verifierat).

All geometri i fräsramen M, millimeter: x bort från balken, y längs balken
(+y är maskinens X max-sida), z upp, fräsaxeln i x=y=0.

Kraven kommer från användaren 2026-11-09: bilderna sys ihop, så servo och dammsko
får synas och maskas bort; servot står kvar; kameran rakt ned, linsen 130 mm;
plats för två diffuserade LED men inget inköp före bildprov.

Torn och arm skiljer ansvar: armens två hårda stopp bestämmer lägena, servot
bara driver rörelsen. Brytare och Pi-kapsling är inte ritade än.

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
Y0, Y1 = 48.5, 72.0
X_DAMMSKO = 107.6

# Kamera: linsens spets. Långsidan (66 grader) ut från balken.
LINS = (94.0, 53.0, 130.0)
KORT_B, KORT_D = 25.0, 23.86
KORT_HAL = (21.0, 12.5)     # nominellt, kontrolleras mot levererat kort
BUK = LINS[2] + 2.6         # tornets plana undersida vid kameran
XEND = LINS[0] + 13.5

# Servo (SPMS664, befintligt läge) och arm.
PX, PZ = 45.0, 43.6
PARK = -140.0               # utfällt 0 grader, parkerat -140 grader
ARM_Y = (21.5, 25.5)
BLT = (61.0, 34.0)
FLANS_Z = 6.4
HUB_D = 18.0
ARM_W = (9.0, 6.0)         # halv bredd vid navet och vid plattan

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


def torn(blt_x=BLT[0]):
    b = BUK
    prof = [(8, 56), (52, 56), (LINS[0] - 8, b), (XEND, b), (XEND, b + 15.4), (84, b + 29.4), (8, b + 29.4)]
    s = prisma_y(prof, Y0, Y1)
    s = fillet(s.edges().filter_by(Axis.Y), 4.0)
    # Fästplatta mot verktygsfästet, samma två M5-lägen som V1E-skruvarna.
    s += box((1, 39, 56), (9, Y0 + 1, 134))
    for z in (64.25, 125.25):
        s += cyl_x(43.95, z, -7.3, 1.2, 9.6)
        s -= cyl_x(43.95, z, -9, 10, 5.4)
    # Servoram med fönster för kroppen, och skena upp till fästplattan.
    xa, xb = PX - 31.5, PX + 16.5
    s += box((xa, 43.3, 27.6), (xb, 49.3, 58.5)) - box((PX - 30.2, 42, 33.4), (PX + 10.2, 51, 53.8))
    s += box((8, 43.3, 53.8), (xb, 52, 58.5))
    # Hårda stopp i armens plan, hållna av skenor över och under servot.
    s += prisma_y(stopp_block(blt_x, -1, ARM_W[0], ARM_W[1]), ARM_Y[0], ARM_Y[1] + 1.2)
    s += box((33, ARM_Y[1] + 1.0, 27.6), (45, 43.5, 33.2))
    s += prisma_y(stopp_block(blt_x, 1, ARM_W[0], ARM_W[1]), ARM_Y[0], ARM_Y[1] + 1.2)
    s += box((31, ARM_Y[1] + 1.0, 54.0), (47, 43.5, 58.5))
    # Kameran: nos under buken, urtag för kortet, två LED-spår symmetriskt runt linsen.
    cx, cy, _ = LINS
    s += box((cx - 13.5, 33, b), (XEND, Y0 + 1, b + 10))
    s -= box((cx - KORT_B / 2 - .1, cy - KORT_D / 2 - .1, b - 1), (cx + KORT_B / 2 + .1, cy + KORT_D / 2 + .1, b + 2.5))
    for dx in (-KORT_HAL[0] / 2, KORT_HAL[0] / 2):
        for dy in (-KORT_HAL[1] / 2, KORT_HAL[1] / 2):
            s -= Pos(cx + dx, cy + dy, b + 4) * Cylinder(0.85, 6)
    for y in (cy - 15.5, cy + 15.5):
        s -= box((cx - 10, y - 2.5, b - 1), (cx + 10, y + 2.5, b + 3))
    return s


def arm(blt_x=BLT[0]):
    y0, y1 = ARM_Y
    w0, w1 = ARM_W
    u, n, L = arm_geo(blt_x)
    bx, bz = blt_x, FLANS_Z + 3
    a = prisma_y([(PX + n[0] * w0, PZ + n[1] * w0), (bx + n[0] * w1, bz + n[1] * w1),
                  (bx - n[0] * w1, bz - n[1] * w1), (PX - n[0] * w0, PZ - n[1] * w0)], y0, y1)
    a += cyl_y(PX, PZ, y0, y1, HUB_D)
    a += box((blt_x - 13, y0, FLANS_Z), (blt_x + 13, 40, FLANS_Z + 4.5))
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
    for n, o in (("torn", t), ("arm", ar), ("bltouch", bl)):
        print(n, "giltig", o.is_valid, "solider", len(o.solids()), "volym cm3", round(o.volume / 1000, 1),
              "bbox", [round(v, 1) for v in (*o.bounding_box().min, *o.bounding_box().max)])
        export_stl(o, str(a.ut / f"{n}.stl"), tolerance=.05, angular_tolerance=.2)
    cx, cy, cz = LINS
    delar = [
        namn(t, "Sidotorn", (.16, .18, .2)),
        namn(ar, "Arm_utfalld", (.9, .62, .29)),
        namn(bl, "BLTouch_utfalld_ATTRAPP", (.85, .2, .15)),
        namn(parkera(copy.deepcopy(ar)), "Arm_parkerad", (.9, .62, .29)),
        namn(parkera(copy.deepcopy(bl)), "BLTouch_parkerad_ATTRAPP", (.85, .2, .15)),
        namn(box((cx - KORT_B / 2, cy - KORT_D / 2, BUK + .5), (cx + KORT_B / 2, cy + KORT_D / 2, BUK + 2.5)), "Kamerakort_ATTRAPP", (.1, .45, .2)),
        namn(Pos(cx, cy, cz + 1.5) * Cylinder(5.5, 3), "Lins_ATTRAPP", (.05, .05, .05)),
        namn(box((14, 52, 120), (79, 66, 146)), "Pi_Zero_utrymme_ATTRAPP", (.15, .55, .3)),
    ]
    for y, e in ((cy - 15.5, "LED_1_ATTRAPP"), (cy + 15.5, "LED_2_ATTRAPP")):
        delar.append(namn(box((cx - 10, y - 2.5, BUK), (cx + 10, y + 2.5, BUK + 2)), e, (.95, .95, .8)))
    export_step(Compound(label="Sidotorn_v2", children=delar), str(a.ut / "sidotorn_v2.step"))
    print("klar")


if __name__ == "__main__":
    main()
