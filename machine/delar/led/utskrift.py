"""Exporterar LED-fästet i utskriftsläge: sidan mot understruten nedåt mot bädden.

Varför vänd: fästets ovansida (z=0) är plan och ligger mot understruten. Mot bädden blir den
slät och plan, och de lutade hyllorna byggs upp från den med kantstagen som bär dem.
Skriver STL och manifest med källans SHA-256, så att printjobbet kan knytas till CAD-källan.

Kör: python utskrift.py --ut print/led-fasten
"""
import argparse
import hashlib
import json
from pathlib import Path

import build123d
from build123d import Pos, Rot, export_stl

import tre_vinklar as tv


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--ut", type=Path, required=True)
    ns = a.parse_args()
    p = tv.Param()
    tv.validera(p)
    kropp = Rot(180, 0, 0) * tv.bygg(p)
    bb = kropp.bounding_box()
    kropp = Pos(-(bb.min.X + bb.max.X) / 2, -(bb.min.Y + bb.max.Y) / 2, -bb.min.Z) * kropp
    ns.ut.mkdir(parents=True, exist_ok=True)
    stl = ns.ut / "led-fasten.stl"
    export_stl(kropp, str(stl), tolerance=.02, angular_tolerance=.1)
    kalla = Path(tv.__file__)
    (ns.ut / "manifest.json").write_text(json.dumps({
        "typ": "led-fasten", "build123d": build123d.__version__,
        "parametrar": {"vinklar": list(p.vinklar), "led_bredd": p.led_bredd, "segment_langd": p.segment_langd},
        "kallor_sha256": {kalla.name: hashlib.sha256(kalla.read_bytes()).hexdigest()},
        "delar": {stl.name: hashlib.sha256(stl.read_bytes()).hexdigest()},
    }, ensure_ascii=False, indent=2) + "\n")
    bb = kropp.bounding_box()
    print(f"led-fasten.stl {bb.size.X:.1f} x {bb.size.Y:.1f} x {bb.size.Z:.2f} mm, {kropp.volume / 1000:.1f} cm3")


if __name__ == "__main__":
    main()
