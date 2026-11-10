"""Parametriskt fäste med tre LED-ytor, direkt på LowRider V4 strutkant.

Status 2026-11-10: CAD-prototyp, inte fysiskt mätt/printad/termiskt verifierad.
X längs balken; Y framåt; Z upp. Strutens nederkant har z=0,
strutskivan är lodrät och fortsätter uppåt (z>0).

Använder inga originalskruvhål. Två klämmor med M3 på varje modul.
Kör: python machine/delar/led/tre_vinklar.py --ut export/led
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from pathlib import Path
from build123d import Box, Cylinder, Pos, Rot, export_stl, export_step


@dataclass(frozen=True)
class Param:
    led_bredd: float = 8.0
    marginal: float = 1.0             # mm på varje sida av COB
    strut_tjocklek: float = 6.0       # ändra vid annan MDF-tjocklek
    strut_spel: float = 0.4
    langd: float = 155.0             # en modul i varje strut-fack
    modul_pitch: float = 160.2       # uppmätt från repo: strut_plate.svg
    startcentrum_x: float = 89.1     # raka underkanten i första facket
    antal: int = 5                  # printa 5 för ca 795 mm längd
    stodbalk_bredd_x: float = 16.0
    stod_offset_x: float = 54.0     # klämmor inom raka strutkanten
    klamvagg: float = 3.5
    m3_haldia: float = 2.7          # prov för M3 gängning i PETG
    fram_sida: int = 1              # +1 eller -1 speglar belysningen
    vinklar: tuple[float,float,float] = (0.0,25.0,50.0)
    hyllor: tuple[tuple[float,float], ...] = ((-16.0,-15.5),(1.0,-17.0),(18.0,-18.5))


def bygga(p: Param):
    assert p.fram_sida in (-1,1)
    assert p.langd > 2*(p.stod_offset_x + p.stodbalk_bredd_x/2)
    assert len(p.vinklar) == len(p.hyllor) == 3
    assert p.led_bredd > 0 and p.strut_tjocklek > 0
    delar = []
    # Kontinuerligt stöd under självhäftande 8 mm LED i varje 155-mm-modul.
    for (y,z),v in zip(p.hyllor,p.vinklar):
        delar.append(
            Pos(0,p.fram_sida*y,z) * Rot(X=p.fram_sida*v)
            * Box(p.langd,p.led_bredd + 2*p.marginal,2.0)
        )
    for x in (-p.stod_offset_x,p.stod_offset_x):
        s = Pos(x,0,-5) * Box(p.stodbalk_bredd_x,50,5)
        for y,_ in p.hyllor:
            s += Pos(x,p.fram_sida*y,-12) * Box(p.stodbalk_bredd_x,3.2,15)
        cuff_w = p.strut_tjocklek + p.strut_spel + 2*p.klamvagg
        cuff = Pos(x,0,5) * Box(p.stodbalk_bredd_x,cuff_w,16)
        cuff -= Pos(x,0,7) * Box(p.stodbalk_bredd_x+0.2,
                                  p.strut_tjocklek+p.strut_spel,16)
        # Från samma sida: 2,7-mm hål i plast för M3 klämskruv.
        hole_len = 7.0
        screw_center_y = cuff_w/2 + 0.5 - hole_len/2
        cuff -= Pos(x,screw_center_y,8) * Rot(X=90) * Cylinder(p.m3_haldia/2,hole_len)
        s += cuff
        delar.append(s)
    out = delar[0]
    for d in delar[1:]:
        out += d
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ut",type=Path,default=Path("export/led"))
    ap.add_argument("--led-bredd",type=float,default=8.0)
    ap.add_argument("--strut-tjocklek",type=float,default=6.0)
    ap.add_argument("--vinklar",type=float,nargs=3,default=[0,25,50])
    ap.add_argument("--fram-sida",type=int,choices=(-1,1),default=1)
    ns=ap.parse_args()
    p=Param(led_bredd=ns.led_bredd,strut_tjocklek=ns.strut_tjocklek,
            vinklar=tuple(ns.vinklar),fram_sida=ns.fram_sida)
    mesh=bygga(p)
    ns.ut.mkdir(parents=True,exist_ok=True)
    export_stl(mesh,str(ns.ut/"led_3vinklar.stl"))
    export_step(mesh,str(ns.ut/"led_3vinklar.step"))
    print(f"Provmodul {p.langd} mm, tre hyllor {p.vinklar} grader; "
          f"printa {p.antal} för ca {p.modul_pitch*(p.antal-1)+p.langd} mm totalt.")


if __name__=="__main__":
    main()
