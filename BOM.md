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

## Redan mottaget — Elecrow

**Mottaget 2026-09-18.**

- [x] Jackpot3 CNC Controller `CQA240812C2`

## Redan mottaget — eBay / POWGE

- [x] 3 × GT2/2GT drive pulley, **beställd specifikation 16T / 5 mm bore / för 10 mm belt / 2 mm pitch** — **mottagna 2026-09-21** enligt användaren. Kontroll av fysisk variant/passning återstår.

## Redan mottaget — LaskaKit

**Mottaget och inventerat komplett 2026-09-13.**

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
- [x] 10 m Tensility `30-00377`, 3×26 AWG, cirka Ø4 mm svart mantel. **PASSNINGSFEL: användaren har verifierat att manteln INTE går i Cores kabeltunnel.** Ingen extrabeställning ännu: bedöm lokal avmantling endast i tunneln (två individuellt isolerade ledare, avlastning/skavskydd) eller tunnare flexibel tvåledarkabel/yttre kabelväg; kontrollera YZ-kanaler också.
- [x] 3 × Molex KK 2,54 mm 2-polig 150 mm cable assembly `2177961021`

## Redan köpt — Amazon.se

- [x] 5 × STEPPERONLINE `17HS19-2004S1`, **59 Ncm / 84 oz-in, 2,0 A, 42×42×48 mm, Ø5 mm D-axel, 1 m kabel**. YZ_Max och Core förväntas kräva förlängningar; exakt längd efter full-travel dry-fit, se `CABLE_ROUTING.md`.
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
- faktisk köpt bordsskiva: **1800 × 1000 mm**, **300 kr**. Bredd 1000 mm räcker för 941 mm minimumfootprint; ingen planerad 41 mm kantbreddning. Underredets status/styvhet måste kontrolleras.

## Kvar — mekanik

- [ ] senaste LR4-printar i 30 mm-variant
- [ ] **Separat printat Makita/65 mm-verktygsfäste för KATSU 101750**, [V1E:s Makita 701 Tool Mount and Dust Shoe](https://www.printables.com/model/1033926-makita-701-tool-mount-and-dust-shoe-for-the-lowrid); **utskriftsstatus okänd**, inte bekräftat bland 14 plattor. Kontrollera rätt del/variant och passning; V1E anger 30 % infill i huvudtabellen. Ej samma sak som köpta 1/8-tumshylsan.
- [ ] **Separat Jackpot3 board box**, [V1E-modell](https://www.printables.com/model/1434650-jackpot3-box); utskriftsstatus okänd, inventera.
- [ ] material till permanenta struts, 5–6 mm MDF/hardboard, max 6,35 mm
- [ ] rail/belt/table-infästning på köpt 180×100-bordsskiva; kontrollera underrede och verklig layout före håltagning

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

- [x] **180×100 cm bordsskiva köpt för 300 kr** (rapporterat 2026-09-19)
- [ ] kontrollera att underredet är styvt och att bordsskivan kan bära LR4
- [ ] fäst rail/belt/table enligt faktisk layout; **ingen 90 cm-kantbreddning behövs**
- [ ] ~12 mm löstagbar MDF-spoilboard över arbetszonen

## Damm

- [ ] LR4 dust shoe för Makita/65 mm
- [ ] TPU-bristles om befintlig TPU är lämplig
- [ ] printad cyklon först
- [ ] styv 15–30 l behållare och kontrollerat vakuumtest
- [ ] **dammsugarslang för rörlig LowRider:** prova först befintlig DeWalt-slang. V1E:s Makita 701 LR4 dust shoe är avsedd för **högst 70 mm slangytterdiameter**, inte en obligatorisk 70 mm-slang. Om befintlig slang är för kort/styv, välj lätt flexibel slang och printa måttanpassad adapter efter mätning av slangens faktiska OD, DeWalt-anslutningen och dust-shoe-ingången. Längd/diameter/inköp ej verifierade, inget ännu beställt.
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
