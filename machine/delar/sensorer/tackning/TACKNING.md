# Täckning: vad är kontrollerat?

Genererad av `tackning.py` ur `komponenter.yaml` och `system.yaml`. Ändra i YAML-filerna, inte här.

Varje ruta har den sämsta status som står i den. **Har kontroll** = A, S, F eller X: rutan har en definierad kontroll eller är inte relevant. F betyder ett **planerat** fysiskt prov; om det är utfört ägs av CHECKLIST.md. Nominella antaganden (N) och SAKNAS räknas inte.

| Matris | Storlek | A (automatisk kontroll) | S (simulerad/beräknad) | F (fysiskt prov) | N (nominellt antagande) | X (ej relevant) | SAKNAS (inte kontrollerat) | Har kontroll |
|---|---|---|---|---|---|---|---|---|
| Komponenter | 30 × 11 | 43 | 44 | 41 | 80 | 86 | 36 | 65 % |
| Systemet | 23 × 8 | 14 | 73 | 29 | 13 | 31 | 24 | 80 % |

## Inte kontrollerat (60 rutor)

| Matris | Rad | Kolumn | Vad saknas |
|---|---|---|---|
| Komponenter | Torn | Last och vibration | styvhet och egenfrekvens för torn och ADXL-platta ej beräknade; knackprov saknas i checklistan |
| Komponenter | Torn | Värme | temperatur i slutet rum med Pi och två LM2596 ej beräknad eller mätt |
| Komponenter | Torn | Damm och spån | öppningar (SD-springa, kabelutgång, panelslitsar) ej bedömda mot spån |
| Komponenter | Sidopanel | Insättning, fri väg | panelens väg in med fingrar, mikrofonram och ledningar ej simulerad |
| Komponenter | Sidopanel | Last och vibration | fingrarnas klämkraft och glapp mot Pi och LM2596 ej beräknade |
| Komponenter | Arm | Elektrisk koppling och kabelväg | CR Touch-kabelns böj vid navet under 150 graders rörelse ej simulerad |
| Komponenter | Arm | Last och vibration | stoppkrafter 105-230 N mot printade stopp ej beräknade i PETG |
| Komponenter | LED-fäste | Elektrisk koppling och kabelväg | lödning och kabelväg på understruten ej projekterad |
| Komponenter | Pi Zero 2 WH | Värme | strypning (throttling) i slutet rum ej bedömd; F 1.5 mäter |
| Komponenter | microSD | Last och vibration | kan vibrera ur; ej bedömt |
| Komponenter | Camera Module 3 | Damm och spån | linsen sticker ut 2,6 mm; inget skydd eller rengöringsrutin |
| Komponenter | ADXL345 | Last och vibration | plattans resonans ej känd; påverkar mätningen |
| Komponenter | LM2596 A | Värme | förlusteffekt i slutet rum ej beräknad |
| Komponenter | LM2596 B | Värme | servoströmmens förlust ej beräknad |
| Komponenter | Servo SPMS664 | Insättning, fri väg | servokroppens väg genom ramen ej simulerad (bara skruvarna) |
| Komponenter | Servo SPMS664 | Last och vibration | beteende och ström mot hårt stopp ej mätt; F 1.2 utan pulser |
| Komponenter | CR Touch | Damm och spån | stiftet i spån och damm ej bedömt |
| Komponenter | Magnet | Last och vibration | hållkraft under vibration ej beräknad; F 4.9 |
| Komponenter | Kopplingskort | Print/tillverkning | hålkortets layout ej ritad |
| Komponenter | Tornkabel 12 ledare | Frigång i drift | böj och längd genom hela X-rörelsen ej simulerad; F 5.3 |
| Komponenter | Y-kabel 8 ledare | Frigång i drift | genom Y-kedjan ej kontrollerat |
| Komponenter | Stopplåda | Mått verifierade | kapsling och layout ej valda eller ritade |
| Komponenter | Stopplåda | Print/tillverkning | kapsling inte vald |
| Komponenter | Stopplåda | Insättning, fri väg | delarnas plats i lådan inte ritad |
| Komponenter | Stopplåda | Fastsättning, åtkomst och grepp | hur lådan sitter på bordet ej bestämt |
| Komponenter | Stopplåda | Service och byte | 230 V-delen ska kunna öppnas säkert |
| Komponenter | Pumpkort | Print/tillverkning | hålkortslayout ej ritad |
| Komponenter | Pumpkort | Insättning, fri väg | plats i lådan inte ritad |
| Komponenter | Pumpkort | Fastsättning, åtkomst och grepp | hur kortet sitter i lådan inte bestämt |
| Komponenter | Kontaktor, nödstopp, startknapp | Insättning, fri väg | lådlayout |
| Komponenter | Kontaktor, nödstopp, startknapp | Fastsättning, åtkomst och grepp | lådlayout |
| Komponenter | HDR-60-24 nr 2 | Insättning, fri väg | lådlayout |
| Komponenter | COB-list | Elektrisk koppling och kabelväg | lödning och kabelväg |
| Komponenter | M5 tornet till maskinen | Mått verifierade | längd beror på befintlig skruv; mät |
| Komponenter | M5 tornet till maskinen | Last och vibration | klämkraft mot PETG-distansen och krypning ej bedömd |
| Komponenter | Självgängande M3 och M2.5 i PETG | Fastsättning, åtkomst och grepp | grepp och åtdragning i PETG ej provat; hornprovet är PLA |
| Systemet | Tornets infästning på maskinen | Simulering eller beräkning | klämkraft, krypning i PETG och tornets vibration ej beräknade |
| Systemet | Tornets infästning på maskinen | Vad händer när det går fel | lossnar skruven syns det inte; ingen kontroll under drift |
| Systemet | Armens rörelse och ändlägen | Simulering eller beräkning | stoppkrafter och magnetens hållkraft |
| Systemet | Armspärren | Simulering eller beräkning | märkets plats ej vald (L6) |
| Systemet | Vibrationsmätning | Simulering eller beräkning | plattans resonans |
| Systemet | Matning, övervakning | Simulering eller beräkning | spänningsfall i 0,25 mm²-ledarna vid 1,3 A ej räknat för hela vägen |
| Systemet | Matning, övervakning | Vad händer när det går fel | ingen säkring vald på 24 V ut från lådan |
| Systemet | Matning, maskin och servo | Simulering eller beräkning | servons strömtopp mot LM2596 B och kabeln ej beräknad |
| Systemet | Jord och störningar | Prov på maskinen | inget prov för störningar på probsignalen med KATSU igång |
| Systemet | Jord och störningar | Vad händer när det går fel | falsk probkontakt under G38 ger fel nollpunkt |
| Systemet | FluidNC-konfiguration | Prov på maskinen | estop_pin på gpio.39 saknas i förslaget |
| Systemet | Programvara på datorn | Vad händer när det går fel | datorn som begär stopp vid sensorlarm är inte byggd |
| Systemet | Kabelföring genom rörelsen | Konstruktion finns | tornkabelns väg längs X ej ritad |
| Systemet | Kabelföring genom rörelsen | Simulering eller beräkning | böjradie och längd per kabel genom rörelsen inte räknade |
| Systemet | Värme i tornet | Krav formulerat | ingen temperaturgräns satt |
| Systemet | Värme i tornet | Simulering eller beräkning | förlusteffekt och temperaturhöjning inte räknade |
| Systemet | Värme i tornet | Prov på maskinen | långkörning med temperaturloggning saknas i checklistan |
| Systemet | Värme i tornet | Ägande fil | ingen fil äger värmekraven |
| Systemet | Damm och spån | Krav formulerat | inget krav formulerat |
| Systemet | Damm och spån | Prov på maskinen | inget prov av damm på lins, mikrofon och CR Touch under fräsning |
| Systemet | Damm och spån | Ägande fil | ingen fil äger dammkraven |
| Systemet | 230 V-säkerhet | Konstruktion finns | stopplådans layout, beröringsskydd och dragavlastning ej ritade |
| Systemet | 230 V-säkerhet | Vad händer när det går fel | felfall i 230 V-delen (kortslutning, jordfel, säkring) inte genomgångna |
| Systemet | Dokumentens samstämmighet | Automatisk kontroll | ingen automatisk kontroll av att BOM stämmer med CAD; skruvraderna rättades för hand 2026-11-11 efter att matrisen hittade fel |

