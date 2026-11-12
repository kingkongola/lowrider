# Aktuellt arbete och verifieringsstatus

**Uppdaterad 2026-11-11.** Detta är den aktuella arbetslistan. Äldre byggchecklista är [arkiverad](docs/arkiv/2026-11-09-status-och-sensorunderlag.md). Orapporterade kontroller nedan är inte godkända; genomförda byggmoment ska inte beställas eller göras om bara för att ett gammalt arbetskort är obockat.

## LED-belysning – aktuellt beslut 2026-11-10 (D022)

- [x] **Valt komponent-/funktionsval:** BRIMETI COB 24 V / 4000 K / 8 mm / 320 LED/m; **G4-lampor utgår**. Rulle 5 m, uppgivet 10 W/m; 145 kr med Prime enligt användaren. Faktisk betalning/mottagning ej bekräftad.
- [x] Parametrisk **build123d-lågprofil** i [`machine/delar/led/tre_vinklar.py`](machine/delar/led/tre_vinklar.py): horisontell understrut, 3 × LED-riktningar med **provvinklar 0°/15°/35° och 9 mm hyllbredd för 8 mm LED**, och **hård Z-budget 6,65 mm för enbart fästet** under plattan. **Både felvända 90°-CAD:n och tidigare ~21 mm nedsänkta pelarversionen är ogiltiga.**
- [ ] Verifiera build123d-export i CI och att rätt STEP/STL ligger i aktuell artefakt; inga gamla STL/STEP.
- [ ] Kontrollera att aktuell CAD-export från build123d innehåller **rundade hörn och 0,2 mm hyllkantfas i **den nya 1,6 mm tunna hyllan****, inte bara den äldre kantiga modellen. Provprinta en ny export, inte tidigare uppladdad STL/STEP.
- [ ] Kontrollera **längsgående kantstag från lägre sidan av 15°-/35°-hyllorna upp mot 0,9 mm överdel**, anslutning mot central skruvad bas och böjstyvhet vid fria ändar; kontrollera att stagen är bakom ljusytorna. Kontrollera verkligt CAD-intrång **≤6,65 mm för själva fästet relativt understrutten** och mät separat LED-listens/tejpens tillkommande Z och verklig maskinfrigång med fräs/dammsko/arbetsstycke. Provprinta **ett** PETG-fäste; kontrollera två M5/Brace-låspunkter (56 mm c/c), skruvgrepp och hel XYZ-frigång innan full montering.
- [ ] Prova kort LED-sektion på PETG, 24 V och fullt ljus: yttemperatur, tejpens vidhäftning och kamerans skuggor/reflexer. **Aluminiumprofil är inte ett beslutat inköp.**
- [ ] Planera **3 × parallella lödda LED-grenar**, isolerade lödpunkter och dragavlastning, och en gemensam tvåledarmatning på balken. Prova först befintlig passage/kant; **om borrning krävs**, märk en enda genomföring efter kontroll av platta, M5/Brace, båda sidor och full XYZ, avgrada och skydda kabeln. Ingen hålposition eller diameter beslutad.
- [ ] Verifiera befintliga aggregat och dimensionera separat matning för installerad LED-längd; Pi/övervakningen ska fortsatt fungera efter maskinstopp. El-/stoppkrav: [`machine/EL_BELYSNING_OCH_STOPP.md`](machine/EL_BELYSNING_OCH_STOPP.md).

## Sensorenheten — hela vägen i ordning (genomgång 2026-11-11)

Genomgången är gjord som en torrkörning från användarens plats: vad som görs, med vad, vad som ska stämma innan nästa steg och vad steget låser upp. **Inget steg är godkänt förrän användaren rapporterat resultatet**; resultat förs i [CALIBRATION.md](CALIBRATION.md), måttändringar i CAD-källan. Varje grind (G) måste vara godkänd innan nästa fas börjar, om inget annat sägs.

### Luckor som genomgången hittade (ingen plan täcker dem än)

