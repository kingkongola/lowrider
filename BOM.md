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
- strut-input 819 mm, `front_wing_size=10.8`
- GT2 999 + 1705 + 1705 = 4409 mm
- minimum ytterfootprint 941 × 1563 mm
- faktisk köpt bordsskiva: **1800 × 1000 mm**, **300 kr**. Bredd 1000 mm räcker för 941 mm minimumfootprint; ingen planerad 41 mm kantbreddning. Underredets status/styvhet måste kontrolleras.

## Sensorenhet: ändlägesbrytare (köpta 2026-11-09)

- [x] **10 × QUARKZMAN KW11-3Z-N, rullspak, COM/NO/NC**, Amazon.se, **92,94 kr visat för hela paketet**, Prime-frakt 0 kr. **Beräknad leverans lördag 2026-11-14; inte mottagna ännu.**
- [ ] **2 ×** installeras som separata lägesgivare för infälld och utfälld BLTouch-arm, med **separata mekaniska hårdstopp**. Hålavstånd/spakväg kräver verklig passningskontroll; monteringen är ännu inte godkänd.
- **Omron SS-3GL13PT från DigiKey reserveras som reservdelar till originalmaskinen**, inte till den nya sensorarmen. Se [ANDLAGEN.md](machine/delar/nollpunkt/ANDLAGEN.md) och [inköp](PROCUREMENT.md).

## Core-sensorer – beställt, ej mottaget (2026-11-08)

- [x] Beställt: **1 × Raspberry Pi Camera Module 3 Standard** (`41020240`), **1 × Pi Zero 2 WH** med stiftlist (`41022617`), **1 × 200 mm CSI 15↔22-pin kabel** (`41020808`). Orderrader och moms i [PROCUREMENT.md](PROCUREMENT.md). **[ ] Mottagning, kabelfrigång och fysisk provpassning återstår.**
- [x] Beställt: **1 × ADXL345** (`41016234`); ingen bestämd fysisk monteringsplats. **[ ] Mottagning återstår.**
- [x] **11 unika CAD-delar, 12 utskrifter inklusive 2 × KW11-hållare, i build123d**: [källa, separata STEP/STL, montage-GLB och grön CI](machine/delar/sensorer/README.md). BRep-kontroll av statiska delintersektioner och 7-läges servoarm/BLTouch-probattrapp godkänd 2026-11-09. **[ ] Fysiskt provprintad/monterad, servohorn/KW11-rullspak/hårdstopp och riktigt Core-/kjol-avstånd är EJ verifierade.** Äldre OpenSCAD-prototyp är arkiverad.
- [ ] Pi:s verkliga **5 V kraftmatning**: regulator, skydd och kabel väljs efter spännings-/last- och EMC-granskning; **inget antaget att detta redan finns**. Se [kopplingsunderlag](machine/delar/sensorer/KOPPLING_CORE_V0.md).
- **Ingen fläkt beställd eller kravsatt** för Pi: börja med passiv kylning och mät temperatur under stillbildsarbete. Uteslut inte framtida kylning om mätningar visar behov.
- **BLTouch** och **SPMS664** har separat tidigare inköps-/designhistorik. Exakt probrevision och mått måste verifieras mot levererad del; inga pinnar är nya tilldelade.

## Servoarmens ändlägesgivare – bestämd princip 2026-11-08

- [x] 10 × Omron/Aratas `SS-3GL13PT` köpta i DigiKey-order 2026-09-03. Originalmaskinen har använt Omron; **kvarvarande Omron ska behållas som LowRider-reserv** och inte förbrukas på sensorenheten. Inventera bara vid behov.
- Servoarmen använder **inga brytare** enligt [D020](DECISIONS.md): hårda stopp, magnet i parkerat läge och kamerakontroll. De 10 köpta QUARKZMAN KW11-3Z-N är reservdelar.
- [x] **Neodymmagneter Ø6 x 3 mm** (Vinabo, 60 st, köpta 2026-10-27 enligt användaren) till armens parkeringsstopp.
- [x] **M3-skruv av stål** till armens parkeringsstopp, finns hemma enligt användaren. Sensorenheten använder också M3 x 10 till kameraklämningen (2 st), ADXL345 (2 st), BLTouch-hylsan (2 st) och sidopanelen (6 st). Inga M2-skruvar behövs.
- [x] **LM2596 DC-DC-moduler** (Zuahaly, 10 st, köpta 2026-10-28 enligt användaren) som regulatorer i sidotornet: två stycken, 24→5,1 V till Pi och BLTouch och 24→6,0 V till servot.

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
- [ ] printad cyklon först: vald modell eifelbiker (med inbyggd undertrycksventil), 30 l lockfat som behållare; mutterinsatser M3x4/M5x5,8, skruvar M3x25/M5x12/M5x25/M4x35 och fjäder 0,5×6×20 mm ska kontrolleras mot lager
- [ ] styv 15–30 l behållare och kontrollerat vakuumtest
- [x] **Befintlig poolslang 4 meter, ID 46 mm (uppmätt 2026-10-14)** – redan ägd; användaren har tidigare kopplat den till DeWalt för rengöring av FTX-kanalerna. DeWalt-originalslangen är för kort. **Inget nytt slanginköp planeras.** Återstår: kontrollera faktisk ID/OD och följsamhet/räckvidd genom full X/Y/Z-rörelse, skapa adapter till Makita-dammsko (och eventuellt DeWalt om behövs), upphängning/dragavlastning. Poolslang är normalt inte antistatisk; utred säker statisk hantering vid användning med trä/MDF, utan att likställa utvändig tråd med antistatisk slang.
- [ ] slangupphängning/dragavlastning
- [ ] verifierad statisk jordväg före XPS/reguljär trä/MDF-drift

## LED och övervakningsmatning – aktuellt 2026-11-10

- **Vald:** BRIMETI COB LED-list 5 m / 24 V / 4000 K / 320 LED/m, angivet 10 W/m och 100 lm/W. Användaren anger **145 kr**. **Betalning/mottagning är inte verifierad**; för inte upp som debiterad i `COSTS.md` utan bekräftelse.
- **Befintligt:** Mean Well HDR-60-24 **24 V / 60 W** för Jackpot3/stegmotorer, 10 × LM2596 buck, möjlig 150 W-laptopladdare (utspänning obekräftad), möjlig 24 V-elsparkcykelladdare (verklig output obekräftad). Klippt Altec Lansing 17 V-kabel är inte aktuell som LED-matning.
- **Behov, ej köpt:** verifierad och separat övervakningsmatning till Pi/kamera utanför maskinstoppets brytna matningsgren, LED-matning efter faktisk installerad längd och kylning. Inga nya boost/PSU eller Shelly-reläer beställda genom denna plan.
- **Fästen, ej klara:** tre LED-remseriktningar under X-strut: **1 ned, 2 fram**; aluminium för värmeavledning och justerbara, utskrivbara hållare utreds. Befintliga forum-STL är inte verifierade för tre remsor/vår geometri. Ingen ny printklar STL har tagits fram.
- **Kanoniskt kravläge, effektbudget, stoppberoenden och nästa tester:** [`machine/EL_BELYSNING_OCH_STOPP.md`](machine/EL_BELYSNING_OCH_STOPP.md). Mjukvarans stoppolicy: [`cnc/docs/verktygsovervakning.md`](https://github.com/kingkongola/cnc/blob/main/docs/verktygsovervakning.md).

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
