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
- 3 × GT2 16T drivhjul, för 10 mm rem
- 6 × GT2 20T smooth idlers, 5 mm hål, för 10 mm rem
- GT2 10 mm rem, **inte stålkord**, slutlig längd från LR4-kalkylatorn
- 5 × endstops
- 14 × 608-2RS, 8×22×7 mm
- 2 × T8/Tr8×8, minst 145 mm, 4-start, 2 mm pitch, 8 mm/rev + rätt mutter
- 2 × 5→8 mm koppling
- 3 × kabel-extensioner från YZ_Max/Core till controller
- 24 V PSU; V1E:s nuvarande kit är i praktiken 60 W / 2,5 A-klassen

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

### Beställningar som ska optimeras ihop

**StepperOnline-korg** är stark kandidat för:
- 5 motorer
- 24 V PSU
- 2 × 5→8 mm flexkoppling

**Amazon Prime / annan EU-butik** ska jämföras som en hel commodity-korg för:
- 608-2RS
- T8/Tr8×8 + muttrar
- 16T pulleys
- 20T smooth idlers
- endstops
- kablage/kontakter
- gänglåsning/småel
- eventuellt rem när slutlängden är låst

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

## PSU — två rationella arkitekturer

### A. Mean Well HDR-60-24 — sannolik vinnare om elen kapslas

- 24 V
- 2,5 A
- 60 W
- DIN-rail
- observerat StepperOnline-pris: **€12,47**
- lager observerat: 200

Fördelar:
- kan samfraktas med motorerna/kopplingarna
- exakt rätt effektklass
- kvalitetsaggregat
- skyddad plastkapsling jämfört med helt öppna metall-PSU:er

Nackdel:
- 230 V-anslutningen måste byggas korrekt och sitta skyddad/kapslad.

https://www.stepperonline.nl/hdr-60-24-meanwell-60w-24vdc-2-5a-115-230vac-ultra-slim-step-shape-din-rail-voeding-hdr-60-24

### B. Mean Well GST60A24-P1J — säkrare/enklare extern bricka

- 24 V
- 2,5 A
- 60 W
- IEC C14 nätintag
- extern Class-I desktopadapter
- 5,5×2,1 mm DC-plugg

Svenska priser observerade 2026-08-29:
- RS: ca **251 kr inkl moms**, lager
- Mouser: ca **177 kr exkl moms** visat pris

Fördel: ingen exponerad 230 V-terminal vid själva CNC-elektroniken.

Nackdel: separat order kan äta upp prisfördelen; DC-plugg måste adapteras/kapas till Jackpot VMOT.

**Beslut ej låst:** jämför slutlig StepperOnline-checkout för A mot verkligt totalpris för B. Om HDR-korgen redan beställs och vi gör en vettig elbox är HDR sannolikt bäst totalt.

## Kopplingar 5→8 mm

StepperOnline **ST-FC04**:
- flexibel beam coupling
- 5 mm → 8 mm
- 18×25 mm
- observerat pris: **€1,16/st**
- 2 behövs

Det är en mycket stark samfraktskandidat med motorerna.

https://www.stepperonline.nl/askoppeling

Styv GX2025-5-8 finns också, men LR4-specen använder coupler och en liten flexibel koppling är den naturliga standardlösningen. Dyrare double-disc MP2635-5-8 (~€6,72/st) ger ingen tydlig nytta här.

## Endstops

V1E:s kompletta LR4-kit använder **5 Omron**.

Exakt kvalitetskandidat i Sverige:
- Omron **SS-5GL2**
- RS artikel 682-2660
- 5-pack observerat omkring **110 kr inkl moms** när tillgängligt

Det är så billigt i relation till hela bygget att äkta Omron är attraktivt om de kan fås utan dyr separat frakt. Köp inte fem no-name-brytare för att spara några tior om de ligger i samma kundvagn som ett bättre alternativ.

## 608-2RS

Krav: 14 × 608-2RS, **8×22×7 mm**, gummitätade.