| # | Lucka | Blockerar | Förslag |
| --- | --- | --- | --- |
| L1 | **Övervakningens nätdel (D023) är inte vald.** Tornet behöver två matningar: maskinens 24 V till servot (LM2596 B) och övervakningens egen till Pi och CR Touch (LM2596 A) | Fas 5 | **Vald 2026-11-11:** en andra Mean Well HDR-60-24 eller likvärdig, ca 30 W last av 60 W ([underlag](machine/EL_BELYSNING_OCH_STOPP.md)). Ej beställd. Bänkproven i fas 1 kan köras på valfri 12–24 V-källa |
| L2 | **Kabeln från tornet till balken är inte projekterad:** övervakningsmatning, 24 V maskin, gemensam jord, servosignal, CR Touch styrning och kontakt, ca 7 ledare | Fas 5 | **Förslag:** skärmad LiYCY 8 × 0,25 mm², ledarlista i [kopplingsunderlaget](machine/delar/sensorer/KOPPLING_CORE_V0.md). Längd mäts med snöre vid full rörelse |
| L3 | **Pi-sidans program saknas:** ingen tjänst som skickar bild till datorn (armspärren förutsätter en adress), ingen läsning av ADXL eller mikrofon | Fas 1 steg 1.6–1.8, fas 6 | **Byggt 2026-11-11:** [`cnc/pi/sensorpi.py`](https://github.com/kingkongola/cnc/tree/main/pi) med installation och tester utan hårdvara. Ej provat på riktig Pi |
| L4 | **Slutdelarnas printjobb finns inte:** material, orientering och stöd för torn, panel, arm och brickor (hylsan och hornbygeln utgick 2026-11-11) är inte valda | Fas 3 | Görs efter fas 2, när måtten är rättade. Utkastet `print/sidotorn-smadelar` (PETG, ca 1,6 h, 25 g) har printa-varningar: sidopanelens 117 mm² plana yta svävar 1,0 mm över bädden, brickan och nedre stoppet har liten bäddkontakt (29/31 mm²) |
| L5 | **LED-fästet saknar printjobb** och LED-listens matning är inte vald (D022/D023) | Fas 6 steg 6.6 | **Printjobb klart 2026-11-11:** `print/led-fasten.printa/led-fasten.3mf`, PETG, ca 32 min, ett provsegment. Matning efter L1 |
| L6 | **Märket för armspärren och mönstret på armen är inte ritade** (beslut 0035/0036 i `cnc`) | Fas 6 steg 6.5 | Väljs från första riktiga kamerabild |
| L8 | **Pi:ns pinnar för stoppet (D024) saknades, och en fast GPIO-utgång släpper inte kontaktorn om Pi:n hänger sig** | Stopplådan | **Löst 2026-11-11:** laddningspump, OK-puls `GPIO23`, startknapp `GPIO25`; [schema och bänkprov](machine/EL_BELYSNING_OCH_STOPP.md#elschema-matning-och-stoppkedja-2026-11-11-förslag-ej-provat). Tornkabeln blir 12-ledare |
| L7 | **Avståndet mellan probstiftets spets och fräsens spets** har ingen mätmetod | Fas 7 | **Löst 2026-11-11:** proben mäter tjocklek som skillnad mot offerskivan, fräsen nollas som i dag; [metod](machine/probstyrning/README.md) |

### Fas 0 — Utskrift pågår

- [ ] **0.0 Skruvprovet i PETG** (på plattan `print/sensorprov-2`, se 0.1): skruva i och ur M3 och M2.5 fem gånger, dra M5-provet till 0,7 Nm. Godkänt: gängan håller och distansen spricker inte.
- [ ] **0.1 Armen på servot** (`print/sensorprov-2.printa/sensorprov-2.3mf`, ca 2 h PETG: arm, kameralock, två stopp, skruvprovet och LED-fästets provsegment). Hornprov 1 underkändes av felmontering; kilbygeln utgick 2026-11-11. Först: M3×10 för hand i servoaxeln (går den inte lätt: stopp, 4-40). Godkänt: hornet går rakt i fickan, sitter utan glapp när M3×10 är dragen, CR Touchen passar foten. [Provförfarande](print/README.md#armen-på-servot--sensorprov-2).

### Fas 1 — Elektronik på bänken, utan printade delar

Allt här görs med lösa delar och sladdar. Varför först: varje komponent provas för sig innan den byggs in, så att ett fel inte förväxlas med ett monteringsfel.

- [ ] **1.1 Regulatorerna.** Mata båda LM2596 från en 12–24 V-källa utan last. Ställ A på **5,1 V** och B på **6,0 V**, mät, säkra skruven med smältlim, mät igen. Godkänt: ±0,05 V efter limning.
- [ ] **1.2 Servot utan pulser** (ESP32-servoprovet, 2 min). `1500`, sedan `x`, vrid hornet för hand. Godkänt: hornet går lätt att vrida. **Om inte:** armsekvensen måste ändras före fas 4. [Probstyrning](machine/probstyrning/README.md).
- [ ] **1.3 CR Touch.** Matning från LM2596 A, styrning från ESP32:n. Stift ut (`650`), in (`1470`), självtest (`1780`), larm av (`2190`). Mät kontaktsignalen när stiftet trycks in. Godkänt: alla fyra kommandon fungerar; signalens nivå vid kontakt antecknad (avgör `gpio.36` eller `gpio.36:low`).
- [ ] **1.4 Mät komponenterna mot CAD:** INMP441-kortet (CAD antar 14 × 14 mm), Pi:ns stiftlist (ska sitta på motsatt långsida mot USB-uttagen, i hålens linje), ADXL-kortets hålbild (CAD antar 15 mm), LM2596 (CAD antar 43 × 21 mm), CR Touchens kropp och hålbild. Godkänt: alla mått inom 0,3 mm, annars rättas CAD i fas 2.
- [ ] **1.5 Pi startar.** Raspberry Pi OS på microSD, Wi-Fi, SSH. Matas från LM2596 A. Godkänt: `vcgencmd get_throttled` ger `0x0` under last (ingen undervolt).
- [ ] **1.6 Kameran.** CSI-kabeln i båda ändar, ta en stillbild. Godkänt: skarp bild, låst fokus på ca 130 mm. *Kräver L3 för att nå datorn.*
- [ ] **1.7 ADXL345 via SPI.** Godkänt: ca 1 g i vila, utslag när bänken knackas. *Kräver L3.*
- [ ] **1.8 INMP441 via I²S** (3,3 V, aldrig 5 V). Godkänt: inspelning där ett fingerknäpp syns tydligt. *Kräver L3.*

**G1:** alla komponenter fungerar lösa och alla mått är kända.

### Fas 2 — Passningsprov och rättad CAD

- [ ] **2.1** CR Touch-provet (`print/crtouch-passning`) och kamerafickeprovet (`print/sensor-passning`). Godkänt: kroppen sitter utan tvång, kamerakortet ligger an mot sina fyra distanser.
- [ ] **2.2** För in mått från 1.4 och provresultat i CAD. Kör kontrollerna (`kontroll_*.py`, CI och `kontroll_omgivning.py` lokalt). Godkänt: alla GODKÄND.
- [ ] **2.3** Om ett mått ändrades kraftigt: nytt litet provbit av just det stället, inte hela tornet.

**G2:** CAD stämmer med de verkliga delarna, alla kontroller gröna.

### Fas 3 — Slutdelarna

- [x] **3.1** (skivat 2026-11-12; armen, kameralocket och stoppdelarna är redan printade och godkända i sensorprov-2, så de ingår inte) Printjobb för torn (`print/sidotorn-torn`, 5,5 h, 121 g PETG) samt sidopanel och tre brickor (`print/sidotorn-smadelar`, 0,8 h, 16 g PETG) (L4): material, orientering så att lasten går längs lagren, stöd. Förhandsvisning granskas.
- [ ] **3.2** Printa. Godkänt: inga lagersläpp, hål och fickor rena från stöd.

### Fas 4 — Montera tornet på bänken

**Detaljerad ordning, skruvlista och ledningslista: [MONTAGE.md](machine/delar/sensorer/MONTAGE.md)** (simulerad 2026-11-11, varje skruv nåbar enligt `kontroll_montage.py`).

Ordningen spelar roll, eftersom panelen är enda åtkomsten och lödning inte går att göra inne i tornet.

- [ ] **4.1 Löd först, utanför tornet:** ledningar på Pi:ns stiftlist (stiften i [kontroll_stiftlist.py](machine/delar/sensorer/kontroll_stiftlist.py)), på mikrofonen och ADXL:en. Inga instickskontakter. Mät ledningslängderna i CAD innan du klipper.
- [ ] **4.2** Kameran underifrån: tappar i hålen, kameralocket rakt upp, två M3×10 genom locket klämmer kanten. CSI-kabeln in i rummet och viks två gånger 45°.
- [ ] **4.3** Magneten Ø6×3 i parkeringsstoppet. ADXL:en på sin platta med M3×10 och brickor.
- [ ] **4.4** Pi på tapparna, LM2596 A och B i fickorna, CSI-kabeln i Pi:n. Mikrofonen i panelens ram med en skumtejpsring runt ljudhålet, dammnät utvändigt.
- [ ] **4.5** Panelen på med sex skruvar; fingrarna ska hålla korten. Godkänt: inget skramlar när tornet skakas.
- [ ] **4.6** Servot in framifrån genom ramen. Hornet i armens formficka, paketet på axeln, M3×10 genom armen som mittskruv. **Sätt paketet på axeln så att armen står ungefär mitt i rörelsen vid 1500 µs**, annars räcker inte servots vinkel till båda stoppen.
- [ ] **4.7** CR Touch direkt i armfoten, kitets 2 × M3×6 underifrån genom öronen. Ingen hylsa (beslut 2026-11-11).
- [ ] **4.8 Ändlägena med ESP32:n.** Stega till respektive stopp, notera `utfalld_us` och `parkerad_us`, skriv in i `machine/probstyrning/installning.json`, kör `makron.py`. Godkänt: makrona skapas, armen ligger an mot båda stoppen, magneten tar.
- [ ] **4.9 Magneten under vibration:** parkerad arm, knacka och skaka tornet. Godkänt: armen faller inte ned.

**G4:** tornet är komplett och fungerar på bänken.

### Fas 5 — På maskinen (fräsen och Jackpot avstängda)

- [ ] **5.1** L1 och L2 lösta: nätdel vald, kabel byggd.
- [ ] **5.2** Tornet på verktygsfästet med två M5.
- [ ] **5.3b Frigång mot kjolen:** armen parkerad, mät att stoppdelarna och tornet ligger ovanför dammkjolens underkant. CAD ger 1,8 mm, vilket är mindre än skanningens noggrannhet, så det är inte bevisat. Godkänt: minst 1 mm uppmätt.
- [ ] **5.3 Hela rörelsen för hand eller med låg hastighet:** X, Y och Z ytterlägen. Godkänt: inget tar i, kabeln sträcks inte. Kabellängden förs in i [CABLE_ROUTING.md](CABLE_ROUTING.md).

### Fas 6 — Koppla till Jackpot och dator

- [ ] **6.1** Jackpots utgångsbygel på 5 V. Läs maskinens aktuella `config.yaml`, kör `konfig.py`, granska de sex raderna, ladda upp. Ladda upp makrona.
- [ ] **6.2** Från konsolen, fräsen avstängd: stift ut och in, `arm_ut.nc`, `arm_in.nc`. Godkänt: rätt rörelse, servot släpper vid stoppen.
- [ ] **6.3** `?` i konsolen med stiftet fritt och intryckt för hand. Godkänt: probe-statusen växlar åt rätt håll.
- [ ] **6.4** Strömbortfall: slå av maskinens matning med parkerad arm. Godkänt: armen stannar parkerad, Pi:n lever vidare (D023).
- [ ] **6.5** Märke och armmönster (L6), sedan armspärrens inlärning med riktiga bilder i båda lägena. Godkänt: `cnc armsparr kolla` säger parkerad respektive utfälld; täckt lins ger stopp.
- [ ] **6.6** LED-fästet printas och monteras (L5), listen tänds. Godkänt: jämnt ljus i kamerabilden utan blänk på blanka beslag.
- [ ] **6.7 Knackprov:** knacka på tornet och verktygsfästet medan `/adxl?s=2` spelar in. Godkänt: tornets första resonans ligger över 1,2 kHz eller utanför 300–1000 Hz (fräsens tandfrekvenser). Annars styvas fästet.
- [ ] **6.8 Störningsprov:** KATSU igång utan ingrepp, `?` i konsolen i 5 minuter. Godkänt: probe-statusen växlar aldrig. Därefter G38 i luften med KATSU igång: inget falskt stopp.
- [ ] **6.9 Långkörning:** en timme med bilder var tionde sekund, `vcgencmd measure_temp` och lufttemperatur i tornet loggas. Godkänt: luft under 50 °C, processor under 80 °C, ingen strypning.
- [ ] **6.10 Cykelprov:** armen ut och in 200 gånger. Godkänt: CR Touch-kabeln hel (kontinuitet), magneten håller, stoppen oskadda.
- [ ] **6.11 Uppstartsrutin:** KATSU går inte före grön knapp; nödstoppet stoppar; märkfärgen på M5 obruten.

### Fas 7 — Mätning och kalibrering, på spill

Kräver att grundmaskinens Z-nivå och squaring nedan är godkända, annars mäter kameran och proben fel maskin.

- [ ] **7.1** Stiftets offset mot fräsens spets (L7).
- [ ] **7.2** `mat_z.nc` tio gånger på samma punkt. Godkänt: spridning under 0,05 mm.
- [ ] **7.3** Kamerakalibrering enligt `cnc` (beslut 0034) och XY-kontroll mot fräst kontur. Godkänt: under 0,5 mm fel.

### Fas 8 — Övervakning under fräsning

- [ ] **8.0 Dammprov:** efter ett jobb på spill: linsen, mikrofonens nät och CR Touchens stift kontrolleras; armspärren ska inte larma för oskärpa.
- [ ] **8.0b Vibrationsnivå:** ADXL:ens toppvärde under fräsning jämförs med magnetens marginal (ca 3,7 g). Ligger toppen över: byt till magnet Ø8 × 3.
- [ ] **8.1** Spela in ADXL och mikrofon under ett stegrat prov på spill och jämför med körloggen, enligt [verktygsövervakningen](https://github.com/kingkongola/cnc/blob/main/docs/verktygsovervakning.md). Godkänt: ett avsiktligt fel syns tydligt över bruset.

Utbyggnad efter fas 8 (bildsammanfogning, skruvbrickor, materialindexering) är inte krav för första versionen; se [kameraunderlaget](machine/KAMERA_ANHALL.md).

## Grundmaskin — kvarstående dokumenterade kontroller

- [ ] Z-nivå efter permanenta struts och planfräst offerskiva; ännu inte loggad som godkänd i [CALIBRATION.md](CALIBRATION.md).
- [ ] Ytterligare squaringkontroll efter offerskivearbetet som begärdes i byggloggen. Den tidigare godkända mätningen ska inte raderas; se mätloggen.
- [ ] Full X/Y/Z-rörelse med slang och kablar, därefter slutlig dragavlastning och uppmätta kabelkaplängder i [CABLE_ROUTING.md](CABLE_ROUTING.md).
- [ ] Cyklonens färdigställande, behållare, ventil-/vakuumprov och jordväg för dammhanteringen: senaste loggade status finns i [BUILD_LOG.md](BUILD_LOG.md). Senare slutrapport saknas.
- [ ] Bekräfta slutligt utförande/prov av kapsling, dragavlastning och maskinstopp/NVR (återstartsskydd, som hindrar automatisk start efter strömavbrott). Någon slutrapport för dessa elkontroller har inte hittats i genomgången. Kraven ägs av [AUDIT.md](AUDIT.md); detta är inte en uppgift om att installationen faktiskt saknas.

Dessa punkter hindrar inte fristående provprint av sensordelar. Maskinrörelser och probning kräver sitt eget verifierade förfarande.
