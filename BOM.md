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

- [ ] **Jackpot3 CNC Controller** — Elecrow `CQA240812C2`, $76.99 observerat 2026-08-29, in stock, 300 g; kräver flashning. Sverige-frakt/import fortfarande checkout-gated.
- [ ] 5 × NEMA17-stegmotorer — StepperOnline `5-17HS19-2004S1`, 59 Ncm / 83.55 oz-in, 2 A, 5 mm D-axel, 24 mm axel, 1 m kabel
- [ ] stepper wire extenders endast där dry-fit visar att motorernas befintliga 1 m-kablar inte räcker
- [ ] 3 × GT2 10 mm, 16T remhjul, 5 mm hål
- [ ] 6 × GT2 10 mm, 20T släta idlers, 5 mm hål
- [ ] GT2 10 mm rem — låsta segment 999 / 1705 / 1705 mm; 5 m totalt räcker
- [ ] **5 × Omron `SS-3GL13PT` installerade; planerat köp 10 st från DigiKey (5 reserv)**
- [ ] **10 m LaskaKit `LA150151A`, UL2464 26 AWG 3×0,14 mm²**, använd 2 ledare för NC-endstops
- [ ] 5 × 2-poliga 2,54 mm board-side endstopkontakter/pigtails; köp extra kontakter billigt för reserv
- [ ] 14 × 608-2RS lager; köp helst 20-pack <=200 kr levererat
- [ ] 2 × T8 trapetsskruv + mutter, minst 145 mm, 4-start / 2 mm pitch / 8 mm per varv
- [ ] 2 × koppling 5 mm → 8 mm
- [ ] **Mean Well `HDR-60-24`, 24 V / 2,5 A / 60 W DIN-nätaggregat**
- [ ] ca 1 m flexibel **20 AWG / ~0,52 mm² 2-ledare** från HDR-60-24 till Jackpot3; LaskaKit UL2464-familj, välj uttryckligen 2-core i dropdown
- [ ] **genuin KEDU KJD12**, 230 V, DPST/2-polig, NVR/no-restart, emergency-stop cover; köp <=500 kr levererat. IKH `XW026-1` är svensk fallback ~482 kr levererat men tillverkaren är inte uttryckligen KEDU på sidan.
- [ ] **IP65 DIN-kapsling för KJD12 + HDR** — Biltema `35-0065`, 4 moduler, 120×160×90 mm, integrerad DIN-skena, 99,90 kr. Dry-fit KJD12 + HDR innan håltagning. Biltema `35-0067`, 12 moduler, 229 kr är fallback om den lilla blir trång.
- [ ] **1 × 3 m jordad 3G1,5 / 16 A skarvsladd som donor för fabriksmonterad han- och honkontakt**, t.ex. Biltema `46-3610`, 59,90 kr
- [ ] **2 × M20 kabelgenomföring/förskruvning** för 3G1,5-pigtails, t.ex. Jula/Rutab `402070`, 2-pack 39,90 kr
- [ ] **3 × genuin Wago 221-413** för intern L/N/PE-fördelning; Jula 12-pack `001480` 129 kr om inga redan finns
- [ ] **4 × isolerad 6,3×0,8 mm flatstiftshylsa/Faston** som passar faktisk KJD12 + 1,5 mm² kabel; Biltema helisolerad 1,5–2,5 mm² `44-0020` är billig referens
- [ ] **VEVOR 0700C, 800 W, 65 mm router** — exakt SKU `YXKXBJ710W65AH7WLV2`, product ID `010235793217`; €83.99 observerat 2026-08-29, VEVOR EU Sverige-frakt förväntat €0
- [ ] **3 × Sorotec `L1S.M.0317`**, 3,175 mm single-flute upcut, 9 mm skärlängd — första/commissioning-fräsar. €3,70/st; tre + Sorotec Sverige-frakt ~€19,40 totalt.
- [ ] **lång 3,175 mm single-flute 25–32 mm skärlängd** endast när första 18–19 mm plywood-jobbet faktiskt ska göras; köp inte nu
- [ ] **SUNLU ordinary PLA, 6 × 1 kg normalspolar Mix & Match** — nuvarande Pareto-förstaval, cirka €9,19/kg / ~€55,14 för 6 kg om checkout håller bulkpris och EU-frakt. 5 kg-jättespole ~€39,99 är absolut billigare men inte förstaval.
- [ ] **2 × Motonet rundrör Ø30×1,5 mm ×2 m, artikel `88-7123`, 189 kr/st observerat**; kontrollera faktisk OD/straightness, kapa till 1505 / 816 / 816 mm
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
- [ ] **ingen dedikerad clamp/T-track-order för första körningarna** — skruva arbetsstycke/sacrificial tabs direkt i MDF-spoilboard utanför toolpath; printa cam/edge clamps när verkliga jobb kräver det
- [ ] värmekrympslang för endstoplödpunkter
- [ ] ändhylsor/ferrules där de passar skruvterminalerna, om lämplig tång redan finns

