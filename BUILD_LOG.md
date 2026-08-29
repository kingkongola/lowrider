# Build log

## 2026-08-29 — initial design/procurement pass

- Privat GitHub-repo skapat för LowRider V4-bygget.
- Maskinvalet avslutat: **LowRider V4 ska byggas**.
- HaWiWe-order lagd och **betald**, totalt **165,50 € inklusive 8,00 € frakt**:
  - Aluminium XZ plates — 39,50 €
  - Linear rail set LowRider 4 — 57,00 €
  - Screw set LowRider 4 — 32,00 €
  - Makita/Elaire 1/8" collet — 29,00 €
- Arbetsytan låst till **650 × 1250 mm** med aktuell V1E-kalkylator och köpta 6,0 mm XZ-plattor.
- Exakt geometri dokumenterad:
  - rör 816 / 816 / 1505 mm
  - strut-input 819 mm
  - GT2 999 / 1705 / 1705 mm, totalt 4409 mm
  - minimum bord 941 × 1563 mm
  - praktisk CNC-deck ~1000 × 1620 mm
- Jackpot3 valt.
- Routerspår: **VEVOR 0700C 800 W, 65 mm**.
- PSU/endstops: **Mean Well HDR-60-24 + Omron SS-3GL13PT**.
- Dammhantering satt som grundkrav.
- Laser skjuten till tidigast 2027; plasma utanför nuvarande scope.

## 2026-08-29 — oberoende system-/fysisk audit

En andra pass genomfördes med annan uppgift än första researchen: försök falsifiera planen och kontrollera att delsystemen faktiskt går ihop i en fysisk LR4.

### Grund som överlevde audit utan omtag

- LowRider V4
- 650 ×1250 arbetsyta
- 816 / 816 / 1505 mm rörgeometri
- 819 mm strut-input
- 999 / 1705 / 1705 mm GT2
- Ø30×1,5 mm stålrails
- StepperOnline `17HS19-2004S1`
- Jackpot3
- Mean Well HDR-60-24
- Omron SS-3GL13PT
- VEVOR 0700C-spåret, med kvarstående fysisk collet/runout-gate
- reuse-first DeWalt dust extraction

### Konkreta fel/luckor som hittades och korrigerades

1. **~1 m 24 V-kabel var fel sak att låsa.** HDR sitter fast på bordet men Jackpot rör sig med beam/gantry. Ändrat till 3 m inköpsmarginal + slutlig kapning först efter full-travel dry-fit.
2. **Egen LV-kabelgenomföring saknades.** De två M20 går åt till nät in/ut; 24 V får separat dimensionerad genomföring.
3. **Printdiameter var för implicit.** Alla diameterberoende delar låsta till **30 mm-variant**.
4. **Strut-generatorn saknade wing-parametern.** Låst till `strut_length=819`, `front_wing_size=30`.
5. **90 cm bord var geometriskt rätt men kantlasten var odokumenterad.** ~50 mm decköverhäng ska lokalt stödjas/fästas i LR4:s rail/wheel/belt-clip-zon.
6. **Routerkabelns rörelse saknades som gate.** Slang + 24 V + router + stepper/endstop ska nu full-travel-testas tillsammans före slutlig kabelinfästning.
7. **KJD12 kallades för säkert "nödstopp" för starkt.** Ny terminologi: NVR/maskinstopp med röd stoppkåpa; safety-rated E-stop-status ej verifierad.
8. **Statisk jordning hade ingen färdig definierad slutpunkt.** Det är nu blockerande gate före XPS/reguljär dammig drift; HDR är Class II och inte jordpunkt.
9. **Elecrow Jackpot3-flashning var inte explicit i byggordningen.** Nu gate före driven rörelse/homing.
10. **Toppnivåfiler hade driftat isär.** `README.md` och `SOURCING.md` hade kvar 608 som orphan och äldre bordssökkrav trots nyare `PROCUREMENT.md`. Canonical state reconcilerat.
11. Äldre geometry research hade kvar ett provisoriskt **32 mm** railmål trots nu låst 30 mm Motonet-spår. Researchfilen korrigerad.

### Repo uppdaterat

- nytt `AUDIT.md`
- `CHECKLIST.md` — fysiska build gates
- `TABLE.md` — verklig edge-support/load path
- `README.md` — aktuell state
- `SOURCING.md` — reconcilerad mot procurement
- `PROCUREMENT.md` — rörlig kabelintegration
- `BOM.md` — korrigerad fysisk BOM
- `DECISIONS.md` — nya auditbeslut D011–D013
- `research/2026-08-29-geometry-650x1250.md` — 30 mm-spåret reconcilerat

### Kvarvarande osäkerhet är nu av rätt typ

Följande ska **inte** avgöras genom mer skrivbordsresearch innan delarna finns:
- verklig Motonet-rördiameter/rakhet
- Elaire-collet i verklig VEVOR-kona + runout
- exakt KJD12-panel-/terminalvariant
- faktisk bordsvridstyvhet/kantstöd
- kabel-/slanglängder efter verklig komponentplacering

De är uttryckliga mät-/dry-fit-gates i `AUDIT.md` och `CHECKLIST.md`.