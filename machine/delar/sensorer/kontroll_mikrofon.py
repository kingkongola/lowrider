"""Exakt CAD-kontroll av INMP441-mikrofonen i sidopanelen. Avbryter med fel om något krockar.

Kontrollerar med booleska volymer i build123d (inte STL-stickprov):
det runda kortet (uppmätt Ø14,2 x 2,0 mm), lödtenn och ledningar bakom chipsidan,
ledningsvägen upp till Pi:ns stiftlist och ljudhålet. Negativtest: ett för stort kort ska krocka.

Kör: python kontroll_mikrofon.py
"""
import sidotorn as S
from kontrollhjalp import krock as _krock

t, p = S.torn(), S.sidopanel()
mx, mz = S.MIK
Y1 = S.Y1


def krock(a, b):
    return _krock(a, b)


kort = S.cyl_y(mx, mz, Y1 - 2.05 - S.MIK_T - .45, Y1 - 2.05, S.MIK_D)          # kortet + skumtejpens plats
lod = S.cyl_y(mx, mz, Y1 - 2 - 4.5, Y1 - 2.05 - S.MIK_T - .45, S.MIK_D)        # lödtenn och ledningar bakåt
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
# Negativtest: ett kort som är 0,6 mm större än ramen ska krocka, annars mäter kontrollen inget.
stor = S.cyl_y(mx, mz, Y1 - 4.5, Y1 - 2.05, S.MIK_RUTA + .6)
v = krock(stor, p)
print(f"negativtest, för stort kort mot panelen: {v:.3f} mm3")
if v <= 0.01:
    fel.append("negativtestet krockade inte; kontrollen är blind")
if fel:
    raise SystemExit("UNDERKÄND: " + "; ".join(fel))
print("GODKÄND: mikrofonens kort, lödning, ledningsväg och ljudhål")
