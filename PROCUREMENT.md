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
- 1 × `LA190032A` T8×8 400 mm rod
- 2 × `LA190033A` T8×8 brass nuts
- 2 × `LA190031` 5→8 couplers
- 1 × `LA190013C` 5 m / 10 mm fiberglass GT2 belt om i lager
- **fallback:** 3 × 2 m av samma 10 mm fiberglass GT2-spec om 5 m-rullen är slut; 999/1705/1705 mm ryms utan skarvar
- 10 m `LA150151A` endstop cable
- **3 m** flexibel UL2464 20 AWG / ~0,52 mm² **2-core** PSU-output cable
- board-side endstop connector/pigtail route efter om lämplig crimper finns

**T8 audit:** V1E kräver 145 mm eller längre. Kapa inte 400 mm-stången slentrianmässigt mitt itu till ~199 mm. Sikta praktiskt på ungefär **150–160 mm per Z-skruv**, verifierat mot verklig assembly före kapning; extra längd fungerar men ger bara mer utstick.

**24 V audit:** tidigare ~1 m var ett falskt låst mått. HDR sitter fast på bordet medan Jackpot sitter på den rörliga beam/gantryn. Köp 3 m som billig längdmarginal men kapa/terminera först efter full-travel dry-fit. Den valda 2-core UL2464-familjen är nominellt ~4,8 mm OD. 20 AWG är elektriskt rimligt för denna längd, men kabeln är inte dokumenterad som drag-chain/continuous-flex; använd stor avslappnad rörelseloop. Om verklig routing kräver snäv repetitiv böj, byt kabeltyp innan slutmontage.

### 3. StepperOnline Germany — motors only
- 1 × fempack `5-17HS19-2004S1`
- 59 Ncm / 2 A / 5 mm D-axel / 24 mm axel / 1 m kabel
- Germany warehouse

Stepperextensioner beställs först efter fysisk kabeldragning. V1E:s standardlayout använder förlängningar från YZ_Max/Core, så 2–3 kan visa sig behövas.

Fysisk kompatibilitet är god: Jackpot3 har öppna 2,54 mm motorheaders. Vid commissioning verifieras coil-pair/connector-orientering och motorriktning. Vänd aldrig motorplugg med kortet spänningssatt.

### 4. DigiKey — konsoliderad komponentkorg

Köp:
- 1 × Mean Well `HDR-60-24` / `1866-2249-ND`
- 10 × Omron `SS-3GL13PT` / `SW768-ND`
- 16 × `608-2RS-W/CHEVRONSRI2` / `1995-1010-ND` — exact 8×22×7 mm, 14 installeras + 2 reserv
- 3 × genuine Wago `221-413`
- 2 × Altech `5309 720/SET` — M20×1.5, IP68, för de två 3G1,5 nätpigtailsen
- 10 × TE Connectivity `3-350820-2` — fully insulated 6.35×0.8 mm female receptacle, 14–16 AWG

Senast beräknad merchandise-total: ungefär **622 kr inkl moms**.

**Audit correction:** DigiKey anger fri Sverige-frakt vid 615 kr och 170 kr under gränsen, men deras hjälpsida gör inte tydligt om gränsen tillämpas före eller efter moms. Behandla därför fri frakt som **checkout-gated**. Korgen är fortfarande rationell eftersom varje rad behövs; köp inte filler enbart för att jaga gränsen.

**Separat liten rad:** 24 V-kabeln ut ur elboxen behöver en egen mindre kabelgenomföring/dragavlastning. Nominell kabel-OD är ~4,8 mm, alltså passar inte M20-delens dokumenterade 5–12 mm-spann med säker marginal. Välj mindre gland efter faktisk kabel-OD.

### 5. VEVOR EU — router
- exact **VEVOR 0700C**
- SKU `YXKXBJ710W65AH7WLV2`
- product ID `010235793217`
- 800 W / 65 mm / 10k–30k rpm
- observerat **€83,99**

65 mm-kroppen matchar Makita-formatets LR4-tool mount. Provpassa redan köpt Elaire-collet och kontrollera runout efter ankomst. Routerkabelns räckvidd över hela maskinens rörelseområde är en fysisk gate; köp ingen förlängning före dry-fit.

### 6. Elecrow — Jackpot3
- exact `CQA240812C2`
- observerat **US$76,99**
- slutlig Sverige-frakt/VAT/import checkout-gated
- Elecrow-versionen kräver flashning: använd V1E:s vid byggtillfället aktuellt testade FluidNC + rätt LR4-config före driven rörelse
- Elecrow listar board + 5 tvåledarpluggkontakter + 6 självhäftande heatsinks; **microSD anges inte som inkluderat**

Commissioning-inventering före extra köp:
- **microSD:** >2 GB, FAT32, helst Class 4–6 enligt V1E; inventera först, köp endast om inget kompatibelt kort finns. Ett enkelt 4–32 GB-kort räcker.
- **USB-C:** verifiera data-kapabel kabel för flashing; charge-only fungerar inte.

Jackpot3 monteras i sin rörliga board box med fri luftväg. Kablar ska gå bredvid kortet, inte över kort/antenn, och avlastas innan de lämnar boxen. Fläkt är valfri och köps inte utan faktiskt behov.

### 7. SUNLU — PLA
- ordinary PLA
- LR4 kräver cirka 2,7 kg för full sats inklusive tool mount + board box
- bulkplan: 6 × 1 kg normala spolar om checkout håller ungefär **100–110 kr/kg levererat**
- alla diameterberoende LR4-delar ska printas i **30 mm-variant**; tool mount i Makita/65 mm-variant

