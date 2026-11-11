"""Skruvprov i PETG: samma förborrade hål som i tornet, för att prova grepp och åtdragning.

Hornprovet är PLA och säger inget om PETG. Blocket har fyra Ø2,6-hål (M3), två Ø2,1-hål (M2.5)
och ett M5-distansprov Ø9,6 med Ø5,4-hål. Hålen ritas med samma mått som sidotorn.py använder.
Kör: python skruvprov.py --ut print/skruvprov-petg
"""
import argparse
import hashlib
import json
from pathlib import Path

from build123d import Box, Cylinder, Pos, export_stl

import sidotorn as S


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--ut", type=Path, required=True)
    ns = a.parse_args()
    b = Pos(0, 0, 6) * Box(60, 16, 12)
    for i, x in enumerate((-24, -16, -8, 0)):
        b -= Pos(x, 0, 12 - 4.5) * Cylinder(S.SERVO_PILOT / 2, 9.2)
    for x in (8, 15):
        b -= Pos(x, 0, 12 - 4.5) * Cylinder(2.1 / 2, 9.2)
    b += Pos(24, 0, 12 + 4.25) * Cylinder(9.6 / 2, 8.5)
    b -= Pos(24, 0, 10) * Cylinder(5.4 / 2, 30)
    ns.ut.mkdir(parents=True, exist_ok=True)
    f = ns.ut / "skruvprov.stl"
    export_stl(b, str(f))
    (ns.ut / "manifest.json").write_text(json.dumps({"typ": "skruvprov-petg", "kallor_sha256": {
        n: hashlib.sha256((Path(__file__).parent / n).read_bytes()).hexdigest() for n in ("skruvprov.py", "sidotorn.py")},
        "delar": {f.name: hashlib.sha256(f.read_bytes()).hexdigest()}}, indent=2) + "\n")
    print("skrev", f)


if __name__ == "__main__":
    main()
