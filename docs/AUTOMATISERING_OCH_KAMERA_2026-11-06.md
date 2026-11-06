# Pågående idéarbete: självmatande LowRider, vakuum, prob och maskinseende

**Datum:** 2026-11-06  
**Status:** koncept / provplan. Inga lösningar är beslutade, monterade eller driftsatta genom detta dokument.  
**Ekonomi:** låga merkostnader prioriteras; tidigare uttalat tak **1 500 kr för automatisk verktygsväxling**, *inte* en verifierad totalbudget för alla uppgraderingar.  
**Kanonisk uppdelning:** detta repo äger verklig hårdvara, mekanik, infästning och kalibrering. [`kingkongola/cnc`](https://github.com/kingkongola/cnc/blob/main/docs/kamera-prob-och-skanning.md) äger jobblogik, vision-integration, G-kod, loggning, riskkontroll och analys. Ändra inte låsta beslut i `DECISIONS.md` utan ett nytt explicit beslut.

## 1. Problemet, inte lösningsförslagen

Målet är en CNC som i ökande grad kan:
1. **Observera** verkligt arbetsstycke, verktyg och bearbetning.
2. **Referera** materialets läge och höjd till maskinens koordinater, även efter att skivan flyttats.
3. **Hålla fast / släppa** arbetsstycket säkert.
4. **Mata fram / indexera** längre material än arbetsområdet.
5. **Byta verktyg**, mäta verktygslängd och verifiera att verktyget sitter säkert.
6. **Dokumentera avvikelser**, men aldrig förväxla bilder, stegräknad position eller en trådlös sensor med säkerhetscertifierad maskinövervakning.

Komponenterna är utbytbara. Kamera, BLTouch, fysisk Z-knapp, drivskruv och vakuum är möjliga sätt att uppfylla funktionerna, inte mål i sig. Bygg i små verifierbara delsteg.

## 2. Maskinens förutsättningar och befintliga delar

- **LowRider V4**, KATSU 101750 (cirka 65 mm), Jackpot3/FluidNC, Bambu P1S för CAD-/hållardelar. Verifierade axelgränser och frigångar läses från aktuell maskinkonfiguration och `CALIBRATION.md`, inte historiska uppskattningar i README.
- **Tapo C200** är enligt användaren ansluten till nätverket 2026-11-06 och har **kamerakonto aktiverat**. RTSP-video/-ljud måste fortfarande testas på datorn; närfokus är inte verifierat.
- **Google Coral M.2 Edge TPU** sitter i HP EliteDesk 800 G3 Mini:s tidigare Wi-Fi-plats; inte verifierat i detta dokument att drivrutin och runtime fungerar. Lokal inferens kan köras där, men vanlig OpenCV bör testas först. Coral är endast för kompatibla kvantiserade/kompilerade modeller.
- **ESP32-S3** finns; **INMP441**-mikrofoner är beställda enligt användaren. De är tänkta för ljudanalys, inte nödvändiga för kameravalet.
- **Spektrum SPMS664** servo finns. Kandidat för fysisk fällarm.
- Grannen har erbjudit en **BLTouch-liknande sensor**; exakt modell, elektriska nivåer, stiftlängd och skick måste identifieras på den verkliga prylen innan CAD/inkoppling.
- **Fast Z-verktygsmätarknapp** planerad, se CNC:s `docs/beslut/0007-hardvara-pa-sikt.md`. Den behövs även om BLTouch används på armen, för att mäta *frässtålets* längd efter byte.
- Garagedrivning: användaren har en **Genie garageportsöppnare med skruvdrift**. Modell, skruvslag, styrning, vridmoment, hastighet och säkerhetsfunktioner är ännu okända.

## 3. Kamera – randvillkor innan hårdvaruval

### Primära arbetsuppgifter

**A. Överblick och ljud** (befintlig Tapo, fast montage): övervaka arbetet, upptäcka tydliga avvikelser, dokumentera och synkronisera med körlogg.

**B. Maskinvision vid arbetsstycket** (ytterligare kamera *endast om provet kräver*): lokalisera materialkanter, referenshål/markörer, synliga skruvskallar och klämmor; registrera materialets XY-läge/rotation; underlätta inspektion. Försök med smådelsskanning kräver separat 3D-metod. En kamera ersätter inte kontaktprobens Z-mätning.

**C. Säkerhetskritik:** Kamera får inte ensam godkänna att en fräsbana är fri från skruvar och klämmor. Ocklusioner, spån, reflexer och missade detektioner ger falska negativa. Om vakuumfastspänning ersätter skruvar sjunker värdet av särskild skruv-AI.

### Dimensionerande krav för en eventuell kamera på Core

| Egenskap | Initialt krav eller mål | Verifieringsmetod |
|---|---|---|
| Arbetsavstånd | **Circa 100–300 mm** från lins till yta, *förslag*, inte mätt frigång | Fysisk provmontering med full Z-rörelse, höga ämnen och dammsko |
| Fokus | Skarp stillbild på verkligt arbetsavstånd, **låsbar fokusposition** för mätning | Fokustest + fotografera kalibreringsmönster flera gånger |
| Upplösning | **Minst 5 MP** kandidat, **12 MP** intressant för översikt av litet område; upplösning sekundär till optik | Skruv-/kantdetaljer i faktiska bilder |
| Bildfält | Tillräckligt för 2+ markörer eller rutnätsvis skanning; hellre kontrollerat normalfält än fisheye | Mät mm/bild vid monteringshöjd; testa registeringsöverlapp |
| Repeterbarhet | **Föreslaget acceptanstest:** XY-fel högst ±0,5 mm på osedda referenspunkter | Kalibrering, repeterade mätningar över hela relevant fält, olika Z-höjder |
| Slutare / rörelse | Stillbilder när maskinen står stilla, spindeln av för kalibrering; global shutter ej huvudkrav | Testa rolling-shutter-/vibrationsartefakter |
| Kalibrering | Kameraintrinsik, distorsion, kamerans offset till verktygsaxel, XY-planets höjd och dokumenterat osäkerhetsmått | Rutnät eller AprilTag/ChArUco; jämför fysisk maskinmätning |
| Mekanik | Låg vikt, styvt fäste, spånskydd, sidobelysning, ingen kollision eller skymd prob | Full-travel-test och repetertest efter homing |
| Datagränssnitt | Stillbilder lokalt via USB/UVC, CSI/Pi eller Wi-Fi; inget krav på realtidsvideo | Tid till bild, paketförlust, överföringsstabilitet |
| Drift | Får fungera utan moln; mjukvaran ska kunna köras utan kamerasensor | Offline-prov |
| Kostnad | Håll merkostnad låg, börja med redan ägd Tapo | Inga inköp före första experimentet |

**Viktig koordinatregel:** Homografi från en enda bild gäller ett bestämt plan. Ändrad materialtjocklek/Z-höjd ger perspektivfel om man inte korrigerar med känd höjd, per-höjd-kalibrering eller rätt kameramodell. Kamera på Z-vagnen har dessutom dynamiskt avstånd till materialet. Skilj *detektion* från *metrologi*.

### Kameraalternativ, ännu ej inköpsbeslut

- **Tapo C200:** redan ägd; bra första överblickskamera/ljud, men fast fokus, optisk närgräns okänd och PTZ måste låsas vid kalibrering.
- **Raspberry Pi Camera Module 3 standard**: 12 MP, IMX708, motorfokus cirka 10 cm till oändligheten, kontroll över fokus och 66° horisontellt fält. Finns i Sverige (Electrokit hade listat 339 kr 2026-11-06). Kräver Raspberry Pi, CSI-adapterkabel för Zero/Zero 2 och ström; **Pi Zero 2 W var slut hos Electrokit** vid kontrollen. Normallins, inte Wide/NoIR, är förstaval *om* Pi-plattform väljs.
- **5 MP USB/UVC, fokus justerbart/autofokus:** kan vara **enklare än Pi/ESP32** om USB kan dras i befintlig kabelkedja till garage-PC. Kontrollera verklig optisk närgräns, tillgång till fokuslås i Linux och vikt innan köp.
- **Waveshare ESP32-S3 + OV5640**: potentiellt färre komponenter och Wi-Fi direkt på Core; begränsad mjukvaru-/bildkontroll och oklar närgräns för **den levererade linsen**. Avfärda inte, men köp inte enbart på 5 MP/specifikation.
- **Lös OV5647 till Raspberry Pi** (CSI, ofta fokus 1 m till oändlighet) eller en generisk kamera med okänd lins är inte lämpliga förstahandsval för närbilder.

Valmetod: först pröva Tapo med testmönster/skruv på arbetsstycket. Om den inte uppfyller behoven, pröva en **styvt monterad närbildskamera**. Välj sedan USB om det ger lägst total komplexitet, eller Pi Camera 3 standard om CSI/wifi ger tydlig fördel. **Raspberry Pi, ESP32 och USB är transport-/värdval, inte primärt kamerans optiska kvalitet.**

### Bildanalys på garderobsservern

Kamera → stillbild med tidsstämpel/metadata → OpenCV och eventuell **egen ML-detektor** på HP/Coral → positioner med källa, osäkerhet och koordinatram → CNC:s befintliga hinder-/registreringsmodell.

Egna skruv-/klämdetektorer kan tränas med bilder från *det faktiska bordet*. Multimodala AI-agenter kan föreslå bounding boxes/masker, men automatiskt genererade etiketter måste granskas; modellfel kan vara korrelerade. Separera tränings- och testbilder **per jobb/tillfälle**, inte bara slumpmässiga närliggande bildrutor. Använd svåra negativa exempel och mät särskilt **missade skruvar**, inte bara medelprecision. Coral kräver kompatibel TFLite-modell, full heltalskvantisering och Edge TPU-kompilering. Använd inte en okontrollerad detektor som enda hinderbevis.

## 4. BLTouch på servoarm kontra egen XYZ-prob

**Ny arbetsidé:** använd grannens BLTouch på den **befintliga SPMS664-fällarmsprincipen**. Den är inte ett mekaniskt drop-in-byte mot den hittills modellerade cylindriska proben.

- BLTouch kan finna materialkanter i X/Y genom att leta efter **Z-nivåövergångar** mot offerskivan; även vissa hål kan hittas uppifrån. Repetera med minskande stegstorlek. Det går däremot inte att mäta en vertikal sidovägg direkt eller säkert känna ett dolt underhäng. Små skruvar, spån och utstickande ämnen kan ge falska övergångar.
- BLTouch kan göra Z-höjdkarta; separat fast verktygsmätarknapp mäter fräsens längd.
- Fällarmen ska ha **hårt mekaniskt nedre stopp** för repeterbar geometri, **verifierat uppfällt läge** och säkert beteende vid strömbortfall. Stiftet måste också fällas in, utan att fräsen/dammsko kolliderar.
- Granska [`fallarm_c.py`](../machine/delar/nollpunkt/fallarm_c.py) (direkt på servo), [`fallarm.py`](../machine/delar/nollpunkt/fallarm.py) (fyrled) och krockskripten som inspirations- och provunderlag. **Versionerna är studier, inte testade produkter.** Gör om CAD utifrån det faktiskt erhållna BLTouch-kortets mått, slaglängd och kablar.
- **Beslut krävs efter test:** om BLTouch ger tillräckligt god kant-/hålregistrering behöver vi inte tillverka den ursprungliga 3D/XYZ-proben. Behåll den som alternativ för vertikala sidoytor, invändiga väggar eller XY-precisionskrav som BLTouch inte klarar.
- Probing ska ske på maskinkontrollerns tidskorrekta ingång med verifierade nivåer/signallogik; inga antaganden om BLTouch:s 5 V/3,3 V-kompatibilitet med Jackpot. Undvik att dra direkt till fel ingång innan elschema granskats.

## 5. Vakuumfastspänning i stället för skruv

**Möjlig hög marginalnytta:** slippa skruvar och snabbt kunna släppa/återfästa arbetsstycket. Inspirationskälla: Izzy Swan och ett [modulärt 3D-printat vakuumbord för LowRider V4](https://forum.v1e.com/t/3d-printed-modular-vacuum-workholding-table-for-lr4-or-anything-for-that-matter/50261).

Börja inte med hela bordet: **en liten separat vakuumzon** med frästa kanaler, utbytbar/plan yta och cellgummitätning runt ytan. Testa med olika plywood (porositet/läckage), spånskivor, ojämnheter, liten kvarvarande detalj och genomfräsning. Hållfasthet bestäms av **tryckskillnad × verklig tätt omsluten area** och friktion, inte av nominellt pumpwatt. Exempel: 10 kPa × 0,12 m² = 1 200 N *idealt* nedåtriktad kraft, före läckage och dynamik; inget löfte om motsvarande sidokraft.

- Vakuum **ersätter inte sidostopp** som ska ta skärkrafter och förhindra glidning.
- Vanlig grovdammsugare kan användas för **kort kontrollerat prov**, men måste tåla reducerat luftflöde och ha separat spånutsug vid fräsning. Börja med tryckgivare, läckagetest och överhettningskontroll.
- Automatisk matning kräver av/på, verifierat fastspänd/lossad skiva, skydd mot oavsiktligt återpåslag och mekaniska anslag/klämmor.
- **Genomfräsningar bryter tätningen.** Planera zonindelning, flikar/skin-onion eller en lösning där detaljer inte kan lossna.

## 6. Automatisk frammatning av långa skivor med Genie

Idé: bearbeta en del av en ca **2400 × 800 mm** skiva, dra eller mata fram med tillgänglig Genie skruvdrift, lås och registrera om – repetera.

Maskinens faktiska fräsbara bredd är **mindre än 800 mm** (historiskt uppmätt cirka 640 mm för X); en 800 mm skiva går därför **inte att bearbeta över hela bredden** i en enda XY-uppställning. Det går inte att lösa med bara frammatning i längdled. Första försöket bör använda en skiva smalare än uppmätt fräsbar bredd. Kontrollera stöd för 2,4 m längd och hur infästning på Genie-vagnen sker utan att skivan vrids.

**Skilj matningsmotor från mätsystem**: Genie flyttar grovt, sedan skall skivan mekaniskt styras/låsas och positionen mätas på nytt med två långt separerade referenser (probhål eller kameramarkörer) före nästa CNC-rörelse. Genies inbyggda säkerhetssystem får inte kringgås. Gör en separat riskanalys för klämning, ändlägen, bakmatning och samverkan med CNC:s rörelsevolym.

Provsekvens (utan skärning): lyft fräsen → bekräfta safe Z → frigör vakuum/klämma → flytta en begränsad sträcka → lås/skapa vakuum → mät referenser → verifiera felgräns → endast därefter tillåt fortsatt jobb.

## 7. Automatisk frässtålväxling inom låg budget

- Riktig pneumatisk ATC-spindel och kommersiella ATC-kit avförs **som inköp nu**; sannolikt långt över budget 1 500 kr.
- Behåll KATSU och prova konceptet **fast station + motordriven hylsa + mekaniskt spindellås**. Först manuell bytesstation, sedan motorstyrt test utan skärning.
- Kritiska problem: spindeln helt stilla och spänningslös under byte; säker axellåsning; korrekt spännmutter-/hylsgeometri; **reproducerbar åtdragning och verifierad fastspänning**; verktyg som inte faller; tillräcklig frigång i Z; att bytesstation kan nås utan kollision.
- Mät verktygslängd på den fasta knappen efter varje byte.
- Ett experiment under 1 500 kr är möjligt med återbrukade delar; **pålitlig obemannad ATC är inte demonstrerad** och får inte antas utifrån fungerande motor.

## 8. Vända en stor skiva

Automatisk vändning av en hel 2,4 m plywoodskiva kräver betydligt mer mekanik än matning. Behåll som långsiktig idé. För dubbelsidig fräsning börja med **manuell vändning mot två registreringsstift/hål**, efterföljande maskinmätning och kontrollerad ny Z0.

## 9. Prioriterad falsifiering – inga nya inköp först

1. **Tapo-test:** RTSP-video/-ljud, bild på verklig skiva och skruvar, olika standoffs/vinklar, med känd linjal/markörer. Prova OpenCV på CPU. Kontrollera hur bra bildpositionerna blir vid olika materialhöjder.
2. **Vakuumtest:** tät liten zon, tryckfall och kraft mot sidostopp samt säkerhet vid plötsligt vakuumbortfall. Om det fungerar kan skruvdetektering prioriteras ner.
3. **BLTouch-test:** identifiera verkligt kort, mät elektrisk nivå/stift, printa attrapp, svep hela Z och alla kritiska positioner med KATSU avstängd. Mät kantdetektion jämfört med referens.
4. **Kamerabeslut:** välj först efter ett faktiskt kravfel i Tapo-testet. USB/UVC via befintlig kabelkedja bör jämföras med Pi Camera Module 3 standard + Pi Zero och ESP32-S3 OV5640. Ingen extra inferensmaskin behövs; garderobsserverns Coral används endast om ML krävs.
5. **Genie-frammatning:** löst prov med tomt bord och mekanisk styrning, mät registreringsfel efter minst tio matningscykler, innan fräsning.
6. **ATC-station:** konstruera mekanik oberoende av kamera/vakuum, provbyt utan aktiv fräs och verifiera spännkraft. Bygg inte autonom drift utan säkerhetsbevis.
7. **Dubbel sida:** manuell vändning med stift som baslinje.

### Öppna frågor / mätningar som krävs

- Verklig standoff och synfält som går att uppnå på Core utan intrång i dammsko/servoprob och kabelkedja.
- Vem håller kameran stilla när maskinen homar? Hur kalibreras kamera→fräsaxel och Z-förändringar?
- Vilken upplösning på *arbetsytan* behövs för pålitlig detektion och registrering? Testa antal pixlar över minsta relevanta detalj.
- Vilken BLTouch-variant får vi egentligen? Hur beter den sig i damm och spån?
- Genie-modell, löpmekanism, kraft och ändlägen.
- Vakuumpump/dammsugare, verkligt undertryck och temperatur vid flödesbegränsning.
- Automatisk bytesstation: spindellåsning, verktygslåsning och vad som ska hända vid ström-/signalfel.

## Källor

- CNC-repots [pågående kamera-/probplan](https://github.com/kingkongola/cnc/blob/main/docs/kamera-prob-och-skanning.md)
- LowRiders [servo-probstudier](../machine/delar/nollpunkt/)
- [Raspberry Pi officiella kameraspecifikationer](https://www.raspberrypi.com/documentation/accessories/camera.html)
- [Electrokit: Pi Camera Module 3](https://www.electrokit.com/raspberry-pi-kameramodul-3-12mp-75)
- [Electrokit: Pi Zero 2 W](https://www.electrokit.com/raspberry-pi-zero-2-w)
- [V1E: modulärt vakuumbord](https://forum.v1e.com/t/3d-printed-modular-vacuum-workholding-table-for-lr4-or-anything-for-that-matter/50261)