### Valfritt senare

- [ ] touch plate / verktygslängdsgivare
- [ ] T-track / threaded-insert-grid / vacuum-table endast efter faktisk användning visar behov
- [ ] laser — tidigast 2027, inte del av nuvarande grundbygge

## Styrkort — Jackpot3

**Val:** Jackpot3.

Aktuella priser verifierade 2026-08-29:
- V1E: **$75.99**, pre-flashed för LR4
- Elecrow: **$76.99**, SKU `CQA240812C2`, in stock, måste flashas

Jackpot3 innehåller **6 integrerade TMC2226-drivare**, så inga separata stepperdrivare ska köpas.

Elecrow är fortfarande förstaval för Sverige eftersom V1E själv rekommenderar den direkta internationella rutten, men slutkostnaden måste inkludera frakt, svensk moms, den nya lågvarutullen från 1 juli 2026 och eventuell transportörs administrationsavgift. Se `research/2026-08-29-jackpot3-order.md`.

**Jackpot2 väljs bort:** $55 är billigare headline, men den saknar PWM på utgångarna. Det är en onödig framtida begränsning med planerad laser senare.

## PSU — Mean Well HDR-60-24

**Val:** Mean Well **`HDR-60-24`**, 24 V / 2,5 A / 60 W, DIN-rail.

Current planned source: DigiKey together with exact Omron endstops.

Reasons:
- correct V1-class 24 V / 60 W supply
- closed/touch-protected DIN format rather than exposed LRS terminals
- cheaper current procurement path than the external GST60 brick
- fits the planned compact machine-level NVR/control enclosure cleanly

See `research/2026-08-29-final-psu-endstop-wiring-cart.md`.

## 230 V maskinmatning / kapsling

**Baseline:**

`vägg -> KJD12 -> [HDR-60-24 + DeWalt AUTO]`

`VEVOR -> DeWaltens verktygsuttag`

DeWalt-manualen anger 2450 W max ansluten verktygslast; VEVOR är 800 W. Ingen separat vakuumtrigger behövs.

Kapslings-Pareto:
- **Biltema `35-0065`, 4 moduler, IP65, 120×160×90 mm, DIN-skena inkluderad, 99,90 kr**
- Biltema `35-0067`, 12 moduler, IP65, 225×200×110 mm, 229 kr är fallback om den lilla blir trång
- KJD12 monteras i sida/ände först **efter fysisk mall/dry-fit**; KJD12 finns i flera mekaniska varianter
- HDR på DIN-skenan
- billig 3 m 3G1,5/16 A skarvsladd återbrukas som fabriksmonterad Schuko-hane in + Schuko-hona ut
- tre Wago 221-413 delar L/N/PE
- PE är kontinuerlig och oswitchad till DeWalt-uttaget
- 2 × M20-förskruvning ger dragavlastning för nätpigtails

Budget för kapsling/fördelning exklusive KJD12 och HDR: **~354 kr om allt köps nytt**, runt **~200 kr** om Wago/Faston redan finns.

