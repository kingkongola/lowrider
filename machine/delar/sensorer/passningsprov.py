"""Små passningsprov hämtade ur aktuell sidotornsgeometri.

Kameraprovet kontrollerar kortficka, styrtappar och kontaktutrymme.
Det ersätter inte prov av tornets infästning, kabelväg eller belysning.
Kör: uv run --offline --no-project --python 3.12 --with build123d==0.13.0 \
    python machine/delar/sensorer/passningsprov.py --ut print/sensor-passning
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import build123d
from build123d import Pos, Rot, export_stl

import sidotorn as cad


def pa_badden(del_):
    bb = del_.bounding_box()
    return Pos(-bb.min.X, -bb.min.Y, -bb.min.Z) * del_


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ut", type=Path, required=True)
    a = ap.parse_args()
    a.ut.mkdir(parents=True, exist_ok=True)

    # Behåll själva kamerafickan ur tornet. Den avkapade ovansidan ligger
    # mot bädden; inga nya toleranser eller hål läggs till i provet.
    kamera = cad.torn() & cad.box(
        (77.5, 33.0, cad.BUK), (cad.XEND, 69.0, cad.KORT_TAK + 3.0)
    )
    delar = {
        "kamera-passning.stl": pa_badden(Rot(180, 0, 0) * kamera),
        "bricka.stl": pa_badden(cad.bricka()),
    }
    kallor = [Path(cad.__file__), Path(__file__)]
    manifest = {
        "build123d": build123d.__version__,
        "kallor_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in kallor},
        "delar": {},
    }
    for namn, del_ in delar.items():
        if not del_.is_valid or len(del_.solids()) != 1:
            raise ValueError(f"{namn}: ogiltig eller delad CAD-kropp")
        fil = a.ut / namn
        export_stl(del_, fil, tolerance=0.01, angular_tolerance=0.1)
        bb = del_.bounding_box()
        manifest["delar"][namn] = {
            "sha256": hashlib.sha256(fil.read_bytes()).hexdigest(),
            "mm": [round(v, 3) for v in bb.size],
            "volym_mm3": round(del_.volume, 3),
        }
    (a.ut / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
