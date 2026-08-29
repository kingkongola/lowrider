# Sourcing plan — 29 Aug 2026

Mål: bra kvalitet utan dumsnålhet, låg total kostnad inklusive frakt, och så få beställningar som rimligt.

## Låsta val

- Controller: **Jackpot3**
- Router: **VEVOR VV-1B-220V, 710 W, 65 mm, 13k–33k rpm**
- Amazon Prime finns och ska användas som fraktfördel när totalpriset blir bäst.

## Rekommenderad butikskombo

### 1. Elecrow — Jackpot3

- Jackpot3: **$76.99**
- Aktuell kurs 29/8/2026: ca **737 kr före frakt**
- V1E hänvisar internationella köpare till Elecrow för mer direkt/billigare frakt.
- Kortet har 6 integrerade TMC2226-drivare och FluidNC.

**Köp här om frakten i checkout är rimlig.** V1E:s egen butik tar $75.99 men internationell frakt är normalt sämre.

### 2. Amazon.se / Prime — motorer + standarddelar

Motorer:
- STEPPERONLINE 5-pack NEMA17, 59 Ncm / 84 oz-in, 2 A, 1 m kabel
- Aktuellt observerat pris: **608 kr**
- Matchar momentet i V1E:s LR4-kit.

Standarddelar att samla i samma Prime-order:
- 3 × GT2 10 mm 16T pulleys
- 6 × GT2 10 mm 20T smooth idlers, 5 mm bore
- GT2 10 mm belt, längd efter kalkylator
- 14 × 608-2RS bearings
- 2 × T8 leadscrew + brass nut, minst 145 mm, 8 mm lead / 4-start
- 2 × 5→8 mm shaft couplers
- 5 × mechanical endstops + cable
- stepper extension cables
- 24 V PSU, ca 60 W

Prisindikationer som faktiskt hittats:
- 20-pack 608-2RS på Amazon: ca **123 kr**
- 10-pack 5→8 mm couplers på Amazon: ca **140 kr** (överkant i antal men fortfarande billigt)
- stepper extension cable 5-pack på Amazon: ca **107 kr**

För GT2, T8, endstops och PSU ska exakt Amazon-artikel verifieras i checkout innan köp. Prioritera rätt spec framför lägsta pris.

### 3. VEVOR EU — router

- Modell: **VV-1B-220V**
- 710 W, 220 V, 65 mm kropp
- 13 000–33 000 rpm
- fixed-base-version
- Aktuellt pris: **€42.90 ≈ 477 kr före eventuell frakt**
- Inkluderar 1/4", 6 mm och 8 mm collets

Den dyrare 3-/4-base-versionen ger ingen relevant nytta när motorn sitter permanent i CNC:n.

## Total kostnadsbild

Bekräftade/observerade delpriser hittills, exklusive ännu okänd frakt och de Amazon-smådelar där exakt artikel inte är låst:

- Jackpot3: ~737 kr
- 5 motorer: 608 kr
- VEVOR-router: ~477 kr
- 608-lager: ~123 kr
- couplers: ~140 kr
- stepper extension cables: ~107 kr

**Delsumma: ~2 192 kr**

Till detta kommer GT2-rem/pulleys/idlers, T8-skruvar, ändlägen, PSU och frakt. Rimlig total för allt återstående elektronik/mekanik/router bedöms fortfarande ligga ungefär **3 000–4 000 kr**, men slutpriset ska inte låsas förrän exakt Amazon-korg och Elecrow-frakt är verifierade.

## Viktigt

- Köp inte 6 mm GT2-delar — LR4 använder **10 mm**.
- Köp inte 4-driver-controller — LR4 ska ha individuella drivare till fem motorer.
- Köp inte svagare motorer bara för att spara lite; 59 Ncm / 84 oz-in är rätt nivå.
- Köp inte stort 300–350 W PSU av slentrian; V1E:s eget kit använder 24 V och relativt låg effekt.
- Den redan köpta Makita 3.175 mm-colleten ska **inte** räknas som kompatibel med VEVOR förrän det är verifierat.
