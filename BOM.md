# BOM

Här ska bara delar för den LowRider V4 som faktiskt byggs finnas.

## Inköpsförutsättning

- [x] **Amazon Prime-medlemskap** — använd Prime som möjlig fraktfördel, men välj butik efter totalpris inklusive frakt.

## Redan köpt — HaWiWe, 29 augusti 2026

**Order betald.** Ordertotal: **165,50 € inklusive 8,00 € frakt**.

- [x] Aluminium XZ plates — **39,50 €**
- [x] Linear rail set LowRider 4 — **57,00 €**
- [x] Screw set LowRider 4 — **32,00 €**
- [x] Makita/Elaire 1/8 inch (3,175 mm) collet — **29,00 €**
- [x] Frakt — **8,00 €**

### Exakt innehåll i köpta HaWiWe Screw set LowRider 4

Verifierat mot HaWiWe produktsida **2026-08-29**:
https://hawiwe.de/produkt/schraubenset-lowrider-4/

- [x] 14 × **M8×40**, DIN 933 / ISO 4017, 8.8, förzinkad
- [x] 14 × **M8 nyloc/låsmutter**, DIN 985
- [x] 60 × **M5×30**, DIN 7985, 4.8, krysspår, förzinkad
- [x] 60 × **M5 nyloc/låsmutter**, DIN 985
- [x] 83 × **M3×10**, DIN 7985, 4.8, krysspår, förzinkad
- [x] 10 × **M2.5×12**, DIN 7985, 4.8, krysspår, förzinkad

**Viktigt:** detta kit är endast skruvar + muttrar. Det innehåller **inte** lager, T8-skruvar, T8-muttrar, kopplingar, remhjul, idlers, rem, ändlägen, motorer, kablage eller nätaggregat.

## Redan ägt — relevant verkstadsutrustning/material

- [x] **DeWalt grovdammsugare / wet-dry shop-vac**, mycket sannolikt **DXV30SAPTA** enligt användarens Jula-skärmdump. 30 l, 1050 W, 15 kPa, 37,8 l/s, 48 mm × 2,1 m slang. Bekräfta typskylt innan modellunika reservdelar beställs.
- [x] **Äldre FTX-aggregat**, modell/prestanda ännu okänd. Potentiell återbrukskandidat för sekundär luftfiltrering eller undertryck/utsug kring CNC-zonen; ska inte matas med rått CNC-spån/damm utan separat primäravskiljning.
- [x] **TPU-filament** — finns redan. Kontrollera durometer på rullen; cirka 95A är V1E:s standard för LR4 dust-shoe-bristles. Ingen TPU ska köpas för bygget.

## Kvar till själva LR4-maskinen

### Måste köpas

- [ ] **Jackpot3 CNC Controller**
- [ ] 5 × NEMA17-stegmotorer — StepperOnline `5-17HS19-2004S1`, 59 Ncm / 83.55 oz-in, 2 A, 5 mm D-axel, 24 mm axel, 1 m kabel
- [ ] stepper wire extenders endast där dry-fit visar att motorernas befintliga 1 m-kablar inte räcker
- [ ] 3 × GT2 10 mm, 16T remhjul, 5 mm hål
- [ ] 6 × GT2 10 mm, 20T släta idlers, 5 mm hål
- [ ] GT2 10 mm rem — låsta segment 999 / 1705 / 1705 mm; 5 m totalt räcker
- [ ] **5 × Omron `SS-3GL13PT` installerade; planerat köp 10 st från DigiKey (5 reserv)**
- [ ] **10 m LaskaKit `LA150151A`, UL2464 26 AWG 3×0,14 mm²**, använd 2 ledare för NC-endstops
- [ ] 5 × 2-poliga 2,54 mm board-side endstopkontakter/pigtails; köp extra kontakter billigt för reserv
- [ ] 14 × 608-2RS lager
- [ ] 2 × T8 trapetsskruv + mutter, minst 145 mm, 4-start / 2 mm pitch / 8 mm per varv
- [ ] 2 × koppling 5 mm → 8 mm
- [ ] **Mean Well `HDR-60-24`, 24 V / 2,5 A / 60 W DIN-nätaggregat**
- [ ] ca 1 m flexibel **20 AWG / ~0,52 mm² 2-ledare** från HDR-60-24 till Jackpot3; LaskaKit UL2464-familj, välj uttryckligen 2-core i dropdown
- [ ] **VEVOR 0700C, 800 W, 65 mm router**
- [ ] minst 1 × 1/8" / 3,175 mm single-flute frässtål
- [ ] PLA för LR4-delarna — ca 2,7 kg faktisk förbrukning; köp med marginal
- [ ] stålrör i slutliga längder: 816 / 816 / 1505 mm
- [ ] bord/underrede
- [ ] plan bordsskiva / löstagbar spoilboard
- [ ] material till permanenta 819 mm strut plates, max 6,35 mm; bootstrap med printade temp-struts och fräs slutliga ur billig skivrest
- [ ] ca 18 × M4×12 mm eller längre trä-/plåtskruv för infästning i bordet; V1E anger dessa separat och de ingår inte i HaWiWe screw set

