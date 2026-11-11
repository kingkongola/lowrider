"""Beräkningar för sidotornet med kriterier. Avbryter med UNDERKÄND om ett kriterium inte håller.

Grov fysik enligt verkstad KONTROLLER.md princip 10: enkla räkningar där konsekvensen kräver det.
Varje antagande står i ANTAG med källa och osäkerhet; byt mot mätvärde när det finns (CALIBRATION.md).
Geometri läses från sidotorn.py, så räkningen följer CAD:en.

Kör: python berakning_sidotorn.py
"""
import math

import sidotorn as S

ANTAG = {
    "petg_tryckgrans_mpa": (50, "PETG tryckhållfasthet, typiskt databladsvärde; print lägre"),
    "petg_krypgrans_mpa": (18, "ca en tredjedel av tryckgränsen som långtidsgräns; antagande"),
    "petg_skikt_skjuv_mpa": (15, "vidhäftning mellan lager i skjuvning; försiktigt antagande"),
    "servo_moment_nm": (1.6, "SPMS664 226 oz-in vid 6 V, Horizon Hobby"),
    "servo_stromtopp_a": (3.0, "typisk standardservo med metalldrev vid 6 V; ej uppmätt"),
    "m5_moment_nm": (0.7, "vald åtdragning 0,6-0,8 Nm (MONTAGE.md)"),
    "mutter_faktor_k": (0.2, "friktionsfaktor torr gänga"),
    "magnet_dragkraft_n": (12.0, "Ø6 x 3 N42 mot tjockt stål, typiskt säljarvärde"),
    "magnet_glapp_faktor": (0.45, "0,6 mm plast mellan magnet och stål; grov tumregel"),
    "magnet_mal_faktor": (0.6, "litet stålmål (M3-skalle Ø5,5) mättas"),
    "armpaket_g": (26, "arm 5,6 + hylsa 5,6 + CR Touch ca 12 + bygel och skruvar ca 3 g"),
    "armpaket_tp_mm": (30, "tyngdpunktens avstånd från axeln, ur CAD ungefärligt"),
    "vibration_g": (3.0, "antagen topp vid verktygsfästet under fräsning; mäts i fas 8"),
    "pi_effekt_w": (1.5, "medel; 3 W vid bildtagning"),
    "pi_topp_w": (3.0, ""),
    "lm2596_verkningsgrad": (0.78, "24 V till 5 V vid 0,4 A, typiskt datablad"),
    "konvektion_w_m2k": (9.0, "naturlig konvektion och strålning, liten låda"),
    "torn_yta_m2": (0.035, "effektiv yttre yta, ur tornets mått"),
    "omgivning_max_c": (35.0, "garage sommar"),
    "ledare_ohm_per_m": (0.07, "0,25 mm² koppar"),
    "kabel_m": (3.0, "tornkabeln"),
}
V = {k: v[0] for k, v in ANTAG.items()}
rader, fel = [], []


def krav(namn, varde, enhet, villkor, text):
    rader.append(f"{'OK ' if villkor else 'FEL'} {namn}: {varde:.3g} {enhet} ({text})")
    if not villkor:
        fel.append(namn)


# 1. M5 mot PETG: distansens ring mot örats försänkning och skallen med bricka mot plattan.
F_m5 = V["m5_moment_nm"] / (V["mutter_faktor_k"] * 0.005)
ring = math.pi / 4 * (9.6 ** 2 - 5.4 ** 2)
bricka = math.pi / 4 * (9.0 ** 2 - 5.4 ** 2)
krav("M5 tryck på distansen", F_m5 / ring, "MPa", F_m5 / ring <= V["petg_krypgrans_mpa"], f"förspänning {F_m5:.0f} N på {ring:.0f} mm²")
krav("M5 tryck under brickan", F_m5 / bricka, "MPa", F_m5 / bricka <= V["petg_krypgrans_mpa"], f"DIN 433 Ø9 på {bricka:.0f} mm²")
krav("M5-kanalen rymmer brickan", S.M5_KANAL_D - 9.0, "mm spel", S.M5_KANAL_D - 9.0 >= 0.3, f"kanal Ø{S.M5_KANAL_D}")

# 2. Hårda stopp: servots moment på stoppets inre ände (värsta fall).
r_min = S.STOPP_T[0] / 1000
F_stopp = V["servo_moment_nm"] / r_min
kontakt = (S.STOPP_T[1] - S.STOPP_T[0]) * (S.ARM_Y[1] - S.ARM_Y[0])
krav("Stopp, yttryck", F_stopp / kontakt, "MPa", F_stopp / kontakt <= V["petg_krypgrans_mpa"], f"{F_stopp:.0f} N på {kontakt:.0f} mm²")
fot = (S.STOPP_T[1] - S.STOPP_T[0]) * 5.2
sf = V["petg_skikt_skjuv_mpa"] / (F_stopp / fot)
krav("Stopp, säkerhet mot skjuvning i lagren", sf, "", sf >= 2.0, f"fot {fot:.0f} mm²")

