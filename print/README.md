# Sensorenhetens passningsprov

Jobbet [sensor-passning.json](sensor-passning.json) innehåller **en liten kameraficka ur senaste sidotornet**, inte hela tornet. Syftet är att kontrollera den mottagna Camera Module 3 Standard innan en stor utskrift. [CR Touch-provet](#cr-touch--armfot) har en separat platta. Fysisk provning är ännu inte rapporterad; aktuell status ägs av [CHECKLIST.md](../CHECKLIST.md).

## Underlag och beredning

- [passningsprov.py](../machine/delar/sensorer/passningsprov.py) skär ut kamerafickan direkt ur [sidotorn.py](../machine/delar/sensorer/sidotorn.py), vänder den med öppningen uppåt och placerar den på bädden. Inga nya passningsmått läggs till.
- [manifest.json](sensor-passning/manifest.json) knyter exporten till källorna med SHA-256, ett digitalt fingeravtryck av filinnehållet. Vid källändring exporteras provet om; om STL-innehållet ändrats ska det skivas om.
- PLA och standardprofil med 0,20 mm lager: billigt passningsprov utan krav på slutdelens värme- eller lasttålighet. Automatisk trädstöd används för utskurna kabelvägar och överhäng. Stöden bryts loss efter print.
- Bambu P1S, 0,4 mm munstycke, texturerad PEI-platta. Jobbet förutsätter PLA i skrivaren; laddat material är inte verifierat här.
- `bricka.stl` exporteras samtidigt men ingår inte i första plattan.
- Vid passningsberedning ska [användarens erfarenhet av för små printade hål](../CALIBRATION.md#2026-11-10--erfarenhetsvärde-för-printade-hål) beaktas. Detta första prov behåller tornets befintliga spelmått; dess geometri och skivning har inte ändrats av erfarenhetsnoteringen. Provpassningen avgör om ytterligare korrigering behövs.

```sh
uv run --offline --no-project --python 3.12 --with build123d==0.13.0 python machine/delar/sensorer/passningsprov.py --ut print/sensor-passning
uv run --project ~/dev/printa printa bild print/sensor-passning/kamera-passning.stl
uv run --project ~/dev/printa printa skiva print/sensor-passning.json
```

Öppna `sensor-passning.printa/sensor-passning.3mf` i Bambu Studio efter granskning av `forhandsvisning.png`. Utskrift startas av användaren.

## Vad vi provar

1. Ta bort stöden och lägg kamerakortet i fickan med linsen ut från fickan. Kortet ska gå i utan tvång, styrtapparna ska träffa hålen och kortet ska ligga stadigt på stödytorna.
2. Kontrollera att kamerans komponenter och flatkabelns kontakt går fria. Provet har avkapade kabelvägar; det godkänner inte hela flatkabelns dragning genom tornet.
3. Rapportera var det tar emot och mät eventuell avvikelse. Resultat förs i [CALIBRATION.md](../CALIBRATION.md), ändrade passningsmått i CAD-källan. Kapa inte kamerakortet och skala inte modellen i slicern.

Detta prov godkänner inte M3-skruvarnas slutliga längd, kamerans fulla fasthållning, tornets maskininfästning, servohorn, CR Touch, belysning eller den övriga elektroniken.

## Alla tre PLA-proven på en platta

[sensorprov-pla.json](sensorprov-pla.json) lägger hornprovet, CR Touch-provet (bara foten) och kameraprovet på samma platta: ca 37 min, 12,8 g PLA (omskivad 2026-11-11 utan hylsan). Styrkeprofilen gäller alla tre; den ger fler väggar och mer fyllning men samma mått. Automatiskt stöd byggs bara vid kamerafickan, enligt förhandsvisningen 2026-11-11; Provförfarandena nedan gäller som för de separata jobben.

## Servohorn — ficka och M3-bygel

[horn-passning.json](horn-passning.json) innehåller en liten hornficka och en separat kilbygel, en del med sned kontaktyta som pressar hornet mot fasta stöd. Geometrin kommer från [hornfaste.py](../machine/delar/sensorer/hornfaste.py); [manifestet](horn-passning/manifest.json) anger källor och exporter. Provkroppen har extra plan rygg för utskriften. Själva fickan, stöden, bygeln och skruvhålen motsvarar armens infästning.

PLA, 0,20 mm lager, styrkeprofil med fem väggar och 30 % inre fyllning: klämfunktionen behöver styvare provdelar än ett rent formprov. Fickan står med ryggen på bädden och bygeln med utsidan nedåt. Automatiska stöd används vid överhäng och tas bort före provning. Slutarmens material och utskrift bereds efter provet.

Slutplattan är kontrollerad och skivad utan fel eller varningar: cirka **13 minuter och 4,7 g PLA**. [Monteringsbild](horn-passning/delar.png) visar delarna isärdragna; det förenklade hornet är endast referens och skrivs inte ut.

```sh
uv run --offline --no-project --python 3.12 --with build123d==0.13.0 python machine/delar/sensorer/passningsprov.py --typ horn --ut print/horn-passning
uv run --project ~/dev/printa printa skiva print/horn-passning.json
```

Granska `horn-passning.printa/forhandsvisning.png` före utskrift och öppna därefter `horn-passning.3mf` i Bambu Studio. Utskrift startas av användaren.

**Provmontering med löst horn:**

1. Ta bort stöd och löst material. För in hornet från fickans öppna sida, något lyft från botten, och sänk det mot botten och sidostöden. Navet ska nå sitt bakre anslag utan tvång. Det större runda urtaget ska inte pressa navet runtom.
2. Lägg bygelns sneda nos mot hornets kant. Sätt i **två M3×10** av befintlig typ. Skruvarna går genom bygeln och formar gängor i fickans blinda Ø2,6-hål; de går inte genom originalhornet. Inga M2 eller nya muttrar ingår.
3. Dra växelvis och försiktigt för hand tills hornet hålls. Bygelns nos ska nå hornet innan bygeln bottnar; skruvarna ska klämma innan spetsarna når hålbottnen. Avbryt om plastgängan släpper, något spricker eller hornet bara sitter när bygeln böjs kraftigt.
4. Håll provkroppen och försök vicka hornet åt båda håll. Kontrollera även om det kan lyftas eller förskjutas längs fickan. Lossa och återmontera för att se att greppet går att upprepa. Rapportera glapp och var delarna tar emot i [mätloggen](../CALIBRATION.md).

[CAD-kontrollen](horn-passning/kontroll-cad.json) prövar 81 måttkombinationer och den monterade armens rörelse. Den bevisar inte friktion, plastgängornas hållfasthet eller verkligt glapp. Skala inte hela provet och borra inte originalhornet för denna metod.

## CR Touch — armfot

[crtouch-passning.json](crtouch-passning.json) innehåller **en liten armfot** ur aktuell CAD, gjord med [passningsprov.py](../machine/delar/sensorer/passningsprov.py). [Manifestet](crtouch-passning/manifest.json) knyter den till källor och CR Touch-referens. Provet är PLA, 0,20 mm lager, utan stöd, för Bambu P1S 0,4 mm och texturerad PEI-platta.

**Skyddshylsan utgick 2026-11-11** (användarens beslut efter CR Touch-prov 1, där den inte gick att montera). CR Touchen skruvas direkt i foten, som Creality avsett. Cirka 5 minuter och 1,6 g PLA (skivat 2026-11-11), utan stöd; ett litet överhäng på 6 mm² får brygga. Resultat i `crtouch-passning.printa/`; öppna `crtouch-passning.3mf` i Bambu Studio först efter bildgranskning.

```sh
uv run --offline --no-project --python 3.12 --with build123d==0.13.0 python machine/delar/sensorer/passningsprov.py --typ crtouch --ut print/crtouch-passning
uv run --project ~/dev/printa printa skiva print/crtouch-passning.json
```

**Provmontering, utan matning:**

1. Lägg provfoten över sensorn med den öppna kontaktsidan bort från armryggen. Kontakten och kabeln ska gå fria genom öppningen. Provet verifierar inte hela kabelns böjning när armen rör sig.
2. Montera med kitets två M3×6 från undersidan, genom sensorns öron in i provfotens plastgänghål. Skruva försiktigt för hand.
3. Kontrollera att örat ligger an mot foten, skruvarna går att nå och skruvskallarna går fria från sensorkroppen. Referensens egna skruvskallar har en liten modellöverlappning; verklig skalle/fläns måste därför bedömas här. Tvinga inte ihop delarna om det tar emot.
4. Rapportera passning och mått till [CALIBRATION.md](../CALIBRATION.md) innan slutdelar bereds. Modellen har redan inritat kroppsspel och håltillägg enligt [kitunderlaget](../research/2026-11-10-crtouch-anpassning.md); skala inte hela plattan.

[CAD-kontrollen](crtouch-passning/kontroll-cad.json) och [maskinreferensernas stickprov](crtouch-passning/kontroll-maskin.txt) redovisar digital kontroll och avgränsningar. Detta är ett **passningsprov**, inte godkänd elektrisk probing eller monterad servofunktion. Servohornets infästning, verkligt kablage, belysning och den slutliga tornutskriften återstår enligt checklistan.

## Kameralock

[kameralock-prov.json](kameralock-prov.json) är **kameralocket** ur aktuell CAD (`kameralock()` i [sidotorn.py](../machine/delar/sensorer/sidotorn.py)), samma STL som slutdelen men i PLA. Locket täcker kamerafickan underifrån så att bara objektivet syns (användarens önskan 2026-11-11). Det hålls av kamerans två M3 × 10: skallen trycker lockets öra mot kortkanten, precis där skallen klämde förut, och får 9 mm gänga.

Plattan ligger mot bädden. Öronen ligger 4,5 mm upp över skruvhålen och får **stöd bara under sig**, inne i hålen; plocka bort det med pincett. Ingen orientering klarar sig utan stöd: upp och ned hamnar hela plattan i luften. Öronen sitter diagonalt, så locket går bara in på ett sätt. Cirka 5 minuter och 1,2 g PLA (skivat 2026-11-11).

**Prov på kamerafickeprovet (det du redan har printat), utan matning:**

1. Lägg provbiten med fickan uppåt och kortet i fickan på tapparna, objektivet uppåt.
2. Lägg locket rakt på: öronen in i skruvhålen, objektivet genom mitthålet.
3. Två M3 × 10 genom lockets hål, insex 2,5. Dra tills kortet sitter still, inte hårdare.
4. Kontrollera: kortet glappar inte, locket ligger an mot undersidan utan glipa, objektivet går fritt i hålet och inget av lockets kant syns i bilden (om kameran går att koppla in).

## Lampdocka — kallt skruv- och styrprov

**Utgått enligt D022, printas inte.** Belysningen är COB-list under horisontell understrut.

[lampdock-passning.json](lampdock-passning.json) innehåller en liten del av tornväggen och lampmodulens fot, i PLA med 0,20 mm lager och utan stöd. Ingen lampa eller sockel ingår. [Manifest](lampdock-passning/manifest.json) och [CAD-kontroll](lampdock-passning/kontroll-cad.json) hör till aktuell källgeometri. Provbitens bakre hålrum är fyllt för stödfria lager; framsida, styrtapp och blindhålsdjup behålls. Huvudtornets elektronikrum har inte fyllts.

Plattan är printkontrollerad och skivad utan fel eller varningar: cirka **8 minuter, 2,6 g PLA**. Fysisk utskrift och passning är ännu inte rapporterade.

```sh
uv run --offline --no-project --python 3.12 --with build123d==0.13.0 python machine/delar/sensorer/passningsprov.py --typ lampdock --ut print/lampdock-passning
uv run --project ~/dev/printa printa skiva print/lampdock-passning.json
```

Visa `lampdock-passning.printa/forhandsvisning.png` och öppna sedan `lampdock-passning.3mf` i Bambu Studio. Prova så här utan matning:

1. Lägg foten mot dockans framsida. Tappen ska gå fritt i sitt hål. Upp och ned ska foten stoppas av tappen.
2. Prova två M3×6 för hand. De blinda pilothålen är små hål där skruven formar gängor i plasten. Foten ska ligga an innan skruvarna når hålbottnen; tvinga inte om den kärvar.
3. Lossa, ta bort och återmontera foten. Rapportera om hål/tapp behöver korrigeras i CAD. Modellens frigångshål har redan spel och håltillägg; skala inte hela delen.

Detta är ett kallt passningsprov. Lampbäraren och sockeladaptrarna blir inte värme- eller monteringsgodkända av att dockan passar.
