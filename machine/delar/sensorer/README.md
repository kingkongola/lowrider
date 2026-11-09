# Core-sensorer v0 – CAD att provprinta före leverans

**Gällande status 2026-11-09:** parametrisk testpassnings-CAD, **inte godkänd mekanisk montering eller säker CNC-probning**. Vi använder [OpenSCAD-filen](core_sensorer_v0.scad) för fem små, oberoende modeller. Den befintliga servoarmens tidigare [build123d-modell C](../nollpunkt/fallarm_c.py) förblir mekaniskt referensunderlag för axel och fästen; ingen C-montageplatta byts eller slås samman automatiskt.

## De fem delarna

| Del | CAD-utdata | Funktion | Printstatus |
|---|---|---|---|
| `pi_bas` | `pi_bas.stl` | 80 × 46 × 22 mm öppen kapslingsbas för Pi Zero 2 WH, 58 × 23 mm M2.5-hål, passiv ventilation | **Provpassningsprint möjlig** |
| `pi_lock` | `pi_lock.stl` | Avtagbart lock med pilotskruvar; 40-pin header får inte pressas | **Provpassningsprint möjlig** |
| `kamera` | `kamera.stl` | Justerbar kamera-platta för Camera Module 3 Standard med fritt objektiv | **Provpassningsprint möjlig** |
| `bltouch_mattjigg` | `bltouch_mattjigg.stl` | Liten 18-mm-håljigg, kontroll av M3/pinens riktning på faktisk probe | **Provprint gärna först** |
| `bltouch_arm` | `bltouch_arm.stl` | Preliminär direktdriven servoarm som ersätter gamla Ø33-klämman med **lodrät BLTouch** i mätläge | **Inte säker för montering eller CNC-rörelse** |

STL exporteras från **en enda parametrisk .scad-källa**, utan att ändra projektets Python-/G-kod beroenden:

```sh
cd machine/delar/sensorer
for p in pi_bas pi_lock kamera bltouch_mattjigg bltouch_arm; do
  openscad -o "${p}.stl" -D "part=\"${p}\"" core_sensorer_v0.scad
done
```

**Modellunderlag:** Pi Zero 2 W PCB 65 × 30 mm, hålbild 58 × 23 mm enligt [Raspberry Pi](https://www.raspberrypi.com/documentation/computers/zero.html). Camera Module 3 Standard PCB ~25 × 24 × 11,5 mm enligt [Raspberry Pi](https://www.raspberrypi.com/documentation/accessories/camera.html); kamerans **slitsar i denna första modell är justerpassning, inte uppmätt originalhålbild**. BLTouch-hålavstånd och `flange_tip_mm=36.3` är preliminära mått från ritningsuppgifter, **måste bekräftas mot levererat exemplar**. Den nya armens servoaxel utgår från `fallarm_c.py` `PX=45, PZ=43.6`, men ingen fysisk krockkontroll mot kåpa, Core, dammsko, fräs eller lägen är gjord.

**Direkt praktisk utskriftsordning:** börja med `bltouch_mattjigg`, `kamera`, `pi_bas` och `pi_lock`. Kontrollera visuellt alla portar, CSI-böj, mikroSD, GPIO-header och skruvlängder. **Printa och montera inte `bltouch_arm` som fungerande prob före dimensions- och kollisionsgranskning**. Den finns för att utvärdera verklig geometri, inte för att ta G38-kommandon. Samtliga provdelar är utformade för vanliga FDM-utskrifter, men supports, passning och material måste bedömas i Bambu Studio. Inga nya fysiska delar är rapporterade printade eller provade.

## Fläktar – utelämnas tills mätning visar behov

Pi Zero 2 WH ska i första hand **bara ta kamera-stillbilder**; tung OpenCV/mosaik körs på den befintliga värddatorn. Därmed är aktiv kylning inte designkrav. Pi-kapslingen har passiva öppningar. Fläktar ökar dammintag, vibrationer, vikt, kabeldragning och underhåll. Raspberry Pi:s [kylvägledning](https://pip.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-003608-WP/Cooling-a-Raspberry-Pi-device.pdf) rekommenderar att man först bedömer faktisk temperatur/belastning. Kör `vcgencmd measure_temp` och notera termisk throttling vid verkligt arbetsmönster. Den nuvarande kapslingen är inte spåntät; förbättra skyddet efter verklig damm- och temperaturmätning, inte genom att addera fläkt reflexmässigt. Ingen tidigare nämnd exakt fläktmodell finns verifierad; inga fläktmått antas.

## El och gränser

Se [granskningsbart kopplingsunderlag](KOPPLING_CORE_V0.md): separata signaler för servo, BLTouch-stift, prob-trigger och de två ändlägesbrytarna. Den beställda 200-mm-CSI-kabeln kräver Pi nära kameran på rörliga Core. Ingen av de elektriska portarna eller kablarna är godkända för inkoppling. Touchplattan som tidigare diskuterades köptes inte; fast verktygsknapp är separat.

**Viktigt:** BLTouch måste vara lodrätt i mätläge enligt [ANTCLABS](https://www.antclabs.com/bltouch-v3). De tidigare ritningarna för 2,5D-skanning är **parkerade** och får inte låsa denna arm. Inget i CAD:n utgör verklig frigångs- eller säkerhetsverifiering.
