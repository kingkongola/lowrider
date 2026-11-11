"""Exakt CAD-kontroll av Pi:ns stiftlist: får lödda ledningar plats under sidopanelen?

Beslut 2026-11-11: ledningarna löds direkt på stiften, inga instickskontakter (DuPont).
Skäl: instickskontakter behöver ca 16,5 mm plus kabelböj över kortet men panelen ger 14,1 mm,
och de kan vibrera loss på en fräs. Lödda ledningar kan inte glappa.

För varje använt stift kontrolleras ett lödkuvert: 2,6 x 2,6 mm runt stiftet från listens
plastkropp till 2,6 mm över stifttoppen (lödtenn och ledning som böjs av sidledes).
Därtill en ledningsgata från listen ned mot mikrofon, ADXL och regulatorer.
Instickskontakternas höjd redovisas för jämförelse men är inte ett krav.

Kör: python kontroll_stiftlist.py
"""
import sidotorn as S
from kontrollhjalp import krock as _krock

# Planerade stift, ägs av KOPPLING_CORE_V0.md. Ändra där först.
STIFT = {
    2: "5 V in från LM2596 A", 4: "5 V till CR Touch", 6: "GND", 9: "GND (ADXL)",
    1: "3,3 V ADXL", 17: "3,3 V INMP441",
    19: "ADXL MOSI GPIO10", 21: "ADXL MISO GPIO9", 23: "ADXL SCLK GPIO11", 24: "ADXL CS GPIO8",
    12: "INMP441 SCK GPIO18", 35: "INMP441 WS GPIO19", 38: "INMP441 SD GPIO20", 34: "GND (INMP441)",
    16: "Stopp: OK-puls GPIO23 (laddningspump, D024)", 22: "Stopp: startknapp GPIO25", 20: "GND (stopplådan)",
}

t, p = S.torn(), S.sidopanel()


def krock(a, b):
    return _krock(a, b)


fel = []
for n, vad in sorted(STIFT.items()):
    x, z = S.stift_lage(n)
    kuvert = S.box((x - 1.3, S.LIST_TOPP_Y, z - 1.3), (x + 1.3, S.STIFT_TOPP_Y + 2.6, z + 1.3))
    v = krock(kuvert, t) + krock(kuvert, p)
    print(f"stift {n:2d} ({vad}): x {x:.1f} z {z:.1f}, gods i lödkuvertet {v:.3f} mm3")
    if v > 0.01:
        fel.append(f"stift {n}")
# Ledningsgata ned från listen mot mikrofon/ADXL/regulatorer, mellan kortet och panelen.
# Vänster gata: stift 1-24 ned mot ADXL, regulatorer och mikrofon. Höger gata: stift 34-38 genom
# ribbans kabelfönster bort till mikrofonen. Båda ligger mellan kortet och panelen, nära panelen.
zl = S.PI_CENTER[1] - 15
for namn, g in (("vänster, x 22-47", S.box((22, 62.5, S.MIK[1] + 7.5), (47, S.Y1 - 2.05, zl + 2))),
                ("höger genom ribban, x 40-68", S.box((40, 62.5, 129.5), (68, S.Y1 - 2.05, zl + 2)))):
    v = krock(g, t) + krock(g, p)
    print(f"ledningsgata {namn}: gods {v:.3f} mm3")
    if v > 0.01:
        fel.append(f"ledningsgata {namn}")
fritt = S.Y1 - 2 - (S.PI_Y + 1.4)
print(f"jämförelse: fri höjd över kortet {fritt:.1f} mm; raka instickskontakter behöver ca 16,5 mm plus böj")
if fel:
    raise SystemExit("UNDERKÄND: " + ", ".join(fel))
print("GODKÄND: lödda ledningar på alla planerade stift och ledningsgatan")
