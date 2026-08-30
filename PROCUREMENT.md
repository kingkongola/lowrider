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

### 2. DigiKey — elektronik + elsmådelar + generiskt kablage om priset är rimligt

Köp exakt:
- 1 × Mean Well `HDR-60-24` / `1866-2249-ND`
- 10 × Omron `SS-3GL13PT` / `SW768-ND`
- 16 × `608-2RS-W/CHEVRONSRI2` / `1995-1010-ND`
- 3 × genuine Wago `221-413`
- 2 × Altech `5309 720/SET` M20×1.5, 5–12 mm
- 10 × TE `3-350820-2` via **`A27824-ND`**
- 1 × Amphenol `AIO-CSM12`, M12 / 3–6,5 mm / IP68 för ~4,8 mm 24 V-kabel
- 24 V 2-core ~0,5 mm² och endstopkabel här **endast om** priset är vettigt; annars lokalt. Dessa generiska kablar får inte skapa en separat internationell order.

SKU-fälla: använd inte Marketplace-dubbletten `5831-3-350820-2-ND`.

Nuvarande korg utan extra kabel ~641 kr inkl moms. DigiKeys publicerade fri-fraktgräns är 615 kr; checkout avgör slutligt.

### 3. StepperOnline Germany — motorer

- 1 × fempack `5-17HS19-2004S1`
- 59 Ncm / 2 A
- 5 mm D-axel / 24 mm axel
- 1 m kabel

Behåll separat så länge identiska motorer inte kan köpas materially billigare landat från annan redan använd leverantör.

### 4. Elecrow — Jackpot3

- exact `CQA240812C2`
- unik vald controller
- kräver V1E FluidNC + LR4-config

Inventera data-USB-C och FAT32 microSD hemma först.

### 5. VEVOR — router

- exact `0700C`
- SKU `YXKXBJ710W65AH7WLV2`
- 220–240 V / 800 W / 65 mm

Provpassa Elaire-collet och kontrollera runout efter leverans.

### 6. SUNLU — PLA bulk

- ordinary PLA
- ca 2,7 kg behövs för maskinen; 6 kg-köp är ekonomiskt bulkspår om Sweden-checkout håller målpriset

### 7. NVR/maskinstopp — lokal/Amazon först, **inte egen specialorder som princip**

Reellt krav:
- 230 V NVR/no-voltage-release
- lämplig märkström för maskinen
- tydlig, lättåtkomlig stoppfunktion
- dokumenterad terminalkoppling

`KJD12-14` är en bra verifierad familj, men exakt CEM/KEDU-specialorder är inte ett projektkrav.

Aktuella enkla köpvägar inkluderar:
- Clas Ohlson KJD12 230 V / 10 A, 299 kr — kontrollera fysisk actuator/terminalvariant före val
- Amazon.se-resultat för KEDU KJD12-14 runt 281 kr — checkout/Prime/variant verifieras

Välj billigaste dokumenterade, lämpliga variant. Ingen mening med dyr separat EU-frakt bara för KEDU-proveniens.

### 8. Sorotec-fräsar — **DEFER, inte order nu**

Tekniskt förstaval kvar:
- `L1S.M.0317`
- 3,175 mm solid carbide
- single-flute upcut
- 9 mm skärlängd
- €3,70/st

Ingen bra motsvarighet hittades hos Roboter-Bausatz. VEVOR:s kit är 2-flute och ersätter inte specen; Makera har rätt single-flute men skulle ändå bli separat order.

Därför: skapa **ingen Sorotec-order nu**. Beställ fräs(ar) först när första fräsjobbet närmar sig och kombinera då med eventuellt långt plywoodstål/andra faktiskt uppkomna behov. Målet är att undvika att betala internationell frakt på €11,10 merchandise i förtid.

## Lokala köp — inte shipping-optimering

### Motonet
- 2 × `88-7123`, Ø30×1,5 mm ×2 m
- kontrollera OD/rakhet före köp/kapning

### Biltema / lokal el
- kapsling efter fysisk KJD12/HDR dry-fit
- donor 3G1,5 endast om verklig kabelrutt motiverar det
- generiskt lågspänningskablage kan köpas lokalt om billigare än DigiKey

### Bord/material
- begagnat styvt 160–180 × helst 90–100 cm
- avtagbar ~1000×1620 deck
- ~12 mm MDF spoilboard

## Nuvarande orderantal

**Beställ nu / när checkout håller:**
1. Roboter-Bausatz — mekanik
2. DigiKey — elektronik/el
3. StepperOnline — motorer
4. Elecrow — Jackpot3
5. VEVOR — router
6. SUNLU — PLA

**NVR:** lokal/Amazon, bör inte kräva separat dyr internationell order.

**Sorotec:** uppskjuten tills verkligt fräsbehov; inte del av nuvarande orderbatch.

Det betyder i praktiken **6 huvudbeställningar nu**, plus lokala köp. KEDU-specialorder och Sorotec-paket är borttagna ur baseline.

## Kvar att optimera

1. slutlig landad StepperOnline-kostnad
2. kan DigiKey absorbera 24 V/endstopkabel billigare än lokalt?
3. SUNLU Sweden-checkout
4. Elecrow landad kostnad
5. Roboter-Bausatz checkout och kontinuerlig 5 m rem
6. NVR: välj billig dokumenterad svensk/Amazon-variant när fysisk kapslingslayout är känd

Ändra inte specs bara för färre paket.