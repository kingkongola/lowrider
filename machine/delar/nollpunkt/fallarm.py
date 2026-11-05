"""Fällarm v4 för HLTNC V6-proben: formgiven studie, ej provad.
Krav (Adam 2026-11-04): får sticka ut i Z och maskinens ±Y (x här), aldrig i maskinens ±X (y här, längs balken): y <= 73.
Mått i mm i fräsramen M: x bort från Core, y längs balken, z upp, fräsaxel x=y=0.
Formspråk: V1E:s fasade kanter på fästet, en kapsel som följer proben.
Material: PLA (Adam 2026-11-04). Stag A med kullager, stag B i 3 mm aluminium.
Plana anliggningsytor behålls; beröringskanter rundas."""
from build123d import *
from pathlib import Path
import math

UT = Path(__file__).parent
HYLSA_Z = 14.7        # hylsmutterns underkant (M1 = 16,3 under plattan z 31)
SPETS_UNDER_MUTTER = 54.0  # når ovansidan på 52 mm XPS; hylsmutter ca 111 mm över offerskivan vid översta Z (körlogg)
SPETS_Z = HYLSA_Z - SPETS_UNDER_MUTTER
# Proben: bara Ø6-skaftet är uppgivet, resten uppskattat ur foto
STIFT = 27.0; KROPP_H = 28.0; KROPP_D = 45.0; SKAFT_L = 23.0; SKAFT_D = 6.0
XC, YC = 40.0, 40.0   # probaxel nedfälld
PX, PZ = 30.6, 37.1   # led
OX, OZ = 38.0, 85.0   # servoaxel
R, r, L = 24.0, 14.0, 29.1
TH_UT = -177.0
TH_NED = TH_UT - 90.0
Y_V = 60.5            # servotopp: vev och rocker y 60,5-64,5, stag 64,5-69,5, yttre öra 70-73
Z_MITT = 46.5         # probaxelns höjd infälld
LAGER_D = 16.0; LAGER_B = 5.0   # 625ZZ i navets ändar
STAG_B = 5.0          # stagets tjocklek med 623ZZ (3x10x4); version B: 3 mm aluminium
RUND = 1.0            # kantradie på synliga kanter

def cy(y0, y1, x, z, d):
    return Cylinder(d/2, y1-y0, rotation=(90, 0, 0)).moved(Location((x, (y0+y1)/2, z)))
def cx(x0, x1, y, z, d):
    return Cylinder(d/2, x1-x0, rotation=(0, 90, 0)).moved(Location(((x0+x1)/2, y, z)))
def cz(z0, z1, x, y, d):
    return Cylinder(d/2, z1-z0).moved(Location((x, y, (z0+z1)/2)))
def k(x, y, z):
    return Box(x[1]-x[0], y[1]-y[0], z[1]-z[0], align=Align.MIN).moved(Location((x[0], y[0], z[0])))

def rund(sol, axel, rad=RUND):
    """Rundar kanterna runt ändytorna; ger upp tyst om geometrin inte tillåter."""
    try:
        return fillet(sol.edges().filter_by(axel, reverse=True), rad)
    except Exception:
        return sol

def prisma_xz(pts, y0, y1, rad=0, kant=0):
    """Polygon (x,z) utdragen längs y."""
    f = Plane.XZ * Polygon(*pts, align=None)
    if rad: f = fillet(f.vertices(), rad)
    s = extrude(f, amount=y1-y0, dir=(0, 1, 0)).moved(Location((0, y0, 0)))
    return rund(s, Axis.Y, kant) if kant else s
def prisma_yz(pts, x0, x1, rad=0, kant=0):
    """Polygon (y,z) utdragen längs x."""
    f = Plane.YZ * Polygon(*pts, align=None)
    if rad: f = fillet(f.vertices(), rad)
    s = extrude(f, amount=x1-x0, dir=(1, 0, 0)).moved(Location((x0, 0, 0)))
    return rund(s, Axis.X, kant) if kant else s
def staf(x0, z0, d0, x1, z1, d1, y0, y1, kant=True):
    """Avsmalnande bar mellan två cirklar."""
    dx, dz = x1-x0, z1-z0; n = math.hypot(dx, dz)
    a = math.asin(max(-1, min(1, (d0-d1)/2/n))); b = math.atan2(dz, dx)
    t1, t2 = b + math.pi/2 + a, b - math.pi/2 - a
    pts = [(x0+d0/2*math.cos(t1), z0+d0/2*math.sin(t1)), (x1+d1/2*math.cos(t1), z1+d1/2*math.sin(t1)),
           (x1+d1/2*math.cos(t2), z1+d1/2*math.sin(t2)), (x0+d0/2*math.cos(t2), z0+d0/2*math.sin(t2))]
    h = prisma_xz(pts, y0, y1) + cy(y0, y1, x0, z0, d0) + cy(y0, y1, x1, z1, d1)
    return rund(h, Axis.Y, min(RUND, (y1-y0)/3.2)) if kant else h
