"""Sidotorn för sensorenheten på LowRider V4 Core, utkast (ej printat, ej verifierat).

All geometri i fräsramen M, millimeter: x bort från balken, y längs balken
(+y är maskinens X max-sida), z upp, fräsaxeln i x=y=0.

Kraven kommer från användaren 2026-11-09: bilderna sys ihop, så servo och dammsko
får synas och maskas bort; servot står kvar; kameran rakt ned, linsen 130 mm;
egen belysning krävs i det mörka garaget (förtydligat 2026-11-10). D022 väljer
BRIMETI 24 V COB på horisontell understrut som huvudljus. De gamla LED-urtagen
är provisoriska kabelvägar. Lampdockan ligger kvar som reserv; G4-bäraren har
utgått ur printplanen.

Torn och arm skiljer ansvar: armens två hårda stopp bestämmer lägena, servot
bara driver rörelsen. Parkerat hålls armen av en magnet mot stoppet även utan
servokraft; kameran bekräftar läget före varje jobb (D020), inga brytare.

Kör: python sidotorn.py --ut KATALOG
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math

import crtouch as cr
import lampor
import hornfaste as hf
from pathlib import Path

from build123d import (Box, Circle, Color, Compound, Cylinder, Face, Line, Plane, Polygon, Pos, Rot, Spline,
                       ThreePointArc, Vector, Wire, export_step, export_stl, extrude, fillet, sweep, Axis, RectangleRounded, loft)

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
HUD = 0.6                   # skyddsplast framför magneten
BUK = LINS[2] + 2.6         # tornets plana undersida vid kameran
TOPP = 171.0                # tornets ovansida; bestäms av Pi-kortet som måste gå fritt över den svepande undersidan
XEND = 107.5               # tornets yttersta punkt, innanför dammskon

# Pi Zero 2 WH: kortet i XZ-planet, komponenterna mot locket.
PI_RUM = (12.0, 78.2)                    # x0, x1
PI_Y = 55.0                              # kortets undersida
PI_CENTER = (45.0, 151.0)
PI_HAL = [(PI_CENTER[0] + dx, PI_CENTER[1] + dz) for dx in (-29, 29) for dz in (-11.5, 11.5)]
# microSD sitter på komponentsidan vid kortsidan mitt emot kamerakontakten, alltså mot bakväggen,
# 6,9-18,9 mm från stiftlistans kant (Raspberry Pi Zero 2 W mechanical drawing). Kortet sticker ut
# ca 2,5 mm. En springa genom bakväggen: Pi:n sätts in utan kort, kortet skjuts in utifrån.
SD_Z = (PI_CENTER[1] - 15 + 6.9, PI_CENTER[1] - 15 + 18.9)
SD_SPRINGA = (PI_Y + 1.0, PI_Y + 3.4)        # y: kortet ligger 0-1,5 mm över kretskortet
# Pi:ns 40-poliga stiftlist (WH = fabrikslödd). Kamerakontakten vänd mot kameran (+x) och komponenterna mot
# panelen ger stiftlisten längs kortets nedre långsida, i hålens linje 3,5 mm från kanten, stift 1 mot -x.
# Härlett ur Pi Zeros layout, kontrolleras mot levererat kort. Stiftens topp 8,5 mm över kortet (vanlig list).
STIFT_Z_YTTRE, STIFT_Z_INRE = PI_CENTER[1] - 11.5 - 1.27, PI_CENTER[1] - 11.5 + 1.27   # jämna stift ytterst
STIFT_TOPP_Y = PI_Y + 1.4 + 8.5
LIST_TOPP_Y = PI_Y + 1.4 + 2.5                                   # listens plastkropp


def stift_lage(n):
    """x, z för stift n (1-40)."""
    kol = (n - 1) // 2
    return PI_CENTER[0] - 24.13 + kol * 2.54, STIFT_Z_YTTRE if n % 2 == 0 else STIFT_Z_INRE


PANEL_X = 82.5                           # sidopanelens bakre gräns mot kamerablocket
# Fyra panelskruvar i tornets pelare: två hängande (från y 64,5) och två hela. Pelarna står utanför
# Pi:ns väg in. (71,5, 132,2): lödplats åt stift 38 och fri väg för kortets hörn.
PANEL_HAL = [(15.0, 125.5), (71.5, 132.2), (15.0, 62.5), (45.5, 62.5)]
# Panelens två övre skruvar går genom panelens fingrar och Pi:ns övre hål in i Pi:ns distanser:
# M2.5 x 20, formar gänga i Ø2,1-hål. Sätet i fingret ger rätt djup, så skruven når aldrig framsidan.
PI_SKRUV = [(PI_CENTER[0] - 29, PI_CENTER[1] + 11.5), (PI_CENTER[0] + 29, PI_CENTER[1] + 11.5)]
PI_SKRUV_SATE = 69.3        # skallens anläggning i fingret
PI_SKRUV_L = 20.0
# Kopplingskort (hålkort ca 9 x 23 mm, VHB-tejp på framväggen): jordpunkt, servons kontakt och
# kondensator, CR Touch-kabelns skarvar. Ytan är fri enligt kontroll_montage.py.
KOPPLINGSKORT = ((38.6, 51.0, 111.5), (47.5, 55.5, 135.0))
ACC_HAL = [(18.0, 118.5), (33.0, 118.5)]   # nominellt, kontrolleras mot levererad ADXL345
# Två LM2596-moduler 43 x 21 mm: A till Pi/CR Touch, B till servo.
# Matningsval ägs av KOPPLING_CORE_V0.md; här modelleras modulernas utrymme.
REG_X0 = {"A": 12.5, "B": 34.5}
REG_Z0 = 66.5
# INMP441-mikrofon i sidopanelen: panelen är utbytbar och vänd bort från fräsen, så spån
# inte blåser rakt i ljudhålet. Modulen är nominellt 14 x 14 mm (vissa 14 x 12), mäts vid leverans.
# Ljudhålet sitter på kortets undersida (bottenport) och läggs mot panelens hål med en ring skumtejp som tätning.
MIK = (39.5, 121.0)          # x, z för ljudhålets mitt på panelen, mellan regulatorernas fingrar och Pi:n
MIK_RUTA = 14.6              # ramens innermått, rymmer 14 x 14 med spel
MIK_HAL_D = 1.5              # ljudhål genom panelen
MIK_NAT = (7.0, 0.4)         # utvändig försänkning för dammnät eller ventildekal: diameter, djup
REG_FINGER = [(x0 + dx, REG_Z0 + dz) for x0 in REG_X0.values() for dx, dz in ((3.0, 3.5), (18.0, 39.5))]   # panelens fingrar pressar modulens hörn

# Infästning mot maskinen: V1E:s två M5 genom verktygsfästets öron in i Core, ca 16 mm längre
# eftersom tornets distans och platta (x -7,3 till 9) hamnar mellan skallen och örat.
M5_Z = (64.25, 125.25)
M5_KANAL_D = 9.4            # M5 insex-skalle Ø8,5 och smal bricka DIN 433 Ø9
SERVO_PILOT = 2.6           # M3 formar egen gänga i PETG

# Stoppdelarnas skruvar: två per del, M3 x 20 genom skenan in i ramen (formar gänga i Ø2,6).
STOPP_SKRUV = [(35.2, 30.4), (39.8, 30.4), (43.0, 56.8), (50.0, 56.8)]   # övre förbi parkeringsstoppet
STOPP_PILOT_DJUP = 9.0

# Servo (SPMS664, befintligt läge) och arm.
PX, PZ = 45.0, 43.6
PARK = -150.0               # utfällt 0, parkerat mot magnet och hårt stopp (D020)
SERVO_DY = -2.0
SERVO_KRAGE = (12.0, 1.0)   # diameter, höjd över servots plana ovansida; uppmätt 2026-11-11             # hela servopaketet flyttat längs balken så att kåpans vägg ryms före Core-änden
ARM_Y = (21.5 + SERVO_DY, 25.5 + SERVO_DY)
PROB = (61.0, 34.0 + SERVO_DY)
FRAM_Y = (43.3 + SERVO_DY, 49.3 + SERVO_DY)
FLANS_Z = 6.4
HUB_D = 15.0
MAGNET = (6.2, 3.2)         # urtag för Ø6 x 3 mm neodymmagnet (Vinabo, finns hemma) i parkeringsstoppet
BULA_T = 11.0               # armens bula för M3-skruvens stålhuvud, mm längs armen
ARM_W = (7.5, 5.0)         # halv bredd vid navet och vid plattan

BULA_Y = (23.5,29.5)  # kontaktens stålskruv bakom hornets platta arm (H=10)
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


def arm_geo(prob_x):
    """Armens riktning u och sidnormal n, längden L."""
    bx, bz = prob_x, FLANS_Z + 3
    L = math.hypot(bx - PX, bz - PZ)
    ux, uz = (bx - PX) / L, (bz - PZ) / L
    return (ux, uz), (-uz, ux), L


def horn_lage(o, prob_x=PROB[0], spegla=True):
    """H mäts från servohusets ovansida vid axeln till hornets plana utsida."""
    u, _, _ = arm_geo(prob_x)
    horn_y = 32.6 + SERVO_DY - hf.H_MONTERAT
    # Bygeln placeras på armens andra sida för frigång mot undre verktygsfästet.
    return Pos(PX,horn_y,PZ) * Rot(0,math.degrees(math.atan2(-u[1],u[0])),0) * (o.mirror(Plane.XY) if spegla else o)


def magnet_skruv_attrapp(prob_x=PROB[0]):
    """M3x10-kuvert av stål, skallen i sitt 3,3 mm djupa säte; verklig längd provas."""
    _,_,L=arm_geo(prob_x)
    w=ARM_W[0]+(ARM_W[1]-ARM_W[0])*BULA_T/L
    y=sum(BULA_Y)/2-(32.6+SERVO_DY-hf.H_MONTERAT)
    s=Pos(BULA_T,y,w-1.8)*Cylinder(2.75,3)+Pos(BULA_T,y,w-8.3)*Cylinder(1.5,10)
    return horn_lage(s,prob_x,spegla=False)


def vrid(p, grader):
    """Samma vridning som parkera(), runt navet i XZ-planet."""
    g = math.radians(grader)
    dx, dz = p[0] - PX, p[1] - PZ
    return (PX + dx * math.cos(g) + dz * math.sin(g), PZ - dx * math.sin(g) + dz * math.cos(g))


def stopp_block(prob_x, sida, w0, w1):
    """Fyrhörning som ligger an mot armens sida; sida=-1 utfällt, +1 parkerat."""
    u, n, L = arm_geo(prob_x)
    def pkt(t, ut):
        w = w0 + (w1 - w0) * t / L + ut
        return (PX + u[0] * t + sida * n[0] * w, PZ + u[1] * t + sida * n[1] * w)
    pts = [pkt(STOPP_T[0], 0), pkt(STOPP_T[1], 0), pkt(STOPP_T[1], STOPP_TJOCK), pkt(STOPP_T[0], STOPP_TJOCK)]
    return [vrid(p, PARK) for p in pts] if sida > 0 else pts


def magnet_lage(prob_x):
    """Punkten där M3-huvudet möter huden, och riktningen in i stoppet."""
    u, n, L = arm_geo(prob_x)
    w = ARM_W[0] + (ARM_W[1] - ARM_W[0]) * BULA_T / L
    x, z = vrid((PX + u[0] * BULA_T + n[0] * w, PZ + u[1] * BULA_T + n[1] * w), PARK)
    vinkel = math.degrees(math.atan2(n[1], n[0])) - PARK    # sidnormalen efter parkering
    return x, z, vinkel


def magnet_urtag(prob_x):
    """Ø6 magnet i parkeringsstoppet. Hålet tas bakifrån till en tunn hud mot armen."""
    x, z, vinkel = magnet_lage(prob_x)
    ut = (math.cos(math.radians(vinkel)), math.sin(math.radians(vinkel)))
    langd = STOPP_TJOCK + 2.0 - HUD
    mitt = (x + ut[0] * (HUD + langd / 2), z + ut[1] * (HUD + langd / 2))
    return Pos(mitt[0], sum(BULA_Y) / 2, mitt[1]) * Rot(0, 90 - vinkel, 0) * Cylinder(MAGNET[0] / 2, langd)


def stoppdelar(prob_x=PROB[0]):
    """Hårda stopp i armens plan som två egna delar, skruvade mot ramens framsida.

    Varför egna delar: stoppen står framför servots framsida, så servot kan inte föras in genom
    ramen om de är printade i tornet (kontroll_montage.py steg 1b). Ett trasigt stopp printas om
    utan nytt torn och utan ny kamerakalibrering. Två M3 x 20 per del, skallen försänkt.
    """
    def stopp(sida):
        y = (ARM_Y[0], ARM_Y[1] + 1.2) if sida < 0 else (ARM_Y[1] - 2.5, BULA_Y[1] + .5)
        p = prisma_y(stopp_block(prob_x, sida, ARM_W[0], ARM_W[1]), y[0], y[1])
        return fillet(p.edges().filter_by(Axis.Y), 0.8)
    nedre = stopp(-1) + fillet(box((33, ARM_Y[1] + 1.0, 27.6), (42, FRAM_Y[0], 33.2)).edges().filter_by(Axis.Y), 1.2)
    ovre = stopp(1) + fillet(box((31, 30.5, 54.0), (54.5, FRAM_Y[0], 59.4)).edges().filter_by(Axis.Y), 1.2)   # under M5-kanalen
    ovre += box((33.5, ARM_Y[0] + 2.0, 54.0), (37.0, 33.0, 58.5))
    ovre -= magnet_urtag(prob_x)
    delar = []
    for d in (nedre, ovre):
        for x, z in STOPP_SKRUV:
            if d.bounding_box().min.Z - .1 <= z <= d.bounding_box().max.Z + .1 and d.bounding_box().min.X <= x <= d.bounding_box().max.X:
                d -= cyl_y(x, z, 20, FRAM_Y[0] + 1, 3.4)
                fram = d.bounding_box().min.Y if z < 40 else 30.5
                d -= cyl_y(x, z, fram - 1, fram + 3.5, 6.0)
        delar.append(d)
    return delar[0], delar[1]


def torn_monterat(prob_x=PROB[0]):
    """Tornet med stoppdelarna påskruvade: det läge armen och proben möter i drift."""
    nedre, ovre = stoppdelar(prob_x)
    return torn(prob_x) + nedre + ovre


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
    # Kragen runt axeln: Ø12, 1 mm över servots plana ovansida (uppmätt 2026-11-11).
    krage = cyl_y(PX, PZ, 32.6 + d - SERVO_KRAGE[1], 32.6 + d, SERVO_KRAGE[0])
    return kropp + oron + krage + cyl_y(PX, PZ, 26.6 + d, 33.0 + d, 6.0)


def torn(prob_x=PROB[0]):
    b = BUK
    s = extrude(Face(silhuett()), amount=Y1 - Y0, dir=(0, 1, 0))
    s = fillet(s.edges().filter_by(Axis.Y).filter_by(lambda e: e.center().X < 9), 7.0)
    s = fillet(s.faces().sort_by(Axis.Y)[0].edges(), 5.0)
    s = fillet(s.faces().sort_by(Axis.Y)[-1].edges(), 1.2)
    # Fästplatta mot verktygsfästet, samma två M5-lägen som V1E-skruvarna.
    s += fillet(box((1, 39, 56), (9, Y0 + 1, 134)).edges().filter_by(Axis.Z), 1.5)
    s += fillet(box((1, Y0, 56), (14, 53, 134)).edges().filter_by(Axis.Z), 1.5)      # bär över lasten från fästplattan in i tornet
    # Distansen Ø9,6 sitter i verktygsfästets försänkning för skallen (ca Ø10): formpassning håller
    # läget, så klämkraften kan hållas låg (0,6-0,8 Nm, se berakning_sidotorn.py) mot PETG-krypning.
    for z in M5_Z:
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
    # Servoskruvarna: M3 x 10 formar egen gänga i förborrat Ø2,6-hål (bakom ramen är det massivt,
    # så en mutter får inte plats). Blint hål 3 mm förbi ramen.
    for x in (PX - 33.3, PX + 14):
        for z in (PZ - 4.7, PZ + 4.7):
            s -= cyl_y(x, z, FRAM_Y[0] - 1, FRAM_Y[1] + 3, SERVO_PILOT)
    # Stoppdelarna skruvas mot ramens framsida efter att servot satts in (se stoppdelar()).
    for x, z in STOPP_SKRUV:
        s -= cyl_y(x, z, FRAM_Y[0] - .1, FRAM_Y[0] + STOPP_PILOT_DJUP, SERVO_PILOT)
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
    # Permanent docka för separat lampbärare; inga lampmått låses i kamerafästet.
    s += lampor.tornbossar()
    s -= lampor.tornhal()
    # Den nedre M5-skruvens skalle döljs av servokåpan: en rak kanal ovanför servot för skruven och
    # insexnyckeln, utifrån (+x). Skärs sist, så att inget senare fyller igen den.
    s -= cyl_x(43.95, M5_Z[0], 9.0, 130, M5_KANAL_D)
    return s


def med_elektronik(s):
    """Elektronikrum bakom en enda sidopanel, och alla kablar dolda inuti tornet."""
    b = BUK
    x0, x1 = PI_RUM
    s -= prisma_y(inset(sidoprofil(), 4.0), 51, Y1 - 1.9)
    s -= prisma_y(inset(sidoprofil(), 1.9), Y1 - 2, Y1 + 1)   # panelsätet: 0,25 mm spel mot panelen
    # Tvärribba som styvar väggarna; fönster för kablar.
    s += box((48, 50.5, 110.5), (51, Y1 - 2.1, 135))
    s -= box((47.5, 62.0, 129.0), (51.5, Y1 - 1.9, 135.5))   # kabelfönster: ledningar från stift 34-38 till mikrofonen
    # Pi (hålbild 58 x 23) och accelerometer på tornets innervägg.
    # Pi:n ligger på fyra pelare med tappar i hålen (Ø2,75) och hålls på plats av panelens fingrar.
    for x, z in PI_HAL:
        s += cyl_y(x, z, 50.5, PI_Y, 6.0)
        if (x, z) in PI_SKRUV:
            s -= cyl_y(x, z, PI_SKRUV_SATE - PI_SKRUV_L - .3, PI_Y + .1, 2.1)
        else:
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
    for x, z in PANEL_HAL[:2]:
        s += cyl_y(x, z, 64.5, Y1 - 2, 7.0)
    for x, z in PANEL_HAL[2:]:
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
    # Servokabeln upp ovanför servot; CR Touch-kabeln genom skenan över servot.
    s -= box((25, 52, 53.5), (43, 62, 61))
    # Börja bakom magnetstoppet: kabelspåret får inte öppna magnetens skyddshud.
    s -= box((37, 30.5, 55), (43, 52.5, 57.5))
    # Springa för microSD genom bakväggen, med nagelgrop runt öppningen.
    s -= box((PI_RUM[0] - 6.5, SD_SPRINGA[0], SD_Z[0] - .6), (PI_RUM[0] + 1.0, SD_SPRINGA[1], SD_Z[1] + .6))
    s -= box((PI_RUM[0] - 6.5, SD_SPRINGA[0] - 1.5, SD_Z[0] + 2), (PI_RUM[0] - 3.0, SD_SPRINGA[1] + 1.5, SD_Z[1] - 2))
    # Samlad kabel ut bakåt, in i gapet mot Core där den inte syns framifrån.
    s -= box((7, 56, 108), (13, 66, 118))
    for y in (60, 65):                                      # buntbandsbryggor strax ovanför utgången; slutar före ADXL-skruven
        s += box((11, y, 118.5), (14.3, y + 2, 121.5))
    return s


def sidopanel():
    """Tornets hela sida som en enda panel, plan mot X max-sidan."""
    p = prisma_y(inset(sidoprofil(), 2.15), Y1 - 2, Y1)
    p &= box((0, Y1 - 3, 0), (PANEL_X - 2.15, Y1 + 1, 200))   # klipper insetsens spets vid kamerablockets hörn
    for x, z in PANEL_HAL:
        p -= cyl_y(x, z, Y1 - 3, Y1 + 1, 3.4)
        p -= cyl_y(x, z, Y1 - 1, Y1 + 1, 6.2)
    # Fingrar som pressar korten mot sina anlägg när panelen skruvas på.
    for x, z in PI_HAL:
        if (x, z) in PI_SKRUV:
            p += cyl_y(x, z, PI_Y + 1.45, Y1 - 1.9, 7.0)
            p -= cyl_y(x, z, PI_Y + 1.0, Y1 + 1, 2.9)
            p -= cyl_y(x, z, PI_SKRUV_SATE, Y1 + 1, 5.0)
        else:
            p += cyl_y(x, z, PI_Y + 1.45, Y1 - 1.9, 5.0) - cyl_y(x, z, PI_Y + 1.0, PI_Y + 2.6, 3.2)
    for x, z in REG_FINGER:
        p += cyl_y(x, z, PI_Y + 1.65, Y1 - 1.9, 5.0)
    for z in (139, 144, 149, 154, 159, 164):
        p -= box((28, Y1 - 3, z - 0.9), (62, Y1 + 1, z + 0.9))
    for z in (78, 83, 88, 93, 98):                           # luft in vid regulatorerna, ut vid Pi:n
        p -= box((15, Y1 - 3, z - 0.9), (53, Y1 + 1, z + 0.9))
    # Mikrofonram på insidan: tre sidor håller kortet mot panelen. Översidan är helt öppen, eftersom
    # kortets sex lödpunkter sitter i en rad längs den kanten (ca 13 mm); lödning och sex ledningar
    # går fritt uppåt mot Pi:n bakom panelen. Bakom kortet är tornet öppet, så lödtennets höjd begränsar inte.
    mx, mz = MIK
    h, v, d = MIK_RUTA / 2, 1.2, 2.5
    ram = box((mx - h - v, Y1 - 2 - d, mz - h - v), (mx + h + v, Y1 - 1.9, mz + h))
    ram -= box((mx - h, Y1 - 2 - d - 1, mz - h), (mx + h, Y1 - 1.95, mz + h + 1))
    p += ram
    p -= cyl_y(mx, mz, Y1 - 3, Y1 + 1, MIK_HAL_D)
    p -= cyl_y(mx, mz, Y1 - MIK_NAT[1], Y1 + 1, MIK_NAT[0])
    return p


def bricka():
    """Distansbricka under M3-huvudet på ADXL-kortet, så att M3 x 10 inte når tornets framvägg. Två stycken."""
    return Cylinder(3.5, 3.5) - Cylinder(1.7, 4.0)


def arm(prob_x=PROB[0]):
    """Svepande arm: navets rundning går över i en fot som bär CR Touchen."""
    y0, y1 = ARM_Y
    w0, w1 = ARM_W
    u, n, L = arm_geo(prob_x)
    bx, bz = prob_x, FLANS_Z + 3
    F = FLANS_Z
    def sid(t, s):
        w = w0 + (w1 - w0) * t / L
        return (PX + u[0] * t + s * n[0] * w, PZ + u[1] * t + s * n[1] * w)
    rygg = (PX - u[0] * w0, PZ - u[1] * w0)
    fot_h, fot_v = (prob_x + 11, F), (prob_x - 11, F)
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
    # Foten: mjuk platta som CR Touchen skruvas under.
    fot = box((prob_x - 15, y0, F), (prob_x + 15, PROB[1] + 6, F + 4.5))
    fot = fillet(fot.edges().filter_by(Axis.Z), 5.0)
    fot = fillet(fot.faces().sort_by(Axis.Z)[-1].edges(), 1.6)
    a += fot
    # Bula för skruvhuvudet som fäster mot magneten.
    t = BULA_T
    w = w0 + (w1 - w0) * t / L
    # Bredare bula ger gods runt huvudurtaget och överlappar armens framyta.
    # Ändytan ligger 0,5 mm innanför nominella sidplanet; stålhuvudet tar mot magneten.
    bula = Pos(PX + u[0] * t + n[0] * (w - 3.5), sum(BULA_Y) / 2, PZ + u[1] * t + n[1] * (w - 3.5)) * Rot(0, 90 - math.degrees(math.atan2(n[1], n[0])), 0) * Cylinder(3.7, 6.0)
    bula &= box((-100,-100,-100),(200,30.0,200))  # frigång till servohusets ovansida
    a += bula
    s_p = (PX + u[0] * t + n[0] * w, PZ + u[1] * t + n[1] * w)
    rot = Rot(0, 90 - math.degrees(math.atan2(n[1], n[0])), 0)
    a -= Pos(s_p[0] - n[0] * 1.65, sum(BULA_Y) / 2, s_p[1] - n[1] * 1.65) * rot * Cylinder(2.95, 3.3)   # M3-huvud, skruvdjupet ställer hållkraften
    a -= Pos(s_p[0] - n[0] * 7, sum(BULA_Y) / 2, s_p[1] - n[1] * 7) * rot * Cylinder(1.3, 9)
    # Öppet kabelspår: 6 x 2,2 mm kuvert för fem ledare; 1,8 mm rygg lämnas.
    a -= prisma_y([sid_p for sid_p in ((PX + u[0] * 18 + n[0] * 3.0, PZ + u[1] * 18 + n[1] * 3.0),
                   (bx + n[0] * 3.0, bz + n[1] * 3.0), (bx - n[0] * 3.0, bz - n[1] * 3.0),
                   (PX + u[0] * 18 - n[0] * 3.0, PZ + u[1] * 18 - n[1] * 3.0))], y1 - 2.2, y1 + .1)
    a -= box((prob_x - 1.75, y1 - .5, F + 3), (prob_x + 1.75, PROB[1] - 4.5, F + 5))
    for x in (prob_x - cr.HAL_CC / 2, prob_x + cr.HAL_CC / 2):
        a -= Pos(x, PROB[1], F + 2) * Cylinder(cr.M3_PILOT_D / 2, 10)  # M3 x 8 genom hylsa och fläns, eller M3 x 6 utan hylsa
    a -= Pos(prob_x, PROB[1], F + 2) * Cylinder(5, 10)
    # Öppet framåt: kontakten kan kopplas ur utan att klämmas mellan arm och prob.
    a -= box((prob_x - cr.KONTAKT_B / 2, PROB[1] + cr.KONTAKT_Y[0], F - 1),
             (prob_x + cr.KONTAKT_B / 2, PROB[1] + cr.KONTAKT_Y[1], F + cr.KONTAKT_H))
    # Hornet kläms mot botten, två sidostöd och bakre navanslag.
    # Ø11-hålet avlastar navet i sidled; bygeln använder befintliga M3-typer.
    a += horn_lage(hf.kropp(),prob_x)
    a -= horn_lage(hf.urtag(),prob_x)
    a -= horn_lage(hf.bulthal(),prob_x)
    a += horn_lage(hf.anlaggningar(),prob_x)
    # Bevara utfällda lägets stoppribba längs den öppna fickans sida.
    # Hornet förs in 0,5 mm ovanför botten och sänks därefter till sina anlägg.
    ribba=[sid(7,-1),sid(15,-1)]
    ribba += [(p[0]+n[0]*1.5,p[1]+n[1]*1.5) for p in reversed(ribba)]
    horn_y=32.6+SERVO_DY-hf.H_MONTERAT
    a += prisma_y(ribba,horn_y-1.0,horn_y+.3)
    return a


def crtouch(prob_x=PROB[0]):
    """Verklig separat CR Touch-referens: kropp och utfällt stift, inte printdel."""
    return Pos(prob_x, PROB[1], FLANS_Z) * cr.referens()


def kontaktkuvert(prob_x=PROB[0]):
    """Reserverat kontakt-/kabelutrymme, konstruktionskuvert som måste provpassas."""
    return box((prob_x - cr.KONTAKT_B / 2, PROB[1] + cr.KONTAKT_Y[0], FLANS_Z),
               (prob_x + cr.KONTAKT_B / 2, PROB[1] + cr.KONTAKT_Y[1], FLANS_Z + cr.KONTAKT_H))


def skyddshylsa(prob_x=PROB[0]):
    """Öppen CR Touch-hylsa med gemensamma M3-fästen, fri stiftände och 0,6 mm kroppsspel."""
    x, y, f = prob_x, PROB[1], FLANS_Z
    t, b = -cr.FLANS_T, -cr.KROPP_DJUP - .6
    cy = cr.STIFT_Y
    def profil(bredd, djup, z):
        return Pos(0, cy, z) * RectangleRounded(bredd, djup, 2.0)
    # Bred vid flänsens skuldra, smal kring kroppen; sluttningen kan printas utan dold stödhylla.
    def svep(extra, z0, z1):
        return loft([profil(w + 2 * extra, 18.7 + 2 * extra, z)
                     for w, z in ((28.4, z0), (28.4, -8), (17.4, -14), (17.4, z1))], ruled=True)
    k = svep(1.6, t, b) - svep(0, t + .2, b - .2)
    # Två underlägg under originalflänsen, fria från kroppen och förenade med ytterringen.
    kropp = cr.kropp_med_sidospel()
    for hx in (-cr.HAL_CC / 2, cr.HAL_CC / 2):
        pad = Pos(hx, 0, t - 1) * Cylinder(3.4, 2)
        xa, xb = sorted((hx, (-1 if hx < 0 else 1) * 15.7))
        pad += box((xa, -2.5, t - 2), (xb, 2.5, t))
        k += pad - kropp
        k -= Pos(hx, 0, t - 1) * Cylinder(cr.M3_FRITT_D / 2, 5)
        # Öppning under skruvhuvudet för verktyg; hylsan får inte låsa skruven inne.
        k -= Pos(hx, 0, (b - 1 + t - 2) / 2) * Cylinder(3.2, t - 2 - b + 1)
    return Pos(x, y, f) * k


def parkera(o):
    return Pos(PX, 0, PZ) * Rot(0, PARK, 0) * Pos(-PX, 0, -PZ) * o


def namn(o, etikett, farg):
    o.label = etikett
    o.color = Color(*farg)
    return o


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ut", required=True, type=Path)
    p.add_argument("--prob-x", "--blt-x", dest="prob_x", type=float, default=PROB[0])
    a = p.parse_args()
    a.ut.mkdir(parents=True, exist_ok=True)
    t, ar, bl = torn(a.prob_x), arm(a.prob_x), crtouch(a.prob_x)
    sn, so = stoppdelar(a.prob_x)
    l = sidopanel()
    for n, o in (("torn", t), ("arm", ar), ("crtouch", bl), ("sidopanel", l), ("kabel", kabel()), ("bricka", bricka()), ("kapa", skyddshylsa(a.prob_x)), ("lampbarare-utkast", lampor.barare()), ("hornbygel",horn_lage(hf.bygel(),a.prob_x)), ("stopp-nedre", sn), ("stopp-ovre", so)):
        forvantat = 2 if n == "crtouch" else 1
        if not o.is_valid or len(o.solids()) != forvantat:
            raise ValueError(f"{n}: ogiltig geometri eller fel antal solider")
        print(n, "giltig", o.is_valid, "solider", len(o.solids()), "volym cm3", round(o.volume / 1000, 1),
              "bbox", [round(v, 1) for v in (*o.bounding_box().min, *o.bounding_box().max)])
        export_stl(o, str(a.ut / f"{n}.stl"), tolerance=.05, angular_tolerance=.2)
    export_stl(horn_lage(hf.skruvar(),a.prob_x),a.ut/'hornskruvar-referens.stl')
    export_stl(magnet_skruv_attrapp(a.prob_x),a.ut/'magnetstal-referens.stl')
    cx, cy, cz = LINS
    delar = [
        namn(t, "Sidotorn", (.16, .18, .2)),
        namn(servo_attrapp(), "Servo_SPMS664_ATTRAPP", (.1, .1, .12)),
        namn(sn, "Stoppdel_nedre", (.16, .18, .2)),
        namn(so, "Stoppdel_ovre", (.16, .18, .2)),
        namn(kabel(), "Kabel_ATTRAPP", (.1, .1, .1)),
        namn(ar, "Arm_utfalld", (.9, .62, .29)),
        namn(horn_lage(hf.bygel(),a.prob_x),"Hornbygel_utfalld",(.3,.5,.7)),
        namn(parkera(horn_lage(hf.bygel(),a.prob_x)),"Hornbygel_parkerad",(.3,.5,.7)),
        namn(horn_lage(hf.horn(),a.prob_x),"Servohorn_YTTRE_REFERENS",(.15,.15,.15)),
        namn(horn_lage(hf.skruvar(),a.prob_x),"Hornbygel_M3x10_REFERENS",(.6,.6,.6)),
        namn(magnet_skruv_attrapp(a.prob_x),"Magnetkontakt_M3x10_REFERENS",(.6,.6,.6)),
        namn(bl, "CR Touch_utfalld_ATTRAPP", (.85, .2, .15)),
        namn(parkera(copy.deepcopy(ar)), "Arm_parkerad", (.9, .62, .29)),
        namn(parkera(copy.deepcopy(bl)), "CR Touch_parkerad_ATTRAPP", (.85, .2, .15)),
        namn(skyddshylsa(a.prob_x), "CR Touch_hylsa_utfalld", (.9, .62, .29)),
        namn(parkera(skyddshylsa(a.prob_x)), "CR Touch_hylsa_parkerad", (.9, .62, .29)),
        namn(box((cx - KORT_B / 2, KORT_Y[0], KORT_FRAM), (cx + KORT_B / 2, KORT_Y[1], KORT_BAK)), "Kamerakort_ATTRAPP", (.1, .45, .2)),
        namn(box((cx - 11.45, KORT_Y[1] - 6.9, KORT_BAK), (cx + 11.45, KORT_Y[1] - .4, KONTAKT_TOPP)), "Flatkontakt_ATTRAPP", (.85, .8, .6)),
        namn(Pos(cx, cy, cz + 3.45) * Cylinder(4.25, 6.9), "Lins_ATTRAPP", (.05, .05, .05)),
        namn(box((PI_CENTER[0] - 32.5, PI_Y, PI_CENTER[1] - 15), (PI_CENTER[0] + 32.5, PI_Y + 1.4, PI_CENTER[1] + 15)), "Pi_Zero_2_ATTRAPP", (.15, .55, .3)),
        namn(l, "Sidopanel", (.16, .18, .2)),
        namn(lampor.barare(), "Lampbarare_PRELIMINAR", (.3, .5, .7)),
        namn(lampor.lampkuvert(), "G4_SOCKEL_OCH_LAMPA_KONSTRUKTIONSUTRYMME", (.95, .95, .7)),
        namn(box((PI_CENTER[0] - 32.5 - 2.6, PI_Y + 1.4, SD_Z[0] + .5), (PI_CENTER[0] - 32.5 + 12.0, PI_Y + 2.4, SD_Z[1] - .5)), "microSD_ATTRAPP", (.2, .2, .2)),
        namn(box((PI_CENTER[0] - 25.4, PI_Y + 1.4, PI_CENTER[1] - 11.5 - 2.54), (PI_CENTER[0] + 25.4, LIST_TOPP_Y, PI_CENTER[1] - 11.5 + 2.54)), "Stiftlist_ATTRAPP", (.1, .1, .1)),
        namn(box((MIK[0] - 7, Y1 - 2 - 2.5, MIK[1] - 7), (MIK[0] + 7, Y1 - 2.5, MIK[1] + 7)), "INMP441_ATTRAPP", (.45, .2, .55)),
        *[namn(box((x0, PI_Y, REG_Z0), (x0 + 21, PI_Y + 14, REG_Z0 + 43)), f"LM2596_{k}_ATTRAPP", (.1, .25, .6)) for k, x0 in REG_X0.items()],
    ]
    export_step(Compound(label="Sidotorn_v2", children=delar), str(a.ut / "sidotorn_v2.step"))
    # Komponenternas lägen till granskningen, så att den alltid kontrollerar det som faktiskt ritats.
    (a.ut / "elektronik.json").write_text(json.dumps({
        "Pi": [[PI_CENTER[0] - 32.5, PI_Y, PI_CENTER[1] - 15], [PI_CENTER[0] + 32.5, PI_Y + 1.4, PI_CENTER[1] + 15]],
        **{f"LM2596_{k}": [[x0, PI_Y, REG_Z0], [x0 + 21, PI_Y + 14, REG_Z0 + 43]] for k, x0 in REG_X0.items()},
        "ADXL": [[ACC_HAL[0][0] - 2.5, PI_Y, ACC_HAL[0][1] - 7.8], [ACC_HAL[1][0] + 2.5, PI_Y + 3, ACC_HAL[0][1] + 7.8]],
        "microSD": [[PI_CENTER[0] - 32.5 - 2.6, PI_Y + 1.4, SD_Z[0] + .5], [PI_CENTER[0] - 32.5 + 12.0, PI_Y + 2.4, SD_Z[1] - .5]],
        "Mikrofon": [[MIK[0] - 7, Y1 - 2 - 2.5, MIK[1] - 7], [MIK[0] + 7, Y1 - 2.5, MIK[1] + 7]], "mik": [*MIK, MIK_HAL_D],
        "Kort": [[cx - KORT_B / 2, KORT_Y[0], KORT_FRAM], [cx + KORT_B / 2, KORT_Y[1], KORT_BAK]],
        "Flatkontakt": [[cx - 11.45, KORT_Y[1] - 6.9, KORT_BAK], [cx + 11.45, KORT_Y[1] - .4, KONTAKT_TOPP]],
        "magnet": [*magnet_lage(a.prob_x), sum(BULA_Y) / 2], "kort_hal": KORT_HAL, "kort_bak": KORT_BAK, "kort_fram": KORT_FRAM, "klammor": KLAMMOR, "ffc_b": FFC_B, "lins": LINS, "prob_montage": [a.prob_x, PROB[1], FLANS_Z], "prob_hal_cc": cr.HAL_CC, "prob_flans_t": cr.FLANS_T, "prob_kropp_djup": cr.KROPP_DJUP, "prob_stift_y": cr.STIFT_Y,
        "pi_hal": PI_HAL, "panel_hal": PANEL_HAL, "pi_skruv": PI_SKRUV, "topp": TOPP}))
    kallor = [Path(__file__), Path(cr.__file__), cr.REFERENS, Path(lampor.__file__),Path(hf.__file__)]
    exporter = [a.ut / f"{n}.stl" for n in ("torn", "arm", "crtouch", "sidopanel", "kabel", "bricka", "kapa", "lampbarare-utkast", "hornbygel", "stopp-nedre", "stopp-ovre")]
    exporter += [a.ut / "sidotorn_v2.step", a.ut / "elektronik.json"]
    exporter += [a.ut/'hornskruvar-referens.stl',a.ut/'magnetstal-referens.stl']
    (a.ut / "manifest.json").write_text(json.dumps({
        "kallor_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in kallor},
        "exporter_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in exporter},
        "prob_x": a.prob_x, "referenslicens": "CC BY-NC-SA 4.0, Jonathan Harper; se referenser/README.md"
    }, ensure_ascii=False, indent=2) + "\n")
    print("klar")


if __name__ == "__main__":
    main()
