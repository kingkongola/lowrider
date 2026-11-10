"""Demonterbar lampbärare och standardiserad docka vid kameran.

Dockan kan printas med tornet före lampköp. Lampbäraren är ett utkast för
två fria G4-kapslar; sockelfästen/temperatur måste verifieras mot valda delar.
Lamp- och sockelkuvert är konstruktionsutrymme, inte verifierad komponent-CAD.
"""
from build123d import Axis, Box, Compound, Cylinder, Pos, Rot, fillet

DOCK_HAL = ((54.5, 131.0), (73.0, 131.0))  # vänster boss överlappar ribban, ingen tangent/knivegg
DOCK_Y = 48.0
DOCK_D = 8.0
DOCK_SLUT_Y = 56.0
STYRTAPP = (64.0, 133.0)  # asymmetrisk tapp förhindrar uppochnervänd lampmodul
M3_PILOT_D = 2.6
M3_FRITT_D = 3.4  # frigång och printtillägg ingår; ingen extra skalfaktor
PLATT_T = 2.0
LAMP_Y = (13.0, 88.0)
STAG_Y = (25.0, 76.0)  # stagen passerar mellan lamporna, inte genom deras kroppar
LAMP_Z = 130.0
SOCKEL_X = (60.0, 74.0)
SOCKEL_D = 18.0
LAMP_X = (74.0, 106.0)  # preliminär kropp; 7 mm av 39 mm antas ligga in i sockelutrymmet
LAMP_D = 10.0


def box(a, b):
    return Pos(*((v + w) / 2 for v, w in zip(a, b))) * Box(*(w - v for v, w in zip(a, b)))


def cy(x, z, y0, y1, d):
    return Pos(x, (y0 + y1) / 2, z) * Rot(90, 0, 0) * Cylinder(d / 2, y1 - y0)


def cx(y, z, x0, x1, d):
    return Pos((x0 + x1) / 2, y, z) * Rot(0, 90, 0) * Cylinder(d / 2, x1 - x0)


def tornbossar():
    """Två permanenta skruvfästen; lampmodulen kan tas bort separat."""
    return Compound(children=[*[cy(x, z, DOCK_Y, DOCK_SLUT_Y, DOCK_D) for x, z in DOCK_HAL],
                              cy(*STYRTAPP, 47.0, 50.0, 3.0)])


def tornhal():
    """Blinda pilothål; öppnar inte ett kabelhål rakt in till elektroniken."""
    return Compound(children=[cy(x, z, DOCK_Y - .1, 54.8, M3_PILOT_D) for x, z in DOCK_HAL])


def dockplatta():
    """Fot till lampbäraren; M3x6 från CR Touch-kitet avses räcka."""
    p = fillet(box((50, DOCK_Y - PLATT_T, 126), (77, DOCK_Y, 136)).edges().filter_by(Axis.Y), 2)
    for x, z in DOCK_HAL:
        p -= cy(x, z, DOCK_Y - PLATT_T - .1, DOCK_Y + .1, M3_FRITT_D)
        p -= cy(x, z, DOCK_Y - PLATT_T - .1, DOCK_Y - PLATT_T + .8, 6.2)
    p -= cy(*STYRTAPP, DOCK_Y - PLATT_T - .1, DOCK_Y + .1, 3.4)
    return p


def sockelplatta(y):
    """Utbytbar sockeladapter bultas i slitsarna; inga okända sockelmått låses här."""
    p = fillet(box((57.5, y - 13, 124), (60, y + 13, 142)).edges().filter_by(Axis.X), 2)
    p -= cx(y, LAMP_Z, 57, 61, 8)  # endast kabelgenomföring, inte passning för en keramiksockel
    for sida in (-1, 1):
        ya, yb = sorted((y + sida * 7.0, y + sida * 9.5))
        p -= cx(ya, LAMP_Z, 57, 61, M3_FRITT_D)
        p -= cx(yb, LAMP_Z, 57, 61, M3_FRITT_D)
        p -= box((57, ya, LAMP_Z - M3_FRITT_D / 2), (61, yb, LAMP_Z + M3_FRITT_D / 2))
    return p


def barare():
    """Öppen bärare runt kameran; lampor/socklar sitter utanför tornet."""
    b = dockplatta()
    b += box((51, 40, 126.2), (105.5, 43.1, 128.7))
    b += box((51, 43.0, 126.2), (77, 47.0, 128.0))  # går under skruvskallarna
    b += box((102.5, STAG_Y[0], 126.2), (105.5, STAG_Y[1], 129.2))
    for y, stag in zip(LAMP_Y, STAG_Y):
        b += box((102.5, stag - 1.5, 126.2), (105.5, stag + 1.5, 141))
        b += box((57.5, stag - 1.5, 138), (105.5, stag + 1.5, 141))
        b += sockelplatta(y)
    return b


def lampkuvert():
    """Två preliminära G4-kroppar och keramiksocklar; kontrolleras som reserverat utrymme."""
    return Compound(children=[o for y in LAMP_Y for o in
        (cx(y, LAMP_Z, *SOCKEL_X, SOCKEL_D), cx(y, LAMP_Z, *LAMP_X, LAMP_D))])
