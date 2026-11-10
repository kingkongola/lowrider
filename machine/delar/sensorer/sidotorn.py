"""Sidotorn för sensorenheten på LowRider V4 Core, utkast (ej printat, ej verifierat).

All geometri i fräsramen M, millimeter: x bort från balken, y längs balken
(+y är maskinens X max-sida), z upp, fräsaxeln i x=y=0.

Kraven kommer från användaren 2026-11-09: bilderna sys ihop, så servo och dammsko
får synas och maskas bort; servot står kvar; kameran rakt ned, linsen 130 mm;
två preliminära kamera-LED-spår (inte valt huvudljus). D022 väljer i stället
BRIMETI 24 V COB på horisontell understrut. Dessa spår är endast reserv om
bildprov senare visar behov; inget köp eller inkoppling beslutad för dem.

Torn och arm skiljer ansvar: armens två hårda stopp bestämmer lägena, servot
bara driver rörelsen. Parkerat hålls armen av en magnet mot stoppet även utan
servokraft; kameran bekräftar läget före varje jobb (D020), inga brytare.

Kör: python sidotorn.py --ut KATALOG
"""
from __future__ import annotations

import argparse
import copy
import json
import math
from pathlib import Path

from build123d import (Box, Circle, Color, Compound, Cylinder, Face, Line, Plane, Polygon, Pos, Rot, Spline,
                       ThreePointArc, Vector, Wire, export_step, export_stl, extrude, fillet, sweep, Axis)

# Tornets gränser: inte förbi Core-änden längs balken, inte förbi dammskon utåt.
Y0, Y1 = 48.5, 72.5
X_DAMMSKO = 107.6

# Kamera: linsens spets. Långsidan (66 grader) ut från balken.
LINS = (93.0, 53.0, 130.0)
# Camera Module 3 Standard, mått ur Raspberry Pi:s STEP RP-008154 och ritning RP-008153.
# Linsen sitter inte mitt på kortet: 14,4 mm till kanten bort från kontakten, 9,46 mm till kontaktkanten.
KORT_B, KORT_D = 25.0, 23.862
KORT_Y = (LINS[1] - 14.4, LINS[1] + 9.462)   # kontaktkanten vänd mot X max-sidan
KORT_HAL = [(LINS[0] + dx, KORT_Y[0] + dy) for dx in (-10.5, 10.5) for dy in (2.0, 14.5)]
# Korthålen är Ø2,2: M3 går inte igenom. Tappar i hålen ger läget, två M3 x 10 strax utanför kortet klämmer kanten med huvudet.
KLAMMOR = [(LINS[0] - 10.6, KORT_Y[0] - 1.9), (LINS[0] + 10.4, KORT_Y[1] + 1.9)]
LED_X = ((LINS[0] - 7.6, LINS[0] + 10.0), (LINS[0] - 10.0, LINS[0] + 7.9))   # listerna kortade där skruvhuvudena sitter
KORT_FRAM = LINS[2] + 6.91  # kortets framsida; linsens spets sitter 6,91 mm framför den
KORT_BAK = KORT_FRAM + 0.75
KONTAKT_TOPP = KORT_BAK + 2.6    # flatkontakten på kortets baksida
KORT_TAK = KONTAKT_TOPP + 0.35   # kamerafickans tak
FFC_B = 16.0                # flatkabelns bredd i kameraänden (15-polig, 1 mm delning)
LED_Y = (LINS[1] - 17.5, LINS[1] + 15.5)     # kortet sticker längre åt fräsen, därför 2 mm från symmetri
HUD = 0.6                   # plast mellan magneten och M3-huvudet, så att stålet aldrig slår på magneten
BUK = LINS[2] + 2.6         # tornets plana undersida vid kameran
TOPP = 171.0                # tornets ovansida; bestäms av Pi-kortet som måste gå fritt över den svepande undersidan
XEND = 107.5               # tornets yttersta punkt, innanför dammskon

