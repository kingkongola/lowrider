"""Exporterar sidotornets slutdelar i utskriftsläge, med manifest. Orienteringen är vald med
överhängsanalys 2026-11-11 (sex axelriktningar per del, minst brant överhäng och plan anläggning).

| Del       | Läge                         | Varför |
| torn      | upp och ned, ovansidan mot bädden | ingen plan baksida finns; kamerafickan pekar uppåt utan stöd |
| sidopanel | yttersidan mot bädden        | slät utsida, fingrar och mikrofonram uppåt |
| arm       | som ritad                    | minst överhäng, lagren går längs armen |
| kapa      | upp och ned                  | flänsytan mot bädden |
| hornbygel | utsidan mot bädden           | som i passningsprovet |
| bricka    | som ritad                    | |

Läser STL från sidotorn.py:s export. Kör:
  python sidotorn.py --ut UT && python utskrift_slutdelar.py --fran UT --ut print/sidotorn-slutdelar
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import trimesh

LAGE = {"torn": ([1, 0, 0], 180), "sidopanel": ([1, 0, 0], -90), "arm": ([1, 0, 0], 0),
        "kapa": ([1, 0, 0], 180), "hornbygel": ([1, 0, 0], -90), "bricka": ([1, 0, 0], 0)}


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--fran", type=Path, required=True)
    a.add_argument("--ut", type=Path, required=True)
    ns = a.parse_args()
    ns.ut.mkdir(parents=True, exist_ok=True)
    delar = {}
    for n, (ax, g) in LAGE.items():
        m = trimesh.load(ns.fran / f"{n}.stl", force="mesh")
        m.apply_transform(trimesh.transformations.rotation_matrix(np.radians(g), ax))
        m.apply_translation(-m.bounds[0])
        f = ns.ut / f"{n}.stl"
        m.export(f)
        delar[f.name] = hashlib.sha256(f.read_bytes()).hexdigest()
        print(f"{n}: {m.extents.round(1).tolist()} mm")
    kallor = json.loads((ns.fran / "manifest.json").read_text())["kallor_sha256"]
    (ns.ut / "manifest.json").write_text(json.dumps({"typ": "sidotorn-slutdelar", "kallor_sha256": kallor,
                                                     "delar": delar}, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
