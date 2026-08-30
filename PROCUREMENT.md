# Procurement optimization

Syfte: minimera **total landad kostnad** för hela bygget, inte antal paket eller enskilda artikelpriser.

Målfunktion:
`varor + frakt + moms/import + omköpsrisk + liten olägenhetskostnad per extra order`

Låsta tekniska specs ändras inte bara för att minska paketantalet.

## Redan betalt

### HaWiWe — CLOSED
**165,50 € inklusive 8,00 € frakt**
- 6,0 mm aluminium XZ-plattor
- 4 × MGN12H 150 mm rails
- LR4 screw set
- Elaire/Makita-style 1/8" collet

Vid leverans räcker normal mottagningskontroll: transportskada + att de fyra beställda produktgrupperna finns med.

## Kända förutsättningar

- arbetsyta **650×1250 mm**
- rör **816 / 816 / 1505 mm**, Ø30×1,5 mm
- GT2 **999 / 1705 / 1705 mm = 4409 mm**
- printer **Bambu Lab P1S**
- garagegrupp **10 A**, praktiskt beprövad med svets; CNC är inte ett öppet matningsproblem
- V1E anger **ca 2,7 kg PLA** för full LR4-sats inklusive tool mount + board box

## Optimerad ordergraf

### 1. Roboter-Bausatz — samlad mekanik

Detta ersätter tidigare LaskaKit + separat rem + Allegro.

Köp:
- 6 × `RBS12910` smooth idler, 5 mm hål, för 10 mm rem
- 1 × `RBS12872` T8×8 400 mm + 1 brass nut
- 1 × `RBS12749` extra T8×8 brass nut
- 2 × `RBS10595` 5→8 mm flexible coupler
- 5 m × `RBS12747` GT2 / 2 mm / 10 mm / rubber + fiberglass
- 3 × `RBS12867` GT2 16T / 5 mm bore / för 10 mm belt

Ungefärlig merchandise ~€39–40; publicerad Sverige-frakt **€14,99**. Totalt ~€54–55 före eventuella checkoutavvikelser.

För remmen: bekräfta att 5 löpmeter levereras som en kontinuerlig längd.

T8 kapas först efter fysisk assembly-check; praktiskt mål ~150–160 mm ×2.

### 2. DigiKey — elektronik + elsmådelar + båda generiska kabelraderna

Köp exakt:
- 1 × Mean Well `HDR-60-24` / `1866-2249-ND`
- 10 × Omron `SS-3GL13PT` / `SW768-ND`
- 16 × `608-2RS-W/CHEVRONSRI2` / `1995-1010-ND`
- 3 × genuine Wago `221-413`
- 2 × Altech `5309 720/SET` M20×1.5, 5–12 mm
- 10 × TE `3-350820-2` via **`A27824-ND`**
- 1 × Amphenol `AIO-CSM12`, M12 / 3–6,5 mm / IP68
- **3 m Tensility `30-00416`**, 2×20 AWG, ca 3,99 mm OD, Digi-Spool — 24 V fast box → rörlig Jackpot
- **10 m Tensility `30-00377`**, 3×26 AWG UL2464, ca 3,99 mm OD, Digi-Spool — endstops

Kabelbeslut: DigiKey-kablarna kostar ungefär **274 kr totalt** för 3 m + 10 m med aktuella meterpriser. De är dyrare per meter än LaskaKit, men billigare för hela systemet eftersom de inte skapar en separat €8,93-order. Därför tas LaskaKit bort helt ur baseline.

`30-00416` är flexibel flertrådig PVC-kabel men inte uttryckligen continuous-flex/drag-chain. Samma fysiska regel kvarstår: stor mjuk rörelseloop; byt endast om slutlig routing kräver snäv repetitiv böj.

SKU-fälla: använd inte Marketplace-dubbletten `5831-3-350820-2-ND`.

Tidigare korg utan kablar ~641 kr inkl moms. Med kablarna blir korgen klart över DigiKeys publicerade fri-fraktgräns **615 kr**; checkout är fortfarande slutlig auktoritet.

### 3. StepperOnline Germany — motorer

- 1 × fempack `5-17HS19-2004S1`
- **€41,06** aktuell artikelkostnad
- 59 Ncm / 2 A
- 5 mm D-axel / 24 mm axel
- 1 m kabel
- fempacket väger ca **2,03 kg**
- Germany warehouse stöder uttryckligen leverans till Sverige

StepperOnline publicerar inte en statisk Sverige-frakt för denna korg; exakt DHL Paket(EU)-pris räknas efter valt land/lager i cart. Detta är ett **rent checkout-prisfrågetecken**, inte ett komponentfrågetecken.

### 4. Elecrow — Jackpot3

