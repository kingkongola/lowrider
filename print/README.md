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

[sensorprov-pla.json](sensorprov-pla.json) (historik, ersatt av sensorprov-2) lägger hornfickan, CR Touch-foten och kameraprovet på samma platta: ca 37 min, 12,8 g PLA (omskivad 2026-11-11 utan hylsan). Styrkeprofilen gäller alla tre; den ger fler väggar och mer fyllning men samma mått. Automatiskt stöd byggs bara vid kamerafickan, enligt förhandsvisningen 2026-11-11; Provförfarandena nedan gäller som för de separata jobben.

## Armen på servot — sensorprov-2

[sensorprov-2.json](sensorprov-2.json): **armen**, kameralocket och de två stoppdelarna i PETG, styrkeprofil, cirka **1,0 h och 10 g** (skivat 2026-11-11, stöd 3 % av banan). Armen är en riktig slutdel och provas direkt på servot, utan tornet. Den ersätter hornprovet och CR Touch-fotprovet. Lilla nedre stoppet har liten bäddkontakt (31 mm²); printa får en brätte runt det.

**Prov, utan matning:**

1. **Gängan först:** skruva en M3×10 för hand i servots mässingsaxel, utan horn. Går den lätt flera varv: fortsätt. Tar den emot: sluta, axeln är 4-40.
2. Kontrollera att hornet är plant. Tryck in det **rakt i armens ficka** från servosidan; navet åt servot. De sju krossribborna ska ta emot de sista 2 mm: tryck med tummen eller kläm försiktigt i ett skruvstycke med mjuka käftar. Hornet ska sitta utan glapp i sidled och inte falla ur av egen vikt.
3. Sätt paketet arm + horn på axeln. M3×10 genom navbossen, insex 2,5. Dra tills det sitter, inte hårdare.
4. Vicka armen åt båda håll med servot stilla: inget glapp mellan arm och horn. Skruva CR Touchen i foten med kitets M3×6.
5. Rapportera i [mätloggen](../CALIBRATION.md).

Kontrollen [kontroll_horn.py](../machine/delar/sensorer/kontroll_horn.py) prövar fickan, skruvstapeln, insättningen och svepet. Den bevisar inte hållfasthet eller verkligt glapp.

Det gamla hornprovet (`horn-passning`, kilbygel) har utgått. `horn-passning.json` innehåller nu bara navets formficka som liten reservprovbit.

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