### Dammhantering — del av grundbygget

- [ ] LR4 dust shoe — printas; **printa V1E:s TPU-bristles med redan ägd TPU om den är ~95A**. 1 mm hobbyfoam finns kvar som fallback.
- [x] grovdammsugare / shop-vac — befintlig DeWalt, sannolikt DXV30SAPTA
- [ ] cyklonavskiljare — **3D-print först**, kommersiell separator endast fallback
- [ ] separat styv 15–30 l uppsamlingsbehållare före DeWalt; billig stålhink/askhink är förstaval
- [ ] rörlig dammsugarslang — **testa befintlig DeWalt 48 mm × 2,1 m först**; köp 2.5" endast om dry-fit/prestanda kräver det
- [ ] kort stationär cyklon→DeWalt-koppling, helst slangstum/rör/printad adapter
- [ ] slangupphängning/dragavlastning så slangen inte belastar Z/gantry
- [ ] enkel avskärmning/gardin eller annan lösning som håller CNC-smutszonen lättstädad
- [ ] jordning/antistatisk lösning; befintlig DeWalt-slang är inte dokumenterad som ESD, så separat jordledare enligt V1E-plan ska utvärderas
- [ ] utvärdera befintligt FTX-aggregat som sekundär luftfiltrering/undertryck efter att modell och flöde identifierats

### Rekommenderat / småsaker

- [ ] gänglåsning för remhjulens stoppskruvar
- [ ] lätt smörjmedel till idlers/linjärskenor
- [ ] buntband eller annan kabelinfästning
- [ ] arbetsstyckesfastsättning/clamps
- [ ] värmekrympslang för endstoplödpunkter
- [ ] ändhylsor/ferrules där de passar skruvterminalerna, om lämplig tång redan finns

### Valfritt senare

- [ ] touch plate / verktygslängdsgivare
- [ ] laser — tidigast 2027, inte del av nuvarande grundbygge

## Styrkort — Jackpot3

**Val:** Jackpot3.

Aktuella priser verifierade 2026-08-29:
- V1E: **$75.99**
- Elecrow: **$76.99**

Jackpot3 innehåller **6 integrerade TMC2226-drivare**, så inga separata stepperdrivare ska köpas.

## PSU — Mean Well HDR-60-24

**Val:** Mean Well **`HDR-60-24`**, 24 V / 2,5 A / 60 W, DIN-rail.

Current planned source: DigiKey together with exact Omron endstops.

Reasons:
- correct V1-class 24 V / 60 W supply
- closed/touch-protected DIN format rather than exposed LRS terminals
- cheaper current procurement path than the external GST60 brick
- fits the planned machine-level NVR/control enclosure cleanly

See `research/2026-08-29-final-psu-endstop-wiring-cart.md`.

## Endstops

**Exact type:** Omron `SS-3GL13PT`.

- LR4 requires 5 installed
- planned buy: **10** at DigiKey qty-10 tier
- five spares cost only ~32 SEK more than buying five at the current price structure
- wire **Normally Closed**, using COM + NC
- default switch termination: solder + heatshrink

## Router — VEVOR 0700C 800 W Makita-klon

**Val:** VEVOR **0700C**, 800 W, 220–240 V / 50 Hz, 65 mm kropp, 10 000–30 000 rpm.

Detta ersätter den tidigare 710 W VV-1B-220V-kandidaten.

VEVOR anger Makita 0700-bas-kompatibilitet för denna 0700C-familj. Det finns dessutom dokumenterad V1E-erfarenhet där en VEVOR 0700C körs med en Makita-style/Sienci 1/8"-spännhylsa i VEVOR:s originalmutter med mycket liten runout.

### Köpt Makita/Elaire 3,175 mm-spännhylsa → VEVOR 0700C

**Status 2026-08-29: hög sannolikhet att den passar; ska provpassas före drift.**

Den köpta HaWiWe-hylsan är en **Elaire Makita-style 1/8" collet**, produktfamilj **MRP-1250**, avsedd för bl.a. Makita RT700C / RT0700CX3 / RT0701C.

Det saknas ett explicit datablad från Elaire/VEVOR som nämner exakt kombinationen MRP-1250 + VEVOR 0700C. När routern kommer: provpassa hylsan utan verktyg, kontrollera korrekt säte i kona/mutter och kontrollera därefter runout med ett rakt 1/8"-verktyg.

## Motorer

**Val:** StepperOnline 5-pack **`5-17HS19-2004S1`**.

StepperOnline-order ska hållas motors-only om inte checkout visar en annan redan behövd del från samma Germany warehouse. PSU ska inte flyttas dit via China-route bara för falsk samfrakt.

## Redan täckt av HaWiWe-köpet

- [x] XZ-plattor
- [x] 4 × MGN12H 150 mm linjärskenor
- [x] LR4-skruv/mutter-set — exakt innehåll dokumenterat ovan
- [x] Makita/Elaire 3,175 mm-spännhylsa — köpt; hög sannolikhet att den passar vald VEVOR 0700C, ska provpassas innan drift
