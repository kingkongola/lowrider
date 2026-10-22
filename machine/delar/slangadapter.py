"""Reduceradapter för dammskon: 69,5 mm borrning -> 46 mm slang (ID).

Två filer: slangadapter_46mm.stl (hylsan mot bordet) och slangadapter_46mm_upp-och-ned.stl (stosen mot\nbordet, inga fria överhäng i slicern). 4 väggar (0,4 mm munstycke), PLA.
Konens vägg är lika tjock (1,6 mm) hela vägen: en tjockare vägg som smalnar av fick slicern att lägga
ut "floating vertical shell" över hela konen. Insidan får därför en avsats där konen börjar.
Kör: uv run --no-project --with manifold3d --with numpy python3 slangadapter.py  -> slangadapter_46mm.stl
"""
import struct
import numpy as np
import manifold3d as m

# Mått (mm)
SKO_ID = 69.5            # uppmätt borrning i dammskon
PRESS = -0.05            # radie; hylsa OD 69,4 = 0,1 mindre än borrningen
HYLSA_R = SKO_ID / 2 + PRESS
HYLSA_H = 16.0           # hur långt hylsan går ned i skon
FLANGE_R = 36.4          # skons kant är en ring r 34,5-37,0; litet överhäng (1,7 mm) så det går att skriva ut
FLANGE_H = 3.0
SLANG_ID = 46.0
STOS_R = SLANG_ID / 2 - 0.2      # slangen trycks över; stos OD 45,6
RIBB = 0.6               # en liten ribba vid kanten; slät yta under för slangklämman
STOS_H = 30.0
KON_H = 25.0
VAGG_STOS = 1.6          # 4 linjer à 0,4; klämman ligger här
VAGG_HYLSA = 1.6
INRE_STOS_R = STOS_R - VAGG_STOS   # fri öppning i stosen (ID 42,4)
INRE_HYLSA_R = HYLSA_R - VAGG_HYLSA

z0 = 0.0
z1 = z0 + HYLSA_H
z2 = z1 + FLANGE_H
z3 = z2 + KON_H
z4 = z3 + STOS_H

# Profil (r, z), moturs, sluten
yttre = [
    (INRE_HYLSA_R, z0), (HYLSA_R, z0),
    (HYLSA_R, z1), (FLANGE_R, z1), (FLANGE_R, z2),
    (STOS_R, z3),
    (STOS_R, z4 - 5), (STOS_R + RIBB, z4 - 3), (STOS_R, z4 - 1),
    (STOS_R, z4),
    (INRE_STOS_R, z4),
    (INRE_STOS_R, z3),
    (INRE_STOS_R + (FLANGE_R - STOS_R), z2),
    (INRE_HYLSA_R, z2),
]
N = 180


def kropp(profil):
    """Roterar profilen (r, z) runt z med manifold3d; CrossSection kräver moturs ordning."""
    area = sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(profil, profil[1:] + profil[:1]))
    pts = profil if area > 0 else profil[::-1]
    return m.CrossSection([pts]).revolve(N)


def stl(man, fil):
    mesh = man.to_mesh()
    v = np.array(mesh.vert_properties)[:, :3]
    tri = v[np.array(mesh.tri_verts)]
    with open(fil, 'wb') as f:
        f.write(b'slangadapter'.ljust(80, b' '))
        f.write(struct.pack('<I', len(tri)))
        for p in tri:
            nv = np.cross(p[1] - p[0], p[2] - p[0])
            nv = nv / (np.linalg.norm(nv) or 1)
            f.write(struct.pack('<12fH', *nv, *p.ravel(), 0))
    return tri


if __name__ == '__main__':
    k = kropp(yttre)
    t = stl(k, 'slangadapter_46mm.stl')
    print(len(t), 'trianglar; volym', round(k.volume()), 'mm3; genus', k.genus(), '; status', k.status(),
          '; höjd', z4, 'mm; hylsa OD', 2 * HYLSA_R, 'stos OD', 2 * STOS_R)
    # Upp och ned (stosen mot bordet): inga överhäng över 32°, flänsens plana sida överst. Avsatsen behövs inte.
    avsats = (INRE_STOS_R + (FLANGE_R - STOS_R), z2)
    vand = kropp([p for p in yttre if p != avsats]).rotate([180, 0, 0]).translate([0, 0, z4])
    stl(vand, 'slangadapter_46mm_upp-och-ned.stl')
    print('upp och ned: volym', round(vand.volume()), 'mm3; status', vand.status())
