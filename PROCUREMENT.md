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
- Amazon Prime finns; Amazon-köp behöver därför **inte** samordnas för fraktens skull

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

**Remkontroll 2026-08-30:** RBS12747 är uttryckligen `Meterware`; produktsidan säger att priset gäller 1 m och att fler meter beställs genom högre antal. Specen är GT2 / 2 mm / 10 mm / gummi med glasfiberkärna. Detta är rätt typ. Vid order: 5 st = 5 löpmeter; om checkout/orderbekräftelse mot förmodan visar kapade enmetersbitar, stoppa ordern.

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

**Frakt verifierad 2026-08-30:** DigiKey anger fri leverans till Sverige vid **≥615 kr i SEK** och 170 kr under gränsen. Marketplace-produkter räknas inte in. Vår korg ligger klart över 615 kr och använder den vanliga `A27824-ND`, inte Marketplace-dubbletten. Baseline är därför **0 kr DigiKey-frakt**, under förutsättning att checkout inte flaggar någon rad som Marketplace/separat leverans.

### 3. StepperOnline Germany — motorer

- 1 × fempack `5-17HS19-2004S1`
- aktuell artikelkostnad cirka **€41 / $41,90 beroende på storefront/valuta**
- 59 Ncm / 2 A
- 5 mm D-axel / 24 mm axel
- 1 m kabel
- fempacket väger ca **2,1 kg**
- Germany warehouse stöder uttryckligen leverans till **Sverige**

StepperOnline rekommenderar lokalt EU-lager för EU och deras aktuella hjälpsida listar Sverige bland länder som tyska lagret levererar till. Exakt fraktpris publiceras däremot inte statiskt utan kräver adress/postnummer i cart/checkout. Detta är nu ett **rent prisfält att läsa av i checkout**, inte något mer research kan lösa säkert.

### 4. Elecrow — Jackpot3

- exact `CQA240812C2`
- aktuell artikelkostnad **$76,99**
- in stock
- produktvikt **300 g**
- unik vald controller
- kräver V1E FluidNC + LR4-config

Elecrow anger att frakt beräknas i cart/checkout. Deras publicerade policy säger också att importskatter/avgifter inte ingår och betalas av mottagaren. För 300 g finns air-mail som möjlig fraktklass, men faktisk Sverige-frakt måste läsas i cart. Därför är **Elecrow den största kvarvarande landad-kostnad-osäkerheten**.

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
- tack vare Prime finns **ingen samköpsbonus** med NVR eller andra Amazon-varor; optimera varje Amazon-rad separat

Webbsökningen visar exempelvis ordinary PLA runt 170–180 kr/kg på Amazon.se, men Amazon-priser är dynamiska. Välj vid köp efter aktuellt Prime-pris; 3 kg är behovet, inte 6 kg.

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

Välj billigaste dokumenterade lämpliga variant. Prime gör att NVR-valet inte behöver påverkas av andra Amazon-köp.

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
6. Amazon/Prime — 3 kg PLA

**NVR:** lokal/Amazon, optimeras separat eftersom Prime eliminerar behovet av samköp.

**Sorotec:** uppskjuten.

= **6 huvudbeställningar**, plus lokala/Prime-småköp som inte behöver orderkonsolideras.

## Kvar efter webbresearch 2026-08-30

**Verifierat nog för köp utan mer research:**
- Roboter-Bausatz: spec + meterware-rem + publicerad Sverige-frakt
- DigiKey: spec + korg över verifierad 615 kr fri-fraktgräns
- StepperOnline: exakt motor/fempack + tyska lagret levererar till Sverige
- Elecrow: exakt Jackpot3, pris/lager/vikt
- Amazon PLA: 3 kg är rätt kvantitet; välj aktuellt Prime-pris

**Kan endast avgöras i faktisk checkout:**
1. StepperOnline Germany → exakt Sverige-frakt för ~2,1 kg
2. Elecrow Jackpot3 → exakt Sverige-frakt; därefter lägg på svensk importmoms/ev. transportörsavgift enligt faktisk fraktmetod
3. Roboter-Bausatz → sista orderbekräftelsen att qty 5 meterware hanteras som sammanhängande längd
4. DigiKey → kontrollera att checkout verkligen visar 0 kr frakt och ingen Marketplace-rad

Det finns inget värde i att gissa dessa checkoutfält. Nästa steg är att öppna respektive kundvagn och läsa de faktiska totalsummorna innan betalning.