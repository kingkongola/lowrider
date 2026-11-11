#!/usr/bin/env python3
"""Kontrollerar matrisschema och CAD-exportdrift utan CAD-beroenden.

Utan --strict: dataintegritet och källsynk, exit 0 även när fysiska prover
saknas. Med --strict: driftspärr tills samtliga relevanta rutor har bevisat
godkänt resultat. Ersätter INTE geometriska eller elektriska prov.
"""
import argparse
import ast
import json
from collections import Counter
from pathlib import Path

DIR = Path(__file__).resolve().parent
ROOT = DIR.parents[3]
PHASES = ["matt","print","insattning","infastning","koppling","rorelse",
          "last_vibration","varme","damm","service","funktion"]
LEVELS = ["krav","konstruktion","automatisk","berakning","bankprov",
          "maskinprov","felhantering","aterstallning"]
STATUSES = {"A","S","F","N","X","SAKNAS"}
RESULTS = {"ej_utfort","godkand","underkand","ej_tillampligt"}


def check_matrix(name, entries, keys):
    seen = set()
    counts = Counter()
    problems = []
    for entry in entries:
        ident = entry.get("id")
        if not ident or ident in seen:
            problems.append(f"{name}: dubblett/tomt id {ident!r}")
        seen.add(ident)
        fields = entry.get("kontroller", {})
        if set(fields) != set(keys):
            problems.append(f"{name}/{ident}: fel faser, saknas {set(keys)-set(fields)}")
        for phase in keys:
            cell = fields.get(phase, {})
            status, result = cell.get("status"), cell.get("resultat")
            if status not in STATUSES or result not in RESULTS:
                problems.append(f"{ident}/{phase}: okänd status/resultat")
                continue
            if not cell.get("kontroll", "").strip():
                problems.append(f"{ident}/{phase}: kontrollinstruktion saknas")
            if status == "X" and result != "ej_tillampligt":
                problems.append(f"{ident}/{phase}: X kräver ej_tillampligt")
            if status != "X" and result == "ej_tillampligt":
                problems.append(f"{ident}/{phase}: N/A utan X")
            if status in ("A","S","N") and not cell.get("evidens"):
                problems.append(f"{ident}/{phase}: {status} kräver källreferens")
            if result == "godkand":
                evidence = cell.get("evidens", "").strip()
                if status in ("X","N","SAKNAS") or not evidence:
                    problems.append(f"{ident}/{phase}: saknar giltigt verifieringsbevis")
            counts[status] += 1
    return problems, counts


def exported_stls(source):
    """Hämta namn ur for n,o in ((\"torn\",t),...) utan att importera build123d."""
    tree = ast.parse(source.read_text(encoding="utf-8"))
    matches = []
    for node in ast.walk(tree):
        if isinstance(node, ast.For) and isinstance(node.iter, (ast.Tuple, ast.List)):
            vals = []
            for item in node.iter.elts:
                if (isinstance(item, ast.Tuple) and len(item.elts) == 2
                        and isinstance(item.elts[0], ast.Constant)
                        and isinstance(item.elts[0].value, str)):
                    vals.append(item.elts[0].value)
            if set(vals).issuperset({"torn", "arm", "bltouch", "sidopanel", "kabel", "kapa", "bricka"}):
                matches.append(vals)
    if len(matches) != 1:
        raise ValueError("Kunde inte entydigt läsa STL-exportregistret i sidotorn.py")
    return set(matches[0])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="kräv utförda godkända kontroller")
    args = parser.parse_args()
    a = json.loads((DIR/"komponentmatris.json").read_text(encoding="utf-8"))
    b = json.loads((DIR/"systemmatris.json").read_text(encoding="utf-8"))
    errors = []
    if a.get("faser") != PHASES or b.get("steg") != LEVELS:
        errors.append("fas-/nivåkontraktet har ändrats")
    errors += check_matrix("komponenter", a["komponenter"], PHASES)[0]
    errors += check_matrix("system", b["systemfunktioner"], LEVELS)[0]
    stls = exported_stls(ROOT/"machine/delar/sensorer/sidotorn.py")
    declared = set(a["utskrifter"]) | set(a["attrapper_eller_hjalpgeometri"])
    if stls != declared:
        errors.append(f"CAD-export drift: CAD={sorted(stls)}, matris={sorted(declared)}")
    actual_prints = {c["ritningsdel"] for c in a["komponenter"] if c["typ"] == "printad"}
    if actual_prints != set(a["utskrifter"]):
        errors.append(f"Matrisen har ofullständig print-BOM: {actual_prints!r}")
    if any("KW11" in c["namn"] for c in a["komponenter"]):
        errors.append("KW11 är supersederat av D020; får inte vara aktiv sidotornsdel")
    overall = [cell for data, fields in ((a["komponenter"], PHASES),
                                        (b["systemfunktioner"], LEVELS))
               for row in data for phase in fields
               if (cell := row["kontroller"][phase])["status"] != "X"]
    done = sum(x["resultat"] == "godkand" for x in overall)
    counts = Counter(x["status"] for x in overall)
    print(f"Komponenter: {len(a['komponenter'])}, systemfunktioner: {len(b['systemfunktioner'])}")
    print(f"Relevanta rutor: {len(overall)}. Verifierat godkända: {done}. Status: {dict(counts)}")
    if args.strict and done != len(overall):
        errors.append(f"Driftgrind: {len(overall)-done} relevanta rutor inte godkända")
    if errors:
        for err in errors:
            print("FEL:", err)
        raise SystemExit(1)
    print("Schema och CAD-exportregistret OK. Ingen fysisk provning har skett genom detta skript.")


if __name__ == "__main__":
    main()
