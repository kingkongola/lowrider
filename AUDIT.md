# Systemaudit — 2026-08-29

Syfte: oberoende kontroll av att LowRider V4-planen inte bara är dokumentmässigt konsekvent utan faktiskt går att bygga, koppla och köra i den fysiska världen.

Statusnyckel:
- **VERIFIERAT** — stöds av aktuell primärkälla eller direkt geometri.
- **FYSISK GATE** — kan inte avgöras säkert före provpassning/mätning av verkliga delar.
- **KORRIGERAT** — tidigare plan innehöll ett konkret fel eller en för stark formulering.

## Samlad bedömning

Grundarkitekturen är sund. Ingen upptäckt kräver byte av maskin, arbetsyta, rördimension, motorer, styrkort eller routerspår.

Det fanns däremot flera integrationsluckor som kunde ha orsakat omköp eller ett dåligt bygge om BOM:en följdes mekaniskt. De viktigaste är kabelrörelse från fast elbox till rörlig maskin, exakt 30 mm-printvariant, strut-generatorinställning, infästning i deckens överhäng och oklar terminologi kring KJD12 som "nödstopp".

## VERIFIERAT

### Geometri

För 650 × 1250 mm användbar arbetsyta och 6,0 mm XZ-plattor ger aktuell V1E-kalkylator:
- X-rör: 816 mm ×2
- Y-rör: 1505 mm
- strut-input: 819 mm
- GT2: 999 + 1705 + 1705 = 4409 mm
- minimum bord: 941 × 1563 mm

5 m korrekt 10 mm GT2-rem räcker med cirka 591 mm nominell marginal.

### Rör

Ø30 × 1,5 mm stål ligger inom V1E:s LR4-krav: 29,5/30/32 mm OD, ±0,2 mm och minst 1,3 mm vägg. Två 2 m-rör räcker till 1505 + 816 + 816 mm.

### Motorer och drivning

StepperOnline `17HS19-2004S1` uppfyller kraven: NEMA17, 5 mm D-axel, 24 mm axellängd, 2 A och 1 m kabel. Jackpot3 har öppna 2,54 mm motorheaders, så fabrikskontakterna är praktiskt användbara.

LR4 kräver 3 × 16T/10 mm/5 mm drive pulleys, 6 × släta 20T-idlers för 10 mm rem, 14 × 608-2RS och två T8×8 Z-skruvar. Nuvarande spec matchar detta.

### Styrning och PSU

Jackpot3 accepterar 9–24 VDC och V1E anger minst 19 W. Mean Well HDR-60-24, 24 V/2,5 A/60 W, är därför elektriskt rimlig med god marginal för grundmaskinen.

### XZ-plattor

HaWiWe 6,0 mm XZ-plattor + HaWiWe LR4-skruvset är en avsiktlig EU-kombination, inte en oavsiktlig blandning. Provmontera ändå M3-skruvarna mot MGN-blocken innan slutdragning.

## KORRIGERAT / måste ändras i projektstate

### 1. Fast HDR-box → rörlig Jackpot: 1 m 24 V-kabel får inte vara låst

V1E:s standardlösning monterar PSU och styrkort på den rörliga beam/gantryn. Vår lösning flyttar HDR-60-24 till en fast KJD12-box på bordet men behöll cirka 1 m PSU-kabel i BOM:en.

Det är en integrationsmiss: kabeln måste nu följa Y-rörelsen och ha service-loop utan drag i kontakterna.

**Ny regel:** köp 3 m flexibel 20 AWG / ~0,52 mm² tvåledare som billig längdmarginal, men kapa/terminera först efter full-travel dry-fit. Om den verkliga rutten mot förmodan blir längre ska kabelarea/spänningsfall omvärderas.

### 2. Separat lågspännings-genomföring saknades

De två planerade M20-förskruvningarna går åt till 3G1,5 in/ut. 24 V-kabeln behöver egen mekanisk dragavlastning genom boxen.

**Ny regel:** välj en separat mindre kabelgenomföring efter uppmätt ytterdiameter på den faktiska 20 AWG-kabeln.

### 3. Printvariant måste vara exakt 30 mm

"Senaste LR4-delar" räcker inte som instruktion. LR4 har dimensionsvarianter för rören.

**Ny regel:** alla rail-/brace-/clip-delar med diameterstorlek ska vara **30 mm-varianten** för Motonet Ø30-röret. Kontrollera slicerfilnamn före långa prints.

### 4. Strut-generatorn behöver två låsta parametrar

För vår maskin:
- `strut_length = 819`
- `front_wing_size = 30`

V1E anger att generatorn avsiktligt gör slutkonturen cirka 0,5 mm mindre; 819 mm ska därför matas in i generatorn, inte användas som manuellt färdigmått på SVG:n.

### 5. 90 cm bord är fortsatt giltigt, men 50 mm decköverhäng måste bära maskinens kantzon

