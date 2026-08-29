# Sourcing plan — researched 2026-08-29

Mål: bra kvalitet utan dumsnålhet, låg total kostnad inklusive frakt och så få beställningar som rimligt.

**Temporalitet:** priser/lageruppgifter ska omkontrolleras före köp.

## Låsta val

- Maskin: **LowRider V4** — PrintNC/IndyMill är inte längre aktiva alternativ.
- Controller: **Jackpot3**
- Router: **VEVOR 0700C, 800 W, 65 mm, 10 000–30 000 rpm**
- Amazon Prime finns och används som möjlig fraktfördel, men butik väljs efter totalpris inklusive frakt.
- Laser väntar till tidigast 2027.
- Plasma ingår inte i nuvarande scope.
- Dammutsug är ett grundkrav, inte en senare lyxuppgradering.

## Redan köpt och betalt — ska inte sourcas igen

HaWiWe-order 2026-08-29, **165,50 € inklusive 8,00 € frakt, betald**:
- Aluminium XZ plates — 39,50 €
- 4 × MGN12H 150 mm linear rails — 57,00 €
- Schraubenset LowRider 4 — 32,00 €
- Elaire/Makita-style 1/8" (3,175 mm) collet — 29,00 €

Schraubenset täcker exakt:
- 14 × M8×40
- 14 × M8 nyloc
- 60 × M5×30
- 60 × M5 nyloc
- 83 × M3×10
- 10 × M2.5×12

Källa: https://hawiwe.de/produkt/schraubenset-lowrider-4/

## Kvar att köpa

### Elecrow / V1E
- 1 × **Jackpot3 CNC Controller**
  - Elecrow SKU: **CQA240812C2**
  - Elecrow pris observerat 2026-08-29: **US$76.99** före checkout-frakt
  - https://www.elecrow.com/jackpot3-cnc-controller.html
  - V1E referens: https://www.v1e.com/products/jackpot3-cnc-controller

### StepperOnline / Amazon — motorer och PSU
- 1 paket = 5 × NEMA17, 59 Ncm / 83.55 oz-in, 2 A
  - paket: **5-17HS19-2004S1**
  - motor: **17HS19-2004S1**
  - jämför StepperOnline EU mot Amazon Prime på totalpris inklusive frakt
- 1 × 24 V PSU, minst 36 W
  - Mean Well är föredraget när priset är rimligt
  - kandidat: **HDR-60-24**, 24 V / 2,5 A / 60 W

### VEVOR EU — rätt router
- 1 × **VEVOR 0700C, 800 W** compact router
  - modell: **0700C**
  - VEVOR produkt-ID/URL: **010235793217**
  - 220–240 V / 50 Hz
  - 800 W
  - 10 000–30 000 rpm
  - 65 mm kropp
  - VEVOR anger kompatibilitet med Makita 0700-bas
  - https://eur.vevor.com/compact-router-c_10131/vevor-wood-router-1-25hp-800w-compact-wood-trimmer-router-combo-tool-with-plunge-and-fixed-base-30000rpm-6-variable-speeds-with-1-4-5-16-collets-dust-hood-for-woodworking-slotting-trimming-p_010235793217

**Varför denna och inte VV-1B-220V 710 W:**
- den heter uttryckligen 0700C och matchar därmed bättre den Makita 700-familj som den redan köpta Elaire-hylsan är gjord för
- dokumenterat V1E-fall finns där en VEVOR 0700C körs med Makita-style/Sienci 1/8"-collet i VEVOR:s originalmutter med mycket liten runout
- https://forum.v1e.com/t/crappy-router-collet/50663/8

### PLA — målet är nära 100 kr/kg

LR4 behöver ungefär **2,7 kg PLA**. Köp hellre 4–6 kg så att omprint och framtida reservdelar inte kräver ny färg/batch.

**Bästa prisvärda kandidat hittad 2026-08-29:**
- **SUNLU vanlig PLA 1,75 mm, bulk/Mix&Match direkt från SUNLU EU**
- MOQ: 6 kg
- observerat bulkpris vid 6 rullar: från **€9,19/kg**
- 10+ rullar: från €8,99/kg
- SUNLU anger fri frakt till större delen av EU; Sverige ska verifieras i checkout före köp
- dimensionstolerans enligt produktsidan: 1,75 ± 0,02 mm
- https://store.sunlu.com/sv-fr/products/over-6kg-of-pla-pla-meta-3d-filaments-1kg-2-2lbs-fit-most-of-fdm-printer

