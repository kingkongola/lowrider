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

## Invarianta LR4-krav

Verifierat mot V1E:s aktuella LR4-hardware kit/dokumentation 2026-08-29:

- 5 × NEMA17, ungefär 84 oz-in-klassen, axel minst 20 mm
- 3 × GT2 16T drivhjul, för 10 mm rem, 5 mm motoraxel
- 6 × GT2 20T smooth idlers, 5 mm hål, för 10 mm rem
- GT2 10 mm rem, **glasfiber/icke-stålkord**, slutlig längd från LR4-kalkylatorn
- 5 × endstops
- 14 × 608-2RS, 8×22×7 mm
- 2 × T8/Tr8×8, minst 145 mm, 4-start, 2 mm pitch, 8 mm/rev + rätt mutter
- 2 × 5→8 mm koppling
- 3 × kabel-extensioner från YZ_Max/Core till controller
- 24 V PSU; 60 W / 2,5 A-klassen är en bra match

Källor:
- https://www.v1e.com/products/lowrider-v4-hardware-kit
- https://docs.v1e.com/lowrider/
- https://www.v1e.com/products/wiring-kit-1

## Kundvagnsstrategi

### Redan klar

**HaWiWe — BETALD**
- XZ-plattor
- 4 × MGN12H 150 mm rails
- LR4 screw set
- Elaire/Makita-style 1/8" collet

### Specialbeställningar som sannolikt är rationella

1. **Elecrow** — Jackpot3. Specialprodukt; svår att samfrakta vettigt med resten.
2. **VEVOR** — rätt 0700C 800 W router. Specialvariant vald för kompatibilitet med den redan köpta Makita/Elaire-hylsan.
3. **Filamentbutik** — bara om bulkpriset verkligen hamnar nära 100 kr/kg levererat.

### Viktig korrigering: StepperOnline är inte automatiskt en enda EU-korg

Färsk produktnivåkontroll 2026-08-29 visar:
- motorpaketet `5-17HS19-2004S1` erbjuder **Germany warehouse**
- Mean Well `HDR-60-24` visas däremot som **Ships from China**
- `ST-FC04` 5→8 mm flexkoppling visas också som **Ships from China**
- andra Mean Well-alternativ som kontrollerats hos StepperOnline, t.ex. `GST60A24-P1J` och `MDR-60-24`, visas också som China/CN-sale

Alltså ska vi **inte** lägga PSU och två billiga kopplingar i motorordern bara för att butiksnamnet är samma. Det riskerar extra försändelse/importhantering och förstör samfraktsvinsten.

**Nuvarande bättre arkitektur:**
- StepperOnline Germany: sannolikt **endast fempacket motorer**
- PSU: köp från Sverige/EU där totalpris och elsäkerhet blir bäst
- 5→8-kopplingar: lägg i commodity-korgen tillsammans med GT2/T8/lager/endstops om möjligt

## Motorer — verkliga alternativ

### A. StepperOnline 5-17HS19-2004S1 — förstahandsval

Pris observerat 2026-08-29: **€38,13 / 5-pack**.

Per motor:
- 17HS19-2004S1
- 59 Ncm / 83,55 oz-in
- 2,0 A
- 1,8°
- 1,6 ohm
- 3,0 mH
- 42×42×48 mm
- 5 mm D-axel
- 24 mm axellängd
- 1 m kabel

Detta träffar V1E:s 84 oz-in-klass nästan exakt och har rätt mekaniska mått.

https://www.stepperonline.nl/5st-nema-17-bipolair-59ncm-83-55oz-in-2a-42x48mm-4-draden-met-1m-kabel-aansluiting-5-17hs19-2004s1

### B. StepperOnline 5-17HE19-2004S — budgetalternativ

Pris observerat 2026-08-29: **€26,65 / 5-pack**, alltså bara €11,48 mindre för hela maskinen.

