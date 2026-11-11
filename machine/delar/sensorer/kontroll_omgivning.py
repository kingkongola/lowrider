"""Exakt kontroll av sidotornet mot den skannade omgivningen. Avbryter med fel vid krock.

Skärningsvolymer räknas med manifold3d (exakta booleska operationer på täta mesh), inte med
punktprov. Armen, CR Touchen, hylsan, hornbygeln och skruvarna vrids genom hela rörelsen
(parkerat -150 till utfällt 0 grader, 2 graders steg) och kontrolleras mot referensdelarna,
mot tornet och mot skanningens punktmoln.

Referensdata finns inte i git, se skanning/README.md.

Kör: python sidotorn.py --ut UT && python kontroll_omgivning.py --ut UT --ref ~/dev/lowrider-data/skanning-2026-11-09
"""
import argparse
import json
from pathlib import Path

import numpy as np
import trimesh

import sidotorn as S

ap = argparse.ArgumentParser()
ap.add_argument("--ut", type=Path, required=True, help="katalog med sidotorn.py:s export")
ap.add_argument("--ref", type=Path, required=True, help="skanning och referens-STL")
ap.add_argument("--rapport", type=Path)
a = ap.parse_args()

GRANS_MM3 = 0.5          # mer gods än så i en annan del räknas som krock (STL-avrundning ligger under 0,05)
STEG = 2
PIV = np.array([S.PX, 0.0, S.PZ])

# Skanningsdatan ska vara exakt den som kontrollsummorna i repot anger (granskning issue #2, fynd 6).
import hashlib
_summor = dict(reversed(r.split()) for r in (Path(__file__).parent / "skanning" / "SHA256SUMS").read_text().splitlines() if r.strip())
for _namn, _sha in _summor.items():
    if hashlib.sha256((a.ref / _namn).read_bytes()).hexdigest() != _sha:
        raise SystemExit(f"UNDERKÄND: {_namn} stämmer inte med skanning/SHA256SUMS; fel skanningsdata")
_cad = json.loads((a.ut / "manifest.json").read_text())["kallor_sha256"]
L = lambda p: trimesh.load(p, force="mesh")
ref = {k: L(a.ref / f"R_{k}.stl") for k in ("befintlig_core", "tool_mount_t", "tool_mount_b", "dammsko", "kjol", "SPMS664_referens")}
ref["SPMS664_referens"].apply_translation([0, S.SERVO_DY, 0])
del_ = {n: L(a.ut / f"{n}.stl") for n in ("torn", "sidopanel", "arm", "crtouch", "kapa", "hornbygel", "hornskruvar-referens", "magnetstal-referens", "stopp-nedre", "stopp-ovre")}
P = np.load(a.ref / "scan_pts_plan.npy")

# Avsiktliga anläggningar: tornets M5-distanser ligger mot verktygsfästena och servot sitter i sin ram.
AVSIKT = {("torn", "tool_mount_t"), ("torn", "tool_mount_b"), ("torn", "SPMS664_referens")}


def kroppar(m):
    return [m] if m.is_volume else [d for d in m.split(only_watertight=False) if d.is_volume]


def vol(a_, b_):
    if not (np.all(a_.bounds[0] <= b_.bounds[1]) and np.all(b_.bounds[0] <= a_.bounds[1])):
        return 0.0
    tot = 0.0
    for x in kroppar(a_):
        for y in kroppar(b_):
            s = trimesh.boolean.intersection([x, y], engine="manifold")
            tot += float(s.volume) if len(s.faces) else 0.0
    return tot


SKAN_TOL = 2.0           # skanningens noggrannhet, mm (README: offerskivan ±2 mm)


def skanpunkter(m):
    """Skanpunkter som ligger mer än SKAN_TOL inne i delen; grundare punkter är mätbrus eller anläggning."""
    lo, hi = m.bounds
    q = P[((P > lo + SKAN_TOL) & (P < hi - SKAN_TOL)).all(1)]
    if not len(q):
        return 0
    q = q[m.contains(q)]
    return int((m.nearest.on_surface(q)[1] > SKAN_TOL).sum()) if len(q) else 0


fel, rapport = [], {"statiskt": {}, "rorelse": {}}
for n in ("torn", "sidopanel", "stopp-nedre", "stopp-ovre"):
    for k, r in ref.items():
        v = vol(del_[n], r)
        rapport["statiskt"][f"{n}/{k}"] = round(v, 3)
        avsikt = (n, k) in AVSIKT
        print(f"{n} mot {k}: {v:.3f} mm3{' (avsiktlig anläggning, redovisas)' if avsikt else ''}")
        if v > GRANS_MM3 and not avsikt:
            fel.append(f"{n} krockar med {k} ({v:.1f} mm3)")
    sp = skanpunkter(del_[n])
    rapport["statiskt"][f"{n}/skanning_punkter"] = sp
    print(f"{n}: skanpunkter mer än {SKAN_TOL} mm inne i delen: {sp}")
    if sp:
        fel.append(f"{n} går in i skanningen ({sp} punkter)")

rorliga = ("arm", "crtouch", "kapa", "hornbygel", "hornskruvar-referens", "magnetstal-referens")
for n in rorliga:
    varst = {}
    for g in range(int(S.PARK), 1, STEG):
        m = del_[n].copy()
        m.apply_transform(trimesh.transformations.rotation_matrix(np.radians(g), [0, 1, 0], PIV))
        mal = dict(ref)
        if g not in (int(S.PARK), 0):          # vid ändlägena ska armen ta i stoppen
            mal["torn"] = del_["torn"]
            mal["stopp-nedre"], mal["stopp-ovre"] = del_["stopp-nedre"], del_["stopp-ovre"]
        mal["sidopanel"] = del_["sidopanel"]
        for k, r in mal.items():
            if n in ("hornbygel", "hornskruvar-referens") and k == "SPMS664_referens":
                continue                         # hornet sitter på servots axel
            v = vol(m, r)
            if v > varst.get(k, (-1, 0))[0]:
                varst[k] = (round(v, 3), g)
        sp = skanpunkter(m)
        if sp > varst.get("skanning_punkter", (-1, 0))[0]:
            varst["skanning_punkter"] = (sp, g)
    rapport["rorelse"][n] = varst
    print(n, "största intrång (mm3 eller punkter, vinkel):", varst)
    for k, (v, g) in varst.items():
        if k == "skanning_punkter":
            if v > 0:
                fel.append(f"{n} går in i skanningen vid {g} grader ({v} punkter)")
        elif v > GRANS_MM3:
            fel.append(f"{n} krockar med {k} vid {g} grader ({v:.1f} mm3)")

if a.rapport:
    a.rapport.write_text(json.dumps({**rapport, "fel": fel, "cad_kallor_sha256": _cad, "skanning_sha256": _summor},
                                    ensure_ascii=False, indent=1) + "\n")
if fel:
    raise SystemExit("UNDERKÄND: " + "; ".join(fel))
print("GODKÄND: torn, panel och armens hela rörelse mot skannad omgivning")
