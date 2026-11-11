# Sensorenhet — aktuell konstruktion och printunderlag

**Uppdaterad 2026-11-11.** Senaste konstruktionsspåret är **sidotorn v2** i [sidotorn.py](sidotorn.py), nu mekaniskt anpassat till CR Touch. Grundgeometrin kommer från commit `46f1f6b` 2026-11-09; probreferens, armfot, kabelurtag, horninfästning och magnetstopp har därefter ändrats, och hylsan har utgått. Det är ännu inte rapporterat provprintat eller monterat. Aktuell arbets- och verifieringsstatus ägs av [CHECKLIST.md](../../../CHECKLIST.md).

**CR Touch-anpassningen finns i CAD.** [crtouch.py](crtouch.py) läser en separat, källangiven tredjepartsreferens för sensorns kropp och stift. Armfoten har uppmätt 17,5 mm hålavstånd, öppet kontaktutrymme och bredare kabelspår. CR Touchen skruvas direkt i foten med kitets M3×6 underifrån; skyddshylsan utgick 2026-11-11 efter CR Touch-prov 1. [Kit- och konstruktionsunderlaget](../../../research/2026-11-10-crtouch-anpassning.md) skiljer tillverkaruppgifter, CAD-referens och verkliga mätningar. **Fysisk passning är fortfarande inte verifierad.** Kamerafickeprovets geometri är oförändrad.

## Vad konstruktionen innehåller

