# Procurement — canonical order matrix

**Live snapshot: 2026-09-03.** Syfte: minimera total landad kostnad utan att ändra låsta specs. Lager/priser är flyktiga; faktisk checkout vinner alltid över denna snapshot. Faktiskt debiterade SEK-belopp bokförs i `COSTS.md`.

## Redan betalt

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

Controllerköpet är stängt. Ingen Jackpot2-fallback ska längre jämföras.

### eBay / POWGE — CLOSED / ORDERED

- säljare: **POWGE Synchronous Belts and Pulleys**
- 3 × **2GT/GT2 drive pulley, 16T, 5 mm bore, för 10 mm belt, 2 mm pitch**
- vald packvariant: **3 × 2GT pulleys**
- listningen visade **fri frakt** och **`Includes import fees`**
- listat leveransfönster vid köp: **17 sep – 7 okt 2026**
- faktiskt debiterat: **72 kr**

Den tidigare DMW-vägen behövs inte längre. eBay-spåret löste den svåraste mekanikraden billigare genom en Kina-säljare där eBay hanterade importavgifterna i köpet.

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

De två T8×8-mässingsmuttrarna var slut hos LaskaKit och köptes därför separat på eBay nedan.

### eBay / HKGY01 — CLOSED / ORDERED

Köpt 2026-09-03:
- **2 × flänsad T8×8 brass nut**
- vald variant: `T8 × 8 mm`
- 2 mm pitch / 4-start / 8 mm lead
- pack: **2 Pcs**, quantity 1
- annonsen visade **`Includes import fees`**
- listat leveransfönster: **9 okt – 9 nov 2026**
- faktiskt debiterat: **67 kr**

Detta stänger den sista lilla mekaniska orphan-raden som uppstod när LaskaKit `LA190033A` var slut.

## Beställ nu

### 1. DigiKey — elektronik + lager + kablage

Köp exakt:
- 1 × Mean Well `HDR-60-24` / `1866-2249-ND`
- 10 × Omron/Aratas `SS-3GL13PT` / `SW768-ND`
- 16 × 608-2RS / `1995-1010-ND`
- 3 × Wago `221-413`
- 2 × Altech `5309 720/SET`, M20×1.5 / 5–12 mm
- 10 × TE `3-350820-2` via **`A27824-ND`**
- 1 × Amphenol `AIO-CSM12`
- 3 m Tensility `30-00416`, Digi-Spool, 2×20 AWG
- 10 m Tensility `30-00377`, Digi-Spool, 3×26 AWG

Livefakta:
- `HDR-60-24`: 5 753 i lager; 198,93 kr ex moms / 248,66 kr inkl moms.
- `30-00416`: 26 274 m i lager; 23,96 kr/m ex moms vid 1–4 m; tre meter = 71,88 kr ex moms.
- `30-00377`: svensk DigiKey-listning visar 294 m i lager; behovet är 10 m.
- övriga låsta rader visar också tillräckligt lager i aktuell kontroll.
- `A27824-ND` är den vanliga lagerartikeln; använd inte Marketplace-dubbletten.
- full korg passerar DigiKeys svenska fri-fraktgräns **615 kr**; under gränsen kostar frakt 170 kr.

Exakt full korgsumma ska läsas i DigiKey-korgen eftersom flera mängdrabatter och lokaliserade priser är dynamiska. **Ingen filler. Ingen Marketplace-rad.** Välj förbetald UPS/FedEx om checkout erbjuder det och DDP-villkoret visas; DigiKey anger DDP för förbetald UPS/FedEx och CPT för DHL.

### 2. StepperOnline Germany — motorer

Köp:
- 1 × fempack `5-17HS19-2004S1`

Snapshot:
- **38,13 €**
- **200 i lager**
- 59 Ncm / 2 A
- 5 mm D-axel / 24 mm axel
- 1 m kabel
- brutto 2,10 kg
- välj **Germany warehouse**

Exakt Sverige-frakt visas först i checkout. Germany warehouse är EU-spåret och ska användas om checkout håller.

### 3. VEVOR EU — router

Köp exakt:
- `0700C`
- SKU `YXKXBJ710W65AH7WLV2`
- product ID `010235793217`
- 220–240 V / 50 Hz
- 800 W
- 65 mm kropp

