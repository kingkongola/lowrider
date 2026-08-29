# Systemaudit — current state 2026-08-30

Syfte: kontrollera att LowRider-planen faktiskt går ihop mekaniskt, elektriskt och praktiskt — inte bara att BOM-raderna ser rimliga ut.

Status:
- **VERIFIERAT** — kan behandlas som projektstate.
- **FYSISK GATE** — måste mätas/provas på verkliga delar.
- **CHECKOUT GATE** — exakt frakt/total kan inte fastställas säkert från indexerade sidor.

## Samlad bedömning

Grundarkitekturen håller. Ingen audit har krävt byte av LowRider V4, 650×1250-arbetsyta, Ø30×1,5-rör, motorer, Jackpot3, HDR-60-24 eller VEVOR 0700C.

De tidigare farliga luckorna har flyttats från antaganden till uttryckliga bygg-/checkout-gates.

## VERIFIERAT — mekanik

- arbetsyta **650×1250 mm**
- X-rör **816 mm ×2**, Y-rör **1505 mm**
- strut-generator: `819`, `front_wing_size=30`
- GT2 **999 / 1705 / 1705 mm = 4409 mm**
- 5 m 10 mm fiberglass GT2 räcker
- 3 × drive pulley: GT2, 16T, 5 mm bore, 10 mm belt
- 6 × smooth idler, 5 mm hole, 10 mm belt
- 14 × 608-2RS installeras
- T8×8, 4-start, 8 mm lead; V1E minimum 145 mm
- StepperOnline `17HS19-2004S1`: rätt NEMA17/axelström/axeldimension

T8 400 mm-röret kapas först efter assembly-check; cirka **150–160 mm ×2** är praktiskt mål, inte två 199 mm-halvor.

## VERIFIERAT — print

Printer är **Bambu Lab P1S, 256×256×256 mm**. V1E:s minimum 200×200×190 är redan uppfyllt.

Alltså: **ingen printer-capability gate**.

Kvar före hela print-satsen:
- latest LR4
- alla diameterberoende delar = **30 mm**
- router mount = **Makita/65 mm**
- `Z_Stub` + `Z_Nut` snabb testfit
- slicer-preview av bridges/unsupported features

## VERIFIERAT — drivning/styrning

- Jackpot3 accepterar 24 V
- HDR-60-24, 24 V/2,5 A/60 W är rätt storleksklass
- Omron `SS-3GL13PT` kopplas NC via COM+NC
- endstops är home/auto-square-sensorer, **inte runtime hard limits** i standardconfig
- Elecrow Jackpot3 kräver flashning/config före driven rörelse
- microSD ingår inte dokumenterat; inventera FAT32-kort
- data-kapabel USB-C krävs för säker flashing

## VERIFIERAT — live inköpsrader 2026-08-30

### LaskaKit
5 m / 10 mm fiberglass GT2 är live i lager. Idlers, T8, muttrar, kopplingar och kablage är också tillgängliga i aktuell kontroll.

### StepperOnline
`5-17HS19-2004S1` är live i lager med Germany warehouse och Sverige stöds.

### DigiKey
Korgen är variantverifierad. Två viktiga korrigeringar:
- Faston ska vara **DigiKey `A27824-ND`**, inte Marketplace-dubbletten med MOQ 1000.
- lägg till **Amphenol `AIO-CSM12`**, M12 / 3–6,5 mm / IP68 för ~4,8 mm 24 V-kabeln.

Detta löser den tidigare saknade LV-förskruvningen.

### KEDU
Preferred family är nu **genuine KEDU KJD12-14**:
- 230 V/50 Hz coil option finns
- **15 A AC-3 / 18 A AC-1** enligt KEDU-datablad
- 6,3×0,8 Faston
- IP54
- emergency-stop button/cover finns som KEDU-tillbehör

CEM Elettromeccanica har live genuin KEDU med svamp/kåpa och deras eBay-annons identifierar delen som `KJD12-14`.

Vi kallar ändå helheten **NVR/maskinstopp**, inte certifierad safety-rated E-stop-krets.

## KORRIGERAT — 24 V-kabelrörelse

