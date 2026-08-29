# Procurement optimization

Syfte: optimera **hela bygget**, inte varje komponent isolerat.

Målet är lägsta vettiga totalpris inklusive artikelpris, frakt, moms/import, variant-/kvalitetsrisk och risken att behöva köpa om något. Den här filen är kanonisk orderöversikt; `AUDIT.md` innehåller integrationsgates.

## Redan betalt

### HaWiWe — CLOSED
**165,50 € inklusive 8,00 € frakt**.

Täcker:
- aluminium XZ-plattor, 6,0 mm
- 4 × MGN12H 150 mm rails
- LR4 screw set
- Elaire/Makita-style 1/8" collet

## Låst geometri

- användbar yta: **650 × 1250 mm**
- rör: **816 / 816 / 1505 mm**
- strut-generatorinput: **819 mm**, `front_wing_size=30`
- GT2: **999 / 1705 / 1705 mm**, totalt **4409 mm**
- minimum bord: **941 × 1563 mm**
- praktisk CNC-deck: cirka **1000 × 1620 mm**
- rail/printdiameter: **30 mm**

## Aktuell ordergraf

### 1. Motonet — rör, lokal pickup
- 2 × `88-7123`
- Ø30×1,5 mm ×2 m
- observerat 189 kr/st = **378 kr**
- kontrollera OD/rakhet/bucklor före köp

### 2. LaskaKit — mekanik + lågspänningskabel
- 6 × `LA190008E` smooth idlers — 5 mm lagerhål, 10 mm rem
- 1 × `LA190032A` T8×8 400 mm rod, kapas till två Z-skruvar
- 2 × `LA190033A` T8×8 brass nuts
- 2 × `LA190031` 5→8 couplers
- 1 × `LA190013C` 5 m / 10 mm fiberglass GT2 belt
- 10 m `LA150151A` endstop cable
- **3 m** flexibel UL2464 20 AWG / ~0,52 mm² **2-core** PSU-output cable
- board-side endstop connector/pigtail route efter om lämplig crimper finns

**Audit correction:** tidigare ~1 m 24 V-kabel var ett falskt låst mått. HDR sitter fast på bordet medan Jackpot sitter på den rörliga beam/gantryn. Köp 3 m som billig längdmarginal men kapa/terminera först efter full-travel dry-fit. Om verklig rutt blir längre än detta ska kabelarea/spänningsfall omvärderas innan köp.

### 3. StepperOnline Germany — motors only
- 1 × fempack `5-17HS19-2004S1`
- 59 Ncm / 2 A / 5 mm D-axel / 24 mm axel / 1 m kabel
- Germany warehouse

Stepperextensioner beställs först efter fysisk kabeldragning. V1E:s standardlayout använder förlängningar från YZ_Max/Core, så 2–3 kan visa sig behövas.

### 4. DigiKey — konsoliderad fri-frakt-korg

Köp:
- 1 × Mean Well `HDR-60-24` / `1866-2249-ND`
- 10 × Omron `SS-3GL13PT` / `SW768-ND`
- 16 × `608-2RS-W/CHEVRONSRI2` / `1995-1010-ND` — exact 8×22×7 mm, 14 installeras + 2 reserv
- 3 × genuine Wago `221-413`
- 2 × Altech `5309 720/SET` — M20×1.5, IP68, för de två 3G1,5 nätpigtailsen
- 10 × TE Connectivity `3-350820-2` — fully insulated 6.35×0.8 mm female receptacle

Senast beräknad total: ungefär **622 kr inkl moms**, över DigiKeys 615 kr fri-fraktgräns.

**Ny separat liten rad:** 24 V-kabeln ut ur elboxen behöver en egen mindre kabelgenomföring/dragavlastning, vald efter uppmätt kabel-OD. Köp där den blir billigast; gissa inte M12/M16 innan kabeln finns/måttet är känt.

### 5. VEVOR EU — router
- exact **VEVOR 0700C**
- SKU `YXKXBJ710W65AH7WLV2`
- product ID `010235793217`
- 800 W / 65 mm / 10k–30k rpm
- observerat **€83,99**

Provpassa redan köpt Elaire-collet och kontrollera runout efter ankomst. Routerkabelns räckvidd över hela maskinens rörelseområde är en fysisk gate; köp ingen förlängning före dry-fit.

### 6. Elecrow — Jackpot3
- exact `CQA240812C2`
- observerat **US$76,99**
- slutlig Sverige-frakt/VAT/import checkout-gated
- Elecrow-versionen kräver flashning: använd V1E:s vid byggtillfället aktuellt testade FluidNC + rätt LR4-config före driven rörelse

