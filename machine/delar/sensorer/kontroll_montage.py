"""Simulerad montering: når verktyget varje skruv i den ordning delarna sätts ihop?

Varje steg har ett verktyg som cylinder (skaft eller nyckel plus skalle) och de delar som redan
sitter på plats i just det steget. Krock = verktyget går inte att föra fram. Exakta booleska
volymer i build123d. Avbryter med UNDERKÄND om något steg är blockerat.

Kör: python kontroll_montage.py
"""
import math

from build123d import Cylinder, Pos, Rot

import hornfaste as hf
import sidotorn as S
from kontrollhjalp import krock as _krock

Y1 = S.Y1
torn_utan, arm, crt, panel = S.torn(), S.arm(), S.crtouch(), S.sidopanel()
stopp_n, stopp_o = S.stoppdelar()
torn = torn_utan + stopp_n + stopp_o      # från steg 1c sitter stoppdelarna på
servo = S.servo_attrapp()
P = S.parkera


def cyl_y(x, z, y0, y1, d):
    return S.cyl_y(x, z, min(y0, y1), max(y0, y1), d)


def cyl_x(y, z, x0, x1, d):
    return S.cyl_x(y, z, min(x0, x1), max(x0, x1), d)


def cyl_z(x, y, z0, z1, d):
    return Pos(x, y, (z0 + z1) / 2) * Cylinder(d / 2, abs(z1 - z0))


def krock(verktyg, delar):
    ut = {}
    for namn, d in delar.items():
        v = _krock(verktyg, d, namn)
        if v > 0.05:
            ut[namn] = round(v, 1)
    return ut


steg = []
# 1. Servot in framifrån, fyra skruvar genom öronen. Skallen ligger mot öronens framsida (y 38,8).
for x in (S.PX - 33.3, S.PX + 14):
    for z in (S.PZ - 4.7, S.PZ + 4.7):
        steg.append((f"1 servoskruv x{x:.0f} z{z:.0f} (mejsel Ø6 framifrån)",
                     cyl_y(x, z, -80, 38.8 - 2.5, 6.0), {"torn": torn_utan}))
# 1b. Servokroppen in framifrån genom ramens fönster (kropp och öron svepta 60 mm).
kropp = S.box((14.8, 32.6 + S.SERVO_DY - 60, 33.6), (55.2, 73 + S.SERVO_DY, 53.6))
x0, ky = S.PX - 30.2, S.kabel_y()
tatning = S.box((x0 - S.KABEL_C, ky - S.KABEL_H / 2 - 60, S.PZ - S.KABEL_B / 2), (x0, ky + S.KABEL_H / 2, S.PZ + S.KABEL_B / 2))   # tätningen svepts med kroppen
oron = S.box((5.1, 40.8 + S.SERVO_DY - 60, 33.6), (64.9, 43.3 + S.SERVO_DY, 53.6))
steg.append(("1b servokroppen och kabeltätningen in genom ramen (svep), stoppdelarna inte på", kropp + oron + tatning, {"torn": torn_utan}))
# 1c. Stoppdelarna mot ramens framsida, två M3 x 20 var; servot sitter, armen inte på.
for x, z in S.STOPP_SKRUV:
    seat = (min(stopp_n.bounding_box().min.Y, 99) if z < 40 else 30.5) + 3.5
    steg.append((f"1c stoppdelens skruv x{x:.0f} z{z:.0f} (mejsel Ø5,5 framifrån)", cyl_y(x, z, -80, seat - 3.2, 5.5),
                 {"torn": torn_utan, "servo": servo, "stopp nedre": stopp_n, "stopp övre": stopp_o}))
# 2. Hornet i armens formficka på bänken; armen med hornet rakt in på servoaxeln (15 mm i steg).
#    Servots axel är avsedd anläggning för hornets nav; resten av servot och tornet får inte röras.
axel = S.cyl_y(S.PX, S.PZ, 0, 60, 6.2)
paket = arm + S.horn_lage(hf.horn())
for d in [0.2, 0.5] + list(range(1, 16)):
    steg.append((f"2a armen med hornet {d} mm från axeln", Pos(0, -d, 0) * paket,
                 {"torn": torn, "servo utom axeln": servo - axel}))
