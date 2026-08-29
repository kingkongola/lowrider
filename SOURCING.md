# Sourcing plan — current 2026-08-29

Mål: bra kvalitet utan dumsnålhet, låg total kostnad inklusive frakt och så få beställningar som **ekonomiskt rimligt**.

**Temporalitet:** priser/lager ska omkontrolleras före köp. Exakta evidens och historiska alternativ finns i daterade filer under `research/`. `PROCUREMENT.md` är den kanoniska order-/kundvagnsöversikten.

## Låsta val

- Maskin: **LowRider V4**
- Arbetsyta: **650 × 1250 mm**
- CNC-deck: cirka **1000 × 1620 mm**
- Controller: **Jackpot3**
- Router: **VEVOR 0700C, 800 W, 65 mm**
- PSU: **Mean Well HDR-60-24**
- Endstops: **Omron SS-3GL13PT**, köp 10/installera 5
- Motorer: StepperOnline **`5-17HS19-2004S1`** fempack
- Amazon Prime finns som möjlig fraktfördel, men butik väljs efter totalpris och rätt variant
- Laser väntar till tidigast 2027
- Plasma ingår inte i nuvarande scope
- Dammutsug är ett grundkrav

## Redan köpt och betalt — ska inte sourcas igen

HaWiWe, **165,50 € inklusive 8,00 € frakt**:
- Aluminium XZ plates, 6,0 mm
- 4 × MGN12H 150 mm linear rails
- LR4 screw set
- Elaire/Makita-style 1/8" (3,175 mm) collet

## Aktuella köpvägar

### Motonet — rör
- 2 × `88-7123`
- Ø30×1,5 mm ×2 m
- observerat 189 kr/st
- kontrollera OD/rakhet före betalning
- kapa 1505 / 816 / 816 mm

### LaskaKit — mekanik + lågspänningskablage
- 6 × `LA190008E` smooth idlers
- 1 × `LA190032A` Tr8×8 400 mm
- 2 × `LA190033A` Tr8×8 brass nuts
- 2 × `LA190031` 5→8 couplers
- 1 × `LA190013C` 5 m, 10 mm fiberglass GT2 belt om lager; annars 3 × `LA190013B`
- 10 m `LA150151A` endstop cable
- ~1 m UL2464 20 AWG **2-core** PSU-output cable
- board connectors/pigtails efter crimperläge

### StepperOnline Germany — motors only
- 1 × `5-17HS19-2004S1`
- Germany warehouse
- observerat €38,13
- checkout-frakt till Sverige återstår

### DigiKey — PSU + endstops
- 1 × Mean Well `HDR-60-24`, `1866-2249-ND`
- 10 × Omron `SS-3GL13PT`, `SW768-ND`
- senaste beräknade korg ~495 kr levererad

Detta supersederar äldre GST60/RS-spår.

### VEVOR EU — router
- exakt **0700C**
- SKU `YXKXBJ710W65AH7WLV2`
- product ID `010235793217`
- observerat €83,99
- provpassa redan köpt Elaire-collet och kontrollera runout efter ankomst

### Elecrow — Jackpot3
- `CQA240812C2`
- observerat US$76,99
- Sverige-frakt/VAT/import ska avgöras i checkout

### SUNLU — PLA
- ordinary PLA
- 6 × 1 kg normala spolar
- observerad Mix & Match-nivå från €9,19/kg
- köp endast om Sverige-checkout håller ungefär 100–110 kr/kg levererat

### Sorotec — första frässtål
- 3 × `L1S.M.0317`
- 3,175 mm single-flute upcut, 9 mm skärlängd
- senast cirka €19,40 levererat

### Orphan: GT2 16T
- 3 × exact 16T / 5 mm bore / 10 mm belt
- preferred Allegro `GT2-16T-5B_10mm_K`
- aktuellt 7,20 PLN/st
- köp om total <=150–180 kr levererat

### Orphan: 608-2RS
- exact 8×22×7 mm / 2RS
- 14 behövs
- preferred 20-pack <=200 kr levererat
- aktuell svensk fallback: två Tradera 8-pack á 79 kr; om samfrakt ger en 39-kronorsfrakt blir 16 st **197 kr levererat**
- checkout måste bekräfta totalen

### NVR / el
- genuin KEDU KJD12, 2-polig NVR/no-restart med emergency-stop cover, köp <=500 kr levererat
- IKH `XW026-1` är svensk fallback om genuin KEDU inte vinns på totalpris
- Biltema `35-0065` IP65 4-moduls kapsling förstahandsval efter fysisk dry-fit

## Bord / underrede

Huvudspår:
- begagnat styvt **180×90 eller 180×100 cm**
- helst <=700 kr
- behåll befintlig skiva
- skruva/bulta avtagbar ~1000×1620 OSB/ply CNC-deck ovanpå
- separat ~12 mm MDF-spoilboard

Aktuell live research:
- en verifierad Gävle-lead på 700 kr finns, men mått och underrede är ännu inte verifierade
- två tidigare nämnda leads kunde inte återverifieras och ska inte behandlas som aktuella

Se:
- `TABLE.md`
- `research/2026-08-29-table-live-candidates.md`

## Ska inte köpas ännu

- stepper-extensioner före dry-fit av motorernas befintliga 1 m-ledningar
- extra 1/8"-spännhylsa
- lång plywoodfräs före konkret 18–19 mm jobb
- T-track / insert-grid / vacuum-table före verkligt behov
- ny grovdammsugare eller ny slang innan befintlig DeWalt-lösning testats
- laserutrustning före 2027
- prestandauppgraderingar innan standardmaskinen fungerar

## Nästa sourcingarbete

Ingen bred komponentjakt behövs nu.

Återstår främst:
1. verifiera live checkout för 16T + 608
2. verifiera checkout-totaler på de redan valda huvudkorgarna
3. kontrollera Motonet-rören fysiskt
4. hitta/inspektera ett faktiskt 180×90/100-bord
5. uppdatera daterad research om pris/lager ändras så mycket att ett val faktiskt behöver omprövas
