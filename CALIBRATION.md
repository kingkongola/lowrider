# Kalibrering — protokoll och mätlogg

Maskinkalibreringen gäller LR-30 / manualens "Initial Calibration" ([docs.v1e.com/lowrider](https://docs.v1e.com/lowrider/)). Detta är enda kanoniska loggen för kalibreringsmätningar och fysiska sensorprov; `BUILD_LOG.md` får bara hänvisa hit. Ordning: **1 steps/mm → 2 squaring → 3 Z-nivå**. Gör inte om ett tidigare steg utan att alla senare steg mäts om.

Ändra aldrig annat i config än det steget kräver. Spara config-backup (`machine/`) före och efter varje ändring.

## Aktuell maskinkalibrering 2026-11-10 – källfil kontra fysisk mätning

- **Konfiguration i Git** enligt `machine/AKTIV` → `config-2026-11-05-z800.yaml`: **X max_travel 637 mm**, Y 1240 mm, Z **max_travel 98 mm**; Z **max_rate 800 mm/min**. Den äldre tabellen nedan är uttryckligen **baslinjen från 2026-10-04** (X 642 och Z max_rate 900), inte gällande värden. Z 800 avser matningshastighet, **inte** axelns rörelseområde eller Z-nivå.
- **Fysisk squaring:** kontrollmätt **efter struts 2026-10-13**, diagonalskillnad **0,5 mm** och då godkänd; se loggraden nedan. `BUILD_LOG.md` 2026-10-22 begär senare ny kontroll efter ytterligare arbete med offerskivan; någon sådan **ytterligare kontrollmätning är inte loggad**.
- **Z-nivå (steg 3):** fortfarande **inte loggad som uppmätt/godkänd**. Planfräsning `plan07` klar 2026-10-22 enligt `BUILD_LOG.md`; detta bevisar inte att balken nivellerats.
- **Maskinens faktiskt laddade config just nu:** inte liveavläst i denna granskning. `machine/AKTIV` är repots avsedda version, inte verifierad mätning från kortet.

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
| 2026-10-13 | 2 (om, efter struts) | Efter strutplattorna: diagonaler (måttband) **1↔3 = 1346,0**, **2↔4 = 1343,25**, skillnad **2,75 mm** (1↔3 längst). Y motor0 `pulloff_mm` 6,2 → **7,7** (+1,5 mm, skalat från 4/10: +2,2 mm gav −2,4 mm skillnad). Efter `$HY` och nya tejpmärken: **1↔3 = 1344,5**, **2↔4 = 1344,0** | Skillnad **0,5 mm** → **godkänd** (<1 mm). Y-bältet flyttades under sessionen (hårdvarustopp Y fungerade inte pga rem). Pulloff gick förlorad vid omstart när den bara var live; sparad som config | `config-2026-10-13-step2b.yaml` (motor0 7,7), uppladdad som `config.yaml` och verifierad identisk |

## Historisk status 2026-10-04

- Steg 1 steps/mm: **klart** (X 50,0835, Y 50,2054).
- Steg 2 squaring: **klart för tillfället** (diagonalskillnad 1,6 mm); görs om efter permanenta struts.
- Steg 3 Z-nivå: **uppskjutet** (se ovan).
- Aktuell config på maskinen: `machine/config-2026-10-04-step2a.yaml` (Y motor0 pulloff 6,2; X homing mpos_mm 2,99).

## 2026-10-22 — X-rörelsen kortare än config

- `max_travel_mm: 642` i X (soft limit MPos 645) är **för långt**: körning mot MPos 644,8 fick remmen att hoppa över kuggar (två gånger, först tolkat som ett kärvande buntband). Larmet Hard Limit uppstod sedan på vägen tillbaka, eftersom X-positionen tappats.
- Efter homing joggade användaren till **MPos X 613,0** , **MPos X 640,0** och **MPos X 642,0**, alla fria. **Vid MPos X 643,0 tar något i** (okänt vad). **Infört:** soft limit MPos 640 (`max_travel_mm: 637`), 3 mm marginal; `config-2026-10-22-x637.yaml` uppladdad, verifierad med `$I` efter omstart. Backup: `config-2026-10-22-fore.yaml`. `cnc` (MASKIN_GRANS) följer samma gräns.
- Åtgärd (poka-yoke): sätt `max_travel_mm` i X så att soft limit ligger några mm före det verkliga ändläget; då vägrar FluidNC alla program som går längre. `cnc`:s `MASKIN_X`/`MASKIN_GRANS` följer samma värde.

## 2026-11-10 — Fällservots rörelseomfång verifierat på bänk

**Resultat: osäkerheten om servot klarar CAD-armens 150° rörelse är stängd.** Sidotornets arm går mellan utfällt 0° och parkerat −150° enligt D020 och `machine/delar/sensorer/sidotorn.py`. Användaren såg minst 180° rörelse i det lösa servot och godkände omfånget för konstruktionen. Vinkeln är visuellt bedömd, inte uppmätt med vinkelverktyg.

- **Utrustning:** Spektrum S664 / SPMS664, fristående ESP32-S3 som servotestare, USB `/dev/cu.usbmodem3101`. Ingen arm eller annan mekanisk last ansluten.
- **Inkoppling:** GPIO 18 till vit signal, separat 6 V till röd, svart till matningsminus och ESP:ns GND. Användaren mätte 6 V mellan röd och svart samt 6,06 V mellan röd och ESP:ns GND.
- **Prov:** 50 Hz; först 1500 → 1800 → 1200 → 1500 µs, därefter 1600 → 2500 → 500 µs. Användaren såg rörelse efter programrättningen och bekräftade bra gång/ljud vid de två yttersta provlägena. 500 och 2500 µs är provade kommandovärden; de är inte uppmätta mekaniska stopp.
- **Programfel rättat:** ursprungsprogrammet begärde 16 bitars pulsupplösning, men ESP32-S3 stöder högst 14 för denna pulsgenerator. Ändrat till 14 bitar med motsvarande pulsskalning och kontroll av att `ledcAttach` lyckas. USB-seriekommunikation vid start aktiverad med `CDCOnBoot=cdc`. Den provade källkoden är sparad i [servoprov.ino](machine/servoprov/servoprov.ino), kompilerad med Arduino-ESP32 3.3.12 för `esp32:esp32:esp32s3:CDCOnBoot=cdc`.
- **Avgränsning:** detta verifierar det lösa servots rörelseomfång. Monterade armens pulsvärden, passning och rörelse mot stoppen provas efter montage. Jackpot3/FluidNC och `machine/AKTIV` har inte ändrats.

## 2026-11-10 — Erfarenhetsvärde för printade hål

- **Användarens erfarenhet:** hål blir lite mindre vid utskrift. För ett önskat färdigt hål på Ø20,00 mm behövs ungefär Ø20,10–20,15 mm i modellen. Tillägget avser **hela diametern**, motsvarande 0,05–0,075 mm per sida.
- Detta är användarens ungefärliga erfarenhetsvärde, inte ett nytt uppmätt prov. Material, hålriktning och utskriftsinställningar för exemplet är inte specificerade. Värdet används som start vid passningsberedning, inte som en generell procentuell skalning av hela delen.
- Kontrollera befintlig spelmån före ändring, så att tillägget inte läggs på två gånger. Ett frigångshål (där skruven ska löpa fritt), ett gänghål och en ficka behöver bedömas efter sin funktion. Små hål och yttre styrtappar ska inte automatiskt få samma korrigering som exemplet med Ø20 mm.
- Behåll funktionsmåttet och redovisa passningstillägget i CAD-underlaget. Bekräfta resultatet med provprint i avsett material och utskriftsläge innan större delar låses.

## 2026-11-10 — Servohornets nav, första måtten

Användaren rapporterar följande enligt det annoterade fotot av det tillgängliga hornet:

| Mått | Definition | Rapporterat värde |
| --- | --- | --- |
| A | Navets ytterdiameter, ytterkant till ytterkant över den runda kragen | Ø9 mm |
| B | Total höjd vid navet, lägsta till högsta plastytan, utan centrumskruv | 6 mm |
| C | Hela armens bredd tvärs längdriktningen vid mittenhålets centrum | 7,3 mm |
| D | Hela armens bredd tvärs längdriktningen vid yttersta hålets centrum | 6,8 mm |

Användaren rättade C från 7,5 till **7,3 mm i samma svar**; det senare värdet gäller. Båda breddmåtten avser plastens ytterkanter, inte håldiametrarna. Den rapporterade breddskillnaden är 0,5 mm mellan mätpunkterna; avståndet mellan dem är ännu inte angivet, så avsmalningsvinkeln kan inte bestämmas.

Instrument och mätosäkerhet är inte angivna. Värdena är komponentmått, inte färdiga CAD-fickmått eller tillägg för printspel. Den flata armens tjocklek och hålens lägen återstår. Navets sittläge på servoaxeln och det färdiga montaget är inte verifierade genom dessa mått. Konstruktionens infästning ägs av [CAD-underlaget](machine/delar/sensorer/README.md).