# Pi Zero 2 WH: kortet i XZ-planet, komponenterna mot locket.
PI_RUM = (12.0, 78.2)                    # x0, x1
PI_Y = 55.0                              # kortets undersida
PI_CENTER = (45.0, 151.0)
PI_HAL = [(PI_CENTER[0] + dx, PI_CENTER[1] + dz) for dx in (-29, 29) for dz in (-11.5, 11.5)]
PANEL_X = 82.5                           # sidopanelens bakre gräns mot kamerablocket
PANEL_HAL = [(15.0, 125.5), (70.0, 134.4), (23.0, 164.5), (67.0, 164.5), (15.0, 62.5), (45.5, 62.5)]
ACC_HAL = [(18.0, 118.5), (33.0, 118.5)]   # nominellt, kontrolleras mot levererad ADXL345
# Två LM2596-moduler 43 x 21 mm sida vid sida: A 5,1 V till Pi och BLTouch, B 6,0 V bara till servot (SPMS664 är specat 6,0-7,4 V).
REG_X0 = {"A": 12.5, "B": 34.5}
REG_Z0 = 66.5
REG_FINGER = [(x0 + dx, REG_Z0 + dz) for x0 in REG_X0.values() for dx, dz in ((3.0, 3.5), (18.0, 39.5))]   # panelens fingrar pressar modulens hörn

# Servo (SPMS664, befintligt läge) och arm.
PX, PZ = 45.0, 43.6
PARK = -150.0               # utfällt 0, parkerat mot magnet och hårt stopp (D020)
SERVO_DY = -2.0             # hela servopaketet flyttat längs balken så att kåpans vägg ryms före Core-änden
ARM_Y = (21.5 + SERVO_DY, 25.5 + SERVO_DY)
BLT = (61.0, 34.0 + SERVO_DY)
FRAM_Y = (43.3 + SERVO_DY, 49.3 + SERVO_DY)
FLANS_Z = 6.4
HUB_D = 15.0
MAGNET = (6.2, 3.2)         # urtag för Ø6 x 3 mm neodymmagnet (Vinabo, finns hemma) i parkeringsstoppet
BULA_T = 11.0               # armens bula för M3-skruvens stålhuvud, mm längs armen
ARM_W = (7.5, 5.0)         # halv bredd vid navet och vid plattan

BULA_Y = (ARM_Y[0] - 2.0, ARM_Y[1])   # armen är tjockare där M3-skruvens huvud möter magneten
KAPA_Y = Y1
KAPA_T = 1.4

# Hårda stopp: armens två sidor slår mot var sitt fast block på 7-15 mm radie.
STOPP_T = (7.0, 15.0)       # längs armen från navet
STOPP_TJOCK = 4.0


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


def V(x, z):
    return Vector(x, Y0, z)


def undersida():
    """Svepet från servokåpan upp till kamerans plana buk."""
    return Spline([V(44, 56), V(86, BUK)], tangents=[V(1, 0) - V(0, 0), V(1, 0) - V(0, 0)])


def silhuett():
    """Tornets sida som en sammanhängande kurva, utan raka facetter mot framkanten."""
    b, top = BUK, TOPP
    nos = Spline([V(103, b), V(107.5, b + 6)], tangents=[Vector(1, 0, 0), Vector(0, 0, 1)])
    rygg = Spline([V(107.5, b + 6), V(105.5, 150), V(96, 163.5), V(70, top)],
                  tangents=[Vector(0, 0, 1), Vector(-1, 0, 0)])
    return Wire.combine([Line(V(8, 56), V(44, 56)), undersida(), Line(V(86, b), V(103, b)), nos, rygg,
                         Line(V(70, top), V(8, top)), Line(V(8, top), V(8, 56))])[0]


def sidoprofil():
    """Tornets sida bakom panelen, följer svepet på undersidan."""
    u = undersida()
    pts = [u.position_at(t) for t in [i / 48 for i in range(49)]]
    kurva = [(p.X, p.Z) for p in pts if p.X < PANEL_X]
    p0, p1 = next(((pts[i], pts[i + 1]) for i in range(48) if pts[i].X < PANEL_X <= pts[i + 1].X))
    z = p0.Z + (p1.Z - p0.Z) * (PANEL_X - p0.X) / (p1.X - p0.X)
    return [(8, 56)] + kurva + [(PANEL_X, z), (PANEL_X, TOPP), (8, TOPP)]


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


