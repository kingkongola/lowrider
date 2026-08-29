# Procurement optimization

Syfte: optimera **hela bygget**, inte varje komponent isolerat.

Målet är lägsta vettiga totalkostnad inklusive:
- artikelpris
- frakt / packavgifter
- moms / import
- antal separata beställningar
- leveranstid
- variant- och kvalitetsrisk
- sannolikheten att delen måste köpas om

Ett par kronor billigare komponent är ointressant om den skapar en extra frakt, fel variant eller osäker kompatibilitet.

**Den här filen är den kanoniska orderöversikten.** Daterade filer i `research/` innehåller evidens och historiska alternativ. Om äldre research nämner t.ex. GST60 som favorit eller ofryst geometri är det supersederat av senare beslut nedan.

## Låsta LR4-krav

Maskingeometri:
- användbart område: **650 × 1250 mm**
- rör: **816 / 816 / 1505 mm**
- strut: **819 mm**
- GT2: **999 / 1705 / 1705 mm**, totalt **4409 mm**
- minimum bord: **941 × 1563 mm**
- praktisk CNC-deck: cirka **1000 × 1620 mm**

Maskinhårdvara:
- 5 × NEMA17, ungefär 84 oz-in-klassen
- 3 × GT2 16T, 10 mm rem, 5 mm hål
- 6 × GT2 smooth idlers, 10 mm rem, 5 mm hål
- 10 mm GT2-rem med glasfiber/icke-stålkord
- 5 installerade Omron `SS-3GL13PT` endstops, NC
- 14 × 608-2RS, 8×22×7 mm
- 2 × Tr8×8/T8, 4-start, 2 mm pitch, 8 mm/rev
- 2 × 5→8 mm koppling
- 24 V / 60 W PSU-klassen

## Redan klar

### HaWiWe — BETALD

**165,50 € inklusive 8,00 € frakt.**

Täcker:
- aluminium XZ-plattor, 6,0 mm
- 4 × MGN12H 150 mm rails
- LR4 screw set
- Elaire/Makita-style 1/8" collet

Ska inte sourcas igen.

## Aktuell ordergraf

### 1. Motonet — lokalt, nära purchase-ready

- 2 × `88-7123`
- rundrör Ø30×1,5 mm × 2 m
- observerat **189 kr/st = 378 kr**

Fysisk acceptans före köp:
- mät faktisk OD
- kontrollera rakhet/bucklor

Kapplan:
- 1505 mm
- 816 + 816 mm

Research: `research/2026-08-29-steel-tubes-gavle.md`

### 2. LaskaKit — checkout-ready mekanik + lågspänningskabel

Planerad kärnkorg:
- 6 × `LA190008E` smooth GT2 idlers
- 1 × `LA190032A` T8×8 400 mm rod
- 2 × `LA190033A` T8×8 brass nuts
- 2 × `LA190031` 5→8 mm couplers
- helst 1 × `LA190013C` 5 m / 10 mm fiberglass GT2 belt
- fallback 3 × `LA190013B` 2 m om 5 m är slut
- 10 m `LA150151A` 26 AWG 3-core endstop cable
- ~1 m UL2464 20 AWG, **välj uttryckligen 2-core** till 24 V PSU→Jackpot
- board-side 2-pin connectors/pigtails enligt om lämplig DuPont-crimper redan finns

Senast beräknad levererad korg ungefär **€49–55**, beroende på kabelkontaktväg och 5 m-remmens lager.

Research:
- `research/2026-08-29-laskakit-final-mechanical-cart.md`
- `research/2026-08-29-final-psu-endstop-wiring-cart.md`

### 3. StepperOnline Germany — motors only

- 1 × fempack `5-17HS19-2004S1`
- 59 Ncm / 83,55 oz-in / 2 A
- 5 mm D-axel, 24 mm axel
- 1 m kabel
- observerat **€38,13**
- **Germany warehouse** ska vara valt

Köp inga China-only PSU/kopplingar bara för att butiksnamnet är samma.

Återstår: faktisk Germany→Sweden checkout-frakt.

Research: `research/2026-08-29-stepperonline-motor-order-live.md`

### 4. DigiKey — HDR + exact Omron

- 1 × Mean Well `HDR-60-24`, DigiKey `1866-2249-ND`
- 10 × Omron `SS-3GL13PT`, DigiKey `SW768-ND`

5 endstops installeras; 5 hålls som reserv.

Senast beräknad levererad korg: **~495 kr** inklusive 170 kr small-order-frakt.

Detta är den aktuella PSU-riktningen och **supersederar tidigare GST60A24-P1J-plan**.

Research: `research/2026-08-29-final-psu-endstop-wiring-cart.md`

### 5. VEVOR EU — purchase-ready router

Exakt modell:
- **VEVOR 0700C**
- SKU `YXKXBJ710W65AH7WLV2`
- product ID `010235793217`
- 800 W
- 65 mm
- 10 000–30 000 rpm

Observerat pris: **€83,99**.

Efter ankomst:
- provpassa redan köpt Elaire-hylsa
- kontrollera collet seat/runout innan riktig fräsning

Research: `research/2026-08-29-vevor-0700c-router.md`

### 6. Elecrow — Jackpot3

- Jackpot3
- SKU `CQA240812C2`
- observerat **US$76,99**

Återstår i checkout:
- Sverige-frakt
- VAT/IOSS/importbehandling
- total landad kostnad

Elecrow-kort antas behöva flashning/configuration.

Jackpot2 ska inte återöppnas som standardalternativ; PWM-begränsningen är en onödig framtida låsning.

Research: `research/2026-08-29-jackpot3-order.md`

