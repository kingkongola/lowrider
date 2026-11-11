# LowRider V4

**Aktuellt 2026-11-11.** Repot äger den fysiska maskinen och dess sensorenhet: konstruktion, delar, inköp, koppling, konfiguration och verifierade mått. Allt arbete fortsätter från [CHECKLIST.md](CHECKLIST.md).

## Nuläge

- **Grundmaskinen är byggd och har fräst.** Permanenta struts och dammsugning är monterade enligt byggloggen. Offerskivan är planfräst. Återstående kalibrering och kontroller står i checklistan; den gamla monteringsordningen är inte nästa arbete.
- **Sensorenhetens senaste konstruktionsspår är sidotornet** i [sidotorn.py](machine/delar/sensorer/sidotorn.py). Ett [litet kamerafickeprov](print/README.md) är printkontrollerat och skivat. Sidotornet är ännu inte rapporterat provprintat eller monterat. Tidigare modulbygge och dess gröna tester är historik, inte godkännande av sidotornet.
- **Electrokit-order är mottagen. CR Touch Auto Leveling Kit är tillgängligt.** Probfästets CAD och kopplingsplan är nu anpassade till CR Touch och en [separat provplatta](print/crtouch-passning.json) är framtagen. Fysisk passning och inkoppling återstår. Full leveransstatus ägs av [PROCUREMENT.md](PROCUREMENT.md).
- **Servots rörelseomfång är verifierat och räcker till konstruktionen.** Provresultatet ägs av [CALIBRATION.md](CALIBRATION.md#2026-11-10--fällservots-rörelseomfång-verifierat-på-bänk).
- **Horninfästningen är omgjord 2026-11-11:** hornet i formficka i armen och M3×10 genom armen som mittskruv; kilbygeln utgick. Provas med armen själv på servot ([sensorprov-2](print/README.md#armen-på-servot--sensorprov-2)).
- **Belysningen är BRIMETI 24 V COB-list enligt D022:** tre banor under horisontell understrut, provvinklar 0°/15°/35°, cirka 6,6 mm nedstick för fästet. G4-lamporna och sidotornets lampdocka/G4-bärare har utgått ur printplanen. [LED-underlaget](machine/delar/led/README.md), [el och stopp](machine/EL_BELYSNING_OCH_STOPP.md). Fysisk passning, värme och ljusbild är inte provade.
- **Pinnar för Jackpot3 är planerade men sensoranslutningen är inte driftsatt.** Aktuella beslut ägs av [DECISIONS.md](DECISIONS.md). Bänkprovet 2026-11-10 använde en fristående ESP32-S3. Repots avsedda maskinkonfiguration pekas ut av [machine/AKTIV](machine/AKTIV); den är inte liveavläst i denna dokumentgranskning.

## En källa per uppgift

| Fråga | Källa som äger svaret |
| --- | --- |
| Vad ska göras härnäst, och vad återstår att verifiera? | [CHECKLIST.md](CHECKLIST.md) |
| Vad har vi bestämt? | [DECISIONS.md](DECISIONS.md) |
| Vilka delar behövs eller finns? | [BOM.md](BOM.md) |
| Vad är beställt, mottaget eller väntar på leverans? | [PROCUREMENT.md](PROCUREMENT.md) |
| Vad har faktiskt debiterats? | [COSTS.md](COSTS.md) |
| Vilken sensorkonstruktion och vilka printdelar gäller? | [Sensorenhetens CAD-underlag](machine/delar/sensorer/README.md) |
| Hur är sensorernas planerade elkoppling uppdelad? | [Kopplingsunderlaget](machine/delar/sensorer/KOPPLING_CORE_V0.md) |
| Hur matas belysning, Pi och stopp? | [EL_BELYSNING_OCH_STOPP.md](machine/EL_BELYSNING_OCH_STOPP.md), beslut D022–D024 |
| Vad är uppmätt eller fysiskt provat? | [CALIBRATION.md](CALIBRATION.md) |
| Vilken maskinkonfiguration avses? | [machine/AKTIV](machine/AKTIV) → sparad konfigurationsfil |
| Vad hände tidigare? | [BUILD_LOG.md](BUILD_LOG.md) |
| Vad äger kamerans program och användarflöde? | [cnc:s sensorarkitektur](https://github.com/kingkongola/cnc/blob/main/docs/sensorarkitektur.md) och [kameraflöde](https://github.com/kingkongola/cnc/blob/main/docs/kamera-arbetsflode.md) |

Sammanfattningar hänvisar till ägarfilen. Levererad, ritad, digitalt kontrollerad, provprintad, monterad och fysiskt verifierad är skilda tillstånd. Okända uppgifter markeras som okända; en stängd osäkerhet öppnas bara om nya observationer motsäger resultatet.

## Referens och historik

[Monteringsguiden](docs/MONTERING_SV.md), [arbetskorten](WORK_ORDERS.md) och [webbguiden](https://kingkongola.github.io/lowrider/) beskriver byggmetoden. Gamla, obockade byggkort betyder inte att hela maskinen återstår att bygga. Webbens lokala kryssrutor är inte projektstatus.

Bord och kabelvägar ägs av [TABLE.md](TABLE.md) respektive [CABLE_ROUTING.md](CABLE_ROUTING.md). Kontrollkrav finns i [AUDIT.md](AUDIT.md), daterad inköpsevidens i [SOURCING.md](SOURCING.md) och äldre utredningar i [research/](research/README.md).

Tidigare statuslistor och sensorförslag är samlade i [arkivet](docs/arkiv/2026-11-09-status-och-sensorunderlag.md). De används som historik, inte som aktuell bygg- eller printorder. [Automationsidéerna](docs/AUTOMATISERING_OCH_KAMERA_2026-11-06.md) är också idéunderlag.