## Komponenter

| | Mått verifierade | Print/tillverkning | Insättning, fri väg | Fastsättning, åtkomst och grepp | Elektrisk koppling och kabelväg | Frigång i drift | Last och vibration | Värme | Damm och spån | Service och byte | Funktionsprov |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Torn | A | F | X | F | X | A | **SAKNAS** | **SAKNAS** | **SAKNAS** | S | F |
| Sidopanel | A | S | **SAKNAS** | A | S | X | **SAKNAS** | N | N | S | F |
| Arm | A | S | A | F | **SAKNAS** | A | **SAKNAS** | X | N | S | F |
| Skyddshylsa | A | S | A | F | X | A | N | X | N | S | F |
| Hornbygel | A | S | A | F | X | A | F | X | X | S | F |
| Distansbricka | A | S | A | A | X | X | N | X | X | X | X |
| LED-fäste | A | S | N | N | **SAKNAS** | N | X | F | N | N | F |
| Pi Zero 2 WH | N | X | A | A | A | X | N | **SAKNAS** | N | A | F |
| microSD | S | X | A | N | X | X | **SAKNAS** | X | N | A | F |
| Camera Module 3 | A | X | S | A | S | X | N | N | **SAKNAS** | S | F |
| CSI-kabel | N | X | S | N | S | X | N | X | X | S | F |
| ADXL345 | N | X | A | A | A | X | **SAKNAS** | X | X | S | F |
| INMP441 | N | X | A | N | A | X | N | X | S | S | F |
| LM2596 A | N | X | A | N | S | X | N | **SAKNAS** | X | S | F |
| LM2596 B | N | X | A | N | S | X | N | **SAKNAS** | X | S | F |
| Servo SPMS664 | N | X | **SAKNAS** | A | S | F | **SAKNAS** | N | N | S | F |
| Servohorn | F | X | A | F | X | A | F | X | X | S | F |
| CR Touch | N | X | A | A | N | A | N | X | **SAKNAS** | S | F |
| Magnet | N | X | A | N | X | X | **SAKNAS** | N | N | N | F |
| Kopplingskort | N | **SAKNAS** | A | N | S | X | N | N | X | S | F |
| Tornkabel 12 ledare | N | X | S | S | S | **SAKNAS** | N | X | N | N | F |
| Y-kabel 8 ledare | N | X | N | N | S | **SAKNAS** | N | X | N | N | F |
| Stopplåda | **SAKNAS** | **SAKNAS** | **SAKNAS** | **SAKNAS** | S | X | X | N | N | **SAKNAS** | F |
| Pumpkort | S | **SAKNAS** | **SAKNAS** | **SAKNAS** | S | X | X | N | X | N | F |
| Kontaktor, nödstopp, startknapp | N | X | **SAKNAS** | **SAKNAS** | S | X | X | N | N | N | F |
| HDR-60-24 nr 2 | N | X | **SAKNAS** | N | S | X | X | N | N | N | F |
| COB-list | N | X | N | N | **SAKNAS** | X | X | F | N | N | F |
| Jackpot-anslutningar | N | X | X | N | S | X | X | X | X | N | F |
| M5 tornet till maskinen | **SAKNAS** | X | A | S | X | X | **SAKNAS** | X | X | S | F |
| Självgängande M3 och M2.5 i PETG | A | N | A | **SAKNAS** | X | X | N | X | X | N | F |

