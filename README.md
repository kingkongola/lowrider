# LowRider V4

Det här repot är single source of truth för den LowRider V4 som faktiskt byggs.

## Aktuellt läge — 2026-09-03

- Maskin: **LowRider V4**. PrintNC/IndyMill är inte aktiva alternativ.
- Arbetsyta: **650 × 1250 mm**.
- Geometri: rör **816 / 816 / 1505 mm**, Ø30×1,5 mm; strut-input **819 mm**; GT2 **999 / 1705 / 1705 mm**; minimum bord **941 × 1563 mm**; praktisk deck cirka **1000 × 1620 mm**.
- HaWiWe-order: **165,50 € betald och nu skickad**. Innehåll: 6,0 mm XZ-plattor, 4 × MGN12H 150 mm, LR4 screw set och Makita/Elaire 1/8" collet.
- Printer: **Bambu Lab P1S**; alla diameterberoende LR4-printar ska vara **30 mm-variant**, tool mount **Makita/65 mm**.
- Router: **VEVOR 0700C**, 800 W, 65 mm.
- Controller för aktivt inköp: **Elecrow Jackpot3 `CQA240812C2`**. Jackpot2 var tekniskt Pareto-val för router-only, men den aktiva köpvägen ändrades 2026-09-03 av ett konkret lager-/distributionsproblem; se `DECISIONS.md`.
- Bord: styvt begagnat **160–180 × helst 90–100 cm**, helst ≤700 kr, med avtagbar ~1000×1620 deck.
- Garagegrupp: **10 A**, praktiskt beprövad med svets; CNC är inte ett öppet elproblem om säkringen faktiskt håller.
- Dammhantering är del av grundbygget.

## Kanoniska filer

- `DECISIONS.md` — låsta beslut och explicita supersessions.
- `BOM.md` — exakt vad bygget behöver och vad som redan finns.
- `PROCUREMENT.md` — **enda kanoniska ordermatrisen**: vad som ska köpas var, aktuell snapshot och checkout-gates.
- `CHECKLIST.md` — nästa arbete i fysisk ordning.
- `AUDIT.md` — mekaniska/elektriska/fysiska gates; innehåller inte flyktiga priser.
- `SOURCING.md` — daterad sourcing-evidens och länkar; ska inte duplicera en alternativ BOM.
- `TABLE.md` — bord/deck.
- `BUILD_LOG.md` — historik; gamla val får finnas här som historik men är inte current state.
- `research/` — historisk evidens. Top-level-filerna ovan supersederar research vid konflikt.

## Aktuell arbetsordning

1. Lägg de fem externa huvudorderna enligt `PROCUREMENT.md`: Roboter-Bausatz, DigiKey, StepperOnline Germany, Elecrow Jackpot3 och VEVOR.
2. Köp **3 kg vanlig styv PLA** via billigaste verifierade Sverige/Prime/EU-väg; filamentmärket är inte låst.
3. Köp Motonet-rör först efter fysisk OD-/rakhetskontroll.
4. Hitta begagnat bord och gör rackingtest.
5. När HaWiWe kommer: kontrollera transportskada + fyra produktgrupper och provpassa M3×10 mot XZ/MGN.
6. Provprinta `Z_Stub` + `Z_Nut`, verifiera 30 mm/65 mm-varianter och printa full LR4-sats.
7. Bygg deck/spoilboard och montera mekanik.
8. Dry-fit elbox och kör full-travel kabel/slang-test innan slutlig kabelinfästning.
9. Flasha/configurera Jackpot3, jogga 1 mm i taget, home/square och gör första testfräsningen.

Bred komponentresearch ska inte återöppnas utan ett konkret pris-, lager-, kompatibilitets- eller integrationsproblem.