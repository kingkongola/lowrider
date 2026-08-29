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
- garagegrupp: **10 A**

## Aktuell ordergraf

### 1. Motonet — rör, lokal pickup
- 2 × `88-7123`
- Ø30×1,5 mm ×2 m
- observerat 189 kr/st
- kontrollera fysisk OD/rakhet/bucklor före betalning och kapning

### 2. LaskaKit — mekanik + lågspänning

Köp:
- 6 × `LA190008E` smooth idlers, 5 mm hål, 10 mm rem
- 1 × `LA190032A` T8×8 400 mm rod
- 2 × `LA190033A` T8×8 brass nuts
- 2 × `LA190031` 5→8 couplers
- 1 × `LA190013C` **5 m / 10 mm fiberglass GT2** — live 2026-08-30 i lager
- 10 m `LA150151A` endstop cable
- 3 m UL2464 20 AWG / ~0,52 mm² **2-core**, nominellt ~4,8 mm OD
- board-side 2-pin endstop connector/pigtail-lösning efter crimperläge

Fallback om 5 m-remmen ändrar lagerstatus: 3 × 2 m av samma 10 mm fiberglass-spec. Segmenten 999/1705/1705 mm ryms utan skarv.

T8: kapa inte stången mitt itu. V1E minimum är 145 mm; sikta praktiskt på **~150–160 mm ×2 efter fysisk assembly-check**.

24 V-kabeln går från fast HDR-box till rörlig Jackpot. UL2464 är inte bevisad continuous-flex-kabel; använd stor mjuk rörelseloop. Om verklig routing kräver snäv repetitiv böj/kabelkedja: byt kabeltyp.

### 3. StepperOnline Germany — motors only

- 1 × fempack `5-17HS19-2004S1`
- 59 Ncm / 2 A
- 5 mm D-axel / 24 mm axel
- 1 m fabrikskabel
- Germany warehouse, live i lager och Sverige stöds

Stepperextensioner köps först efter full-travel dry-fit; 2–3 kan behövas men inget ska gissas.

### 4. DigiKey — konsoliderad komponentkorg

Köp exakt:
- 1 × Mean Well `HDR-60-24` / `1866-2249-ND`
- 10 × Omron `SS-3GL13PT` / `SW768-ND`
- 16 × `608-2RS-W/CHEVRONSRI2` / `1995-1010-ND` — 14 + 2 reserv
- 3 × genuine Wago `221-413`
- 2 × Altech `5309 720/SET` — M20×1.5, 5–12 mm, nät in/ut
- 10 × TE Connectivity `3-350820-2` **via DigiKey `A27824-ND`**
- 1 × Amphenol `AIO-CSM12` — M12×1.5, 3–6.5 mm, IP68, till ~4,8 mm 24 V-kabel

**SKU-fälla:** använd inte Marketplace-listningen `5831-3-350820-2-ND` för Faston; den har MOQ 1000/separat fraktrisk. `A27824-ND` är den vanliga DigiKey-lagerartikeln.

`AIO-CSM12` löser den tidigare saknade lilla LV-förskruvningen och är en riktig behövd rad, inte filler.

Live pris-sanity 2026-08-30:
- tidigare sex rader ~494,48 kr ex moms / ~618,10 kr inkl moms
- + AIO-CSM12 → ~513,17 kr ex moms / ~641,46 kr inkl moms

DigiKey anger 615 kr fri-fraktgräns men offentliga sidan klargör inte säkert momsbasen. **Checkout avgör. Köp ingen filler.**

### 5. VEVOR EU — router

- exact `0700C`
- SKU `YXKXBJ710W65AH7WLV2`
- product ID `010235793217`
- 220–240 V / 50 Hz
- 800 W
- 65 mm body
- 10 000–30 000 rpm

VEVOR:s EU-marknadsföring återanvänder texten “6.5A motor”, men samma 6,5 A-text används på 120 V / 800 W-versionen där den matematiskt hör hemma. 0700C-manualen anger 220–240 V och 800 W men ingen 6,5 A EU-märkström. **6,5 A används därför inte som EU-current-spec.**

Med sannolik DeWalt DXV30SAPTA är sammanlagd märkteffekt ~1,91 kW = ~8,3 A real-power-ekvivalent vid 230 V. Det är inte en garanti för verklig RMS-ström/startförlopp; 10 A-gruppen belastningsprovas.

Provpassa köpt Elaire-collet och mät runout. Routerförlängning endast efter full-travel dry-fit.

### 6. Elecrow — Jackpot3