def magnet_lage(blt_x):
    """Punkten där M3-huvudet möter huden, och riktningen in i stoppet."""
    u, n, L = arm_geo(blt_x)
    w = ARM_W[0] + (ARM_W[1] - ARM_W[0]) * BULA_T / L
    x, z = vrid((PX + u[0] * BULA_T + n[0] * w, PZ + u[1] * BULA_T + n[1] * w), PARK)
    vinkel = math.degrees(math.atan2(n[1], n[0])) - PARK    # sidnormalen efter parkering
    return x, z, vinkel


def magnet_urtag(blt_x):
    """Ø6 magnet i parkeringsstoppet. Hålet tas bakifrån till en tunn hud mot armen."""
    x, z, vinkel = magnet_lage(blt_x)
    ut = (math.cos(math.radians(vinkel)), math.sin(math.radians(vinkel)))
    langd = STOPP_TJOCK + 2.0 - HUD
    mitt = (x + ut[0] * (HUD + langd / 2), z + ut[1] * (HUD + langd / 2))
    return Pos(mitt[0], sum(BULA_Y) / 2, mitt[1]) * Rot(0, 90 - vinkel, 0) * Cylinder(MAGNET[0] / 2, langd)


def servokapa():
    """Yttre form runt servots bakdel; samma hörnradie som tornet."""
    k = box((12.6, FRAM_Y[0] + 1, 29.6), (57.4, KAPA_Y, 70.0))
    k = fillet(k.edges().filter_by(Axis.Y), 6.0)
    return fillet(k.faces().sort_by(Axis.Y)[-1].edges(), 1.2)


KABEL_VAG = [(7.0, 61.0, 113.0), (-2.0, 61.0, 128.0), (-3.0, 61.0, 165.0), (-8.0, 61.0, 205.0)]
KABEL_D = 6.0               # samlad kabel, se tabellen i README


def kabel():
    """Samlad kabel från tornets baksida, upp i gapet mot Core."""
    bana = Spline([Vector(*p) for p in KABEL_VAG])
    return sweep(Plane(origin=bana @ 0, z_dir=bana % 0) * Circle(KABEL_D / 2), bana)


def servo_attrapp():
    d = SERVO_DY
    kropp = box((14.8, 32.6 + d, 33.6), (55.2, 73 + d, 53.6))
    oron = box((5.1, 40.8 + d, 33.6), (64.9, 43.3 + d, 53.6))
    return kropp + oron + cyl_y(PX, PZ, 26.6 + d, 33.0 + d, 6.0)