### 7. SUNLU — PLA
- ordinary PLA
- LR4 kräver cirka 2,7 kg
- bulkplan: 6 × 1 kg normala spolar om checkout håller ungefär **100–110 kr/kg levererat**
- alla diameterberoende LR4-delar ska printas i **30 mm-variant**; tool mount i Makita/65 mm-variant

### 8. Sorotec — commissioning cutters
- 3 × `L1S.M.0317`
- 3,175 mm single-flute upcut
- cirka **€19,40 levererat** enligt senaste verifiering

Ingen lång plywoodfräs ännu.

### 9. GT2 16T — enda riktiga mekaniska orphan-raden

Need 3 exact:
- GT2 / 2 mm pitch
- 16T
- 5 mm bore
- för 10 mm belt

Preferred exact Allegro:
- `GT2-16T-5B_10mm_K`
- dual grub screws

Köp om Sverige-totalen är rimlig. DigiKeys 16T-del för 6 mm rem är fel och ska inte användas för att konsolidera.

### 10. KEDU KJD12 — separat maskinstopp/NVR

Mål:
- genuine **KEDU KJD12**
- 230 V / 50 Hz-variant
- 2-polig NVR/no-restart
- röd emergency-stop/stoppkåpa
- 6,3×0,8 mm Faston
- märkström som säkert täcker DeWalt + 800 W router enligt faktisk variant

**Terminologi efter audit:** detta är vår NVR/maskinstopp. Vi har inte verifierat att den valda varianten utgör en safety-rated E-stop enligt maskinsäkerhetsstandard.

Köp inte bara på modellnamnet: KJD12 finns i flera panel-/terminalvarianter. Kontrollera exakt märkning, dimensionsritning och terminalschema.

### 11. Biltema — lokal elbox-korg
- `35-0065` IP65 4-module enclosure — förstaval
- `35-0067` 12-module enclosure — fallback om riktig dry-fit blir trång
- `46-3610` 3 m jordad 3G1,5 donor extension cord — endast om den verkliga in+ut-rutten ryms inom användbar längd efter kapning

KJD12 ska monteras så stoppet är direkt nåbart från normal operatörsplats.

### 12. Bord / deck / spoilboard

Sök:
- **160–180 cm långt**
- helst 90–100 cm djupt
- stabilt/vridstyvt
- helst ≤700 kr

160×90 fungerar geometriskt. Med ~1000 mm deck på 900 mm bord blir långsidesöverhänget ~50 mm; rail/wheel/belt-clip-zonen måste därför få verkligt lokalt stöd och säker infästning enligt `TABLE.md`.

## Damm

Behåll reuse-first-planen:
- ägd DeWalt shop-vac
- printad 65 mm/Makita-kompatibel dust shoe
- printad cyclone
- separat styv 15–30 l behållare
- testa befintlig 48 mm ×2,1 m slang först
- printa adaptrar
- slangbom/dragavlastning

**Statisk gate:** stockslangen är inte dokumenterad antistatisk. Före XPS/reguljär dammig körning ska den ha avsiktlig jordledare till definierad PE-punkt med kontinuitetskontroll, eller ersättas av en groundable hose. HDR-60-24 är Class II och är inte jordpunkten.

## Småsaker / explicit inte köp

- ingen extra threadlocker; befintlig används
- stepper-extensioner först efter dry-fit
- router-förlängning först efter full-travel dry-fit
- ingen T-track/clamp-korg före verkligt behov
- ingen lång plywoodfräs före konkret jobb
- ingen extra 1/8" collet

## Fysisk checkout-gate innan kabel-/elköp låses

När bordet finns, placera temporärt:
- KJD12/HDR-box
- DeWalt/cyklon
- rörlig beam/Jackpot-position
- router
- 48 mm hose

Mät sedan verkliga kabelvägar. Det är först då 24 V-kabel, eventuell routerförlängning, donor-cordens användbara längder och kabelgenomföringarnas placering är slutligt kända.

## Nuvarande slutsats

Produktarkitekturen håller. Auditens viktigaste ändring är att **fasta och rörliga delsystem inte längre får kopplas ihop med uppskattade kabellängder**.

Kvar som verkligt checkoutarbete:
1. Allegro 16T Sverige-total
2. StepperOnline Germany→Sweden-frakt
3. LaskaKit slutlig total/lager + 3 m 2-core variant
4. Elecrow Jackpot3 landad kostnad
5. KEDU exakt variant + Sverige-frakt
6. SUNLU checkout
7. mindre LV-kabelgenomföring efter verklig kabel-OD

Ändra inte specifikationer bara för att minska antal paket.