"""CAD-kontroll av lampdocka, preliminär bärare och servicestickprov.

Lamp-/sockelkuvert är antaganden, inte mått på inköpta delar.
Kör med samma build123d-version som sidotorn.py, --ut rapport.json.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

import build123d
from build123d import Compound, Cone, Cylinder, Pos, Rot
import sidotorn as cad


def volym(o):
    return 0.0 if o is None else sum(s.volume for s in o.solids())


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ut", type=Path, required=True)
    a = ap.parse_args()
    torn, panel, barare = cad.torn(), cad.sidopanel(), cad.lampor.barare()
    lampor = cad.lampor.lampkuvert()
    lins = Pos(*cad.LINS) * Pos(0, 0, 3.45) * Cylinder(4.25, 6.9)
    kamera = cad.box((80.5, cad.KORT_Y[0], cad.KORT_FRAM),
                     (105.5, cad.KORT_Y[1], cad.KORT_BAK))
    # 90° full öppningsvinkel från linscentrum: konservativt konstruktionsprov,
    # ingen uppmätt optik eller analys av ljus/reflexer på arbetsstycket.
    synfalt = Pos(*cad.LINS) * Pos(0, 0, -7) * Cone(14, 0, 14)
    kallor = [Path(__file__), Path(cad.__file__), Path(cad.lampor.__file__),
              Path(cad.cr.__file__), cad.cr.REFERENS]
    r = {"build123d": build123d.__version__, "kallor_sha256": {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in kallor},
        "komponenter": {}, "granssnitt": {}, "svep": {}, "fel": []}
    for namn, o in (("torn", torn), ("panel", panel), ("barare", barare)):
        r["komponenter"][namn] = {"giltig": o.is_valid, "solider": len(o.solids()),
            "bbox_mm": [round(v, 3) for v in (*o.bounding_box().min, *o.bounding_box().max)]}
        if not o.is_valid or len(o.solids()) != 1:
            r["fel"].append(f"Ogiltig/delad kropp: {namn}")

    def granssnitt(namn, o1, o2):
        d = o1.distance_to(o2)
        v = volym(o1 & o2) if d < .0001 else 0.0
        r["granssnitt"][namn] = {"intrang_mm3": round(v, 6), "avstand_mm": round(d, 5)}
        if v > .001:
            r["fel"].append(f"Intrång {namn}: {v:.4f} mm³")

    for namn, o in (("torn", torn), ("panel", panel), ("lampkuvert", lampor),
                     ("lins", lins), ("kamerakort", kamera), ("synfalt90", synfalt)):
        granssnitt(f"barare/{namn}", barare, o)
    for namn, o in (("torn", torn), ("panel", panel), ("lins", lins), ("synfalt90", synfalt)):
        granssnitt(f"lampkuvert/{namn}", lampor, o)
    for x, z in cad.lampor.DOCK_HAL:
        skruv = cad.lampor.cy(x, z, 43.8, 46.8, 5.5) + cad.lampor.cy(x, z, 46.8, 52.8, 3)
        mejsel = cad.lampor.cy(x, z, 13.8, 43.8, 4.0)
        granssnitt(f"M3x6_{x}/barare", skruv, barare)
        granssnitt(f"mejsel_{x}/barare", mejsel, barare)
        granssnitt(f"mejsel_{x}/torn", mejsel, torn)
    r["skruvstapel_mm"] = {"M3x6_grepp_i_docka": 4.8, "till_blind_halbotten": 2.0,
                            "till_dockans_baksida": 3.2}
    fot = cad.lampor.dockplatta()
    mitt = fot.bounding_box().center()
    felvand = Pos(mitt.X, 0, mitt.Z) * Rot(0, 180, 0) * Pos(-mitt.X, 0, -mitt.Z) * fot
    nyckel = cad.lampor.cy(*cad.lampor.STYRTAPP, 47, 50, 3)
    r["felvand_fot_blockeras_mm3"] = round(volym(felvand & nyckel), 6)
    if r["felvand_fot_blockeras_mm3"] < 1:
        r["fel"].append("Styrtappen stoppar inte uppochnervänd fot")

    hinder = Compound(children=[barare, lampor])
    for namn, o in (("arm", cad.arm()), ("prob", cad.crtouch()),
                     ("hylsa", cad.skyddshylsa()), ("kontaktkuvert", cad.kontaktkuvert())):
        bb = o.bounding_box()
        radie = max(math.hypot(x-cad.PX, z-cad.PZ)
                    for x in (bb.min.X, bb.max.X) for z in (bb.min.Z, bb.max.Z))
        granser = 2 * radie * math.sin(math.radians(2) / 4)
        rader = []
        for g in range(int(cad.PARK), 1, 2):
            q = Pos(cad.PX, 0, cad.PZ) * Rot(0, g, 0) * Pos(-cad.PX, 0, -cad.PZ) * o
            d = q.distance_to(hinder)
            v = volym(q & hinder) if d < .0001 else 0.0
            rader.append({"grader": g, "avstand_mm": round(d, 5), "intrang_mm3": round(v, 6)})
            if v > .001:
                r["fel"].append(f"{namn}/lampmodul vid {g}°: {v:.4f} mm³")
        minrad = min(rader, key=lambda x: x["avstand_mm"])
        r["svep"][namn] = {"minsta": minrad, "rotationsgrans_mm": round(granser, 5),
            "mellanlagen_fria_mot_lampmodul": minrad["avstand_mm"] > granser, "lagen": rader}
        print(namn, minrad, flush=True)

    # Service med proben utfälld, därefter matningen frånkopplad. Skruvar borttagna.
    fasta = Compound(children=[torn, panel, kamera, lins, cad.arm(), cad.crtouch(), cad.skyddshylsa()])
    lagen = [(0, -i / 10, 0) for i in range(13)]
    lagen += [(0, -1.2, -i / 2) for i in range(1, 17)]
    lagen += [(i, -1.2, -8) for i in range(1, 66)]
    service = []
    for lage in lagen:
        q = Pos(*lage) * hinder
        d = q.distance_to(fasta)
        v = volym(q & fasta) if d < .0001 else 0.0
        service.append({"forflyttning_mm": lage, "intrang_mm3": round(v, 6)})
        if v > .001:
            r["fel"].append(f"Demontering vid {lage}: {v:.4f} mm³")
    r["demontering_stickprov"] = service
    r["begransningar"] = [
        "G4-kroppar och socklar är preliminära utrymmeskuvert, inte verifierad produktgeometri.",
        "Sockeladapter, verkliga fästskruvar, ledningar, värme och ljusbild återstår.",
        "Demonteringsbanan är stickprov, inte kontinuerligt bevis. Arm först i mätläge; matning sedan frånkopplad.",
        "Synfältskonen utgår från linscentrum; verklig optik och maskning provas med kameran.",
        "Skruvmejselkuvert: Ø4 x30 mm skaft. Verkligt handtag/bits kontrolleras vid montage.",
        "Originalmaskin och skanning ingår inte i denna exakta CAD-kontroll."]
    a.ut.parent.mkdir(parents=True, exist_ok=True)
    a.ut.write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n")
    print("Fel:", r["fel"], flush=True)
    raise SystemExit(bool(r["fel"]))


if __name__ == "__main__":
    main()
