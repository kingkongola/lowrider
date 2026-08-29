# BOM

Här ska bara delar för den LowRider V4 som faktiskt byggs finnas.

## Inköpsförutsättning

- [x] **Amazon Prime-medlemskap** — räkna alltid Amazon Prime-frakt när vi jämför totalpris.

## Redan köpt — HaWiWe, 29 augusti 2026

Ordertotal: **165,50 € inklusive 8,00 € frakt**.

- [x] Aluminium XZ plates — **39,50 €**
- [x] Linear rail set LowRider 4 — **57,00 €**
- [x] Screw set LowRider 4 — **32,00 €**
- [x] Makita 1/8 inch (3,175 mm) collet — **29,00 €**
- [x] Frakt — **8,00 €**

## Kvar till själva LR4-maskinen

Utgår från V1E:s aktuella officiella LR4-BOM och räknar bort sådant som redan köpts ovan. PLA/printmaterial och stålrör hanteras separat och listas inte här.

- [ ] 1 × styrkort med minst 5 drivare
- [ ] 5 × NEMA17-stegmotorer, ca 59 Ncm / 84 oz-in, 5 mm axel, axel minst 20 mm
- [ ] 3 × stepper wire extenders / förlängningskablage
- [ ] 3 × GT2 10 mm, 16T remhjul
- [ ] 6 × GT2 10 mm, 20T släta idlers, 5 mm hål
- [ ] GT2 10 mm rem — exakt längd från LR4-kalkylatorn
- [ ] 5 × ändlägesbrytare + kablage/kontakter
- [ ] 14 × 608-2RS lager
- [ ] 2 × T8 trapetsskruv + mutter, minst 145 mm, 4-start / 2 mm pitch / 8 mm per varv
- [ ] 2 × koppling 5 mm → 8 mm
- [ ] 1 × nätaggregat, 24 V, minst 36 W
- [ ] gänglåsning för remhjulens stoppskruvar
- [ ] lätt smörjmedel till idlers/linjärskenor

## Aktuell inköpskandidat — research 29 augusti 2026

Målet är låg totalkostnad inklusive frakt, utan att dumsnåla, och helst få beställningar.

### Amazon.se / Prime — stark kandidat för smådelar + motorer

- STEPPERONLINE 5-pack NEMA17, **59 Ncm / 84 oz-in, 2 A, 1 m kabel** — omkring **608 kr** vid kontroll. Detta matchar momentet i V1E:s eget LR4-kit (84 oz-in) och är därför förstahandsval framför billigare svagare motorer.
- 5 × TMC2209 finns omkring 300–370 kr om SKR Pro väljs.
- 5→8 mm kopplingar och diverse GT2/kablage finns billigt och Prime kan göra samlad Amazon-order ekonomiskt attraktiv.

**Viktigt:** kontrollera Prime/frakt och aktuell säljare i kassan innan köp; sökresultat garanterar inte att varje artikel har Prime.

### Styrkort

V1E:s dokumentation har färdig LR-firmware för **BIGTREETECH SKR Pro V1.1/V1.2 + TMC2209**, och rekommenderar 5-driver-kort för LR4. Det är därför ett låg-risk-val om det hittas till bra totalpris. Undvik att köpa ett billigare 4-driver-kort — LR4 behöver fem individuellt drivna motorer för standard dual-endstop-upplägget.

### Nätaggregat

V1E:s BOM kräver minst 36 W och deras eget LR4-kit använder **24 V**. 24 V / 2.5 A (60 W) är beprövat i V1E-kitet och räcker; köp inte ett stort 350 W-aggregat bara för att summera motorernas märkström — stepperdrivarna fungerar inte så från nätaggregatets sida.

### Router

**Makita RT0702C** är målet eftersom den köpta 3,175 mm-spännhylsan är för Makita 700-serien. Prisresearch 29/8:
- Prisjakt: ca **1 532 kr** lägsta observerade pris
- Proshop: **1 657 kr inklusive fri frakt**
- CS Megastore: **1 626 kr inklusive fri frakt** vid kontroll

Köp separat från billig svensk/EU-butik om Amazon inte slår totalpriset; det finns ingen anledning att betala extra bara för att minska antalet paket.

## Verktyg / för att kunna fräsa

- [ ] Makita RT0702C
- [ ] minst 1 × 1/8" / ca 3,175 mm single-flute frässtål för första körningarna och strut plates

## Maskinens bord / fasta delar

- [ ] bord/underrede
- [ ] plan bordsskiva / spoilboard
- [ ] material till permanenta strut plates, max 6,35 mm
- [ ] trä-/plåtskruv för att fästa maskindelar i bordet
- [ ] buntband eller annan enkel kabelinfästning

## Praktiskt men inte nödvändigt för första rörelsen

- [ ] dammsugarslang / spånutsug
- [ ] jordning av dammsugarslang om slanglösningen kan bygga statisk elektricitet
- [ ] touch plate / verktygslängdsgivare — valfritt

## Redan täckt av HaWiWe-köpet

- [x] XZ-plattor
- [x] 4 × MGN12H 150 mm linjärskenor (linear rail set)
- [x] LR4-skruv/mutter-set
- [x] Makita 3,175 mm-spännhylsa