På ett 900 mm djupt bord med ~1000 mm deck blir överhänget cirka 50 mm per långsida. V1E monterar Y-rail/belt clips med den yttre bordskanten som gemensam referens.

**Ny regel:** deckens båda långkanter ska ha lokal bärighet och säker skruvinfästning där LR4 rullar/rail/belt clips ligger. Om befintlig bordsskiva slutar 50 mm in ska kanten vid behov få underliggande list/blockning eller genomgående infästning. Godkänn inte en lös 11 mm OSB-kant bara för att totala måttet stämmer.

### 6. Routerkabeln är också en rörlig kabel

VEVOR-kabeln måste följa Core/gantry tillsammans med övriga ledningar/slang. Dess fabriksledning får inte antas räcka innan bordet och elboxens placering är kända.

**Ny regel:** inga slutliga kabelclips före ett gemensamt full-travel-test med routerkabel, 24 V, motor/endstop och dammsugarslang på plats.

### 7. KJD12: kalla den inte säkerhetsklassad E-stop utan bevis

KJD12 är verifierad som tvåpolig elektromagnetisk NVR/start-stop med underspänningsutlösning, och varianter finns med röd emergency-stop-kåpa. Underlaget räcker däremot inte för att påstå att den valda varianten utgör en verifierad säkerhetsklassad nödstoppfunktion enligt maskinsäkerhetsstandard.

**Ny terminologi:** `KJD12 NVR/maskinstopp med röd stoppkåpa`. Den ska vara direkt nåbar från normal operatörsplats. Exakt variant, terminalschema och märkdata kontrolleras före håltagning/koppling.

### 8. Statisk jordning är ännu inte färdigdesignad

Den återanvända DeWalt 48 mm-slangen är inte dokumenterad som antistatisk. V1E varnar uttryckligen för statisk laddning i vac-hose.

**Gate före XPS/reguljär dammig körning:** antingen groundable/steel-ribbed hose eller en avsiktlig jordledare med definierad PE-anslutningspunkt och kontinuitetskontroll. HDR-60-24 är Class II och är inte jordpunkten.

### 9. Elecrow Jackpot3 kräver firmware/config innan motorprov

Elecrow-kortet är inte V1E-förkonfigurerat.

**Ny regel:** flasha V1E:s vid byggtillfället aktuellt testade FluidNC-paket och rätt LR4-konfiguration innan driven rörelse/homing provas.

### 10. Jackpot-boxen ska inte hamna i den slutna 230 V-boxen

V1E betonar luftflöde över Jackpot3 och rekommenderar board box på YZ_Min/beam. Vår fasta kapsling innehåller KJD12 + HDR + nätfördelning; Jackpot3 ligger separat på den rörliga beam/gantryn.

## Andra auditpasset — inköpsrad för inköpsrad

### 11. T8-stången: kapa inte slentrianmässigt i två lika ~199 mm-bitar

V1E kräver två T8×8-skruvar **145 mm eller längre**. En 400 mm-stång är därför ett bra köp, men två lika halvor ger onödigt mycket stång som sticker upp över Z vid full höjd.

**Ny regel:** utgå från cirka **150–160 mm per Z-skruv**, inte halva stången. Slutlig kaplängd bekräftas mot de verkliga delarna före kapning. Extra längd är mekaniskt tillåten men ger ingen funktionell vinst här.

### 12. GT2 5 m har en exakt fallback om lagret svajar

Låsta segment är 999 / 1705 / 1705 mm. Om LaskaKit 5 m-rullen `LA190013C` är slut kan **3 × 2 m av samma 10 mm fiberglass GT2-spec** användas: varje maskinsegment ryms på en egen 2 m-längd. Ingen skarv behövs.

### 13. 20 AWG-kabeln är elektriskt okej men inte automatiskt en drag-chain-kabel

Den valda LaskaKit 2-core UL2464-kabeln är nominellt 20 AWG / 0,52 mm² och cirka **4,8 mm OD**. Tre meter 20 AWG ger rimligt spänningsfall även vid PSU:ns fulla 2,5 A, men UL2464/PVC-specen i sig bevisar inte continuous-flex/drag-chain-rating.

**Ny regel:** använd stor avslappnad rörelseloop och undvik snäv repetitiv böj. Om den verkliga kabeldragningen kräver liten böjradie i kabelkedja ska kabeltypen bytas till uttryckligt continuous-flex innan slutmontage.

Den nominella 4,8 mm OD:n bekräftar också varför M20-genomföringen för 5–12 mm nätkabel inte ska återanvändas till 24 V-ledningen.

### 14. DigiKey fri frakt är inte verifierad förrän checkout säger det

DigiKey anger fri Sverige-frakt vid **615 kr** och 170 kr under gränsen. Nuvarande komponentkorg har uppskattats till cirka 622 kr **inklusive moms**. Hjälpsidan anger inte tydligt om 615-kronorsgränsen bedöms före eller efter moms.