### 7. SUNLU — PLA

Nuvarande Pareto-default:
- ordinary PLA
- 6 × 1 kg normala spolar
- Mix & Match bulk
- observerad 6-rollsnivå från **€9,19/kg**, cirka **€55,14** för 6 kg

Checkout-gate:
- ordinary PLA, inte fel materialvariant
- Sverige/EU
- bulkpris faktiskt applicerat
- frakt fortfarande låg/fri

Research: `research/2026-08-29-pla-bulk.md`

### 8. Sorotec — commissioning cutters

- 3 × `L1S.M.0317`
- 3,175 mm single-flute upcut
- 9 mm cutting length
- observerat **€3,70/st**
- senast beräknat **~€19,40 levererat**

Ingen lång plywoodfräs nu. Köp den först när ett verkligt 18–19 mm genomskärningsjobb finns.

Ingen clamp/T-track-korg för commissioning; börja med skruv/sacrificial tabs i MDF-spoilboard.

Research: `research/2026-08-29-first-cutters-workholding.md`

## Små orphan-delar — live checkout, inte mer arkitekturresearch

### 3 × GT2 16T / 5 mm / 10 mm

Preferred exact Allegro:
- `GT2-16T-5B_10mm_K`
- 7,20 PLN/st observerat 2026-08-29
- två stoppskruvar
- aktuell listing fortfarande live

**Köpgräns:** 3 st <=150–180 kr levererat till Sverige.

Om internationell frakt förstör dealen: verifiera exact AliExpress Choice 5-pack eller annan exact EU-listing. Variant måste uttryckligen vara 16T / 5 mm / 10 mm.

### 608-2RS

Behov:
- 14 installerade
- exact 8×22×7 mm, double rubber seal

Preferred format är 20-pack <=200 kr levererat.

Aktuell svensk fallback 2026-08-29:
- Tradera `Motion_And_Rotaion`
- exact 8-pack
- 79 kr + 39 kr visad frakt
- två pack = 16 lager
- om samfrakt i checkout blir en enda 39-kronorsfrakt: **197 kr totalt**

Det är en bra köpväg om combined checkout faktiskt visar <=200 kr. Anta inte samfrakten utan att se totalen.

Research: `research/2026-08-29-16t-bearings-orphan-cart.md`

## NVR / 230 V maskinmatning

Principen är låst:

`vägg -> KJD12 -> [HDR-60-24 + DeWalt AUTO]`

`VEVOR -> DeWaltens verktygsuttag`

Preferred:
- genuin **KEDU KJD12**
- DPST/2-polig
- NVR/no-restart
- emergency-stop cover
- köp om <=500 kr levererat

Svensk fallback:
- IKH `XW026-1`, ungefär 482 kr levererat i tidigare research, men tillverkaren är inte uttryckligen KEDU på sidan

Kapsling:
- Biltema `35-0065`, 4 DIN modules, IP65, 120×160×90 mm, 99,90 kr
- fysisk KJD12 + HDR dry-fit innan håltagning
- fallback `35-0067` om för trångt

Research:
- `research/2026-08-29-final-nvr-estop.md`
- `research/2026-08-29-mains-enclosure-distribution.md`

## Bord / underrede

Arkitektur är låst, fysisk bas är opportunistisk:
- stabilt begagnat 180×90 eller 180×100 först
- helst <=700 kr
- befintlig top behålls
- avtagbar ~1000×1620 OSB/ply CNC-deck ovanpå
- separat ~12 mm MDF-spoilboard

Nuvarande live-pass har en verifierad 700-kronors Gävle-lead men mått/underrede är ännu inte verifierade. Två tidigare nämnda leads kunde inte återverifieras och ska inte behandlas som aktuella.

Research:
- `TABLE.md`
- `research/2026-08-29-table-base-local-sourcing.md`
- `research/2026-08-29-table-live-candidates.md`

## Damm — bygg mer än köp

Ägt:
- DeWalt wet/dry shop-vac
- TPU
- 3D-printer
- gammalt FTX-aggregat för eventuell sekundär luftbehandling

Plan:
- printa LR4 dust shoe
- printa cyclone
- använd separat styv 15–30 l uppsamlingsbehållare
- testa befintlig 48 mm ×2,1 m DeWalt-slang först
- printa uppmätta adaptrar
- bygg slangupphängning/dragavlastning

Köp inte ny vakuum/slang innan den ägda lösningen är testad.

## Order-placement sequence

Det här är **lager-/variant-riskordning**, inte teknisk byggordning:

1. Motonet tubes — fysisk kontroll lokalt
2. LaskaKit — lower-stock T8/belt components
3. StepperOnline motors — Germany warehouse
4. DigiKey HDR + Omron
5. VEVOR router
6. Jackpot3 Elecrow
7. SUNLU PLA när checkout håller ungefär €55–60 / ~100–110 kr/kg
8. Sorotec 3× commissioning cutters
9. orphan 16T + 608 under ovanstående trösklar
10. KJD12 + Biltema-kapsling efter fysisk switchvariant/dry-fit
11. bord/deck/spoilboard när ett faktiskt begagnat underrede är valt

## Vad som återstår som research

Broad alternativresearch är i princip klar.

Återstående arbete är främst:
- live checkout-totaler
- variantkontroll
- lager/warehouse precis före order
- aktuellt begagnat bord
- fysisk kontroll av rör och senare bord

Öppna inte äldre komponentval igen utan att ett konkret pris-, lager- eller kompatibilitetsproblem uppstår.

Aktuell konsoliderad status finns även i:
- `research/2026-08-29-purchase-ready-order-graph.md`
- `research/2026-08-29-procurement-gap-audit.md`
