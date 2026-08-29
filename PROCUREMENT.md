# Procurement optimization

Syfte: optimera **hela bygget**, inte varje komponent isolerat. `AUDIT.md` innehåller fysiska integrationsgates; daterad research är evidens/historik.

## Redan betalt

### HaWiWe — CLOSED
**165,50 € inklusive 8,00 € frakt**.

Täcker:
- 6,0 mm aluminium XZ-plattor
- 4 × MGN12H 150 mm rails
- LR4 screw set
- Elaire/Makita-style 1/8" collet

## Kända förutsättningar

- arbetsyta **650×1250 mm**
- rör **816 / 816 / 1505 mm**, Ø30×1,5 mm
- strut `819`, `front_wing_size=30`
- GT2 **999 / 1705 / 1705 mm = 4409 mm**
- minimum bord **941×1563 mm**, praktisk deck ~1000×1620
- printer: **Bambu Lab P1S 256³** — LR4-byggvolym är redan löst
- garagegrupp: **10 A**, praktiskt beprövad med svets; CNC är inte ett öppet matningsproblem

## Aktuell ordergraf

### 1. Motonet — rör, lokal pickup
- 2 × `88-7123`, Ø30×1,5 mm ×2 m
- kontrollera fysisk OD/rakhet/bucklor före betalning och kapning

### 2. LaskaKit — mekanik + lågspänning, rem exkluderad

Köp:
- 6 × `LA190008E` smooth idlers, 5 mm hål, 10 mm rem
- 1 × `LA190032A` T8×8 400 mm rod
- 2 × `LA190033A` T8×8 brass nuts
- 2 × `LA190031` 5→8 couplers
- 10 m `LA150151A` endstop cable
- 3 m UL2464 20 AWG / ~0,52 mm² **2-core**, nominellt ~4,8 mm OD
- board-side 2-pin endstop connector/pigtail-lösning efter crimperläge

**Lagerkorrigering 2026-08-30:** direkt produktsida för LaskaKit `LA190013C` 5 m / 10 mm fiberglass GT2 visar **slut**, och även deras 2 m-alternativ visas slut. Äldre kategoridata som sade lager var stale. Remmen flyttas därför till separat källa.

T8: kapa inte stången mitt itu. V1E minimum är 145 mm; sikta praktiskt på **~150–160 mm ×2 efter fysisk assembly-check**.

24 V-kabeln går från fast HDR-box till rörlig Jackpot. UL2464 är inte bevisad continuous-flex-kabel; använd stor mjuk rörelseloop. Om verklig routing kräver snäv repetitiv böj/kabelkedja: byt kabeltyp.

### 3. GT2-rem — separat källa

Exakt krav:
- GT2 / 2 mm pitch
- 10 mm bredd
- gummi/neopren
- glasfiberförstärkning, **ingen stålcord**
- minst tre kontinuerliga bitar 999 / 1705 / 1705 mm

**Förstaval live:** Roboter-Bausatz `RBS12747`:
- GT2, 2 mm
- 10 mm
- gummi + fiberglass core
- meterware/open belt
- omedelbart tillgänglig
- vid 5 m: **€2,25/m = €11,25 före frakt**

Beställ 5 löpmeter endast om checkout/butik bekräftar att meterware levereras som en kontinuerlig längd. Det räcker till 4409 mm med ~591 mm marginal.

Alternativ:
- V1E:s egen Amazon-länk, SeekLiny ASIN `B097T4DFM6`, 10 m / 10 mm / fiberglass; Sverige/Prime checkout-gated
- Technobots `6002-591`, 5 m / 10 mm fiberglass; exakt men UK gör den sekundär

### 4. StepperOnline Germany — motors only

- 1 × fempack `5-17HS19-2004S1`
- 59 Ncm / 2 A
- 5 mm D-axel / 24 mm axel
- 1 m fabrikskabel
- Germany warehouse, live i lager och Sverige stöds

Stepperextensioner köps först efter full-travel dry-fit.

### 5. DigiKey — konsoliderad komponentkorg

Köp exakt:
- 1 × Mean Well `HDR-60-24` / `1866-2249-ND`
- 10 × Omron `SS-3GL13PT` / `SW768-ND`
- 16 × `608-2RS-W/CHEVRONSRI2` / `1995-1010-ND` — 14 + 2 reserv
- 3 × genuine Wago `221-413`
- 2 × Altech `5309 720/SET` — M20×1.5, 5–12 mm, nät in/ut
- 10 × TE Connectivity `3-350820-2` **via DigiKey `A27824-ND`**
- 1 × Amphenol `AIO-CSM12` — M12×1.5, 3–6.5 mm, IP68, till ~4,8 mm 24 V-kabel

**SKU-fälla:** använd inte Marketplace-listningen `5831-3-350820-2-ND`; den har MOQ 1000/separat fraktrisk.

`AIO-CSM12` löser den tidigare saknade lilla LV-förskruvningen och är inte filler.

Live pris-sanity 2026-08-30:
- tidigare sex rader ~494,48 kr ex moms / ~618,10 kr inkl moms
- + AIO-CSM12 → ~513,17 kr ex moms / ~641,46 kr inkl moms

DigiKey anger 615 kr fri-fraktgräns men offentliga sidan klargör inte säkert momsbasen. **Checkout avgör. Köp ingen filler.**

