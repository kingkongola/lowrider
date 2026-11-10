"""Reproducerbar kontroll av CR Touch-anpassningens verkliga CAD-gränssnitt.

Exakta BRep-avstånd/intrång inom CAD, 2° stickprov över hela armrörelsen.
En rotationsgräns anger om avstånden även täcker mellanlägen mot CAD-tornet.
Originalmaskinens STL/skanning granskas separat med granska_sidotorn.py.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import build123d
from build123d import Cylinder, Pos, Rot, import_step
import sidotorn as cad


def volym(o):
    return 0.0 if o is None else sum(s.volume for s in o.solids())


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ut", required=True, type=Path)
    a = ap.parse_args()
    a.ut.parent.mkdir(parents=True, exist_ok=True)
    torn, arm = cad.torn(), cad.arm()
    hylsa, prob, kontakt = cad.skyddshylsa(), cad.crtouch(), cad.kontaktkuvert()
    stift = Pos(cad.PROB[0], cad.PROB[1] + cad.cr.STIFT_Y,
                cad.FLANS_Z - (46 + 29) / 2) * Cylinder(1.6, 46 - 29)
    delar = {"torn": torn, "arm": arm, "hylsa": hylsa, "prob": prob, "kontaktkuvert": kontakt,
             "stiftkuvert": stift}
    kallor = [Path(cad.__file__), Path(cad.cr.__file__), cad.cr.REFERENS, Path(__file__),
              Path(cad.lampor.__file__)]
    rapport = {"build123d": build123d.__version__, "kallor_sha256": {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in kallor},
        "komponenter": {}, "granssnitt": {}, "svep": {}, "fel": [], "oppna_referensfragor": []}
    for namn, o in delar.items():
        rapport["komponenter"][namn] = {"giltig": o.is_valid, "solider": len(o.solids())}
        if not o.is_valid or (namn in ("arm", "hylsa", "torn") and len(o.solids()) != 1):
            rapport["fel"].append(f"Ogiltig/delad kropp: {namn}")
    for n1, n2 in (("arm", "prob"), ("hylsa", "prob"), ("arm", "hylsa"),
                   ("arm", "kontaktkuvert"), ("hylsa", "stiftkuvert")):
        v = volym(delar[n1] & delar[n2])
        rapport["granssnitt"][f"{n1}/{n2}"] = {"intrang_mm3": round(v, 6),
                                                    "avstand_mm": round(delar[n1].distance_to(delar[n2]), 5)}
        if v > .001:
            rapport["fel"].append(f"Intrång {n1}/{n2}: {v:.4f} mm³")
    # M3x8: 2 mm skyddsöra + 1,9 mm referensfläns => 4,1 mm in i 4,5 mm armfot.
    # Originalets egna M3x6-skruvar har också ett litet intrång i dess sensorattrapp.
    # Kontrollera att vår nya skruvstapel inte inför ett större intrång; redovisa
    # källmodellens avvikelse som öppen referensfråga, inte som godkänd fysisk passning.
    original = import_step(cad.cr.REFERENS)
    originalprob = next(c for c in original.children if c.label == "CR-Touch_Mockup_v1")
    originalskruvar = [c for c in original.children[-1].children
                       if c.label.startswith("Screw") and c.bounding_box().max.Z > 50]
    referensintrang = max(volym(originalprob & s) for s in originalskruvar)
    rapport["referensens_egna_skruvintrang_mm3"] = round(referensintrang, 6)
    for sida in (-1, 1):
        x, y = cad.PROB[0] + sida * cad.cr.HAL_CC / 2, cad.PROB[1]
        sate = cad.FLANS_Z - cad.cr.FLANS_T - 2
        skruvref = next(s for s in originalskruvar
                        if (s.center().X < 3) == (sida > 0))
        # Använd originalets faktiska huvudform, inte en överskattande hel cylinder.
        skruv = Pos(cad.PROB[0], y, cad.FLANS_Z - 2) * Rot(0, 0, 180) * Pos(-3, 2.618, -50) * skruvref
        skruv += Pos(x, y, sate + 6.75) * Cylinder(1.5, 2.5)  # förläng M3x6-referensen till M3x8
        for namn, o in (("prob", prob), ("hylsa", hylsa)):
            v = volym(skruv & o)
            rapport["granssnitt"][f"M3x8_{sida}/{namn}"] = {"intrang_mm3": round(v, 6)}
            if namn == "prob" and 0 < v <= referensintrang + .0001:
                rapport["oppna_referensfragor"].append(
                    f"M3-huvud {sida}: {v:.6f} mm³ i probattrappen; samma avvikelse finns i originalets egna skruvar. Kontrollera verklig skalle/utrymme.")
            elif v > .001:
                rapport["fel"].append(f"Skruvintrång {sida}/{namn}: {v:.4f} mm³")
    # Avståndsgräns mellan två provvinklar: varje punkt flyttar högst
    # 2*r*sin(steg/4) till närmaste provläge. Distansfunktionen är 1-Lipschitz.
    steg = 2
    for namn in ("arm", "prob", "hylsa", "kontaktkuvert", "stiftkuvert"):
        o = delar[namn]
        b = o.bounding_box()
        radie = max(math.hypot(x - cad.PX, z - cad.PZ)
                    for x in (b.min.X, b.max.X) for z in (b.min.Z, b.max.Z))
        granser = 2 * radie * math.sin(math.radians(steg) / 4)
        rader = []
        for g in range(int(cad.PARK), 1, steg):
            q = Pos(cad.PX, 0, cad.PZ) * Rot(0, g, 0) * Pos(-cad.PX, 0, -cad.PZ) * o
            d = q.distance_to(torn)
            v = volym(q & torn) if d < .0001 else 0.0
            rader.append({"grader": g, "avstand_mm": round(d, 5), "intrang_mm3": round(v, 6)})
            if v > .001:
                rapport["fel"].append(f"{namn}/torn vid {g}°: {v:.4f} mm³")
        minrad = min(rader, key=lambda r: r["avstand_mm"])
        rapport["svep"][namn] = {"steg_grader": steg, "minsta": minrad,
            "rotationsgrans_mm": round(granser, 5),
            "mellanlagen_fria_mot_cad_torn": minrad["avstand_mm"] > granser,
            "lagen": rader}
        print(namn, "minsta", minrad, "mellanlägesgräns", round(granser, 3), flush=True)
    rapport["begransningar"] = [
        "Referensmodellen är tredjeparts-CAD; fysisk passning och stiftlägen är inte uppmätta.",
        "Kontaktkuvertet är reserverat utrymme, inte en uppmätt kontakt eller flexibel kabelmodell.",
        "Arm mot sina stopp får ha nollavstånd; mellanlägesgränsen godkänner inte avsedd stoppkontakt.",
        "Maskinens ursprungsdelar och skanning ingår i separat STL-stickprovskontroll.",
        "Servohornets infästning och fysisk montering återstår enligt CHECKLIST.md."]
    a.ut.write_text(json.dumps(rapport, ensure_ascii=False, indent=2) + "\n")
    print("Fel:", rapport["fel"], flush=True)
    raise SystemExit(bool(rapport["fel"]))


if __name__ == "__main__":
    main()
