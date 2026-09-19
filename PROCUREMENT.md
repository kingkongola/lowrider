# Procurement — canonical order matrix

**Live snapshot: 2026-09-19.** Syfte: minimera total landad kostnad utan att ändra låsta specs. Lager/priser är flyktiga; faktisk checkout vinner alltid över denna snapshot. Faktiskt debiterade SEK-belopp bokförs i `COSTS.md`.

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

### eBay / POWGE — CLOSED / ORDERED

- 3 × **2GT/GT2 drive pulley, 16T, 5 mm bore, för 10 mm belt, 2 mm pitch**
- faktiskt debiterat: **72 kr**
- **ej mottagna per 2026-09-19**. eBay-spårning: importklarering 11 sep, "RECEIVED BY LMC" (DEFRAA) 12 sep; väntar slutleverans. Angivet leveransfönster vid köp: 17 sep–7 okt.

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
- printa 4 temporära struts (15 % infill), bygg/driftsätt LR4 och fräs sedan egna permanenta front-/bottenplattor med maskinen. Köp material när första skäret närmar sig; strut-generator: `strut_length=819`, `front_wing_size=30`.

### NVR/maskinstopp

Aktiv kandidat: Clas Ohlson art. `50-2929`, **KJD12 230 V / 10 A, 299 kr**.
Köp först när terminalschema/mått är tillräckliga för kapslingen.

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

**Obs:** De köpta 3 × 16T-remhjulen har ännu inte levererats per 2026-09-19; följ spårningen, köp inte dubbelt.

Motorer, router, controller, PSU, endstops, lager, GT2-delar, T8-skruv, kopplingar, Z-muttrar, 3 kg PLA och rör är köpta/beställda och **samtliga hittills lagda köp är debiterade**. DigiKey-paketet, LaskaKit-paketet och Z-muttrarna är mottagna.

## Checkout-gates

1. Motonet-rör — kontrollera fysisk OD/rakhet/längd före kapning.
2. Köpt 180×100-bordsskiva — verifiera mått, underrede/styvhet och planerad maskinplacering.
3. Markera rail/belt-layout på 180×100-skivan innan infästning; någon planerad kantbreddning för 90 cm behövs inte.
4. KATSU vid leverans — provpassa Elaire 1/8"-collet och kontrollera runout.
5. Stepperkablar — dry-fit innan eventuella extensioner köps.
6. NVR/kapsling — fysisk/layoutmässig dry-fit innan boxstorlek och kabelrutter låses.
