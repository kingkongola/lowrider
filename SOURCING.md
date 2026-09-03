# Sourcing evidence

**Snapshot 2026-09-03.** `PROCUREMENT.md` är den kanoniska ordermatrisen. Den här filen dokumenterar varför de aktiva köpvägarna är valda och ska inte skapa alternativa BOM-rader. Faktisk kostnad finns i `COSTS.md`.

## Roboter-Bausatz — BLOCKED

Roboter-Bausatz hade rätt delar och publicerade en Sverige-frakt på 14,99 €, men köpvägen fallerade i faktisk checkout 2026-09-03:
- Sverige saknades i butikens manuella landlista.
- Amazon Pay kunde läsa den svenska adressen.
- efter återgång till handlaren svarade checkouten: **"Leveranser till den valda leveransadressen är inte möjliga."**

Det publicerade fraktpriset är alltså inte tillräckligt bevis för faktisk svensk leverans. Roboter-Bausatz är borttaget som aktiv källa tills deras checkout ändras.

## LaskaKit — aktiv mekanikkärna

LaskaKit publicerar **GLS Sweden 8,93 €** och har en verklig internationell frakttabell med Sverige.

Aktiva rader:
- `LA190008E` smooth GT2 idler, 5 mm bearing, 10 mm belt — aktuell kontroll visar gott lager.
- `LA190032A` T8×8 400 mm, stainless 304, 4-start / 8 mm lead — mutter ingår uttryckligen inte.
- `LA190033A` T8×8 brass nut — köp 2.
- `LA190031` flexible coupling 5×8 mm — köp 2.
- `LA190013B` GT2 2 m × 10 mm fiberglass — köp 3.

Den tidigare perfekta 5 m-rullen `LA190013C` är nu **slutsåld**. Tre 2 m-rullar är ändå mekaniskt rena eftersom våra tre remsegment är 999 / 1705 / 1705 mm och därför kan tas ett per rulle utan skarv.

## 16T drive pulleys — Allegro checkout-gate

LaskaKit har inte aktuell 16T-variant för 10 mm rem. Exakt aktuell kandidat på Allegro:
- tillverkarkod/listningskod `16T W10 B5 WZ`
- GT2 2 mm pitch
- 16T
- 5 mm bore
- 10 mm belt
- ca 11 mm tooth track
- två låsskruvar
- 8,99 PLN/st vid kontroll, 19 st visade

Allegro har internationell leveransinfrastruktur till Sverige, men exakt säljarerbjudande måste bekräfta Sverige i checkout. Specen är låst även om säljaren behöver bytas.

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
- Technobots GT2 — endast historisk fallback
- separat KEDU/CEM-specialorder — inte baseline
- Sorotec — deferred tills verkligt fräsbehov
- SUNLU 6 kg — borttaget; behovet är 3 kg
- 3D Prima PLA — ersatt av billigare komplett landad 3DJake-baseline
- Jackpot2 — historiskt controlleralternativ; Jackpot3 är redan köpt