Prisreferenser 2026-08-29:
- Amazon/Prisjakt-index: generiskt 20-pack omkring **123 kr** har förekommit.
- RS PRO: ca **25,62 kr/st inkl moms**, betydligt dyrare om de köps separat.

**Preliminär strategi:** 20-pack commodity-lager för cirka 120–170 kr är mer rationellt än premiumlager. Belastningen och varvtalet i LR4 motiverar inte SKF-pris; 6 reservlager är dessutom användbara.

## T8 / Tr8×8

Kravet får inte reduceras till bara “T8”. Det ska vara:
- Ø8 mm
- 8 mm lead / varv
- 2 mm pitch
- **4-start**
- minst 145 mm lång
- matchande mutter

200 mm är helt okej och kan kapas. Det ökar marknaden jämfört med att leta exakt 145/150 mm.

Verifierad referens:
- Tr8x8-200, 200 mm, 8 mm diameter, 8 mm lead: ca **€11,88/st** hos OyoStepper (mutter måste verifieras separat).

Ingen slutlig leverantör vald ännu; denna rad ska optimeras mot Amazon/EU-korgen.

## GT2 — variantfällor

Drivhjul:
- exakt **16T**
- GT2 / 2 mm pitch
- **10 mm rembredd**
- **5 mm bore**
- 3 st

Idlers:
- **20T diameter/klass**
- **smooth** förstahandsval
- för **10 mm rem**
- **5 mm bore**
- 6 st

V1E säger att toothed idlers kan ersätta smooth om smooth inte går att få tag i, men smooth är standardvalet.

Många svenska 3D-butiker som ser rätt ut säljer egentligen bara 6 mm-varianter. Exempel: 123-3D:s 16T/5 mm-listning är uttryckligen max 6 mm rem och är därför **fel för LR4**.

## Kablage — viktigt förtydligande

V1E:s egna LowRider-extensioner är:
- 3 st
- 1,5 m
- 22 AWG
- sex ledare, eftersom fyra används till stepper och två kan användas till endstop

Men **sexledarkabel är inte ett mekaniskt krav**. V1E-dokumentationen visar i praktiken stepper- och endstopledningar som går tillsammans genom maskinen. Vi kan därför antingen:

A. efterlikna V1E med 3 × 6-ledarhärvor, eller
B. använda 4-ledar stepper-extension + separat 2-ledar endstopkabel.

Eftersom de valda StepperOnline-motorerna redan har **1 m kabel** ska vi inte köpa stora mängder dyr specialkabel innan slutlig maskinstorlek och controllerplacering är bestämda.

**Beslut:** kabeldimension/längd optimeras efter fryst bord och controllerplacering. Köp inte generiska “stepper extensions” ännu bara för att de råkar vara billiga.

## StepperOnline-frakt

StepperOnline har tyskt lager för flera motorvarianter och rekommenderar EU-kunder att prioritera lokalt lager för snabbare leverans och enklare tullhantering. De anger också att beställningar från tyskt lager med fler än två artiklar kan få en mindre packavgift.

Det betyder att vi måste jämföra **checkout-totalen**, inte bara radpriserna.

## Nuvarande bästa orderarkitektur

1. HaWiWe — **klar/betald**.
2. StepperOnline — sannolikt `5-17HS19-2004S1` + `HDR-60-24` + 2× `ST-FC04`, om allt kan skickas rationellt från EU/Tyskland.
3. Elecrow — Jackpot3.
4. VEVOR — 0700C 800 W.
5. En enda commodity-korg, helst Amazon Prime eller annan EU-butik, för GT2/T8/lager/endstops/kablage efter exakt variantverifiering.
6. PLA från billig bulkkanal om den slår commodity-korgens totalpris tydligt.

## Nästa optimeringspass

Innan någon av de återstående commodity-delarna beställs:

- samla 2–5 exakta kandidater per rad
- notera SKU/ASIN/modell, vald variant, pris och lager
- markera vilka som kan ligga i samma kundvagn
- räkna checkout-/fraktkostnad för hela kandidatkorgar
- välj billigaste **korrekta korgkombination**, inte billigaste enskilda komponent
