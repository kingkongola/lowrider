"""Fällarm version C: armen direkt på servots axel. Studie, ej provad.
Mått i mm i fräsramen M: x bort från Core, y längs balken (maskinens X), z upp, fräsaxel x=y=0.
Krav: y <= 73, låsknapp vid ca (19, 15, 40) ska nås, inga länkar. Material PLA."""
from build123d import *
from pathlib import Path
import math
from fallarm import cy, cx, cz, k, staf, prisma_yz, prisma_xz, kapsel_delar, rund, RUND, HYLSA_Z, SPETS_Z, SKAFT_D
import fallarm
# Prob V5/TP05C, ritning i annonsen (ej uppmätt): kropp Ø33 x 21, skaft 20, stylus 26
STIFT, KROPP_H, KROPP_D, SKAFT_L = 26.0, 21.0, 33.0, 20.0
# Kontakt på kroppens sida, vänd mot -y. Uppskattad ur annonsens foto: mäts vid leverans
KONTAKT_UNDER_TOPP, KONTAKT_L, KONTAKT_D = 7.0, 25.0, 9.0
UT = Path(__file__).parent
YC = 34.0              # probaxel längs balken
PX, PZ = 45.0, 43.6    # servoaxel = led
E = 16.0               # probaxel utanför servoaxeln
XC = PX + E
Y_TOPP = 32.6          # husets topp; ritning S664: hus 40,4, totalt 46,4, botten y 73
LX, LZ = 36.6, 64.26   # klämskruvens läge i verktygsfästet (CAD)
OX_B = 72.0            # balken når över armens klämma, där stoppen sitter
X_STOPP, X_MAGNET = 64.0, 70.0   # infällt stopp och magnet längs balken
Y_RAM = 43.3           # öronens undersida 29,7 från botten (ritning S664); servot sticks in från -y
T_RAM = 6.0            # godstjocklek i ramen, minst 6 mm för PLA
fallarm.YC = YC; fallarm.Z_MITT = PZ + E  # kapselformen läser dessa
Z_MITT = PZ + E
WI = KROPP_D/2 + 1.5   # kåpans innerradie
V_KAPA = 3.0           # kåpans vägg
Z_TAK = Z_MITT + WI    # pelarens topp, kåpans tunga vilar här
Z_BALK = Z_TAK - 1.0   # balkens ovansida, under tungan

def servo():
    """Bara för bilder, mått ur ritning S664: 40 x 20 x 40,4, öron 59,8 långa, 3,7 tjocka, axel 10 från änden."""
    s = k((PX-30, PX+10), (Y_TOPP, Y_TOPP+40.4), (PZ-10, PZ+10))
    s = fillet(s.edges().filter_by(Axis.Y), 2)
    s += k((PX-10-29.9, PX-10+29.9), (Y_RAM-3.7, Y_RAM), (PZ-10, PZ+10))
    s += cy(Y_TOPP-0.8, Y_TOPP, PX, PZ, 14)
    s += cy(Y_TOPP-6, Y_TOPP, PX, PZ, 6)
    return s

def faste():
    p = prisma_yz([(38.8, 55), (72.5, 55), (72.5, 100), (62, 110), (52, 124), (52, 132), (38.8, 132)], 1, 6, 2.5, RUND)
    for z in (64.25, 125.25):
        p += cx(-7.3, 1.2, 43.95, z, 9.6)
        p += cx(4.5, 8.5, 43.95, z, 12)
    # servoram: öronen vilar mot -y-sidan, kraftiga balkar runt fönstret
    ram = prisma_xz([(PX-41, PZ-16), (PX+21, PZ-16), (PX+21, PZ+18), (PX-41, PZ+18)], Y_RAM, Y_RAM+T_RAM, 4, 0)
    ram -= k((PX-30.2, PX+10.2), (Y_RAM-1, Y_RAM+T_RAM+1), (PZ-10.2, PZ+10.2))
    p += ram
    p += k((1, 8), (Y_RAM, Y_RAM+T_RAM), (PZ+10.2, 66))
    # pelare upp till kapselns tak
    p += prisma_xz([(PX+8, PZ+12), (PX+21, PZ+12), (PX+23, Z_TAK), (PX+8, Z_TAK)], Y_RAM, Y_RAM+T_RAM, 3, 0)
    # stag pelare-platta: triangel som tar böjningen, slutar under övre skruvskallen
    p += prisma_xz([(3, 96), (3, 113), (14, 113), (PX+9, 86), (PX+9, 66)], Y_RAM, Y_RAM+T_RAM, 3, 0)
    # gratis fästpunkt: klämskruven i nedre verktygsfästet (x 36,6, z 64,26, säte y 12)
    p += cy(12, 19.5, LX, LZ, 9.6)
    p += prisma_xz([(LX-6, LZ-6), (LX+6, LZ-6), (OX_B, 70), (OX_B, Z_BALK), (33, Z_BALK), (LX-6, LZ+6)], 19.5, 21, 3, 0)
    p += prisma_xz([(33, 70), (OX_B, 70), (OX_B, Z_BALK), (33, Z_BALK)], 19.5, Y_RAM+1, 2, 0)
    p -= cy(10, 27, LX, LZ, 5.4)
    # stopp infälld: M4-skruv ner genom balken mot klämman, och magnet Ø10x3 i balkens undersida
    p -= cz(66, 82, X_STOPP, YC-4, 3.3)
    p -= cz(69, 73, X_MAGNET, YC+4, 10.1)
    # stopp nere: lugg från ramen, M4-skruv i x-led mot klämmans sida
    p += k((PX+1, PX+5), (YC+4, Y_RAM+1), (19, PZ-10.5))
    p -= cx(PX-2, PX+10, YC+6.5, 23.0, 3.3)
    for z in (64.25, 125.25):
        p -= cx(-10, 12, 43.95, z, 5.4)
    # buntband för servots sladd: går genom plattan, glappet mot Core ger plats åt bandet
    for y in (56, 64):
        p -= cx(0, 7, y, 85, 3.4)
    for dz in (-5, 5):
        for x in (PX-33.3, PX+14):   # ritning S664: 33,3 och 14 från axeln, avlånga för att ta upp 48,5-måttet
            p -= k((x-1.7, x+1.7), (Y_RAM-1, Y_RAM+T_RAM+1), (PZ+dz*0.94-1.7, PZ+dz*0.94+1.7))
    for x in (PX+13, PX+19):
        p -= cz(Z_TAK-8, Z_TAK+1, x, Y_RAM+T_RAM/2, 2.6)
    return p

