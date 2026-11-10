# Sensorenhet — aktuell konstruktion och printunderlag

**Uppdaterad 2026-11-10.** Senaste konstruktionsspåret är **sidotorn v2** i [sidotorn.py](sidotorn.py), nu mekaniskt anpassat till CR Touch. Grundgeometrin kommer från commit `46f1f6b` 2026-11-09; probreferens, armfot, kabelurtag, hylsa och magnetbula har därefter ändrats. Det är ännu inte rapporterat provprintat eller monterat. Aktuell arbets- och verifieringsstatus ägs av [CHECKLIST.md](../../../CHECKLIST.md).

**CR Touch-anpassningen finns i CAD.** [crtouch.py](crtouch.py) läser en separat, källangiven tredjepartsreferens för sensorns kropp och stift. Armfoten har 18 mm hålavstånd, öppet kontaktutrymme och bredare kabelspår; den nya hylsan har kroppsspel och åtkomst till skruvarna. [Kit- och konstruktionsunderlaget](../../../research/2026-11-10-crtouch-anpassning.md) skiljer tillverkaruppgifter, CAD-referens och verkliga mätningar. **Fysisk passning är fortfarande inte verifierad.** Kamerafickeprovets geometri är oförändrad.

## Vad konstruktionen innehåller

- Löstagbart tillbehör på befintliga M5-fästpunkter vid verktygsfästet. **Core** betyder V1E:s ursprungliga maskindel; sensorenheten är vårt tillbehör.
- Sidotorn med integrerad servoram, kameraficka, Pi-utrymme, två regulatorfickor, kabelvägar och avtagbar sidopanel.
- Separat CR Touch-anpassad probarm och skyddshylsa. Hårda stopp och magnetparkering enligt [D020](../../../DECISIONS.md#d020--inga-armbrytare-hårda-stopp-tyngdkraft-och-kamerakontroll). Inga armbrytare eller KW11-hållare.
- Camera Module 3 Standard riktad rakt ned. Bilder får innehålla servo/dammsko som maskas bort; överlappande bilder ska täcka materialet enligt det överenskomna kameraflödet.
- Två förberedande LED-urtag som är öppna från undersidan, med ritade ledningsvägar till elektronik-/CSI-rummet. Ingen faktisk LED-produkt, lödanslutning, hållare eller diffusor är passningsverifierad. Eftermonteringens åtkomst ska kontrolleras före tornets print; utbytbar belysning beskrivs i [kameraunderlaget](../../KAMERA_ANHALL.md#belysning--minsta-möjliga-lösning-bedömt-2026-11-09-inte-inköp).
- Pi Zero 2 WH tar bilder; värddatorn gör den tyngre analysen. ADXL345 sitter på massiv bärare kopplad till övre maskininfästningen för vibrationsmätning. INMP441 har ännu ingen färdig integrerad placering i sidotornet.
- Två LM2596 planerade: en för Pi/CR Touch, en för servot. Matning och valda Jackpot-pinnar beskrivs i [kopplingsunderlaget](KOPPLING_CORE_V0.md); komponenttillgång ägs av [BOM.md](../../../BOM.md).

Geometrins mått ägs av CAD-källan, inte av manuellt kopierade koordinater i denna text. Dagens servoprov bekräftar att rörelseomfånget räcker; se [mätloggen](../../../CALIBRATION.md#2026-11-10--fällservots-rörelseomfång-verifierat-på-bänk).

## Delar att bereda för utskrift

Detta är modellens delindelning, inte en färdig skivad printorder.

| Export från `sidotorn.py` | Antal | Avsikt |
| --- | ---: | --- |
| `torn.stl` | 1 | Torn, infästning, servoram och fasta stopp |
| `sidopanel.stl` | 1 | Avtagbart lock med hållfingrar för elektroniken |
| `arm.stl` | 1 | Rörlig CR Touch-arm; servohornsinfästningen återstår före slutprint |
| `kapa.stl` | 1 | Ny CR Touch-hylsa; fysisk provpassning återstår |
| `bricka.stl` | 2 | Distanser vid ADXL345 |

`crtouch.stl`, `kabel.stl`, kontaktkuvert, servo- och elektronikobjekt i sammanställningen är **referenser**, inte printdelar. Gamla `bltouch.stl` hör till det ersatta underlaget. STEP-sammanställningen visar både utfällt och parkerat läge för samma arm; det betyder inte två armar. Referensmodellens licens/attribution finns i [referenskatalogen](referenser/README.md).

Källan exporterar huvudsakligen i monteringskoordinater. Delarna måste orienteras för utskrift och läggas mot byggplattan före skivning; en monteringsmodell är inte automatiskt rätt printläge. Hylsan är avsedd med öronen mot bädden enligt CAD-kommentaren. Övriga lägen, lagerlast, stöd och material är inte slutligt beredda.

**Första lilla kamerafickeprovet är nu berett:** [jobb och provförfarande](../../../print/README.md). Det tas direkt ur aktuell torngeometri och har ett källmanifest. Det är ett passningsprov, inte ett godkännande av hela tornet. Armens nuvarande Ø7,5-hål vid servoaxeln definierar inte en färdig koppling till servohornet; den infästningen återstår före armens slutprint.

**CR Touch har en egen provplatta:** [crtouch-passning.json](../../../print/crtouch-passning.json), med liten armfot och hela skyddshylsan. Den kan verifiera sensorns montage utan att hela armen eller tornet printas. Hylsan vänds med flänsytan mot bädden; efter prov i PLA bereds eventuell slutdel i avsett material på nytt.

## Vad de digitala kontrollerna visar

- De återfunna STL-filerna från kl. 09:08 är ersatta som aktuellt probunderlag. Nu exporteras färsk CR Touch-anpassad geometri med giltighetskontroll och `manifest.json` som knyter källor och exportfiler till varandra. Kör `sidotorn.py --ut KATALOG` för komplett STEP/STL-underlag.
- [kontroll_crtouch.py](kontroll_crtouch.py) kontrollerar verkliga CAD-intrång, skruvstapel och rörelse i 2° steg. Avståndsgränsen i rapporten kan även utesluta kollision mellan provlägen för prob, hylsa, stiftkuvert och kontaktkuvert mot CAD-tornet. Det gäller inte skanning eller en verklig flexibel kabel. Referensens egna skruvhuvudavvikelser redovisas separat som kvarstående fysisk kontroll.
- [granska_sidotorn.py](granska_sidotorn.py) undersöker armens svep, stopp, komponentutrymmen, kabelutrymme och närhet till skannad maskin/geometrireferenser. Den skriver mätresultat och använder sampling; den är inte ett fullständigt automatiskt godkännande. Skanning och referensfiler finns inte i Git och måste tillföras för en reproducerbar ny körning.
- Det befintliga GitHub-flödet `core-build123d.yml` bygger **core_enhet.py**, inte sidotornet. Dess gröna körningar får inte anges som godkännande för senaste modellen.
- Ingen fysisk passning, skruvåtkomst, verklig kabelböj, magnetkraft eller monterad rörelse är verifierad enbart av dessa kontroller. Första provprinten används för att pröva just sådana passningar.

Inför print: följ nästa steg i [CHECKLIST.md](../../../CHECKLIST.md). Inför inkoppling: [provförfarandet](../nollpunkt/INKOPPLING_OCH_PROV.md). Kamerans kalibreringsprincip och den låga Y-listen beskrivs i [KAMERA_ANHALL.md](../../KAMERA_ANHALL.md).

## Tidigare konstruktionsspår

`core_enhet.py` är det äldre modulbygget med separat Pi-låda och brytarhållare. `core_sensorer_v0.scad` är en ännu äldre OpenSCAD-studie. `kw11_faste.py` och de gamla arm C-filerna är historiska underlag. De finns kvar som referenser, men deras STL/3MF och GitHub-artefakter är inte sidotornets utskriftsleverans.

Beslut D018:s princip om servicebarhet och original-Core gäller fortfarande. Sidotornet är senaste arbetsmodell, inte en genomförd eller driftsgodkänd ersättning. Tidigare granskningar och mått finns i [arkivet](../../../docs/arkiv/2026-11-09-status-och-sensorunderlag.md) och Git-historiken.
