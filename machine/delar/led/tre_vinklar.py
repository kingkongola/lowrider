"""LowRider V4 – lågprofilsfäste för tre BRIMETI 8 mm COB-lister.

VIKTIGT: bottenstrutten är HORISONTELL. Dess undersida definierar z=0.
X längs balken, Y mot maskinens framkant när framat=+1, Z upp.
Befintliga M5/Brace-hål c/c 56 mm enligt strut_plate.svg används.

Utformningskrav: MINIMERA INTRÅNG I MASKINENS Z. De gamla 13–17 mm
låga LED-hyllorna på pelare är ersatta av tunna ytor direkt mot plattan.
KODEN AVVISAR geometrier som överskrider max_z_intrang_mm. Angivna
vinklar 0/15/25 grader är valda för att hålla den teoretiska tjockleken
under 6.2 mm. Äldre 0/25/50-grader var endast provvärden; 50 grader
kan ge runt 9 mm intrång med samma 10 mm breda hylla.

STILL NOT DRIFT-VERIFIED: physical brace clearance, M5 bolt length,
LED temperature, cable passage, and fully assembled XYZ sweep.
Inga nya borrhål eller kabelgenomföringar ingår i denna CAD.

Kör:
  python machine/delar/led/tre_vinklar.py --ut export/led
  python machine/delar/led/tre_vinklar.py --vinklar 0 10 20
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import cos, radians, sin
from pathlib import Path

from build123d import Axis, Box, Cylinder, Pos, Rot, chamfer, fillet, export_step, export_stl


@dataclass(frozen=True)
class Param:
    led_bredd: float = 8.0
    led_marginal: float = 1.0       # 10 mm brett fäste; ger 8 mm plan LED-yta
    vinklar: tuple[float, float, float] = (0.0, 15.0, 25.0)
    led_ys: tuple[float, float, float] = (-16.0, 0.0, 16.0)
    framat: int = 1                # +1 eller -1 beroende på monteringssida
    segment_langd: float = 154.0
    brace_pitch: float = 160.2
    skruv_pitch_y: float = 56.0
    skruv_haldia: float = 5.4
    bas_bredd_x: float = 16.0
    bas_langd_y: float = 76.0
    bas_webb_tjocklek: float = 1.0
    boss_bredd_y: float = 12.0
    boss_tjocklek: float = 2.2
    led_hylla_tjocklek: float = 1.6
    led_toppfrigang: float = 0.15
    max_z_intrang_mm: float = 6.2
    bas_hornradie: float = 0.7
    boss_hornradie: float = 0.6
    hylla_hornradie: float = 1.2
    hylla_kantfas: float = 0.2


def teoretiskt_intrang(p: Param) -> float:
    """Övre gräns nedanför z=0 inklusive hörn på oavrundad LED-hylla."""
    w = p.led_bredd + 2 * p.led_marginal
    return max(
        p.led_toppfrigang + w * sin(radians(abs(v))) +
        p.led_hylla_tjocklek * cos(radians(abs(v)))
        for v in p.vinklar
    )


def validera(p: Param) -> None:
    if p.framat not in (-1, 1):
        raise ValueError("framat måste vara 1 eller -1")
    if len(p.vinklar) != 3 or len(p.led_ys) != 3:
        raise ValueError("Exakt tre LED-banor krävs")
    if any(v < 0 or v > 80 for v in p.vinklar):
        raise ValueError("LED-vinklar måste ligga mellan 0° och 80°")
    if p.led_bredd <= 0 or p.led_marginal < 0:
        raise ValueError("Ogiltig LED-bredd/marginal")
    if p.segment_langd <= p.bas_bredd_x:
        raise ValueError("Segmentet måste vara längre än tvärfästet")
    if p.boss_tjocklek <= p.bas_webb_tjocklek or p.bas_webb_tjocklek <= 0:
        raise ValueError("Boss ska vara tjockare än webb")
    if p.skruv_pitch_y + p.skruv_haldia >= p.bas_langd_y:
        raise ValueError("M5-hålen får inte plats på tvärfästet")
    if any(abs(y) + (p.led_bredd + 2 * p.led_marginal) / 2 >=
           p.skruv_pitch_y / 2 - p.boss_bredd_y / 2
           for y in p.led_ys):
        raise ValueError("LED-ytan inkräktar på M5-bossarna")
    z = max(teoretiskt_intrang(p), p.boss_tjocklek)
    if z > p.max_z_intrang_mm + 1e-6:
        raise ValueError(
            f"Z-intrång {z:.2f} mm > tillåtet {p.max_z_intrang_mm:.2f} mm. "
            "Minska vinklar/bredd eller ändra uttryckligen Z-budgeten."
        )


def bygg(p: Param):
    validera(p)
    # En tunn lokal tvärwebb plus små förstärkningar just vid de två M5-hålen.
    # Ingen 3 mm tjock hel bas och inga distanspelare.
    web = Box(p.bas_bredd_x, p.bas_langd_y, p.bas_webb_tjocklek)
    web = fillet(web.edges().filter_by(Axis.Z), radius=p.bas_hornradie)
    out = Pos(0, 0, -p.bas_webb_tjocklek / 2) * web

    for y in (-p.skruv_pitch_y / 2, p.skruv_pitch_y / 2):
        boss = Box(p.bas_bredd_x, p.boss_bredd_y, p.boss_tjocklek)
        boss = fillet(boss.edges().filter_by(Axis.Z), radius=p.boss_hornradie)
        out += Pos(0, y, -p.boss_tjocklek / 2) * boss

    # Lysytan sitter på en tunn hyllas UNDERSIDA. För varje vinkel sätts
    # hyllans högsta punkt 0.15 mm under z=0; ingen del ska sticka in i plattan.
    w = p.led_bredd + 2 * p.led_marginal
    t = p.led_hylla_tjocklek
    for y, angle in zip(p.led_ys, p.vinklar):
        v = radians(abs(angle))
        z = -(p.led_toppfrigang + w / 2 * sin(v) + t / 2 * cos(v))
        rail = Box(p.segment_langd, w, t)
        rail = fillet(rail.edges().filter_by(Axis.Z), radius=p.hylla_hornradie)
        rail = chamfer(rail.edges().filter_by(Axis.X), length=p.hylla_kantfas)
        out += Pos(0, p.framat * y, z) * Rot(X=p.framat * angle) * rail

    for y in (-p.skruv_pitch_y / 2, p.skruv_pitch_y / 2):
        out -= Pos(0, y, -1.0) * Cylinder(
            p.skruv_haldia / 2, p.boss_tjocklek + 5.0
        )
    return out


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--ut", type=Path, default=Path("export/led"))
    a.add_argument("--led-bredd", type=float, default=8.0)
    a.add_argument("--vinklar", nargs=3, type=float, default=(0, 15, 25))
    a.add_argument("--fram-sida", choices=(-1, 1), type=int, default=1)
    a.add_argument("--m5-pitch", type=float, default=56.0)
    a.add_argument("--segment-langd", type=float, default=154.0)
    a.add_argument("--max-z-intrang", type=float, default=6.2)
    ns = a.parse_args()
    p = Param(
        led_bredd=ns.led_bredd, vinklar=tuple(ns.vinklar),
        framat=ns.fram_sida, skruv_pitch_y=ns.m5_pitch,
        segment_langd=ns.segment_langd, max_z_intrang_mm=ns.max_z_intrang
    )
    body = bygg(p)
    ns.ut.mkdir(parents=True, exist_ok=True)
    export_stl(body, str(ns.ut / "led_3vinklar.stl"))
    export_step(body, str(ns.ut / "led_3vinklar.step"))
    bb = body.bounding_box()
    assert bb.min.Z >= -p.max_z_intrang_mm - 1e-4, bb.min.Z
    assert bb.max.Z <= 1e-4, bb.max.Z
    print(
        f"LowRider LED lågprofil: vinklar={p.vinklar}, "
        f"teoretiskt Z-intrång={teoretiskt_intrang(p):.2f} mm, "
        f"verkligt CAD-intrång={-bb.min.Z:.2f} mm, "
        f"Z-tak={p.max_z_intrang_mm:.2f} mm"
    )


if __name__ == "__main__":
    main()