Per motor:
- 17HE19-2004S
- 55 Ncm / 77,88 oz-in
- 2,0 A
- 1,8°
- 1,3 ohm
- 2,4 mH
- 42×42×48 mm
- 5 mm D-axel
- 24 mm axellängd
- 1 m kabel

Elektriskt kan den lägre induktansen vara gynnsam vid hastighet, men hållmomentet är lägre och den avviker från V1E:s ~84 oz-in-standard. Kabelns fasordning skiljer sig dessutom från S-serien.

**Nuvarande bedömning:** välj A. Besparingen på cirka €11,5 totalt är för liten för att frångå den välmatchade V1E-klassen. B finns dokumenterat som ett verkligt alternativ om A:s pris/frakt ändras kraftigt.

https://www.stepperonline.nl/5st-e-serie-nema-17-bipolair-55ncm-77-88oz-in-2a-42x48mm-4-draden-met-1m-kabel-connector-5-17he19-2004s

### Varianter som väljs bort

- 0,9° NEMA17: ingen praktisk vinst för LR4 som motiverar avvikelsen.
- kortare/lägre moment-klasser: onödig marginalförlust.
- större/längre NEMA17/NEMA23: passningsrisk och inte standard-LR4.
- integrerad leadscrew-stepper: annan mekanisk konstruktion än LR4.

## PSU — ny huvudriktning: extern 24 V / 60 W Mean Well

### A. Mean Well GST60A24-P1J — nuvarande favorit

- 24 V
- 2,5 A
- 60 W
- extern Class-I desktopadapter
- IEC C14 nätintag
- 5,5×2,1 mm DC-plugg
- CE/GS m.fl. godkännanden

Färska prisreferenser 2026-08-29:
- RS Sverige: **250,90 kr inkl moms**, 713 st redo att levereras; fri frakt först över 750 kr, annars frakt kan göra ensam order dyr
- DigiKey Sverige: omkring **214,53 kr inkl moms**, färsk crawl visar lager; nätsladd säljs separat
- Mouser Sverige: **176,81 kr visat enhetspris**, 1150 i lager, men deras sida anger att produkten i EU kan vara begränsad till OEM/EMS/konstruktionskunder — ska därför inte räknas som säker konsumentkanal utan checkout-verifiering

Fördel: ingen exponerad 230 V-terminal vid CNC-elektroniken. Det är särskilt attraktivt i dammig garageinstallation.

**Inköpsregel:** köp inte från RS ensamt om 119 kr frakt tillkommer. Försök antingen samköpa andra relevanta RS-delar över fraktgränsen, hitta samma GST60A24-P1J på Amazon/annan svensk EU-kanal, eller använd DigiKey om totalen blir lägre.

### B. Mean Well HDR-60-24

- 24 V / 2,5 A / 60 W
- DIN-rail
- StepperOnline observerat pris €12,47

Elektriskt bra, men den aktuella StepperOnline-produkten är **China-only**, så den är inte längre en naturlig del av Germany-motorordern. Dessutom kräver den korrekt kapslad 230 V-installation.

**Bedömning:** endast intressant om en annan EU-säljare ger bra totalpris eller om vi ändå bygger en ordentlig elbox och kan samköpa den.

## Kopplingar 5→8 mm

StepperOnline `ST-FC04` är tekniskt rätt:
- flexibel beam coupling
- 5 mm → 8 mm
- 18×25 mm
- €1,16/st

Men aktuella sidan visar **China-only**. Två kopplingar för drygt €2 är därför inte värda en separat StepperOnline-försändelse.

Verifierat EU-alternativ:
- Anodas `AN0641`, flexibel 5×8×25 mm: **€3,40/st**
- Anodas `AN-12583`, flexibel 5×8 mm: **€4,40/st**

**Bedömning:** köp två standard 5→8 mm flexkopplingar i samma commodity-korg som övrig mekanik. Betala hellre några tior mer än skapa en separat China-order.

## Endstops