def torn(blt_x=BLT[0]):
    b = BUK
    s = extrude(Face(silhuett()), amount=Y1 - Y0, dir=(0, 1, 0))
    s = fillet(s.edges().filter_by(Axis.Y).filter_by(lambda e: e.center().X < 9), 7.0)
    s = fillet(s.faces().sort_by(Axis.Y)[0].edges(), 5.0)
    s = fillet(s.faces().sort_by(Axis.Y)[-1].edges(), 1.2)
    # Fästplatta mot verktygsfästet, samma två M5-lägen som V1E-skruvarna.
    s += fillet(box((1, 39, 56), (9, Y0 + 1, 134)).edges().filter_by(Axis.Z), 1.5)
    s += fillet(box((1, Y0, 56), (14, 53, 134)).edges().filter_by(Axis.Z), 1.5)      # bär över lasten från fästplattan in i tornet
    for z in (64.25, 125.25):
        s += cyl_x(43.95, z, -7.3, 1.2, 9.6)
        s -= cyl_x(43.95, z, -9, 10, 5.4)
    # Servoram med fönster för kroppen, och skena upp till fästplattan.
    xa, xb = 7.0, 67.0      # fästöronen sitter vid x 11,7 och 59
    ram = box((xa, FRAM_Y[0], 27.6), (xb, FRAM_Y[1], 58.5))
    ram = fillet(ram.edges().filter_by(Axis.Y), 9.0)
    s += fillet(ram.faces().sort_by(Axis.Y)[0].edges(), 2.0)
    # Kåpa runt servots bakre del, i samma plan som sidopanelen.
    s += servokapa()
    s -= box((PX - 30.2, FRAM_Y[0] - 1, 33.4), (PX + 10.2, FRAM_Y[1] + 2, 53.8))
    s -= box((PX - 30.4, FRAM_Y[1], 33.2), (PX + 10.4, KAPA_Y - KAPA_T, 54.0))
    s += box((8, FRAM_Y[0], 53.8), (xb - 3, 52, 58.5))
    for x in (PX - 33.3, PX + 14):
        for z in (PZ - 4.7, PZ + 4.7):
            s -= cyl_y(x, z, FRAM_Y[0] - 1, FRAM_Y[1] + 1, 3.4)
    # Hårda stopp i armens plan, hållna av skenor över och under servot.
    def stopp(sida):
        y = (ARM_Y[0] if sida < 0 else BULA_Y[0] - 0.5, ARM_Y[1] + 1.2)
        p = prisma_y(stopp_block(blt_x, sida, ARM_W[0], ARM_W[1]), y[0], y[1])
        return fillet(p.edges().filter_by(Axis.Y), 0.8)
    s += stopp(-1)
    s += fillet(box((33, ARM_Y[1] + 1.0, 27.6), (45, FRAM_Y[0] + .2, 33.2)).edges().filter_by(Axis.Y), 1.2)
    s += stopp(1)
    s += fillet(box((31, ARM_Y[1] + 1.0, 54.0), (47, FRAM_Y[0] + .2, 58.5)).edges().filter_by(Axis.Y), 1.2)
    s += box((33.5, ARM_Y[0] + 2.0, 54.0), (37.0, ARM_Y[1] + 1.2, 58.5))   # förstärker parkeringsstoppet mot skenan
    s -= magnet_urtag(blt_x)
    # Kameran: nos under buken, urtag för kortet, två LED-spår symmetriskt runt linsen.
    cx, cy, _ = LINS
    # Nosen stiger mjukt upp i tornets framsida i stället för att vara en kloss.
    prof = Plane.YZ.offset(cx - 15.5) * Polygon((30, b), (Y0 + 1, b), (Y0 + 1, b + 22), (30, b + 14), align=None)
    nos = extrude(prof, amount=XEND - (cx - 15.5), dir=(1, 0, 0))
    nos = fillet(nos.edges().filter_by(Axis.X), 3.5)
    s += fillet(nos.faces().sort_by(Axis.X)[-1].edges(), 2.5)
    # Nosens ände går hela vägen till sidan, så att fickan för kamerakortet har en vägg runt om.
    kant = box((100, Y0, b), (XEND, Y1, b + 9))
    s += fillet(kant.faces().sort_by(Axis.X)[-1].edges(), 2.5)
    # Ficka öppen nedåt; kortet skruvas mot fyra distanser från linssidan, kontakten ryms under taket.
    s -= box((cx - KORT_B / 2 - .1, KORT_Y[0] - .1, b - 1), (cx + KORT_B / 2 + .1, KORT_Y[1] + .1, KORT_TAK))
    for x, y in KORT_HAL:
        s += Pos(x, y, (KORT_BAK + KORT_TAK + .5) / 2) * Cylinder(2.2, KORT_TAK + .5 - KORT_BAK)
        s += Pos(x, y, KORT_BAK - .8) * Cylinder(1.0, 1.7)      # tappen i kortets Ø2,2-hål
    for x, y in KLAMMOR:
        s -= Pos(x, y, (b - 1 + KORT_FRAM + .2) / 2) * Cylinder(2.85, KORT_FRAM + .2 - b + 1)   # plats för M3-huvudet
        s -= Pos(x, y, KORT_FRAM + 5.35) * Cylinder(1.3, 10.7)
    for y, (x0, x1) in zip(LED_Y, LED_X):
        s -= box((x0, y - 2.5, b - 1), (x1, y + 2.5, b + 2))
        s -= Pos(cx - 6.5, y, b + 6) * Cylinder(1.5, 12) if y < cy else Pos(cx - 6.5, y, b + 3) * Cylinder(1.5, 6)
    s = med_elektronik(s)
    return s