Se `research/2026-08-29-mains-enclosure-distribution.md`.

## Första frässtål / workholding

**Första köp:** 3 × Sorotec `L1S.M.0317`.

- 3,175 mm diameter och skaft
- single flute upcut
- 9 mm skärlängd
- solid carbide
- €3,70/st
- Sorotec Sverige-frakt upp till 0,5 kg: €8,30
- tre fräsar levererat ungefär €19,40

De korta fräsarna används först för XPS, tunnare material, testkörningar och de permanenta ~6 mm strutsen. De är styvare och bättre att lära sig på än en extra lång fräs.

**Lång fräs:** vänta. När 18–19 mm plywood verkligen ska profilfräsas köps 1–2 single-flute med minst ~22–25 mm faktisk skärlängd; EU-kandidater finns kring €8–10.

**Workholding:** börja med raka skruvar/sacrificial tabs i MDF-spoilboard. Ingen T-track, insert-grid eller clamp-kit behövs för commissioning. Se `research/2026-08-29-first-cutters-workholding.md`.

## Endstops

**Exact type:** Omron `SS-3GL13PT`.

- LR4 requires 5 installed
- planned buy: **10** at DigiKey qty-10 tier
- five spares cost only ~32 SEK more than buying five at the current price structure
- wire **Normally Closed**, using COM + NC
- default switch termination: solder + heatshrink

## Router — VEVOR 0700C 800 W Makita-klon

**Val:** VEVOR **0700C**, SKU `YXKXBJ710W65AH7WLV2`, product ID `010235793217`.

Current official VEVOR EU observation 2026-08-29:
- **€83.99**
- in stock
- 220–240 V / 50 Hz
- 800 W
- 65 mm body
- 10 000–30 000 rpm
- standard VEVOR EU shipping policy implies **free Sweden shipping** for this non-heavy product

This replaces the old price-unknown state and the stale 710 W candidate.

### Köpt Makita/Elaire 3,175 mm-spännhylsa → VEVOR 0700C

**Status 2026-08-29: hög sannolikhet att den passar; ska provpassas före drift.**

Den köpta HaWiWe-hylsan är en **Elaire Makita-style 1/8" collet**, produktfamilj **MRP-1250**, avsedd för bl.a. Makita RT700C / RT0700CX3 / RT0701C.

Det saknas ett explicit datablad från Elaire/VEVOR som nämner exakt kombinationen MRP-1250 + VEVOR 0700C. När routern kommer: provpassa hylsan utan verktyg, kontrollera korrekt säte i kona/mutter och kontrollera därefter runout med ett rakt 1/8"-verktyg.

## Rails — Motonet 30 mm

**Nuvarande förstaval:** Motonet `88-7123`, rundrör **Ø30×1,5 mm, 2 m**.

V1E accepterar 30 mm OD och minst 1,3 mm vägg, så nominellt är röret direkt inom LR4-spec.

Köp:
- 2 × 2 m
- observerat pris: **189 kr/st = 378 kr totalt**

Kapa:
- 1505 mm
- 816 mm
- 816 mm

Kontrollera med skjutmått att faktisk OD ligger ungefär 29,8–30,2 mm och välj raka/oslagna exemplar innan kapning. Se `research/2026-08-29-steel-tubes-gavle.md`.

## Motorer

**Val:** StepperOnline 5-pack **`5-17HS19-2004S1`**.

StepperOnline-order ska hållas motors-only om inte checkout visar en annan redan behövd del från samma Germany warehouse. PSU ska inte flyttas dit via China-route bara för falsk samfrakt.

## Redan täckt av HaWiWe-köpet

- [x] XZ-plattor
- [x] 4 × MGN12H 150 mm linjärskenor
- [x] LR4-skruv/mutter-set — exakt innehåll dokumenterat ovan
- [x] Makita/Elaire 3,175 mm-spännhylsa — köpt; hög sannolikhet att den passar vald VEVOR 0700C, ska provpassas innan drift