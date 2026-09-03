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

## Beställ nu

### 1. LaskaKit — mekanikkärna

Roboter-Bausatz är **BLOCKED** för Sverige; se `SOURCING.md`. Aktiv ersättare för fem av sex mekanikrader är LaskaKit.

Köp exakt:

| Rad | Antal | Pris-snapshot | Delsumma |
|---|---:|---:|---:|
| `LA190008E` smooth GT2 idler, 5 mm bearing, 10 mm belt | 6 | 1,86 € | 11,16 € |
| `LA190032A` T8×8 400 mm stainless rod, **utan mutter** | 1 | 8,19 € | 8,19 € |
| `LA190033A` T8×8 brass nut | 2 | 1,31 € | 2,62 € |
| `LA190031` flexible coupling 5→8 mm | 2 | 1,83 € | 3,66 € |
| `LA190013B` GT2 2 m × 10 mm fiberglass belt | 3 | 4,85 € | 14,55 € |

**Varor snapshot: 40,18 €. Publicerad GLS-frakt till Sverige: 8,93 €. Baseline före eventuell destinationsmomsjustering: 49,11 €. Checkout är facit.**

Varför 3 × 2 m rem: maskinen behöver tre segment om **999 / 1705 / 1705 mm**. Varje segment ryms på en egen 2 m-rulle och lämnar totalt cirka 1,59 m reserv. Den exakta 5 m-rullen `LA190013C` är just nu slutsåld och ska inte blockera bygget.

### 2. Allegro — 3 × exakt 16T drive pulley

LaskaKit saknar aktuell **16T / 5 mm bore / 10 mm belt**-variant. Aktiv kandidat:

- 3 × `16T W10 B5 WZ`
- GT2 / 2 mm pitch
- 16 tänder
- 5 mm axelhål
- för 10 mm rem
- cirka 11 mm tandbana
- 2 låsskruvar ingår
- aktuell listning: **8,99 PLN/st**, 19 st visade

Allegro stöder leverans till Sverige som plattform, men den exakta säljarens Sverige-frakt är **checkout-gated**. Köp endast om just denna order erbjuder Sverige och landad totalsumma är rimlig. Ändra inte spec för att slippa frakt.

### 3. DigiKey — elektronik + lager + kablage

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

### 4. StepperOnline Germany — motorer

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

### 5. VEVOR EU — router

Köp exakt:
- `0700C`
- SKU `YXKXBJ710W65AH7WLV2`
- product ID `010235793217`
- 220–240 V / 50 Hz
- 800 W
- 65 mm kropp

Exakt modell/SKU är köpbar på VEVOR:s EU-spår. Tysk storefront visade 63,99 € i dagens kontroll, men VEVOR justerar moms efter destinationsland och den svenska/EU-sidan är dynamisk. **Svensk checkout är facit.** VEVOR:s EU-fraktpolicy anger för närvarande fri frakt för normala produkter till Sverige.

Efter leverans: provpassa den redan köpta Elaire/Makita-style 1/8"-hylsan och kontrollera runout före riktig fräsning.

### 6. 3DJake Sverige — PLA

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

## Blockerad sourcingväg

### Roboter-Bausatz — BLOCKED 2026-09-03

Butikens fraktsida publicerar Sverige/14,99 €, men faktisk checkout saknar Sverige i landlistan. Amazon Pay accepterade den svenska adressen som identitet/adress men återgången till butiken gav uttryckligen **"Leveranser till den valda leveransadressen är inte möjliga."** Därmed är Roboter-Bausatz inte en användbar köpväg och ska inte provas igen utan att butiken ändrar checkouten.

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

## Orderantal nu

Kvarvarande huvudorder:
1. LaskaKit
2. Allegro 16T
3. DigiKey
4. StepperOnline Germany
5. VEVOR EU
6. 3DJake

Elecrow är redan köpt. Plus fysisk Motonet-rörkontroll och senare lokala el/bordsmaterial.

## Checkout-gates — enda kvarvarande prisosäkerheterna

1. LaskaKit → svensk checkout/destinationsmoms; publicerad GLS Sverige-frakt 8,93 €.
2. Allegro 16T → exakt Sverige-frakt för aktuell säljarlistning.
3. StepperOnline Germany → Sverige-frakt.
4. DigiKey → full korgsumma, 0 kr frakt, ingen Marketplace-rad.
5. VEVOR EU → svensk destinationsmoms/slutpris i checkout.

3DJake PLA har ett komplett offentligt landat baselinepris: **559 kr**.

Bred sourcingresearch är avslutad utom där en konkret checkout-gate fallerar.
