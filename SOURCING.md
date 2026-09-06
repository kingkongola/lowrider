# Sourcing evidence

**Snapshot 2026-09-06.** `PROCUREMENT.md` är den kanoniska ordermatrisen. Den här filen dokumenterar varför köpvägar valdes eller stängdes och ska inte skapa alternativa BOM-rader. Faktisk kostnad finns i `COSTS.md`.

## Checkout-regel efter falska positiva

**En fraktsida, plattformsfrakt eller korgsumma räcker inte.** En köpväg räknas som svensk först när den faktiska handlar-/säljarcheckouten accepterar svensk leveransadress. Roboter-Bausatz och Allegro är dokumenterade exempel på varför.

För billiga standardiserade mekanikdelar ska Amazon/eBay/andra marknadsplatser kontrolleras tidigt när exakt variant kan verifieras. Ursprungsland i sig är inte ett skäl att avvisa en bättre väg; total landad kostnad, exakt spec, importfriktion och leveranstid är de relevanta beslutsvariablerna.

## LaskaKit, Tjeckien — CLOSED / ORDERED

Köpt 2026-09-03:
- 6 × `LA190008E` smooth GT2 idler, 5 mm bearing, för 10 mm belt
- 1 × `LA190032A` T8×8 400 mm, 8 mm lead / 4-start
- 2 × `LA190031` flexible coupling 5×8 mm
- 1 × `LA190013C` GT2 5 m × 10 mm fiberglass

Faktisk checkout:
- varor 30,75 €
- GLS Sweden 8,93 €
- total 39,68 €
- faktiskt debiterat 444 kr

`LA190033A` T8×8 brass nut var inte tillgänglig och ingår inte i ordern. Muttrarna sourcades därför separat.

5 m-remmen täcker behovet 999 + 1705 + 1705 = 4409 mm och lämnar cirka 591 mm total marginal.

LaskaKit har inte vår drive pulley: deras 16T/5 mm-spår matchade inte 10 mm-remmen. Den raden är redan köpt via eBay/POWGE.

## Amazon.se / euroharry — CLOSED / ORDERED T8×8 nuts

Beställt 2026-09-05 från användarens live Amazon-sida:
- 4 × flänsad T8-mässingsmutter
- för Ø8 mm Tr8-spindel
- **2 mm pitch**
- **4-start**
- därmed **8 mm lead**
- mässing
- 4-pack
- visat orderpris **101,76 kr**
- Prime

LR4 behöver två muttrar; två blir reserv. Detta är nu den aktiva leveransvägen och stänger T8-mutter-sourcingen.

Amazon-spåret är särskilt relevant som lärdom: ett komplett QWORK-Z-kit med två T8-skruvar, muttrar och kopplingar hittades också för 259 kr, men eftersom LaskaKit-skruven och kopplingarna redan var köpta var det mer rationellt att köpa endast muttrarna. Den separata 4-pack-listningen gav rätt spec utan att dubblera fler delar än nödvändigt.

## eBay / HKGY01 — CANCELLATION PENDING / OUT OF STOCK

Order lagd 2026-09-03:
- 2 × flänsad T8×8 brass nut
- vald variant `T8 × 8 mm`
- 2 mm pitch / 4-start / 8 mm lead
- 2-pack
- faktiskt debiterat 67 kr

Den 2026-09-05 meddelade säljaren att varan var **out of stock** och bad köparen annullera. Köparen skickade annulleringsbegäran och eBay visar **`The cancellation is pending`**.

Detta är inte längre en aktiv leveransväg. Ersättningsköpet är gjort via Amazon.se/euroharry. Återbetalningen bokförs först när den faktiskt är verifierad i `COSTS.md`.

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

DMW hade tekniskt rätt variant men bara två exemplar kvar när köp skulle göras. eBay gav i stället ett komplett trepack till låg landad kostnad med importhanteringen inbakad.

Lärdom: den tidigare sökningen överviktade EU-butik som proxy för låg friktion. För commodity-delar ska Amazon/eBay sökas tidigt med hela variantspecen och faktisk checkout/importtext som gate.

## DigiKey — CLOSED / ORDERED

Köpt 2026-09-03. DigiKey absorberade PSU, endstops, lager och lågspännings-/elsmådelar i en enda order.

Låsta SKU-fällor:
- `HDR-60-24` = `1866-2249-ND`
- TE `3-350820-2` = `A27824-ND`
- `AIO-CSM12` = LV-gland
- `30-00416` och `30-00377` beställdes som meterware

