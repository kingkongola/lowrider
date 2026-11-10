# Core-kamera, Y-anhåll och kalibrering – fysisk design (ej monterat)

**Konsoliderad 2026-11-10.** Denna fil äger kamerans fysiska användningskrav, Y-anhållet och kalibreringsprincipen. Konstruktion/printdelar ägs av [sensorenhetens CAD-underlag](delar/sensorer/README.md), aktuell status av [CHECKLIST.md](../CHECKLIST.md), mottagning av [PROCUREMENT.md](../PROCUREMENT.md) och verkliga mått av [CALIBRATION.md](../CALIBRATION.md).

Program/mätlogik och användarflöde ägs av [cnc/docs/kamera-arbetsflode.md](https://github.com/kingkongola/cnc/blob/main/docs/kamera-arbetsflode.md), [kameraindexering 0033](https://github.com/kingkongola/cnc/blob/main/docs/beslut/0033-dubbelring-kameraindexering.md) och [kalibreringsutredning 0034](https://github.com/kingkongola/cnc/blob/main/docs/beslut/0034-kamerakalibrering-z.md). Detta dokument äger endast fysisk konstruktion och maskinbegränsningar.

## Beslut och tänkt funktion

- Kameran för arbetsstyckesregistrering och indexering är **Raspberry Pi Camera Module 3 Standard** på sensorenheten vid rörliga Core, kopplad till Pi Zero 2 WH. Modellvalet är avgjort. Aktuell leveransstatus läses i ordermatrisen; den kopieras inte hit. Ingen Tapo krävs för dessa arbetsflöden.
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

**CAD-krav:** kamera i styvt, kalibreringsstabilt fäste på gemensamma Core-basen, med lodrät optisk riktning som nominell parameter. Välj faktisk X/Y-offset, objektivavstånd, fri sikt, dammskofrigång och rörliga Z-gränser efter CAD-kollisionsprov och fysisk verifiering. Optiken kompenseras i Z och kalibreras; rak montering gör inte pixel→XY automatiskt exakt. Servo och dammsko får synas och maskas bort; överlappande bilder ska tillsammans täcka den yta som ska avläsas. Armens kabel får inte fastna eller påverka kamerans kalibrerade läge.

## Mekaniskt underlag

Aktuellt sidotorn, modellens delindelning, digitala kontroller och printberedning beskrivs bara i [sensorenhetens CAD-underlag](delar/sensorer/README.md). Gamla arm C-, OpenSCAD- och modulbyggen är historik i [arkivet](../docs/arkiv/2026-11-09-status-och-sensorunderlag.md), inte alternativa printorder.

## 2,5D-flatbäddsskanning – historisk idé, inte mekaniskt krav

Historik 2026-11-08: undersökte kamera + BLTouch som höjdskanner; en framåtriktad prob med lägre Z än fräsens riskutsatta delar föreslogs för att undvika hinder. **Denna funktion är parkerad.** Den får **inte** styra servoarmens geometri, monteringsvinkel, stiftets försprång eller inköp i aktuell Core-design.

**Aktuellt krav:** armen måste kunna mäta valt Z-plan med frigång för verktyg, dammsko, bord och kablage i kända lägen. Minimera massa och antal delar. Återuppta skanning och säker rörelseplanering **endast om verkligt behov uppstår**.

**Kontroll vid fysisk armprovning:** [beslut 0007](https://github.com/kingkongola/cnc/blob/main/docs/beslut/0007-hardvara-pa-sikt.md) strök BLTouch 2026-10-12 på grund av dess korta stift (~8 mm enligt dåvarande antagande) och önskat verktygsavstånd (~12 mm). Senare beslut överväger annan, utfällbar mekanik men **verklig frigång är ännu inte fysiskt verifierad**. Mät faktiska probmått, verktygsspets, armens stopp och höjd i båda lägena innan BLTouch-fäste låses. **Inget löfte om fysisk kollisionsfrihet.**

## Beslut 2026-11-08 – en enda rund 3D-printad skruvbricka, identisk överallt

**Slutligt användarval:** alla brickor är **identiska och runda**. Brickans egen synliga runda form/kontrast är den maskinläsbara markören, med centrumhål för skruven. **Inga QR-koder, unika ID:n, dekaler eller individuella varianter**. Programmet känner redan **antal skruvar och deras planerade XY-positioner**; en enda brickmodell räcker till alla jobb. Målet är enkel robust OpenCV-detektion av cirkelcentrum, inte generella neurala nätverk.

**Prototypkrav:** enkel cirkulär optisk markör med definierad kontrast till vanlig träyta, läsbar vid aktuell kamera-Z och även vid rotation, damm och varierande belysning. Tidigare exempel Ø20 mm är **inte beslutat mått**. Markören måste optiskt kunna särskiljas från de **två frästa koncentriska indexeringsringarna** på arbetsstycket. En tunn bricka eller krage ska inte lossna, glida från skruvcentrum eller störa prob, fräs, dammsko och kamera. Undvik att printad plast ensam bär klämkraften: låt skruv och metallbricka/annan verifierad lösning hålla materialet, och fånga den optiska brickan mekaniskt. Beräkna keepout från dess **verkliga diameter och höjd**.

**Kontrollkontrakt:** identifiera N synliga brickor och jämför med N planerade skruvpositioner; **antalet är nödvändigt men inte tillräckligt**. Mät även varje mittpunkt med kalibrerad kamera och koppla entydigt till en planerad XY inom tolerans. Felplacering, saknad/extra markör eller låg bildkvalitet blockerar skarp körning. Kamera kan inte intyga att alla andra (omarkerade/dolda) skruvar saknas eller att skruven dragits åt. Se [CNC:s kameraflöde](https://github.com/kingkongola/cnc/blob/main/docs/kamera-arbetsflode.md).

**Status:** konceptbeslut, inte CAD-modellerad, utskriven eller verifierad detalj.

## Belysning – minsta möjliga lösning (bedömt 2026-11-09, inte inköp)

**Kameran är en IMX708 (Raspberry Pi Camera Module 3 Standard) på Core, nominellt rakt ned.** Den har liten sensor och gynnas av stabilt ljus. **Belysning är ett mätförhållande, men inte automatiskt ytterligare en produktfunktion.**

**Användarkrav, förtydligat 2026-11-10:** garaget är mörkt och befintlig belysning duger inte till kameran. **Egen belysning ska ingå.** Tidigare förslag att börja med enbart garage-/arbetsljus är därmed ersatt. Användaren vill ha rejält ljus och undersöker G4 LED; exakt lampa och antal är ännu inte valda.

Vi tar stillbilder med maskinen stilla, så exponeringstid är fortfarande en avvägning mot ljusstyrka. Användarens bedömning om cirka fem sekunder i det befintliga mörkret är inte en uppmätt exponering. Vibrationer ska ha lagt sig före bilden; jämnt ljus och tydliga kanter avgör det verkliga behovet. Daterade kandidater och räkneexempel finns i [belysningsutredningen](../research/2026-11-10-kamerabelysning-och-exponering.md).

1. **Välj och provbelys med egen LED-belysning.** Fotografera plywood/äldre urfräsningar, synliga skruvbrickor och blankare beslag; kontrollera verkliga skuggor från bom, dammsko och fixturer.
2. **Jämnt, ljusspritt vitt LED-ljus vid kameran**, gärna från två sidor. Ger ljus som följer kameran utan att en bom skymmer ett avlägset armfäste. Minimerad vikt/servicebehov är krav; exakta lampor, ljusflöde, matning och infästning är ännu inte låsta.
3. Undvik starka reflexer, skuggor och potentiellt LED-flicker; verifiera jämförbarhet med låst fokus och efter behov låst exponering/gain/vitbalans. Enbart samma lampplacering betyder **inte** färg- eller måttkonstans.
4. Kontrollera lampornas tillåtna spänning och verkliga yttermått före val. Fästet ska ha optisk fri sikt och belysningen kunna eftermonteras utan krock med servoarm, BLTouch, dammsko eller kablar. Ingen automatisk dimring krävs för första provet.

### Eftermontering — förslag diskuterat 2026-11-10, ej färdig konstruktion

Användaren vill kunna börja printa utan att lampornas leverans styr hela bygget. Förslaget är två små vita LED-delar som kan monteras från undersidan och bytas separat, med separat löstagbar diffusor (ett lock som sprider ljuset). Ledningar kan fördras till en åtkomlig kopplingspunkt bakom sidopanelen och lämnas frånkopplade och isolerade tills lamporna finns.

CAD har redan LED-urtag och ledningsvägar, men de är preliminära. Före huvudtornets utskrift behöver vi kontrollera att vald LED-typ, dess tillåtna kaplängd, lödningar och infästning ryms och går att montera senare. Om formatet inte kan väljas nu är en separat utbytbar lamphållare ett möjligt alternativ; sådan hållare finns inte i nuvarande modell. Ingen omprintsfri eftermontering är ännu verifierad.

En enkel möjlig matning är en egen gren för tvåledar-LED från den befintliga regulatorn för Pi/BLTouch, om LED-delarna är specificerade för den verkliga utspänningen och lastprovet visar tillräcklig marginal. Det är ett förslag, inte ett fastställt spännings- eller inköpsval. Kontinuerligt ljus utan programmerad dimring är första provet. Kabel- och matningsgränsen beskrivs i [kopplingsunderlaget](delar/sensorer/KOPPLING_CORE_V0.md#belysning--förberedelse-för-senare-montage).

**Konflikter i bilderna:** prova ett **nytt foto från annan Core-position** före separat riktad BLTouch-mätning. BLTouch behöver ett faktiskt oklart höjd/djupvärde och säker rörelseprövning; det är inte en allmän problemlösare för skuggor eller färger. Se [kameraflödets avgränsning](https://github.com/kingkongola/cnc/blob/main/docs/kamera-kod.md).

## Fysiska nästa steg

Aktuell arbetsordning och leveransstatus finns i [CHECKLIST.md](../CHECKLIST.md). Denna fil håller ingen separat arbetslista.
