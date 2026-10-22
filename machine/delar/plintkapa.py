"""Plintkåpa med inbyggd dragavlastning för Mean Well HDR-60-24 på undre strutplattan.

Kåpan sitter över aggregatets nätända (plint 5/6). Aggregatet är en trappa: ändsteget med plintarna är
bara ca 13 mm långt och ca 32 mm djupt, nästa steg ca 43 mm, mitten 54,5 mm. Kåpan täcker bara ändsteget
och slutar vid trappans stigning. Den skruvas i plattan med flänsar. DIN-skenan (dinskena_ts35.py) ger 7,5 mm till aggregatets rygg.
Nätsladden går ut genom kortväggen och klämms i en stos som sitter ihop med kåpan; ett lock med
fyra skruvar går genom lock + stos in i plattan, så sladdens drag tas av plattan.

Utskrift (PETG): båda delarna som de ligger i filen. Kåpan står på flänsarna med öppningen nedåt;
taket bryggar ca 54 mm (blir lite hängigt på insidan, påverkar inte funktionen). Inget stöd behövs.
Inte ett certifierat beröringsskydd; elkunnig person kontrollerar nätinstallationen (LR-22).
Kör:  uv run --no-project --with manifold3d --with numpy python3 plintkapa.py
"""
import struct
import numpy as np
import manifold3d as m

# --- Aggregatet (HDR-60, databladet; tolerans ±0,5) ---
PSU_B = 52.5             # bredd (över skenan)
END_DJUP = 32.5          # djup från ryggen i ändsteget med plintarna (mätt i databladets sidovy, ±1 mm)
SKENA_H = 7.5            # ryggen ligger på skenans flänsar (z = 7,5 från plattan)
LANG_ANDE = 13.2         # ändstegets längd (till trappans stigning)

# --- Kåpa ---
T = 2.4                  # vägg
LUFT_X = 1.0             # total sidoluft (0,5 per sida)
LUFT_Z = 1.0             # luft över framsidan
INNER_B = PSU_B + LUFT_X
INNER_H = SKENA_H + END_DJUP + LUFT_Z
RUM = 16.0               # fritt rum mellan kortvägg och aggregatets ände (ledare, mantelände)
SPALT = 0.8              # kåpan slutar så här före trappans stigning
LC = RUM + LANG_ANDE - SPALT   # invändig längd; öppningen stängs av aggregatets egen stigning
FL_B = 14.0              # flänsbredd
FL_T = 3.0               # flänstjocklek
GUSS = 7.0               # 45°-stöd (fillet) mellan vägg och fläns
SKR_D = 3.5              # hål för 3 mm träskruv (max 8 mm långa mot 6 mm MDF)
SKR_F = 7.0              # försänkning
SKR_Y = (4.0, LC / 2, LC - 4.0)
FAS = 2.0                # fasning av kåpans yttre kanter
FAS_FL = 3.0             # fasade hörn på flänsar, stos och lock

# --- Sladd och dragavlastning ---
KABEL_D = 6.5            # lampsladdens ytterdiameter: MÄT och ändra
ZK = 12.0                # sladdens centrumhöjd över plattan (= stosens höjd)
K_B, K_L = 24.0, 30.0    # stosens bredd och längd (utåt från kortväggen)
K_LOCK_H = 6.0
K_SKR_X = 8.5
K_SKR_Y = (6.0, K_L - 6.0)
K_PINCH = 0.3            # spåret är så mycket mindre än sladden per sida (kläm)


def box(x0, x1, y0, y1, z0, z1):
    return m.Manifold.cube([x1 - x0, y1 - y0, z1 - z0]).translate([x0, y0, z0])


def prisma(pts, z0, z1):
    return m.CrossSection([pts]).extrude(z1 - z0).translate([0, 0, z0])


def oktagon(x0, x1, y0, y1, c):
    return [(x0 + c, y0), (x1 - c, y0), (x1, y0 + c), (x1, y1 - c),
            (x1 - c, y1), (x0 + c, y1), (x0, y1 - c), (x0, y0 + c)]


def cyl_z(r1, r2, h, x, y, z):
    return m.Manifold.cylinder(h, r1, r2, 48).translate([x, y, z])


def cyl_y(r1, r2, y0, y1, x, z):
    """Cylinder längs y, r1 vid y0 och r2 vid y1."""
    return m.Manifold.cylinder(y1 - y0, r1, r2, 48).rotate([-90, 0, 0]).translate([x, y0, z])


def stod_fillet(s, y0, y1):
    x0 = s * (INNER_B / 2 + T)
    pts = [(x0, FL_T), (x0 + s * GUSS, FL_T), (x0, FL_T + GUSS)]
    cs = m.CrossSection([pts if s > 0 else pts[::-1]])
    return cs.extrude(y1 - y0).rotate([90, 0, 0]).translate([0, y1, 0])