def kapa():
    v, wi = V_KAPA, WI
    zb = Z_MITT - KROPP_D/2 - 1.5       # kåpan täcker kroppens underkant
    x_kropp = PX + (PZ - (SPETS_Z+STIFT+KROPP_H))      # kroppens överkant infälld
    x_spets = PX + (PZ - SPETS_Z)
    x0, xm, x1 = x_kropp-11, x_kropp+21, x_spets+6     # bakkanten lämnar vägg bakom kontaktens slits
    k1, p1 = kapsel_delar(wi+v, 8.0, x0, xm, x1, zb)
    k2, p2 = kapsel_delar(wi, 5.5, x0-1, xm, x1-v, zb-13)
    c = (k1 + p1) - p2
    c = c - k2
    c -= k((0, 150), (0, 110), (-30, zb))
    # tunga mot pelaren och fäste
    c += k((PX+9, x0+4), (Y_RAM-1, Y_RAM+T_RAM+1), (Z_TAK, Z_TAK+v+1))
    c += k((x0, x0+4), (Y_RAM-1, Y_RAM+T_RAM+1), (Z_MITT+wi-2.4, Z_TAK+v+1))
    for x in (PX+13, PX+19):
        c -= cz(Z_TAK-2, Z_TAK+v+3, x, Y_RAM+T_RAM/2, 3.4)
    # slits för kontakten på -y-sidan: öppen nedåt, följer kontaktens båge (nästan rakt upp)
    xk = PX + (PZ - (SPETS_Z+STIFT+KROPP_H-KONTAKT_UNDER_TOPP))
    rs = KONTAKT_D/2 + 0.7
    c -= k((xk-rs, xk+rs+3), (-5, YC-wi+1), (zb-1, Z_MITT))
    c -= cy(-5, YC-wi+1, xk, Z_MITT, 2*rs)
    # två hål för buntband i väggen bredvid slitsen: sladden avlastas här, så att böjen inte hamnar i kontakten
    for dz in (-5, 5):
        c -= cy(-5, YC-wi+1, xk+15, Z_MITT-9+dz, 3.4)
    return c

def arm():
    z0 = SPETS_Z+STIFT+KROPP_H+1
    z1 = SPETS_Z+STIFT+KROPP_H+SKAFT_L-1
    zm = (z0+z1)/2
    y0, y1 = Y_TOPP-11.1, Y_TOPP-7.1      # skiva mot servoarmen i metall (sitter y Y_TOPP-8..Y_TOPP-4 på splinen)
    a = cy(y0, y1, PX, PZ, 18)
    a += staf(PX, PZ, 18, XC, zm, 16, y0, y1, False)
    a += cz(z0, z1, XC, YC, 18)
    a += k((XC-4.5, XC+4.5), (YC-9, YC), (z0, z1))        # klämöron bort från ramen
    a += k((XC-6, XC+6), (y0, YC-5), (z0, z1))         # fyller glappet mellan skiva och klämma
    for r in (-7, 7):
        a -= cy(y0-1, y1+1, PX, PZ+r, 2.4)
    a -= cy(y0-1, y1+1, PX, PZ, 7.5)
    a -= cz(z0-2, z1+2, XC, YC, SKAFT_D+0.2)
    a -= k((XC-0.75, XC+0.75), (YC-10, YC), (z0-2, z1+2))
    a -= cx(XC-9, XC+9, YC-6.5, zm, 3.2)
    a -= cx(XC+3, XC+10, YC+4, PZ-(X_MAGNET-PX), 2.6)   # stålskruv som magneten griper
    return a

if __name__ == "__main__":
    print('spets', XC, YC, SPETS_Z, 'avstånd från fräsen', round(math.hypot(XC, YC), 1), 'infälld spets x', PX+PZ-SPETS_Z, 'axel z', Z_MITT)
    for n, f in (("faste", faste), ("kapa", kapa), ("arm", arm)):
        d = f(); export_stl(d, str(UT/f"fallarm_C_{n}.stl"), tolerance=0.05, angular_tolerance=0.2); export_step(d, str(UT/f"fallarm_C_{n}.step"))
        bb = d.bounding_box(); print(n, d.is_valid, round(d.volume/1000, 1), len(d.solids()), [round(v, 1) for v in bb.min], [round(v, 1) for v in bb.max])
    export_stl(servo(), str(UT/"fallarm_C_servo_bild.stl"), tolerance=0.02, angular_tolerance=0.15)
