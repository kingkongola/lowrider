# Sensorenhet — planerad elkoppling

**Uppdaterad 2026-11-10.** Detta är kopplingsunderlaget för sidotornet. Beslutade pinnar ägs av [D021](../../../DECISIONS.md#d021--pinnar-på-jackpot3-för-sensorenhetens-arm-och-bltouch). Den planerade sensoranslutningen är inte rapporterad inkopplad eller driftsatt på Jackpot3. Repots avsedda konfiguration bestäms av [machine/AKTIV](../../AKTIV), inte av tabellen nedan.

## Signalvägar

| Funktion | Vald anslutning enligt D021 | Kontroll före inkoppling |
| --- | --- | --- |
| Fällservots styrsignal | Jackpot `gpio.27`, utgång i 5 V-läge | Fysisk kontakt, signalnivå, 50 Hz, uppstart och monterade lägespulser |
| BLTouch-stiftets styrsignal | Jackpot `gpio.26`, utgång i 5 V-läge | Faktisk probrevision, pulskommandon och beteende vid uppstartspuls |
| BLTouch-kontakt | Jackpot `gpio.36` | Utsignalsnivå, polaritet och status vid kontakt/larm |
| Fast verktygslängdsknapp | Planerad `toolsetter_pin` på `gpio.39` | Knappens faktiska montage/anslutning är ännu inte verifierad |
| Kamera | Camera Module 3 → CSI-kabel → Pi Zero 2 WH | Kontaktriktning, låsning, verkliga böjar och räckvidd |
| Kamera till värddator | Pi → bild och metadata via nätverk | Kameratjänst, låst fokus och bildprov |
| ADXL345 | Lokalt till Pi; SPI är den planerade vägen för vibrationer | Levererat kort, matning, hålbild och signalanslutningar |
| INMP441 | Separat ljudinhämtning utreds vid praktiskt prov | Ingen färdig sidotornsplacering eller verifierad leveransstatus |

Armbrytare och deras GPIO ingår inte enligt D020. Bordets och maskinens befintliga ändlägen påverkas inte.

## Matning och kabel

- Befintlig 24 V-försörjning → **LM2596 A inställd på 5,1 V** till Pi och BLTouch.
- Samma 24 V-försörjning → **LM2596 B inställd på 6,0 V** till servot. Separat regulator ska hindra servots strömtoppar från att dra ned Pi-matningen.
- Regulatorerna finns enligt BOM; båda utgångarna ställs och mäts innan elektroniken ansluts. Dimensionering av ström, säkring, ledningar och prov med faktisk last återstår.
- Gemensam signaljord krävs mellan Jackpot och servomatning. Lägg servots returström så att den inte skapar störningar i prob- eller Pi-jord. Planerad kondensator nära servokontakten är 470–1000 µF; faktisk installation och val är inte verifierade.
- Jackpot-utgångarnas spänningsbygel ska stå på **5 V**. De utgångarna är styrsignaler; servot matas från sin egen regulator. Ingen 24 V får nå Pi, kamera eller servots signal.
- Den planerade kabelstammen från tornet innehåller 24 V, GND, servosignal, BLTouch-styrning och BLTouch-kontakt. Verkliga kaplängder mäts med hela rörelsen och loggas i [CABLE_ROUTING.md](../../../CABLE_ROUTING.md).

## Belysning — förberedelse för senare montage

LED-produkt och matningsspänning är ännu inte valda. Förslaget är tvåledar-LED med egen matningsgren och åtkomlig, polaritetsmärkt anslutning bakom sidopanelen. Fördra vid behov ett ledningspar från vardera LED-läget till kopplingspunkten; ledararea och kontakt väljs efter lampornas ström och verkliga kabelutrymme. Lämna förberedda ändar frånkopplade, separat isolerade och dragavlastade tills anslutningen är fastställd.

Den planerade kabelstammen innehåller redan 24 V till tornet; lokal belysning behöver därför inte automatiskt en extra matningskabel längs maskinen. Delning med Pi/BLTouch-regulatorn är möjlig först när LED:s tillåtna spänning och regulatorns lastmarginal är verifierade. Koppla inte lampor direkt till Pi:s signalpinnar eller till servots 6 V-gren. Ingen extra styrelektronik behövs för första prov med kontinuerligt ljus.

Eftermonteringens mekaniska krav finns i [kameraunderlaget](../../KAMERA_ANHALL.md#eftermontering--förslag-diskuterat-2026-11-10-ej-färdig-konstruktion). Förslaget är ännu inte en färdig inkopplingsorder.

## Skillnad mellan bänkprov och maskininstallation

Dagens prov körde servot på **en fristående ESP32-S3, GPIO 18**, med separat servomatning och gemensam jord. Resultatet och provprogrammet finns i [CALIBRATION.md](../../../CALIBRATION.md#2026-11-10--fällservots-rörelseomfång-verifierat-på-bänk). Detta ändrar inte D021:s val av Jackpot-pinne eller maskinens FluidNC-konfiguration.

Vid framtida konfigurationsförslag måste GPIO 27/26 flyttas från sina digitala utgångar till separata 50 Hz-utgångar; de får inte vara dubbelallokerade. Skapa då ett komplett förslag från senast avläst konfiguration och granska det innan uppladdning. Ett fristående YAML-utdrag här är inte en konfigurationsfil att ladda upp.

FluidNC:s två probe-ingångar behandlas av samma G38-kontaktlogik. Båda måste ha entydiga vilolägen; ett lyckat mätkommando bevisar inte vilken givare som triggade. Prova utan maskinrörelse enligt [inkopplingsförfarandet](../nollpunkt/INKOPPLING_OCH_PROV.md).

Kamerans startspärr är implementerad i `cnc`, men **aktiveras först efter inlärning**. Utan inlärning släpper dagens kod igenom för att grundmaskinen ska fungera utan sensorenhet. Efter inlärning ska utebliven eller oklar bild stoppa jobbstart. Inlärning och fysiska felprov måste ingå vid driftsättning; spärren är ingen säkerhetsfunktion och stoppar inte pågående rörelse. Se [beslut 0035](https://github.com/kingkongola/cnc/blob/main/docs/beslut/0035-armsparr-med-kamera.md).