def flans(s):
    """Fläns på sida s med fasade yttre hörn (vägghörnen gömda i kåpan)."""
    xa = s * (INNER_B / 2 + T / 2)
    xb = s * (INNER_B / 2 + T + FL_B)
    c = FAS_FL
    pts = [(xa, -T), (xb - s * c, -T), (xb, -T + c), (xb, LC - c), (xb - s * c, LC), (xa, LC)]
    return prisma(pts if s > 0 else pts[::-1], 0, FL_T)


def kapa():
    hw = INNER_B / 2 + T
    H = INNER_H + T
    # yttre skal: fasade lodräta hörn och fasad överkant (hull av två oktagoner)
    nedre = prisma(oktagon(-hw, hw, -T, LC, FAS), 0, H - FAS)
    ovre = prisma(oktagon(-hw + FAS, hw - FAS, -T + FAS, LC - FAS, FAS * 0.5), H - FAS, H)
    skal = (nedre + ovre).hull()
    rum = box(-INNER_B / 2, INNER_B / 2, 0, LC + 1, -1, INNER_H)
    k = skal - rum
    # sladdstos (sitter ihop med kortväggen) med spår överst
    c = FAS_FL
    stos = prisma([(-K_B / 2, -T + 1), (-K_B / 2, -T - K_L + c), (-K_B / 2 + c, -T - K_L),
                   (K_B / 2 - c, -T - K_L), (K_B / 2, -T - K_L + c), (K_B / 2, -T + 1)], 0, ZK)
    k = k + stos
    # hål genom kortväggen med fas på båda sidor, och spår i stosen
    rh = (KABEL_D + 1.5) / 2
    k = k - cyl_y(rh, rh, -T - 1, 1, 0, ZK)
    k = k - cyl_y(rh + 1.5, rh, -T - 0.01, -T + 1.5, 0, ZK) - cyl_y(rh, rh + 1.5, -1.5 + 0.01, 0.01, 0, ZK)
    k = k - cyl_y(KABEL_D / 2 - K_PINCH, KABEL_D / 2 - K_PINCH, -T - K_L - 1, -T + 0.5, 0, ZK)
    k = k - cyl_y(KABEL_D / 2 - K_PINCH + 1.0, KABEL_D / 2 - K_PINCH, -T - K_L - 0.01, -T - K_L + 1.0, 0, ZK)
    for sx in (-K_SKR_X, K_SKR_X):
        for yy in K_SKR_Y:
            k = k - cyl_z(1.7, 1.7, ZK + 2, sx, -T - yy, -1)
    # flänsar med fillet och försänkta skruvhål
    for s in (1, -1):
        k = k + flans(s) + stod_fillet(s, -T, LC)
        xs = s * (INNER_B / 2 + T + GUSS + (FL_B - GUSS) / 2)
        for y in SKR_Y:
            k = k - cyl_z(SKR_D / 2, SKR_D / 2, FL_T + 2, xs, y, -1)
            k = k - cyl_z(SKR_D / 2, SKR_F / 2, FL_T - 1.0 + 0.01, xs, y, 1.0)
    return k


def lock():
    c = FAS_FL
    pts = [(-K_B / 2, 0), (K_B / 2, 0), (K_B / 2, K_L - c), (K_B / 2 - c, K_L),
           (-K_B / 2 + c, K_L), (-K_B / 2, K_L - c)]
    l = prisma(pts, 0, K_LOCK_H) - cyl_y(KABEL_D / 2 - K_PINCH, KABEL_D / 2 - K_PINCH, -1, K_L + 1, 0, 0)
    l = l - cyl_y(KABEL_D / 2 - K_PINCH + 1.0, KABEL_D / 2 - K_PINCH, -0.01, 1.0, 0, 0)
    for sx in (-K_SKR_X, K_SKR_X):
        for y in K_SKR_Y:
            l = l - cyl_z(1.7, 1.7, K_LOCK_H + 2, sx, y, -1) \
                - cyl_z(1.7, 3.3, 1.7, sx, y, K_LOCK_H - 1.7 + 0.01) - cyl_z(3.3, 3.3, 2, sx, y, K_LOCK_H)
    # utskrift: spåret uppåt (vänd), y spegelvänds tillbaka in i positivt
    return l.rotate([180, 0, 0]).translate([0, K_L, K_LOCK_H])


def stl(man, fil):
    mesh = man.to_mesh()
    v = np.array(mesh.vert_properties)[:, :3]
    tri = v[np.array(mesh.tri_verts)]
    with open(fil, 'wb') as f:
        f.write(fil.encode().ljust(80, b' ')[:80])
        f.write(struct.pack('<I', len(tri)))
        for p in tri:
            n = np.cross(p[1] - p[0], p[2] - p[0])
            n = n / (np.linalg.norm(n) or 1)
            f.write(struct.pack('<12fH', *n, *p.ravel(), 0))
    vol = np.einsum('ij,ij->i', tri[:, 0], np.cross(tri[:, 1], tri[:, 2])).sum() / 6
    print(fil, len(tri), 'trianglar, volym', round(vol), 'mm3, bbox', v.min(0).round(1), v.max(0).round(1), man.status())


if __name__ == '__main__':
    stl(kapa(), 'plintkapa.stl')
    stl(lock(), 'plintkapa_lock.stl')
