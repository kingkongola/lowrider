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

- [x] Jackpot3 CNC Controller `CQA240812C2`

## Redan köpt — eBay / POWGE

- [x] 3 × GT2/2GT drive pulley, **16T / 5 mm bore / för 10 mm belt / 2 mm pitch**

## Redan köpt — LaskaKit

- [x] 6 × smooth GT2 idler, 5 mm hål/bearing, för 10 mm rem — `LA190008E`
- [x] 1 × T8×8 400 mm, 4-start / 8 mm lead — `LA190032A`
- [x] 2 × flexible coupler 5→8 mm — `LA190031`
- [x] 1 × 5 m GT2/2 mm, 10 mm, glasfiberförstärkt — `LA190013C`

## eBay / HKGY01 — annullering väntar

Ordern på 2 × T8×8-mässingsmuttrar är inte längre aktiv; ersatt av Amazon/euroharry.

## Redan mottaget — Amazon.se / euroharry

**Mottaget 2026-09-10.**

- [x] 4 × flänsad T8 brass nut, **Ø8 mm / 2 mm pitch / 4-start / 8 mm lead**; 2 används + 2 reserv

## Redan köpt — DigiKey

- [x] 1 × Mean Well `HDR-60-24`
- [x] 10 × Omron/Aratas `SS-3GL13PT`
- [x] 16 × 608-2RS 8×22×7 mm
- [x] 3 × Wago `221-413`
- [x] 2 × Altech `5309 720/SET`, M20 / 5–12 mm
- [x] 10 × TE `3-350820-2`
- [x] 1 × Amphenol `AIO-CSM12`, M12 / 3–6,5 mm
- [x] 3 m Tensility `30-00416`, 2×20 AWG
- [x] 10 m Tensility `30-00377`, 3×26 AWG
- [x] 3 × Molex KK 2,54 mm 2-polig 150 mm cable assembly `2177961021`

## Redan köpt — Amazon.se

- [x] 5 × STEPPERONLINE `17HS19-2004S1`, **59 Ncm / 84 oz-in, 2,0 A, 42×42×48 mm, Ø5 mm D-axel, 1 m kabel**
- [x] KATSU `101750`, 220–240 V, 710 W, variabelt varvtal, cirka 64,8/65 mm motorhus

## Redan köpt — PrintOnion

- [x] 3 kg vanlig styv PLA 1,75 mm för LR4-printarna — **426 kr**

## Redan köpt — Motonet

**Köpt 2026-09-07: 2 rör för totalt 340 kr.**

- [x] 2 × stålrör för LR4, planerad spec `88-7123`, **Ø30×1,5×2000 mm**
- [ ] verifiera faktisk OD/rakhet/längd före kapning

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
- minimum ytterfootprint 941 × 1563 mm
- huvudmål bord: **1800 × 900 mm**, med lokal breddning eftersom 900 mm är cirka 41 mm smalare än minimumfootprint

## Kvar — mekanik

- [ ] senaste LR4-printar i 30 mm-variant
- [ ] Makita/65 mm tool mount
- [ ] material till permanenta struts, 5–6 mm MDF/hardboard, max 6,35 mm
- [ ] rail/belt/table-infästning och smal lokal kantbreddning enligt faktisk 180×90-bordsskiva

## Kvar — motorer/styrning/lågspänning

- [x] Elecrow Jackpot3 `CQA240812C2`
- [x] 5 × STEPPERONLINE `17HS19-2004S1`
- [x] Mean Well `HDR-60-24`
- [x] 10 × Omron `SS-3GL13PT`
- [x] lågspänningskablage/glands/pigtails enligt DigiKey-order
- [ ] stepperextensioner endast om dry-fit visar behov
- [ ] data-USB-C: inventera först
- [ ] microSD >2 GB FAT32: inventera först

## 230 V / NVR

- [ ] KJD12-familj NVR, 230 V; Clas Ohlson 50-2929 är aktiv kandidat
- [ ] kapsling först efter fysisk NVR/HDR dry-fit
- [ ] jordad 3G1,5 donor lead om faktisk rutt kräver det
- [ ] PE kontinuerlig/oswitchad

## Router / första skär

- [x] KATSU `101750`
- [ ] provpassa Elaire/Makita-style 1/8"-collet och kontrollera runout
- [ ] commissioning-fräs `L1S.M.0317` eller motsvarande 3,175 mm single-flute upcut när första fräsjobbet närmar sig

## Bord / spoilboard

- [ ] styvt begagnat **180×90 cm** bord, helst ≤700 kr; 180×100 cm är jackpot
- [ ] använd bordets befintliga skiva direkt som strukturell maskinbas
- [ ] bygg endast smal lokal kantbreddning/rail-support för den cirka 41 mm totala breddbristen på 90 cm bord
- [ ] ~12 mm löstagbar MDF-spoilboard över arbetszonen

## Damm

- [ ] LR4 dust shoe för Makita/65 mm
- [ ] TPU-bristles om befintlig TPU är lämplig
- [ ] printad cyklon först
- [ ] styv 15–30 l behållare och kontrollerat vakuumtest
- [ ] testa befintlig DeWalt-slang före ny slang
- [ ] slangupphängning/dragavlastning
- [ ] verifierad statisk jordväg före XPS/reguljär trä/MDF-drift

## Köp inte ännu

- hel OSB/ply-deck om inte det verkliga bordet visar konkret behov
- T-track/vacuum-table
- routerförlängning
- stepperextensioner
- extra collet
- controllerfläkt
- ny shop-vac/slang
- lång plywoodfräs
- microSD/USB-C innan inventering