# 3. Mittskruven M3 x 10 utifrån genom armens botten; insex 2,5 med skaft Ø5,5 rakt längs axeln.
skalle_y = 32.6 + S.SERVO_DY - hf.H_MONTERAT - hf.BOTTEN - hf.SKALLE[1]
steg.append(("3 mittskruven M3 x 10 genom armen (insex 2,5, skaft Ø5,5 utifrån)",
             cyl_y(S.PX, S.PZ, skalle_y - .05, skalle_y - 80, 5.5),
             {"torn": torn, "servo": servo, "arm": arm, "horn": S.horn_lage(hf.horn())}))
# 4. M5 till verktygsfästet, insexnyckel från tornets insida (+x) med allt monterat.
#    Tornet monteras med armen utfälld.
for z in S.M5_Z:
    alla = {"torn": torn, "servo": servo, "arm utfälld": arm, "CR Touch utfälld": crt}
    steg.append((f"4 M5 z{z:.0f}, armen utfälld (insex 4, skalle och bricka Ø9 rakt utifrån)", cyl_x(43.95, z, 9.6, 130, 9.0), alla))
# 5. Kameralocket rakt upp underifrån (15 mm i steg), sedan de två klämskruvarna genom locket.
#    Skallen sitter under lockets öra, 1 mm lägre än utan lock; verktyget når den genom plattans hål.
lock = S.kameralock()
for d in [0.2, 0.5] + list(range(1, 16)):
    steg.append((f"5a kameralocket {d} mm under sitt läge", Pos(0, 0, -d) * lock, {"torn": torn}))
skalle_z = S.KORT_FRAM - S.LOCK_ORA_T - 3.0
for x, y in S.KLAMMOR:
    steg.append((f"5b kameraskruv x{x:.0f} genom locket (insex 2,5 Ø3 sista {skalle_z - S.BUK + .05:.2f} mm i tornets hål, skaft Ø6 från buken)",
                 cyl_z(x, y, skalle_z - .05, S.BUK - .05, 3.0) + cyl_z(x, y, S.BUK - .05, S.BUK - 80, 6.0),
                 {"torn": torn, "kameralock": lock, "arm parkerad": P(arm), "CR Touch parkerad": P(crt)}))
    steg.append((f"5c kameraskruvens skalle x{x:.0f} i sitt läge under örat",
                 cyl_z(x, y, skalle_z, skalle_z + 3.0, 5.5), {"torn": torn, "kameralock": lock}))
# 6. ADXL-skruvar från panelsidan innan Pi:n sitter.
for x, z in S.ACC_HAL:
    steg.append((f"6 ADXL-skruv x{x:.0f} (mejsel Ø6 från panelsidan)", cyl_y(x, z, S.PI_Y + 3.6, Y1 + 60, 6.0), {"torn": torn}))
# 7. Pi:n rakt in från panelsidan (inga pelare i vägen sedan 2026-11-11).
#    Kortet 1,4 mm, komponenter 1,6 mm, stiftlist med lödda ledningar 11 mm vid nederkanten.
cx, cz = S.PI_CENTER


def pi_kropp(dz, y0, y1):
    k = S.box((cx - 32.5, y0, cz - 15 + dz), (cx + 32.5, y1 + 3.0, cz + 15 + dz))
    k += S.box((cx - 25.4, y0, cz - 11.5 - 2.6 + dz), (cx + 25.4, y1 + 11.0, cz - 11.5 + 2.6 + dz))
    for x, z in S.PI_HAL:
        k -= cyl_y(x, z + dz, S.PI_Y - 1, Y1 + 20, 3.0)
    return k


TOPP_TAPP = S.PI_Y + 1.9
steg.append(("7a Pi:n rakt in till strax ovanför tapparna (med lödda ledningar)", pi_kropp(0, TOPP_TAPP + .1, Y1 + 5), {"torn": torn}))
steg.append(("7b Pi:n ned på tapparna", pi_kropp(0, S.PI_Y + .05, TOPP_TAPP + 1.5), {"torn": torn}))
# 8. LM2596 in i fickorna.
for k, x0 in S.REG_X0.items():
    lm = S.box((x0, S.PI_Y + .05, S.REG_Z0), (x0 + 21, Y1 + 5, S.REG_Z0 + 43))
    steg.append((f"8 LM2596 {k} in i fickan (svep)", lm, {"torn": torn}))
