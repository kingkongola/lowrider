# Build log

## 2026-08-29 — initial design/procurement pass

- Privat GitHub-repo skapat för LowRider V4-bygget.
- Maskinvalet avslutat: LowRider V4.
- HaWiWe-order lagd och betald: 165,50 € inklusive 8,00 € frakt.
- Arbetsytan låst till 650 × 1250 mm.
- Exakt geometri: rör 816 / 816 / 1505 mm, strut 819, GT2 999 / 1705 / 1705 mm, minimum bord 941 × 1563 mm, deck ~1000×1620 mm.
- Tidigt controller-spår var Jackpot3.

## 2026-08-29 — oberoende system-/fysisk audit

- 24 V-rutten korrigerades från skrivbordsmått till 3 m marginal + full-travel dry-fit.
- LV-gland blev explicit.
- alla diameterberoende prints = 30 mm; strut `819` + `front_wing_size=30`.
- 90 cm bord godkändes med explicit kantstöd.
- routerkabel + 24 V + stepper/endstop + vac-hose ska provas samtidigt.
- KJD12 benämns NVR/maskinstopp, inte safety-rated E-stop.
- statisk jordning blev gate.

## 2026-08-30 — commissioning-audit

- T8 400 mm kapas efter assembly-check; ~150–160 mm ×2.
- UL/PVC-rörelsekabel är inte explicit continuous-flex; stor mjuk loop och byte endast vid verkligt behov.
- microSD + data-USB-C inventeras före köp.
- endstops = home/auto-square, inte runtime hard limits.
- DigiKey SKU-fällan `A27824-ND` identifierades.
- Amphenol `AIO-CSM12` lades till.

## 2026-08-30 — sourcingoptimering

- LaskaKit-remmen visade stale lagersaldo.
- Roboter-Bausatz hittades som exakt källa för 10 mm GT2 glasfiber.
- mekanikkorgen konsoliderades gradvis till Roboter-Bausatz.
- DigiKey absorberade lågspänningskablar för att undvika separat order.
- PLA-behovet korrigerades till cirka 2,7 kg → köp 3 kg, inte 6 kg.
- Jackpot2 valdes som tekniskt router-first-baseline eftersom laser inte ingår i grundbygget.

## 2026-09-03 — HaWiWe skickat + full repo reconciliation

- HaWiWe har skickat den redan betalda ordern.
- Hela top-level-repot reconcilerades eftersom äldre `BOM/CHECKLIST/SOURCING/AUDIT` fortfarande bar Jackpot3/LaskaKit/6 kg SUNLU/Allegro/KEDU-specialorder trots nyare beslut.
- En tydlig kanonisk hierarki infördes: `PROCUREMENT.md` är enda ordermatrisen; BOM innehåller specs/kvantiteter; sourcing innehåller evidens; audit innehåller fysiska gates.
- Roboter-Bausatz-korgen liveverifierades: alla sex artikeltyper tillgängliga; 37,53 € varor + 14,99 € Sverige-frakt = 52,52 € snapshot.
- StepperOnline fempack `5-17HS19-2004S1` liveverifierades till 38,13 €, 200 i lager; Germany warehouse är aktivt EU-spår.
- VEVOR 0700C exakt SKU liveverifierades till 63,99 € och köpbar.
- DigiKey fri-fraktgräns Sverige verifierades till 615 kr; `HDR-60-24` och 20 AWG Digi-Spool visades med stort lager.
- Clas Ohlson KJD12 230 V/10 A verifierades till 299 kr som enkel NVR-kandidat; exakt KEDU-proveniens togs bort som krav.
- SUNLU/filament gjordes medvetet butiksolåst: endast 3 kg ordinary stiff PLA är projektkravet.
- Controllerköpet flyttades från teknisk Jackpot2-baseline till **Elecrow Jackpot3 `CQA240812C2`** som aktiv köpväg: Elecrow visar $76,99/In stock medan V1E-butikstatus är motsägelsefull. D015 dokumenterar att ändringen är sourcingdriven, inte laserdriven.
- Historiska val behölls endast som historik; aktiva filer säger nu samma sak.