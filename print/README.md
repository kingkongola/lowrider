# Sensorenhetens första passningsprov

Jobbet [sensor-passning.json](sensor-passning.json) innehåller **en liten kameraficka ur senaste sidotornet**, inte hela tornet. Syftet är att kontrollera den mottagna Camera Module 3 Standard innan en stor utskrift. Fysisk provning är ännu inte rapporterad; aktuell status ägs av [CHECKLIST.md](../CHECKLIST.md).

## Underlag och beredning

- [passningsprov.py](../machine/delar/sensorer/passningsprov.py) skär ut kamerafickan direkt ur [sidotorn.py](../machine/delar/sensorer/sidotorn.py), vänder den med öppningen uppåt och placerar den på bädden. Inga nya passningsmått läggs till.
- [manifest.json](sensor-passning/manifest.json) knyter exporten till källorna med SHA-256, ett digitalt fingeravtryck av filinnehållet. Vid källändring ska provet exporteras och skivas om.
- PLA och standardprofil med 0,20 mm lager: billigt passningsprov utan krav på slutdelens värme- eller lasttålighet. Automatisk trädstöd används för utskurna kabelvägar och överhäng. Stöden bryts loss efter print.
- Bambu P1S, 0,4 mm munstycke, texturerad PEI-platta. Jobbet förutsätter PLA i skrivaren; laddat material är inte verifierat här.
- `bricka.stl` exporteras samtidigt men ingår inte i första plattan.

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

Detta prov godkänner inte M3-skruvarnas slutliga längd, kamerans fulla fasthållning, tornets maskininfästning, servohorn, BLTouch, belysning eller den övriga elektroniken.
