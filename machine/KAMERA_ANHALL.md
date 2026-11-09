# Core-kamera, Y-anhåll och kalibrering – fysisk design (ej monterat)

**2026-11-08 · Status: konstruktionsunderlag och öppna kontroller – INGEN verifierad montering.**

Program/mätlogik och användarflöde ägs av [cnc/docs/kamera-arbetsflode.md](https://github.com/kingkongola/cnc/blob/main/docs/kamera-arbetsflode.md), [kameraindexering 0033](https://github.com/kingkongola/cnc/blob/main/docs/beslut/0033-dubbelring-kameraindexering.md) och [kalibreringsutredning 0034](https://github.com/kingkongola/cnc/blob/main/docs/beslut/0034-kamerakalibrering-z.md). Detta dokument äger endast fysisk konstruktion och maskinbegränsningar.

## Beslut och tänkt funktion

- Kameran för arbetsstyckesregistrering, indexering och framtida oregelbunden nesting är **Raspberry Pi Camera Module 3 på den rörliga Core**. Hårdvaran är **beställd och exakt variant bekräftad via orderbild 2026-11-09: Raspberry Pi Camera Module 3 Standard**, Electrokit art. `41020240`. Raspberry Pi Zero 2 WH (`41022617`) och CSI-kabel 200 mm (`41020808`) finns i samma order. **Mottagning är inte bekräftad.** Ingen Tapo krävs för dessa arbetsflöden.
- Även vid en full geometrisk kamerakalibrering behöver en **känt mätt materialyta/plan** finnas för metrisk pixel-till-XY. Befintlig/planerad **BLTouch** kan efter fysisk verifiering användas för ytplanets Z eller trepunktsplan – kameran blir inte därmed en full 3D-skanner.
- **Y-anhållet:** användaren vill skjuta fram mycket långa skivor, t.ex. 2,4 m, mot en list **längs maskinens Y** utan obligatoriskt kortsidesanslag. En låg skruvad list kan monteras ungefär parallellt och rätas med befintligt `cnc anslag trimma`. Färdigtrimmad arbetskant ska ligga **så nära minsta verkligt användbara X** som möjligt; om listen står längre i negativ X skapas onödigt materialspill, i positiv X försvinner fräsbredd. **Exakt läge är EJ valt**.
- Skruvhuvuden måste vara försänkta och fria från fräsbanor; förlägg skruvarna på listens yttersida, aldrig i skärsvängen. Mät verkligt minsta Core-/dammsko-/kameraunderrede-X, fräsradie och motsvarande höjd/Z-svep före borrning. En lista vid X-min kan ändå kollidera med dammskon på tunna ämnen.
- Välj i första hand **låg, löstagbar/segmenterad list** med fri skivförflyttning i Y och gott stöd för långa ämnen. Kontrollera med den verkliga maskinen, med spindeln avstängd, över aktuella X/Y/Z och med hela verktygskedjan monterad.
- Befintliga historiska beslut om **två linjalanslag** i `cnc/docs/beslut/0002-fast-horn.md` och `0015-listorna-ar-linjaler.md` finns kvar; användaren har nu också uttryckt behov av **endast Y-list** för valfri Y-position. Fysisk ombyggnad/val av lösning återstår.

## Indexeringsmarkör

- Två grunda koncentriska gravyrspår runt samma **mekaniska styrhål på arbetsstycket**. Lägg i spill där det är säkert och återanvänd befintlig fräs/operation om möjligt. Exempeldiametrar på spårens centrumlinjer Ø12/Ø20 mm runt Ø6/Ø8 mm indexeringshål, ej fysiskt testade.
- Vid skivförflyttning: mekaniska pinnar bibehålls först; kamera jämför optisk förflyttning i passiv shadow mode. Ringen måste vara åtkomlig för kamera både före och efter förflyttningen. **En markör mäter inte oberoende vridning**; listans raka anliggning måste verifieras eller minst två åtskilda referenser användas.

## Kalibreringsfixtur – vald första metod, ej fysisk kalibrering

- **Valt för första iterationen: 2D-bildanalys med Z-kompensation.** Ta bilder av ett plant kalibreringsmönster vid flera kända **kamera–materialavstånd**. Utgå inte från en enda 2D-homografi som antas giltig vid alla Z. Kalibreringen ska ge metrisk pixel→XY för ett **känt arbetsplan på aktuell höjd**, med uppmätt osäkerhet.
- Ett plant **utskrivet A4 ChArUco-mönster**, utskrivet utan skalning och kontrollerat med skjutmått i **båda** riktningar, fästs på MDF eller annat plant underlag. Knyt tavlans XY till verifierade maskinkoordinater via oberoende referens/fixtur; ett godtyckligt placerat papper räcker inte för fräscentrums koordinater.
- Ta bilder från flera **kända MPos X/Y/Z** med stillastående Core. Kontrollera kamera/objektivets verkliga avstånd, bildfält och fokusområde vid leverans. Håll fokus definierat/låst per kalibrerad serie; förändrad fokusposition kan kräva ny kalibrering eller verifierad profil.
- **BLTouch avses ge materialytans Z** när prob, servoarm, elektrisk anslutning, offset och precision fysiskt är verifierade. Kamerans relativa höjd över materialet bestäms av Core-Z och det uppmätta ytplanet. Innan dess kan känd Z för provskivan användas. BLTouch mäter inte av sig själv full 3D-yta och kompenserar inte för optiskt perspektiv utan kalibreringen ovan.
- Kamerafästet ska vara styvt relativt Core, med säker frigång för dammsko, fräs, Y-anhåll, probe och kablar i hela relevant X/Y/Z. Fysiska offset/plan och verifierad modell finns ännu inte.
- Kontrollhoming är inte en kontinuerlig encoder; verifierad maskinposition för bildtagning får inte antas om steg kan ha tappats.

### Referensfixtur och offset till fräscentrum – konkretiserad 2026-11-08

Första kalibreringsfixtur är ett styvt plant A4-ChArUco-mönster (ingen skrivarautoskalning; kontrollmät i **X och Y**). Den optiska delen kalibreras med **låst fokus**. För att slippa manuellt uppskatta kamerans monterings-offset kan en **separat, godkänd** kalibreringskörning fräsa ett enkelt mönster av referenshål/markörer på kända G-kod-XY (t.ex. nio illustrativa punkter) som fotograferas från verifierade Core-positioner. De ger gemensamma referenser mellan kamera och verktygsaxel. Observera att G-kod-positioner inte automatiskt bevisar verklig hålposition: vid fysisk validering behövs oberoende kontroll av geometri, stegförlust och verktygskast.

Fixtur, referensmönster, fokusläge och fotografier på **flera Z-höjder** ingår i [CNC:s beslut 0034](https://github.com/kingkongola/cnc/blob/main/docs/beslut/0034-kamerakalibrering-z.md). Enhetens fäste måste förbli styvt så att offseten inte ändras efter kalibrering. **Inga referenshål har frästs eller mått verifierats i detta steg.**

## Kamerariktning vald 2026-11-08

**Core-kamerans optiska axel ska nominellt peka rakt ned, vinkelrätt mot ett normalt plant arbetsstycke**, inte avsiktligt mot fräsens ingrepp. Den äger optisk registrering, oregelbundna skivkonturer, indexering och resultatkontroll; **Tapo C200** är separat fast överblickskamera. **INMP441 + ADXL345** jämförs mot förväntat fräsingrepp som passiv övervakning. Undvik att ändra kameravinkel för att kunna se verktyget genom dammskon.

**CAD-krav:** kamera i styvt, kalibreringsstabilt fäste på gemensamma Core-basen, med lodrät optisk riktning som nominell parameter. Välj faktisk X/Y-offset, objektivavstånd, fri sikt, dammskofrigång och rörliga Z-gränser efter CAD-kollisionsprov och fysisk verifiering. Optiken kompenseras i Z och kalibreras; rak montering gör inte pixel→XY automatiskt exakt. Servoarmens lägen och kabelväg får inte skymma kameran i planerade bildlägen.

## Återfunna CAD-modeller som underlag för gemensam Core-enhet (2026-11-08)

**Ursprung:** befintliga CAD-filer checkades in i commit [59efbec6](https://github.com/kingkongola/lowrider/commit/59efbec6c1a6) **2026-11-05**. Användaren vill kombinera dessa med Core-kamera, accelerometer och mikrofon, servoarm, BLTouch-stift, två armändlägen och kablage på **befintliga Core-skruvar/fästen**. Detta är en konstruktionsinriktning, **inte** färdig CAD eller beslut om montering.

**Börja i Version C (direktdriven arm, utan fyrled):**

- Parametrisk källa: [`machine/delar/nollpunkt/fallarm_c.py`](delar/nollpunkt/fallarm_c.py) (`build123d`), som importerar delar från [`fallarm.py`](delar/nollpunkt/fallarm.py). Variablerna `PX/PZ, LX/LZ, XC/YC` och formgeneratorerna ger underlag för en gemensam, reproducerbar montering.
- Genererade STEP: [`fallarm_C_faste.step`](delar/nollpunkt/fallarm_C_faste.step), [`fallarm_C_arm.step`](delar/nollpunkt/fallarm_C_arm.step), [`fallarm_C_kapa.step`](delar/nollpunkt/fallarm_C_kapa.step); STL-varianter ligger bredvid. Färdigpreparerat [`fallarm_C.3mf`](delar/nollpunkt/fallarm_C.printa/fallarm_C.3mf) med [förhandsvisning](delar/nollpunkt/fallarm_C.printa/forhandsvisning.png). Enligt `sammanfattning.json` ca **3,32 h / 73,9 g PLA**, **inte faktiskt utskriftsprov**.
- [`kontroll_c.py`](delar/nollpunkt/kontroll_c.py) har utkast till kollisionssvep mot Core, Makita-fästen, dammsko, kjol och ett tidigare skannat punktmoln. **Kan inte köras reproducerbart ur git som det står**: hårdkodade lokala sökvägar till `/Users/bemca/...`, `/tmp/nollpunkt-prov0/cad/Core.stl` och `scan_M.npy`; **Core.stl och scan_M.npy finns inte i detta repos nuvarande träd**. Måste ersättas med spårade källor eller explicit bygg-/importsteg för att verifiera fri gång.
- Version C:s två modellerade fästpunkter har lokala koordinater **(y=43,95; z=64,25 och 125,25 mm)** samt en modellerad nedre klämskruv **(x=36,6; z=64,26 mm)**. Koordinaterna är i den **lokala fräsramen M**, inte maskinens MPos. Hålbilden bygger på dåvarande CAD och är **inte fysiskt inmätt**.
- Version C är byggd kring **tidigare V5/TP05C-prob med cylindrisk kropp Ø33 mm**. **BLTouch är inte en drop-in-del**: kontrollera faktisk BLTouch-variant, stifthöjd, skruvhål, kabelriktning och rörelse-/kontaktgeometri innan kåpa, arm och servostopp ändras. Tidigare version [`fallarm.py`](delar/nollpunkt/fallarm.py) med stag/vev är jämförelse, inte rekommenderad grund.

**Designprincip för sammanslagning (att CAD:a senare):**

1. **En gemensam bärande basplatta/rygg** på verifierade befintliga Core-/verktygsfästskruvar, så få nya fästen och kablage som möjligt; inga antagna nya hål i Core.
2. **Flera utbytbara funktionsmoduler** i stället för en monolitisk 3D-print: (a) direktdriven servoarm med BLTouch, egna stela stopp och två Omron-givare; (b) styv kamerabracket med fast avstånd till Core och egen optisk sikt; (c) **accelerometer styvt mot Core** och (d) mikrofon med akustiskt öppet men dammskyddat läge. Stora mekaniska vibrationer bör inte direkt färga mikrofonens luftljud, medan accelerometern måste kunna följa Core.
3. Eventuell Pi/ESP32, kontakter och dragavlastning är separata servicebara delmoduler under samma övergripande fäst-/kabelstrategi. **Placering och eltopologi är öppna.**
4. Säkerställ åtkomst till befintlig fräsverktygsklämma, fast verktygsmätarknapp, dammsko, Z-rörelse och full X/Y-reach; kameran ska kunna se markörer på material utan att servoarmen/skon skymmer. Kablage får inte gå i rörlig probarm utan nödvändig avlastning.
5. Bygg CAD **efter** att rätt original-Core-mesh/STEP och levererade sensormått samlats. Kör därefter reproducerbart kollisionssvep med både armens alla lägen och maskinens X/Y/Z, och jämför mot fysiken. Ingen dimension, strömförsörjning eller krockfrihet är ännu fastställd.

## Komplettering 2026-11-09: KW11-rullbrytare beställda och CAD-fästen integrerade

**Beställt och inte levererat:** 10 × QUARKZMAN `KW11-3Z-N` (rullspak, 1NO/1NC, 92,94 kr, fri Prime-frakt, beräknad ankomst **2026-11-14**). Omron från original-LowRidern sparas som reserv. **Gällande CAD har nu 11 unika STL/STEP-delar**, eftersom en ny universalhållare `kw11_hallare` printas **2 ×** och skruvas på varsitt kort integrerat fästöra på servokassetten. Kod [kw11_faste.py](delar/sensorer/kw11_faste.py), komplett montage [core_enhet.py](delar/sensorer/core_enhet.py), [grön CI](https://github.com/kingkongola/lowrider/actions/runs/42616662416). Ingen original-Core modifieras; kamera och Pi rörs inte vid servobyte.

**Avsiktligt ej godkänt:** KW11-rullspakarnas verkliga slag och aktivering av rörlig arm, separat hårdstopp i båda lägena, kabelanslutning och fysisk damm-/servohornfrigång. Den gröna CI-körningen bevisar **endast** intern CAD-mesh och att delarna inte överlappar modellens övriga solider. M2-hålbild för 8,5–9,5 mm är ett justerbart utkast tills de köpta exemplarens mått kan kontrolleras vid leverans.

## Gällande sensorenhet – build123d, modularitet och CAD-verifiering 2026-11-09

**Core betyder här befintlig V1E-del; den NYA konstruktionen heter sensorenheten.** Nuvarande [build123d-konstruktion](delar/sensorer/core_enhet.py), [modul-/utskriftskontrakt](delar/sensorer/README.md) och [kopplingsutkast](delar/sensorer/KOPPLING_CORE_V0.md) supersederar **OpenSCAD-studien nedan**. 10 separata moduler: bärplatta på samma två befintliga M5 som tidigare C-servofäste, öppningsbar kabelkåpa, servicebar SPMS664-kassett, lös BLTouch-arm, separat kamera, Pi-kapsling+lock+docka, rigid ADXL345-bricka och egen INMP441-pod på Pi-kapslingen. **Kamera/Pi behöver inte tas loss när servot byts.**

**[Grön CAD/3D-montage-CI](https://github.com/kingkongola/lowrider/actions/runs/42609388224)**: 10 STL och 10 STEP genereras av samma build123d-källa. Alla 10 STL är vattentäta med en komponent. Exakta BRep-test ger **inga korsningar mellan modulerna**, inklusive armen + förenklat BLTouch-hus i 7 vinklar från 0° till −90° mot våra övriga moduler och ritad servo. [Genererad GLB-översikt](https://github.com/kingkongola/lowrider/actions/runs/42609388224/artifacts/13669886409) innehåller den verkliga Core-referensmeshen, tool mounts, dammsko/kjol och separata nya moduler; den är **inte bevisad verklig passning**.

**Kvar P0 före arm-/maskinmontage:** 2 fysiska Omron + hårda anslag ännu inte integrerade i den nya mekaniken, servo-METALLHORN, flexible BLTouch-kabel och all X/Y/Z/kjol-frigång under fysisk drift. BLTouch använder 45,7 mm till utfällt stift enligt tillverkarritning som **utkast**, bekräfta faktiskt exemplar. Core-/dammsko-STL kontrolleras endast med **samplad yt-närhet**, inte en exakt kollisionsalgoritm. Fästskruvar, faktiskt servo, befintlig kåpa/verktygsfäste och dimensioner behöver fysisk jämförelse. **Endast bänktest/provprint av fristående kapslingar/kåpor är aktuellt, inte automatisk probning.**

## Första parametriska Core-prototypen incheckad 2026-11-09 (arkiverad OpenSCAD-studie) (test-CAD, inte färdig montering)

**Kod + provprintfiler:** [machine/delar/sensorer/core_sensorer_v0.scad](delar/sensorer/core_sensorer_v0.scad) och [README](delar/sensorer/README.md). Fem separata CAD-delar: `pi_bas`, `pi_lock`, `kamera`, `bltouch_mattjigg`, `bltouch_arm`. Ger **fysiskt provbara** kamerahållare och Pi Zero 2 WH-kapsling, samt BLTouch-arm som **endast är ett geometriskt utkast** utifrån direktdriven servoarm C. **Ingen fläkt** i denna passiva Pi-kapsling (temperatur ska mätas under verklig belastning). Alternativet bordsmonterad lång ljusarm är inte inbyggt; LED kan vid behov eftermonteras efter ljusprov.

**[Automatiskt CAD-prov på GitHub](https://github.com/kingkongola/lowrider/actions/runs/42599158774) grönt:** fem STL exporteras från incheckad OpenSCAD-källa och verifieras som vattentäta, enkelkomponents mesher med giltig positiv volym. Detta bevisar **inte** mekanisk passning, servohorn, skruvhål eller krockfrihet i riktig LowRider. [Kopplingsutkast](delar/sensorer/KOPPLING_CORE_V0.md) markerar alla oallokerade GPIO, regulator/strömskydd och kabelvägar.

**P0 före fysisk armmontering:** original-Core-mesh/STEP eller verifierade infästningspunkter, faktiskt BLTouch-hålmönster och stiftavstånd samt passning mot befintliga `fallarm_C_faste` och `fallarm_C_kapa`. Den gamla kåpan och basplattan är **inte omgjorda eller bevisat kompatibla** med den nya armen. Varje tänkt säker mätsekvens kräver dessutom elektrisk I/O-verifiering och fysisk rörelsegrind.

## 2,5D-flatbäddsskanning – historisk idé, inte mekaniskt krav

Historik 2026-11-08: undersökte kamera + BLTouch som höjdskanner; en framåtriktad prob med lägre Z än fräsens riskutsatta delar föreslogs för att undvika hinder. **Denna funktion är parkerad.** Den får **inte** styra servoarmens geometri, monteringsvinkel, stiftets försprång eller inköp i aktuell Core-design.

**Aktuellt krav:** armen måste kunna mäta valt Z-plan med frigång för verktyg, dammsko, bord och kablage i kända lägen. Minimera massa och antal delar. Återuppta skanning och säker rörelseplanering **endast om verkligt behov uppstår**.

**Kontroll före arm-CAD:** [beslut 0007](https://github.com/kingkongola/cnc/blob/main/docs/beslut/0007-hardvara-pa-sikt.md) strök BLTouch 2026-10-12 på grund av dess korta stift (~8 mm enligt dåvarande antagande) och önskat verktygsavstånd (~12 mm). Senare beslut överväger annan, utfällbar mekanik men **motsägelsen är inte geometriskt löst**. Mät faktiska probmått, verktygsspets, armens stopp och höjd i båda lägena innan BLTouch-fäste låses. **Inget löfte om fysisk kollisionsfrihet.**

## Beslut 2026-11-08 – en enda rund 3D-printad skruvbricka, identisk överallt

**Slutligt användarval:** alla brickor är **identiska och runda**. Brickans egen synliga runda form/kontrast är den maskinläsbara markören, med centrumhål för skruven. **Inga QR-koder, unika ID:n, dekaler eller individuella varianter**. Programmet känner redan **antal skruvar och deras planerade XY-positioner**; en enda brickmodell räcker till alla jobb. Målet är enkel robust OpenCV-detektion av cirkelcentrum, inte generella neurala nätverk.

**Prototypkrav:** enkel cirkulär optisk markör med definierad kontrast till vanlig träyta, läsbar vid aktuell kamera-Z och även vid rotation, damm och varierande belysning. Tidigare exempel Ø20 mm är **inte beslutat mått**. Markören måste optiskt kunna särskiljas från de **två frästa koncentriska indexeringsringarna** på arbetsstycket. En tunn bricka eller krage ska inte lossna, glida från skruvcentrum eller störa prob, fräs, dammsko och kamera. Undvik att printad plast ensam bär klämkraften: låt skruv och metallbricka/annan verifierad lösning hålla materialet, och fånga den optiska brickan mekaniskt. Beräkna keepout från dess **verkliga diameter och höjd**.

**Kontrollkontrakt:** identifiera N synliga brickor och jämför med N planerade skruvpositioner; **antalet är nödvändigt men inte tillräckligt**. Mät även varje mittpunkt med kalibrerad kamera och koppla entydigt till en planerad XY inom tolerans. Felplacering, saknad/extra markör eller låg bildkvalitet blockerar skarp körning. Kamera kan inte intyga att alla andra (omarkerade/dolda) skruvar saknas eller att skruven dragits åt. Se [CNC:s kameraflöde](https://github.com/kingkongola/cnc/blob/main/docs/kamera-arbetsflode.md).

**Status:** konceptbeslut, inte CAD-modellerad, utskriven eller verifierad detalj.

## Belysning – minsta möjliga lösning (bedömt 2026-11-09, inte inköp)

**Kameran är en IMX708 (Raspberry Pi Camera Module 3 Standard) på Core, nominellt rakt ned.** Den har liten sensor och gynnas av stabilt ljus. **Belysning är ett mätförhållande, men inte automatiskt ytterligare en produktfunktion.**

1. **Testa först befintlig arbetsbelysning och flyttbar lampa**, utan extra elektronik eller permanenta fästen. Fotografera plywood/äldre urfräsningar, synliga skruvbrickor och blankare beslag vid flera Core-positioner; kontrollera verkliga skuggor från bom, dammsko och fixturer.
2. Om testet visar att fast garagebelysning ger positionsberoende skuggor: **liten vit diffuserad LED vid kameran på Core**, gärna två små symmetriska ljuskällor runt dess siktfält i stället för en hård sidostråle. Ger ljus som följer kameran utan att en bom skymmer ett avlägset armfäste. Minimerad vikt/servicebehov är krav; inga faktiska dimensioner, ljusstyrkor, spänning, kabeldragning eller delar beslutade.
3. Undvik starka reflexer, skuggor och potentiellt LED-flicker; verifiera jämförbarhet med låst fokus och efter behov låst exponering/gain/vitbalans. Enbart samma lampplacering betyder **inte** färg- eller måttkonstans.
4. **Inga inköp, extra LED-drivrutiner eller CAD-fästen före fysisk bildjämförelse.** Kontrollera från start att fästet har tillräcklig optisk fri sikt och att det går att eftermontera litet ljus utan att krocka med servoarm, BLTouch, dammsko eller kablar.

**Konflikter i bilderna:** prova ett **nytt foto från annan Core-position** före separat riktad BLTouch-mätning. BLTouch behöver ett faktiskt oklart höjd/djupvärde och säker rörelseprövning; det är inte en allmän problemlösare för skuggor eller färger. Se [kameraflödets avgränsning](https://github.com/kingkongola/cnc/blob/main/docs/kamera-kod.md).

## Fysiska nästa steg

1. Inventera den **beställda Camera Module 3 Standard**, Raspberry Pi Zero 2 WH och CSI-kabel 200 mm, verifiera fysisk kontakt, räckvidd och dragavlastning före montering (inget ytterligare inköp är här beslutat).
2. Provmontera kartongattrapp/3D-printat tillfälligt fäste och mät kameras möjliga avstånd till materialplan samt full verktygs-/dammsko-/probe-kollision.
3. Provpassa låg Y-list och trimreserve utan att låsa MPos eller skruvposition; granska överhäng/säker stödning för 2,4 m lång skiva.
4. Provframställ kontrollmätt, maskinregistrerad A4-kalibreringstavla; samla bilder vid **flera kända Z-avstånd** och verifiera Z-kompenserad XY-mätning innan användning. Ingen full 3D-skanning.