V1E:s kompletta LR4-kit använder **5 Omron**.

Exakt kvalitetskandidat:
- Omron **SS-5GL2**
- RS artikel 682-2660
- 5-pack observerat **109,90 kr inkl moms**

RS-resultaten är tidsmässigt motstridiga: en färskare crawl visar ”Add to Basket” till 109,90 kr medan en äldre crawl visar slut i lager. **Lager ska omkontrolleras precis före köp.**

Alternativ `SS-5GL2-FT` finns kring 120 kr/5 men har flatstift och är inte automatiskt bättre för LR4.

**Bedömning:** om SS-5GL2 faktiskt finns och kan samfraktas rationellt är äkta Omron klart värt ~110 kr för fem. Köp inte no-name bara för att spara 30–50 kr.

## 608-2RS

Krav: 14 × 608-2RS, **8×22×7 mm**, gummitätade.

Prisreferenser:
- generiskt 20-pack på svenska marknaden har setts omkring **123–170 kr**
- Tradera-exempel: 20 st för 170 kr + 10 kr frakt, men den annonsen är inte aktuell nog att vara köpunderlag
- Fyndiq 20-pack är 309 kr + frakt och är därmed dålig deal
- svenska stycklager 82–87 kr/st är helt fel kostnadsnivå för denna applikation

**Strategi:** köp ett verifierat 20-pack commodity-608-2RS kring 120–180 kr. Premium SKF/RS ger ingen rimlig nytta här och 6 reservlager är användbara.

## T8 / Tr8×8

Kravet får inte reduceras till bara “T8”. Det ska vara:
- Ø8 mm
- 8 mm lead / varv
- 2 mm pitch
- **4-start**
- minst 145 mm lång
- matchande mutter

200 mm är helt okej och kan kapas. Det ökar marknaden jämfört med att leta exakt 145/150 mm.

Verifierade referenser:
- OyoStepper `Tr8x8-200`: 200 mm, Ø8, 8 mm lead, cirka **€11,88/st**; mutter måste verifieras separat
- Anodas har verifierade Tr8×8-muttrar: POM `NUTBLOCK-TR8*8`, p2, 4-start, lead 8 mm, cirka **€4,36**; anti-backlash brass `AS0591`, 4-start, cirka **€4,80**

**Viktigt:** integrerade NEMA17+T8-motorer är fel arkitektur för LR4 även om deras skruvspec råkar vara rätt.

Ingen slutlig leverantör vald ännu. Målet är ett **2-pack 200 mm Tr8×8 + 2 rätt muttrar** från samma commodity-säljare.

## GT2 — nu har vi exakta verkliga kandidater

### Drivhjul — 3 st

Krav:
- exakt 16T
- GT2 / 2 mm pitch
- för 10 mm rem
- 5 mm bore
- dubbel stoppskruv är önskvärt

Verifierade EU-kandidater:
- Allegro Polen, produktkod **GT2-16T-5B_10mm_K**, 16T / 10 mm / 5 mm, 2 stoppskruvar: **7,20 PLN/st**
- Anodas Litauen, produktkod **AN-18925**, 16T / 10 mm / 5 mm: **€3,00/st**
- Hellas Digital EU, artikel **070.0051**, 16T / 10 mm / 5 mm: cirka **€1,61 inkl moms/st**

Anodas är tekniskt verifierat men internationell frakt till Sverige anges som individuellt förhandlad, vilket gör den mindre attraktiv som ensam liten order.

### Smooth idlers — 6 st

Verifierad mycket bra EU-kandidat:
- LaskaKit / POWGE **LA190008E**
- smooth GT2 idler
- för 10 mm rem
- 5 mm lagerhål
- cirka **€1,86–1,87/st inkl moms**
- färskt lager omkring 98–132 st

Även Zen3D har exakt POWGE 20T toothless / 5 mm / 9–10 mm variant, cirka €4,03, men den sågs som slut i lager.

### Rem

