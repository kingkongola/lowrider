# Sensorenhet — planerad elkoppling

**Uppdaterad 2026-11-10.** Detta är kopplingsunderlaget för sidotornet. Beslutade pinnar ägs av [D021](../../../DECISIONS.md#d021--pinnar-på-jackpot3-för-sensorenhetens-arm-och-bltouch). Den planerade sensoranslutningen är inte rapporterad inkopplad eller driftsatt på Jackpot3. Repots avsedda konfiguration bestäms av [machine/AKTIV](../../AKTIV), inte av tabellen nedan.

**Anpassat för CR Touch Auto Leveling Kit.** Creality anger nominellt 5 V. Funktionskopplingen nedan behåller D021:s pinnval; den är ännu inte fysiskt inkopplad eller provad. Kit, källor och referensbegränsningar finns i [CR Touch-underlaget](../../../research/2026-11-10-crtouch-anpassning.md).

## Förtydligande 2026-11-10 – Pi:s oberoende matning

**Kravändring för kommande elkonstruktion:** Raspberry Pi/kamera ska kunna fortsätta logga efter att KATSU och Jackpot3 har frånkopplats. Därför är diagrammets äldre `P24 → V5 → PI` (Pi från samma brytna 24 V som Jackpot) **historiskt och inte längre giltigt som matningslösning**. Använd en separat, verifierad kraftdomän utanför maskinstoppets frånkopplade gren; 20 V-laptopladdare är kandidat, inte bestämd. Servo/prob ska inte kunna bakmata avstängd Jackpot. Matningsgrupperna är valda i D023 och stoppet i D024. Se [aktuell SSOT för el/LED/stopp](../../EL_BELYSNING_OCH_STOPP.md) och [cnc:s övervakningsplan](https://github.com/kingkongola/cnc/blob/main/docs/verktygsovervakning.md). **Inga aktiva pinnar eller kablar ändras här.**

## Brytare utgår 2026-11-09

## Signalvägar

| Funktion | Vald anslutning enligt D021 | Kontroll före inkoppling |
| --- | --- | --- |
| Fällservots styrsignal | Jackpot `gpio.27`, utgång i 5 V-läge | Fysisk kontakt, signalnivå, 50 Hz, uppstart och monterade lägespulser |
| CR Touch-stiftets styrsignal | Jackpot `gpio.26`, utgång i 5 V-läge | Faktisk kabelordning, pulskommandon och beteende vid uppstartspuls |
| CR Touch-kontakt | Jackpot `gpio.36` | Utsignalsnivå, polaritet och status vid kontakt/larm |
| Fast verktygslängdsknapp | Ingen pinne: `gpio.39` går till stoppet (D024). Modulporten eller struken, ej avgjort | Knappens faktiska montage/anslutning är ännu inte verifierad |
| Stopp (nödstopp + Pi i serie) | `gpio.39` som `control/estop_pin`, D024 | FluidNC-beteende, optokopplare och ledningsdragning ej provade |
| Kamera | Camera Module 3 → CSI-kabel → Pi Zero 2 WH | Kontaktriktning, låsning, verkliga böjar och räckvidd |
| Kamera till värddator | Pi → bild och metadata via nätverk | Kameratjänst, låst fokus och bildprov |
| ADXL345 | Lokalt till Pi; SPI är den planerade vägen för vibrationer | Levererat kort, matning, hålbild och signalanslutningar |
| INMP441 | Till Pi via I²S, 3,3 V (aldrig 5 V). Planerat: SCK → GPIO18 (stift 12), WS → GPIO19 (stift 35), SD → GPIO20 (stift 38), L/R → GND, VDD → 3,3 V (stift 1/17), GND. Krockar inte med ADXL:ens SPI (GPIO 8–11) | Placerad i sidopanelen 2026-11-11. Leverans, Pi-drivrutin och samtidig drift med kamera och ADXL ej provade |

Armbrytare och deras GPIO ingår inte enligt D020. Bordets och maskinens befintliga ändlägen påverkas inte.

## Originalkabelns fem funktioner

Behåll kitets kontakt vid sensorn. [TH3D:s sensor-side guide](https://tickets.th3dstudio.com/help-guides/article/crtouch-sensor-pinout-%E2%80%93-sensor-side) används för att identifiera funktionerna vid just sensorkontakten. Tabellen nedan är en **funktionskarta**, inte färgordning eller vänster–höger-numrering av användarens kabel.

| Funktion vid sensorn | Planerad anslutning |
| --- | --- |
| Matningsjord, GND | LM2596 A minus och gemensam signaljord |
| +5 V matning | LM2596 A plus, 5,1 V |
| SERVO, styrsignal in till proben | Jackpot GPIO 26:s signalutgång i 5 V-läge |
| ZStop GND, kontaktsignalens jord | Jackpot probe-portens G |
| ZStop, kontaktsignal ut från proben | Jackpot probe-portens S, GPIO 36 |

Identifiera och kontinuitetsmät varje ledare med matningen frånkopplad innan kortänden anpassas. Lita inte på en annan kabels färger eller på IN/OUT-etiketter på ett Creality-moderkort. Manualens Ender-firmware och instruktion att ta bort skrivarens Z-brytare gäller inte vår LowRider; dess homingbrytare behålls.

## Matning och kabel

- Befintlig 24 V-försörjning → **LM2596 A ställs till 5,1 V** för Pi och CR Touch (användarens val 2026-11-10). 5,1 V är Raspberrys egen nätdels spänning; marginalen tar kabelns spänningsfall när Pi:n drar mycket, och ligger inom CR Touchens nominella 5 V. Utgången mäts tomgång och med last. Ingen fysisk justering är gjord här. Justerskruven säkras med smältlim efter inställning; mät igen efter limning.
- Samma 24 V-försörjning → **LM2596 B inställd på 6,0 V** till servot. Separat regulator ska hindra servots strömtoppar från att dra ned Pi-matningen.
- Regulatorerna finns enligt BOM; båda utgångarna ställs och mäts innan elektroniken ansluts. Dimensionering av ström, säkring, ledningar och prov med faktisk last återstår.
- Gemensam signaljord krävs mellan Jackpot och servomatning. Lägg servots returström så att den inte skapar störningar i prob- eller Pi-jord. Planerad kondensator nära servokontakten är 470–1000 µF; faktisk installation och val är inte verifierade.
- Jackpot-utgångarnas spänningsbygel ska stå på **5 V**. De utgångarna är styrsignaler; servot matas från sin egen regulator. Ingen 24 V får nå Pi, kamera eller servots signal.
- Den planerade kabelstammen från tornet innehåller 24 V, GND, servosignal, CR Touch-styrning och CR Touch-kontakt. Lokalt har probkabeln även separat jordledare för kontaktsignalen enligt funktionskartan ovan. Verkliga kaplängder mäts med hela rörelsen och loggas i [CABLE_ROUTING.md](../../../CABLE_ROUTING.md).

## Belysning — förberedelse för senare montage

LED-produkt och matningsspänning är ännu inte valda. Förslaget är tvåledar-LED med egen matningsgren och åtkomlig, polaritetsmärkt anslutning bakom sidopanelen. Fördra vid behov ett ledningspar från vardera LED-läget till kopplingspunkten; ledararea och kontakt väljs efter lampornas ström och verkliga kabelutrymme. Lämna förberedda ändar frånkopplade, separat isolerade och dragavlastade tills anslutningen är fastställd.

Den planerade kabelstammen innehåller redan 24 V till tornet; lokal belysning behöver därför inte automatiskt en extra matningskabel längs maskinen. Delning med Pi/prob-regulatorn är möjlig först när LED:s tillåtna spänning och regulatorns lastmarginal är verifierade. Koppla inte lampor direkt till Pi:s signalpinnar eller till servots 6 V-gren. Ingen extra styrelektronik behövs för första prov med kontinuerligt ljus.

**Utgått enligt D022:** G4 används inte; COB-listens matning ägs av [EL_BELYSNING_OCH_STOPP.md](../../EL_BELYSNING_OCH_STOPP.md) och D023. Historik: de undersökta G4-lamporna är 12 V-produkter. De kräver separat lämplig matning, exempelvis en ytterligare regulator från 24 V; någon sådan placering och lastmarginal är ännu inte verifierad. Tornets två regulatorfickor är redan avsedda för Pi/CR Touch och servo.

Eftermonteringens mekaniska krav finns i [kameraunderlaget](../../KAMERA_ANHALL.md#eftermontering--demonterbar-lampmodul). Lampdockan finns nu i CAD, men matningen är ännu inte en färdig inkopplingsorder.

## Skillnad mellan bänkprov och maskininstallation

Dagens prov körde servot på **en fristående ESP32-S3, GPIO 18**, med separat servomatning och gemensam jord. Resultatet och provprogrammet finns i [CALIBRATION.md](../../../CALIBRATION.md#2026-11-10--fällservots-rörelseomfång-verifierat-på-bänk). Detta ändrar inte D021:s val av Jackpot-pinne eller maskinens FluidNC-konfiguration.

Vid framtida konfigurationsförslag måste GPIO 27/26 flyttas från sina digitala utgångar till separata 50 Hz-utgångar; de får inte vara dubbelallokerade. Skapa då ett komplett förslag från senast avläst konfiguration och granska det innan uppladdning. Ett fristående YAML-utdrag här är inte en konfigurationsfil att ladda upp.

FluidNC:s två probe-ingångar behandlas av samma G38-kontaktlogik. Båda måste ha entydiga vilolägen; ett lyckat mätkommando bevisar inte vilken givare som triggade. Prova utan maskinrörelse enligt [inkopplingsförfarandet](../nollpunkt/INKOPPLING_OCH_PROV.md).

Kamerans startspärr är implementerad i `cnc`, men **aktiveras först efter inlärning**. Utan inlärning släpper dagens kod igenom för att grundmaskinen ska fungera utan sensorenhet. Efter inlärning ska utebliven eller oklar bild stoppa jobbstart. Inlärning och fysiska felprov måste ingå vid driftsättning; spärren är ingen säkerhetsfunktion och stoppar inte pågående rörelse. Se [beslut 0035](https://github.com/kingkongola/cnc/blob/main/docs/beslut/0035-armsparr-med-kamera.md).
