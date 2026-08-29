# BOM

Här ska bara delar för den LowRider V4 som faktiskt byggs finnas. `AUDIT.md` innehåller de fysiska integrationsgates som inte får ersättas av antaganden.

## Inköpsförutsättning

- [x] Amazon Prime-medlemskap — möjlig fraktfördel, men butik väljs efter totalpris och rätt variant

## Redan köpt — HaWiWe, 29 augusti 2026

**Order betald: 165,50 € inklusive 8,00 € frakt.**

- [x] Aluminium XZ plates, **6,0 mm** — 39,50 €
- [x] 4 × MGN12H 150 mm linear rails — 57,00 €
- [x] Screw set LowRider 4 — 32,00 €
- [x] Makita/Elaire 1/8" (3,175 mm) collet — 29,00 €
- [x] Frakt — 8,00 €

### Exakt innehåll i HaWiWe screw set

- [x] 14 × M8×40 + 14 × M8 nyloc
- [x] 60 × M5×30 + 60 × M5 nyloc
- [x] 83 × M3×10
- [x] 10 × M2.5×12

Kitet innehåller inte lager, T8, T8-muttrar, kopplingar, remhjul, idlers, rem, endstops, motorer, kablage eller PSU.

## Redan ägt

- [x] DeWalt wet/dry shop-vac, mycket sannolikt DXV30SAPTA; sannolik spec 30 l / 1050 W / 15 kPa / 37,8 l/s / 48 mm ×2,1 m slang. Bekräfta typskylt före modellunika köp.
- [x] Äldre FTX-aggregat — endast kandidat för sekundär luftfiltrering/undertryck, aldrig rått CNC-spån utan primäravskiljning
- [x] TPU-filament — kontrollera hårdhet; ~95A passar V1E:s dust-shoe-bristles
- [x] Threadlocker finns redan

## Låst maskingeometri

- användbar arbetsyta: **650 × 1250 mm**
- X-rör: **816 mm ×2**
- Y-rör: **1505 mm**
- strut-generatorinput: **819 mm**
- strut `front_wing_size`: **30 mm**
- GT2: **999 + 1705 + 1705 = 4409 mm**
- minimum bord: **941 × 1563 mm**
- praktisk CNC-deck: cirka **1000 × 1620 mm**

## Kvar — mekanik

