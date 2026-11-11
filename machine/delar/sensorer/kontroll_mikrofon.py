"""Exakt CAD-kontroll av INMP441-mikrofonen i sidopanelen. Avbryter med fel om något krockar.

Kontrollerar med booleska volymer i build123d (inte STL-stickprov):
kortet, lödkanten med sex ledningar, ledningsvägen upp till Pi:ns stiftlist och ljudhålet.
Kortmåtten är nominella (14 x 14 mm); mät levererad modul och ändra MIK_RUTA vid behov.

Kör: python kontroll_mikrofon.py
"""
import sidotorn as S
from kontrollhjalp import krock as _krock

t, p = S.torn(), S.sidopanel()
mx, mz = S.MIK
Y1 = S.Y1


def krock(a, b):
    return _krock(a, b)


kort = S.box((mx - 7, Y1 - 2 - 2.5, mz - 7), (mx + 7, Y1 - 2.05, mz + 7))
lod = S.box((mx - 7, Y1 - 2 - 4.5, mz + 7), (mx + 7, Y1 - 2.05, mz + 15))      # lödtenn och sex ledningar
vag = S.box((mx - 4, Y1 - 2 - 4.5, mz + 7), (mx + 4, Y1 - 2.05, 166))          # upp till Pi:ns stiftlist
hal = S.cyl_y(mx, mz, Y1 - 2.2, Y1 + .2, S.MIK_HAL_D - .05)
ring = S.cyl_y(mx, mz, Y1 - 1.9, Y1 - .5, S.MIK_HAL_D + 1.2) - S.cyl_y(mx, mz, Y1 - 2, Y1, S.MIK_HAL_D + .1)

fel = []
for namn, a in (("kortet", kort), ("lödkanten", lod), ("ledningsvägen till Pi", vag)):
    for del_, b in (("tornet", t), ("panelen", p)):
        v = krock(a, b)
        print(f"{namn} mot {del_}: {v:.3f} mm3")
        if v > 0.01:
            fel.append(f"{namn} krockar med {del_}")
v = krock(hal, p)
print(f"gods i ljudhålet: {v:.3f} mm3")
if v > 0.01:
    fel.append("ljudhålet är igensatt")
v = krock(ring, p)
print(f"gods runt ljudhålet: {v:.2f} av {ring.volume:.2f} mm3")
if v < 0.9 * ring.volume:
    fel.append("för lite gods runt ljudhålet för tätningen")
if fel:
    raise SystemExit("UNDERKÄND: " + "; ".join(fel))
print("GODKÄND: mikrofonens kort, lödning, ledningsväg och ljudhål")
