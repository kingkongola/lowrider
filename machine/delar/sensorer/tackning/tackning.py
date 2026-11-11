"""Kontrollerar täckningsmatriserna och skriver TACKNING.md.

Vägrar om en ruta saknas, har okänd status, om en A-ruta pekar på ett kontrollskript som inte
finns i repot, om en exporterad CAD-del saknar rad (--cad), eller om en resultatpost pekar fel.
Skiljer på att en kontroll FINNS (statusen i rutan) och att den är UTFÖRD med godkänt utfall
(resultat.yaml med datum, metod, protokoll, ansvarig).

Kör: python tackning.py [--cad MANIFEST]            skriver TACKNING.md
     python tackning.py --kontroll [--cad MANIFEST]  felar om TACKNING.md inte är aktuell
     python tackning.py --strikt                     felar tills varje relevant ruta är verifierad
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
        if "utgatt" in rad:
            continue                      # utgången rad: finns kvar som historik, räknas inte
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
    return kol, rader, fel, d


def tabell(kol, rader):
    ut = ["| | " + " | ".join(kol.values()) + " |", "|---" * (len(kol) + 1) + "|"]
    for namn, rad in rader.items():
        ut.append(f"| {namn} | " + " | ".join(("**SAKNAS**" if status(str(rad[k])) == "SAKNAS" else status(str(rad[k])))
                                               for k in kol) + " |")
    return ut


BEVIS = ("datum", "metod", "protokoll", "ansvarig", "utfall")


def resultat(matriser):
    utg = matriser.get("_utgangna", {})
    """Senaste spårbara resultat per ruta styr: ett senare underkännande upphäver ett äldre godkännande."""
    poster = (yaml.safe_load((HAR / "resultat.yaml").read_text()) or {}).get("poster") or []
    fel, senaste = [], {}
    for i, p in enumerate(poster):
        saknas = [k for k in BEVIS if not str(p.get(k, "")).strip()]
        if saknas:
            fel.append(f"resultat.yaml post {i}: saknar {saknas}")
            continue
        kol, rader = matriser.get(p.get("matris"), ({}, {}))
        fil = str(p["protokoll"]).split(",")[0].split()[0]
        if (p.get("matris"), p.get("rad")) in utg:
            continue                      # prov på utgången del: historik, påverkar inte täckningen
        if p.get("rad") not in rader or p.get("kolumn") not in kol:
            fel.append(f"resultat.yaml post {i}: {p.get('matris')}/{p.get('rad')}/{p.get('kolumn')} finns inte")
        elif p["utfall"] not in ("godkänd", "underkänd"):
            fel.append(f"resultat.yaml post {i}: utfall ska vara godkänd eller underkänd")
        elif not any((REPO / d / fil).exists() for d in ("", "machine/delar/sensorer", "machine/delar/sensorer/tackning")):
            fel.append(f"resultat.yaml post {i}: protokollet {fil!r} finns inte i repot")
        else:
            nyckel = (p["matris"], p["rad"], p["kolumn"])
            if nyckel not in senaste or str(p["datum"]) >= str(senaste[nyckel]["datum"]):
                senaste[nyckel] = p
    godkant = {k for k, p in senaste.items() if p["utfall"] == "godkänd"}
    underkant = {k for k, p in senaste.items() if p["utfall"] == "underkänd"}
    return godkant, underkant, fel


def cad_kontroll(manifest, d):
    import json
    namn = {Path(n).stem for n in json.loads(Path(manifest).read_text())["exporter_sha256"] if n.endswith(".stl")}
    karta, undantag = d.get("cad") or {}, d.get("cad_undantag") or {}
    fel = [f"CAD-delen {n}.stl har ingen rad i komponenter.yaml" for n in sorted(namn) if n not in karta and n not in undantag]
    fel += [f"cad: {n} pekar på raden {r!r} som inte finns" for n, r in karta.items() if r not in d["komponenter"]]
    return fel


def rendera(cad=None):
    delar, fel = [], []
    sammanfattning = []
    saknas = []
    matriser = {}
    for fil, nyckel, rubrik in (("komponenter.yaml", "komponenter", "Komponenter"), ("system.yaml", "funktioner", "Systemet")):
        kol, rader, f, d = las(fil, nyckel)
        fel += f
        matriser["komponenter" if nyckel == "komponenter" else "system"] = (kol, {n: r for n, r in rader.items() if "utgatt" not in r})
        matriser.setdefault("_utgangna", {}).update({(("komponenter" if nyckel == "komponenter" else "system"), n): r["utgatt"] for n, r in rader.items() if "utgatt" in r})
        if nyckel == "komponenter" and cad:
            fel += cad_kontroll(cad, d)
        if f:
            continue
        aktiva = {n: r for n, r in rader.items() if "utgatt" not in r}
        utgangna = [n for n, r in rader.items() if "utgatt" in r]
        rader = aktiva
        c = Counter(status(str(r[k])) for r in rader.values() for k in kol)
        tot = sum(c.values())
        mkey = "komponenter" if nyckel == "komponenter" else "system"
        relevanta = [(n, k) for n, r in rader.items() for k in kol if status(str(r[k])) != "X"]
        sammanfattning.append((mkey, f"| {rubrik} | {len(rader)} × {len(kol)} | " + " | ".join(str(c[s]) for s in STATUS)
                              + f" | {round(100 * (tot - c['SAKNAS'] - c['N']) / tot)} % | VERIFIERAT | {len(relevanta)} |"))
        delar += [f"## {rubrik}", "", *tabell(kol, rader), ""]
        for namn, rad in rader.items():
            for k, rubr in kol.items():
                if status(str(rad[k])) == "SAKNAS":
                    saknas.append(f"| {rubrik} | {namn} | {rubr} | {rad[k].split('SAKNAS', 1)[1].strip(' :;')} |")
    godkant, underkant, f = resultat(matriser)
    fel += f
    if fel:
        raise SystemExit("UNDERKÄND:\n" + "\n".join(fel))
    sammanfattning = [rad.replace("VERIFIERAT", f"{sum(1 for v in godkant if v[0] == m)} / {sum(1 for v in underkant if v[0] == m)}")
                      for m, rad in sammanfattning]
    utg = matriser.pop("_utgangna", {})
    x_utan = [f"{m}/{n}/{k}" for m, (kol, rader) in matriser.items() for n, r in rader.items() for k in kol
              if status(str(r[k])) == "X" and len(str(r[k]).strip()) <= 2]
    a_typ = Counter()
    for m, (kol, rader) in matriser.items():
        for n, r in rader.items():
            for k in kol:
                t = str(r[k])
                if status(t) != "A" and not t.startswith("A "):
                    continue
                if re.search(r"test_\w+\.py|cnc|sensorpi", t):
                    a_typ["extern (cnc-repot)"] += 1
                elif "kontroll_omgivning" in t or "skanning" in t:
                    a_typ["lokal (skanningsdata, ej CI)"] += 1
                else:
                    a_typ["i lowriders CI"] += 1
    huvud = ["# Täckning: vad är kontrollerat?", "",
             "Genererad av `tackning.py` ur `komponenter.yaml` och `system.yaml`. Ändra i YAML-filerna, inte här.", "",
             "Varje ruta har den sämsta status som står i den. **Har kontroll** = A, S, F eller X: rutan har en definierad kontroll eller är inte relevant. F betyder ett **planerat** fysiskt prov; om det är utfört ägs av CHECKLIST.md. Nominella antaganden (N) och SAKNAS räknas inte.", "",
             "| Matris | Storlek | " + " | ".join(f"{s} ({NAMN[s]})" for s in STATUS) + " | Har kontroll | Godkända / underkända | Relevanta rutor |",
             "|---" * (len(STATUS) + 5) + "|", *sammanfattning, "",
             "**Godkända / underkända** räknar rutornas senaste prov i `resultat.yaml` (datum, metod, protokoll, ansvarig). Ett senare underkännande upphäver ett äldre godkännande. Att en kontroll finns (A) är inte detsamma som att den är utförd.", "",
             "**Var de automatiska kontrollerna körs:** " + ", ".join(f"{k}: {v}" for k, v in sorted(a_typ.items())) + ". cnc-repots tester körs i cnc, inte i lowriders CI.", "",
             "## Underkända prov", "", *([f"- {m} / {n} / {k}" for m, n, k in sorted(underkant)] or ["- inga"]), "",
             "## Utgångna rader", "", *([f"- {m} / {n}: {sk}" for (m, n), sk in sorted(utg.items())] or ["- inga"]), "",
             f"## X utan skäl ({len(x_utan)} rutor)", "", "Ett X ska ha ett skäl. Dessa saknar det och underkänns i strikt läge.", "",
             *(", ".join(x_utan[i:i + 6]) for i in range(0, len(x_utan), 6)), "",
             f"## Inte kontrollerat ({len(saknas)} rutor)", "", "| Matris | Rad | Kolumn | Vad saknas |", "|---|---|---|---|", *saknas, ""]
    return "\n".join(huvud + delar)


def strikt():
    matriser = {}
    for fil, nyckel, m in (("komponenter.yaml", "komponenter", "komponenter"), ("system.yaml", "funktioner", "system")):
        kol, rader, _, _ = las(fil, nyckel)
        matriser[m] = (kol, {n: r for n, r in rader.items() if "utgatt" not in r})
        matriser.setdefault("_utgangna", {}).update({(m, n): r["utgatt"] for n, r in rader.items() if "utgatt" in r})
    godkant, underkant, _ = resultat(matriser)
    matriser.pop("_utgangna", None)
    kvar = [(m, n, k) for m, (kol, rader) in matriser.items() for n, r in rader.items() for k in kol
            if status(str(r[k])) != "X" and (m, n, k) not in godkant]
    x_utan = [(m, n, k) for m, (kol, rader) in matriser.items() for n, r in rader.items() for k in kol
              if status(str(r[k])) == "X" and len(str(r[k]).strip()) <= 2]
    if kvar or underkant or x_utan:
        raise SystemExit(f"STRIKT UNDERKÄND: {len(kvar)} relevanta rutor utan godkänt bevis, {len(underkant)} underkända, "
                         f"{len(x_utan)} X utan skäl")
    print("STRIKT GODKÄND: varje relevant ruta är verifierad")


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--kontroll", action="store_true")
    a.add_argument("--strikt", action="store_true")
    a.add_argument("--cad", type=Path)
    ns = a.parse_args()
    if ns.strikt:
        return strikt()
    text = rendera(ns.cad)
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