- [ ] 2 × Motonet `88-7123`, stålrör Ø30×1,5 mm ×2 m; mät OD/rakhet före kapning
- [ ] **senaste LR4-printar i 30 mm-variant** på alla diameterberoende delar
- [ ] Makita/**65 mm** tool mount för VEVOR 0700C
- [ ] cirka 2,7 kg vanlig styv PLA krävs; bulkplan 6 × 1 kg SUNLU om checkout håller
- [ ] 3 × GT2 16T / 5 mm bore / för 10 mm belt
- [ ] 6 × smooth GT2 idlers / 5 mm bearing bore / för 10 mm belt, LaskaKit `LA190008E`
- [ ] 1 × 5 m, 10 mm fiberglass GT2 belt, LaskaKit `LA190013C`; 5 m räcker till 4409 mm kalkylerat behov
- [ ] 16 × exact 608-2RS 8×22×7 mm; 14 installeras + 2 reserv
- [ ] 1 × T8×8 400 mm rod, 4-start / 2 mm pitch / 8 mm per rev; kapas till två >145 mm Z-skruvar
- [ ] 2 × matching T8×8 brass nuts
- [ ] 2 × 5→8 mm flexible couplers
- [ ] material till permanenta strut plates, 5–6 mm MDF/hardboard preferred, max 6,35 mm
- [ ] ca 18 × M4×12 eller längre trä-/plåtskruv för rail/belt-clip/table-infästning enligt verklig deck

## Kvar — motorer, styrning och lågspänning

- [ ] Jackpot3 CNC Controller — Elecrow `CQA240812C2`; kräver flashning/config
- [ ] 5 × StepperOnline `17HS19-2004S1`, 59 Ncm / 2 A / 5 mm D-axel / 24 mm axel / 1 m kabel
- [ ] stepper-extensioner endast där full-travel dry-fit visar behov; V1E-layouten gör 2–3 sannolika
- [ ] 10 × Omron `SS-3GL13PT`; 5 installeras, 5 reserv; kopplas NC via COM+NC
- [ ] 10 m LaskaKit `LA150151A`, UL2464 26 AWG 3×0,14 mm²; använd 2 ledare för endstops
- [ ] 2-poliga 2,54 mm board-side endstopkontakter/pigtails + reserv
- [ ] Mean Well `HDR-60-24`, 24 V / 2,5 A / 60 W DIN PSU
- [ ] **3 m** flexibel UL2464 20 AWG / ~0,52 mm² **2-core** för fast HDR-box → rörlig Jackpot; kapa först efter full-travel dry-fit
- [ ] **1 separat mindre kabelgenomföring/dragavlastning för 24 V-kabeln**, dimensionerad efter faktisk kabel-OD

### Fysisk kabelregel

HDR-boxen är fast på bordet medan Jackpot3 sitter på den rörliga beam/gantryn. Därför får ingen 24 V-längd, routerkabel eller stepperextension slutmonteras utifrån skrivbordsmått.

Före slutliga clips/remspänning ska maskinen manuellt kunna nå alla fyra hörn + Z-extremer med samtidigt monterade:
- 24 V-kabel
- VEVOR-routerkabel
- motor/endstopkablar
- dammsugarslang

Inget får sträckas, bära kontaktlast, kinka eller kunna falla över bordskant/rörelsezon.

## Kvar — 230 V maskinmatning

Baseline:

`vägg -> KJD12 NVR -> [HDR-60-24 + DeWalt AUTO]`

`VEVOR -> DeWaltens verktygsuttag`

- [ ] genuin **KEDU KJD12**, 230 V/50 Hz, 2-polig NVR/no-restart, röd stoppkåpa, korrekt märkström och terminalvariant
- [ ] Biltema `35-0065` IP65 4-moduls DIN-kapsling, 120×160×90 mm — **endast om riktig dry-fit ger säker terminal-/böjradie**
- [ ] Biltema `35-0067` 12-moduls kapsling — fallback om lilla boxen blir trång
- [ ] jordad 3G1,5 donor extension lead, t.ex. Biltema `46-3610`; 3 m endast om faktisk in+ut-rutt räcker
- [ ] 2 × M20×1,5 kabelgenomföring för 3G1,5 nät in/ut
- [ ] 3 × genuine Wago 221-413 för L/N/PE-fördelning
- [ ] isolerade 6,3×0,8 mm Faston som passar faktisk KJD12 och kabelarea

**Terminologi:** KJD12 är här **NVR/maskinstopp med röd stoppkåpa**. Safety-rated E-stop-status är inte verifierad. Montera den direkt nåbar från normal operatörsplats.

PE till DeWalt-uttaget ska vara kontinuerlig och oswitchad. HDR-60-24 är Class II och ska inte användas som jordpunkt.

## Router / frässtål

- [ ] VEVOR 0700C, 800 W, 65 mm body, 10 000–30 000 rpm — SKU `YXKXBJ710W65AH7WLV2`, product ID `010235793217`
- [ ] provpassa köpt Elaire/Makita-style 1/8" collet och kontrollera korrekt säte + runout före riktig fräsning
- [ ] 3 × Sorotec `L1S.M.0317`, 3,175 mm single-flute upcut, 9 mm skärlängd
- [ ] router-förlängningskabel **endast** om full-travel dry-fit visar att fabriksledningen inte räcker
- [ ] lång 3,175 mm single-flute, minst ~22–25 mm faktisk skärlängd, först inför verkligt 18–19 mm plywoodjobb

## Bord / deck / spoilboard

- [ ] styvt begagnat bord **160–180 cm långt**, helst 90–100 cm djupt, helst ≤700 kr
- [ ] avtagbar ~1000×1620 structural CNC deck, 11 mm OSB value default eller ~12 mm konstruktionsplywood
- [ ] separat löstagbar ~12 mm MDF-spoilboard över arbetszonen
- [ ] lokal blockning/list/genomgående infästning där 90 cm-bord lämnar ~50 mm decköverhäng under LR4:s rail/wheel/belt-clip-zon

Se `TABLE.md`.

## Dammhantering — del av grundbygget

- [ ] LR4 dust shoe för Makita/65 mm — printas
- [ ] V1E TPU-bristles med redan ägd TPU om ~95A
- [x] DeWalt shop-vac finns
- [ ] 3D-printad cyklonavskiljare först; kommersiell endast fallback
- [ ] styv 15–30 l uppsamlingsbehållare före DeWalt
- [ ] testa befintlig DeWalt 48 mm ×2,1 m slang först
- [ ] kort stationär cyclone→DeWalt-koppling
- [ ] slangupphängning/dragavlastning så slangen inte belastar Core/Z
- [ ] enkel avtorkningsbar avskärmning/gardin runt CNC-zonen
- [ ] **statisk jordning:** definierad PE-anslutning + kontinuitetskontroll för stockslangen, eller groundable/steel-ribbed hose; måste vara löst före XPS/reguljär trä/MDF-körning
- [ ] utvärdera FTX endast som sekundär luftfiltrering/undertryck efter modellidentifiering

## Småsaker

- [ ] lätt smörjmedel till idlers/linjärskenor
- [ ] buntband/tape/wire sleeve för kabelinfästning efter full-travel-test
- [ ] värmekrympslang för endstoplödpunkter
- [ ] ändhylsor/ferrules där de passar skruvterminalerna och rätt tång finns
- [ ] ingen T-track/clamp-order nu — skruv/tabs i spoilboard först

## Konfigurationsgate för Jackpot3

Elecrow-kortet är inte V1E-förkonfigurerat. Före driven rörelse:
- flasha V1E:s vid byggtillfället aktuellt testade FluidNC-paket
- ladda rätt LR4-konfiguration
- kontrollera motorutgångar/endstopstatus
- börja jogga 1 mm i taget

Jackpot3 ska sitta separat på den rörliga beam/YZ_Min-sidan med fri luftväg; stoppa den inte i den slutna 230 V-kapslingen.

## Valfritt senare

- [ ] touch plate / verktygslängdsgivare
- [ ] T-track / threaded-insert-grid / vacuum-table först efter faktisk användning
- [ ] laser tidigast 2027

## Fysiska gates som blockerar slutgodkännande

- [ ] Motonet-rör uppmätta/raka
- [ ] HaWiWe-delar inventerade/provmonterade
- [ ] VEVOR-collet/runout verifierad
- [ ] faktiskt bord racking- och edge-support-godkänt
- [ ] KJD12/HDR-box fysisk dry-fit godkänd
- [ ] full-travel kabel/slang-test godkänt
- [ ] statisk jordväg verifierad
- [ ] 230 V PE/L/N/dragavlastning verifierad före energisering