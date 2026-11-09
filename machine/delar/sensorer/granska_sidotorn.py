"""Kontroll av sidotornet mot skanning och V1E-delar. Bevisar geometri, inte passning.

--ref ska innehålla R_*.stl (Core, fästen, sko, kjol, servo) och scan_pts_plan.npy:
skanningens punkter i fräsramen med bordet plant (5,9 graders rättning 2026-11-09).
Dessa filer är för stora för repot och kommer från handover/skanning.
"""
import argparse
from pathlib import Path

import numpy as np
import trimesh
from scipy.spatial import cKDTree

p = argparse.ArgumentParser()
p.add_argument("--ut", required=True, type=Path)
p.add_argument("--ref", required=True, type=Path)
p.add_argument("--servo-dy", type=float, default=-2.0)
a = p.parse_args()
L = lambda n: trimesh.load(a.ref / f"{n}.stl")
ref = {k: L("R_" + k) for k in ("befintlig_core", "tool_mount_t", "tool_mount_b", "dammsko", "kjol", "SPMS664_referens")}
ref["SPMS664_referens"].apply_translation([0, a.servo_dy, 0])
torn, arm, bl, lock, kabel = (trimesh.load(a.ut / f"{n}.stl") for n in ("torn", "arm", "bltouch", "sidopanel", "kabel"))
P = np.load(a.ref / "scan_pts_plan.npy")
PIV, PARK = np.array([45.0, 0, 43.6]), -150
sm = lambda m, n: trimesh.sample.sample_surface(m, n, seed=2)[0]
K = {k: (cKDTree(sm(v, 90000)), v) for k, v in {**ref, "torn": torn}.items()}
S = cKDTree(P[(P[:, 0] > -60) & (P[:, 0] < 170) & (P[:, 1] > -40) & (P[:, 1] < 120) & (P[:, 2] > -60)])
print("torn bbox", torn.bounds.round(1).tolist(), "tät", torn.is_watertight)
sk = P[((P > torn.bounds[0]) & (P < torn.bounds[1])).all(1)]
print("skanpunkter i tornet x>12:", int((sk[torn.contains(sk)][:, 0] > 12).sum()))
T = lambda g: trimesh.transformations.rotation_matrix(np.radians(g), [0, 1, 0], PIV)
for nm, o in (("arm", arm), ("BLTouch", bl)):
    q0 = sm(o, 9000)
    b = {}
    for g in range(PARK, 1, 5):
        q = trimesh.transform_points(q0, T(g))
        for k, (t, m) in K.items():
            if k == "torn" and g in (PARK, 0):  # stoppen ska ta i där
                continue
            d = t.query(q)[0]
            dm = float(d.min())
            if (d < 6).any() and m.contains(q[d < 6]).any():
                dm = -1.0
            if k not in b or dm < b[k][0]:
                b[k] = (round(dm, 1), g)
        dm = float(S.query(q)[0].min())
        if "skanning" not in b or dm < b["skanning"][0]:
            b["skanning"] = (round(dm, 1), g)
    print(nm, "minsta avstånd (mm, vinkel), -1 = inne i:", sorted(b.items(), key=lambda kv: kv[1][0]))
print("parkerad BLTouch bbox", trimesh.transform_points(bl.vertices, T(PARK)).min(0).round(1).tolist(), trimesh.transform_points(bl.vertices, T(PARK)).max(0).round(1).tolist())


# Passningsytor: varje gränssnitt mäts, inget antas. Avstånd i mm, None = ingen träff.
def stralar(o, d, m):
    h = m.ray.intersects_location([o], [d])[0]
    return sorted(round(float(np.linalg.norm(p - np.array(o))), 2) for p in h)


servo, nx = ref["SPMS664_referens"], lambda o, d, m: (stralar(o, d, m) or [None])[0]
print("--- passningsytor")
for x in (11.7, 59.0):
    for z in (38.9, 48.3):
        print(f"servoöra x{x} z{z}: avstånd till öra {nx([x + 2.5, 43.3 + a.servo_dy, z], [0, -1, 0], servo)}, skruvhål fritt {nx([x, 43.0 + a.servo_dy, z], [0, 1, 0], torn) is None}")
q = sm(arm, 20000)
t = cKDTree(sm(torn, 400000))
for g_ in (0, -1, PARK + 1, PARK):
    w = trimesh.transform_points(q, T(g_))
    print(f"stopp vid {g_} grader: minsta avstånd {t.query(w)[0].min():.2f}")
print("BLTouch-fläns mot armplatta:", round(float(arm.bounds[0, 2] - bl.bounds[1, 2]), 2))
for z, o, nm in ((64.25, ref["tool_mount_b"], "undre"), (125.25, ref["tool_mount_t"], "övre")):
    print(f"M5 {nm}: boss mot fäste {[nx([-5, 43.95 + r * np.cos(v), z + r * np.sin(v)], [-1, 0, 0], o) for r, v in ((4.5, 0), (4.5, 1.57), (4.5, 3.14), (4.5, 4.71))]}, hål fritt {nx([-5, 43.95, z], [-1, 0, 0], o) is None}")
print("kortets skruvhål djup:", [nx([94 + dx, 53 + dy, 134.5], [0, 0, 1], torn) for dx in (-10.5, 10.5) for dy in (-6.25, 6.25)])
for nm, o, d in (("botten", [30, 66, 60.5], [0, 0, -1]), ("ramp", [65, 66, 100], [0, 0, -1]), ("tak", [45, 60, 157.5], [0, 0, 1]), ("front", [45, 51.4, 140], [0, -1, 0]), ("rygg", [12.5, 60, 90], [-1, 0, 0]), ("CSI-golv", [90, 58, 136.5], [0, 0, -1])):
    h = stralar(o, d, torn)
    print(f"väggtjocklek {nm}: {round(h[1] - h[0], 2) if len(h) > 1 else None}")
print("Y max med lock:", round(float(max(torn.bounds[1, 1], lock.bounds[1, 1])), 2))

kq = sm(kabel, 12000)
for k, (t, m) in K.items():
    if k != "torn":
        print(f"kabel mot {k}: {t.query(kq)[0].min():.1f} mm, inne: {int(m.contains(kq[t.query(kq)[0] < 8]).sum())}")
print("kabel mot skanning (minsta):", round(float(S.query(kq)[0].min()), 1))

# Intrång i fasta delar; M5-distansernas planläge x = -7,3 ska ligga an och räknas bort.
for k, m in ref.items():
    lo, hi = np.maximum(m.bounds[0], [-7.2, *torn.bounds[0][1:]]), np.minimum(m.bounds[1], torn.bounds[1])
    if (hi > lo).all():
        q = np.random.default_rng(1).uniform(lo, hi, (800000, 3))
        print(f"intrång torn mot {k}: {float((torn.contains(q) & m.contains(q)).mean() * np.prod(hi - lo)):.2f} mm3")
