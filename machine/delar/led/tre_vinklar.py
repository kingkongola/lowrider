"""LowRider V4: tre LED-banor under den HORISONTELLA bottom strut plate.

Parametrisk provmodell, inte verifierad på fysisk maskin.
X = längs balken, Y = tvärs balken (framåt = +Y), Z = upp.
Undre strutplattans undersida ligger vid z=0; dess plan är XY.

Fästet monteras med två BEFINTLIGA M5-skruvpositioner i den undre
strutplattan, 56 mm centrumavstånd i Y enligt repo/strut_plate.svg.
Konstruktionen får inte ändra låsning eller justering av original-Brace.

3 × 8 mm COB-banor: 0°, 25°, 50° nedåt/framåt; ändringsbara.
Modullängd 154 mm; originalets brace-/hålpitch är 160.2 mm längs X.

Kör:
    python machine/delar/led/tre_vinklar.py --ut export/led
    python machine/delar/led/tre_vinklar.py --vinklar 0 20 45 --led-bredd 8.2
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

from build123d import Box, Cylinder, Pos, Rot, export_stl, export_step


@dataclass(frozen=True)
class Param:
    led_bredd: float = 8.0
    led_marginal: float = 1.0
    led_vinklar: tuple[float, float, float] = (0.0, 25.0, 50.0)
    led_ys: tuple[float, float, float] = (-16.0, 0.0, 17.0)
    led_zs: tuple[float, float, float] = (-13.5, -15.0, -16.5)
    framat: int = 1                # +1 eller -1: vrid/spegla mot verklig framsida
    segment_langd: float = 154.0   # kortare än brace-pitch; 6.2 mm springa
    brace_pitch: float = 160.2
    # Originalbottenplattans skruvar, två rader 56 mm från varandra:
    skruv_pitch_y: float = 56.0
    skruv_haldia: float = 5.4       # M5 genomgång (inte gängat i PETG)
    bottenplattans_bredd_y: float = 78.3   # nominellt från SVG, EJ uppmätt montage
    bas_bredd_x: float = 18.0
    bas_langd_y: float = 78.0
    bas_tjocklek_z: float = 3.0
    rygg_bredd: float = 3.2        # längsgående stabiliseringsribba ovanför LED
    rygg_hojd: float = 4.0
    hyll_tjocklek: float = 2.4
    stolpe_bredd_x: float = 18.0
    stolpe_bredd_y: float = 4.0


def bygg(p: Param):
    if p.framat not in (-1, 1):
        raise ValueError("framat måste vara +1 eller -1")
    if p.segment_langd <= p.bas_bredd_x:
        raise ValueError("Segmentet är för kort")
    if p.skruv_pitch_y + p.skruv_haldia >= p.bas_langd_y:
        raise ValueError("Skruvhålen ryms inte på basplattan")

    # Den verkliga bottenstrutplattan ligger HORISONTELLT i XY.
    # Detta är en separat adapter UNDER plattan, inte en klämma
    # på den vertikala frontstrutens kant.
    f = Pos(0, 0, -p.bas_tjocklek_z / 2) * Box(
        p.bas_bredd_x, p.bas_langd_y, p.bas_tjocklek_z
    )

    for y0, z0, angle in zip(p.led_ys, p.led_zs, p.led_vinklar):
        # LED med sin självhäftande rygg mot hyllans NEDRE yta.
        # Stabiliseringen (rygg) ligger ovanför, så att ljuset inte
        # blockeras av en kontinuerlig ribba under själva LED-listen.
        rail = Box(p.segment_langd,
                   p.led_bredd + 2*p.led_marginal,
                   p.hyll_tjocklek)
        rail += Pos(0, 0, 2.5) * Box(
            p.segment_langd, p.rygg_bredd, p.rygg_hojd
        )
        f += Pos(0, p.framat*y0, z0) * Rot(X=p.framat*angle) * rail

        # En kort pelare från understruten ned mot skenans rygg.
        # Pelaren har inte full segmentlängd; LED-riktningen
        # bestäms av den långa lutande hyllan, inte av skruven.
        ztop = -2.5
        zbot = z0 - 0.4
        height = ztop - zbot
        if height <= 0:
            raise ValueError("LED-hyllan måste ligga under basen")
        f += Pos(0, p.framat*y0, (ztop+zbot)/2) * Box(
            p.stolpe_bredd_x, p.stolpe_bredd_y, height
        )

    # Två redan existerande M5-stationer på samma Brace.
    # Undersök aktuell skruvlängd/skalle innan skruvarna lossas;
    # fästet tillför bas_tjocklek_z i gripmåttet.
    for y in (-p.skruv_pitch_y/2, p.skruv_pitch_y/2):
        f -= Pos(0, y, -1.5) * Cylinder(
            p.skruv_haldia/2, p.bas_tjocklek_z+5.0
        )
    return f


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--ut", type=Path, default=Path("export/led"))
    a.add_argument("--led-bredd", type=float, default=8.0)
    a.add_argument("--vinklar", nargs=3, type=float, default=(0,25,50))
    a.add_argument("--fram-sida", choices=(-1,1), type=int, default=1)
    a.add_argument("--m5-pitch", type=float, default=56.0)
    a.add_argument("--segment-langd", type=float, default=154.0)
    ns = a.parse_args()
    p = Param(led_bredd=ns.led_bredd,
              led_vinklar=tuple(ns.vinklar),
              framat=ns.fram_sida,
              skruv_pitch_y=ns.m5_pitch,
              segment_langd=ns.segment_langd)
    body = bygg(p)
    ns.ut.mkdir(parents=True, exist_ok=True)
    export_stl(body, str(ns.ut/"led_3vinklar.stl"))
    export_step(body, str(ns.ut/"led_3vinklar.step"))
    print("Fäste för horisontell understrut:",
          p.led_bredd, "mm LED, vinklar", p.led_vinklar,
          "M5 pitch", p.skruv_pitch_y, "mm",
          "längd", p.segment_langd, "mm")


if __name__ == "__main__":
    main()
