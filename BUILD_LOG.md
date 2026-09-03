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
- Hela top-level-repot reconcilerades eftersom äldre `BOM/CHECKLIST/SOURCING/AUDIT` fortfarande bar gamla sourcing-/controller-val trots nyare beslut.
- En tydlig kanonisk hierarki infördes: `PROCUREMENT.md` är enda ordermatrisen; BOM innehåller specs/kvantiteter; sourcing innehåller evidens; audit innehåller fysiska gates.
- StepperOnline fempack `5-17HS19-2004S1` liveverifierades till 38,13 €, 200 i lager; Germany warehouse är aktivt EU-spår.
- VEVOR 0700C exakt SKU liveverifierades köpbar; svensk checkout är prisgate.
- DigiKey fri-fraktgräns Sverige verifierades till 615 kr.
- Clas Ohlson KJD12 230 V/10 A verifierades till 299 kr som enkel NVR-kandidat.
- PLA låstes till 3 × eSUN PLA Basic Black 1 kg från 3DJake: 148 kr/st, 444 kr varor + 115 kr svensk standardfrakt = 559 kr landat baseline.

## 2026-09-03 — verkliga kostnader + Jackpot3 köpt

- HaWiWe-kostnaden reconcilerades mot faktisk bankdebitering: **1 853 kr** för de fyra produktgrupperna, ordervaluta 165,50 €.
- Jackpot3 `CQA240812C2` köpt från Elecrow.
- rabatt gav controllerpris **69,44 €**.
- DDP Economy **14,11 €** valdes.
- checkout total **83,55 €**.
- faktisk bankdebitering **937 kr**.
- faktisk spenderad projektsumma hittills: **2 790 kr**.
- `COSTS.md` skapades som kanonisk ledger; SEK-debitering är facit framåt.

## 2026-09-03 — Roboter-blockering och Allegro-falsk positiv

- Roboter-Bausatz nekade faktisk svensk leverans även efter Amazon Pay-adressöverföring; publicerad Sverige-frakt var inte tillräcklig evidens.
- Allegro-korgen konsoliderades därefter till `4Makers_pl` + `ABC-RC_pl` och visade 191,88 PLN inklusive två frakter.
- Efter inloggning och faktisk svensk adress visade det sig att **varken 4Makers_pl eller ABC-RC_pl levererar till Sverige**.
- Allegro-spåret stängdes. Lärdom: plattformsfrakt/korgsumma räcker inte; faktisk seller-checkout med svensk adress är facit.

## 2026-09-03 — mekanik flyttad till LaskaKit + HomeDIYer

- LaskaKits egen fraktsida listar explicit **GLS Sweden 8,93 €**.
- `LA190008E`, `LA190032A`, `LA190033A` och `LA190031` är rätt mekanikspecer.
- Den tidigare slutsålda 5 m-rullen `LA190013C` visades åter i lager i det nyare kategoriindexet, vilket gör 1 × 5 m bättre än 3 × 2 m om faktisk korg bekräftar lager.
- LaskaKit saknar fortfarande exakt 16T / 5 mm / 10 mm drive pulley.
- Ett kort icke-EU-spår via HomeDIYer noterades, men det ersattes innan köp.

## 2026-09-03 — DMW identifierad som EU-spår

- Icke-EU-spåret HomeDIYer stängdes utan köp.
- Exakt **GT2 16T / 5 mm bore / 10 mm belt** hittades hos **DMW Industrietechnik i Sindelfingen, Tyskland**, eBay item `124891176610`.
- Listningen hade valbara `Synchronriemenscheibe / 10mm / 5mm / Z 16` och gästcheckout.
- DMW:s säljarfrakt angavs som Warenpost International Premium och fraktscope som Europa.
- Vid faktisk köpgenomgång visade det sig senare att endast **2** exakta exemplar fanns kvar, så spåret kunde inte fylla behovet på 3.

## 2026-09-03 — 16T-remhjulen köpta via eBay/POWGE

- eBay söktes bredare på den fulla variantspecen och gav ett **3-pack** från `POWGE Synchronous Belts and Pulleys`.
- Vald variant: **GT2/2GT, 16T, 5 mm bore, för 10 mm belt**, pack quantity 3.
- eBay visade **fri frakt** och **`Includes import fees`**.
- Listat leveransfönster vid köp: **17 sep – 7 okt 2026**.
- Faktiskt debiterat: **72 kr**.
- DMW och övriga 16T-fallbacks stängdes därmed.
- Faktiskt spenderad projektsumma efter köpet: **2 862 kr**.
- Sourcinglärdom: för billiga variantkänsliga commodity-delar ska eBay sökas tidigt. EU-ursprung är inte målet i sig; rätt spec + låg total landad kostnad + tydlig importhantering är bättre beslutsvariabler.
