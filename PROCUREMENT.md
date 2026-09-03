# Procurement — canonical order matrix

**Live snapshot: 2026-09-03.** Syfte: minimera total landad kostnad utan att ändra låsta specs. Lager/priser är flyktiga; faktisk checkout vinner alltid över denna snapshot.

## Redan betalt

### HaWiWe — CLOSED / SHIPPED
**165,50 € inklusive 8,00 € frakt.**

6,0 mm XZ-plattor + 4 × MGN12H 150 mm + LR4 screw set + Makita/Elaire 1/8" collet.

## Beställ nu

### 1. Roboter-Bausatz — mekanik

Köp exakt:

| Rad | Antal | Pris 2026-09-03 | Delsumma |
|---|---:|---:|---:|
| `RBS12910` smooth idler 5 mm / 10 mm belt | 6 | 1,34 € | 8,04 € |
| `RBS12872` T8×8 400 mm + brass nut | 1 | 9,95 € | 9,95 € |
| `RBS12749` extra brass nut | 1 | 1,67 € | 1,67 € |
| `RBS10595` flexible coupler 5→8 mm | 2 | 1,75 € | 3,50 € |
| `RBS12747` GT2 10 mm fiberglass meterware | 5 m | 2,25 €/m | 11,25 € |
| `RBS12867` GT2 16T / 5 mm / 10 mm | 3 | 1,04 € | 3,12 € |

**Varor: 37,53 €. Sverige-frakt: 14,99 €. Snapshot total: 52,52 € inklusive tysk moms.**

Alla sex artikeltyper visas som omedelbart tillgängliga. `RBS12747` är meterware; qty 5 ska motsvara 5 m. Kontrollera orderbekräftelsen och stoppa endast om den uttryckligen skulle visa fem separata 1 m-bitar.

Detta ersätter LaskaKit + separat Allegro helt.

### 2. DigiKey — elektronik + lager + kablage

Köp exakt:
- 1 × Mean Well `HDR-60-24` / `1866-2249-ND`
- 10 × Omron `SS-3GL13PT` / `SW768-ND`
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
- `A27824-ND` är den vanliga lagerartikeln; använd inte Marketplace-dubbletten.
- full korg passerar DigiKeys svenska fri-fraktgräns **615 kr**; under gränsen kostar frakt 170 kr.

Exakt full korgsumma ska läsas i DigiKey-korgen eftersom flera mängdrabatter och kabelpriser är dynamiska. **Ingen filler. Ingen Marketplace-rad.** Välj förbetald UPS/FedEx om checkout erbjuder det och DDP-villkoret visas; DigiKey anger DDP för förbetald UPS/FedEx och CPT för DHL.

### 3. StepperOnline Germany — motorer

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

### 4. Elecrow — controller

Köp:
- 1 × **Jackpot3 CNC Controller `CQA240812C2`**

Snapshot:
- **$76,99**
- **In stock**
- 300 g
- säljs av V1 Engineering via Elecrow

Elecrow räknar frakt i cart/checkout. Deras policy säger att importskatt/tull inte ingår i frakten. Kontrollera därför **landat estimat** innan betalning.

Fallback-regel: om V1E Jackpot2 faktiskt kan checkas ut och landar klart billigare utan väntan får Jackpot2 ersätta denna rad. Annars köp Elecrow Jackpot3 och gå vidare.

### 5. VEVOR — router

Köp exakt:
- `0700C`
- SKU `YXKXBJ710W65AH7WLV2`
- product ID `010235793217`
- 220–240 V / 50 Hz
- 800 W
- 65 mm kropp

VEVOR DE snapshot: **63,99 €**, köpbar 2026-09-03.

Efter leverans: provpassa den redan köpta Elaire/Makita-style 1/8"-hylsan och kontrollera runout före riktig fräsning.

### 6. PLA — 3 kg, butik inte låst

Behovet är cirka 2,7 kg. Köp **3 × 1 kg vanlig styv PLA** eller motsvarande 3 kg, inte 6 kg.

Regel:
- Amazon Prime får gärna vinna om levererat pris är lägst.
- SUNLU är inte låst; deras 3 kg-/bulkvarianter visar varierande lagerstatus just nu.
- undvik silk/flex/wood-filled och andra special-PLA till maskindelarna.
- välj välrecenserad ordinary PLA som P1S kör stabilt.

Den här raden ska prissättas samma dag som ordern läggs; dynamiska Amazon/SUNLU-priser ska inte hårdkodas som projektfakta.

## Lokalt / separat

### Motonet — rör

- 2 × `88-7123`, Ø30×1,5×2000 mm.
- köp **inte blint online**: fysisk OD/rakhet är en gate.
- kapa först efter kontroll: 1505 / 816 / 816 mm.

### NVR/maskinstopp

Enkel aktiv kandidat: Clas Ohlson art. `50-2929`, **KJD12 230 V / 10 A, 299 kr**.

Köp först när terminalschema/mått är tillräckliga för den planerade kapslingen. Exakt KEDU/KJD12-14-proveniens är inte krav.

### Biltema/elbox

Kapsling, donor 3G1,5 och lokal elsmåvara först efter fysisk dry-fit av NVR + HDR. Köp inte boxstorlek på skrivbordsmått.

## Uppskjutet

### Sorotec-fräsar

`L1S.M.0317` är fortsatt tekniskt bra commissioning-fräs, men separat order är **DEFER**. Köp när första fräsjobbet närmar sig och kombinera med de fräsar som då faktiskt behövs.

## Orderantal nu

Huvudorder:
1. Roboter-Bausatz
2. DigiKey
3. StepperOnline Germany
4. Elecrow
5. VEVOR
6. PLA via aktuell billigaste Sverige/Prime/EU-väg

Plus fysisk Motonet-rörkontroll och senare lokala el/bordsmaterial.

## Checkout-gates — enda kvarvarande prisosäkerheterna

1. StepperOnline Germany → Sverige-frakt.
2. Elecrow Jackpot3 → Sverige-frakt + faktisk import-/momsbehandling.
3. DigiKey → full korgsumma, 0 kr frakt, ingen Marketplace-rad.
4. PLA → samma-dag-pris.
5. Roboter-Bausatz → bekräfta qty 5 meterware; snapshot total 52,52 € bör annars hålla.

Bred sourcingresearch är avslutad. Återöppna endast om någon av dessa checkout-gates fallerar.