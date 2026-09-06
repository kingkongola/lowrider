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

### Amazon.se — KATSU router — CLOSED / ORDERED

Beställt 2026-09-03:
- **KATSU `101750`**
- 220–240 V
- 710 W
- variabelt varvtal
- cirka **64,8/65 mm** motorhus, Makita RT0700-familjens formfaktor
- visat pris vid köp: **620,00 kr**
- Prime / fri frakt

### Amazon.se / euroharry — T8×8 brass nuts — CLOSED / ORDERED

Beställt 2026-09-05:
- **4 × flänsad T8-mässingsmutter**
- Ø8 mm Tr8
- **2 mm pitch / 4-start / 8 mm lead**
- visat orderpris: **101,76 kr**
- Prime

Två används i LR4 och två blir reserv.

### PrintOnion — PLA — CLOSED / ORDERED

Köpt 2026-09-06:
- **3 kg PLA, 1,75 mm**
- vanlig styv PLA för LR4-printarna
- faktiskt betalt: **426 kr**

Behovet är cirka 2,7 kg, så 3 kg täcker basbyggets utskrifter.

## Blockerade / ej aktiva sourcingvägar

### eBay / HKGY01 T8×8-muttrar — CANCELLATION PENDING / OUT OF STOCK

- tidigare order: 2 × T8×8 brass nut
- faktiskt debiterat: **67 kr**
- säljaren uppgav out of stock och bad köparen annullera
- ersättningsköpet är gjort via Amazon.se/euroharry
- återbetalningen bokförs först när den faktiskt är verifierad

### StepperOnline direkt / eBay 5-pack — INACTIVE

Amazon.se löste exakt `17HS19-2004S1` 5-pack för **608,37 kr med Prime/fri frakt**. Ingen fortsatt motorsourcing behövs.

### VEVOR `0700C` router — BLACKLISTED

Köp inte VEVOR `0700C`. KATSU `101750` är köpt ersättare.

### 3DJake PLA — INACTIVE / REPLACED

Den tidigare baslinjen var 3 × eSUN PLA Basic Black för 559 kr landat. Den är ersatt av faktiskt PrintOnion-köp: 3 kg PLA för 426 kr.

## Lokalt / separat

### Motonet — rör

- 2 × `88-7123`, Ø30×1,5×2000 mm
- köp **inte blint online**: fysisk OD/rakhet är gate
- kapa först efter kontroll: 1505 / 816 / 816 mm

### Bord / spoilboard

Ny baseline 2026-09-06:
- köp ett **styvt begagnat 180×90 cm bord**, helst ≤700 kr; 180×100 cm är jackpot
- använd den befintliga bordsskivan direkt som strukturell maskinbas
- vår minimumfootprint är 941×1563 mm, så 900 mm djup saknar bara cirka **41 mm totalt**
- lös detta med smal lokal kantbreddning/rail-support efter fysisk dry-fit
- **köp ingen full ~1000×1620 OSB/ply-deck som baseline**
- köp senare ~12 mm löstagbar MDF-spoilboard över arbetsområdet

Separat deck/torsionsbox återinförs endast om det verkliga bordet visar konkret behov p.g.a. skevhet, vek skiva eller olämplig infästning.

### Permanenta struts

- 5–6 mm MDF/hardboard, max 6,35 mm
- köp när första bootstrap-/strutfräsningen närmar sig; en mindre skiva räcker normalt

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
2. **Styvt begagnat 180×90-bord**; ingen full deck som baseline.
3. **~12 mm MDF-spoilboard** när bordet finns.
4. **Smal lokal kantbreddning/rail-support** för den cirka 41 mm totala breddbristen på 90 cm bord.
5. **Material till permanenta struts**.
6. **NVR + kapsling/elmaterial** efter fysisk dry-fit.
7. **Commissioning-fräs** när första skär närmar sig.
8. **Dammbehållare/slangupphängning** när maskinen byggs.

Motorer, router, controller, PSU, endstops, lager, GT2-delar, T8-skruv, kopplingar, Z-muttrar och 3 kg PLA är köpta/beställda.

## Checkout-gates

1. Motonet-rör — fysisk Ø30 mm/rakhetskontroll före köp/kapning.
2. Bord — rackingtest + faktisk L×D×H; 180×90 är huvudmål.
3. 90 cm bord — fysisk rail/belt-layout innan kantbreddning dimensioneras.
4. KATSU vid leverans — provpassa Elaire 1/8"-collet och kontrollera runout.
5. Stepperkablar — dry-fit innan eventuella extensioner köps.
6. NVR/kapsling — fysisk/layoutmässig dry-fit innan boxstorlek och kabelrutter låses.

Sourcingdata från användarens live checkout/skärmbild vinner över gamla indexerade webbsidor.
