# BOM

Den här filen innehåller endast delar för den LowRider V4 som faktiskt byggs. Flyktiga priser/lager finns i `PROCUREMENT.md`; faktisk kostnad finns i `COSTS.md`.

## Redan köpt — HaWiWe

**Betald 2026-08-29: faktiskt debiterat 1 853 kr. Ordervaluta 165,50 € inklusive 8,00 € frakt. Skickad 2026-09-03.**

- [x] Aluminium XZ plates, 6,0 mm
- [x] 4 × MGN12H 150 mm linear rails
- [x] LR4 screw set:
  - 14 × M8×40 + 14 × M8 nyloc
  - 60 × M5×30 + 60 × M5 nyloc
  - 83 × M3×10
  - 10 × M2.5×12
- [x] Makita/Elaire 1/8" / 3,175 mm collet

## Redan köpt — Elecrow

**Betald 2026-09-03: faktiskt debiterat 937 kr. Checkout 83,55 € inklusive DDP Economy.**

- [x] Jackpot3 CNC Controller `CQA240812C2`

## Redan ägt

- [x] Bambu Lab P1S
- [x] DeWalt wet/dry shop-vac; exakt modell/typskylt ska bekräftas före modellunika antaganden
- [x] TPU-filament; kontrollera hårdhet före dust-shoe-bristles
- [x] Threadlocker
- [x] äldre FTX-aggregat; endast kandidat som sekundär filtrering/undertryck

## Låst geometri

- arbetsyta 650 × 1250 mm
- X-rör 816 mm ×2
- Y-rör 1505 mm
- Ø30×1,5 mm
- strut-input 819 mm, `front_wing_size=30`
- GT2 999 + 1705 + 1705 = 4409 mm
- minimum bord 941 × 1563 mm
- deck cirka 1000×1620 mm

## Kvar — mekanik

- [ ] 2 × Motonet `88-7123`, Ø30×1,5×2000 mm stålrör; fysisk OD/rakhet före kapning
- [ ] 6 × Roboter-Bausatz `RBS12910`, smooth idler, 5 mm hål, 10 mm rem
- [ ] 1 × `RBS12872`, T8×8 400 mm + brass nut
- [ ] 1 × `RBS12749`, extra T8×8 brass nut
- [ ] 2 × `RBS10595`, flexible coupler 5→8 mm
- [ ] 5 m × `RBS12747`, GT2/2 mm, 10 mm, gummi + glasfiber, meterware
- [ ] 3 × `RBS12867`, GT2 16T / 5 mm / 10 mm
- [ ] 16 × exact 608-2RS 8×22×7 mm; 14 installeras + 2 reserv
- [ ] senaste LR4-printar i 30 mm-variant
- [ ] Makita/65 mm tool mount
- [ ] cirka 2,7 kg vanlig styv PLA; köp **3 kg**, inte 6 kg
- [ ] material till permanenta struts, 5–6 mm MDF/hardboard, max 6,35 mm
- [ ] rail/belt/table-infästning enligt faktisk deck

## Kvar — motorer/styrning/lågspänning

- [x] Elecrow Jackpot3 `CQA240812C2`
- [ ] 1 × StepperOnline fempack `5-17HS19-2004S1`
- [ ] Mean Well `HDR-60-24`
- [ ] 10 × Omron `SS-3GL13PT`
- [ ] 3 m Tensility `30-00416`, 2×20 AWG, för fast HDR-box → rörlig Jackpot
- [ ] 10 m Tensility `30-00377`, 3×26 AWG, för endstops
- [ ] 1 × Amphenol `AIO-CSM12`, M12 / 3–6,5 mm / IP68
- [ ] 2-poliga board-side endstopkontakter/pigtails
- [ ] stepperextensioner endast om dry-fit visar behov
- [ ] data-USB-C: inventera först
- [ ] microSD >2 GB FAT32: inventera först

## DigiKey-el/smådelar

- [ ] 3 × genuine Wago `221-413`
- [ ] 2 × Altech `5309 720/SET`, M20×1.5 / 5–12 mm
- [ ] 10 × TE `3-350820-2` via **`A27824-ND`**, inte Marketplace-dubblett

## 230 V / NVR

Baseline: `vägg -> NVR -> [HDR-60-24 + DeWalt AUTO]`, `VEVOR -> DeWalt tool socket` om DeWalt-typskylten bekräftar rätt funktion.

- [ ] KJD12-familj NVR, 230 V, minst lämplig märkström; Clas Ohlson 50-2929 230 V/10 A är aktiv enkel kandidat
- [ ] kapsling först efter fysisk NVR/HDR dry-fit
- [ ] jordad 3G1,5 donor lead om faktisk rutt kräver det
- [ ] PE kontinuerlig/oswitchad

## Router / första skär

- [ ] VEVOR 0700C, SKU `YXKXBJ710W65AH7WLV2`, 220–240 V, 800 W, 65 mm
- [ ] provpassa Elaire-collet och kontrollera säte/runout
- [ ] commissioning-fräs `L1S.M.0317` eller motsvarande 3,175 mm single-flute upcut först när första fräsjobbet närmar sig; separat Sorotec-order är fortfarande uppskjuten
- [ ] lång 3,175 mm plywoodfräs först vid verkligt 18–19 mm jobb

## Bord/deck

- [ ] styvt begagnat bord 160–180 × helst 90–100 cm, helst ≤700 kr
- [ ] avtagbar ~1000×1620 deck, 11 mm OSB value default eller ~12 mm konstruktionsplywood
- [ ] ~12 mm löstagbar MDF-spoilboard
- [ ] lokal kantblockning/infästning om 90 cm bord ger ~50 mm överhäng

## Damm

- [ ] LR4 dust shoe för Makita/65 mm
- [ ] TPU-bristles om befintlig TPU är lämplig
- [ ] printad cyklon först
- [ ] styv 15–30 l behållare och kontrollerat vakuumtest
- [ ] testa befintlig DeWalt-slang före ny slang
- [ ] slangupphängning/dragavlastning
- [ ] verifierad statisk jordväg före XPS/reguljär trä/MDF-drift

## Köp inte ännu

- T-track/vacuum-table
- routerförlängning
- stepperextensioner
- extra collet
- controllerfläkt
- ny shop-vac/slang
- lång plywoodfräs
- microSD/USB-C innan inventering