def med_elektronik(s):
    """Elektronikrum bakom en enda sidopanel, och alla kablar dolda inuti tornet."""
    b = BUK
    x0, x1 = PI_RUM
    s -= prisma_y(inset(sidoprofil(), 4.0), 51, Y1 - 1.9)
    s -= prisma_y(inset(sidoprofil(), 2.0), Y1 - 2, Y1 + 1)
    # Tvärribba som styvar väggarna; fönster för kablar.
    s += box((48, 50.5, 110.5), (51, Y1 - 2.1, 135))
    # Pi (hålbild 58 x 23) och accelerometer på tornets innervägg.
    # Pi:n ligger på fyra pelare med tappar i hålen (Ø2,75) och hålls på plats av panelens fingrar.
    for x, z in PI_HAL:
        s += cyl_y(x, z, 50.5, PI_Y, 6.0)
        s += cyl_y(x, z, PI_Y - .5, PI_Y + 1.9, 2.4)
    # ADXL345 mäter fräsningens vibrationer: den sitter på en massiv platta som går direkt in i fästblocket vid övre M5.
    s += box((12, 50.5, 111), (38, 53.5, 126))
    for x, z in ACC_HAL:
        s += cyl_y(x, z, 50.5, PI_Y, 6.0)
        s -= cyl_y(x, z, 49.9, PI_Y + 1, 2.6)
    # LM2596: läget ges av modulens ytterkant, så hålbilden spelar ingen roll. Panelens fingrar håller den.
    for x0 in REG_X0.values():
        s += box((x0 - 1.2, 50.5, REG_Z0 - 1.2), (x0 + 22.2, PI_Y + 2.0, REG_Z0 + 44.2))
    for x0 in REG_X0.values():
        s -= box((x0 - .15, PI_Y, REG_Z0 - .15), (x0 + 21.15, PI_Y + 3, REG_Z0 + 43.15))
        s -= box((x0 + .5, 51.0, REG_Z0 + .5), (x0 + 20.5, PI_Y + .5, REG_Z0 + 42.5))
    for x0 in REG_X0.values():
        for dx, dz in ((0, 0), (18, 0), (0, 40), (18, 40)):
            s += box((x0 + dx, 50.5, REG_Z0 + dz), (x0 + dx + 3, PI_Y, REG_Z0 + dz + 3))
    for x, z in PANEL_HAL[:4]:
        s += cyl_y(x, z, 64.5, Y1 - 2, 7.0)
    for x, z in PANEL_HAL[4:]:
        s += cyl_y(x, z, 50.5, Y1 - 2, 7.0)
    for x, z in PANEL_HAL:
        s -= cyl_y(x, z, 62.0, Y1 - 1.5, 2.5)
    # CSI-rummet: flatkabeln lämnar kamerakortets kontakt, reser sig och viks två gånger 45 grader mot Pi:ns kortsida.
    rum = [(x1 - .5, b + 3.5), (LINS[0] + 8.6, b + 3.5), (LINS[0] + 8.6, 149.5), (LINS[0] - 2.0, 160.5), (x1 - .5, 160.5)]
    s -= prisma_y(rum, 60.5, 68.5)
    s -= prisma_y([(83.0, b + 3.5), *rum[1:4], (83.0, 160.5)], 68.4, 70.0)        # mot panelens anläggning lämnas mer gods
    s -= box((x1 - 0.5, 54.5, KORT_TAK + 1.5), (LINS[0] - 8.5, 60.6, 160.5))  # fram till Pi-kortets kontakt
    # LED-ledningen från den främre listen går över kamerafickans tak in i CSI-rummet.
    s -= box((LINS[0] - 7.5, LED_Y[0] - 1.0, KORT_TAK + 1.2), (LINS[0] - 5.5, 62.5, KORT_TAK + 3.0))
    # Servokabeln upp ovanför servot; BLTouch-kabeln genom skenan över servot.
    s -= box((25, 52, 53.5), (43, 62, 61))
    s -= box((37, ARM_Y[1] + 0.5, 55), (43, 52.5, 57.5))
    # Samlad kabel ut bakåt, in i gapet mot Core där den inte syns framifrån.
    s -= box((7, 56, 108), (13, 66, 118))
    for y in (60, 65):                                      # buntbandsbryggor strax ovanför utgången, utanför ADXL-kortet
        s += box((11, y, 118.5), (20, y + 2, 121.5))
    return s