# 2b. Stoppdelarna bärs av två M3 x 20 var; stoppkraften delas på två skruvar (skjuvning/urdragning).
F_per = F_stopp / 2
ur_stopp = math.pi * 3.0 * S.STOPP_PILOT_DJUP * 0.5 * V["petg_skikt_skjuv_mpa"]
krav("Stoppdel, säkerhet per skruv", ur_stopp / F_per, "", ur_stopp / F_per >= 3, f"{F_per:.0f} N mot {ur_stopp:.0f} N")

# 3. Magneten håller den parkerade armen, utan servo.
F_mag = V["magnet_dragkraft_n"] * V["magnet_glapp_faktor"] * V["magnet_mal_faktor"]
M_arm = V["armpaket_g"] / 1000 * 9.81 * V["armpaket_tp_mm"] / 1000
F_behov = M_arm / (S.BULA_T / 1000)
krav("Magnet, säkerhet vid 1 g", F_mag / F_behov, "", F_mag / F_behov >= 3, f"{F_mag:.1f} N mot {F_behov:.2f} N")
a_max = F_mag / F_behov - 1
krav("Magnet, tål vibration upp till", a_max, "g", a_max >= V["vibration_g"], f"antagen topp {V['vibration_g']} g; mäts med ADXL i fas 8")

# 4. Självgängande M3 i PETG: urdragning mot största last (servons reaktionsmoment).
L_ingrepp = S.FRAM_Y[1] - S.FRAM_Y[0]
F_ur = math.pi * 3.0 * L_ingrepp * 0.5 * V["petg_skikt_skjuv_mpa"]
avst = ((S.PX + 14) - (S.PX - 33.3)) / 1000
F_skruv = V["servo_moment_nm"] / avst / 2
krav("Servoskruv, säkerhet mot urdragning", F_ur / F_skruv, "", F_ur / F_skruv >= 5, f"{F_ur:.0f} N mot {F_skruv:.0f} N per skruv")

# 5. Värme i tornet.
forlust_A = V["pi_topp_w"] * (1 / V["lm2596_verkningsgrad"] - 1)
P_medel = V["pi_effekt_w"] + V["pi_effekt_w"] * (1 / V["lm2596_verkningsgrad"] - 1) + 0.12
P_topp = V["pi_topp_w"] + forlust_A + 0.12
dT = P_topp / (V["konvektion_w_m2k"] * V["torn_yta_m2"])
krav("Värme, luft i tornet vid topp", V["omgivning_max_c"] + dT, "°C", V["omgivning_max_c"] + dT <= 50, f"{P_topp:.1f} W, ΔT {dT:.0f} K; medel {P_medel:.1f} W")
krav("Värme, marginal till PETG mjukning", 80 - (V["omgivning_max_c"] + dT), "K", 80 - (V["omgivning_max_c"] + dT) >= 20, "PETG Tg ca 80 °C")

# 6. Spänningsfall och jordförskjutning i tornkabeln.
R = V["ledare_ohm_per_m"] * V["kabel_m"]
I_servo = 6.0 * V["servo_stromtopp_a"] / 0.85 / 24
krav("Servo, ström i 24 V-ledaren vid topp", I_servo, "A", I_servo <= 1.5, "LM2596 B 6 V, 85 %")
jord = R * (I_servo + 0.3)
krav("Jordförskjutning torn mot Jackpot", jord, "V", jord <= 0.5, "signaler 3,3/5 V tål detta; proben har egen jordledare")
krav("Servo, toppström mot LM2596 B", V["servo_stromtopp_a"], "A", V["servo_stromtopp_a"] <= 3.0, "modulen klarar 3 A kort tid; pulserna stängs av vid stoppet")

# 7. CR Touch-kabeln vid navet.
r_kabel = S.HUB_D / 2
langd = r_kabel * math.radians(-S.PARK)
krav("CR Touch-kabel, längdändring vid navet", langd, "mm", True, "kräver en fri ögla på minst 40 mm, böjradie minst 15 mm; F cykelprov")

# Negativtest (KONTROLLER.md princip 7): full åtdragning 2,5 Nm måste underkännas.
assert 2.5 / (V["mutter_faktor_k"] * 0.005) / ring > V["petg_krypgrans_mpa"], "M5-kriteriet kan inte fela"

print("\n".join(rader))
print("\nAntaganden (byt mot mätvärden när de finns):")
for k, (v, kalla) in ANTAG.items():
    print(f"  {k} = {v}  {kalla}")
if fel:
    raise SystemExit("UNDERKÄND: " + ", ".join(fel))
print("GODKÄND: alla beräkningar inom kriterierna")
