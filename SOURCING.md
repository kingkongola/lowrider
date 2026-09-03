# Sourcing evidence

**Snapshot 2026-09-03.** `PROCUREMENT.md` är den kanoniska ordermatrisen. Den här filen dokumenterar varför de aktiva köpvägarna är valda och ska inte skapa alternativa BOM-rader. Faktisk kostnad finns i `COSTS.md`.

## Checkout-regel efter falska positiva

**En fraktsida, plattformsfrakt eller korgsumma räcker inte.** En köpväg räknas som svensk först när den faktiska handlar-/säljarcheckouten accepterar svensk leveransadress. Roboter-Bausatz och Allegro är dokumenterade exempel på varför.

För billiga standardiserade mekanikdelar ska eBay/andra marknadsplatser kontrolleras tidigt när exakt variant kan verifieras och checkouten tydligt hanterar svensk moms/import. Ursprungsland i sig är inte ett skäl att avvisa en bättre väg; total landad kostnad, exakt spec, importfriktion och leveranstid är det relevanta.

## LaskaKit, Tjeckien — ACTIVE mekanikkärna

Direktbutikens aktuella fraktsida listar uttryckligen **GLS Sweden 8,93 €** och anger att försändelserna går från Rychnov nad Kněžnou, Tjeckien.

Verifierat 2026-09-03:
- `LA190008E` smooth GT2 idler, 5 mm bearing, för 10 mm belt — aktuell POWGE-kategori visar **76 i lager**, 1,86 €/st; köp 6.
- `LA190032A` T8×8 400 mm — 8 mm lead, 4-start — aktuell CNC-kategori visar **5 i lager**, 8,19 €; köp 1.
- `LA190033A` T8×8 brass nut — rätt Tr8×8 / 8 mm lead / 4-start — köp 2.
- `LA190031` flexible coupling 5×8 mm — aktuell kategori visar **19 i lager**, 1,82 €/st; köp 2.
- `LA190013C` GT2 5 m × 10 mm fiberglass — aktuell CNC-kategori visar **18 i lager**, 7,81 €; köp 1.

5 m-remmen är optimal: behovet är 999 + 1705 + 1705 = 4409 mm, vilket lämnar cirka 591 mm total marginal.

Det finns en cachekonflikt för `LA190013C`: äldre direkt produktsida säger slutsåld medan nyare kategoriindex säger 18 i lager. Därför är faktisk LaskaKit-korg lagerfacit. Om 5 m-rullen faller bort används 3 × 2 m 10 mm fiberglass-rem utan att ändra maskinspec.

LaskaKit har inte vår drive pulley: deras aktuella 16T/5mm är för **6 mm belt**, medan 10 mm-varianterna är 20T. Ändra inte 16T-specen. Den raden är nu redan köpt via eBay/POWGE.

## eBay / POWGE — CLOSED 16T drive pulleys

Köpt 2026-09-03 från **POWGE Synchronous Belts and Pulleys** via eBay:
- 3 × GT2/2GT drive pulley
- **16T**
- **5 mm bore**
- för **10 mm belt**
- 2 mm pitch
- vald packvariant: `3 × 2GT pulleys`
- fri frakt
- eBay visade **`Includes import fees`**
- listat leveransfönster vid köp: **17 sep – 7 okt 2026**
- faktisk debitering: **72 kr**

Detta stängde den enda svårfunna mekanikraden. DMW hade tekniskt rätt variant men bara två exemplar kvar när köp skulle göras. eBay gav i stället ett komplett trepack till låg landad kostnad med importhanteringen inbakad.

Lärdom: den tidigare sökningen överviktade EU-butik som proxy för låg friktion. För commodity-delar ska eBay sökas tidigt med hela variantspecen och faktisk checkout/importtext som gate.

## DMW Industrietechnik — INACTIVE / REPLACED

DMW Industrietechnik i Tyskland, eBay item `124891176610`, hade tekniskt korrekt `Synchronriemenscheibe / 10mm / 5mm / Z 16`. Vid faktisk köpgenomgång återstod dock endast **2** av den exakta varianten, medan bygget kräver 3.

Spåret ersattes av det genomförda POWGE/eBay-köpet. Köp inget från DMW för denna rad nu.

## Roboter-Bausatz — BLOCKED

Roboter-Bausatz hade rätt delar och publicerade Sverige-frakt, men faktisk checkout 2026-09-03 nekade svensk adress även efter Amazon Pay-adressöverföring. Vägen är stängd.

## Allegro — BLOCKED

Allegro-korgen med `4Makers_pl` + `ABC-RC_pl` visade en till synes komplett order och frakt, men efter inloggning/adressval nekade båda säljarna leverans till Sverige. Detta bevisar att plattformens generella Sverige-stöd och korgfrakt inte är tillräcklig evidens.

Historiska Allegro-rader får finnas i `BUILD_LOG.md`, men ska inte återaktiveras utan faktisk svensk seller-checkout.

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

Aktiv väg 2026-09-03: 3DJake Sverige, **eSUN PLA Basic Black 1,75 mm / 1 kg**. 148 kr/st, 2 979 i lager i aktuell kontroll. Tre spolar = 444 kr; standardfrakt Sverige 115 kr under 1 099 kr; baseline landat **559 kr**.

## Motonet

Rörspår: 2 × `88-7123`, Ø30 mm, 2 m. Själva köpet är fysisk: mät OD/rakhet innan köp och kapning.

## NVR

KJD12-familjen är kravmässigt tillräcklig om exakt levererad variant är 230 V, har lämplig märkström, dokumenterat schema och no-voltage-release. Clas Ohlson `50-2929`, KJD12 230 V/10 A, 299 kr är enkel aktuell kandidat.

## Inte aktiva sourcingvägar

- DMW Industrietechnik — tekniskt rätt 16T, men bara två exakta exemplar kvar vid köp; ersatt av köpt POWGE/eBay-trepack.
- Roboter-Bausatz — svensk checkout blockerar leverans.
- Allegro `4Makers_pl` / `ABC-RC_pl` — faktisk seller-checkout blockerar Sverige.
- HomeDIYer — tekniskt användbar men onödig efter eBay/POWGE-köpet.
- Hellas Digital 16T — exakt komponent finns, men behövs inte efter köpet.
- Amazon-indexerade 16T-alternativ — inte längre relevanta.
- Technobots GT2 — endast historisk fallback.
- separat KEDU/CEM-specialorder — inte baseline.
- Sorotec — deferred tills verkligt fräsbehov.
- SUNLU 6 kg — borttaget; behovet är 3 kg.
- 3D Prima PLA — ersatt av billigare komplett landad 3DJake-baseline.
- Jackpot2 — historiskt controlleralternativ; Jackpot3 är redan köpt.
