"""DIN-skena TS35/7,5 (EN 60715), 70 mm, för Mean Well HDR-60-24 på undre strutplattan.

Plan mot 6 mm MDF, träskruv genom bottnen (försänkta hål, förskjutna rader så att några passar).
Skrivs ut PETG, upp och ned: flänsarna mot bordet, bottnen överst (broar 23 mm).
Kör:  uv run --no-project --with manifold3d --with numpy python3 dinskena_ts35.py
Gör: dinskena_ts35.stl
"""
import numpy as np
import manifold3d as m

# Mått (mm)
L = 70.0
BREDD = 35.0             # över flänsarna (TS35)
KROPP = 27.0             # skenans kropp i botten (TS35)
HOJD = 7.5               # TS35/7,5
VAGG = 2.0               # sidoväggar
BOTTEN = 2.5             # botten mot MDF
FLANS_T = 1.2            # flänstjocklek (original 1,0); klipset hakar under
HAL_D = 3.5              # genomgående hål för 3-3,5 mm träskruv
FORS_D = 7.5             # försänkningens diameter överst
RAD_Y = 5.5              # radernas avstånd från mitten (insida vägg = 11,5)
TEGEL = 10.0             # delning längs skenan


def prisma(x0, x1, y0, y1, z0, z1):
    return m.Manifold.cube([x1 - x0, y1 - y0, z1 - z0]).translate([x0, y0, z0])


# Användningsläge: botten på z=0, flänsarna överst (z=HOJD). Längd längs x.
kropp = prisma(0, L, -KROPP / 2, KROPP / 2, 0, HOJD)
kanal = prisma(-1, L + 1, -KROPP / 2 + VAGG, KROPP / 2 - VAGG, BOTTEN, HOJD + 1)
flans = prisma(0, L, -BREDD / 2, BREDD / 2, HOJD - FLANS_T, HOJD)
oppning = prisma(-1, L + 1, -KROPP / 2 + VAGG, KROPP / 2 - VAGG, HOJD - FLANS_T - 1, HOJD + 1)
skena = (kropp - kanal) + (flans - oppning)

# Försänkta hål
h_ned = HAL_D / 2
for rad, (y, x_start) in enumerate(((-RAD_Y, 5.0), (RAD_Y, 10.0))):
    x = x_start
    while x <= L - 5.0 + 1e-6:
        hal = m.Manifold.cylinder(BOTTEN + 2, h_ned, h_ned, 48).translate([x, y, -1])
        # försänkning: smal nere, bred uppe (0,4 mm rakt hål kvar i botten)
        kon = m.Manifold.cylinder(BOTTEN - 0.4, h_ned, FORS_D / 2, 48).translate([x, y, 0.4])
        skena = skena - hal - kon
        x += TEGEL

# Vänd upp och ned för utskrift (flänsarna mot bordet)
skena = skena.rotate([180, 0, 0]).translate([0, 0, HOJD])
mesh = skena.to_mesh()
v = np.array(mesh.vert_properties)[:, :3]
t = np.array(mesh.tri_verts)
tri = v[t]
import struct
with open('dinskena_ts35.stl', 'wb') as f:
    f.write(b'dinskena TS35/7,5'.ljust(80, b' '))
    f.write(struct.pack('<I', len(tri)))
    for p in tri:
        n = np.cross(p[1] - p[0], p[2] - p[0]); n = n / (np.linalg.norm(n) or 1)
        f.write(struct.pack('<12fH', *n, *p.ravel(), 0))
vol = np.einsum('ij,ij->i', tri[:, 0], np.cross(tri[:, 1], tri[:, 2])).sum() / 6
print(len(tri), 'trianglar, volym', round(vol), 'mm3, bbox', v.min(0).round(1), v.max(0).round(1), 'genus', skena.genus(), 'status', skena.status())
