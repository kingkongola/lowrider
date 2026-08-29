# Sourcing plan — researched 2026-08-29

Mål: bra kvalitet utan dumsnålhet, låg total kostnad inklusive frakt, och så få beställningar som rimligt.

**Temporalitet:** alla priser/lageruppgifter nedan är kontrollerade **2026-08-29** och ska omkontrolleras före köp.

## Låsta val

- Controller: **Jackpot3**
- Router: **VEVOR VV-1B-220V, 710 W, 65 mm, 13 000–33 000 rpm**
- Amazon Prime finns och ska användas som möjlig fraktfördel, men butik väljs efter totalpris inklusive frakt.

## Rekommenderad köpstruktur

### A. Elecrow — controller

| Antal | Artikel | SKU / art.nr | Pris 2026-08-29 | Frakt | URL | Status |
|---:|---|---|---:|---|---|---|
| 1 | Jackpot3 CNC Controller | **CQA240812C2** | **US$76.99** | visas i checkout; ej publikt verifierad | https://www.elecrow.com/jackpot3-cnc-controller.html | **KÖP** om checkout-frakten till Sverige är rimlig |

V1E hänvisar internationella köpare direkt till Elecrow. Jackpot3 har 6 integrerade TMC2226-drivare och kör FluidNC. V1E:s egen butik tar US$75.99 men anger själv Elecrow som alternativ för billigare/direct international shipping.

V1E referens: https://www.v1e.com/products/jackpot3-cnc-controller

### B. StepperOnline EU/Germany — motorer + PSU

| Antal | Artikel | Modell / art.nr | Pris 2026-08-29 | Frakt | URL | Status |
|---:|---|---|---:|---|---|---|
| 1 pkt = 5 st | NEMA17 59 Ncm / 83.55 oz-in, 2 A, 48 mm kropp, 1 m kabel | **5-17HS19-2004S1**; motor MPN **17HS19-2004S1** | **€38.13 / 5-pack** | checkout; välj Germany warehouse | https://www.stepperonline.nl/5st-nema-17-bipolair-59ncm-83-55oz-in-2a-42x48mm-4-draden-met-1m-kabel-aansluiting-5-17hs19-2004s1 | **KÖP** |
| 1 | Mean Well DIN-PSU 24 VDC, 2.5 A, 60 W | **HDR-60-24** | **€12.47** | samfraktas lämpligen med motorerna | https://www.stepperonline.nl/hdr-60-24-meanwell-60w-24vdc-2-5a-115-230vac-ultra-slim-step-shape-din-rail-voeding-hdr-60-24 | **KÖP** |

Motorerna matchar V1E:s 84 oz-in-nivå och har 24 mm lång 5 mm D-axel, alltså över V1E:s minimikrav 20 mm axellängd.

PSU:n är kvalitetsmässigt bättre än generisk no-name och fortfarande billig. Jackpot3 accepterar 9–24 VDC och V1E lyfter 24 V som standardval.

### C. VEVOR EU — fräsmotor

| Antal | Artikel | Modell / produkt-ID | Pris 2026-08-29 | Frakt | URL | Status |
|---:|---|---|---:|---|---|---|
| 1 | VEVOR compact router, fixed base, 710 W, 65 mm | **VV-1B-220V**; VEVOR produkt-ID i URL **010376710625** | **€42.90** observerat | kontrollera checkout | https://eur.vevor.com/compact-router-c_10131/vevor-electric-hand-trimmer-palm-router-with-three-collets-and-fixed-base-710w-p_010376710625 | **KÖP** |

Spec: 220 V, 710 W, 13 000–33 000 rpm, 65 mm kropp. Levereras med 1/4", 6 mm och 8 mm spännhylsor.

**Obs:** den redan köpta Makita 3,175 mm-spännhylsan får inte räknas som kompatibel med VEVOR-fräsen förrän konan/gängan är verifierad.

## Commodity-delar — exakt LR4-spec

V1E:s officiella LR4-BOM, kontrollerad 2026-08-29:
https://docs.v1e.com/lowrider/

| Antal | Del | Exakt krav | V1E:s officiella inköpslänk |
|---:|---|---|---|
| 3 | GT2 drive pulley | **16T, GT2, för 10 mm rem, 5 mm motoraxel** | https://amzn.to/3n9mUGM |
| 6 | Smooth idler | **20T, smooth, för 10 mm rem, 5 mm bore** | https://amzn.to/4dRxh9L |
| enl. kalkylator | GT2-rem | **10 mm bred, GT2, utan stålkord** | https://amzn.to/48cO4mt |
| 5 | Endstop | mekanisk enligt V1E-upplägg | https://amzn.to/396oRzi |
| 14 | Lager | **608-2RS** | https://amzn.to/3FDI8EI |
| 2 | T8 lead screw + nut | **minst 145 mm, 4-start, 2 mm pitch, 8 mm/rev** | https://amzn.to/4eDgHLN |
| 2 | Axelkoppling | **5 mm → 8 mm** | https://amzn.to/4etRhjC |
| 1 | PSU-alternativ | **9–24 V, minst 36 W** | https://amzn.to/3TXtjoM |
| 3 | Stepper extension | V1E:s standard extension wiring | https://amzn.to/3BJMgov |

