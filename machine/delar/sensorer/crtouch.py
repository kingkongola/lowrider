"""CR Touch-referens och passningsparametrar för sidotornet.

Geometri från Jonathan Harpers E34M1, CC BY-NC-SA 4.0, se referenser/README.md.
Måtten är CAD-referensmått, inte mätningar på användarens exemplar.
Origo: mitt mellan fästhålen på flänsens ovansida. Stiftet går i -Z.
Proben vrids så att kontakt/kropp ligger bort från armens rygg (+Y).
"""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from build123d import Pos, Rot, import_step

REFERENS = Path(__file__).parent / "referenser/e34m1-crtouch.step"
HAL_CC = 18.0
FLANS_T = 1.9
KROPP_DJUP = 37.0
STIFT_UTFALLT = 46.0  # konservativt referensläge; Creality anger 39,3 mm yttermått och 6 mm slag
STIFT_Y = 2.25
KONTAKT_B = 12.0      # konstruktionskuvert, inte uppmätt kontakt
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