Exakt modell/SKU är köpbar på VEVOR:s EU-spår. Tysk storefront visade 63,99 € i dagens kontroll, men VEVOR justerar moms efter destinationsland och den svenska/EU-sidan är dynamisk. **Svensk checkout är facit.** VEVOR:s EU-fraktpolicy anger för närvarande fri frakt för normala produkter till Sverige.

Efter leverans: provpassa den redan köpta Elaire/Makita-style 1/8"-hylsan och kontrollera runout före riktig fräsning.

### 4. 3DJake Sverige — PLA

Köp exakt:
- **3 × eSUN PLA Basic Black**
- 1,75 mm
- 1 kg/spole
- tillverkar-EAN `6922572210929`

Live 2026-09-03:
- **148 kr/st inklusive moms**
- **2 979 st i lager** vid aktuell kontroll
- varor: **444 kr**
- svensk standardfrakt under 1 099 kr: **115 kr**
- **landad baseline: 559 kr**
- EU-intern leverans, ingen importtull

Köp inte 6 kg; behovet är cirka 2,7 kg.

## Blockerade / ej aktiva sourcingvägar

### DMW Industrietechnik — INACTIVE / REPLACED

DMW/eBay.de hade tekniskt korrekt `Synchronriemenscheibe / 10mm / 5mm / Z 16`, men bara två exemplar visade sig finnas kvar när köpet skulle göras. Spåret ersattes av POWGE/eBay-köpet med ett färdigt trepack. Köp inte DMW-remhjul nu.

### Roboter-Bausatz — BLOCKED 2026-09-03

Butikens fraktsida publicerade Sverige/14,99 €, men faktisk checkout saknade Sverige i landlistan. Amazon Pay accepterade svensk adress, men handlarens checkout svarade **"Leveranser till den valda leveransadressen är inte möjliga."**

### Allegro / `4Makers_pl` + `ABC-RC_pl` — BLOCKED 2026-09-03

Allegro-korgen kunde visa varor och beräknad frakt, men efter inloggning och faktisk svensk leveransadress gick varken `4Makers_pl` eller `ABC-RC_pl` att leverera till Sverige. **Korg-/plattformfrakt är inte leveransbevis.** Allegro-spåret är stängt.

### HomeDIYer — INACTIVE

Tekniskt korrekt 16T-variant identifierades, men den behövs inte efter POWGE/eBay-köpet.

## Lokalt / separat

### Motonet — rör

- 2 × `88-7123`, Ø30×1,5×2000 mm.
- köp **inte blint online**: fysisk OD/rakhet är en gate.
- kapa först efter kontroll: 1505 / 816 / 816 mm.
- aktuell nätlager/pris har inte kunnat verifieras tillräckligt robust; hitta inte på ett tal.

### NVR/maskinstopp

Enkel aktiv kandidat: Clas Ohlson art. `50-2929`, **KJD12 230 V / 10 A, 299 kr**.

Köp först när terminalschema/mått är tillräckliga för den planerade kapslingen. Exakt KEDU/KJD12-14-proveniens är inte krav.

### Biltema/elbox

Kapsling, donor 3G1,5 och lokal elsmåvara först efter fysisk dry-fit av NVR + HDR. Köp inte boxstorlek på skrivbordsmått.

## Uppskjutet

### Sorotec-fräsar

`L1S.M.0317` är fortsatt tekniskt bra commissioning-fräs, men separat order är **DEFER**. Köp när första fräsjobbet närmar sig och kombinera med de fräsar som då faktiskt behövs.

## Orderarkitektur nu

Kvarvarande huvudorder:
1. DigiKey
2. StepperOnline Germany
3. VEVOR EU
4. 3DJake

Redan köpt: HaWiWe, Elecrow, eBay/POWGE-remhjulen, LaskaKit-mekanikkärnan och eBay/HKGY01 T8×8-muttrarna. Plus fysisk Motonet-rörkontroll och senare lokala el/bordsmaterial.

## Checkout-gates — kvarvarande prisosäkerheter

1. StepperOnline Germany → Sverige-frakt.
2. DigiKey → full korgsumma, 0 kr frakt, ingen Marketplace-rad.
3. VEVOR EU → svensk destinationsmoms/slutpris i checkout.

3DJake PLA har ett komplett offentligt landat baselinepris: **559 kr**.

Bred sourcingresearch är avslutad utom där en konkret checkout-gate fallerar.
