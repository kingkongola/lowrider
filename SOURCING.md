# Sourcing evidence

**Snapshot 2026-09-03.** `PROCUREMENT.md` är den kanoniska ordermatrisen. Den här filen dokumenterar varför de aktiva köpvägarna är valda och ska inte skapa alternativa BOM-rader. Faktisk kostnad finns i `COSTS.md`.

## Roboter-Bausatz — BLOCKED

Roboter-Bausatz hade rätt delar och publicerade en Sverige-frakt på 14,99 €, men köpvägen fallerade i faktisk checkout 2026-09-03:
- Sverige saknades i butikens manuella landlista.
- Amazon Pay kunde läsa den svenska adressen.
- efter återgång till handlaren svarade checkouten: **"Leveranser till den valda leveransadressen är inte möjliga."**

Det publicerade fraktpriset är alltså inte tillräckligt bevis för faktisk svensk leverans.

## Allegro — aktiv konsoliderad mekanikväg

Målet är att slippa separat LaskaKit-order. Allegro har officiell DPD/DHL-infrastruktur från Polen till Sverige, men **säljaren måste själv ha Sverige aktiverat**, så checkout är fortfarande facit.

### `4Makers_pl` — fem mekanikrader hos samma säljare

Verifierat 2026-09-03:

- **Smooth idler:** `KOŁO SWOBODNE GŁADKIE GT2 10mm WAŁEK 5mm JAK 20T`
  - producer code `KSG1020T`
  - 10 mm GT2 belt
  - 5 mm shaft/bore
  - 7,99 PLN/st
  - offer `10997887930`
  - köp 6

- **Drive pulley:** `KOŁO NAPĘDOWE PASKA GT2 10mm WAŁEK 5mm ZĘBY 16T`
  - GT2
  - 16T
  - 5 mm shaft
  - 10 mm belt
  - aktuell 4Makers-listning 6,90 PLN/st
  - köp 3

- **Belt:** `PASEK ZĘBATY GT2 10mm RDZEŃ WŁÓKNO SZKLANE - 1m`
  - producer code `GT210WS1M`
  - pitch 2 mm
  - width 10 mm
  - fiberglass core
  - 13,00 PLN/m
  - offer `11895522331`
  - annonsen säger att flera köpta meter levereras som **ett helt sammanhängande stycke**
  - köp qty 5 = 5 m

- **Coupler:** `SPRZĘGŁO ALUMINIOWE ELASTYCZNE 5x8mm`
  - producer code `SPE5X8`
  - 5 mm ↔ 8 mm
  - 6,25 PLN/st
  - offer `10997503256`
  - köp 2

- **Extra T8 nut:** vanlig 4-håls `NAKRĘTKA MOSIĘŻNA ŚRUBY TRAPEZOWEJ TR8x8`
  - producer code `NAKMOS8L`
  - brass
  - Tr8×8 / 8 mm lead / 4-start
  - 4,29 PLN i aktuell korg
  - köp **1**, inte 2

4Makers-varor totalt: **150,43 PLN**.

Riktad sökning genom 4Makers aktuella Allegro-utbud hittar **Tr8×8-muttrar men ingen korrekt Tr8×8-spindel**. Den 400 mm-spindel som faktiskt lades i användarens 4Makers-korg är märkt **TR8X2**, alltså 2 mm lead, och dessutom **"Nowy z defektem"**. Den ska tas bort och får inte användas som substitut.

### `ABC-RC_pl` — exakt T8×8-spindel + första muttern

Aktuell verifierad Allegro-listning:
- `Śruba Trapezowa T8x8 400mm - Nakrętka z Brązu THSL-400-8D`
- offer `17625893658`
- product code `THSL-400-8D` / 8605
- diameter 8 mm
- 4 starts
- lead 8 mm
- length 400 mm
- **bronsmutter ingår**
- skick `Nowy`, vilket Allegro definierar som ny utan fel/defekter
- aktuell offer-snapshot 19,58 PLN, 95 st visade

Detta matchar den låsta LR4-specen exakt. 400 mm räcker eftersom bygget kapar två slutliga Z-spindlar om cirka 150–160 mm vardera efter assembly-check.

Detta är varför 4Makers-korgen bara ska innehålla **en extra mutter**. Totalt blir det två muttrar.

### Allegro-fraktgräns

