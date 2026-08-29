# Build log

## 2026-08-29 — initial design/procurement pass

- Privat GitHub-repo skapat för LowRider V4-bygget.
- Maskinvalet avslutat: **LowRider V4 ska byggas**.
- HaWiWe-order lagd och **betald**, totalt **165,50 € inklusive 8,00 € frakt**:
  - Aluminium XZ plates — 39,50 €
  - Linear rail set LowRider 4 — 57,00 €
  - Screw set LowRider 4 — 32,00 €
  - Makita/Elaire 1/8" collet — 29,00 €
- Arbetsytan låst till **650 × 1250 mm**.
- Exakt geometri: rör 816 / 816 / 1505 mm, strut 819, GT2 999 / 1705 / 1705 mm, minimum bord 941 × 1563 mm, deck ~1000×1620 mm.
- Jackpot3, VEVOR 0700C, HDR-60-24 och Omron-spåret valdes.

## 2026-08-29 — oberoende system-/fysisk audit

Grundarkitekturen överlevde. Konkreta korrigeringar:
- ~1 m 24 V-kabel var fel att låsa när HDR är fast och Jackpot rörlig → 3 m marginal + full-travel dry-fit.
- separat LV-gland behövs.
- alla dimensionsberoende prints = 30 mm; strut `819` + `front_wing_size=30`.
- 90 cm bord fungerar men ~50 mm decköverhäng måste ha verkligt stöd i LR4:s kantzon.
- routerkabel + 24 V + stepper/endstop + vac-hose ska provas tillsammans över full rörelse.
- KJD12 beskrivs som NVR/maskinstopp, inte verifierad safety-rated E-stop.
- statisk jordning blev explicit gate.
- Elecrow Jackpot3 måste flashas/configureras.
- canonical top-level state reconcilerades.

## 2026-08-30 — inköpsrad + commissioning-audit

Huvudkomponenterna överlevde igen. Fynd:
- T8 400 mm ska inte automatiskt halveras; ~150–160 mm ×2 efter assembly-check, V1E minimum 145 mm.
- UL2464 20 AWG är inte explicit continuous-flex; stor mjuk loop, chain-flex bara om verklig routing kräver det.
- microSD + data-USB-C är commissioning-dependencies men inventeras före köp.
- standard-endstops är home/auto-square, inte runtime hard limits.
- Jackpot-kablar ska gå bredvid kort/antenn med fri luftväg.
- DigiKey-frifrakt behandlas som checkout-gated.

## 2026-08-30 — live cart reconciliation

Live-kontroll av riktiga produktsidor gav ytterligare korrigeringar:

1. **Bambu P1S var aldrig en verklig print-gate.** P1S 256³ överstiger V1E:s minimum 200×200×190. Kvar är endast rätt LR4-version/30 mm/65 mm variant, slicer-preview och litet `Z_Stub`/`Z_Nut` testfit.
2. **10 A-garagegruppen de-eskalerades.** Gruppen är praktiskt beprövad med svets; plasma har kunnat lösa säkringen. VEVOR 800 W + DeWalt + controller betraktas därför inte som öppet projektproblem. Endast normal sanity-check vid första samtidiga körningen.
3. **VEVOR:s “6.5A” på EU-sidan identifierades som återanvänd 120 V-marknadsföring.** Manualen anger EU 220–240 V / 800 W, inte 6,5 A. Ingen falsk 6,5 A EU-last används i dimensioneringen.
4. **LaskaKit-remmens lagerstatus var stale.** Äldre kategoridata sade lager, men direkta produktsidan visar både 5 m och 2 m 10 mm fiberglass GT2 som slut. Remmen flyttades ur LaskaKit-korgen.
5. **GT2-remmen fick ny exakt EU-källa:** Roboter-Bausatz `RBS12747`, GT2/2 mm, 10 mm, gummi + glasfiber, meterware, live i lager, €2,25/m vid 5 m. Fem meter räcker till exakta 4409 mm; checkout ska bekräfta kontinuerlig 5 m-längd och Sverige-frakt.
6. **DigiKey SKU-fälla hittades:** TE `3-350820-2` ska köpas som vanliga lagerartikeln `A27824-ND`, inte Marketplace-dubbletten med MOQ 1000.
7. **Saknad LV-gland löstes konkret:** Amphenol `AIO-CSM12`, M12 / 3–6,5 mm / IP68 passar nominell ~4,8 mm 24 V-kabel och läggs i DigiKey-korgen.
8. **KEDU spikades till rätt familj:** genuine `KJD12-14`, 230 V/50 Hz-variant, 15 A AC-3 / 18 A AC-1, Faston 6,3×0,8 och röd svamp/gul kåpa. CEM/eBay är konkret köpväg.
9. **SUNLU:** Sverige är uttryckligen listat i EU-leveransområdet; officiella sidan anger normalt fri EU-frakt, men checkout för den faktiska korgen är fortfarande facit.
10. **Jackpot3:** live $76.99/in stock vid kontrollen.

Efter reconciliation är komponent-specifikationen i praktiken klar. Kvar är främst verkliga checkout-totaler samt fysiska kontroller av rör, bord, collet/runout, DeWalt-typskylt och kabel/slangrörelse.