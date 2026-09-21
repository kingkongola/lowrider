# LowRider V4

Det här repot är single source of truth för den LowRider V4 som faktiskt byggs.

## Aktuellt läge — 2026-09-21

- Maskin: **LowRider V4**. PrintNC/IndyMill är inte aktiva alternativ.
- Arbetsyta: **650 × 1250 mm**.
- Geometri: rör **816 / 816 / 1505 mm**, Ø30×1,5 mm; strut-input **819 mm**; GT2 **999 / 1705 / 1705 mm**; minimum bord **941 × 1563 mm**; praktisk deck cirka **1000 × 1620 mm**.
- HaWiWe-order: **betald 1 853 kr och mottagen**, enligt användarens uppgifter. Ordervaluta 165,50 € inkl frakt. Innehåll: 6,0 mm XZ-plattor, 4 × MGN12H 150 mm, LR4 screw set och Makita/Elaire 1/8" collet.
- Controller: **Elecrow Jackpot3 `CQA240812C2` är mottagen**, faktisk debitering **937 kr** inklusive DDP Economy.
- Drive pulleys: **3 × GT2/2GT 16T / 5 mm bore / 10 mm belt är köpta via eBay/POWGE**, faktisk debitering **72 kr**, fri frakt och importavgifter inkluderade i eBay-köpet.
- LaskaKit-mekanikkärna: **mottagen**, 444 kr. Innehåll: 6 smooth idlers, T8×8 400 mm, 2 × 5→8-koppling och 5 m GT2 10 mm glasfiber. **4 × ersättnings-T8×8-mässingsmuttrar från Amazon är mottagna** (2 används + 2 reserv).
- Faktiskt betalt inklusive bordsskivan: **6 756,11 kr brutto**; **6 689,11 kr** exklusive 67 kr annullerad eBay-order som väntar återbetalning. Se `COSTS.md`.
- Mekanikinköp: grundmekaniken inklusive **3 × eBay/POWGE 16T-remhjul är mottagen**. Verifiera fysisk passning och antal mot beställningsspec innan montering. Köp inte T8-muttrar igen.
- Printer: **Bambu Lab P1S**; alla diameterberoende LR4-printar ska vara **30 mm-variant**, tool mount **Makita/65 mm**.
- Router: **KATSU 101750**, 710 W, cirka 65 mm; köpt.
- Filament: **3 kg PLA från PrintOnion** för 426 kr; utskrifterna är igång.
- Bord: **180×100 cm bordsskiva köpt för 300 kr**; ingen planerad 90 cm-kantbreddning, kontrollera underrede. Löstagbar ~12 mm MDF-spoilboard köps senare.
- Garagegrupp: **10 A**, praktiskt beprövad med svets; CNC är inte ett öppet elproblem om säkringen faktiskt håller.
- Dammhantering är del av grundbygget.
- Prints: användaren har rapporterat utskrift av **platta 14/14** samt att **hela Core är omprintad utan tidigare 0,20 mm förskjutning**. Den tidigare defekta Core används inte. **Det är inte bekräftat att det separata Makita/65 mm-verktygsfästet (eller Jackpot3-boxen) ingick i dessa plattor.** Se LR-00 och inventera utskrifterna före Core-montage.
- 3 × 16T-remhjul från eBay/POWGE: **mottagna 2026-09-21** enligt användaren; antal och tekniska mått kontrolleras under nästa inventering.
- Projektkostnad inklusive köpt bordsskiva: **6 756,11 kr brutto**, **6 689,11 kr** exklusive annullerad eBay-order på 67 kr som väntar återbetalning.

## Kanoniska filer

- `DECISIONS.md` — låsta beslut och explicita supersessions.
- `BOM.md` — exakt vad bygget behöver och vad som redan finns/köpts.
- `PROCUREMENT.md` — **enda kanoniska ordermatrisen** för kvarvarande köp.
- `COSTS.md` — **enda kanoniska kostnadsledgern**; faktiskt debiterade SEK-belopp.
- `CHECKLIST.md` — nästa arbete i fysisk ordning.
- `AUDIT.md` — mekaniska/elektriska/fysiska gates; innehåller inte flyktiga priser.
- `SOURCING.md` — daterad sourcing-evidens och länkar; ska inte duplicera en alternativ BOM.
- `TABLE.md` — bord/deck.
- `BUILD_LOG.md` — historik; gamla val får finnas här som historik men är inte current state.
- `WORK_ORDERS.md` — arbetskort om cirka en timme, med beroenden och återrapportering; lokal webbsidestatus är inte SSOT.

## Monteringsguide

- [`docs/MONTERING_SV.md`](docs/MONTERING_SV.md) — svensk, utökad monteringsguide för den faktiska LR4-konfigurationen med **Jackpot3**. Läs tillsammans med V1E:s originalbilder; guiden ersätter inte kanoniska beslut eller checklistan.
- [Publicerad guide och arbetsordrar](https://kingkongola.github.io/lowrider/) — originalbilder inline, 30 entimmespass och kopierbar återrapport. Lokal status på webbplatsen synkas inte automatiskt med repot.
- `research/` — historisk evidens. Top-level-filerna ovan supersederar research vid konflikt.

## Aktuell arbetsordning

1. Inventera utskrivna LR4-delar. **Kontrollera explicit om det separat nedladdade Makita 701/65 mm-verktygsfästet finns; vid frånvaro skriv ut det enligt LR-00.** Verifiera även 30 mm-varianter, rätt Jackpot3-box och **4 × temporära struts (15 % infill)**. Platta 14/14 innebär inte att separat mount-set automatiskt ingick.
2. Kontrollera köpta 180×100-skivans underrede/styvhet och provlägg rail/belt-layout. Mät/kapa rör efter OD-/rakhetskontroll.
3. Inventera HaWiWe, DigiKey, remhjul och el-/kabeldelar mot BOM. Alla tre beställda 16T-remhjul är mottagna; kontrollera tänder/hål/rembredd före montering.
4. Köp/ordna ~12 mm MDF-spoilboard, 5–6 mm strutmaterial, första 3,175 mm-fräs samt NVR/kapsling efter fysisk dry-fit.
5. Montera maskinen med temporära struts, konfigurera Jackpot3, torrkör och fräs permanenta struts (`819`, `front_wing_size=30`) med maskinen själv.
6. Byt till permanenta struts, gör full-travel-test för kablar/slang, färdigställ dammhantering och planfräs offerskivan.

Bred komponentresearch ska inte återöppnas utan ett konkret pris-, lager-, kompatibilitets- eller integrationsproblem.
