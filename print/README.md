# Sensorenhetens passningsprov

Jobbet [sensor-passning.json](sensor-passning.json) innehåller **en liten kameraficka ur senaste sidotornet**, inte hela tornet. Syftet är att kontrollera den mottagna Camera Module 3 Standard innan en stor utskrift. [CR Touch-provet](#cr-touch--armfot-och-skyddshylsa) har en separat platta. Fysisk provning är ännu inte rapporterad; aktuell status ägs av [CHECKLIST.md](../CHECKLIST.md).

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

## CR Touch — armfot och skyddshylsa

[crtouch-passning.json](crtouch-passning.json) innehåller **en liten armfot och den nya skyddshylsan**. Båda tas direkt ur aktuell CAD med [passningsprov.py](../machine/delar/sensorer/passningsprov.py). [Manifestet](crtouch-passning/manifest.json) knyter dem till källor och CR Touch-referens. Provet är PLA, 0,20 mm lager, utan stöd, för Bambu P1S 0,4 mm och texturerad PEI-platta.

Hylsans flänsyta ligger mot bädden. Den avsmalnande formen undviker en dold stödhylla. Printkontrollen ger en varning för 13 mm² små överhäng vid skruvunderläggen: här får plasten brygga en kort sträcka mellan kanterna. Inga kontrollfel finns. Resultat och förhandsvisning ligger i `crtouch-passning.printa/`; öppna `crtouch-passning.3mf` i Bambu Studio först efter bildgranskning.

```sh
uv run --offline --no-project --python 3.12 --with build123d==0.13.0 python machine/delar/sensorer/passningsprov.py --typ crtouch --ut print/crtouch-passning
uv run --project ~/dev/printa printa skiva print/crtouch-passning.json
```

**Provmontering, utan matning:**

1. För in sensorkroppen från hylsans breda ände tills underläggen möter flänsens undersida. Den smala änden kan inte svälja flänsen; formen visar monteringsriktningen.
2. Lägg provfoten över sensorn med den öppna kontaktsidan bort från armryggen. Kontakten och kabeln ska gå fria genom öppningen. Provet verifierar inte hela kabelns böjning när armen rör sig.
3. Montera med kitets två M3×8 från undersidan, genom hylsa och sensorfläns in i provfotens plastgänghål. Skruva försiktigt för hand. Utan hylsa är den nominella avsikten M3×6.
4. Kontrollera att delarna ligger an, skruvarna går att nå, skruvskallarna går fria från sensorkroppen och hylsans öppna ände går fri från stiftet. Referensens egna skruvskallar har en liten modellöverlappning; verklig skalle/fläns måste därför bedömas här. Tvinga inte ihop delarna om det tar emot.
5. Rapportera passning och mått till [CALIBRATION.md](../CALIBRATION.md) innan slutdelar bereds. Modellen har redan inritat kroppsspel och håltillägg enligt [kitunderlaget](../research/2026-11-10-crtouch-anpassning.md); skala inte hela plattan.

[CAD-kontrollen](crtouch-passning/kontroll-cad.json) och [maskinreferensernas stickprov](crtouch-passning/kontroll-maskin.txt) redovisar digital kontroll och avgränsningar. Detta är ett **passningsprov**, inte godkänd elektrisk probing eller monterad servofunktion. Servohornets infästning, verkligt kablage, belysning och den slutliga tornutskriften återstår enligt checklistan.

## Lampdocka — kallt skruv- och styrprov

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
