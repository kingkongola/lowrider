# Offerskivan: hål och skruvar (SSOT)

Allt som sitter i eller under offerskivan och som fräsen, pinnarna eller maskinhuvudet kan
träffa. Koordinater i **maskinkoordinater (MPos)**, alltså oberoende av jobbets nolla.
Uppdatera här när något borras, skruvas eller mäts.

## Styrhål (indexering/vändning)

Borrade 2026-10-23 av `provbit_rundning/provbit_1_SKARP.nc` (upcut 3,175) med G54
X 2,995 Y 43,008 Z −66,2 (ytan på provbitens MDF 9 mm). Räknat ur körloggen och jobbets
indata: MPos = G54 + bitens koordinater. Hålen går 7 mm ner i offerskivan (Z −16 från
provbitens yta). Diametern är pinnens; hålet i offerskivan är fräst med presspassning.

| Pinne | MPos X | MPos Y | Bitens X, Y |
|---|---|---|---|
| Ø6 | 22,0 | 52,0 | 19, 9 |
| Ø6 | 22,0 | 334,0 | 19, 291 |
| Ø8 | 74,0 | 52,0 | 71, 9 |
| Ø8 | 74,0 | 334,0 | 71, 291 |

Vändlinje för provbiten: X 40 i bitens koordinater (MPos X 43,0).

Inte inmätt fysiskt; mät gärna ett hål mot hörnet med fräsen när tillfälle ges.
Den fasta hålraden (cnc beslut 0024) är inte borrad än.

## Skruvar i offerskivan

**Ej kartlagt.** Användaren 2026-10-23: tre skruvar sitter ungefär mitt på offerskivan.

Att göra:
1. Kartlägg alla skruvar (MPos X, Y, skallens diameter och höjd), till exempel genom att
   jogga fräsen över varje skruv och läsa positionen.
2. Lägg in dem här och gör dem till fasta hinder i cnc, så att varje jobb kontrolleras mot
   dem utan att någon behöver komma ihåg det (FMEA C5).
3. Markera dem på offerskivan (färg runt skallen), så att de syns när ett ämne läggs ut.