HDR sitter fast i bordets elbox medan Jackpot sitter på rörlig beam. Därför:
- köp 3 m 20 AWG 2-core som längdmarginal
- kapa efter full-travel dry-fit
- stor mjuk rörelseloop
- UL2464 är inte bevisad continuous-flex; använd riktig chain-flex endast om verklig routing kräver snäv repetitiv böj
- separat M12-gland `AIO-CSM12`

## KORRIGERAT — VEVOR 6,5 A

VEVOR:s 220–240 V-webbsida återanvänder marknadsföringstext “6.5A motor”. Samma 6,5 A används på 120 V / 800 W-versionen, där siffran är matematiskt rimlig. 0700C-manualen anger 220–240 V och 800 W men ingen 6,5 A EU-märkström.

**Slutsats:** 6,5 A ska inte användas som EU-routerström.

Med bekräftad DXV30SAPTA skulle märkteffekterna summera till ~1,91 kW, motsvarande ~8,3 A real power vid 230 V. Verklig RMS-ström/starttransient är fortfarande fysisk gate.

## 10 A GARAGEGRUPP — designförutsättning

Garagegruppen är **10 A**, inte 16 A.

Det är inte automatiskt ett blockerande problem, men marginalen är tillräckligt liten för att kräva verkligt belastningsprov.

Före riktig fräsning:
1. identifiera B10/C10/etc, jordfelsbrytare och delade laster
2. bekräfta DeWalt-typskylt
3. DeWalt ensam
4. controller + DeWalt AUTO + router utan skärlast
5. normal fräsning utan andra stora laster på gruppen

Om gruppen löser: ändra last-/kretsarkitektur. **Uppsäkra aldrig som workaround utan att fasta installationen verifierats.**

## FYSISK GATE — bord

Minimum footprint är 941×1563 mm; praktisk deck ~1000×1620.

160–180 × 90–100 cm begagnat bord är giltigt. På 90 cm djup överhänger deck ~50 mm per långsida; LR4:s rail/wheel/belt-clip-zon måste få verkligt lokalt stöd/infästning. En lös 11 mm OSB-kant räcker inte som bärande antagande.

## FYSISK GATE — damm

- bekräfta DeWalt-modell
- testa befintlig 48 mm ×2,1 m slang först
- slangens vikt får inte belasta Core/Z
- stockslangen är inte verifierat antistatisk; ordna definierad jordväg eller groundable hose före XPS/reguljär dammig drift
- stål-cyclone-can är inte automatiskt vacuum-säker; kontrollerat deformationstest krävs

## FYSISK GATE — router

VEVOR 0700C:
- 65 mm body är rätt mountklass
- 800 W / 220–240 V
- Elaire/Makita-style 1/8" collet har hög sannolikhet men exakt kombination saknar formellt kompatibilitetsdatablad

Provpassa collet och kontrollera runout innan riktig fräsning.

## FYSISK GATE — full rörelse

Före slutliga clips/remspänning ska maskinen nå alla fyra hörn + Z-extremer med samtidigt monterade:
- 24 V-kabel
- routerkabel
- stepper/endstop-kablar
- vac-hose

Inget får sträckas, kinka, bära kontaktlast eller falla in i rörelsezonen.

## 230 V gate

Före energisering:
- riktig KJD12-14/HDR dry-fit i kapsling
- exakt terminalschema
- PE kontinuerlig/oswitchad till DeWalt-uttaget
- korrekta Faston/crimps
- riktiga kabelgenomföringar/dragavlastning
- inga åtkomliga live-delar
- PE-kontinuitet och ingen L/N→PE-kortslutning
- NVR/no-restart-test med router frånkopplad

## CHECKOUT GATES

Specen är klar för:
- LaskaKit
- StepperOnline
- DigiKey
- VEVOR
- Elecrow
- SUNLU
- Sorotec
- Allegro 16T
- CEM/eBay KEDU KJD12-14

Det som återstår där är landad kostnad/frakt — inte ny komponentresearch.

## Nästa verkliga osäkerheter

Mer webbresearch ger nu låg marginalnytta för:
- Motonet-rörens faktiska rakhet/OD
- bordets verkliga vridstyvhet
- collet/runout
- DeWalt-typskylt
- kabel-/slangrörelse
- 10 A-gruppens beteende under verklig last

De ska mätas/provas.