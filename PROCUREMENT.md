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

### 1. Allegro — konsoliderad mekanik, två säljare

Roboter-Bausatz är blockerad för Sverige. LaskaKit behövs inte som separat huvudorder om båda Allegro-säljarna faktiskt erbjuder Sverige i checkout.

#### Säljare A: `4Makers_pl`

Köp exakt:

| Rad | Antal | Pris-snapshot | Delsumma |
|---|---:|---:|---:|
| smooth GT2 idler, 10 mm belt / 5 mm shaft, `KSG1020T` | 6 | 7,99 PLN | 47,94 PLN |
| GT2 10 mm fiberglass belt, 1 m listing, `GT210WS1M` | 5 m | 13,00 PLN/m | 65,00 PLN |
| GT2 drive pulley 16T / 5 mm shaft / 10 mm belt | 3 | 6,90 PLN | 20,70 PLN |
| flexible aluminium coupling 5×8 mm, `SPE5X8` | 2 | 6,25 PLN | 12,50 PLN |
| standard brass Tr8×8 nut, **4-hole**, `NAKMOS8L` | 1 | 4,29 PLN | 4,29 PLN |

**4Makers goods subtotal: 150,43 PLN.**

Remannonsen säger uttryckligen att flera köpta meter levereras som **ett sammanhängande stycke**; qty 5 ska därför ge 5 m i ett stycke. Det är idealiskt för våra segment **999 / 1705 / 1705 mm**.

Använd den vanliga 4-hålsmuttern `NAKMOS8L`, inte den avkapade 2-hålsvarianten `NAKMOS8LSC`.

#### Säljare B: `Zadar-Sklep`

Köp:
- 1 × **T8×8 400 mm, 8 mm diameter, 4-start / 8 mm lead + brass nut**
- snapshot: **29,50 PLN**
- offer/listing: `8954932033`

Viktigt: denna rad **innehåller redan en mutter**. Därför köps bara **1 extra Tr8×8-mutter** från 4Makers. Totalt blir det exakt två muttrar, inte tre.

**Allegro goods total före frakt: 179,93 PLN.**

Allegro-plattformen stöder DPD/DHL till Sverige, men varje säljare måste ha Sverige aktiverat. **Checkout för båda säljarna är därför gate.** Samma Allegro-korg betyder inte nödvändigtvis samma paket eller en enda fraktavgift.

Om båda säljarna erbjuder Sverige till rimlig total: köp och stäng mekanikkorgen. Om en av dem blockerar Sverige byter vi endast den blockerade raden/säljaren; specs ändras inte. LaskaKit är fallback, inte aktiv huvudorder.

### 2. DigiKey — elektronik + lager + kablage

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

### 4. VEVOR EU — router

Köp exakt:
- `0700C`
- SKU `YXKXBJ710W65AH7WLV2`
- product ID `010235793217`
- 220–240 V / 50 Hz
- 800 W
- 65 mm kropp

Exakt modell/SKU är köpbar på VEVOR:s EU-spår. Tysk storefront visade 63,99 € i dagens kontroll, men VEVOR justerar moms efter destinationsland och den svenska/EU-sidan är dynamisk. **Svensk checkout är facit.** VEVOR:s EU-fraktpolicy anger för närvarande fri frakt för normala produkter till Sverige.

Efter leverans: provpassa den redan köpta Elaire/Makita-style 1/8"-hylsan och kontrollera runout före riktig fräsning.

### 5. 3DJake Sverige — PLA

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

## Blockerade / fallback sourcingvägar

### Roboter-Bausatz — BLOCKED 2026-09-03

Butikens fraktsida publicerar Sverige/14,99 €, men faktisk checkout saknar Sverige i landlistan. Amazon Pay accepterade den svenska adressen som identitet/adress men återgången till butiken gav uttryckligen **"Leveranser till den valda leveransadressen är inte möjliga."** Därmed är Roboter-Bausatz inte en användbar köpväg.

### LaskaKit — FALLBACK

LaskaKit har tekniskt korrekta idlers/T8/nuts/couplers och 2 m 10 mm fiberglass-rem samt publicerad Sverige-frakt. Behåll endast som fallback om någon konkret Allegro-rad inte kan checkas ut till Sverige. Skapa inte en separat LaskaKit-order bara av gammal planvana.

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

Kvarvarande huvudplattformar:
1. Allegro — mekanik, **2 säljare / sannolikt 2 försändelser**
2. DigiKey
3. StepperOnline Germany
4. VEVOR EU
5. 3DJake

Elecrow är redan köpt. Plus fysisk Motonet-rörkontroll och senare lokala el/bordsmaterial.

Detta tar bort LaskaKit som egen huvudorder. Allegro är dock inte ärligt en enda fysisk leverans eftersom mekaniken kommer från två säljare.

## Checkout-gates — enda kvarvarande prisosäkerheterna

1. Allegro `4Makers_pl` → Sverige måste erbjudas; läs faktisk frakt och kontrollera 5 m sammanhängande rem.
2. Allegro `Zadar-Sklep` → Sverige måste erbjudas; läs faktisk frakt.
3. StepperOnline Germany → Sverige-frakt.
4. DigiKey → full korgsumma, 0 kr frakt, ingen Marketplace-rad.
5. VEVOR EU → svensk destinationsmoms/slutpris i checkout.

3DJake PLA har ett komplett offentligt landat baselinepris: **559 kr**.

Bred sourcingresearch är avslutad utom där en konkret checkout-gate fallerar.