def pin(th):
    return (PX + r*math.cos(math.radians(th)), PZ + r*math.sin(math.radians(th)))
def pol(th, rad):
    return (PX + rad*math.cos(math.radians(th)), PZ + rad*math.sin(math.radians(th)))

def faste():
    # platta mot verktygsfästet
    p = prisma_yz([(38.8, 50), (72.5, 50), (72.5, 100), (62, 110), (52, 124), (52, 132), (38.8, 132)], 1, 6, 2.5, RUND)
    for z in (64.25, 125.25):
        p += cx(-7.3, 1.2, 43.95, z, 9.6)
        p += cx(4.5, 8.5, 43.95, z, 12)
    # hylla ut till servot och det inre örat
    hylla = Plane.XY * Polygon((1, 40), (30, 40), (31, YC-13), (39, YC-13), (39, Y_V-0.5), (1, Y_V-0.5), align=None)
    p += extrude(hylla, amount=6, dir=(0, 0, 1)).moved(Location((0, 0, 56)))
    # inre öra från hyllan ner till axeln
    p += staf(PX, PZ, 14, 35, 58, 8, YC-13, YC-10, False)
    # yttre öra: rakt ben från axeln upp till plattan
    p += staf(PX, PZ, 16, 3.5, 72, 10, 70, 73, False)
    # servoram: fönster för kroppen, öronen vilar på +y-sidan
    ram = k((OX-14, OX+13), (47, 51), (60, OZ+41))
    ram -= k((OX-10.2, OX+10.2), (46, 52), (OZ-10.2, OZ+30.2))
    p += ram
    p += k((6, OX-13), (47, 51), (106, 112))                # stag mot plattan
    # hål
    for z in (64.25, 125.25):
        p -= cx(-10, 12, 43.95, z, 5.4)
    p -= cy(YC-20, 80, PX, PZ, 5.2)
    for dx in (-5, 5):
        for z in (OZ-14.75, OZ+34.75):
            p -= cy(44, 54, OX+dx, z, 2.6)
    for z in (71.5, 76.5):
        p -= cx(OX+9, OX+15, 49, z, 2.6)                     # kåpans skruvar
    return p

def kapsel_delar(ri, nos_r, x0, xm, x1, zb):
    """Rotationskropp och plan-prisma var för sig, för säkra booleska operationer."""
    n = 24
    pts = [(x0, ri), (xm, ri)]
    for i in range(1, n+1):
        t = i/n
        pts.append((xm+(x1-nos_r-xm)*t, nos_r+(ri-nos_r)*(0.5+0.5*math.cos(math.pi*t))))
    for i in range(1, 8):               # slutar i en liten plan yta, inte i en spets: ger tät mesh
        a = math.pi/2*i/8
        pts.append((x1-nos_r+nos_r*math.sin(a), nos_r*math.cos(a)))
    prof = make_face(Plane.XY * Wire.make_polygon([Vector(p[0], p[1], 0) for p in pts] + [Vector(pts[-1][0], 0, 0), Vector(x0, 0, 0)], close=True))
    kr = revolve(prof, Axis.X, 360).moved(Location((0, YC, Z_MITT)))
    q = pts[:-1]
    plan = prisma_plan([(p[0], YC+p[1]) for p in q] + [(pts[-1][0], YC)] + [(p[0], YC-p[1]) for p in reversed(q)], zb, Z_MITT)
    return kr, plan

def prisma_plan(pts, z0, z1):
    f = Plane.XY * Polygon(*pts, align=None)
    return extrude(f, amount=z1-z0, dir=(0, 0, 1)).moved(Location((0, 0, z0)))

