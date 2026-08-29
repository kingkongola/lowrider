# Sourcing plan — researched 2026-08-29

Mål: bra kvalitet utan dumsnålhet, låg total kostnad inklusive frakt och så få beställningar som rimligt.

**Temporalitet:** priser/lageruppgifter ska omkontrolleras före köp.

## Låsta val

- Controller: **Jackpot3**
- Router: **VEVOR VV-1B-220V, 710 W, 65 mm, 13 000–33 000 rpm**
- Amazon Prime finns och används som möjlig fraktfördel, men butik väljs efter totalpris inklusive frakt.

## Redan köpt — ska inte sourcas igen

HaWiWe-order 2026-08-29:
- Aluminium XZ plates
- 4 × MGN12H 150 mm linear rails
- Schraubenset LowRider 4
- Elaire/Makita-style 1/8" (3,175 mm) collet

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

### StepperOnline EU
- 1 paket = 5 × NEMA17, 59 Ncm / 83.55 oz-in, 2 A
  - paket: **5-17HS19-2004S1**
  - motor: **17HS19-2004S1**
  - observerat pris 2026-08-29: **€38.13 / 5-pack**
  - https://www.stepperonline.nl/5st-nema-17-bipolair-59ncm-83-55oz-in-2a-42x48mm-4-draden-met-1m-kabel-aansluiting-5-17hs19-2004s1
- 1 × Mean Well 24 V / 2.5 A / 60 W PSU
  - **HDR-60-24**
  - observerat pris 2026-08-29: **€12.47**
  - https://www.stepperonline.nl/hdr-60-24-meanwell-60w-24vdc-2-5a-115-230vac-ultra-slim-step-shape-din-rail-voeding-hdr-60-24

### VEVOR EU
- 1 × **VV-1B-220V** fixed-base compact router
  - produkt-ID i URL: **010376710625**
  - 710 W, 220 V, 65 mm, 13 000–33 000 rpm
  - observerat pris 2026-08-29: **€42.90**
  - https://eur.vevor.com/compact-router-c_10131/vevor-electric-hand-trimmer-palm-router-with-three-collets-and-fixed-base-710w-p_010376710625

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

## Makita/Elaire-collet → VEVOR: kompatibilitet

**Bedömning 2026-08-29: starkt sannolik kompatibilitet. Ingen extra 1/8"-collet ska köpas i förväg.**

Verifierat underlag:

1. HaWiWe-hylsan är importerad från **Elaire** och är avsedd för Makita RT700C / RT0700CX3 / RT0701C m.fl.
   - https://hawiwe.de/produkt/makita_spannzange/
   - Elaire 1/8" Makita-style: produkt **MRP-1250**
   - https://elairecorp.com/product-category/makita-style-router-collets/
2. VEVOR:s exakta VV-1B-220V har 65 mm kropp; VEVOR anger i sin produktfamilj att den kan ersätta Makita RT0700.
   - https://eur.vevor.com/compact-router-c_10131/vevor-electric-hand-trimmer-palm-router-with-three-collets-and-fixed-base-710w-p_010376710625
3. Praktiskt V1E/CNC-fall: en användare kör **VEVOR 0700C (Makita 700-klon)** med 1/8" Makita-style/Sienci-collet i VEVOR:s originalmutter och rapporterar mycket liten runout.
   - https://forum.v1e.com/t/crappy-router-collet/50663/8

Det saknas däremot ett explicit datablad från VEVOR/Elaire som säger “MRP-1250 passar VV-1B-220V”. Därför ska den provpassas före drift och runout kontrolleras med ett rakt 1/8"-verktyg.

## Bord / fasta delar

Fortfarande kvar:
- bord/underrede
- plan bordsskiva / spoilboard
- material till permanenta strut plates, max 6,35 mm
- kabelinfästning/buntband

## Valfritt senare

- dammsugarslang / spånutsug
- slangjordning vid behov
- touch plate

## Ska inte köpas ännu

- GT2-remlängd före att slutmåtten är låsta i LR4-kalkylatorn
- extra 1/8"-spännhylsa
- prestandauppgraderingar innan standardmaskinen fungerar