Allegro stöder officiellt DPD och DHL från Polen till Sverige. Säljarna måste dock själva ha Sverige aktiverat.

Köpvägen godkänns först när både `4Makers_pl` och `ABC-RC_pl` visas med svensk leverans i faktisk checkout. Samma Allegro-plattform innebär inte automatiskt samma försändelse eller gemensam fraktavgift.

## LaskaKit — FALLBACK

LaskaKit publicerar GLS Sweden och har tekniskt korrekta alternativ för smooth idlers, T8×8, muttrar, 5×8 couplers och 10 mm fiberglass-rem. Det är nu fallback, inte aktiv huvudorder.

Använd LaskaKit endast för den rad som eventuellt fallerar i Allegro-checkout; skapa inte hela LaskaKit-korgen om Allegro håller.

## DigiKey

Aktiv konsoliderad elektronik/el-källa.

Låsta SKU-fällor:
- `HDR-60-24` = `1866-2249-ND`
- TE `3-350820-2` = **`A27824-ND`**, inte Marketplace-dubbletten
- `AIO-CSM12` = LV-gland
- `30-00416` och `30-00377` beställs som Digi-Spool/meterware

DigiKey Sverige anger 0 kr frakt från 615 kr och 170 kr under gränsen. Full planerad korg passerar gränsen. Marketplace kan skapa separat frakt och ska inte användas.

## StepperOnline

Aktiv motorväg: Germany warehouse, fempack `5-17HS19-2004S1`. Verifierat 2026-09-03: 38,13 €, 200 i lager. Frakt till Sverige är checkout-gated.

## Controller — CLOSED

**Elecrow Jackpot3 `CQA240812C2` köpt 2026-09-03.**
- controller efter rabatt: 69,44 €
- DDP Economy: 14,11 €
- checkout: 83,55 €
- faktiskt debiterat: **937 kr**

Jackpot2 var ett tidigare tekniskt router-first-alternativ men är nu endast historik. Controller-sourcing ska inte återöppnas.

## VEVOR

Exakt `0700C`, SKU `YXKXBJ710W65AH7WLV2`, 220–240 V / 50 Hz / 800 W / 65 mm. EU-köpvägen är aktiv och VEVOR:s EU-policy anger fri standardfrakt för normala produkter till Sverige. Slutpriset måste läsas med Sverige som destination eftersom moms kan lokaliseras; tysk 63,99 €-snapshot är inte låst som svensk totalsumma.

## PLA

Aktiv väg 2026-09-03: 3DJake Sverige, **eSUN PLA Basic Black 1,75 mm / 1 kg**. 148 kr/st, 2 979 i lager i aktuell kontroll. Tre spolar = 444 kr; standardfrakt Sverige 115 kr under 1 099 kr; baseline landat **559 kr**. Detta ersätter tidigare SUNLU/3D Prima/Amazon-öppna spår.

## Motonet

Rörspår: 2 × `88-7123`, Ø30 mm, 2 m. Historisk produktidentifiering är stark, men själva köpet är fysisk: mät OD/rakhet innan köp och kapning. Aktuellt webblager/pris är inte tillräckligt robust verifierat och ska därför inte anges som faktum.

## NVR

KJD12-familjen är kravmässigt tillräcklig om exakt levererad variant är 230 V, har lämplig märkström, dokumenterat schema och no-voltage-release. Clas Ohlson `50-2929`, KJD12 230 V/10 A, 299 kr är enkel aktuell kandidat. Exakt KEDU-proveniens är inte ett mål i sig.

## Inte aktiva sourcingvägar

- Roboter-Bausatz — svensk checkout blockerar leverans trots publicerad Sverige-frakt
- 4Makers `TR8X2 400MM` — fel lead och dessutom listad som ny med defekt
- Zadar-Sklep `8954932033` — tidigare kandidat borttagen när defektstatus upptäcktes
- LaskaKit full mekanikkorg — fallback om en Allegro-rad fallerar
- Technobots GT2 — endast historisk fallback
- separat KEDU/CEM-specialorder — inte baseline
- Sorotec — deferred tills verkligt fräsbehov
- SUNLU 6 kg — borttaget; behovet är 3 kg
- 3D Prima PLA — ersatt av billigare komplett landad 3DJake-baseline
- Jackpot2 — historiskt controlleralternativ; Jackpot3 är redan köpt
