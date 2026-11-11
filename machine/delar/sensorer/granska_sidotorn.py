"""Kontroll av sidotornet mot skanning och V1E-delar. Stickprovskontroll, inte bevis på fysisk passning.

--ref ska innehålla R_*.stl (Core, fästen, sko, kjol, servo) och scan_pts_plan.npy:
skanningens punkter i fräsramen med bordet plant (5,9 graders rättning 2026-11-09).
Dessa filer är för stora för repot; se skanning/README.md (kontrollsummor och plats).
"""
import argparse
import json
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
E = json.loads((a.ut / "elektronik.json").read_text())
torn, arm, bl, lock, kabel = (trimesh.load(a.ut / f"{n}.stl") for n in ("torn", "arm", "crtouch", "sidopanel", "kabel"))
hornref,mittskruv,magnetstal=(trimesh.load(a.ut/f'{n}.stl') for n in ('horn-referens','mittskruv-referens','magnetstal-referens'))
lampbarare = trimesh.load(a.ut / "lampbarare-utkast.stl")
for namn, m in ref.items():
    gap = np.maximum(np.maximum(lampbarare.bounds[0] - m.bounds[1], m.bounds[0] - lampbarare.bounds[1]), 0)
    grans = float(np.linalg.norm(gap))
    print(f"lampbärare mot {namn}: avstånd minst {grans:.2f} mm enligt separerade omslutningslådor")
    if grans == 0:
        print("  Överlappande omslutningslådor: kräver särskild mesh-/CAD-granskning, inget godkännande här.")
P = np.load(a.ref / "scan_pts_plan.npy")
PIV, PARK = np.array([45.0, 0, 43.6]), -150
sm = lambda m, n: trimesh.sample.sample_surface(m, n, seed=2)[0]
K = {k: (cKDTree(sm(v, 90000)), v) for k, v in {**ref, "torn": torn}.items()}
S = cKDTree(P[(P[:, 0] > -60) & (P[:, 0] < 170) & (P[:, 1] > -40) & (P[:, 1] < 120) & (P[:, 2] > -60)])
print("torn bbox", torn.bounds.round(1).tolist(), "tät", torn.is_watertight)
sk = P[((P > torn.bounds[0]) & (P < torn.bounds[1])).all(1)]
print("skanpunkter i tornet x>12:", int((sk[torn.contains(sk)][:, 0] > 12).sum()))
T = lambda g: trimesh.transformations.rotation_matrix(np.radians(g), [0, 1, 0], PIV)
for nm, o in (("arm", arm), ("CR Touch", bl), ('horn',hornref),('mittskruv',mittskruv),('magnetstål',magnetstal)):
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
print("parkerad CR Touch bbox", trimesh.transform_points(bl.vertices, T(PARK)).min(0).round(1).tolist(), trimesh.transform_points(bl.vertices, T(PARK)).max(0).round(1).tolist())


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
print("CR Touch-fläns mot armplatta:", round(float(arm.bounds[0, 2] - bl.bounds[1, 2]), 2))
for z, o, nm in ((64.25, ref["tool_mount_b"], "undre"), (125.25, ref["tool_mount_t"], "övre")):
    print(f"M5 {nm}: boss mot fäste {[nx([-5, 43.95 + r * np.cos(v), z + r * np.sin(v)], [-1, 0, 0], o) for r, v in ((4.5, 0), (4.5, 1.57), (4.5, 3.14), (4.5, 4.71))]}, hål fritt {nx([-5, 43.95, z], [-1, 0, 0], o) is None}")
print("kamerakortet: distans mot kortets baksida, ring runt hålet:", [nx([x + 1.5, y, E["kort_bak"] - .2], [0, 0, 1], torn) for x, y in E["kort_hal"]])
print("kamerakortet: tapp i hålet:", [bool(torn.contains([[x, y, E["kort_bak"] - .5]])[0]) for x, y in E["kort_hal"]])
print("kamerakortet: M3-hålets djup över kortets framsida (minst 10):", [nx([x, y, E["kort_fram"] + .05], [0, 0, 1], torn) for x, y in E["klammor"]])
for nm, o, d in (("botten", [30, 66, 60.5], [0, 0, -1]), ("ramp", [65, 66, 100], [0, 0, -1]), ("tak", [45, 60, E["topp"] - 4.5], [0, 0, 1]), ("front", [45, 51.4, 140], [0, -1, 0]), ("rygg", [12.5, 60, 90], [-1, 0, 0]), ("CSI-golv", [90, 67, 136.5], [0, 0, -1])):
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