def sidopanel():
    """Tornets hela sida som en enda panel, plan mot X max-sidan."""
    p = prisma_y(inset(sidoprofil(), 2.15), Y1 - 2, Y1)
    for x, z in PANEL_HAL:
        p -= cyl_y(x, z, Y1 - 3, Y1 + 1, 3.4)
        p -= cyl_y(x, z, Y1 - 1, Y1 + 1, 6.2)
    # Fingrar som pressar korten mot sina anlägg när panelen skruvas på.
    for x, z in PI_HAL:
        p += cyl_y(x, z, PI_Y + 1.45, Y1 - 1.9, 5.0) - cyl_y(x, z, PI_Y + 1.0, PI_Y + 2.6, 3.2)
    for x, z in REG_FINGER:
        p += cyl_y(x, z, PI_Y + 1.65, Y1 - 1.9, 5.0)
    for z in (139, 144, 149, 154, 159, 164):
        p -= box((28, Y1 - 3, z - 0.9), (62, Y1 + 1, z + 0.9))
    for z in (78, 83, 88, 93, 98):                           # luft in vid regulatorerna, ut vid Pi:n
        p -= box((15, Y1 - 3, z - 0.9), (53, Y1 + 1, z + 0.9))
    return p


def bricka():
    """Distansbricka under M3-huvudet på ADXL-kortet, så att M3 x 10 inte når tornets framvägg. Två stycken."""
    return Cylinder(3.5, 3.5) - Cylinder(1.7, 4.0)


def arm(blt_x=BLT[0]):
    """Svepande arm: navets rundning går över i en fot som bär BLTouchen."""
    y0, y1 = ARM_Y
    w0, w1 = ARM_W
    u, n, L = arm_geo(blt_x)
    bx, bz = blt_x, FLANS_Z + 3
    F = FLANS_Z
    def sid(t, s):
        w = w0 + (w1 - w0) * t / L
        return (PX + u[0] * t + s * n[0] * w, PZ + u[1] * t + s * n[1] * w)
    rygg = (PX - u[0] * w0, PZ - u[1] * w0)
    fot_h, fot_v = (blt_x + 11, F), (blt_x - 11, F)
    def v(p):
        return Vector(p[0], y0, p[1])
    h1, v1 = sid(19, 1), sid(19, -1)
    tr = lambda a, b: Vector(b[0] - a[0], 0, b[1] - a[1]).normalized()
    h_sp = Spline([v(h1), v(((h1[0] + fot_h[0]) / 2 + 1.5, (h1[1] + fot_h[1]) / 2 - 1.0)), v(fot_h)],
                  tangents=[tr(sid(10, 1), h1), Vector(1, 0, -.15).normalized()])
    v_sp = Spline([v(fot_v), v(((v1[0] + fot_v[0]) / 2 - 1.0, (v1[1] + fot_v[1]) / 2 - 1.0)), v(v1)],
                  tangents=[Vector(1, 0, .15).normalized(), tr(v1, sid(10, -1))])
    trad = Wire.combine([ThreePointArc(v(sid(0, -1)), v(rygg), v(sid(0, 1))), Line(v(sid(0, 1)), v(h1)), h_sp,
                         Line(v(fot_h), v(fot_v)), v_sp, Line(v(v1), v(sid(0, -1)))])[0]
    a = extrude(Face(trad), amount=y1 - y0, dir=(0, 1, 0))
    a = fillet(a.edges().filter_by(lambda e: abs(e.center().Z - F) > .01), 1.4)
    # Foten: mjuk platta som BLTouchen skruvas under.
    fot = box((blt_x - 13, y0, F), (blt_x + 13, BLT[1] + 6, F + 4.5))
    fot = fillet(fot.edges().filter_by(Axis.Z), 5.0)
    fot = fillet(fot.faces().sort_by(Axis.Z)[-1].edges(), 1.6)
    a += fot
    # Bula för skruvhuvudet som fäster mot magneten.
    t = BULA_T
    w = w0 + (w1 - w0) * t / L
    bula = Pos(PX + u[0] * t + n[0] * (w - 3.5), sum(BULA_Y) / 2, PZ + u[1] * t + n[1] * (w - 3.5)) * Rot(0, 90 - math.degrees(math.atan2(n[1], n[0])), 0) * Cylinder(3.0, 7.0)
    a += bula
    s_p = (PX + u[0] * t + n[0] * w, PZ + u[1] * t + n[1] * w)
    rot = Rot(0, 90 - math.degrees(math.atan2(n[1], n[0])), 0)
    a -= Pos(s_p[0] - n[0] * 1.65, sum(BULA_Y) / 2, s_p[1] - n[1] * 1.65) * rot * Cylinder(2.95, 3.3)   # M3-huvud, skruvdjupet ställer hållkraften
    a -= Pos(s_p[0] - n[0] * 7, sum(BULA_Y) / 2, s_p[1] - n[1] * 7) * rot * Cylinder(1.3, 9)
    # Dolt spår för BLTouch-kabeln, på armens sida mot servot.
    a -= prisma_y([sid_p for sid_p in ((PX + u[0] * 18 + n[0] * 1.75, PZ + u[1] * 18 + n[1] * 1.75),
                   (bx + n[0] * 1.75, bz + n[1] * 1.75), (bx - n[0] * 1.75, bz - n[1] * 1.75),
                   (PX + u[0] * 18 - n[0] * 1.75, PZ + u[1] * 18 - n[1] * 1.75))], y1 - 2, y1 + .1)
    a -= box((blt_x - 1.75, y1 - .5, F + 3), (blt_x + 1.75, BLT[1] - 4.5, F + 5))
    for x in (blt_x - 9, blt_x + 9):
        a -= Pos(x, BLT[1], F + 2) * Cylinder(1.3, 10)     # M3 x 10 gängar direkt i foten, genom hylsans och BLTouchens öron
    a -= Pos(blt_x, BLT[1], F + 2) * Cylinder(5, 10)
    a -= cyl_y(PX, PZ, y0 - 1, y1 + 1, 7.5)
    return a


