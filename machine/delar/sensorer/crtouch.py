"""CR Touch-referens och passningsparametrar för sidotornet.

Geometri från Jonathan Harpers E34M1, CC BY-NC-SA 4.0, se referenser/README.md.
Måtten är CAD-referensmått, utom de som anges som uppmätta (2026-11-11): hålavstånd 17,5, öron 1,8,
fläns 27 x 17,5, kropp 16,1 x 17,5 x 35, kontaktöppning 13,1 x 9,5. Referensens hål ligger 18 mm isär.
Origo: mitt mellan fästhålen på flänsens ovansida. Stiftet går i -Z.
Proben vrids så att kontakt/kropp ligger bort från armens rygg (+Y).
"""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from build123d import Pos, Rot, import_step

REFERENS = Path(__file__).parent / "referenser/e34m1-crtouch.step"
HAL_CC = 17.5        # uppmätt på användarens CR Touch 2026-11-11 (referensen har 18,0)
FLANS_T = 1.8        # öronens tjocklek, uppmätt 2026-11-11; stöd under öronen nära kroppen ej uppmätta
KROPP_DJUP = 37.0
STIFT_UTFALLT = 46.0  # konservativt referensläge; Creality anger 39,3 mm yttermått och 6 mm slag
STIFT_Y = 2.25
KONTAKT_B = 13.1      # kontaktöppningens bredd, uppmätt 2026-11-11 (höjd 9,5)
KONTAKT_Y = (3.5, 14.0)
KONTAKT_H = 10.0
SPEL = 0.6           # per sida runt kroppen, redan inkluderat nedan
HALKOMP_D = 0.15     # tillägg på hela diametern, enligt användarens print-erfarenhet
M3_FRITT_D = 3.25 + HALKOMP_D
M3_PILOT_D = 2.6     # gängar i plast; separat passningsprov, inte samma funktion som frigångshål


@lru_cache(maxsize=1)
def referens():
    asm = import_step(REFERENS)
    komponent = next(c for c in asm.children if c.label == "CR-Touch_Mockup_v1")
    # Hålen i källfilen: (-6,-2.618,50), (12,-2.618,50).
    return Rot(0, 0, 180) * Pos(-3, 2.618, -50) * komponent


def kropp():
    return max(referens().solids(), key=lambda s: s.volume)


def stift():
    return min(referens().solids(), key=lambda s: s.volume)


@lru_cache(maxsize=1)
def kropp_med_sidospel():
    """0,15 mm spel i X/Y för hylsans underlägg, med flänsens höjdplan bevarat."""
    k = kropp()
    return k.fuse(*(Pos(dx, dy, 0) * k for dx, dy in ((.15, 0), (-.15, 0), (0, .15), (0, -.15))))
