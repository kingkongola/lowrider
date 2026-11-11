"""Kontrollerar täckningsmatriserna och skriver TACKNING.md.

Vägrar om en ruta saknas, har okänd status, eller om en A-ruta pekar på ett kontrollskript
som inte finns i repot. Kör: python tackning.py            (skriver TACKNING.md)
                              python tackning.py --kontroll (felar om TACKNING.md inte är aktuell)
"""
import argparse
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

HAR = Path(__file__).parent
REPO = HAR.parents[3]
STATUS = ["A", "S", "F", "N", "X", "SAKNAS"]
NAMN = {"A": "automatisk kontroll", "S": "simulerad/beräknad", "F": "fysiskt prov", "N": "nominellt antagande",
        "X": "ej relevant", "SAKNAS": "inte kontrollerat"}
LOKALA = {p.name for p in REPO.rglob("*.py")} | {p.name for p in (REPO / ".github/workflows").glob("*.yml")}


def status(text: str) -> str:
    """Sämsta status i rutan räknas: en ruta med både A och SAKNAS är SAKNAS."""
    funna = [s for s in STATUS if re.search(rf"(^|; ){s}\b", text)]
    if not funna:
        raise ValueError(f"okänd status: {text!r}")
    return max(funna, key=lambda s: ["A", "S", "F", "X", "N", "SAKNAS"].index(s))


def las(fil, nyckel):
    d = yaml.safe_load((HAR / fil).read_text())
    kol, rader, fel = d["kolumner"], d[nyckel], []
    for namn, rad in rader.items():
        for k in kol:
            if k not in rad or not str(rad[k]).strip():
                fel.append(f"{fil}: {namn}/{k} saknas")
                continue
            try:
                status(str(rad[k]))
            except ValueError as e:
                fel.append(f"{fil}: {namn}/{k}: {e}")
            for s in re.findall(r"([a-z_][a-z_\-]*\.(?:py|yml))\b", str(rad[k])):
                if s.startswith("test_") or s in ("sensorpi.py",):
                    continue                     # ligger i cnc-repot
                if s not in LOKALA:
                    fel.append(f"{fil}: {namn}/{k}: {s} finns inte i repot")
        for k in rad:
            if k not in kol:
                fel.append(f"{fil}: {namn}/{k} är ingen kolumn")
    return kol, rader, fel


def tabell(kol, rader):
    ut = ["| | " + " | ".join(kol.values()) + " |", "|---" * (len(kol) + 1) + "|"]
    for namn, rad in rader.items():
        ut.append(f"| {namn} | " + " | ".join(("**SAKNAS**" if status(str(rad[k])) == "SAKNAS" else status(str(rad[k])))
                                               for k in kol) + " |")
    return ut


def rendera():
    delar, fel = [], []
    sammanfattning = []
    saknas = []
    for fil, nyckel, rubrik in (("komponenter.yaml", "komponenter", "Komponenter"), ("system.yaml", "funktioner", "Systemet")):
        kol, rader, f = las(fil, nyckel)
        fel += f
        if f:
            continue
        c = Counter(status(str(r[k])) for r in rader.values() for k in kol)
        tot = sum(c.values())
        sammanfattning.append(f"| {rubrik} | {len(rader)} × {len(kol)} | " + " | ".join(str(c[s]) for s in STATUS)
                              + f" | {round(100 * (tot - c['SAKNAS'] - c['N']) / tot)} % |")
        delar += [f"## {rubrik}", "", *tabell(kol, rader), ""]
        for namn, rad in rader.items():
            for k, rubr in kol.items():
                if status(str(rad[k])) == "SAKNAS":
                    saknas.append(f"| {rubrik} | {namn} | {rubr} | {rad[k].split('SAKNAS', 1)[1].strip(' :;')} |")
    if fel:
        raise SystemExit("UNDERKÄND:\n" + "\n".join(fel))
    huvud = ["# Täckning: vad är kontrollerat?", "",
             "Genererad av `tackning.py` ur `komponenter.yaml` och `system.yaml`. Ändra i YAML-filerna, inte här.", "",
             "Varje ruta har den sämsta status som står i den. **Har kontroll** = A, S, F eller X: rutan har en definierad kontroll eller är inte relevant. F betyder ett **planerat** fysiskt prov; om det är utfört ägs av CHECKLIST.md. Nominella antaganden (N) och SAKNAS räknas inte.", "",
             "| Matris | Storlek | " + " | ".join(f"{s} ({NAMN[s]})" for s in STATUS) + " | Har kontroll |",
             "|---" * (len(STATUS) + 3) + "|", *sammanfattning, "",
             f"## Inte kontrollerat ({len(saknas)} rutor)", "", "| Matris | Rad | Kolumn | Vad saknas |", "|---|---|---|---|", *saknas, ""]
    return "\n".join(huvud + delar)


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--kontroll", action="store_true")
    ns = a.parse_args()
    text = rendera()
    mal = HAR / "TACKNING.md"
    if ns.kontroll:
        if not mal.exists() or mal.read_text() != text:
            raise SystemExit("TACKNING.md är inte genererad ur aktuella matriser; kör python tackning.py")
        print("GODKÄND: matriserna är kompletta och TACKNING.md aktuell")
        return
    mal.write_text(text)
    print(text.split("## Inte kontrollerat")[0])


if __name__ == "__main__":
    main()
