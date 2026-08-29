# BOM

Här ska bara delar för den LowRider V4 som faktiskt byggs finnas.

## Inköpsförutsättning

- [x] **Amazon Prime-medlemskap** — använd Prime som möjlig fraktfördel, men välj butik efter totalpris inklusive frakt.

## Redan köpt — HaWiWe, 29 augusti 2026

Ordertotal: **165,50 € inklusive 8,00 € frakt**.

- [x] Aluminium XZ plates — **39,50 €**
- [x] Linear rail set LowRider 4 — **57,00 €**
- [x] Screw set LowRider 4 — **32,00 €**
- [x] Makita 1/8 inch (3,175 mm) collet — **29,00 €**
- [x] Frakt — **8,00 €**

### Exakt innehåll i köpta HaWiWe Screw set LowRider 4

Verifierat mot HaWiWe produktsida **2026-08-29**:
https://hawiwe.de/produkt/schraubenset-lowrider-4/

- [x] 14 × **M8×40**, DIN 933 / ISO 4017, 8.8, förzinkad
- [x] 14 × **M8 nyloc/låsmutter**, DIN 985
- [x] 60 × **M5×30**, DIN 7985, 4.8, krysspår, förzinkad
- [x] 60 × **M5 nyloc/låsmutter**, DIN 985
- [x] 83 × **M3×10**, DIN 7985, 4.8, krysspår, förzinkad
- [x] 10 × **M2.5×12**, DIN 7985, 4.8, krysspår, förzinkad

**Viktigt:** detta kit är endast skruvar + muttrar. Det innehåller **inte** lager, T8-skruvar, T8-muttrar, kopplingar, remhjul, idlers, rem, ändlägen, motorer, kablage eller nätaggregat.

## Kvar till själva LR4-maskinen

PLA/printmaterial och stålrör hanteras separat och listas inte här.

### Måste köpas

- [ ] **Jackpot3 CNC Controller**
- [ ] 5 × NEMA17-stegmotorer, ca 59 Ncm / 84 oz-in, 5 mm axel, axel minst 20 mm
- [ ] 3 × stepper wire extenders / förlängningskablage
- [ ] 3 × GT2 10 mm, 16T remhjul
- [ ] 6 × GT2 10 mm, 20T släta idlers, 5 mm hål
- [ ] GT2 10 mm rem — exakt längd från LR4-kalkylatorn
- [ ] 5 × ändlägesbrytare + kablage/kontakter
- [ ] 14 × 608-2RS lager
- [ ] 2 × T8 trapetsskruv + mutter, minst 145 mm, 4-start / 2 mm pitch / 8 mm per varv
- [ ] 2 × koppling 5 mm → 8 mm
- [ ] 1 × nätaggregat, 24 V, minst 36 W
- [ ] **VEVOR VV-1B-220V 710 W router**
- [ ] minst 1 × 1/8" / 3,175 mm single-flute frässtål
- [ ] bord/underrede
- [ ] plan bordsskiva / spoilboard
- [ ] material till permanenta strut plates, max 6,35 mm
- [ ] ca 18 × M4×12 mm eller längre trä-/plåtskruv för infästning i bordet; V1E anger dessa separat och de ingår inte i HaWiWe screw set

### Rekommenderat / småsaker

- [ ] gänglåsning för remhjulens stoppskruvar
- [ ] lätt smörjmedel till idlers/linjärskenor
- [ ] buntband eller annan kabelinfästning

### Valfritt senare

- [ ] dammsugarslang / spånutsug
- [ ] jordning av dammsugarslang om slanglösningen kan bygga statisk elektricitet
- [ ] touch plate / verktygslängdsgivare

## Styrkort — Jackpot3

**Val:** Jackpot3.

Aktuella priser verifierade 2026-08-29:
- V1E: **$75.99**
- Elecrow: **$76.99**

Jackpot3 innehåller **6 integrerade TMC2226-drivare**, så inga separata stepperdrivare ska köpas.

## Router — VEVOR 710 W Makita-klon

**Val:** VEVOR **VV-1B-220V**, 710 W, 65 mm kropp, 13 000–33 000 rpm, fast bas.

Verifierat pris hos VEVOR EU 2026-08-29: **42,90 €**.

Medföljande spännhylsor: **1/4", 6 mm och 8 mm**.

### Makita/Elaire 3,175 mm-spännhylsa → VEVOR

**Status 2026-08-29: starkt sannolik kompatibilitet; köp ingen ytterligare 1/8"-hylsa i förväg.**

Det som är verifierat:

1. Den köpta HaWiWe-hylsan är en **Elaire Makita-style 1/8" collet**, avsedd för bl.a. Makita RT700C / RT0700CX3 / RT0701C.
   - HaWiWe: https://hawiwe.de/produkt/makita_spannzange/
   - Elaire: https://elairecorp.com/product-category/makita-style-router-collets/
2. VEVOR:s sida för den exakta **VV-1B-220V / produkt-ID 010376710625** anger 65 mm kropp. På VEVOR:s sida för samma produktfamilj besvarar VEVOR frågan om den ersätter Makita RT0700 med **ja**.
   - https://eur.vevor.com/compact-router-c_10131/vevor-electric-hand-trimmer-palm-router-with-three-collets-and-fixed-base-710w-p_010376710625
3. Det finns praktisk LR/CNC-erfarenhet på V1E-forum där en **VEVOR 0700C (Makita 700-klon)** körs med en 1/8" Makita-style/Sienci-collet i VEVOR:s originalmutter med mycket liten runout.
   - https://forum.v1e.com/t/crappy-router-collet/50663/8

**Begränsning:** jag har inte hittat ett uttalande från VEVOR/Elaire som uttryckligen säger att just Elaire MRP-1250 passar just VV-1B-220V. Därför är detta inte 100 % formellt verifierat.

**Praktiskt beslut:** köp VEVOR-fräsen men ingen extra 1/8"-hylsa. När fräsen kommer: prova den köpta Elaire-hylsan utan verktyg och verifiera att den sätes korrekt i konan/muttern; därefter kontrollera runout med ett rakt 1/8"-verktyg innan första riktiga körningen.

## Motorer

Fortsatt bra kandidat: **STEPPERONLINE 5-pack NEMA17, ca 59 Ncm / 84 oz-in, 2 A**.

## Redan täckt av HaWiWe-köpet

- [x] XZ-plattor
- [x] 4 × MGN12H 150 mm linjärskenor
- [x] LR4-skruv/mutter-set — exakt innehåll dokumenterat ovan
- [x] Makita/Elaire 3,175 mm-spännhylsa — **köpt; starkt sannolikt kompatibel med vald VEVOR, ska provpassas innan drift**
