# Procurement — canonical order matrix

**Live snapshot: 2026-09-06.** Syfte: minimera total landad kostnad utan att ändra låsta specs. Lager/priser är flyktiga; faktisk checkout vinner alltid över denna snapshot. Faktiskt debiterade SEK-belopp bokförs i `COSTS.md`.

## Redan betalt / beställt

### HaWiWe — CLOSED / SHIPPED

- ordervaluta: **165,50 € inklusive 8,00 € frakt**
- faktiskt debiterat: **1 853 kr**
- innehåll: 6,0 mm XZ-plattor + 4 × MGN12H 150 mm + LR4 screw set + Makita/Elaire 1/8" collet

### Elecrow — CLOSED / ORDERED

- 1 × **Jackpot3 CNC Controller `CQA240812C2`**
- controller efter rabatt: **69,44 €**
- DDP Economy: **14,11 €**
- checkout total: **83,55 €**
- faktiskt debiterat: **937 kr**

### eBay / POWGE — CLOSED / ORDERED

- säljare: **POWGE Synchronous Belts and Pulleys**
- 3 × **2GT/GT2 drive pulley, 16T, 5 mm bore, för 10 mm belt, 2 mm pitch**
- vald packvariant: **3 × 2GT pulleys**
- listningen visade **fri frakt** och **`Includes import fees`**
- listat leveransfönster vid köp: **17 sep – 7 okt 2026**
- faktiskt debiterat: **72 kr**

### LaskaKit, Tjeckien — CLOSED / ORDERED

Köpt 2026-09-03:
- 6 × `LA190008E` smooth GT2 idler, 5 mm bearing, 10 mm belt
- 1 × `LA190032A` T8×8 400 mm, 4-start / 8 mm lead
- 2 × `LA190031` flexible coupling 5→8 mm
- 1 × `LA190013C` GT2 5 m × 10 mm fiberglass belt

Checkout:
- varor: **30,75 €**
- GLS Sweden: **8,93 €**
- total: **39,68 €**
- faktiskt debiterat: **444 kr**

### DigiKey — CLOSED / ORDERED

Köpt 2026-09-03:
- 10 × `SW768-ND` / Omron-Aratas `SS-3GL13PT`
- 16 × `1995-1010-ND` / 608-2RS 8×22×7 mm
- 1 × `1866-2249-ND` / Mean Well `HDR-60-24`
- 3 × `2946-221-413-ND` / Wago `221-413`
- 2 × `1920-5309720/SET-ND` / Altech `5309 720/SET`
- 10 × `A27824-ND` / TE `3-350820-2`
- 1 × `AIO-CSM12-ND` / Amphenol `AIO-CSM12`
- 3 m × `839-30-00416-DS-ND` / Tensility `30-00416`, 2×20 AWG
- 10 m × `839-30-00377-DS-ND` / Tensility `30-00377`, 3×26 AWG
- 3 × `900-2177961021-ND` / Molex KK 2,54 mm 2-polig 150 mm kabelassembly; kapas till 6 pigtails

Checkout:
- delsumma: **789,58 kr**
- frakt: **0,00 kr**
- VAT: **197,40 kr**
- total: **986,98 kr**
- fraktmetod: **UPS Worldwide Saver**
- Incoterms: **DDP, tull betalas av DigiKey**
- beräknad transporttid: **4 dagar**

### Amazon.se — motorer — CLOSED / ORDERED

Beställt 2026-09-03 från användarens live Amazon-sida:
- **5 × STEPPERONLINE `17HS19-2004S1`**
- 59 Ncm / 84 oz-in
- 2,0 A
- 42×42×48 mm
- Ø5 mm D-axel
- 1 m kabel med kontakt
- pack of 5
- visat pris vid köp: **608,37 kr**
- Prime / fri frakt
- visad leverans: **7 september**

Detta stänger motorsourcingen utan avvikelse från den tidigare referensspecen.

### Amazon.se — KATSU router — CLOSED / ORDERED

Beställt 2026-09-03:
- **KATSU `101750`**
- 220–240 V
- 710 W
- variabelt varvtal
- cirka **64,8/65 mm** motorhus, Makita RT0700-familjens formfaktor
- såld av AIM Tools Ltd, skickas från Amazon enligt live-sidan
- visat pris vid köp: **620,00 kr**
- Prime / fri frakt
- visad leverans: **7 september**

KATSU 101750 ersätter den tidigare VEVOR-planen. Vid leverans ska den redan köpta Elaire/Makita-style 1/8"-hylsan provpassas och runout kontrolleras före riktig fräsning.

### Amazon.se / euroharry — T8×8 brass nuts — CLOSED / ORDERED

Beställt 2026-09-05 från användarens live Amazon-sida:
- **4 × flänsad T8-mässingsmutter**
- för Ø8 mm Tr8-spindel
- **2 mm pitch**
- **4-start**
- därmed **8 mm lead**
- mässing
- 4-pack
- visat orderpris: **101,76 kr**
- Prime

Två muttrar behövs i LR4 och två blir reserv. Detta ersätter den annullerade HKGY01-vägen och stänger sourcingbehovet för Z-muttrarna. Faktisk kortdebitering verifieras separat i `COSTS.md`.

### PrintOnion — PLA — CLOSED / ORDERED

Köpt 2026-09-06:
- **3 kg PLA, 1,75 mm**
- vanlig styv PLA för LR4-printarna
- faktiskt betalt: **426 kr**

Behovet är cirka 2,7 kg, så 3 kg täcker basbyggets utskrifter. Den tidigare 3DJake-baseline på 559 kr är ersatt och ska inte längre användas som köporder.

## Blockerade / ej aktiva sourcingvägar

### eBay / HKGY01 T8×8-muttrar — CANCELLATION PENDING / OUT OF STOCK 2026-09-05

