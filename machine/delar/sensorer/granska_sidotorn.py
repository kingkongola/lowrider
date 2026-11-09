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
a = p.parse_args()
L = lambda n: trimesh.load(a.ref / f"{n}.stl")
ref = {k: L("R_" + k) for k in ("befintlig_core", "tool_mount_t", "tool_mount_b", "dammsko", "kjol", "SPMS664_referens")}
torn, arm, bl = (trimesh.load(a.ut / f"{n}.stl") for n in ("torn", "arm", "bltouch"))
P = np.load(a.ref / "scan_pts_plan.npy")
PIV, PARK = np.array([45.0, 0, 43.6]), -140
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