def bltouch(blt_x=BLT[0]):
    x, y, f = blt_x, BLT[1], FLANS_Z
    return box((x - 13, y - 5.75, f - 2.5), (x + 13, y + 5.75, f)) + box(
        (x - 6.5, y - 6.5, f - 36.3), (x + 6.5, y + 6.5, f - 2.5)) + (Pos(x, y, f - 41) * Cylinder(1, 9.4))


def bltouch_kapa(blt_x=BLT[0]):
    """Tunn hylsa runt BLTouchens kropp. Följer med armen, skyddar kroppen i alla lägen och ändrar inte mätläget."""
    x, y, f = blt_x, BLT[1], FLANS_Z
    t = f - 2.5                     # BLTouchens fläns underkant: hylsans öron ligger an här
    b = f - 36.8                    # 0,5 mm under kroppen, stiftet går fritt genom den öppna änden
    k = fillet(box((x - 8.5, y - 8.5, b), (x + 8.5, y + 8.5, t)).edges().filter_by(Axis.Z), 4.0)
    k = fillet(k.faces().sort_by(Axis.Z)[0].edges(), 1.0)
    oron = fillet(box((x - 14.5, y - 6.5, t - 2.0), (x + 14.5, y + 6.5, t)).edges().filter_by(Axis.Z), 4.0)
    k += fillet(oron.faces().sort_by(Axis.Z)[0].edges(), 0.8)
    k -= box((x - 6.9, y - 6.9, b - 1), (x + 6.9, y + 6.9, t + 1))
    for hx in (x - 9, x + 9):
        k -= Pos(hx, y, t - 1) * Cylinder(1.7, 4)
    return k


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
    for n, o in (("torn", t), ("arm", ar), ("bltouch", bl), ("sidopanel", l), ("kabel", kabel()), ("bricka", bricka()), ("kapa", bltouch_kapa())):
        print(n, "giltig", o.is_valid, "solider", len(o.solids()), "volym cm3", round(o.volume / 1000, 1),
              "bbox", [round(v, 1) for v in (*o.bounding_box().min, *o.bounding_box().max)])
        export_stl(o, str(a.ut / f"{n}.stl"), tolerance=.05, angular_tolerance=.2)
    cx, cy, cz = LINS
    delar = [
        namn(t, "Sidotorn", (.16, .18, .2)),
        namn(servo_attrapp(), "Servo_SPMS664_ATTRAPP", (.1, .1, .12)),
        namn(kabel(), "Kabel_ATTRAPP", (.1, .1, .1)),
        namn(ar, "Arm_utfalld", (.9, .62, .29)),
        namn(bl, "BLTouch_utfalld_ATTRAPP", (.85, .2, .15)),
        namn(parkera(copy.deepcopy(ar)), "Arm_parkerad", (.9, .62, .29)),
        namn(parkera(copy.deepcopy(bl)), "BLTouch_parkerad_ATTRAPP", (.85, .2, .15)),
        namn(bltouch_kapa(), "BLTouch_hylsa_utfalld", (.9, .62, .29)),
        namn(parkera(bltouch_kapa()), "BLTouch_hylsa_parkerad", (.9, .62, .29)),
        namn(box((cx - KORT_B / 2, KORT_Y[0], KORT_FRAM), (cx + KORT_B / 2, KORT_Y[1], KORT_BAK)), "Kamerakort_ATTRAPP", (.1, .45, .2)),
        namn(box((cx - 11.45, KORT_Y[1] - 6.9, KORT_BAK), (cx + 11.45, KORT_Y[1] - .4, KONTAKT_TOPP)), "Flatkontakt_ATTRAPP", (.85, .8, .6)),
        namn(Pos(cx, cy, cz + 3.45) * Cylinder(4.25, 6.9), "Lins_ATTRAPP", (.05, .05, .05)),
        namn(box((PI_CENTER[0] - 32.5, PI_Y, PI_CENTER[1] - 15), (PI_CENTER[0] + 32.5, PI_Y + 1.4, PI_CENTER[1] + 15)), "Pi_Zero_2_ATTRAPP", (.15, .55, .3)),
        namn(l, "Sidopanel", (.16, .18, .2)),
        *[namn(box((x0, PI_Y, REG_Z0), (x0 + 21, PI_Y + 14, REG_Z0 + 43)), f"LM2596_{k}_ATTRAPP", (.1, .25, .6)) for k, x0 in REG_X0.items()],
    ]
    for y, e in ((LED_Y[0], "LED_1_ATTRAPP"), (LED_Y[1], "LED_2_ATTRAPP")):
        x0, x1 = LED_X[0 if y < cy else 1]
        delar.append(namn(box((x0, y - 2.5, BUK), (x1, y + 2.5, BUK + 2)), e, (.95, .95, .8)))
    export_step(Compound(label="Sidotorn_v2", children=delar), str(a.ut / "sidotorn_v2.step"))
    # Komponenternas lägen till granskningen, så att den alltid kontrollerar det som faktiskt ritats.
    (a.ut / "elektronik.json").write_text(json.dumps({
        "Pi": [[PI_CENTER[0] - 32.5, PI_Y, PI_CENTER[1] - 15], [PI_CENTER[0] + 32.5, PI_Y + 1.4, PI_CENTER[1] + 15]],
        **{f"LM2596_{k}": [[x0, PI_Y, REG_Z0], [x0 + 21, PI_Y + 14, REG_Z0 + 43]] for k, x0 in REG_X0.items()},
        "ADXL": [[ACC_HAL[0][0] - 2.5, PI_Y, ACC_HAL[0][1] - 7.8], [ACC_HAL[1][0] + 2.5, PI_Y + 3, ACC_HAL[0][1] + 7.8]],
        "Kort": [[cx - KORT_B / 2, KORT_Y[0], KORT_FRAM], [cx + KORT_B / 2, KORT_Y[1], KORT_BAK]],
        "Flatkontakt": [[cx - 11.45, KORT_Y[1] - 6.9, KORT_BAK], [cx + 11.45, KORT_Y[1] - .4, KONTAKT_TOPP]],
        "magnet": [*magnet_lage(BLT[0]), sum(BULA_Y) / 2], "kort_hal": KORT_HAL, "kort_bak": KORT_BAK, "kort_fram": KORT_FRAM, "klammor": KLAMMOR, "ffc_b": FFC_B, "lins": LINS,
        "pi_hal": PI_HAL, "panel_hal": PANEL_HAL, "topp": TOPP}))
    print("klar")


if __name__ == "__main__":
    main()