### 6. VEVOR EU — router

- exact `0700C`
- SKU `YXKXBJ710W65AH7WLV2`
- product ID `010235793217`
- 220–240 V / 50 Hz
- 800 W
- 65 mm body
- 10 000–30 000 rpm

VEVOR:s EU-marknadsföring återanvänder texten “6.5A motor” från 120 V-versionen. 0700C-manualen anger EU-modellen 220–240 V / 800 W men ingen 6,5 A EU-märkström. 6,5 A används inte som EU-current-spec.

Provpassa köpt Elaire-collet och mät runout. Routerförlängning endast efter full-travel dry-fit.

### 7. Elecrow — Jackpot3

- exact `CQA240812C2`
- live $76.99, in stock i senaste kontroll
- Sverige-frakt/VAT/import checkout-gated
- kräver V1E FluidNC + LR4-config före driven rörelse

Elecrow listar board + fem 2-wire terminal plugs + sex heatsinks; microSD anges inte.

Inventera först data-USB-C och FAT32 microSD >2 GB, helst Class 4/6.

### 8. SUNLU — PLA

- ordinary PLA
- LR4 cirka 2,7 kg inklusive mount + board box
- bulkplan 6 × 1 kg normalspolar
- köp om Sweden checkout håller ungefär 100–110 kr/kg levererat

P1S löser byggvolymen. Kvar före full sats: rätt 30 mm/65 mm-filer, slicer-preview och `Z_Stub`/`Z_Nut`-testfit.

### 9. Sorotec — commissioning cutters

- 3 × `L1S.M.0317`
- 3,175 mm dia/shank
- single flute upcut
- 9 mm cutting length
- live ~€3,70/st i senaste kontroll

Rätt för commissioning + 5–6 mm struts. Lång plywoodfräs köps senare vid verkligt behov.

### 10. Allegro — GT2 16T orphan

Need 3 exact:
- `GT2-16T-5B_10mm_K`
- GT2 / 16T
- 5 mm bore
- för 10 mm belt
- dual grub screws
- live ~7,20 PLN/st i senaste kontroll

Byt säljare, inte spec, om Sverige-frakt blir dålig.

### 11. KEDU KJD12-14 — NVR/maskinstopp

Preferred exact family: **KEDU `KJD12-14`**.

KEDU-datablad verifierar:
- 18 A AC-1 / **15 A AC-3**
- coil option `V3` = 230 V / 50 Hz
- 6,3×0,8 mm Faston
- IP54
- accessory `A3` = emergency-stop button + waterproof cover

CEM Elettromeccanica har konkret genuin KEDU med bipolar NVR + röd svamp/gul kåpa; deras eBay-annons identifierar KJD12-14. Sverige-frakt checkout-gated.

Terminologi: **NVR/maskinstopp**, inte påstående att den hemmabyggda helheten är en certifierad safety-rated E-stop-krets.

### 12. Biltema — lokal elbox

- `35-0065` IP65 4-module enclosure — först efter fysisk KJD12/HDR dry-fit
- `35-0067` större fallback
- `46-3610` 3 m 3G1,5 donor extension cord — endast om verklig in+ut-rutt räcker

### 13. Bord / deck / spoilboard

- begagnat styvt **160–180 cm**, helst 90–100 cm djupt
- helst ≤700 kr
- avtagbar ~1000×1620 OSB/ply deck
- separat ~12 mm MDF-spoilboard
- på 90 cm bord: verkligt stöd/infästning under ~50 mm decköverhäng i rail/wheel/belt-clip-zonen

## Damm

Reuse-first:
- befintlig DeWalt — bekräfta typskylt
- 65 mm LR4 dust shoe
- printad cyclone
- separat 15–30 l behållare
- befintlig 48 mm ×2,1 m hose först
- slangavlastning
- statisk jordning/groundable hose före XPS/reguljär dammig drift

Stålbehållare är inte automatiskt vacuum-säker; färdig cyclone-can ska deformationstestas kontrollerat.

## 10 A garagegrupp

Känd 10 A-grupp fungerar praktiskt med svets; plasma har kunnat lösa säkringen. VEVOR 800 W + DeWalt + liten PSU behandlas därför **inte som ett öppet projektproblem**.

Vid första samtidiga körningen: vanlig sanity-check. Om säkringen faktiskt löser, utred då. Uppsäkra aldrig som workaround utan kontroll av fasta installationen.

## Endstop-semantik

5 × Omron är home/auto-square-endstops. I V1E-standardconfig är de aktiva vid homing, inte runtime hard limits/kollisionsskydd.

## Aktuell köpstatus

**Spec klar; endast checkout/frakt kvar:**
1. LaskaKit utan rem
2. Roboter-Bausatz 5 m `RBS12747` — jämför landad kostnad mot Amazon-ASIN
3. StepperOnline Germany
4. DigiKey — `A27824-ND` + `AIO-CSM12`
5. VEVOR 0700C
6. Elecrow Jackpot3
7. SUNLU ordinary PLA
8. Sorotec cutters
9. Allegro 16T
10. CEM/eBay KJD12-14

**Fysisk kontroll istället för mer webbresearch:**
- Motonet-rör
- bord
- VEVOR/Elaire collet/runout
- DeWalt-typskylt
- full-travel kablar/slang

Ändra inte specifikationer bara för att minska antal paket.