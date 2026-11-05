"""Provarm v0 för servoproben (prov 3). Mått i mm i fräsramen M:
x bort från Core, y längs balken, z upp, fräsaxel i x=y=0 (V1E:s Makita-STL)."""
from build123d import *
from pathlib import Path

UT = Path(__file__).parent
LED = (48.0, 35.0)          # led och servoaxel (y, z): samma axel
SPETS_Z = -20.3             # 5 mm under fräs med 30 mm utstick
PL_X = (1.0, 6.0)           # platta framför öronen; bussningar når ner i skruvursparningen
ARM_X = (7.5, 13.5)
SERVO_X = 37.0              # servots öron vilar här (mått från handelsuppgift, slits tar upp fel)
BUSS_R = 4.8               # ryms i fästets skruvursparning (mätt i CAD)
TAK_Z = 90.0                # stopp för uppfälld arm

def kloss(x, y, z):
    return Box(x[1]-x[0], y[1]-y[0], z[1]-z[0], align=Align.MIN).moved(Location((x[0], y[0], z[0])))

def hal_x(y, z, d, x0=-20, x1=70):
    return Cylinder(d/2, x1-x0, rotation=(0, 90, 0)).moved(Location(((x0+x1)/2, y, z)))

def faste():
    p = kloss(PL_X, (38.8, 58), (20, 94)) + kloss(PL_X, (38.8, 52), (94, 132))
    p += kloss((PL_X[0], SERVO_X), (36, 39), (20, 54))            # vägg mot lederna
    p += kloss((PL_X[1], SERVO_X), (38.8, 72), (TAK_Z, TAK_Z+4))      # tak och armstopp
    p += kloss((SERVO_X-4, SERVO_X), (37.5, 62), (20, TAK_Z+4))           # servoplatta
    p += kloss((6.5, 14.5), (36, 42), (19, 29))                  # sätesblock
    # V-spår i sätet: skruvskallen på armen går in här
    v = Polyline((10.5-4.5, 42.1), (10.5, 39.0), (10.5+4.5, 42.1), close=True)
    p -= extrude(Plane.XY.offset(18) * make_face(v), amount=12)
    p -= kloss((SERVO_X-5, SERVO_X+1), (LED[0]-10.3, LED[0]+10.3), (LED[1]-10.3, LED[1]+30.3))  # servohål
    for y in (43.95,):
        for z in (64.25, 125.25):
            p -= hal_x(y, z, 5.4)
    for z in (64.25, 125.25):                               # bussning ner i ursparningen
        p += Cylinder(BUSS_R, PL_X[0]+7.3, rotation=(0, 90, 0)).moved(Location(((PL_X[0]-7.3)/2, 43.95, z)))
        p -= hal_x(43.95, z, 5.4)
    p -= hal_x(LED[0], LED[1], 5.4, -20, 7)                 # ledskruv
    for dy in (-5, 5):                                      # öronhål, standardservo 49,5 x 10
        for dz in (34.75,):  # övre öronen skruvas; nedre örat vilar på plattan
            p -= kloss((SERVO_X-6, SERVO_X+2), (LED[0]+dy-1.7, LED[0]+dy+1.7), (LED[1]+dz-3.2, LED[1]+dz+3.2))
    p += kloss((ARM_X[0], ARM_X[1]), (65, 72), (TAK_Z-6, TAK_Z))  # stoppkloss: armen vilar här uppfälld
    p -= Cylinder(1.3, 8).moved(Location((18, 66, TAK_Z+2)))  # fäste för gummiband, M3
    return p

def arm():
    hub = Cylinder(8, ARM_X[1]-ARM_X[0], rotation=(0, 90, 0)).moved(Location((10.5, *LED)))
    a = hub + kloss(ARM_X, (LED[0]-5, LED[0]+5), (SPETS_Z+3, LED[1]))
    a -= hal_x(LED[0], LED[1], 5.3)
    # probspets: M3-skruv uppifrån underkant
    a -= Cylinder(1.3, 10).moved(Location((10.5, LED[0], SPETS_Z+3+5)))
    # sätesskruv: M3 mot V-spåret, gängas i från armens -y-sida
    a -= Cylinder(1.3, 8, rotation=(90, 0, 0)).moved(Location((10.5, LED[0]-1, 24)))
    # krok för gummibandet
    a += kloss(ARM_X, (LED[0]+5, LED[0]+9), (12, 16))
    return a

if __name__ == "__main__":
    f, a = faste(), arm()
    for namn, d in (("faste", f), ("arm", a)):
        export_stl(d, str(UT/f"provarm_{namn}.stl"))
        export_step(d, str(UT/f"provarm_{namn}.step"))
        bb = d.bounding_box()
        print(namn, round(d.volume/1000, 1), "cm3", bb.min, bb.max)