def kapa():
    v = 2.5
    x0, xm, x1 = 53.0, 80.0, 111.0
    wi = KROPP_D/2+1.5
    k1, p1 = kapsel_delar(wi+v, 10.0, x0, xm, x1, 23.0)
    k2, p2 = kapsel_delar(wi, 7.5, x0-1, xm, x1-v, 10.0)
    c = (k1 + p1) - p2
    c = c - k2
    c -= k((0, 130), (0, 110), (-30, 23.0))           # plan underkant
    # fäste mot servoramen
    c -= k((x0-1, 62), (59, 68), (60, 78))             # urtag för vev och stag
    c += k((OX+13, x0+3), (46, 52), (69.5, 79.5))
    c = c - cx(OX+12, x0+5, 49, 71.5, 3.4) - cx(OX+12, x0+5, 49, 76.5, 3.4)
    return c

def arm():
    z0 = SPETS_Z+STIFT+KROPP_H+1
    z1 = SPETS_Z+STIFT+KROPP_H+SKAFT_L-1
    zm = (z0+z1)/2
    px, pz = pin(TH_NED)
    y0, y1 = YC-9, Y_V+4                                # navets ändar
    bor = cy(y0-10, y1+10, PX, PZ, LAGER_D-0.5)
    nav = cy(y0, y1, PX, PZ, 21)
    nav = nav - cy(y0+6, y1-6, PX, PZ, 6.0)
    nav = nav - cy(y0-1, y0+LAGER_B, PX, PZ, LAGER_D) - cy(y1-LAGER_B, y1+1, PX, PZ, LAGER_D)
    nav = nav - cy(y0+4, y0+7, PX, PZ, 5.6) - cy(y1-7, y1-4, PX, PZ, 5.6)
    bro = staf(PX, PZ, 20, XC, zm, 18, y0+0.5, YC+9, False) - bor
    klamma = cz(z0, z1, XC, YC, 18) + k((XC-4, XC+4), (YC, YC+17), (z0, z1))
    rocker = staf(PX, PZ, 18, px, pz, 9, Y_V, Y_V+4, False) - bor
    a = nav + bro + klamma + rocker
    a -= cy(Y_V-1, Y_V+5, px, pz, 3.2)
    a -= cz(z0-2, z1+2, XC, YC, SKAFT_D+0.2)
    a -= k((XC-0.75, XC+0.75), (YC, YC+18), (z0-2, z1+2))
    a -= cx(XC-9, XC+9, YC+12, zm, 3.2)
    return a

def stag():
    """Version A: printad (PLA) med två 623ZZ. Sänkta säten från båda håll hindrar lagret från att vandra."""
    s = staf(0, 0, 14, L, 0, 14, 0, STAG_B)
    for x in (0, L):
        s -= cy(-1, STAG_B+1, x, 0, 8.0)          # genomgående, lagret hålls av kragen
        s -= cy(0.5, STAG_B+1, x, 0, 10.1)        # lagersäte, 4,5 mm djupt
    return s

def stag_alu():
    """Version B: 3 mm aluminium, fräst. Hål Ø3,2 med M3-skruv som tapp, utan lager."""
    s = staf(0, 0, 10, L, 0, 10, 0, 3)
    s -= cy(-1, 4, 0, 0, 3.2)
    s -= cy(-1, 4, L, 0, 3.2)
    return s

def vev():
    v = staf(0, 0, 20, R, 0, 10, 0, 4)
    v -= cy(-1, 5, R, 0, 3.2)
    v -= cy(-1, 5, 0, 0, 7.5)
    for x, z in ((0, 7), (0, -7)):
        v -= cy(-1, 5, x, z, 2.2)              # skruvas mot servoarmen, mät hålbilden
    return v

def servo():
    """Bara för bilder: SPMS664 ca 40x20x41 enligt annons."""
    s = k((OX-10, OX+10), (Y_V-41, Y_V), (OZ-10, OZ+30))
    s = fillet(s.edges().filter_by(Axis.Y), 2)
    s += k((OX-10, OX+10), (51, 53.5), (OZ-17, OZ+37))
    return s

if __name__ == "__main__":
    delar = {"faste": faste(), "kapa": kapa(), "arm": arm(), "stag": stag(), "stag_B_alu": stag_alu(), "vev": vev()}
    for n, d in delar.items():
        export_stl(d, str(UT/f"fallarm_{n}.stl"), tolerance=0.05, angular_tolerance=0.2); export_step(d, str(UT/f"fallarm_{n}.step"))
        bb = d.bounding_box(); print(n, round(d.volume/1000, 1), 'cm3', [round(v, 1) for v in bb.min], [round(v, 1) for v in bb.max], 'solider', len(d.solids()))
    export_stl(servo(), str(UT/"fallarm_servo_bild.stl"), tolerance=0.02, angular_tolerance=0.15)