- exact `CQA240812C2`
- aktuell artikelkostnad **$76,99**
- in stock
- produktvikt **300 g**
- unik vald controller
- kräver V1E FluidNC + LR4-config

Elecrow anger att frakten beräknas i cart/checkout och att importmoms/skatter inte ingår i frakten. Därför är **landad kostnad fortfarande verkligt checkout-gated**.

Inventera data-USB-C och FAT32 microSD hemma först.

### 5. VEVOR — router

- exact `0700C`
- SKU `YXKXBJ710W65AH7WLV2`
- 220–240 V / 800 W / 65 mm

Provpassa Elaire-collet och kontrollera runout efter leverans.

### 6. PLA — Amazon/Prime först, **3 kg behovsstyrt köp**

V1E anger cirka **2,7 kg filament för en full LR4-sats inklusive tool mount + board box**.

Därför:
- **3 × 1 kg ordinary PLA är baseline-köpet**
- 3 kg lämnar cirka 300 g / ~11 % nominell marginal
- köp en fjärde rulle endast om merkostnaden är liten eller reservfilament ändå är önskat
- inget krav på SUNLU; välj billigaste välrecenserade vanliga styva PLA som fungerar bra i P1S
- Amazon.se/Prime prioriteras om levererat pris slår separat filamentbutik

Den tidigare 6 kg SUNLU-planen är **borttagen**: den optimerade fel variabel (bulkpris/kg) och gav ~3 kg onödigt lager för just detta bygge.

### 7. NVR/maskinstopp — lokal/Amazon först, **inte egen specialorder**

Reellt krav:
- 230 V NVR/no-voltage-release
- lämplig märkström för maskinen
- tydlig, lättåtkomlig stoppfunktion
- dokumenterad terminalkoppling

`KJD12-14` är en bra verifierad familj, men exakt CEM/KEDU-specialorder är inte ett projektkrav.

Aktuella enkla köpvägar inkluderar:
- Clas Ohlson KJD12 230 V / 10 A, 299 kr
- Amazon.se-resultat för KEDU KJD12-14 runt 281 kr

Om NVR och PLA båda köps via Amazon kan de samlas i samma lågfriktionsorder; det är en bonus, inte ett skäl att välja sämre komponent.

### 8. Sorotec-fräsar — **DEFER, inte order nu**

Tekniskt förstaval kvar:
- `L1S.M.0317`
- 3,175 mm solid carbide
- single-flute upcut
- 9 mm skärlängd
- €3,70/st

Ingen bra motsvarighet hittades hos Roboter-Bausatz. VEVOR:s kit är 2-flute och ersätter inte specen; Makera har rätt single-flute men skulle ändå bli separat order.

Därför: skapa **ingen Sorotec-order nu**. Beställ fräs(ar) när första fräsjobbet närmar sig och kombinera med andra verkligt uppkomna fräsbehov.

## Lokala köp — inte shipping-optimering

### Motonet
- 2 × `88-7123`, Ø30×1,5 mm ×2 m
- kontrollera OD/rakhet före köp/kapning

### Biltema / lokal el
- kapsling efter fysisk NVR/HDR dry-fit
- donor 3G1,5 endast om verklig kabelrutt motiverar det

### Bord/material
- begagnat styvt 160–180 × helst 90–100 cm
- avtagbar ~1000×1620 deck
- ~12 mm MDF spoilboard

## Nuvarande orderantal

**Beställ nu / när checkout håller:**
1. Roboter-Bausatz — mekanik
2. DigiKey — elektronik/el + 24 V- och endstopkabel
3. StepperOnline — motorer
4. Elecrow — Jackpot3
5. VEVOR — router
6. Amazon/Prime — 3 kg PLA; NVR kan eventuellt samköpas här

**NVR:** lokal/Amazon.

**Sorotec:** uppskjuten.

= fortfarande **6 huvudbeställningar**, men filamentordern är nu rätt dimensionerad och potentiellt samma Amazon-order som NVR.

## Kvar att verifiera i checkout

1. StepperOnline Germany → Sverige exakt DHL-frakt
2. Elecrow Jackpot3 → Sverige frakt + faktisk moms/importhantering
3. Roboter-Bausatz: €14,99-frakt + bekräfta 5 m rem som kontinuerlig längd
4. DigiKey: bekräfta 0 kr frakt med nya kabelrader i korgen
5. Amazon: välj 3 × 1 kg ordinary PLA efter **lägsta levererade totalpris**, inte märke; överväg samtidig NVR om rätt variant finns

Det finns nu inget starkt skäl att återöppna leverantörsstrukturen. Nästa förbättring kommer främst från checkout-priser, inte fler komponentbyten.