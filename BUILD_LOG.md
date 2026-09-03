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
- Roboter-Bausatz-korgen liveverifierades: alla sex artikeltyper tillgängliga; 37,53 € varor + 14,99 € publicerad Sverige-frakt = 52,52 € butikssnapshot före eventuell svensk destinationsmomsjustering.
- StepperOnline fempack `5-17HS19-2004S1` liveverifierades till 38,13 €, 200 i lager; Germany warehouse är aktivt EU-spår.
- VEVOR 0700C exakt SKU liveverifierades köpbar; tysk storefront visade 63,99 €, men svensk checkout gjordes explicit till prisgate eftersom destinationsmomsen kan ändra summan. EU-fraktpolicy anger fri frakt för normalprodukt till Sverige.
- DigiKey fri-fraktgräns Sverige verifierades till 615 kr; `HDR-60-24` och Digi-Spool-kablar har tillräckligt aktuellt lager.
- Clas Ohlson KJD12 230 V/10 A verifierades till 299 kr som enkel NVR-kandidat; exakt KEDU-proveniens togs bort som krav.
- Controllerköpet flyttades från teknisk Jackpot2-baseline till Elecrow Jackpot3 `CQA240812C2` som aktiv köpväg.
- PLA låstes till 3 × eSUN PLA Basic Black 1 kg från 3DJake: 148 kr/st, 444 kr varor + 115 kr svensk standardfrakt = 559 kr landat baseline.
- Historiska val behölls endast som historik; aktiva filer säger nu samma sak.

## 2026-09-03 — verkliga kostnader + Jackpot3 köpt

- HaWiWe-kostnaden reconcilerades mot faktisk bankdebitering: **1 853 kr** för de fyra produktgrupperna, ordervaluta 165,50 €.
- Jackpot3 `CQA240812C2` köpt från Elecrow.
- rabatt gav controllerpris **69,44 €**.
- DDP Economy **14,11 €** valdes.
- checkout total **83,55 €**.
- faktisk bankdebitering **937 kr**.
- faktisk spenderad projektsumma hittills: **2 790 kr**.
- `COSTS.md` skapades som kanonisk ledger; SEK-debitering är facit framåt.

## 2026-09-03 — Roboter-blockering och Allegro-konsolidering

- Roboter-Bausatz nekade faktisk svensk leverans även efter Amazon Pay-adressöverföring; publicerad Sverige-frakt bedöms stale/otillräcklig och vägen stängdes.
- En kort LaskaKit + separat 16T-plan skapades som fallback.
- Ny kontroll visade att `4Makers_pl` på Allegro har fem av sex exakta mekanikrader: smooth idlers, 10 mm fiberglass GT2-rem, 16T/5 mm/10 mm drive pulleys, 5×8 couplers och Tr8×8 brass nut.
- 5 m-remmen kan köpas som qty 5 av 1 m-annonsen och säljaren anger sammanhängande stycke.
- Exakt T8×8 400 mm + brass nut finns hos `Zadar-Sklep` på samma Allegro-plattform.
- Eftersom spindelraden redan innehåller en mutter korrigerades mekanikkorgen till **bara en extra mutter** från 4Makers.
- Allegro-varor före frakt: **179,93 PLN** totalt över två säljare.
- LaskaKit flyttades från aktiv huvudorder till fallback. Allegro är en plattform men två säljare innebär sannolikt två försändelser; svensk leverans måste verifieras per säljare i checkout.