**Print-gate före full sats:** skrivaren måste ha minst 200×200×190 mm tillgänglig byggvolym enligt V1E. Kontrollera skew/90° och provprinta `Z_Stub` + `Z_Nut` innan de långa printarna. Inspektera slicer-preview för interna bridges, särskilt Dust Skirt/YZ_Plate om Cura-baserad slicer används.

### 8. Sorotec — commissioning cutters
- 3 × `L1S.M.0317`
- 3,175 mm single-flute upcut
- 9 mm skärlängd
- cirka **€19,40 levererat** enligt senaste verifiering

Passar commissioning, skum/tunna material och 5–6 mm permanent strut-material. Den är medvetet för kort för 18–19 mm plywood. Ingen lång plywoodfräs ännu.

### 9. GT2 16T — enda riktiga mekaniska orphan-raden

Need 3 exact:
- GT2 / 2 mm pitch
- 16T
- 5 mm bore
- för 10 mm belt

Preferred exact Allegro:
- `GT2-16T-5B_10mm_K`
- dual grub screws

Specen matchar LR4. Köp om Sverige-totalen är rimlig. DigiKeys 16T-del för 6 mm rem är fel och ska inte användas för att konsolidera.

### 10. KEDU KJD12 — separat maskinstopp/NVR

Mål:
- genuine **KEDU KJD12**
- 230 V / 50 Hz-variant
- 2-polig NVR/no-restart
- röd emergency-stop/stoppkåpa
- 6,3×0,8 mm Faston
- märkström som säkert täcker DeWalt + 800 W router enligt faktisk variant

Nominal last om DeWalt sannolik DXV30SAPTA bekräftas: ~1050 W vac + 800 W router + max 60 W HDR ≈ **1,91 kW / 8,3 A vid 230 V**. Det ligger under den verifierade 15 A-märkningen på den aktuella genuina CEM/KEDU-kandidaten, men exakt variant och inrusningsbeteende ska fortfarande verifieras.

**Terminologi efter audit:** detta är vår NVR/maskinstopp. Vi har inte verifierat att den valda varianten utgör en safety-rated E-stop enligt maskinsäkerhetsstandard.

Köp inte bara på modellnamnet: KJD12 finns i flera panel-/terminalvarianter. Kontrollera exakt märkning, dimensionsritning och terminalschema.

### 11. Biltema — lokal elbox-korg
- `35-0065` IP65 4-module enclosure — förstaval
- `35-0067` 12-module enclosure — fallback om riktig dry-fit blir trång
- `46-3610` 3 m jordad 3G1,5 donor extension cord — endast om den verkliga in+ut-rutten ryms inom användbar längd efter kapning

M20-glands är rätt storleksklass först efter att donor-kabelns faktiska OD bekräftats. KJD12 ska monteras så stoppet är direkt nåbart från normal operatörsplats.

### 12. Bord / deck / spoilboard

Sök:
- **160–180 cm långt**
- helst 90–100 cm djupt
- stabilt/vridstyvt
- helst ≤700 kr

160×90 fungerar geometriskt. Med ~1000 mm deck på 900 mm bord blir långsidesöverhänget ~50 mm; rail/wheel/belt-clip-zonen måste därför få verkligt lokalt stöd och säker infästning enligt `TABLE.md`.

## Damm

Behåll reuse-first-planen:
- ägd DeWalt shop-vac — **modelltypskylt måste bekräftas** innan modellunika data som 2450 W tool outlet behandlas som faktum
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
- microSD och USB-C inventeras först; köp bara om de saknas
- ingen Jackpot-fläkt före verkligt behov
- ingen T-track/clamp-korg före verkligt behov
- ingen lång plywoodfräs före konkret jobb
- ingen extra 1/8" collet

## Endstop-semantik

De fem Omron-brytarna är **home/auto-square-endstops**. I V1E:s standardkonfiguration är de endast aktiva under homing och stoppar inte maskinen under vanlig G-code-körning.

De får därför inte räknas som:
- runtime hard limits
- kollisionsskydd
- nödstopp

Detta är en konfigurations-/säkerhetsfråga, inte ett skäl att köpa andra brytare.

## Fysisk checkout-gate innan kabel-/elköp låses

När bordet finns, placera temporärt:
- KJD12/HDR-box
- DeWalt/cyklon
- rörlig beam/Jackpot-position
- router
- 48 mm hose

Mät sedan verkliga kabelvägar. Det är först då 24 V-kabel, eventuell routerförlängning, donor-cordens användbara längder och kabelgenomföringarnas placering är slutligt kända.

## Nuvarande slutsats

Produktarkitekturen håller. Andra auditpasset hittade främst **commissioning-beroenden och falska antaganden mellan inköpsrader**, inte fel huvudkomponenter.

Kvar som verkligt checkoutarbete:
1. Allegro 16T Sverige-total
2. StepperOnline Germany→Sweden-frakt
3. LaskaKit slutlig total/lager + exakt 2-core variant; använd 3×2 m belt fallback om 5 m-rullen saknas
4. Elecrow Jackpot3 landad kostnad
5. KEDU exakt variant + Sverige-frakt
6. SUNLU checkout
7. mindre LV-kabelgenomföring efter verklig kabel-OD
8. DigiKey faktisk frakt i checkout

Ändra inte specifikationer bara för att minska antal paket.