- Löstagbart tillbehör på befintliga M5-fästpunkter vid verktygsfästet. **Core** betyder V1E:s ursprungliga maskindel; sensorenheten är vårt tillbehör.
- Sidotorn med integrerad servoram, kameraficka, Pi-utrymme, två regulatorfickor, kabelvägar och avtagbar sidopanel.
- Separat CR Touch-anpassad probarm, utan skyddshylsa (beslut 2026-11-11). Hårda stopp och magnetparkering enligt [D020](../../../DECISIONS.md#d020--inga-armbrytare-hårda-stopp-tyngdkraft-och-kamerakontroll). Inga armbrytare eller KW11-hållare.
- Camera Module 3 Standard riktad rakt ned. Bilder får innehålla servo/dammsko som maskas bort; överlappande bilder ska täcka materialet enligt det överenskomna kameraflödet.
- **Utgått ur printplanen enligt D022:** fast lampdocka med två blinda M3-pilothål och asymmetrisk styrtapp. Separat skruvad G4-bärare är ritad som utkast i [lampor.py](lampor.py); lampor och socklar är utrymmeskuvert tills produkter valts och mätts. De gamla små LED-spåren finns kvar som preliminära kabelvägar, inte G4-fästen. Användningskraven ägs av [kameraunderlaget](../../KAMERA_ANHALL.md#eftermontering--demonterbar-lampmodul).
- Pi Zero 2 WH tar bilder; värddatorn gör den tyngre analysen. ADXL345 sitter på massiv bärare kopplad till övre maskininfästningen för vibrationsmätning. INMP441-mikrofonen sitter i en ram på sidopanelens insida (2026-11-11), med ljudhål Ø1,5 mm genom panelen och en utvändig försänkning Ø7 × 0,4 mm för dammnät eller ventildekal. Panelen vänder bort från fräsen, så spån blåser inte rakt i hålet, och mikrofonen byts med panelen utan att kameran rörs. Kortets bottenport läggs mot hålet med en ring skumtejp som tätning, så att mikrofonen hör utsidan och inte tornets hålrum. Ramens översida är helt öppen för de sex lödpunkterna; ledningarna går längs panelens insida upp till Pi:ns stiftlist. Kortmåtten 14 × 14 mm är nominella och mäts på levererad modul.
- Två LM2596 planerade: en för Pi/CR Touch, en för servot. **Justerskruven säkras med en klick smältlim efter inställning** (användarens val 2026-11-11), eftersom vibrationer annars kan vrida den. Mät utspänningen igen efter limningen och efter första långa körningen. Matning och valda Jackpot-pinnar beskrivs i [kopplingsunderlaget](KOPPLING_CORE_V0.md); komponenttillgång ägs av [BOM.md](../../../BOM.md).

Geometrins mått ägs av CAD-källan, inte av manuellt kopierade koordinater i denna text. Dagens servoprov bekräftar att rörelseomfånget räcker; se [mätloggen](../../../CALIBRATION.md#2026-11-10--fällservots-rörelseomfång-verifierat-på-bänk).

## Delar att bereda för utskrift

Detta är modellens delindelning, inte en färdig skivad printorder.

| Export från `sidotorn.py` | Antal | Avsikt |
| --- | ---: | --- |
| `torn.stl` | 1 | Torn, infästning, servoram och fasta stopp |
| `sidopanel.stl` | 1 | Avtagbart lock med hållfingrar för elektroniken |
| `arm.stl` | 1 | Rörlig CR Touch-arm med formad hornficka; provpassning återstår |
| `hornbygel.stl` | 1 | Kilbygel med två M3×10 i blinda plastgänghål; ingen ny muttertyp |
| `bricka.stl` | 2 | Distanser vid ADXL345 |
| `lampbarare-utkast.stl` | 1, senare | Preliminär bärare; sockeladapter, verkliga lampmått och värmeprov återstår |

`crtouch.stl`, `kabel.stl`, `hornskruvar-referens.stl`, `magnetstal-referens.stl`, kontaktkuvert, servo- och elektronikobjekt i sammanställningen är **referenser**, inte printdelar. Gamla `bltouch.stl` hör till det ersatta underlaget. STEP-sammanställningen visar både utfällt och parkerat läge för samma arm; det betyder inte två armar. Referensmodellens licens/attribution finns i [referenskatalogen](referenser/README.md).

Källan exporterar huvudsakligen i monteringskoordinater. Delarna måste orienteras för utskrift och läggas mot byggplattan före skivning; en monteringsmodell är inte automatiskt rätt printläge. Övriga lägen, lagerlast, stöd och material är inte slutligt beredda.

**Första lilla kamerafickeprovet är berett:** [jobb och provförfarande](../../../print/README.md). Det tas direkt ur aktuell torngeometri och har ett källmanifest. Det är ett passningsprov, inte ett godkännande av hela tornet.

**CR Touch har en egen provplatta:** [crtouch-passning.json](../../../print/crtouch-passning.json), med liten armfot. Den kan verifiera sensorns montage utan att hela armen eller tornet printas. Efter prov i PLA bereds eventuell slutdel i avsett material på nytt.

**Utgått enligt D022, printas inte.** Lampdockan har en liten kall provplatta: [lampdock-passning.json](../../../print/lampdock-passning.json), med tornutsnitt och modulens fot. Styrtappen hindrar uppochnervänd montering. Två M3×6 avses ge 4,8 mm grepp i plasten utan att nå hålbottnen; verkliga skruvar och printspel provas före slutprint. Provbiten har extra massiv rygg för stödfria lager; huvudtornets elektronikrum fylls inte igen.

## Hornficka och M3-bygel

Funktionskravet är en stabil, glappfri och servicebar anslutning till det befintliga hornet som tål några tiondelars måttavvikelse. Användarens förslag om klämning är inte ett krav på viss metod. **Aktuellt val är formad ficka och separat M3-kilbygel**, eftersom befintliga M3-typer ska användas utan nytt fraktköp. Hornets små hål lämnas orörda. Metodjämförelse och daterat underlag finns i [infästningsutredningen](../../../research/2026-11-10-servohorn-infastning.md).

[hornfaste.py](hornfaste.py) äger geometrin utifrån [användarens A–I-mått](../../../CALIBRATION.md#2026-11-10--servohornets-nav-första-måtten). Fickans botten, två sidostöd och ett bakre navanslag ger läget. Bygelns sneda yta pressar hornet mot stöden. Två M3×10 formar gänga i blinda Ø2,6-piloter i armkroppen. Skruvspetsarna belastar inte själva hornet. Ingen printad axeltandning eller uppborrning av originalhornet behövs.

Bygeln ska ha kvar klämväg efter kontakt. Fritt utrymme runt övriga ytor är justermån, inte avsedd presspassning. Det större navhålet avlastar navet i sidled; det är sidostöd och anslag som positionerar hornet. Rak avsmalning mellan mätpunkterna och spetsens rundning är modellantaganden. Referenshornet saknar verifierad inre tandning och återger bara de två uppmätta små hållägena.

Bygeln ligger på armens fria sida efter kontroll mot undre verktygsfästet. Magnetens stålskruv ligger bakom hornets platta arm; parkeringsstopp och magneturtag följer den placeringen. Hornet sätts i armen före montering på servoaxeln: för in det från den öppna sidan 0,5 mm ovanför botten och sänk sedan till anläggen. En separat ribba bevarar utfällda lägets mekaniska stopp. Detta ändrar inte D020:s princip med hårda stopp, magnet och kamerakontroll, men fysisk parkering och magnetkraft ska provas efter montage.

**Litet hornprov:** [horn-passning.json](../../../print/horn-passning.json) innehåller ficka och bygel, utan resten av armen. [Kontrollen](../../../print/horn-passning/kontroll-cad.json) prövar 81 kombinationer med oberoende ±0,2 mm avvikelse i de två breddmåtten, armens tjocklek och navdiametern. Den kontrollerar sättning, klämväg och skruvgrepp i CAD. Friktion, plastens hållfasthet/krypning och verkligt glapp är ännu inte verifierade. Glappfri infästning får inte anges som fysiskt godkänd före prov med det verkliga hornet.

## Lampmodulens service och begränsning

**Utgått ur printplanen enligt D022 (COB-list i stället för G4).** Texten nedan är historik; geometrin ligger kvar i CAD som reserv för en eventuell liten kamera-LED efter bildprov.

Kameran sitter kvar när lampmodulen lossas. I CAD prövas demontering med proben i mätläge: ta bort två skruvar, frigör styrtappen genom 1,2 mm rörelse framåt, sänk modulen 8 mm och för den åt sidan. Stäng av matningen efter att armen ställts i mätläge och före demontering. Detta är en geometrisk servicestudie; verkliga ledningar/kontakter och handgrepp återstår att prova. Sidopanelen kan kräva att lampmodulen tas bort först.

Den preliminära G4-bäraren breddar enheten längs balken till **101 mm** enligt CAD. Den ingår alltså inte i tornkroppens tidigare Y-gräns. Slitsarna är till för **utbytbara sockeladaptrar**, inte ett löfte om att en okänd G4-sockel passar direkt. Keramiksockel och eventuell metalladapter väljs efter verkliga delar. Plastens värmetålighet, kabeldragning, nedåtriktat ljus och reflexer kräver prov med vald lampa. Ingen varm lampa ska provas i PLA-passningsdelarna.

## Vad de digitala kontrollerna visar

- De återfunna STL-filerna från kl. 09:08 är ersatta som aktuellt probunderlag. Nu exporteras färsk CR Touch-anpassad geometri med giltighetskontroll och `manifest.json` som knyter källor och exportfiler till varandra. Kör `sidotorn.py --ut KATALOG` för komplett STEP/STL-underlag.
- [MONTAGE.md](MONTAGE.md) äger hur allt sitter fast, monteringsordningen, ledningslistan och provkörningen. [kontroll_montage.py](kontroll_montage.py) kontrollerar att verktyget når varje skruv i den ordningen.
- [kontroll_stiftlist.py](kontroll_stiftlist.py) kontrollerar exakt i CAD att varje planerat stift på Pi:ns stiftlist har plats för lödtenn och ledning under panelen, och att ledningarna kan gå ned till mikrofon, ADXL och regulatorer (genom tvärribbans kabelfönster). **Ledningarna löds direkt på stiften** (2026-11-11): raka instickskontakter behöver ca 16,5 mm plus böj men panelen ger 14,1 mm, och de kan vibrera loss. Stiftlistens läge (nedre långsidan, stift 1 mot −x) är härlett ur Pi Zeros layout och kontrolleras mot kortet.
- [kontroll_mikrofon.py](kontroll_mikrofon.py) kontrollerar exakt i CAD att mikrofonkortet, lödkanten och ledningsvägen till Pi:ns stiftlist inte krockar med torn eller panel, att ljudhålet är fritt och att tätningsringen har gods. Den avbryter med UNDERKÄND vid fel.
- [kontroll_crtouch.py](kontroll_crtouch.py) kontrollerar verkliga CAD-intrång, skruvstapel och rörelse i 2° steg. Avståndsgränsen i rapporten kan även utesluta kollision mellan provlägen för prob, stiftkuvert och kontaktkuvert mot CAD-tornet. Det gäller inte skanning eller en verklig flexibel kabel. Referensens egna skruvhuvudavvikelser redovisas separat som kvarstående fysisk kontroll.
- [kontroll_omgivning.py](kontroll_omgivning.py) räknar **exakta skärningsvolymer** (manifold3d) mellan torn, panel och armens hela rörelse (−150° till 0°, 2° steg) och Core, verktygsfästen, dammsko, kjol, servo och skanningens punktmoln. Den svarar GODKÄND eller UNDERKÄND på under en minut. Skanpunkter räknas först mer än 2 mm in, skanningens noggrannhet. Negativtest 2026-11-11: armen 10° förbi stoppen och tornet förskjutet 5 mm gav krock som väntat. Kräver skanningsdatan och körs därför lokalt, inte i CI.
- [granska_sidotorn.py](granska_sidotorn.py) undersöker armens svep, stopp, komponentutrymmen, kabelutrymme och närhet till skannad maskin/geometrireferenser. Den skriver mätresultat och använder sampling; den är inte ett fullständigt automatiskt godkännande. Skanning och referensfiler finns inte i Git; plats och kontrollsummor står i [skanning/README.md](skanning/README.md).
- [kontroll_lampor.py](kontroll_lampor.py) prövar lampbärarens gränssnitt, skruvar/mejselutrymme, styrtapp, en antagen 90° synfältskon och armens 150° rörelse mot bäraren/lampkuverten. [Rapporten](../../../print/lampdock-passning/kontroll-cad.json) skiljer exakt CAD-kontroll från demonteringens stickprov. Den godkänner inte fysisk optik, värme, valda socklar eller flexibel kabel.
- GitHub-flödet [`sidotorn-build123d.yml`](../../../.github/workflows/sidotorn-build123d.yml) bygger sidotornet med build123d 0.13.0 och kör mikrofon-, stiftlist-, CR Touch- och hornkontrollerna vid varje ändring. Grönt betyder att CAD:en hänger ihop, inte att delarna är fysiskt provade. Det äldre `core-build123d.yml` bygger bara historiska `core_enhet.py`.
- Ingen fysisk passning, skruvåtkomst, verklig kabelböj, magnetkraft eller monterad rörelse är verifierad enbart av dessa kontroller. Första provprinten används för att pröva just sådana passningar.

Inför print: följ nästa steg i [CHECKLIST.md](../../../CHECKLIST.md). Inför inkoppling: [provförfarandet](../nollpunkt/INKOPPLING_OCH_PROV.md). Kamerans kalibreringsprincip och den låga Y-listen beskrivs i [KAMERA_ANHALL.md](../../KAMERA_ANHALL.md).

## Tidigare konstruktionsspår

`core_enhet.py` är det äldre modulbygget med separat Pi-låda och brytarhållare. `core_sensorer_v0.scad` är en ännu äldre OpenSCAD-studie. `kw11_faste.py` och de gamla arm C-filerna är historiska underlag. De finns kvar som referenser, men deras STL/3MF och GitHub-artefakter är inte sidotornets utskriftsleverans.

Beslut D018:s princip om servicebarhet och original-Core gäller fortfarande. Sidotornet är senaste arbetsmodell, inte en genomförd eller driftsgodkänd ersättning. Tidigare granskningar och mått finns i [arkivet](../../../docs/arkiv/2026-11-09-status-och-sensorunderlag.md) och Git-historiken.

**Belysning (D022):** huvudljuset är tre BRIMETI COB-banor under horisontell understrut, se [`../../EL_BELYSNING_OCH_STOPP.md`](../../EL_BELYSNING_OCH_STOPP.md) och [LED-underlaget](../led/README.md). Lampdockan och G4-bäraren nedan har utgått ur printplanen; geometrin ligger kvar i CAD som reserv för en eventuell liten kamera-LED efter bildprov. **Matning (D023):** Pi, kamera, ADXL och CR Touch matas från övervakningsgruppen som lever efter maskinstopp, inte från maskinens brutna 24 V.