### Viktigt om Amazon-länkarna

V1E använder `amzn.to`-kortlänkar. I researchmiljön 2026-08-29 gick länkarna att läsa ur V1E:s officiella BOM men Amazons omdirigering gick inte att lösa till stabil svensk ASIN/produkt-ID. Därför **har jag inte hittat på artikelnummer** för dessa.

Innan köp ska varje kortlänk öppnas och följande dokumenteras här:
- Amazon ASIN
- exakt produktnamn
- pris
- Prime-status
- leverans/frakt till Sverige
- säljare / fulfilled-by

Det är bättre än att låsa en felaktig no-name-listning bara för att fylla en tabell.

## Alternativ EU-referens för flera commodity-delar — Botland

Botland hade 2026-08-29 flera exakt matchande LR4-komponenter med tydliga SKU:er och frakt från **€6.50**, men deras internationella butik visade samtidigt text om registrerade B2B-kunder. Använd därför dessa som **spec/prisreferens**, inte förstahandsköp tills privatköp till Sverige verifierats.

| Del | SKU | Pris | URL |
|---|---|---:|---|
| 16T GT2 pulley, 10 mm belt, 5 mm bore | **AMS-18925** | €1.90/st | https://botland.store/components-for-3d-printers-construction/18925-gt2-timing-belt-6mm-pulley-16t-5mm-hole-5904422354947.html |
| 20T smooth idler, 10 mm belt, 5 mm bore | **AMS-18926** | €6.00/st | https://botland.store/components-for-3d-printers-construction/18926-gt2-timing-belt-toothed-belt-10mm-pulley-idler-20t-5mm-hole-5904422354954.html |
| 5→8 mm flexible coupler | **AMS-18932** | €2.90/st | https://botland.store/components-for-3d-printers-construction/18932-flexible-coupling-aluminum-5x8mm-5904422355005.html |
| T8 screw 400 mm, 2 mm pitch, 8 mm lead | **AMS-18923** | €6.90/st | https://botland.store/components-for-3d-printers-construction/18923-lead-screw-8mm-length-400mm-5904422354923.html |
| T8 brass nut | **AMS-18924** | €1.90/st | https://botland.store/components-for-3d-printers-construction/18924-lead-screw-nut-8mm-5904422354930.html |

Botlands T8-spec är uttryckligen 8 mm diameter, 2 mm pitch och 8 mm lead, alltså rätt LR4-geometri. 400 mm är längre än nödvändigt men går att kapa; V1E kräver minst 145 mm.

## Alternativ svensk PSU

Om StepperOnline-frakten gör deras PSU olönsam:

| Antal | Artikel | Art.nr | Pris 2026-08-29 | URL |
|---:|---|---|---:|---|
| 1 | Desktop PSU 24 VDC 2.5 A 60 W | **Electrokit 4102 2679** | **279 kr** | https://www.electrokit.com/nataggregat-desktop-24v-2.5a-60w |

Nackdel: C13-nätsladd ingår inte. Fördelen är sluten lågspänningsadapter jämfört med öppen PSU. Om Mean Well HDR-60-24 samfraktas med motorerna är Mean Well-alternativet sannolikt bättre totalekonomi.

## Inköpsordning

1. **Elecrow:** Jackpot3, efter att checkout-frakten noterats.
2. **StepperOnline Germany warehouse:** 5-pack 17HS19-2004S1 + HDR-60-24 i samma order.
3. **VEVOR EU:** VV-1B-220V.
4. **Amazon Prime:** LR4-smådelarna från V1E:s egna länkar, men först efter att ASIN/pris/Prime-status verifierats från svensk checkout.

Detta ger normalt **4 beställningar**. Att pressa ner till 2–3 butiker är bara vettigt om totalpriset faktiskt blir lägre; vi ska inte köpa fel GT2-bredd eller sämre motorer för att minska antalet paket.

## Saker som inte ska köpas ännu

- GT2-remlängd: vänta tills slutmåtten är låsta i LR4-kalkylatorn.
- Extra spännhylsa till VEVOR: vänta tills kompatibilitet med redan köpt 3,175 mm-hylsa är utredd.
- Touch plate: valfritt senare.
- Dyra LR4-prestandauppgraderingar: inte före standardmaskinen fungerar.

## Officiell BOM-källa

V1E LowRider V4 Parts Needed, hämtad 2026-08-29:
https://docs.v1e.com/lowrider/
