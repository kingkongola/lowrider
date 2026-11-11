# Procurement — canonical order matrix

**Leveransstatus uppdaterad 2026-11-10.** Äldre pris- och lagerunderlag är daterade inköpsögonblick, inte dagens erbjudanden. Syfte: minimera total landad kostnad utan att ändra låsta specs. Lager/priser är flyktiga; faktisk checkout vinner alltid över denna snapshot. Faktiskt debiterade SEK-belopp bokförs i `COSTS.md`.

## Mikrobrytare för sensorenhet – beställda 2026-11-09

**Amazon.se / QUARKZMAN KW11-3Z-N**, 10 st, rullspak, **1NO + 1NC (SPDT)**. Användaren bekräftade köp 2026-11-09; **visat pris 92,94 kr för 10-pack**, Prime med gratis frakt, **beräknad leverans lördag 2026-11-14**. Amazon-produktlänk: https://amzn.eu/d/06DL5wYW. **Ännu ej mottagna och faktisk kortdebitering ej uttryckligen verifierad**; bokför inte 92,94 kr som debiterat i `COSTS.md` förrän bekräftat.

**Aktuell användning:** reservdelar. Armbrytare och deras hållare utgick genom [D020](DECISIONS.md#d020--inga-armbrytare-hårda-stopp-tyngdkraft-och-kamerakontroll). De ska inte inväntas eller monteras för sidotornet. Omron-reserven behålls till grundmaskinen. Tidigare brytarstudie finns i [arkivet](docs/arkiv/2026-11-09-status-och-sensorunderlag.md).

## Electrokit — mottaget 2026-11-10

**Källa:** användarens skärmbild av Electrokit-order/kvitto 2026-11-09 (priserna på orderraderna visas **exklusive 25 % moms**). Orderbilden bekräftar följande produkter och antal. **Användaren bekräftade 2026-11-10 att kameran och allt i Electrokit-order har kommit.** Det bekräftar mottagning, men inte funktion, passning eller faktisk kortdebitering.

| Produkt | Electrokit art.nr | Antal | Orderrad exkl. moms | Inkl. moms |
| --- | --- | ---: | ---: | ---: |
| Raspberry Pi Camera Module 3 **Standard** (inte Wide) | `41020240` | 1 | 271,20 kr | 339,00 kr |
| Raspberry Pi Zero 2 WH med header | `41022617` | 1 | 199,20 kr | 249,00 kr |
| Raspberry CSI-kamerakabel 200 mm | `41020808` | 1 | 23,20 kr | 29,00 kr |
| 3-axlig accelerometer ADXL345, I2C/SPI | `41016234` | 1 | 55,20 kr | 69,00 kr |
| USB-C till UART (TTL) modul 3,3/5 V, 6-pin, flödeskontroll 6 Mbps | `41035679` | 1 | 55,20 kr | 69,00 kr |
| Testsladdar krokodil 1 m röd + svart | `41022876` | 2 | 51,20 kr | 64,00 kr |
| Micro-testklämmor 10-pack | `41020723` | 1 | 119,20 kr | 149,00 kr |
| Kopplingskabel 40-pol 30 cm Dupont hona/hona | `41012685` | 1 | 44,00 kr | 55,00 kr |
| Testsladdar med banankontakt/krokodil, 3 st | `41010187` | 1 | 31,20 kr | 39,00 kr |

**Delsumma synliga varor:** 849,60 kr exkl. moms. **Frakt:** 39,20 kr exkl. moms; **moms:** 222,20 kr. Dessa belopp motsvarar **1 111,00 kr inkl. moms** för just dessa synliga orderrader. Orderns sista summa är delvis skymd i skärmbilden; bokför därför ännu inte detta som **faktiskt debiterat** i `COSTS.md`.

**Kamerasatsens tre rader:** 493,60 kr **exkl. moms** / **617,00 kr inkl. moms**, utan att allokera gemensam frakt. **Modellvalet är nu definitivt verifierat: Camera Module 3 Standard**, inte Wide; Zero 2 WH och 200 mm CSI-kabel ingår också i den mottagna ordern. Bekräfta fysisk kontakt-/pin-kompatibilitet och kabelräckvidd vid provmontering; artikeltexten i skärmbilden ensam säger inget om mekanisk frigång.

## Övriga sensorleveranser

- **CR Touch Auto Leveling Kit:** användaren bekräftade 2026-11-10 att proben nu är tillgänglig och att kitet heter **CR Touch Auto Leveling Kit**, inte BLTouch som tidigare antagits. Exakt revision, kitinnehåll, mått, elektrisk anslutning och funktion är inte verifierade. Ingen köp-/betalningsuppgift har lämnats. Ingår inte i Electrokit-orderbilden. Detta ersätter den tidigare uppgiften om BLTouch som ännu skulle hämtas hos grannen.

**Kitinnehåll undersökt:** Crealitys standardkit beskrivs i [CR Touch-underlaget](research/2026-11-10-crtouch-anpassning.md). Dokumenterad packlista är inte fysisk kartonginventering. Sensor, kabel och monteringsskruvar kan användas i vår anpassning; inget nytt prob- eller Ender-beslagsköp behövs utifrån konstruktionsbytet.
- **INMP441:** tidigare uppgift om beställning finns, men exakt antal, modell och leverans är fortsatt obekräftade. Den ska inte markeras mottagen genom Electrokit-leveransen.
- **Spektrum S664 / SPMS664:** befintligt servo, använt i dagens bänkprov. Resultat ägs av [mätloggen](CALIBRATION.md#2026-11-10--fällservots-rörelseomfång-verifierat-på-bänk).

**Ansvar:** fysisk monterings-/kollisionskontroll, spänningsnivåer, kraftmatning, probens verkliga signaler och maskinkonfiguration hör hit. [CNC:s kamerakod](https://github.com/kingkongola/cnc/blob/main/docs/kamera-kod.md) är endast offline-prototyp; ingen optisk maskinkalibrering har verifierats på riktig hårdvara.

## Redan betalt / beställt

### HaWiWe — CLOSED / SHIPPED

- ordervaluta: **165,50 € inklusive 8,00 € frakt**
- faktiskt debiterat: **1 853 kr**
- innehåll: 6,0 mm XZ-plattor + 4 × MGN12H 150 mm + LR4 screw set + Makita/Elaire 1/8" collet

### Elecrow — CLOSED / ORDERED

- 1 × Jackpot3 CNC Controller `CQA240812C2`
- controller efter rabatt: **69,44 €**
- DDP Economy: **14,11 €**
- checkout total: **83,55 €**
- faktiskt debiterat: **937 kr**

### eBay / POWGE — CLOSED / RECEIVED

- 3 × **2GT/GT2 drive pulley, 16T, 5 mm bore, för 10 mm belt, 2 mm pitch**
- faktiskt debiterat: **72 kr**
- **Mottagna 2026-09-21** enligt användaren. Kontroll av faktisk håldiameter, tandantal och passning återstår.

### LaskaKit, Tjeckien — CLOSED / RECEIVED

Köpt 2026-09-03, mottaget och inventerat komplett 2026-09-13:
- 6 × `LA190008E` smooth GT2 idler, 5 mm bearing, 10 mm belt
- 1 × `LA190032A` T8×8 400 mm, 4-start / 8 mm lead
- 2 × `LA190031` flexible coupling 5→8 mm
- 1 × `LA190013C` GT2 5 m × 10 mm fiberglass belt
- faktiskt debiterat: **444 kr**

### DigiKey — CLOSED / RECEIVED

Köpt 2026-09-03, hämtat/mottaget 2026-09-09: PSU, endstops, lager, Wago, glands, Faston, kablage och board-pigtails.
- faktiskt debiterat: **986,98 kr**
- innehållet ska fortfarande räknas av mot BOM innan montering

### Amazon.se — motorer — CLOSED / ORDERED / DEBITED

- **5 × STEPPERONLINE `17HS19-2004S1`**
- faktiskt debiterat enligt bekräftelse 2026-09-10: **608,37 kr**, Prime/fri frakt

### Amazon.se — KATSU router — CLOSED / ORDERED / DEBITED

- **KATSU `101750`**, 220–240 V, 710 W, ~65 mm
- faktiskt debiterat enligt bekräftelse 2026-09-10: **620,00 kr**, Prime/fri frakt

### Amazon.se / euroharry — T8×8 brass nuts — CLOSED / RECEIVED / DEBITED

Beställt 2026-09-05, mottaget 2026-09-10:
- 4 × flänsad T8-mässingsmutter, Ø8 mm, 2 mm pitch, 4-start, 8 mm lead
- faktiskt debiterat enligt bekräftelse 2026-09-10: **101,76 kr**, Prime
- 2 används i LR4 + 2 reserv

### PrintOnion — PLA — CLOSED / ORDERED

Köpt 2026-09-06:
- **3 kg PLA, 1,75 mm**
- faktiskt betalt: **426 kr**

### Motonet — rör — CLOSED / PURCHASED

Köpt 2026-09-07:
- **2 × stålrör för LR4**, planerad spec `88-7123`, Ø30×1,5×2000 mm
- faktiskt betalt: **340 kr totalt**
- **kapa inte ännu**; bekräfta faktisk OD/rakhet/längd före kapning till 1505 / 816 / 816 mm

## Blockerade / ej aktiva sourcingvägar

### eBay / HKGY01 T8×8-muttrar — CANCELLATION PENDING / OUT OF STOCK

- tidigare order: 2 × T8×8 brass nut
- faktiskt debiterat: **67 kr**
- ersatt av Amazon.se/euroharry
- återbetalningen bokförs först när den faktiskt är verifierad

### VEVOR `0700C` router — BLACKLISTED

Köp inte VEVOR `0700C`. KATSU `101750` är köpt ersättare.

### 3DJake PLA — INACTIVE / REPLACED

Ersatt av PrintOnion-köpet: 3 kg PLA för 426 kr.

## Lokalt / separat

### Bord / spoilboard

- **180×100 cm begagnad bordsskiva köpt för 300 kr** (rapporterat 2026-09-19); ingen ytterligare skiva ska köpas för grundbygget
- kontrollera att underredet är lämpligt/styvt; eventuellt underredesmaterial först om faktiskt behov finns
- minimumfootprint är 941×1563 mm: den köpta skivan rymmer detta utan den äldre 90 cm-breddningen
- använd köpt skiva direkt som strukturell maskinbas; köp ingen full OSB/ply-deck som baseline
- köp senare ~12 mm löstagbar MDF-spoilboard över arbetsområdet

### Permanenta struts

- 5–6 mm MDF/hardboard, max 6,35 mm
- printa 4 temporära struts (15 % infill), bygg/driftsätt LR4 och fräs sedan egna permanenta front-/bottenplattor med maskinen. Köp material när första skäret närmar sig; strut-generator: `strut_length=819`, `front_wing_size=10.8`.

### NVR/maskinstopp

**Köps inte** (D024, 2026-11-10): ersatt av kontaktorlådan nedan. Tidigare kandidat: Clas Ohlson `50-2929`, KJD12, 299 kr.

### KATSU-stopp från Pi:n, trådbundet — planerat, ej beställt

Användarens val 2026-11-10: kontaktorlösningen, ca 500 kr totalt; ersätter även NVR-brytaren (D024). Pi:n håller kontaktorn dragen; Pi-krasch, omstart, strömavbrott eller nödstopp släpper den, och KATSU startar bara efter tryck på grön knapp (Pi:ns pinnar är av vid start). Bryter bara KATSU, så Jackpot håller Z. Inget nätverk i stoppkedjan; Pushover-notis efteråt.

| Del | Kandidat | Pris |
| --- | --- | ---: |
| Modulkontaktor 24 V AC/DC, 2 × NO, 25 A | Electrokit, Iskra IKD225-20-24V | 219 kr |
| Transistorkort för spolen (< 0,1 A) | ej valt | några tior |
| Kapsling med DIN-skena, stickpropp, uttag | ej valt | ca 150 kr |
| Nödstopp (svampknapp) med **två** brytande kontakter | ej valt | ca 60–100 kr |
| Grön startknapp | ej valt | ca 20 kr |
| Optokopplare, Pi:ns stoppsignal till Jackpot | ej valt | några kr |
| **Summa** | | **ca 500 kr** |

Före köp: motorlastklass (AC-7b/AC-3) i kontaktorns datablad. 230 V-delen kopplas av någon van vid nätspänning. Spolen matas från övervakningens nätdel (D023), som ännu inte är vald.

### Biltema/elbox

Kapsling, donor 3G1,5 och lokal elsmåvara först efter fysisk dry-fit av NVR + HDR.

## Uppskjutet

### Sorotec-fräsar

`L1S.M.0317` eller motsvarande 3,175 mm single-flute upcut: **DEFER** tills första skär närmar sig.

## Orderarkitektur nu

Inga fler huvudorder för kärnmekanik/elektronik/prints/rör är öppna.

Kvar att anskaffa eller ordna:
1. **Kontrollera underredet** till redan köpta 180×100-skivan; ordna först om något saknas.
2. **~12 mm MDF-spoilboard** över arbetsområdet.
3. **5–6 mm MDF/hardboard för permanenta struts**, fräses med LR4 efter montering med 4 printade tillfälliga struts.
4. **NVR + kapsling/elmaterial** efter fysisk dry-fit.
5. **Commissioning-fräs** till första skär och struts.
6. **Dammbehållare/slangupphängning** när maskinen byggs.

**Obs:** Alla tre köpta 16T-remhjul är mottagna 2026-09-21. Kontrollera dem vid inventering; köp inte dubbelt.

Motorer, router, controller, PSU, endstops, lager, GT2-delar, T8-skruv, kopplingar, Z-muttrar, 3 kg PLA och rör är köpta/beställda och **samtliga hittills lagda köp är debiterade**. DigiKey-paketet, LaskaKit-paketet och Z-muttrarna är mottagna.

## Checkout-gates

1. Motonet-rör — kontrollera fysisk OD/rakhet/längd före kapning.
2. Köpt 180×100-bordsskiva — verifiera mått, underrede/styvhet och planerad maskinplacering.
3. Markera rail/belt-layout på 180×100-skivan innan infästning; någon planerad kantbreddning för 90 cm behövs inte.
4. KATSU vid leverans — provpassa Elaire 1/8"-collet och kontrollera runout.
5. Stepperkablar — dry-fit innan eventuella extensioner köps.
6. NVR/kapsling — fysisk/layoutmässig dry-fit innan boxstorlek och kabelrutter låses.