**Korrigering:** behandla fri frakt som checkout-gated. Köp inte filler och räkna inte hem besparingen förrän varukorgen faktiskt visar 0 kr frakt.

### 15. Jackpot3 saknar en explicit microSD-rad i vår BOM

Elecrow anger att paketet innehåller Jackpot3-kort, fem 2-ledarpluggkontakter och sex självhäftande kylflänsar. **MicroSD-kort anges inte som inkluderat.** V1E säger att microSD fortfarande är den föredragna filvägen för G-code och rekommenderar >2 GB, FAT32, Class 4 bäst / upp till Class 6.

**Ny regel:** inventera först. Om inget kompatibelt kort redan finns, köp ett litet **4–32 GB FAT32 Class 4/6 microSD**. Undvik att köpa ett dyrt modernt high-speed/A1-kort bara för CNC:n; V1E beskriver sådana som mer problematiska.

### 16. Data-kapabel USB-C är en commissioning-dependency

Elecrow-kortet måste flashas. V1E:s felsökning pekar uttryckligen ut charge-only USB-kabel som vanlig orsak till utebliven USB-anslutning.

**Ny regel:** verifiera att en data-kapabel USB-C-kabel finns innan flashing. Det är en inventeringspunkt, inte ett automatiskt köp.

### 17. Endstops är inte runtime-limits som standard

V1E är explicit: LR4:s endstops är normalt endast aktiva under homing. De stoppar inte maskinen under vanlig G-code-körning om man inte gör en avancerad limit-konfiguration.

**Konsekvens:** de fem Omron-brytarna är auto-square/home-sensorer, inte kollisionsskydd och inte en ersättning för KJD12/maskinstopp eller operatörstillsyn.

### 18. Printförutsättningarna måste verifieras före 2,7 kg långa prints

V1E anger minst **200×200×190 mm** tillgänglig byggvolym, rekommenderar skew-kontroll och föreslår att `Z_Stub` + `Z_Nut` provprintas för passning innan stora delar. De varnar också för att Cura-baserade slicers kan brygga vissa interna features fel, särskilt Dust Skirt/YZ_Plate.

**Ny gate:** verifiera skrivare/byggvolym/skew, gör de två små passningsprintarna och granska bridges i slicer-preview innan hela satsen körs.

### 19. Jackpot3 kylning/kabeldragning

V1E säger att kablar ska gå **bredvid**, inte över Jackpot3, att antennen inte ska täckas och att anslutningar ska avlastas innan de lämnar board box. Fläkt är valfri; om en används ska den matcha PSU-spänningen.

**Ny regel:** official-style Jackpot3 board box + fri luftväg + kabelavlastning är del av standardmontaget. Köp inte fläkt innan drift visar behov.

### 20. Motoranslutning ska verifieras före första driven rörelse

StepperOnline-motorernas 2,54 mm-kontaktfamilj passar Jackpot3:s öppna headers, men färg/coil-pair och riktning ska ändå kontrolleras före normal jogg. Om en motor går fel håll: spänningslöst först, sedan vänd kontakt enligt V1E:s instruktion.

## FYSISKA GATES — får inte ersättas av mer webbresearch

1. Motonet-rör: mät OD, kontrollera rakhet/bucklor innan kapning.
2. HaWiWe-paket: inventera antal och fysisk passform mot BOM.
3. VEVOR/Elaire-collet: provpassa säte och kontrollera runout.
4. KJD12 + HDR: riktig dry-fit i 120×160×90-box; gå upp till större box om terminal-/böjradie blir trång.
5. Elboxplacering: KJD12 ska vara direkt nåbar och kablarna ska nå utan drag.
6. Bord/deck: kontrollera racking, planhet och lokal styvhet i LR4:s långkantsspår.
7. Komplett rörelseprov utan fräs: alla fyra hörn + Z-extremer med slang och samtliga rörliga kablar monterade.
8. Endstops: kontrollera NC-funktion och kabelavlastning före homing; behandla dem inte som runtime-limits.
9. Statisk jordning: kontinuitet/verifierad jordväg före XPS och regelbunden trä/MDF-körning.
10. 230 V: PE-kontinuitet, korrekt L/N-brytning enligt faktisk KJD12-variant, dragavlastning och inga åtkomliga spänningsförande delar innan energisering.
11. Jackpot3: kompatibelt microSD + data-kapabel USB-C + rätt firmware/config verifierat före första G-code.
12. Printar: byggvolym/skew/testfit/bridge-preview godkänt innan full sats.

## Kvar att auditera senare när delarna finns fysiskt

Det går inte att webverifiera bort toleranserna i:
- verklig rör-OD/rakhet
- router-collet-kona/runout
- exakt KJD12-panelvariant
- kabel- och slanglängder efter faktisk bordplacering
- bordets lokala vridstyvhet
- faktisk continuous-flex-belastning i vald 24 V-kabelrutt

De är därför uttryckliga mät-/dry-fit-gates, inte antaganden.