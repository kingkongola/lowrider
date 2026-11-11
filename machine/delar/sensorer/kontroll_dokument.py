"""Kontrollerar att BOM.md har varje fästelement som MONTAGE.md kräver.

Varför: BOM:en listade gamla panelskruvar efter en CAD-ändring (hittat av täckningsmatrisen
2026-11-11). Fel skruvar köps eller tas fram om listorna glider isär.
Kör: python kontroll_dokument.py
"""
import re
from pathlib import Path

HAR = Path(__file__).parent
MONSTER = re.compile(r"M(\d(?:[.,]\d)?)\s*[×x]\s*(\d+)")


def storlekar(text):
    return {f"M{a.replace(',', '.')} × {b}" for a, b in MONSTER.findall(text)}


def saknade(montage: str, bom: str):
    tabell = montage.split("## Så sitter allt fast", 1)[1].split("\n## ", 1)[0]
    return sorted(storlekar(tabell) - storlekar(bom))


# Negativtest: en BOM utan M3 x 20 måste fångas.
assert saknade("## Så sitter allt fast\n| a | M3 × 20 |\n## x", "| M3 × 10 |") == ["M3 × 20"]

m = (HAR / "MONTAGE.md").read_text()
b = (HAR.parents[2] / "BOM.md").read_text()
fel = saknade(m, b)
print("fästelement i MONTAGE.md:", ", ".join(sorted(storlekar(m.split("## Så sitter allt fast", 1)[1].split("\n## ", 1)[0]))))
if fel:
    raise SystemExit("UNDERKÄND: saknas i BOM.md: " + ", ".join(fel))
print("GODKÄND: BOM.md har alla fästelement som MONTAGE.md kräver")
