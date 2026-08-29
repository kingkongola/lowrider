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

## 2026-08-30 — inköpsrad + commissioning-audit

Nästa auditpass gick igenom kvarvarande köp som en fysisk kedja: rätt del → passar grannkomponenten → går att montera/koppla → kan driftsättas utan dold saknad del.

### Huvudkomponenterna överlevde igen

Ingen anledning hittades att byta:
- Motonet Ø30×1,5-rör
- StepperOnline-motorerna
- GT2 16T / idlers / 10 mm fiberglass-rem
- 608-2RS
- T8×8 + 5→8-kopplingar
- HDR-60-24
- Omron-endstops
- Jackpot3
- VEVOR 0700C
- Sorotec `L1S.M.0317`
- grundarkitekturen för bord/damm/el

### Nya fynd

1. **T8 400 mm ska inte automatiskt halveras.** V1E kräver 145 mm+, så ~199 mm fungerar men ger bara onödigt utstick. Ny praktisk kapregel: cirka 150–160 mm ×2 efter verklig assembly-check.
2. **GT2 5 m har ren lagerfallback:** 3×2 m av samma 10 mm fiberglass-spec, eftersom 999/1705/1705 mm kan få varsin längd utan skarv.
3. **20 AWG UL2464 är inte dokumenterad continuous-flex.** Den används med stor avslappnad rörelseloop; krävs snäv kabelkedjeböj byts kabeltyp.
4. **2-core 20 AWG är nominellt ~4,8 mm OD.** Det bekräftar behovet av separat mindre gland; M20 nätglandens 5–12 mm är fel marginal för LV-kabeln.
5. **DigiKey fri frakt var för självsäkert bokförd.** 615 kr-gränsen är verifierad, men ~622 kr-korgen är en inkl-momsuppskattning och hjälpsidan klargör inte momsbasen. Checkout får avgöra.
6. **MicroSD saknades i vår commissioning-BOM.** Elecrow listar board + 5 tvåledarpluggar + 6 heatsinks, inte kort. V1E föredrar microSD för G-code: >2 GB, FAT32, Class 4–6. Inventera först, köp billigt endast om det saknas.
7. **Data-USB-C är en verklig dependency.** Elecrow-kortet måste flashas och V1E varnar specifikt för charge-only-kablar. Inventera före köp.
8. **Endstops är inte runtime limits som standard.** V1E säger att de bara är aktiva under homing. De är home/auto-square-sensorer, inte kollisionsskydd/nödstopp.
9. **Printmiljön blev en explicit gate.** Minst 200×200×190 mm byggvolym, skew-kontroll, `Z_Stub`/`Z_Nut` testfit och slicer bridge-preview innan hela 2,7 kg-satsen.
10. **Jackpot-kabeldragning/kylning förtydligad.** Board box, fri luftväg, kablar bredvid kortet/inte över antennen och avlastade anslutningar. Ingen fläkt köps utan behov.
11. **Motorcommissioning förtydligad.** 2,54 mm-kontakterna passar Jackpot3; coil/connector-riktning verifieras och eventuell pluggreversering sker endast spänningslöst.

### Canonical state uppdaterat

- `AUDIT.md` — andra auditpasset, fynd 11–20
- `PROCUREMENT.md` — checkout-/microSD-/USB-/T8-/belt-/flexkabelkorrigeringar
- `BOM.md` — commissioning-dependencies och print-gates
- `CHECKLIST.md` — fysisk exekveringsordning
- `SOURCING.md` — bort med antagen DigiKey-frifrakt, in med lagerfallbacks
- `DECISIONS.md` — D014: commissioning-dependencies är del av BOM

Efter detta är kvarvarande osäkerheter huvudsakligen sådant som **bör** vara osäkert tills verkliga delar finns: toleranser, bordets styvhet, kabel/slangrutter, collet-runout, KJD12-variant och checkout-totaler.