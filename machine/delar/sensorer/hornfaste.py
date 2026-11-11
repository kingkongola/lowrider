"""Servohornet i armen: formficka och mittskruven genom armen (omgjort 2026-11-11).

Beprövad lösning (printade robotarmar, pan/tilt): hornet ligger infällt i en ficka med hornets
kontur, så att fickans väggar tar vridmomentet (formlåsning, inte friktion). Servots mittskruv
byts mot en M3 x 10 som går genom armens botten och hornets fläns in i axeln och klämmer
arm, horn och axel i ett förband. Ingen bygel, inga extra skruvar.

Armbotten väljs så att M3 x 10 får exakt fabriksskruvens gängdjup i axeln (6 - 1,7 = 4,3 mm);
då kan den inte bottna i axeln (felsäkring). Mått: CALIBRATION.md 2026-11-10 och 2026-11-11.
Lokalt x längs hornet, y från hornets plana utsida (0) mot servot, z tvärs hornet.
Hornets spetsform och tandning är inte uppmätta; passningen provas med provbiten.
"""
import math
from build123d import Axis, Cylinder, Face, Pos, Rot, Vector, Wire, extrude, fillet

NAV_D, NAV_H = 9.0, 6.0
C, D, E, F, G = 7.3, 6.8, 14.5, 18.8, 2.5
H_MONTERAT = 10.0
HORN_HAL_D = 2.4      # rapporterat cirka 2,4–2,5
SPEL = 0.15           # per sida i fickan; samma typ av passning som kamerafickan (godkänd 2026-11-11)
FLANS = 1.7           # navets fläns under mittskruvens skalle, uppmätt 2026-11-11
FABRIKSSKRUV_L = 6.0  # servots mittskruv, uppmätt 2026-11-11 (Ø3)
MITTSKRUV_L = 10.0    # M3 x 10 ur befintligt lager
BOTTEN = MITTSKRUV_L - FABRIKSSKRUV_L   # 4,0: samma gängdjup som fabriksskruven
SKALLE = (5.5, 3.0)   # M3 insex, Ø x höjd
SATE_D, GENOM_D = 6.2, 3.4
NAV_R = 7.0           # navbossens radie runt axeln
RYGG = 2.5            # gods under hornarmen, utanför fickans botten
FICKA_Y1 = 3.0        # fickan går genom armens platta (lokalt till 2,9) men inte in i bulan


def box(a, b):
    from build123d import Box
    return Pos(*((v+w)/2 for v,w in zip(a,b))) * Box(*(w-v for v,w in zip(a,b)))


def cy(x, z, y0, y1, d):
    return Pos(x, (y0+y1)/2, z) * Rot(90, 0, 0) * Cylinder(d/2, y1-y0)


def py(punkter, y0, y1):
    f = Face(Wire.make_polygon([Vector(x, y0, z) for x,z in punkter], close=True))
    return extrude(f, amount=y1-y0, dir=(0,1,0))


def h(t,c=C,d=D):
    return c/2 + (d-c)/2 * (t-E)/(F-E)


def armkuvert(y0,y1,spel=0,c=C,d=D,nav_d=NAV_D):
    # Spetsradien konstrueras tangent till den raka sidan vid F.
    m = (c-d)/2/(F-E)
    r = d/2 * math.sqrt(1+m*m)
    slut = F-d/2*m
    o = py([(0,-h(0,c,d)-spel),(F,-h(F,c,d)-spel),(F,h(F,c,d)+spel),(0,h(0,c,d)+spel)],y0,y1)
    o += cy(0,0,y0,y1,nav_d+2*spel)
    o += cy(slut,0,y0,y1,2*(r+spel))
    return o


def horn(c=C,d=D,g=G,nav_d=NAV_D):
    """Yttre referens med två uppmätta hållägen; ingen verifierad splinesmodell."""
    o=armkuvert(0,g,c=c,d=d,nav_d=nav_d)+cy(0,0,0,NAV_H,nav_d)
    for t in (E,F):o-=cy(t,0,-.1,g+.1,HORN_HAL_D)
    return o


def nav():
    """Gods som läggs till armen: boss runt axeln och rygg under hela hornet."""
    boss = cy(0, 0, -(BOTTEN + SKALLE[1] + .3), 0, 2 * NAV_R)
    rygg = armkuvert(-RYGG, 0, 2.0)
    return boss + rygg


def ficka():
    """Hornets kontur med spel, öppen mot servot; navet fritt ut mot kragen."""
    return armkuvert(0, FICKA_Y1, SPEL) + cy(0, 0, 0, NAV_H + 3, NAV_D + 2 * SPEL)


def skruvhal():
    """Försänkt säte för M3-skallen och genomgående hål genom botten."""
    return (cy(0, 0, -(BOTTEN + SKALLE[1] + 1), -BOTTEN, SATE_D)
            + cy(0, 0, -BOTTEN - .1, .1, GENOM_D))


def mittskruv():
    """M3 x 10 i sitt läge: skallen i sätet, skaftet genom botten och flänsen in i axeln."""
    return (cy(0, 0, -BOTTEN - SKALLE[1], -BOTTEN, SKALLE[0])
            + cy(0, 0, -BOTTEN, -BOTTEN + MITTSKRUV_L, 3.0))


def gangdjup():
    return MITTSKRUV_L - BOTTEN - FLANS


def provkropp():
    """Litet självständigt prov av armens nav: samma ficka, botten och säte som armen."""
    b = box((-8, -RYGG, -7.5), (25, 2.9, 7.5))
    b = fillet(b.edges().filter_by(Axis.Y), 2.0)
    b += nav()
    b -= ficka()
    b -= skruvhal()
    return b
