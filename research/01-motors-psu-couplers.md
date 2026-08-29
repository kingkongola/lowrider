# Delpass 1 — motorer, 24 V PSU och 5→8 mm-kopplingar

Datum: 2026-08-29

Mål: optimera denna lilla del av LR4-inköpet innan nästa komponentgrupp behandlas.

## Motorer

### Rekommenderat val

**STEPPERONLINE `5-17HS19-2004S1`** — 5-pack.

Verifierade data:
- 59 Ncm / 83,55 oz-in
- 2,0 A/fas
- 1,8°
- 42×42×48 mm
- 5 mm D-axel
- 24 mm axellängd
- 1 m kabel
- Germany warehouse finns som val på aktuell produktsida

Det träffar V1E:s ~84 oz-in-klass nästan exakt och har rätt mekaniska format.

Alternativet `5-17HE19-2004S` på 55 Ncm sparar för lite på hela fempacket för att motivera lägre moment och avvikelse från standardvalet.

**Beslut:** motorvariant kan betraktas som låst till `5-17HS19-2004S1`, förutsatt att checkout-frakten från Germany warehouse inte är orimlig.

Källa: https://www.omc-stepperonline.com/de/5-stueck-nema-17-bipolar-59ncm-84oz-in-2a-42x48mm-4-draehte-mit-1m-kabel-und-stecker-5-17hs19-2004s1

## PSU

### Rekommenderad typ

**Mean Well `GST60A24-P1J`**

- 24 V DC
- 2,5 A
- 60 W
- extern desktopadapter
- IEC C14 på nätsidan
- 5,5×2,1 mm DC-plugg
- Class I
- CE/GS m.fl.

Det är attraktivare än ett öppet DIN-/chassinätaggregat för första LR4-versionen eftersom 230 V hålls utanför CNC-elektronikboxen och den dammiga maskinmiljön.

### Aktuella prisreferenser

- **RS Sverige:** 250,90 kr inkl moms, lager. Fri frakt först över 750 kr; äldre/fräschare RS-data anger ca 119 kr frakt under gränsen. Dålig ensamorder men potentiellt bra om andra relevanta RS-delar samköps.
- **DigiKey Sverige:** cirka 214,5–224,6 kr inkl moms i färska träffar. IEC-nätsladd säljs separat. Frakt måste verifieras i checkout.
- **Reichelt:** cirka €17,80 inkl tysk moms, lager. Frakt till Sverige måste kontrolleras och avgör om det blir en bra korg.
- **Mouser:** lägre listpris (~176,8 kr), men produktsidan säger uttryckligen att den inte säljs till EU/UK-konsumenter; räknas därför inte som köpväg.

**Nuvarande beslut:** PSU-modellen är i praktiken låst till `GST60A24-P1J`. Säljare låses först efter att den kan samoptimeras med nästa delgrupp eller checkout-frakt verifierats.

Källor:
- https://se.rs-online.com/web/p/acdc-adaptrar/8808414
- https://www.digikey.se/en/products/detail/mean-well-usa-inc/GST60A24-P1J/7703715
- https://www.reichelt.com/de/en/shop/product/desktop_power_supply_60_w_24_v_2_5_a-171056

## 5→8 mm flexkopplingar

Krav: 2 st, 5 mm motoraxel → 8 mm T8-skruv, flexibel aluminiumkoppling.

### Ny relevant svensk kandidat

**Invize AB — `mec-flexcoupling-5x8`**

- 49 kr/st
- 10 st i lager vid kontroll
- 25×19×19 mm
- 5 mm → 8 mm
- två stoppskruvar per axel
- svensk butik

Två kostar 98 kr. Invize har fri standardfrakt inom Sverige från **200 kr**, vilket gör delen extra intressant om nästa delpass hittar minst ~102 kr andra korrekta LR4-delar där.

Viktigt: deras GT2-sortiment har redan visat en variantfälla — de har 20T-hjul och 6 mm-idlers som inte matchar LR4:s 16T / 10 mm / smooth-idler-krav. Samköp får därför endast göras med verifierat rätt variant.

**Beslut:** köp inte kopplingarna separat ännu. Håll `mec-flexcoupling-5x8` som förstahandskandidat och försök nå Invizes 200-kronorsgräns med nästa korrekt verifierade commodity-del. Om inget mer passar är 98 kr + deras normala småorderfrakt fortfarande sannolikt rimligt.

Källor:
- https://invize.se/produkt/mec-flexcoupling-5x8/
- https://invize.se/kopvillkor/

## Slutsats delpass 1

- **Motor:** lås `5-17HS19-2004S1`.
- **PSU:** lås modell `GST60A24-P1J`, men inte återförsäljare ännu.
- **Kopplingar:** Invize `mec-flexcoupling-5x8` är nu bästa svenska kandidat; vänta med köp tills nästa korggrupp är analyserad.
- Ingen av dessa tre ska tvingas in i samma butik bara för att minska antalet paket.

## Nästa delpass

GT2-systemet separat:
- 3 × 16T / 5 mm / 10 mm pulley
- 6 × smooth idler / 5 mm / 10 mm
- 10 mm glasfiberförstärkt GT2-rem

Målet är att se om Invize, Amazon Prime eller en EU-specialbutik kan ge en bättre gemensam korg utan fel varianter.