- ordern gällde 2 × flänsad T8×8-mässingsmutter, vald variant `T8 × 8 mm`, 2-pack
- faktiskt debiterat: **67 kr**
- säljaren kontaktade köparen och uppgav **out of stock** samt bad köparen annullera
- annulleringsbegäran skickades 2026-09-05; eBay visar **`The cancellation is pending`**
- ersättningsköpet är nu gjort via Amazon.se/euroharry
- återbetalningen bokförs först när den faktiskt är verifierad

### StepperOnline direkt / eBay 5-pack — INACTIVE 2026-09-03

- StepperOnline-direktens tidigare Germany 5-pack såg först attraktivt ut vid **38,13 €**, men svensk checkout lade på cirka **20 € frakt**.
- Flera eBay-listningar med exakt 5-pack visade sig vara **out of stock** eller inte leverera till Sverige.
- Amazon.se löste i stället exakt `17HS19-2004S1` 5-pack för **608,37 kr med Prime/fri frakt**. Ingen fortsatt motorsourcing behövs.

### VEVOR `0700C` router — BLACKLISTED 2026-09-03

- användarens live VEVOR-sida visar produkten som **discontinued**; de indexerade produktsidor som fortfarande gick att hitta var stale och ska inte användas som lagerbevis.
- dessutom finns en officiell UK Product Safety Report för **VEVOR Electric Router model `0700C`, 110/220V 50/60Hz 800W Class II** där risknivån anges som **Serious** för electric shock.
- rapporten beskriver underkänd electrical strength, otillräcklig insulation och bristande build quality; den berörda importen avvisades och förstördes.
- därför: **köp inte VEVOR 0700C**, inte heller restlager/begagnat enbart för att priset är lågt.
- KATSU `101750` är nu köpt ersättare.

### VEVOR NEMA17 59 Ncm 5-pack — INACTIVE 2026-09-03

- tekniskt såg databladet korrekt ut: ritningen visade Ø5 mm D-axel (4,5 mm var flatmåttet), men användarens live-sida visar motorpaketet som **discontinued**.
- gamla indexerade VEVOR-sidor ska inte behandlas som köpbara.

### DMW Industrietechnik — INACTIVE / REPLACED

DMW/eBay.de hade tekniskt korrekt `Synchronriemenscheibe / 10mm / 5mm / Z 16`, men bara två exemplar visade sig finnas kvar när köpet skulle göras. Spåret ersattes av POWGE/eBay-köpet med ett färdigt trepack.

### Roboter-Bausatz — BLOCKED 2026-09-03

Butikens fraktsida publicerade Sverige/14,99 €, men faktisk checkout saknade Sverige i landlistan. Amazon Pay accepterade svensk adress, men handlarens checkout svarade **"Leveranser till den valda leveransadressen är inte möjliga."**

### Allegro / `4Makers_pl` + `ABC-RC_pl` — BLOCKED 2026-09-03

Allegro-korgen kunde visa varor och beräknad frakt, men efter inloggning och faktisk svensk leveransadress gick varken `4Makers_pl` eller `ABC-RC_pl` att leverera till Sverige. **Korg-/plattformfrakt är inte leveransbevis.**

### HomeDIYer — INACTIVE

Tekniskt korrekt 16T-variant identifierades, men den behövs inte efter POWGE/eBay-köpet.

### 3DJake PLA — INACTIVE / REPLACED 2026-09-06

Den tidigare baslinjen var 3 × eSUN PLA Basic Black för 559 kr landat. Den är ersatt av faktiskt PrintOnion-köp: 3 kg PLA för 426 kr.

## Lokalt / separat

### Motonet — rör

- 2 × `88-7123`, Ø30×1,5×2000 mm.
- köp **inte blint online**: fysisk OD/rakhet är en gate.
- kapa först efter kontroll: 1505 / 816 / 816 mm.

### NVR/maskinstopp

Enkel aktiv kandidat: Clas Ohlson art. `50-2929`, **KJD12 230 V / 10 A, 299 kr**.

Köp först när terminalschema/mått är tillräckliga för den planerade kapslingen.

### Biltema/elbox

Kapsling, donor 3G1,5 och lokal elsmåvara först efter fysisk dry-fit av NVR + HDR. Köp inte boxstorlek på skrivbordsmått.

## Uppskjutet

### Sorotec-fräsar

`L1S.M.0317` är fortsatt tekniskt bra commissioning-fräs, men separat order är **DEFER**. Köp när första fräsjobbet närmar sig och kombinera med de fräsar som då faktiskt behövs.

## Orderarkitektur nu

Inga fler huvudorder för kärnmekanik/elektronik/prints är öppna.

Kvar att anskaffa eller ordna:
1. **2 × Motonet-rör** efter fysisk kontroll.
2. **Styvt bord + deck/spoilboard**.
3. **Material till permanenta struts**.
4. **NVR + kapsling/elmaterial** efter fysisk dry-fit.
5. **Commissioning-fräs** när första skär närmar sig.
6. **Dammbehållare/slangupphängning** när maskinen byggs.

Motorer, router, controller, PSU, endstops, lager, GT2-delar, T8-skruv, kopplingar, Z-muttrar och 3 kg PLA är köpta/beställda.

## Checkout-gates

1. Motonet-rör — fysisk Ø30 mm/rakhetskontroll före köp/kapning.
2. KATSU vid leverans — provpassa Elaire 1/8"-collet och kontrollera runout.
3. Stepperkablar — dry-fit innan eventuella extensioner köps.
4. NVR/kapsling — fysisk/layoutmässig dry-fit innan boxstorlek och kabelrutter låses.

Sourcingdata från användarens live checkout/skärmbild vinner över gamla indexerade webbsidor.
