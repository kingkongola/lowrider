"""Formad hornficka med skruvad M3-kilbygel, konstruktionsutkast.

Komponentmått: CALIBRATION.md, 2026-11-10, servohornets nav.
Lokalt x längs hornet, y från dess plana utsida mot servot, z tvärs hornet.
Yttre hornreferens: rak avsmalning och konstruerad rund spets; inga splines
eller håldiametrar påstås vara uppmätta. Hylsa och servo styrs i sidotorn.py.
"""
import math
from build123d import Axis, Compound, Cylinder, Face, Pos, Rot, Vector, Wire, extrude, fillet, loft

NAV_D, NAV_H = 9.0, 6.0
C, D, E, F, G = 7.3, 6.8, 14.5, 18.8, 2.5
H_MONTERAT = 10.0
HORN_HAL_D = 2.4  # rapporterat cirka 2,4–2,5; mindre värdet i frigångskontroll
SPELRAD = .6  # justermån på fria ytor; fasta anliggningar återläggs efter urtaget
NAV_FRITT_D = 11.0  # sidofrigång; separat bakre navanslag bestämmer längdläget
SKRUVAR = ((22.0,7.5),(28.0,7.5))  # x,z; M3x10, utanför hornet
KAP_Y = (G+.7,G+3.7)
SKRUVSATE = KAP_Y[1]-1.5
SKRUV_L = 10.0
PILOT_BOTTEN = -6.2


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
    # Exakt spetsform återstår att provpassa; den är inte infästningens datum.
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


def kropp():
    b=fillet(box((9,-3,-6),(31.8,0,5)).edges().filter_by(Axis.Y),1.2)
    # Djupet behövs bara vid skruvarna; fri nos undviker dammkjolens svep.
    b+=fillet(box((19.2,-6.8,4),(31.8,0,13.5)).edges().filter_by(Axis.Y),1.2)
    b+=box((16.2,-.1,11),(31.8,5,13.5))
    return b


def anlaggningar():
    """Två sidostöd och bakre navanslag för montering före åtdragning."""
    return Compound(children=[*[py([(ta,-6),(tb,-6),(tb,-h(tb)),(ta,-h(ta))],-.1,1.7)
                              for ta,tb in ((13.2,14.7),(17.9,18.7))],
                              box((-6.5,-.1,-1.5),(-NAV_D/2,1.7,1.5))])


def urtag():
    # Öppen från bygelns sida: hornet kan skjutas in före bygelmontage.
    # Bakom den tunna hornarmen behålls gods för magnetkontaktens skruv.
    return Compound(children=[armkuvert(0,G+.8,SPELRAD),cy(0,0,-8,9,NAV_FRITT_D),
                              box((-5.6,0,0),(F+4,9,11)),box((16.0,.7,.8),(32,9,11))])


def bulthal():
    """Blinda Ø2,6-piloter; M3 formar gänga i plasten, inga nya muttrar."""
    return Compound(children=[cy(x,z,PILOT_BOTTEN,8,2.6) for x,z in SKRUVAR])


def bygel():
    b=py([(16.2,h(16.2)-.8),(31.8,h(31.8)-.8),(31.8,11),(16.2,11)],*KAP_Y)
    snitt=[]
    for t in (16.2,17.8):
        n=h(t)
        snitt.append(Face(Wire.make_polygon([Vector(t,y,z) for y,z in
            ((G+.8,n-.8),(G-.8,n+.8),(G+1.0,n+.8),(G+1.0,n-.8))],close=True)))
    b+=loft(snitt,ruled=True)
    for x,z in SKRUVAR:
        b-=cy(x,z,-1,9,3.4)
        b-=cy(x,z,SKRUVSATE,9,6.2)
    return b


def skruvar():
    return Compound(children=[cy(x,z,SKRUVSATE,SKRUVSATE+3,5.5)
                              +cy(x,z,SKRUVSATE-SKRUV_L,SKRUVSATE,3) for x,z in SKRUVAR])


def provkropp():
    """Litet självständigt prov; plan extra rygg för stödfria lager."""
    b=fillet(box((-6.5,-6.8,-6),(31.8,0,13.5)).edges().filter_by(Axis.Y),1)+kropp()
    b -= urtag()
    b -= bulthal()
    b += anlaggningar()
    return b
