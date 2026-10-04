# Kalibrering — protokoll och mätlogg

Gäller LR-30 / manualens "Initial Calibration" ([docs.v1e.com/lowrider](https://docs.v1e.com/lowrider/)). Detta är enda kanoniska loggen för kalibreringsmätningar; `BUILD_LOG.md` får bara hänvisa hit. Ordning: **1 steps/mm → 2 squaring → 3 Z-nivå**. Gör inte om ett tidigare steg utan att alla senare steg mäts om.

Ändra aldrig annat i config än det steget kräver. Spara config-backup (`machine/`) före och efter varje ändring.

## Baslinje 2026-10-04 (`machine/config-2026-10-04.yaml`, hämtad från 192.168.50.184)

FluidNC 3.9.9, Jackpot3 TMC2226. Homing negativ för X/Y (mpos 3), positiv för Z (mpos 3, toppen). Hard limits på för alla fem brytare, soft limits på X/Y/Z.

| Axel | steps/mm | max_travel | max_rate | acc | pulloff | brytare |
|---|---|---|---|---|---|---|
| X | 50 | 642 | 9000 | 200 | 4 | gpio.25 (neg) |
| Y | 50 | 1240 | 9000 | 200 | 4 (båda) | motor0 gpio.33, motor1 gpio.35 (neg, auto-square) |
| Z | 200 | 98 | 900 | 80 | 4 (båda) | motor0 gpio.32, motor1 gpio.34 (pos) |

Maskinkoordinater efter `$H`: X 3…645, Y 3…1243, Z −95…3. Efter varje strömstart: `$H`.

## Steg 1 — Remkalibrering (steps/mm)

Formel: `ny steps/mm = (begärd / uppmätt) × nuvarande steps/mm`. Gäller X och Y; Z (T8-skruv) ingår inte. GT2 kan avvika upp till ±6 mm över 2400 mm. Mät med samma verktyg/pennspets vid båda märkena; räkna medelvärde av minst 2 mätningar. Godkänt: kontrollmätning inom ±0,5 mm på hela sträckan.

## Steg 2 — Squaring (Y)

Homa X/Y, markera fyra hörn, mät båda diagonalerna. Under 1 mm skillnad är utmärkt; korrigera över 2 mm. Korrigering: Y-brytarnas `pulloff_mm` (motor0/motor1) — flytta hörnet närmast den längre diagonalen bort från sitt stopp. Pulloff får aldrig understiga 4 mm. Mät om efter varje ändring.

## Steg 3 — Z-nivå (balk)

Homa Z, nollställ, probea/nudda touch plate/pappersmätning vid minst vänster, höger och mitt; 3 mätningar per sida, medelvärde. Justera `pulloff_mm` för Z-sidan som triggar mer negativt (aldrig under 4 mm). Godkänt: under 0,5 mm skillnad. Upprepa efter permanenta struts.

## Logg

**Mätverktyg:** alla längdmått nedan är tagna med **tumstock** (och borr Ø3 som pekare), inte stålmåttband. Realistisk mätosäkerhet ca ±0,5–1 mm per mått; avläsningar i cm. Diagonalskillnaden 1,6 mm (steg 2) ligger därför nära mätbruset.

| Tid | Steg | Åtgärd / mått | Resultat | Config |
|---|---|---|---|---|
| 2026-10-04 | – | Baslinje hämtad, maskin Idle, MPos 3/3/3 | – | `config-2026-10-04.yaml` |
| 2026-10-04 | 1 X | Märke A vid X=3 (hem), `G91 G1 X600 F3000` → MPos X 603,000. Uppmätt A–B (borr Ø3 i KATSU-fäste, tejp): **599 mm** (en mätning) | Fel −1 mm (0,17 %). Nytt X steps/mm = 600/599 × 50 = **50,0835** | `$/axes/x/steps_per_mm=50.0835`; sparad som fil via `/files`-upload: `config-2026-10-04-step1.yaml` |
| 2026-10-04 | 1 X | Efter nytt steps/mm homade X till 2,995 (3 mm = 150,25 steg → 150 steg) och gav Alarm 2 mot mjukgräns 3,0. Controllern föll dessutom tillbaka på Default-profil en gång under sessionen (orsak ej fastställd; filen intakt; åtgärd: omstart). | `x.homing.mpos_mm` 3,0 → **2,99** (X-yta 2,99…644,99) | `config-2026-10-04-step1b.yaml`, uppladdad och verifierad |
| 2026-10-04 | 1 X (kontroll) | Efter `$H` märke A2, `G91 G1 X600 F3000` → MPos X 2,995 → 602,993. Användarens bedömning A2–B2: **600 mm ±0,5 eller bättre** (stump borr, ingen siffra) | **X godkänd** (steps/mm 50,0835) | `config-2026-10-04-step1b.yaml` |
| 2026-10-04 | 1 Y | Märke A_Y vid Y=103, `G91 G1 Y1100 F3000` → MPos Y 1203,000. Uppmätt A_Y–B_Y: **1095,5 mm** (måttband, osäkerhet ca ±0,4 mm; en mätning) | Fel −4,5 mm (0,41 %). Nytt Y steps/mm = 1100/1095,5 × 50 = **50,2054**. Position osynkad efter ändring → `$H` krävs | `config-2026-10-04-step1c.yaml`, uppladdad och verifierad |
| 2026-10-04 | 1 Y (kontroll) | Efter `$H`: märke A_Y2 vid Y=103, `G91 G1 Y1100 F3000` → MPos Y 102,997 → 1202,998. Uppmätt A_Y2–B_Y2: **1100,3 mm** (måttband) | Fel +0,3 mm (0,03 %) → **Y godkänd** (steps/mm 50,2054). **Steg 1 klart** (X 50,0835, Y 50,2054) | `config-2026-10-04-step1c.yaml` |
| 2026-10-04 | 2 | Hörn (X,Y) 1 (4,4) · 2 (604,4) · 3 (604,1204) · 4 (4,1204), tejp + borr. Diagonaler (måttband, cm-avläsning): **1↔3 = 1343,5 mm**, **2↔4 = 1339,5 mm**. Skillnad **4,0 mm** (>2 mm) | Modell: höger sida (X-hög) står δ ≈ 2,24 mm längre i +Y än vänster → öka pulloff på vänster Y-motor med ≈2,2 mm. Vilken motor som är vänster är **okänt**; gissning: motor0 (gpio.33) → `y.motor0.pulloff_mm` 4,0 → **6,2** (motor1 oförändrad 4,0). Förväntat efter homing: diagonaldiff ≈0; blir den ≈8 mm är fel motor → flytta till motor1 | `config-2026-10-04-step2a.yaml`, uppladdad och verifierad |
| 2026-10-04 | 2 (X-kontroll) | Märke 1↔2 (X 4→604, Y 4) uppmätt **600,0 mm** | X-kalibrering bekräftad | – |
| 2026-10-04 | 2 (identifiera Y-motor) | Test: `y.motor0.pulloff_mm` sätts tillfälligt till **10** (endast live, ej i fil); efter `$HY` ser användaren vilken balkände som står längre från sitt Y-stopp → den sidan = motor0 | Resultat noteras här | live; fil har 6,2 |
| 2026-10-04 | 2 (kontroll) | Märke 3↔4 (X 604→4 vid Y=1204) uppmätt **598,9 mm** (först felläst som 588,9; rättad av användaren), förväntat 600,0 | −1,1 mm (0,18 %), nära mätnoggrannhet; ingen tecken på förlorade steg. Diagonalmåtten (4,0 mm skillnad) gäller fortfarande | – |
| 2026-10-04 | 2 (identifiera Y-motor) | Med motor0 pulloff 10: Y-stopp ca **6 mm** från släden på **X0-sidan** (brytarsidan för X, låg X, märke 1/4), ca 2 mm på andra sidan | **motor0 = X0-sidan (vänster)** → gissningen stämde. Live-pulloff återställd 10 → **6,2** (motor1 4,0) | fil `config-2026-10-04-step2a.yaml` (oförändrad) |
| 2026-10-04 | 2 (efter justering) | Efter `$H` och `y.motor0.pulloff_mm` 6,2 / motor1 4,0: samma hörn (4,4)(604,4)(604,1204)(4,1204). Diagonaler: **2↔4 = 1341,0 mm**, **1↔3 = 1342,6 mm** | Skillnad **1,6 mm** (förut 4,0). Under manualens korrigeringsgräns 2 mm → **godkänd**; kvarvarande δ ≈ 0,9 mm (skulle kräva motor0 ≈ 7,1). Ingen ytterligare ändring; **görs om efter permanenta struts** | `config-2026-10-04-step2a.yaml` |
| 2026-10-04 | 3 | Z-nivå **uppskjuten**: bordet är inte plant och ingen offerskiva är planfräst, så mätning mot bordet ger fel större än målet (0,5 mm) | Görs efter permanenta struts + planfräst MDF-offerskiva, med bladmått (samma blad vid vänster/mitten/höger, 3 mätningar per punkt, medelvärde). Justera `pulloff_mm` på Z-sidan som triggar mer negativt, aldrig under 4 mm | – |

## Status 2026-10-04

- Steg 1 steps/mm: **klart** (X 50,0835, Y 50,2054).
- Steg 2 squaring: **klart för tillfället** (diagonalskillnad 1,6 mm); görs om efter permanenta struts.
- Steg 3 Z-nivå: **uppskjutet** (se ovan).
- Aktuell config på maskinen: `machine/config-2026-10-04-step2a.yaml` (Y motor0 pulloff 6,2; X homing mpos_mm 2,99).
