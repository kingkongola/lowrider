# Systemaudit — current state 2026-08-30

Syfte: kontrollera att LowRider-planen faktiskt går ihop mekaniskt, elektriskt och praktiskt — inte bara att BOM-raderna ser rimliga ut.

Status:
- **VERIFIERAT** — kan behandlas som projektstate
- **FYSISK GATE** — måste mätas/provas på verkliga delar
- **CHECKOUT GATE** — exakt frakt/total kan inte fastställas från indexerade sidor

## Samlad bedömning

Grundarkitekturen håller. Ingen audit har krävt byte av LowRider V4, 650×1250-arbetsyta, Ø30×1,5-rör, motorer, Jackpot3, HDR-60-24 eller VEVOR 0700C.

## VERIFIERAT — mekanik

- arbetsyta **650×1250 mm**
- X-rör **816 mm ×2**, Y-rör **1505 mm**
- strut-generator `819`, `front_wing_size=30`
- GT2-segment **999 / 1705 / 1705 mm = 4409 mm**
- 3 × drive pulley: GT2, 16T, 5 mm bore, 10 mm belt
- 6 × smooth idler, 5 mm hole, 10 mm belt
- 14 × 608-2RS installeras
- T8×8, 4-start, 8 mm lead; V1E minimum 145 mm
- StepperOnline `17HS19-2004S1` har rätt NEMA17/axelström/axeldimension

T8 400 mm-stången kapas först efter assembly-check; cirka **150–160 mm ×2** är praktiskt mål.

## VERIFIERAT — print

Printer är **Bambu Lab P1S, 256×256×256 mm**. V1E:s minimum 200×200×190 är redan uppfyllt. Ingen printer-capability gate.

Kvar före full sats:
- senaste LR4-filer
- diameterberoende delar = **30 mm**
- tool mount = **Makita/65 mm**
- `Z_Stub` + `Z_Nut` snabb testfit
- slicer-preview av bridges/unsupported features

## VERIFIERAT — styrning

- Jackpot3 + HDR-60-24 är elektriskt kompatibla
- Omron `SS-3GL13PT` kopplas NC via COM+NC
- standard-endstops är home/auto-square, **inte runtime hard limits**
- Elecrow Jackpot3 måste flashas/configureras före driven rörelse
- inventera data-USB-C och FAT32 microSD

## LIVE INKÖPSAUDIT

### LaskaKit — delvis grön, remmen röd

Direkt produktsida 2026-08-30 visar:
- idlers/T8/muttrar/kopplingar/kablage: tillgängliga i aktuell kontroll
- `LA190013C` 5 m / 10 mm fiberglass GT2: **slut**
- direkt produktsida visar även 2 m 10 mm-alternativet som **slut**

Äldre kategorisida visade felaktigt lager för 5 m-rullen. Direkt produktsida väger tyngre. Remmen ska därför sourcas separat eller återkontrolleras senare; ändra inte spec.

V1E:s egen Amazon-länk för LR4-bältet går till SeekLiny ASIN `B097T4DFM6`: **10 m, GT2/2 mm, 10 mm bred, gummi med glasfiberförstärkning**. Sverigepris/Prime-tillgänglighet är inte verifierbar från webindex och är checkout-gated.

EU-exakt fallback som är verifierat i lager: Technobots `6002-591`, 5 m × 10 mm, 2 mm pitch, fiberglass reinforced. UK innebär dock sämre friktionsfri EU-ekonomi, så Amazon-SE/annan EU-källa bör kontrolleras först.

### StepperOnline — grön

`5-17HS19-2004S1` är i lager via Germany warehouse och Sverige stöds. Frakt checkout-gated.

### DigiKey — grön

Exakt korg är variantverifierad. Två korrigeringar:
- Faston = **DigiKey `A27824-ND`**, inte Marketplace-dubbletten med MOQ 1000
- lägg till **Amphenol `AIO-CSM12`**, M12 / 3–6,5 mm / IP68 för ~4,8 mm 24 V-kabeln