- exact `CQA240812C2`
- live $76.99, in stock
- Sverige-frakt/VAT/import checkout-gated
- kräver V1E FluidNC + LR4-config före driven rörelse

Elecrow listar board + fem 2-wire terminal plugs + sex heatsinks; microSD anges inte.

Inventera först:
- data-kapabel USB-C
- FAT32 microSD >2 GB, helst Class 4/6

Jackpot monteras i rörlig board box med fri luftväg; kablar bredvid, inte över kort/antenn. Ingen fläkt före faktiskt behov.

### 7. SUNLU — PLA

- ordinary PLA
- LR4 cirka 2,7 kg inklusive mount + board box
- bulkplan 6 × 1 kg normalspolar
- live 6-roll tier från ~€9,19/kg
- köp om Sweden checkout håller ungefär 100–110 kr/kg levererat

P1S löser byggvolymen. Före hela satsen återstår bara rätt 30 mm/65 mm-filer, slicer-preview och `Z_Stub`/`Z_Nut`-testfit.

### 8. Sorotec — commissioning cutters

- 3 × `L1S.M.0317`
- 3,175 mm dia/shank
- single flute upcut
- 9 mm cutting length
- live ~€3,70/st, tillgänglig

Rätt för commissioning + 5–6 mm struts. Lång plywoodfräs köps först inför verkligt 18–19 mm-jobb.

### 9. Allegro — GT2 16T orphan

Need 3 exact:
- `GT2-16T-5B_10mm_K`
- GT2 / 16T
- 5 mm bore
- för 10 mm belt
- dual grub screws
- live ~7,20 PLN/st

Byt säljare, inte spec, om Sverige-frakt blir dålig. LaskaKits 16T-del för 6 mm rem är fel.

### 10. KEDU KJD12-14 — NVR/maskinstopp

**Preferred exact family is now KEDU `KJD12-14`.**

KEDU-datablad verifierar:
- 18 A AC-1 / **15 A AC-3** (EN60947/TÜV)
- coil option `V3` = 230 V / 50 Hz
- 6,3×0,8 mm Faston
- IP54
- accessory `A3` = emergency-stop button + waterproof cover

CEM Elettromeccanica har live genuin KEDU med bipolar NVR + röd svamp/gul kåpa; deras eBay-annons identifierar delen som **KJD12-14**. Produktpris runt €15 direkt / ~€22 på eBay-nivå; Sverige-frakt är checkout-gated.

Köp endast om den levererade varianten faktiskt är 230 V/50 Hz KJD12-14 med rätt actuator/terminaler. Denna spec har god marginal både mot vår nominella last och 10 A-gruppen.

Terminologi: **NVR/maskinstopp**, inte påstående om att den hemmabyggda helheten är en certifierad safety-rated E-stop-krets.

### 11. Biltema — lokal elbox

- `35-0065` IP65 4-module enclosure — först efter fysisk KJD12/HDR dry-fit
- `35-0067` större fallback
- `46-3610` 3 m 3G1,5 donor extension cord — endast om verklig in+ut-rutt räcker

KJD12 ska vara direkt nåbar från normal operatörsplats.

### 12. Bord / deck / spoilboard

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

## 10 A garagegrupp — designregel

Känd grupp: **10 A**.

Före riktig fräsning:
1. bekräfta DeWalt-typskylt
2. identifiera B10/C10/etc, JFB och delade laster
3. kör DeWalt ensam
4. kör controller + DeWalt AUTO + VEVOR utan skärlast
5. prova normal fräsning utan andra stora laster på samma grupp
6. vid nuisance trip: ändra last-/kretsarkitektur, **aldrig uppsäkra utan verifiering av fasta installationen**

## Endstop-semantik

5 × Omron är home/auto-square-endstops. I V1E-standardconfig är de aktiva vid homing, inte runtime hard limits/kollisionsskydd.

## Aktuell köpstatus

**Spec klar; endast checkout/frakt kvar:**
1. LaskaKit
2. StepperOnline Germany
3. DigiKey — med `A27824-ND` + `AIO-CSM12`
4. VEVOR 0700C
5. Elecrow Jackpot3
6. SUNLU ordinary PLA
7. Sorotec cutters
8. Allegro 16T
9. CEM/eBay KEDU KJD12-14

**Fysisk kontroll istället för mer webbresearch:**
- Motonet-rör
- bord
- VEVOR/Elaire collet/runout
- DeWalt-typskylt
- full-travel kablar/slang
- 10 A-grupp under verklig last

Ändra inte specifikationer bara för att minska antal paket.