## Systemet

| | Krav formulerat | Konstruktion finns | Automatisk kontroll | Simulering eller beräkning | Bänkprov | Prov på maskinen | Vad händer när det går fel | Ägande fil |
|---|---|---|---|---|---|---|---|---|
| Tornets infästning på maskinen | S | S | A | **SAKNAS** | X | F | **SAKNAS** | S |
| Armens rörelse och ändlägen | S | S | A | **SAKNAS** | F | F | N | S |
| Probmätning till nollpunkt | S | S | A | N | F | F | S | S |
| Kamerabild och kalibrering | S | S | A | S | F | F | S | S |
| Belysning | S | S | A | N | F | F | N | S |
| Armspärren | S | S | A | **SAKNAS** | X | F | S | S |
| Vibrationsmätning | S | S | A | **SAKNAS** | F | F | S | S |
| Ljudmätning | S | S | A | N | F | F | S | S |
| Matning, övervakning | S | S | X | **SAKNAS** | F | F | **SAKNAS** | S |
| Matning, maskin och servo | S | S | X | **SAKNAS** | F | F | N | S |
| Jord och störningar | S | S | X | X | X | **SAKNAS** | **SAKNAS** | S |
| Stoppkedjan | S | S | A | S | F | F | S | S |
| Start efter stopp | S | S | A | X | F | F | S | S |
| FluidNC-konfiguration | S | S | A | X | X | **SAKNAS** | N | S |
| Programvara på Pi:n | S | S | A | X | F | F | S | S |
| Programvara på datorn | S | S | A | X | X | F | **SAKNAS** | S |
| Nätverk | S | S | X | X | F | N | S | S |
| Kabelföring genom rörelsen | S | **SAKNAS** | X | **SAKNAS** | X | F | N | S |
| Värme i tornet | **SAKNAS** | S | X | **SAKNAS** | F | **SAKNAS** | N | **SAKNAS** |
| Damm och spån | **SAKNAS** | S | X | X | X | **SAKNAS** | S | **SAKNAS** |
| Underhåll | N | S | A | X | X | N | X | S |
| 230 V-säkerhet | S | **SAKNAS** | X | X | X | F | **SAKNAS** | S |
| Dokumentens samstämmighet | S | X | **SAKNAS** | X | X | X | N | S |
