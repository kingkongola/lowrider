# LowRider V4

Det här repot är single source of truth för den LowRider V4 som faktiskt byggs.

## Aktuellt läge — 2026-09-19

- Maskin: **LowRider V4**. PrintNC/IndyMill är inte aktiva alternativ.
- Arbetsyta: **650 × 1250 mm**.
- Geometri: rör **816 / 816 / 1505 mm**, Ø30×1,5 mm; strut-input **819 mm**; GT2 **999 / 1705 / 1705 mm**; minimum bord **941 × 1563 mm**; praktisk deck cirka **1000 × 1620 mm**.
- HaWiWe-order: **betald 1 853 kr och skickad**. Ordervaluta 165,50 € inkl frakt. Innehåll: 6,0 mm XZ-plattor, 4 × MGN12H 150 mm, LR4 screw set och Makita/Elaire 1/8" collet.
- Controller: **Elecrow Jackpot3 `CQA240812C2` är mottagen**, faktisk debitering **937 kr** inklusive DDP Economy.
- Drive pulleys: **3 × GT2/2GT 16T / 5 mm bore / 10 mm belt är köpta via eBay/POWGE**, faktisk debitering **72 kr**, fri frakt och importavgifter inkluderade i eBay-köpet.
- LaskaKit-mekanikkärna: **köpt för 444 kr** inklusive GLS Sweden. Innehåll: 6 smooth idlers, T8×8 400 mm, 2 × 5→8-koppling och 5 m GT2 10 mm glasfiber. **De två T8×8-mässingsmuttrarna var slut och återstår separat.**
- Faktiskt betalt hittills: **3 306 kr**. Se `COSTS.md`.
- Mekanikinköp: **Roboter-Bausatz och Allegro är blockerade av faktisk svensk checkout.** DMW-spåret ersattes av eBay/POWGE. LaskaKit är nu stängd; återstående lilla mekanikorphan är **2 × T8×8 brass nut, 4-start / 8 mm lead**.
- Printer: **Bambu Lab P1S**; alla diameterberoende LR4-printar ska vara **30 mm-variant**, tool mount **Makita/65 mm**.
- Router: **VEVOR 0700C**, 800 W, 65 mm.
- Filament: **3 × 1 kg eSUN PLA Basic Black 1,75 mm från 3DJake** är aktuell pris-/lagerbaseline: 444 kr varor + 115 kr svensk standardfrakt = **559 kr**.
- Bord: **180×100 cm bordsskiva köpt för 300 kr**; ingen planerad 90 cm-kantbreddning, kontrollera underrede. Löstagbar ~12 mm MDF-spoilboard köps senare.
- Garagegrupp: **10 A**, praktiskt beprövad med svets; CNC är inte ett öppet elproblem om säkringen faktiskt håller.
- Dammhantering är del av grundbygget.
- Prints: **platta 10 av 14 pågår** enligt användaren 2026-09-19.
- 3 × 16T-remhjul från eBay/POWGE är **köpta men ännu inte mottagna** 2026-09-19 (senaste LMC-skanning 12 sep).
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
- `research/` — historisk evidens. Top-level-filerna ovan supersederar research vid konflikt.

## Aktuell arbetsordning

1. Fortsätt printa resterande LR4-plattor; verifiera 30 mm-rördelar, Makita/65 mm tool mount samt **4 × temporära struts (15 % infill)**.
2. Kontrollera köpta 180×100-skivans underrede/styvhet och provlägg rail/belt-layout. Mät/kapa rör efter OD-/rakhetskontroll.
3. Inventera HaWiWe, DigiKey och el-/kabeldelar mot BOM. Avvakta leverans av redan köpta 16T-remhjul (köp inte dubbelt).
4. Köp/ordna ~12 mm MDF-spoilboard, 5–6 mm strutmaterial, första 3,175 mm-fräs samt NVR/kapsling efter fysisk dry-fit.
5. Montera maskinen med temporära struts, konfigurera Jackpot3, torrkör och fräs permanenta struts (`819`, `front_wing_size=30`) med maskinen själv.
6. Byt till permanenta struts, gör full-travel-test för kablar/slang, färdigställ dammhantering och planfräs offerskivan.

Bred komponentresearch ska inte återöppnas utan ett konkret pris-, lager-, kompatibilitets- eller integrationsproblem.
