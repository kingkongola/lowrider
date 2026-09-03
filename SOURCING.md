# Sourcing evidence

**Snapshot 2026-09-03.** `PROCUREMENT.md` är den kanoniska ordermatrisen. Den här filen dokumenterar varför de aktiva köpvägarna är valda och ska inte skapa alternativa BOM-rader.

## Roboter-Bausatz

Aktiv konsoliderad mekanikkälla. Verifierat 2026-09-03:
- `RBS12910` smooth idler — tillgänglig
- `RBS12872` T8×8 400 mm + mutter — tillgänglig
- `RBS12749` extra mutter — tillgänglig
- `RBS10595` 5→8 mm coupler — tillgänglig
- `RBS12747` GT2 10 mm, 2 mm pitch, gummi + glasfiber, meterware — tillgänglig
- `RBS12867` 16T / 5 mm / 10 mm — tillgänglig
- Sverige DHL flat rate 14,99 € publicerat

Korgen ersätter tidigare LaskaKit + separat rem + Allegro. Butikens listpriser använder tysk moms; svensk checkout kan justera destinationsmomsen.

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

## Controller

Aktiv väg: Elecrow `CQA240812C2` Jackpot3. Verifierat 2026-09-03: $76,99, `In stock`, 300 g.

V1E Jackpot2 är fortfarande tekniskt tillräcklig för routerbygget, men V1E:s butikstatus är motsägelsefull. Därför får controllerköpet inte blockeras på Jackpot2. Se D015.

## VEVOR

Exakt `0700C`, SKU `YXKXBJ710W65AH7WLV2`, 220–240 V / 50 Hz / 800 W / 65 mm. EU-köpvägen är aktiv och VEVOR:s EU-policy anger fri standardfrakt för normala produkter till Sverige. Slutpriset måste läsas med Sverige som destination eftersom moms kan lokaliseras; tysk 63,99 €-snapshot är inte låst som svensk totalsumma.

## PLA

Aktiv väg 2026-09-03: 3DJake Sverige, **eSUN PLA Basic Black 1,75 mm / 1 kg**. 148 kr/st, 2 979 i lager i aktuell kontroll. Tre spolar = 444 kr; standardfrakt Sverige 115 kr under 1 099 kr; baseline landat **559 kr**. Detta ersätter tidigare SUNLU/3D Prima/Amazon-öppna spår.

## Motonet

Rörspår: 2 × `88-7123`, Ø30 mm, 2 m. Historisk produktidentifiering är stark, men själva köpet är fysisk: mät OD/rakhet innan köp och kapning. Aktuellt webblager/pris är inte tillräckligt robust verifierat och ska därför inte anges som faktum.

## NVR

KJD12-familjen är kravmässigt tillräcklig om exakt levererad variant är 230 V, har lämplig märkström, dokumenterat schema och no-voltage-release. Clas Ohlson `50-2929`, KJD12 230 V/10 A, 299 kr är enkel aktuell kandidat. Exakt KEDU-proveniens är inte ett mål i sig.

## Inte aktiva sourcingvägar

- LaskaKit — bortkonsoliderad
- Allegro 16T — bortkonsoliderad
- Technobots GT2 — endast historisk fallback
- separat KEDU/CEM-specialorder — inte baseline
- Sorotec — deferred tills verkligt fräsbehov
- SUNLU 6 kg — borttaget; behovet är 3 kg
- 3D Prima PLA — ersatt av billigare komplett landad 3DJake-baseline