Detta löser den tidigare saknade LV-förskruvningen med en riktig behövd del.

### KEDU — grön familj

Preferred family: **genuine KEDU KJD12-14**.
- 230 V/50 Hz coil option
- **15 A AC-3 / 18 A AC-1** enligt KEDU-datablad
- 6,3×0,8 Faston
- IP54
- emergency-stop button/cover finns som tillbehör

CEM har konkret genuin KEDU med svamp/kåpa och deras eBay-annons identifierar KJD12-14. Sverige-frakt checkout-gated.

Terminologi: **NVR/maskinstopp**, inte påstående att den hemmabyggda helheten är safety-rated E-stop.

### Allegro 16T — grön

`GT2-16T-5B_10mm_K` är exakt rätt: 16T, 5 mm bore, 10 mm belt, två låsskruvar. Sverige-frakt checkout-gated.

### Elecrow — grön

Jackpot3 `CQA240812C2`, $76.99, i lager. Landad Sverige-kostnad checkout-gated.

### Sorotec — grön

`L1S.M.0317` 3,175 mm single flute, 9 mm skärlängd, €3,70/st, tillgänglig. Rätt för commissioning och 5–6 mm struts.

## 24 V-kabelrörelse

HDR sitter fast medan Jackpot sitter på rörlig beam:
- 3 m 20 AWG 2-core som längdmarginal
- kapa efter full-travel dry-fit
- stor mjuk rörelseloop
- UL2464 är inte bevisad chain-flex; byt endast om verklig routing kräver snäv repetitiv böj
- M12-gland `AIO-CSM12`

## VEVOR 6,5 A — korrigerat

VEVOR:s 220–240 V-sida återanvänder texten “6.5A motor” från 120 V/800 W-varianten. 0700C-manualen anger EU-modellen som **220–240 V, 800 W** men ingen 6,5 A EU-märkström. 6,5 A används därför inte som EU-current-spec.

## 10 A GARAGEGRUPP — inte en blockerande gate

Garagegruppen är **10 A** och är redan praktiskt beprövad med svets. Plasma har däremot kunnat lösa säkringen. Det är starkare praktisk evidens än att enbart stirra på nominella amperetal.

CNC-kombinationen är cirka 800 W router + sannolik 1050 W DeWalt + liten controller-PSU och bedöms **inte som ett öppet projektproblem**.

Ny regel: ingen separat B10/C10-utredning eller belastningsprocedur krävs i förväg. Vid första samtidiga körningen görs vanlig sanity-check. Om säkringen faktiskt löser, utreds då orsaken. Ingen uppsäkring utan kontroll av fasta installationen.

## FYSISKA GATES

1. Motonet-rör: verklig OD/rakhet före kapning.
2. Bord: racking, planhet och stöd under LR4:s kantzon.
3. VEVOR/Elaire: collet-säte + runout.
4. DeWalt: bekräfta modell/typskylt innan modellunika AUTO-data låses.
5. KJD12/HDR: fysisk dry-fit i kapsling + terminalschema.
6. Full travel: 24 V + routerkabel + motor/endstop + vac-hose samtidigt.
7. Damm: slangavlastning, statisk jordväg, cyclone-can vakuumtålighet.
8. 230 V-box: PE-kontinuitet, dragavlastning, inga åtkomliga live-delar och NVR-test.

## CHECKOUT GATES

Spec klar; kvar är pris/frakt för:
- LaskaKit utan rem
- separat GT2 10 mm-remkälla
- StepperOnline
- DigiKey
- VEVOR
- Elecrow
- SUNLU
- Sorotec
- Allegro 16T
- CEM/eBay KJD12-14

Mer bred komponentresearch har nu låg marginalnytta. Den enda aktuella sourcingluckan är **10 mm GT2-remmen**, plus faktiska checkout-totaler.