# 9. Panelskruvarna utifrån.
for x, z in S.PANEL_HAL:
    steg.append((f"9 panelskruv x{x:.0f} z{z:.0f} (mejsel Ø6 utifrån)", cyl_y(x, z, Y1 + .1, Y1 + 80, 6.0),
                 {"servo": servo, "arm": arm, "arm parkerad": P(arm)}))
for x, z in S.PI_SKRUV:
    steg.append((f"9 Pi-/panelskruv M2.5 x{x:.0f} z{z:.0f} (mejsel Ø5 utifrån)", cyl_y(x, z, Y1 + .1, Y1 + 80, 5.0),
                 {"servo": servo, "arm": arm, "arm parkerad": P(arm)}))
steg.append(("11 kopplingskortets yta på framväggen (kort, löd och kondensator)", S.box(*S.KOPPLINGSKORT),
             {"torn": torn, "panel": panel}))
# 12. microSD skjuts in utifrån genom springan i bakväggen, efter att Pi:n sitter.
sd0 = (S.PI_CENTER[0] - 32.5 - 2.6, S.PI_Y + 1.4, S.SD_Z[0] + .5)
sd1 = (S.PI_CENTER[0] - 32.5 + 12.0, S.PI_Y + 2.4, S.SD_Z[1] - .5)
steg.append(("12 microSD in utifrån genom bakväggen (kortets väg)", S.box((sd0[0] - 15, sd0[1], sd0[2]), sd1), {"torn": torn}))
# 9b. Panelen förs rakt in med fingrar och mikrofonram (25 mm i 1 mm-steg). Pi, LM2596 och
#     mikrofonkortet sitter redan; fingrarna ska stanna 0,05 mm före korten.
from build123d import Pos as _Pos
kort = S.box((S.PI_CENTER[0] - 32.5, S.PI_Y, S.PI_CENTER[1] - 15), (S.PI_CENTER[0] + 32.5, S.PI_Y + 1.4, S.PI_CENTER[1] + 15))
for x0 in S.REG_X0.values():
    kort += S.box((x0, S.PI_Y, S.REG_Z0), (x0 + 21, S.PI_Y + 1.6, S.REG_Z0 + 43))
for d in [0.3] + list(range(1, 26)):
    steg.append((f"9b panelen {d} mm före sitt läge", _Pos(0, d, 0) * panel, {"torn": torn, "kort": kort}))
# 10. Magneten in bakifrån i parkeringsstoppet.
mx, mz, vinkel = S.magnet_lage(S.PROB[0])
ut = (math.cos(math.radians(vinkel)), math.sin(math.radians(vinkel)))
start = S.HUD + S.STOPP_TJOCK + 2.0 - S.HUD + .3
mitt_m = (mx + ut[0] * (start + 15), mz + ut[1] * (start + 15))
vag = Pos(mitt_m[0], sum(S.BULA_Y) / 2, mitt_m[1]) * Rot(0, 90 - vinkel, 0) * Cylinder(S.MAGNET[0] / 2, 30)
steg.append(("10 magneten in bakifrån (väg Ø6,2 × 30 mm)", vag, {"torn": torn, "servo": servo}))

fel = []
for namn, verktyg, delar in steg:
    k = krock(verktyg, delar)
    print(("BLOCKERAT  " if k else "fritt      ") + namn + (f": {k} mm3" if k else ""))
    if k:
        fel.append(namn)
# Negativtest: utan kabelbandet (som tornet såg ut före 2026-11-12) ska tätningen blockera servon.
utan_band = krock(kropp + oron + tatning, {"torn utan kabelband": S.torn(med_kabelband=False)})
if not utan_band:
    raise SystemExit("UNDERKÄND: negativtestet fångar inte en torn utan kabelband")
print(f"negativtest ok: torn utan kabelband blockerar servon {utan_band} mm3")
if fel:
    raise SystemExit(f"UNDERKÄND: {len(fel)} steg blockerade")
print("GODKÄND: alla monteringssteg nåbara")
