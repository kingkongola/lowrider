# Sensorenhet — aktuell konstruktion och printunderlag

**Uppdaterad 2026-11-10.** Senaste konstruktionsspåret är **sidotorn v2** i [sidotorn.py](sidotorn.py), senast ändrat i commit `46f1f6b` 2026-11-09. Det är ritat men ännu inte rapporterat provprintat eller monterat. Aktuell arbets- och verifieringsstatus ägs av [CHECKLIST.md](../../../CHECKLIST.md).

## Vad konstruktionen innehåller

- Löstagbart tillbehör på befintliga M5-fästpunkter vid verktygsfästet. **Core** betyder V1E:s ursprungliga maskindel; sensorenheten är vårt tillbehör.
- Sidotorn med integrerad servoram, kameraficka, Pi-utrymme, två regulatorfickor, kabelvägar och avtagbar sidopanel.
- Separat BLTouch-arm och skyddshylsa. Hårda stopp och magnetparkering enligt [D020](../../../DECISIONS.md#d020--inga-armbrytare-hårda-stopp-tyngdkraft-och-kamerakontroll). Inga armbrytare eller KW11-hållare.
- Camera Module 3 Standard riktad rakt ned. Bilder får innehålla servo/dammsko som maskas bort; överlappande bilder ska täcka materialet enligt det överenskomna kameraflödet.
- Pi Zero 2 WH tar bilder; värddatorn gör den tyngre analysen. ADXL345 sitter på massiv bärare kopplad till övre maskininfästningen för vibrationsmätning. INMP441 har ännu ingen färdig integrerad placering i sidotornet.
- Två LM2596: en för Pi/BLTouch, en för servot. Matning och valda Jackpot-pinnar beskrivs i [kopplingsunderlaget](KOPPLING_CORE_V0.md); komponenttillgång ägs av [BOM.md](../../../BOM.md).

Geometrins mått ägs av CAD-källan, inte av manuellt kopierade koordinater i denna text. Dagens servoprov bekräftar att rörelseomfånget räcker; se [mätloggen](../../../CALIBRATION.md#2026-11-10--fällservots-rörelseomfång-verifierat-på-bänk).

## Delar att bereda för utskrift

Detta är modellens delindelning, inte en färdig skivad printorder.

| Export från `sidotorn.py` | Antal | Avsikt |
| --- | ---: | --- |
| `torn.stl` | 1 | Torn, infästning, servoram och fasta stopp |
| `sidopanel.stl` | 1 | Avtagbart lock med hållfingrar för elektroniken |
| `arm.stl` | 1 | Rörlig BLTouch-arm |
| `kapa.stl` | 1 | Skyddshylsa runt BLTouch-kroppen |
| `bricka.stl` | 2 | Distanser vid ADXL345 |

`bltouch.stl`, `kabel.stl`, servo- och elektronikobjekt i sammanställningen är **referenser**, inte printdelar. STEP-sammanställningen visar både utfällt och parkerat läge för samma arm; det betyder inte två armar.

Källan exporterar huvudsakligen i monteringskoordinater. Delarna måste orienteras för utskrift och läggas mot byggplattan före skivning; en monteringsmodell är inte automatiskt rätt printläge. Hylsan är avsedd med öronen mot bädden enligt CAD-kommentaren. Övriga lägen, lagerlast, stöd och material är inte slutligt beredda.

## Vad de digitala kontrollerna visar

- Lokala STL-exporter från 2026-11-10 kl. 09:08 återfanns. Torn, panel, arm, hylsa och bricka kontrollerades i denna granskning: var och en är tät, består av en sammanhängande kropp och har positiv volym. Exporterna saknar ett sparat manifest som knyter dem entydigt till en källversion; skapa därför ny export från aktuell källa före printberedning.
- [granska_sidotorn.py](granska_sidotorn.py) undersöker armens svep, stopp, komponentutrymmen, kabelutrymme och närhet till skannad maskin/geometrireferenser. Den skriver mätresultat och använder sampling; den är inte ett fullständigt automatiskt godkännande. Skanning och referensfiler finns inte i Git och måste tillföras för en reproducerbar ny körning.
- Det befintliga GitHub-flödet `core-build123d.yml` bygger **core_enhet.py**, inte sidotornet. Dess gröna körningar får inte anges som godkännande för senaste modellen.
- Ingen fysisk passning, skruvåtkomst, verklig kabelböj, magnetkraft eller monterad rörelse är verifierad enbart av dessa kontroller. Första provprinten används för att pröva just sådana passningar.

Inför print: följ nästa steg i [CHECKLIST.md](../../../CHECKLIST.md). Inför inkoppling: [provförfarandet](../nollpunkt/INKOPPLING_OCH_PROV.md). Kamerans kalibreringsprincip och den låga Y-listen beskrivs i [KAMERA_ANHALL.md](../../KAMERA_ANHALL.md).

## Tidigare konstruktionsspår

`core_enhet.py` är det äldre modulbygget med separat Pi-låda och brytarhållare. `core_sensorer_v0.scad` är en ännu äldre OpenSCAD-studie. `kw11_faste.py` och de gamla arm C-filerna är historiska underlag. De finns kvar som referenser, men deras STL/3MF och GitHub-artefakter är inte sidotornets utskriftsleverans.

Beslut D018:s princip om servicebarhet och original-Core gäller fortfarande. Sidotornet är senaste arbetsmodell, inte en genomförd eller driftsgodkänd ersättning. Tidigare granskningar och mått finns i [arkivet](../../../docs/arkiv/2026-11-09-status-och-sensorunderlag.md) och Git-historiken.
