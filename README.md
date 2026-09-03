# LowRider V4

Det här repot är single source of truth för den LowRider V4 som faktiskt byggs.

## Aktuellt läge — 2026-09-03

- Maskin: **LowRider V4**. PrintNC/IndyMill är inte aktiva alternativ.
- Arbetsyta: **650 × 1250 mm**.
- Geometri: rör **816 / 816 / 1505 mm**, Ø30×1,5 mm; strut-input **819 mm**; GT2 **999 / 1705 / 1705 mm**; minimum bord **941 × 1563 mm**; praktisk deck cirka **1000 × 1620 mm**.
- HaWiWe-order: **betald 1 853 kr och skickad**. Ordervaluta 165,50 € inkl frakt. Innehåll: 6,0 mm XZ-plattor, 4 × MGN12H 150 mm, LR4 screw set och Makita/Elaire 1/8" collet.
- Controller: **Elecrow Jackpot3 `CQA240812C2` är köpt**, faktisk debitering **937 kr** inklusive DDP Economy.
- Faktiskt betalt hittills: **2 790 kr**. Se `COSTS.md`.
- Mekanikinköp: **Roboter-Bausatz och Allegro är blockerade av faktisk svensk checkout.** Aktiv väg är LaskaKit för idlers/T8/muttrar/couplers/5 m GT2 och HomeDIYer för exakt 3 × 16T/5mm/10mm; se `PROCUREMENT.md`.
- Printer: **Bambu Lab P1S**; alla diameterberoende LR4-printar ska vara **30 mm-variant**, tool mount **Makita/65 mm**.
- Router: **VEVOR 0700C**, 800 W, 65 mm.
- Filament: **3 × 1 kg eSUN PLA Basic Black 1,75 mm från 3DJake** är aktuell pris-/lagerbaseline: 444 kr varor + 115 kr svensk standardfrakt = **559 kr**.
- Bord: styvt begagnat **160–180 × helst 90–100 cm**, helst ≤700 kr, med avtagbar ~1000×1620 deck.
- Garagegrupp: **10 A**, praktiskt beprövad med svets; CNC är inte ett öppet elproblem om säkringen faktiskt håller.
- Dammhantering är del av grundbygget.

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

1. Bygg LaskaKit-korgen enligt `PROCUREMENT.md`; välj Sverige i riktig checkout och stoppa om svensk adress inte accepteras.
2. Lägg 3 × exakt 16T/5mm/10mm från HomeDIYer; välj den exakta varianten och stoppa om svensk adress inte accepteras.
3. Lägg resterande huvudorder: DigiKey, StepperOnline Germany, VEVOR EU och 3DJake PLA. **Jackpot3 är redan köpt.**
4. Köp Motonet-rör först efter fysisk OD-/rakhetskontroll.
5. Hitta begagnat bord och gör rackingtest.
6. När HaWiWe kommer: kontrollera transportskada + fyra produktgrupper och provpassa M3×10 mot XZ/MGN.
7. Provprinta `Z_Stub` + `Z_Nut`, verifiera 30 mm/65 mm-varianter och printa full LR4-sats.
8. Bygg deck/spoilboard och montera mekanik.
9. Dry-fit elbox och kör full-travel kabel/slang-test innan slutlig kabelinfästning.
10. Flasha/configurera Jackpot3, jogga 1 mm i taget, home/square och gör första testfräsningen.

Bred komponentresearch ska inte återöppnas utan ett konkret pris-, lager-, kompatibilitets- eller integrationsproblem.