LaskaKit har verifierad:
- `LA190013B`: 2 m GT2, 10 mm, **fiberglass**, €4,85, lager
- `LA190013C`: 5 m GT2, 10 mm, fiberglass, cirka €7,8 när i lager; lagerstatus har varierat

Vi **köper inte rem innan slutmåttet är fryst**. Men LaskaKit är intressant eftersom samma korg kan täcka exakt rätt smooth-idlers + korrekt glasfiberrem.

### Korginsikt

LaskaKit har rätt smooth-idlers och rem billigt men deras 16T-katalogvara som hittats är endast för 6 mm rem — **fel**. Så även där måste vi undvika att låta “samma butik” lura oss till fel variant.

Det finns nu två rationella vägar:
1. LaskaKit-korg för 6 idlers + slutlig beltmängd, och 3×16T från annan billig EU-kanal.
2. Hitta en enda Amazon/EU-säljare som verifierat har **alla tre** GT2-rader med rätt varianter och jämför totalen mot väg 1.

## Kablage — viktigt förtydligande

V1E:s egna LowRider-extensioner är:
- 3 st
- 1,5 m
- 22 AWG
- sex ledare, eftersom fyra används till stepper och två kan användas till endstop

Men **sexledarkabel är inte ett mekaniskt krav**. Vi kan antingen:

A. efterlikna V1E med 3 × 6-ledarhärvor, eller
B. använda 4-ledar stepper-extension + separat 2-ledar endstopkabel.

Eftersom de valda StepperOnline-motorerna redan har **1 m kabel** ska vi inte köpa dyr specialkabel innan slutlig maskinstorlek och controllerplacering är bestämda.

**Beslut:** kabeldimension/längd optimeras efter fryst bord och controllerplacering. Köp inte generiska “stepper extensions” ännu bara för att de råkar vara billiga.

## StepperOnline-frakt

StepperOnline rekommenderar EU-kunder att prioritera lokalt tyskt lager för enklare leverans. Produktens egna “Ships from”-val är viktigare än den generella butikstexten.

**Kontrollerat just nu:**
- `5-17HS19-2004S1`: Germany warehouse finns
- `HDR-60-24`: China only på aktuell sida
- `ST-FC04`: China only på aktuell sida

De anger dessutom mindre packavgift för beställningar med fler än två artiklar från vissa lokallager. Räkna alltid checkout-totalen.

## Nuvarande bästa orderarkitektur

1. HaWiWe — **klar/betald**.
2. StepperOnline Germany — sannolikt **endast `5-17HS19-2004S1` fempack**.
3. Elecrow — Jackpot3.
4. VEVOR — 0700C 800 W.
5. PSU — sannolikt extern Mean Well GST60A24-P1J från svensk/EU-kanal, helst samfraktad med annan el om fraktgränsen annars gör den dyr.
6. Commodity-korg A — T8 + muttrar + 5→8-kopplingar + 608-2RS + eventuellt Omron/endstop-kablage från Amazon/EU-säljare.
7. Commodity-korg B/GT2 — optimera 16T + smooth idlers + rem; LaskaKit är nu en stark kandidat för idlers/rem men inte 16T.
8. PLA — billig bulkkanal endast om checkout landar nära 100 kr/kg levererat.

Det är **inte** ett mål i sig att minska antalet paket. En extra order är okej när den sparar tydliga pengar eller säkrar rätt specialvariant. Däremot ska vi gärna betala 30–80 kr extra i en befintlig korg för att slippa en ny liten order.

## Nästa optimeringspass

Innan commodity-delarna beställs:

- hitta 2–5 exakta kandidater per återstående rad
- notera SKU/ASIN/modell, vald variant, pris, lager och ursprungsland/warehouse
- markera vilka som kan ligga i samma kundvagn
- kontrollera faktisk Sverige-frakt i checkout när webbpriset inte räcker
- välj billigaste **korrekta korgkombination**, inte billigaste enskilda komponent