# Korten måste ligga inne i det slutna rummet: inte i väggen och inte ute i luften utanför den svepande formen.
for nm in ("Pi", "LM2596_A", "LM2596_B", "ADXL", "Kort", "Flatkontakt", "Mikrofon"):
    lo, hi = np.array(E[nm][0]), np.array(E[nm][1])
    g = np.array(np.meshgrid(np.linspace(lo[0], hi[0], 53), np.linspace(lo[1] + .05, hi[1] - .05, 4), np.linspace(lo[2], hi[2], 41), indexing="ij")).reshape(3, -1).T
    i_vagg = int(torn.contains(g).sum())
    fritt = [int((~torn.ray.intersects_any(g, np.tile(d, (len(g), 1)))).sum()) for d in ([0, 0, -1], [0, 0, 1], [-1, 0, 0], [1, 0, 0])]
    kant = g[(np.isclose(g[:, 0], lo[0]) | np.isclose(g[:, 0], hi[0]) | np.isclose(g[:, 2], lo[2]) | np.isclose(g[:, 2], hi[2]))]
    print(f"{nm}: punkter i väggen {i_vagg} av {len(g)}, punkter utanför formen (fri stråle ned/upp/bak/fram) {fritt}, minsta spel kant-vägg {torn.nearest.on_surface(kant)[1].min():.2f} mm")
print("Pi: tappar i hålen:", [bool(torn.contains([[x, E["Pi"][0][1] + .7, z]])[0]) for x, z in E["pi_hal"]])
print("panel mot torn, punkter av panelens fingrar inne i tornet:", (lambda q: int(torn.contains(q[q[:, 1] < 70]).sum()))(lock.sample(40000)))
for x, z in E["panel_hal"]:
    v = np.linspace(0, 6.28, 16, endpoint=False)
    p = np.c_[x + 4.2 * np.cos(v), np.full(16, torn.bounds[1, 1] + 5), z + 4.2 * np.sin(v)]
    print(f"panelhål ({x:.0f}, {z:.1f}): godsring runt huvudet täckt av panelen {int(lock.ray.intersects_any(p, np.tile([0, -1, 0], (16, 1))).sum())}/16, skruvhål i pelare {nx([x, 70.0, z], [0, -1, 0], torn)}")

# Flatkabeln som ark, 16 mm bred, från kamerakontakten via två 45-gradersvikningar till Pi-kortets kortsida.
B = E["ffc_b"] / 2
z_k = E["kort_bak"] + 1.3
cx, z_pi, x_pi, y_pi, y_k, y_a = E["lins"][0], (E["Pi"][0][2] + E["Pi"][1][2]) / 2, E["Pi"][1][0], E["Pi"][1][1] + .8, E["Kort"][1][1] - 1.0, 67.0
def ark(pts):
    """pts: mittlinjens punkter (x, y, z) med breddriktning (bx, by, bz); arkets punkter returneras."""
    ut = []
    for (a, ba), (c, bc) in zip(pts, pts[1:]):
        for t in np.linspace(0, 1, 40):
            m = np.array(a) * (1 - t) + np.array(c) * t
            bb = np.array(ba) * (1 - t) + np.array(bc) * t
            ut += [m + bb * u * B for u in np.linspace(-1, 1, 17)]
    return np.array(ut)
ex, ez = (1, 0, 0), (0, 0, 1)
d45 = (.7071, 0, .7071)
d = 6.0
P1, P2 = (cx, y_a, z_pi - d), (cx - d, y_a, z_pi)
bana = [((cx, y_k, z_k), ex), ((cx, y_a - 2.0, z_k + .3), ex), ((cx, y_a, z_k + 3.0), ex), (P1, ex), (P1, d45), (P2, d45), (P2, ez), ((cx - 8.0, y_a, z_pi), ez), (((cx - 8.0 + x_pi) / 2, (y_a + y_pi) / 2, z_pi), ez), ((x_pi + .5, y_pi, z_pi), ez)]
q = ark(bana)
print(f"flatkabel som ark, {E['ffc_b']:.0f} mm: punkter i tornet {int(torn.contains(q).sum())} av {len(q)}, punkter utanför formen {int((~torn.ray.intersects_any(q, np.tile([0, 0, 1], (len(q), 1)))).sum())}, minsta spel {torn.nearest.on_surface(q)[1].min():.2f} mm")
for y in (45, 55, 60):
    print(f"kamerafickans yttervägg vid y {y}:", [nx([E["lins"][0] + 12.65, y, z], [1, 0, 0], torn) for z in (134, 136, 138, 140)])

mx, mz, mv, my = E["magnet"]
ut = np.array([np.cos(np.radians(mv)), 0, np.sin(np.radians(mv))])
start = np.array([mx, my, mz]) + ut * 3
h = stralar(start, -ut, torn)
print(f"magnetens hud mot armen: {round(h[1] - h[0], 2) if len(h) > 1 else None} mm; hålet öppet bakåt: {len(stralar(start, ut, torn)) == 0}")

# Hylsan utgick 2026-11-11; CR Touchen skruvas direkt i armfoten.

# Mikrofonens ljudhål: fri stråle genom panelen och gods runt hålet. Krock för kort,
# lödkant och ledningsväg till Pi:ns stiftlist kontrolleras exakt i CAD (se README).
mx, mz, md = E["mik"]
print("mikrofon: ljudhål fritt genom panelen:", not bool(lock.ray.intersects_any([[mx, 60.0, mz]], [[0, 1, 0]])[0]),
      "panelgods bredvid hålet:", bool(lock.contains([[mx + md / 2 + .6, 71.5, mz]])[0]))