Checkout:
- delsumma 789,58 kr
- svensk VAT 197,40 kr
- frakt 0 kr
- total **986,98 kr**
- UPS Worldwide Saver, DDP

Ingen fortsatt DigiKey-sourcing behövs för baslinjen.

## Motorer — CLOSED / ORDERED

5 × STEPPERONLINE `17HS19-2004S1` köptes via Amazon.se 2026-09-03:
- 59 Ncm / 84 oz-in
- 2,0 A
- 42×42×48 mm
- Ø5 mm D-axel
- 1 m kabel
- pack of 5
- visat orderpris **608,37 kr**
- Prime / fri frakt

StepperOnline direkt och eBay-spåren är därför inaktiva.

## Controller — CLOSED / ORDERED

**Elecrow Jackpot3 `CQA240812C2` köpt 2026-09-03.**
- controller efter rabatt: 69,44 €
- DDP Economy: 14,11 €
- checkout: 83,55 €
- faktiskt debiterat: **937 kr**

Jackpot2 var ett tidigare tekniskt router-first-alternativ men är nu endast historik. Controller-sourcing ska inte återöppnas.

## Router — CLOSED / ORDERED

**KATSU `101750` köpt via Amazon.se 2026-09-03.**
- 220–240 V
- 710 W
- variabelt varvtal
- cirka 64,8/65 mm kropp
- Makita RT0700-familjens formfaktor
- visat orderpris **620,00 kr**
- Prime / fri frakt

Vid leverans ska Elaire/Makita-style 1/8"-hylsan provpassas och runout kontrolleras.

### VEVOR `0700C` — BLACKLISTED / REPLACED

VEVOR-spåret är stängt. Användarens live-sida visade produkten som discontinued, och en officiell UK Product Safety Report för modell `0700C` klassade elchockrisken som allvarlig på grund av bristande isolation/elektrisk hållfasthet. KATSU `101750` är köpt ersättare.

## PLA — CLOSED / ORDERED

**3 kg PLA 1,75 mm köpt från PrintOnion 2026-09-06 för 426 kr.**

Behovet för LR4 är cirka 2,7 kg, så 3 kg täcker basbyggets utskrifter. Den tidigare 3DJake-baseline på 559 kr landat är ersatt och ska inte återaktiveras för basbygget.

## Motonet — ACTIVE fysisk kontroll

Rörspår: 2 × `88-7123`, Ø30×1,5×2000 mm. Själva köpet är fysisk: mät OD/rakhet innan köp och kapning.

## NVR — ACTIVE lokal kandidat

KJD12-familjen är kravmässigt tillräcklig om exakt levererad variant är 230 V, har lämplig märkström, dokumenterat schema och no-voltage-release. Clas Ohlson `50-2929`, KJD12 230 V/10 A, 299 kr är enkel kandidat. Köp först efter fysisk/layoutmässig dry-fit.

## Inte aktiva sourcingvägar

- eBay / HKGY01 — out of stock; cancellation pending; ersatt av Amazon.se/euroharry.
- DMW Industrietechnik — tekniskt rätt 16T, men bara två exakta exemplar kvar vid köp; ersatt av köpt POWGE/eBay-trepack.
- Roboter-Bausatz — svensk checkout blockerar leverans.
- Allegro `4Makers_pl` / `ABC-RC_pl` — faktisk seller-checkout blockerar Sverige.
- HomeDIYer — tekniskt användbar men onödig efter eBay/POWGE-köpet.
- Hellas Digital 16T — exakt komponent finns, men behövs inte efter köpet.
- StepperOnline direkt / motor-eBay — ersatt av Amazon.se-köpet.
- VEVOR NEMA17 — discontinued-spår; ersatt av Amazon.se-köpet.
- VEVOR `0700C` — discontinued/säkerhetsproblem; ersatt av KATSU.
- separat KEDU/CEM-specialorder — inte baseline.
- Sorotec — deferred tills verkligt fräsbehov.
- SUNLU 6 kg — borttaget; behovet är 3 kg.
- 3D Prima PLA — ersatt av PrintOnion-köpet.
- 3DJake PLA — tidigare baseline 559 kr landat; ersatt av PrintOnion 426 kr.
- Jackpot2 — historiskt controlleralternativ; Jackpot3 är redan köpt.