Vid aktuell EUR/SEK-kurs 2026-08-29 motsvarar €9,19/kg ungefär **102 kr/kg** före eventuell checkout-avvikelse. Detta träffar kostnadsmålet betydligt bättre än Amazon just nu.

**Amazon-läget 2026-08-29:**
- SUNLU PLA+ 5 kg svart: ca 699,99 kr ≈ 140 kr/kg
- SUNLU PLA+ 4 kg svart: ca 599,99 kr ≈ 150 kr/kg
- JAYO PLA+ 4,4 kg: ca 602 kr ≈ 137 kr/kg

Amazon/Prime är alltså bekvämt men inte billigast just nu om målet är runt 100 kr/kg.

**Creality:**
- Soleyin Ultra PLA har mycket bra bulkpriser, t.ex. 6 kg för €59 / 10 kg för €89, men de aktuella bundle-varianterna som kontrollerades 2026-08-29 visades som slutsålda. Bevaka, men köp inte baserat på ett stale pris.

**Materialval:** vanlig PLA är förstahandsval för strukturella LR4-delar. PLA+ är inte nödvändigt bara för att namnet låter bättre; V1E-designen är byggd runt styv PLA.

### Commodity-delar — V1E-spec

Källa: https://docs.v1e.com/lowrider/

- 3 × **GT2 16T pulley, 10 mm belt, 5 mm bore**
- 6 × **GT2 20T smooth idler, 10 mm belt, 5 mm bore**
- GT2-rem **10 mm**, utan stålkord — längd från LR4-kalkylatorn
- 5 × mekaniska endstops + kablage/kontakter
- 14 × **608-2RS** lager
- 2 × **T8 leadscrew + nut**, minst 145 mm, 4-start, 2 mm pitch, 8 mm/rev
- 2 × **5→8 mm** axelkoppling
- 3 × stepper extension cables
- ca 18 × **M4×12 mm+** trä-/plåtskruv för bordsmontage; dessa ingår inte i HaWiWe screw set
- gänglåsning till pulley grub screws
- lätt smörjmedel
- minst 1 × 1/8" / 3,175 mm single-flute frässtål

## Makita/Elaire-collet → VEVOR 0700C

**Bedömning 2026-08-29: hög sannolikhet att den passar. Ingen extra 1/8"-collet ska köpas i förväg.**

Verifierat underlag:

1. HaWiWe-hylsan är importerad från **Elaire** och är avsedd för Makita RT700C / RT0700CX3 / RT0701C m.fl.
   - Elaire-produktfamilj: **MRP-1250**
   - https://hawiwe.de/produkt/makita_spannzange/
   - https://elairecorp.com/product-category/makita-style-router-collets/
2. VEVOR:s 800 W-router heter uttryckligen **0700C**, har 65 mm kropp och VEVOR anger Makita 0700-bas-kompatibilitet.
3. Praktiskt V1E-fall: en användare kör **VEVOR 0700C (Makita 700-klon)** med 1/8" Makita-style/Sienci-collet i VEVOR:s originalmutter och rapporterar mycket liten runout.
   - https://forum.v1e.com/t/crappy-router-collet/50663/8

Det saknas ett explicit datablad från VEVOR/Elaire som säger “MRP-1250 passar VEVOR 0700C”. Därför ska den provpassas före drift och runout kontrolleras med ett rakt 1/8"-verktyg.

## Bord / damm

Fortfarande kvar:
- slutlig arbetsyta och bordsmått
- bord/underrede
- plan bordsskiva / spoilboard
- material till permanenta strut plates, max 6,35 mm
- kabelinfästning/buntband
- dust shoe
- grovdammsugare/shop-vac
- cyklonavskiljare
- slang och avlastad slangupphängning
- enkel lättstädad avskärmning/gardin runt CNC-zonen

## Ska inte köpas ännu

- GT2-remlängd före att slutmåtten är låsta i LR4-kalkylatorn
- extra 1/8"-spännhylsa
- laserutrustning före 2027
- prestandauppgraderingar innan standardmaskinen fungerar
