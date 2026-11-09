"""LowRider V4 – modulär sensorbärare, byggd i samma build123d som arm C.

Detta är teknisk konstruktions-CAD, inte en monterad/validerad CNC-del.
Geometri i fräsens M-ram: X ut från Core, Y längs balken, Z upp.
Två ENDA maskinankare från befintliga fallarm C, inga nya Core-hål.

Delarna är fysiskt separerade:
rygg, kabellock, servokassett, BLTouch-arm, kamerakassett,
Pi-kassett, Pi-lock, Pi-dock, accelerometerfäste, mikrofonfäste.
Byte av servo ska inte lossa kamera eller Pi från ryggen.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

from build123d import Axis, Compound, Plane, Polygon, Pos, Rot, extrude, export_step, export_stl

HERE = Path(__file__).resolve().parent
NOLL = HERE.parent / "nollpunkt"
sys.path.insert(0, str(NOLL))
import fallarm_c as C
from fallarm import cy, cx, cz, k, staf, prisma_yz, prisma_xz

# Alla punkter är medvetet dokumenterade. V1E / verktygsfästet:
CORE_SKRUVAR = ((43.95, 64.25), (43.95, 125.25))  # (Y,Z), M5 i X-led
DOCKAR = {
    "servo": ((62.0, 68.0), (62.0, 86.0)),
    "kamera": ((62.0, 107.0), (62.0, 125.0)),
    "pi": ((62.0, 145.0), (62.0, 160.0)),
}
SENSOR_BULTAR = {
    "accel": ((43.5, 91.0), (43.5, 105.0)),
    "mikrofon": ((43.5, 144.0), (43.5, 158.0)),
}
KLIPP_SKRUVAR = ((48.2, 80.0), (48.2, 153.0))

@dataclass(frozen=True)
class Param:
    rygg_x0: float = 1.0
    rygg_x1: float = 9.0
    pi_x: float = 53.0
    pi_y: float = 20.0
    pi_z: float = 135.0
    kamera_x: float = 86.0
    kamera_y: float = 14.0
    kamera_z: float = 110.0  # plattans UNDERSIDA, lins i -Z
    bl_hole_spacing: float = 18.0  # BLTouch-tillverkar-/leveranskontroll
    bl_tip_from_flange: float = 45.7  # utfälld spets enligt ANTCLABS-ritning, kontrollmät före drift
    bl_tip_z: float = -39.3  # tidigare C-designmål, ej fysisk verifiering
    cable_width_mm: float = 6.0
    cable_depth_mm: float = 3.0

    def validate(self):
        if not all(math.isfinite(v) for v in asdict(self).values()):
            raise ValueError("icke-ändliga CAD-mått")
        if not 4 <= self.cable_width_mm <= 8 or not 2 <= self.cable_depth_mm <= 4:
            raise ValueError("orimlig kabelkanal")
        if self.rygg_x1-self.rygg_x0 < self.cable_depth_mm + 3:
            raise ValueError("kabelspår lämnar för tunn rygg")


def _fasad_xy(x0, x1, y0, y1, z0, z1, fas=4.0):
    poly = Plane.XY * Polygon(
        (x0+fas, y0), (x1-fas, y0), (x1, y0+fas),
        (x1, y1-fas), (x1-fas, y1), (x0+fas, y1),
        (x0, y1-fas), (x0, y0+fas), align=None,
    )
    return Pos(0,0,z0) * extrude(poly, amount=z1-z0, dir=(0,0,1))


def rygg(d: Param = Param()):
    """Bärande facetterad platta, två BEFINTLIGA M5 + M3-moduldockor.

    Försänkt kabelstam på utsidan (+X), täcks med en separat kåpa.
    Inga sensorers kabel kräver demontering av maskinankarna.
    """
    d.validate()
    form = [
        (39,52), (65,52), (73,60), (73,159),
        (63,169), (47,169), (39,161),
    ]
    s = prisma_yz(form, d.rygg_x0, d.rygg_x1)
    # Två V1E-inspirerade förstärkningsribbor ligger i basens solid,
    # före borrning av alla skruv-/servicedockhål.
    s += prisma_yz([(63,139),(70,139),(70,153),(63,161)],
                   d.rygg_x1-1.0,d.rygg_x1+1.5)
    # Existerande M5-hål på C-modellens mätta CAD-hålbild.
    for y,z in CORE_SKRUVAR:
        s -= cx(d.rygg_x0-1,d.rygg_x1+1,y,z,5.4)
    for pair in DOCKAR.values():
        for y,z in pair:
            s -= cx(d.rygg_x0-1,d.rygg_x1+1,y,z,3.4)
    for pair in SENSOR_BULTAR.values():
        for y,z in pair:
            s -= cx(d.rygg_x0-1,d.rygg_x1+1,y,z,2.6)
    # Kabelstam 6×3mm. Alltid öppningsbar från utsidan, utan demonterat servo.
    y0 = 52.8-d.cable_width_mm/2
    y1 = 52.8+d.cable_width_mm/2
    x0 = d.rygg_x1-d.cable_depth_mm
    s -= k((x0,d.rygg_x1+1),(y0,y1),(75,165))
    # Tre korta öppna förgreningar till servicekontakter, INTE frästa i Core.
    for z in (95,134,165):
        s -= k((x0,d.rygg_x1+1),(y1,67),(z-2.5,z+2.5))
    # Skruvar för löstagbart kabellock – skilda från kabelspår och M5-ankare.
    for y,z in KLIPP_SKRUVAR:
        s -= cx(3.0, d.rygg_x1+1,y,z,2.4)
    return s


def kabellock(d: Param = Param()):
    """Löstagbart lock över huvudkabeln, inte snäpphakar som kan lossna av vibration."""
    s = prisma_yz(
        [(46.0,73),(54.2,73),(56.0,76),(56.0,164),
         (54.2,167),(46.0,167)],
        d.rygg_x1+0.35, d.rygg_x1+2.6,
    )
    for y,z in KLIPP_SKRUVAR:
        s -= cx(d.rygg_x1, d.rygg_x1+4,y,z,2.9)
    # Avlångt utlopp på framsidan, lätt att inspektera för dragavlastning.
    for z in (95,134,164):
        s -= k((d.rygg_x1, d.rygg_x1+4),(54.0,57.0),(z-2.8,z+2.8))
    return s


def _dock(modul: str, z0: float, z1: float):
    """Serva modul utan att lossa ryggens M5 mot Core."""
    p = prisma_yz(
        [(56.5,z0),(68,z0),(70,z0+2),(70,z1-2),(68,z1),(56.5,z1)],
        10.0, 16.0,
    )
    for y,z in DOCKAR[modul]:
        p -= cx(9,17,y,z,3.5)
    return p


def servokassett():
    """Direktdriven servo C, men som separat demonterbar kassett på ryggen."""
    px,pz=C.PX,C.PZ
    s = _dock("servo",59,94)
    # Materialflöde från dock -> servo och ett urtaget, lågt C-fönster.
    s += prisma_xz([(15,60),(24,60),(45,56),(45,61),(15,83)],
                   57,64)
    s += k((20,30),(44,62),(57,64))
    ram = k((10,67),(43.3,49.3),(27.6,61.6))
    ram -= k((14.8,55.2),(42.3,50.3),(33.4,53.8))
    s += ram
    for z in (pz-4.7,pz+4.7):
        for x in (px-33.3,px+14):
            s -= k((x-1.7,x+1.7),(42.3,50.3),(z-1.7,z+1.7))
    return s


def bltouch_arm(d: Param = Param()):
    """Ny lös BLTouch-arm i C:s servoaxel – ersätter Ø33-cylinderklämman.

    Körförbud till mekanisk stoppläges- och stift/verktygs-kollision är verifierade.
    """
    px,pz=C.PX,C.PZ
    x,y=C.XC,C.YC
    flange_z=d.bl_tip_z+d.bl_tip_from_flange
    y0,y1=C.Y_TOPP-11.1,C.Y_TOPP-7.1
    s = cy(y0,y1,px,pz,18)
    s += staf(px,pz,18,x,flange_z+3,12,y0,y1,False)
    s += k((x-13,x+13),(y-16,y+16),(flange_z,flange_z+4.5))
    # Lätta klämbasen; bevara servohornets ursprungliga två hål.
    for z in (pz-7,pz+7):
        s -= cy(y0-1,y1+1,px,z,2.4)
    s -= cy(y0-1,y1+1,px,pz,7.5)
    # Hålen vrids 90° runt BLTouch-Z för att skruvskallarna inte ska
    # hamna under armens stag. Tillverkarens 18 mm c-c är bevarade.
    for xx in (x-d.bl_hole_spacing/2,x+d.bl_hole_spacing/2):
        s -= cz(flange_z-1,flange_z+15,xx,y,3.4)
    s -= cz(flange_z-1,flange_z+6,x,y,10)
    # Två fria kabelbindarplatser nära armen, men ingen okänd pinout antagen.
    for z in (flange_z+8,flange_z+13):
        s -= cy(y0-1,y1+1,px+9,z,2.6)
    return s


def kamerakassett(d: Param = Param()):
    """Separat styv/facetterad L-fackverkskassett. Ingen montering på servot."""
    x,y,z=d.kamera_x,d.kamera_y,d.kamera_z
    s = _dock("kamera",97,133)
    # Två 7mm-stag, med triangulära sidoförstärkningar utan dold stödstruktur.
    s += k((14,x),(58,65),(116,123))
    s += prisma_xz([(16,107),(x-5,107),(x-5,116),(16,127)],59,62)
    # Stödet börjar BAKOM kamerakortets 24 mm: ingen ribba över optiken.
    s += k((x-4,x+4),(y+14,65),(z+1,z+11))
    s += prisma_yz([(y+18,z+3),(61,z+3),(61,z+15)],x-3,x+3)
    s += _fasad_xy(x-17,x+17,y-17,y+17,z,z+3,fas=4)
    # Camera Module 3 Standard / Module 2 skruvcentrum (21 x 12,5 mm).
    for dx in (-10.5,10.5):
        for dy in (-6.25,6.25):
            s -= cz(z-1,z+4,x+dx,y+dy,2.35)
    s -= cz(z-1,z+4,x,y,15.0)
    # Två små M3-hål för EVENTUELL framtida LED, LED monteras inte nu.
    for dx in (-14,14):
        s -= cz(z-1,z+4,x+dx,y+10,2.5)
    return s


def pi_lada():
    """Pi Zero 2 WH utan fläkt, stängd mot spån och med servislock."""
    w,h=80,46
    s=_fasad_xy(-w/2,w/2,-h/2,h/2,0,22,fas=5)
    # Håligheten måste ligga INNANFÖR de 5 mm fasade hörnen.
    # Gammalt mått +2,5 gav exakt tangerande inner/ytterhörn och öppet STL.
    s-=k((-w/2+4,w/2-4),(-h/2+4,h/2-4),(2.5,23))
    # Fyra originalmontage M2.5 (58 x 23) och separat skruvat lock.
    for xx in (-29,29):
        for yy in (-11.5,11.5):
            # Pelaren måste överlappa botten (0..2,5 mm), annars ger
            # enbart tangerande kontaktyta öppen STL vid triangulering.
            s+=cz(1.7,7,xx,yy,6.0)
            s-=cz(2.5,8,xx,yy,2.7)
    for xx in (-35.25,35.25):
        for yy in (-18.5,18.5):
            s+=cz(2.5,22,xx,yy,6.0)
            s-=cz(13,23,xx,yy,2.6)
    # Utbytbar Pi utan att lossa Core-M5: fästöglor i Y+ sida.
    for xx in (-22,-7):
        s+=k((xx-5,xx+5),(22,32),(0,4))
        s-=cz(-1,5,xx,27,3.4)
    # Ett kabelgenomföringsfönster mot Core, kan dammtätas med mjuk grommet.
    s-=k((-25,-3),(21,24),(8,16))
    return s


def pi_lock():
    w,h=80,46
    s=_fasad_xy(-w/2,w/2,-h/2,h/2,0,2.5,fas=5)
    # Lockets distanskrage för sidledsstabilitet.
    s+=k((-w/2+4.5,w/2-4.5),(-h/2+4.5,h/2-4.5),(2.5,4.0))
    s-=k((-w/2+6.5,w/2-6.5),(-h/2+6.5,h/2-6.5),(2.4,5))
    for xx in (-35.25,35.25):
        for yy in (-18.5,18.5):
            s-=cz(-1,5,xx,yy,3.0)
    return s


def pi_dock():
    """Servicemodul mellan ryggradens PI-port och lådans två M3-öron."""
    s=_dock("pi",137,168)
    s+=prisma_xz([(15,141),(25,141),(40,133),(40,138),(15,158)],59,65)
    # Dockens ovansida Z=135 ligger dikt an Pi-lådans fästöron Z=135.
    # Inget överlapp mellan de olika utskrivna modulernas solider.
    s+=k((22,51),(42,64),(129,135))
    for xx in (53-22,53-7):
        s-=cz(128,136,xx,47,3.4)
    return s


def sensorbricka(typ: str):
    """Två utbytbara M2.5-fästen; inga okända PCB-hål föreskrivs."""
    if typ not in SENSOR_BULTAR:
        raise ValueError(typ)
    z = 98 if typ=="accel" else 151
    s=prisma_yz([(36,z-11),(50,z-11),(53,z-8),
                  (53,z+8),(50,z+11),(36,z+11)],10,14)
    for y,z0 in SENSOR_BULTAR[typ]:
        s-=cx(9,16,y,z0,2.7)
    if typ=="mikrofon":
        # Akustiskt hål i utbytbar kåpa, plats för servicemembran.
        s-=cx(9,16,47,z,3.0)
    else:
        # Klämfickor för liten ADXL-breakout (kortmått kontrolleras vid leverans).
        for zz in (z-5,z+5):
            s-=k((10.5,15),(47,50),(zz-1.3,zz+1.3))
    return s


def delar(d: Param=Param()):
    return {
        "rygg":rygg(d),"kabellock":kabellock(d),
        "servokassett":servokassett(),"bltouch_arm":bltouch_arm(d),
        "kamerakassett":kamerakassett(d),
        "pi_lada":pi_lada(),"pi_lock":pi_lock(),"pi_dock":pi_dock(),
        "accel_bricka":sensorbricka("accel"),
        "mikrofon_bricka":sensorbricka("mikrofon"),
    }


def rapport(d: Param=Param()):
    """Metadata/kontrakt: placering är CAD-antaganden, inte kollisionsbevis."""
    units=delar(d)
    out={"schema":1,"status":"konstruktionsstudie, ej fysisk krockverifiering",
         "ankare_m5_yz_mm":CORE_SKRUVAR,"moduldockar_m3_yz_mm":DOCKAR,
         "sensor_dockar_m2_5_yz_mm":SENSOR_BULTAR,
         "cable_trunk":{"y_center_mm":52.8,"z_mm":[75,165],
                        "width_mm":d.cable_width_mm,"depth_mm":d.cable_depth_mm,
                        "cover_screws_yz_mm":KLIPP_SKRUVAR,
                        "servo_service_loop":"krävs, EJ dimensionerad"},
         "parametrar":asdict(d),
         "moduler":{}}
    for name,part in units.items():
        if not hasattr(part, "bounding_box"):
            raise ValueError(f"{name}: CAD-resultat {type(part).__name__}, "
                             f"{len(part) if hasattr(part, '__len__') else '?'} "
                             "separata/ogiltiga kroppar före export")
        bounds=part.bounding_box()
        out["moduler"][name]={"valid":bool(part.is_valid),
                "volym_cm3":round(part.volume/1000,2),
                "bbox_min_mm":[round(v,1) for v in bounds.min],
                "bbox_max_mm":[round(v,1) for v in bounds.max],
                "solider":len(part.solids())}
    return out


def exportera(path: Path, *, typ: str="stl", d: Param=Param()):
    path.mkdir(parents=True,exist_ok=True)
    report=rapport(d)
    for name,part in delar(d).items():
        if not part.is_valid or len(part.solids()) != 1:
            raise ValueError(f"{name}: ogiltig CAD eller flera separata kroppar")
        if typ=="step":
            export_step(part,str(path/f"{name}.step"))
        else:
            export_stl(part,str(path/f"{name}.stl"),tolerance=.05,angular_tolerance=.2)
    (path/"manifest.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf8")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--ut",type=Path,required=True)
    parser.add_argument("--format",choices=("stl","step"),default="stl")
    args=parser.parse_args()
    exportera(args.ut,typ=args.format)
    print(json.dumps(rapport(),ensure_ascii=False,indent=2))
