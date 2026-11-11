# Decisions

Endast beslut som påverkar den LowRider V4 som faktiskt byggs. Nyare beslut supersederar äldre när det anges uttryckligen. **Aktuell fysisk status ägs av CHECKLIST.md, inte av daterade beslutstexter.** För sensorenheten gäller D020 (ändlägesprincip) och D021 (pinnval). D017–D019 nedan innehåller äldre konstruktionsspår och läses med sina ersättningsnotiser.

## D001 — LowRider V4
**Status:** låst

Bygg LowRider V4. PrintNC och IndyMill är inte aktiva alternativ.

## D002 — Arbetsyta 650 × 1250 mm
**Status:** låst

Geometri:
- X-rör 816 mm ×2
- Y-rör 1505 mm
- Ø30×1,5 mm
- strut-input 819 mm
- `front_wing_size=10.8`
- GT2 999 / 1705 / 1705 mm = 4409 mm
- minimum bord 941 × 1563 mm
- praktisk maskinbredd runt 941 mm minimum

## D003 — Standardnära bygge först
**Status:** låst

Få standardmaskinen körklar innan modifieringar. Uppgraderingar kräver ett visat behov.

## D004 — Begagnat styvt bord som direkt maskinbas
**Status:** låst

**Uppdaterat 2026-09-19:** begagnad **180×100 cm bordsskiva köpt för 300 kr**. Den används direkt som strukturell maskinbas om underredet är styvt. Kontrollera underredet före montering och bygg/förstärk endast om behov finns.

Den köpta skivan rymmer 941×1563 mm minimumfootprint utan den tidigare planerade kantbreddningen för ett 90 cm-bord. Köp inte hel extra OSB/ply-deck utan verifierat behov.

Separat löstagbar ~12 mm MDF används som spoilboard över arbetszonen.

## D005 — Jackpot2 som tekniskt router-first-val
**Status:** superseded av D015

Jackpot2 var det tekniskt billigaste rimliga valet för router-only eftersom snabb laser-PWM inte behövs. Detta är fortfarande en korrekt funktionsbedömning men är inte längre aktiv köpväg.

## D006 — Router: KATSU 101750
**Status:** köpt 2026-09-03

KATSU `101750`, 220–240 V / 710 W / variabelt varvtal / cirka 65 mm kropp, Makita RT0700-familjens formfaktor. Köpt via Amazon.se. Köpt HaWiWe/Elaire Makita-style 1/8" collet ska provpassas och runout verifieras före riktig fräsning.

VEVOR `0700C` är blacklistad/replaced och ska inte köpas.

## D007 — Dammhantering i grundbygget
**Status:** låst

LR4 dust shoe + befintlig DeWalt shop-vac + cyklon + separat uppsamlingsbehållare + slangavlastning. Statisk jordväg ska vara löst före regelbunden MDF/trä/XPS-körning.

## D008 — Laser senare
**Status:** uppskjutet

Laser tidigast 2027 och får inte överoptimera grundbygget.

## D009 — Plasma utanför nuvarande bygge
**Status:** låst

Plasma styr inte bord, controller, el eller inköp i nuvarande bygge. Först byggs och driftsätts en vanlig router-LR4.

En eventuell modulär plasmavariant är ett separat framtida projekt, tidigast nästa vinter. Ingen plasma-framtidssäkring ska få komplicera eller fördyra version 1.

## D010 — Mean Well + Omron + DigiKey-konsolidering
**Status:** låst

- Mean Well `HDR-60-24`, 24 V / 2,5 A / 60 W.
- 10 × Omron `SS-3GL13PT`, 5 installerade + 5 reserv, NC via COM+NC.
- DigiKey samlar även 16 × 608-2RS, Wago, nätgenomföringar, Faston och lågspänningskablar enligt `PROCUREMENT.md`.

## D011 — Ø30 mm rails
**Status:** låst

Alla diameterberoende printar = 30 mm. Permanenta struts: `strut_length=819`, `front_wing_size=10.8`.

## D012 — Fast elbox + rörlig controller
**Status:** superseded av D016

Tidigare plan: NVR + HDR fasta på bordet, Jackpot3 på rörlig balk och lång rörlig 24 V-kabel. Omprövat eftersom V1E:s balkmonterade aggregat ger kortare 24 V-rutt utan att eliminera rörlig 230 V-kabel till fräsen.

## D016 — Tillbaka till V1E:s placering av 24 V-aggregatet
**Status:** beslutad plan; fysisk och elsäker monteringskontroll återstår

NVR/maskinstopp sitter fast och åtkomligt på bordet. Jackpot3 samt Mean Well HDR-60-24 planeras på rörlig balk enligt V1E:s princip. Mean Well-aggregatet är inte identiskt med V1E:s exempel: verifiera lämplig kapsling/beröringsskydd, DIN-infästning, ventilation och dragavlastning innan 230 V ansluts. HDR är klass II utan PE-plint; eventuell skyddsjord i övrig installation och slangjord hanteras separat. Ingen oskyddad nätspänningsplint på balken. Använd inte den långa 24 V-slingan från det gamla förslaget utan ett konkret monteringsbehov. Kontrollera fräskabel, aggregatets matning, motor/endstop och dammsugarslang samtidigt genom hela rörelseområdet. Den redan köpta 3 m 20 AWG-kabeln finns i BOM, men behöver inte användas i denna rutt.

## D013 — NVR/maskinstopp
**Status:** låst; **NVR-brytaren ersatt av D024** (2026-11-10). Kravet på tydlig, lättåtkomlig stoppfunktion gäller.

Kravet är 230 V NVR/no-voltage-release med lämplig märkström, tydlig lättåtkomlig stoppfunktion och dokumenterad terminalkoppling. Exakt KEDU-proveniens är inte ett projektkrav. Funktionen kallas NVR/maskinstopp, inte verifierad safety-rated E-stop.

## D014 — Commissioning-dependencies
**Status:** låst

Inventera data-USB-C och FAT32 microSD innan köp. T8 400 mm kapas efter fysisk assembly-check, praktiskt mål ~150–160 mm ×2, inte automatiskt i halvor. **Förtydligat 2026-09-29:** V1E anger 145 mm eller längre; detta bevisar inte att 150 mm passar våra faktiska kopplingar/muttrar. Provpassa en sida i taget före kapning enligt manualens kapitel 0. Endstops är home/auto-square, inte runtime hard limits.

## D024 — Ett stopp för hand och från Pi:n: kontaktor för KATSU, larmingång för Jackpot
**Status:** valt 2026-11-10 av användaren; ersätter D013:s NVR-brytare (KJD12 köps inte). Inget köpt eller inkopplat. Delar: [PROCUREMENT.md](PROCUREMENT.md#katsu-stopp-från-pin-trådbundet--planerat-ej-beställt).

- **KATSU** matas via en kontaktor (24 V spole). Nödstoppets ena brytkontakt och Pi:ns utgång sitter i spolens krets. Spolen släpper vid nödstopp, Pi-larm, Pi-krasch, omstart eller strömavbrott. Pi:n drar den bara efter tryck på grön startknapp, och dess pinnar är av vid start, så KATSU startar aldrig av sig själv. Detta ersätter NVR-funktionen.
- **Jackpot** bryts inte. Nödstoppets andra brytkontakt och Pi:ns stoppsignal (via optokopplare) ligger i serie på **en** ingång, satt som FluidNC-larmingång (`control/estop_pin`). Öppen krets = stopp och larm. Motorerna behåller ström, så Z faller inte.
- **Ingång:** alla sju skyddade ingångar är tagna (fem ändlägen, `gpio.36` prob, `gpio.39` planerad verktygslängdsknapp). **Stoppet tar `gpio.39`** (användaren 2026-11-10), eftersom det är viktigare och behöver skyddad ingång. Verktygslängdsknappen flyttas till modulporten (`gpio.13`/`gpio.14`, oskyddad 3,3 V) eller stryks; inte avgjort.
- **Avvägning, medvetet vald:** motorernas stopp är programvara, inte strömbrytning. Stegmotorer stannar när pulserna upphör; fräsen, den farliga delen, bryts elektriskt.
- **Falskt stopp är billigt** tack vare körlogg, återstart och svarta lådan i `cnc` (0019, 0031). Därför får sensorer stoppa. Villkor: återstarten provas en gång på riktiga maskinen med avsiktligt stopp på spill. Pushover-notis skickas efter stopp men ingår inte i stoppkedjan.
- **Före inkoppling:** att FluidNC 3.9.9 stoppar som väntat på `estop_pin`, kontaktorns motorlastklass, och att spolens matning (D023) finns.
- **Inte säkerhetsklassat (förtydligat 2026-11-11, granskning issue #2):** laddningspumpen och Pi:ns stoppvakt är ett övervakningsstopp, inte en säkerhetsklassad nödstoppskrets. Nödstoppsknappens brytande kontakter är säkerhetskedjan. Stoppvakten kör i övervakat läge (start kräver friska sensorer och hjärtslag från datorn) eller uttryckligt manuellt läge.
- **Utförande 2026-11-11 (förslag, ej provat):** Pi:n styr spole och larmslinga med **en pulsad signal via laddningspump**, inte med fasta utgångar, så att en Pi som hänger sig också släpper kontaktorn. Pinnar: OK-puls `GPIO23`, startknapp `GPIO25`. Schema och bänkprov: [EL_BELYSNING_OCH_STOPP.md](machine/EL_BELYSNING_OCH_STOPP.md#elschema-matning-och-stoppkedja-2026-11-11-förslag-ej-provat).

## D023 — Två matningsgrupper: maskin och övervakning
**Status:** valt 2026-11-10 av användaren; inget köpt eller inkopplat. Underlag: [EL_BELYSNING_OCH_STOPP.md](machine/EL_BELYSNING_OCH_STOPP.md).

- **Maskin:** KATSU på 230 V; Mean Well HDR-60-24 till Jackpot3 och motorer; LM2596 B **6,0 V** till fällservot. **Förtydligat 2026-11-11 enligt D024:** nödstoppet bryter bara KATSU; HDR nr 1 och Jackpot behåller ström så att Z inte faller, och bryts först när maskinen kopplas från nätet. Servot hör hit eftersom Jackpot styr det: en avstängd Jackpot får inte lämna servot strömsatt med flytande signal.
- **Övervakning, lever efter stopp:** egen matning före maskinstoppet; LM2596 A **5,1 V** till Pi, kamera, ADXL och mikrofon.
- **CR Touch matas från Pi:ns 5,1 V** (Pi:ns 5 V-stift eller buck A, samma skena). Endast styrsignal (`gpio.26`), kontaktsignal (`gpio.36`) och jord går till Jackpot. Inget extra kablage vid Jackpot och ingen tredje buck i tornet.
- **Godtagen korsning:** med Jackpot avstängd kan proben mata in högst ca 0,5 mA via ingångens 10 kΩ (beräknat, ej uppmätt). Försumbart. Proben kör sitt självtest när Pi:n startar, inte när maskinen gör det.
- **Nätdel vald 2026-11-11 av användaren:** en andra Mean Well HDR-60-24 eller likvärdig 24 V DIN-nätdel, före nödstoppet. Den matar övervakningen, LED-listen (lyser efter stopp så kameran ser) och kontaktorns spole (D024), ca 30 W av 60 W. Inte beställd.

## D022 — COB-list ersätter G4-lampor för LowRider-belysning
**Status:** valt 2026-11-10; montering, strömförsörjning och CAD ej fysiskt verifierade

**Aktuellt belysningsval är BRIMETI 24 V COB LED-list**: 5 m rulle, 4000 K neutralvit, **8 mm** bredd, 320 LED/m, säljaruppgift **10 W/m och 100 lm/W**, pris **145 kr via Amazon Prime** enligt användaren. Angivet ljusflöde är därmed cirka 1 000 lm/m, inte uppmätt. Inköp/betalning/mottagning verifieras separat. **Tidigare idéer med G4-lampor, den gamla 12 V RGB-listen eller enbart kameranära LED som huvudbelysning är inte längre aktuella. Köp eller CAD-projektera inte G4-lampor till detta bygge.** Detta är ett komponent- och funktionsval, inte ett påstående att ljusmängden eller CRI är verifierad.

**Placering och Z-budget (35° accepterat 2026-11-10):** tre 8 mm remsor på LowRider V4:s **horisontella undre strutplatta** längs X, **en rakt ned och två framåt**. Aktuellt parametriskt prov: **0°/15°/35°**, **9 mm breda hyllor till 8 mm LED-list**, med längsgående stag upp mot en tunn överyta. Användaren accepterar **cirka 6,6 mm nedstick för själva fästet**. Teoretiskt max blir **6,62 mm**; koden använder en strikt avrundningsmarginal på **6,65 mm** (`max_z_intrang_mm`). LED-listens/tejpens egen tjocklek, lödning och möjliga skruvskallar ingår inte. De tidigare 0°/15°/30°, 0°/15°/25° och 0°/25°/50° är supersederade som aktuella CAD-vinklar. **Z-minimering är fortsatt prioriterad**; ingen vinkel får ökas utan kontroll av faktisk utskjutning och ljusbild.

**Ogiltiga modeller:** den första 90° felvända strutmodellen och den efterföljande cirka 21 mm nedhängande modellen. [Aktuell build123d-källa](machine/delar/led/tre_vinklar.py) använder de två befintliga M5/Brace-positionerna 56 mm c/c i `strut_plate.svg`. Riktig Brace-kollision, M5-grepp, rörelse, temperatur, printbarhet och belysningsbild är ännu **inte verifierade**. [Detaljerad montagegrind](machine/delar/led/README.md). **Ingen separat aluminiumprofil som första lösning.**

**Matning:** befintlig Mean Well HDR-60-24 (24 V/60 W) reserveras för Jackpot3 och motorerna. LED och Pi ska inte okritiskt läggas på den. LED-matning dimensioneras efter faktiskt monterad längd (10 W/m uppgivet); återbruk av befintliga aggregat utreds innan ytterligare köp. Pi/kamera ska kunna övervaka/logga efter frånkopplad maskin och får därför inte vara beroende av maskinens brutna matningsgren. Fysisk NVR/stoppväg kvarstår oberoende av sensorövervakning. Automatisk kompletterande frånkoppling ska utredas separat. **Inget färdigt elschema och ingen säkerhetsklassning genom detta beslut.**

**Ägare:** [samlad fysisk SSOT/elektrisk status](machine/EL_BELYSNING_OCH_STOPP.md), [LED-fästets kontrollgrindar](machine/delar/led/README.md), [komponentstatus i BOM](BOM.md). Kamerabildens mätkvalitet verifieras separat. G4 i G-kod betyder väntkommando och har inget med lampvalet att göra.

## D021 — Pinnar på Jackpot3 för sensorenhetens arm och BLTouch
**Status:** valt 2026-11-09 på användarens uppdrag; ej inkopplat, `machine/AKTIV` och FluidNC är oförändrade

**Modelluppgift 2026-11-10:** den tillgängliga proben är CR Touch Auto Leveling Kit, se [orderlistan](PROCUREMENT.md). Beslutet nedan togs med BLTouch som antagande. Pinnvalet ligger kvar som plan, men CR Touchens elektriska kompatibilitet måste verifieras enligt [kopplingsunderlaget](machine/delar/sensorer/KOPPLING_CORE_V0.md) före anslutning. Detta är ingen konfigurationsändring.

**Fällservots signal på `gpio.27`, BLTouch-styrning på `gpio.26`, BLTouch-signal på `gpio.36` (probe-porten).** Fast verktygslängdsknapp flyttas till `gpio.39` som `toolsetter_pin` (**ersatt av D024:** `gpio.39` går till stoppet). Utgångarna ställs på 5 V, inte 24 V, med bygeln på kortet. Armen och proben styrs alltså från Jackpot, inte via Wi-Fi från Pi:n.

**Varför:** de fyra utgångsportarna (`gpio.26/27/0/2`) är de enda med full PWM på 5 V-läget. `gpio.0/2` är startpinnar på ESP32, så de undviks. `gpio.26` kan ge en kort puls vid start enligt V1 Engineering; den går till BLTouch, där uppstartsbeteendet behöver provas separat utan att fällarmen drivs av samma signal, och `gpio.27` till servot. `gpio.36` är den port probe redan använder.

**Inför inkoppling:** bygeln kontrolleras med multimeter, utgångens signalnivå mäts, och BLTouch-signalens polaritet provas med `?`-rapporten före G38. Konfigändringen står i `machine/delar/sensorer/KOPPLING_CORE_V0.md`.

## D020 — Inga armbrytare: hårda stopp, tyngdkraft och kamerakontroll
**Status:** beslutat 2026-11-09; ersätter brytarkraven i D017–D019. Senaste arbetsmodell är `machine/delar/sensorer/sidotorn.py`. Aktuell provstatus: [CHECKLIST.md](CHECKLIST.md).

Armens lägen avkänns **inte** med KW11. De två hårda stoppen bestämmer lägena. **Parkerat ligger armen vid -150 grader och hålls av en Ø6 x 3 mm neodymmagnet i stoppet mot ett M3-skruvhuvud i armen, så att den inte faller vid strömavbrott.** Kameran ska bekräfta parkerat läge som **startspärr före varje jobb när sensorenheten tas i bruk**. Dagens kod aktiverar spärren först efter inlärning; därefter ger inget svar eller oklar bild ingen start. Före inlärning släpper koden igenom så att grundmaskinen kan användas utan sensorenhet. Inlärning och fysisk verifiering återstår. Spärren är ingen säkerhetsfunktion och stoppar inte pågående rörelse, enligt `machine/delar/sensorer/KOPPLING_CORE_V0.md`.

**Varför:** sökning i CAD hittade ingen plats för brytaren i utfällt läge utan extra bärande del. Utan brytare försvinner hållare, tapp, lödning och två Jackpot-ingångar.

**Magneten** sätts in bakifrån i stoppet mot 0,6 mm plast och låses med en droppe superlim på baksidan; skruvhuvudet slår aldrig på magneten. Servot är original från Arrma Quake och orkar dra loss armen. **Prov före drift:** att magneten håller armen med servot strömlöst när maskinen körs. De 10 köpta KW11 behålls som reservdelar. Spärrens programvara hör till `kingkongola/cnc`.

## D019 — Separata KW11-brytare på servokassetten, spara Omron
**Status:** historiskt brytarspår; ersatt av D020. Inköpet är fortsatt verkligt, men brytarna är reservdelar. Texten nedan beskriver det tidigare förslaget.

Beställt **10 × QUARKZMAN KW11-3Z-N med rullspak (COM/NO/NC)** på Amazon.se för visade 92,94 kr, fri Prime-frakt, beräknad leverans lördag **2026-11-14**. De **befintliga Omron SS-3GL13PT är reserv för originalmaskinens ändlägen**; förbrukas inte på sensorenheten.

En enda liten **build123d KW11-hållare printas 2 ×** och har justerbara M2-hål för 8,5–9,5 mm brytarhålbild och M3-slits för lägesjustering. Båda brytarna tillhör löstagbar servokassett; Core, kamera och Pi behöver inte ändras. [Grön CAD-körning med 11 STL + 11 STEP](https://github.com/kingkongola/lowrider/actions/runs/42616662416), inga BRep-överlapp med våra fasta moduler eller i det förenklade BLTouch-svepet. **Aktiveringskammar och två separata hårdstopp saknas fortfarande och är P0**; grön CAD betyder inte att man har verifierat rullspaksvägen. Inga GPIO/maskininställningar ändrade.

## D018 — Modulär sensorenhet i build123d, original-Core orörd
**Status:** äldre modulärt CAD-spår (2026-11-09). Principerna om servicebarhet och original-Core gäller; brytarkraven ersätts av D020. Senaste sidotornsmodell och dess egen kontrollstatus beskrivs i [CAD-underlaget](machine/delar/sensorer/README.md). Följande stycken är den daterade modulgranskningen.

Det som tidigare i chattar kallades "Core-enheten" ska heta **sensorenheten**; **Core** betyder enbart V1E:s befintliga del. Löstagbar gemensam bärplatta på **två befintliga M5 från servoarm C:s verktygsfäste**, skruvade och individuellt utbytbara kamera, SPMS664/BLTouch, Pi Zero, ADXL345 och INMP441. Ingen helplastklump, inga nya borrhål på Core. Skruvat kanallock gör kabelstammen inspekterbar. Servo ska kunna bytas utan att kamera och dess kalibrering rubbas.

**Då granskad CAD:** [build123d `core_enhet.py`](machine/delar/sensorer/core_enhet.py), [dokument](machine/delar/sensorer/README.md), [kabel-/GPIO-utkast](machine/delar/sensorer/KOPPLING_CORE_V0.md). Den tidigare OpenSCAD-prototypen (`core_sensorer_v0.scad`) är arkiverad; dess gamla STL/zip ska **inte printas för montage**. [GitHub CI 42609388224](https://github.com/kingkongola/lowrider/actions/runs/42609388224): 10 separata vattentäta STL och 10 STEP, inga BRep-kollisioner i statiskt montage eller 0–90° probarmssvep mot **egna** CAD-delar/servoskissen, färgkodad GLB. **Inget provat på riktig maskin.**

**Öppna frågor vid den äldre modulgranskningen:** fysisk passning, servohorn, då planerade brytarrullar, stopp, stift, kablar och pinnval var inte verifierade. Brytarkraven har därefter ersatts av D020 och pinnvalet avgjorts i D021. Aktuellt återstående arbete läses i CHECKLIST.md, inte i denna historiska granskning. En fläkt är inte basfunktion; termisk mätning först.

## D017 — Core-kamera och mätarm: minsta fysiska prototyp
**Status:** historiskt prototypunderlag från 2026-11-09, följt av D018–D021. Följande leverans- och pinnstatus avser beslutstillfället; aktuell status finns i ägarfilerna.

Vid beslutstillfället var Camera Module 3 **Standard** och Pi Zero 2 WH beställda och inte mottagna; senare leveranser ägs av PROCUREMENT.md. Pi placeras inom 200 mm CSI-kabel från kameran på Core, med **fläktlös provkapsling** tills mätt termiskt behov finns. Tidigare plan att prova befintlig belysning före LED-inköp **ersätts av D022 (2026-11-10)**: huvudbelysningen är BRIMETI COB under horisontell understrut; separat kamera-LED är en möjlig senare optisk komplettering.

Servoarm **C** används som mekaniskt referens-CAD. Ny BLTouch-anpassning utgår från samma servoaxel, men kroppens korta stift, horisontella frigång, kabel och lodrätt mätläge **är ännu inte verifierade**. Den äldre cylindriska klämman ersätts i *prototypstudien*, inte på den levande CNC:n. Skannerförsprång och 2,5D är **parkerade**, får inte skapa nya CAD-krav.

S-09 (två mekaniskt åtskilda vilolägen, utan mux i basplanen) ligger kanoniskt i [cnc:s sensorarkitektur](https://github.com/kingkongola/cnc/blob/main/docs/sensorarkitektur.md). Vid detta beslutstillfälle var inga nya GPIO reserverade; D021 anger det senare pinnvalet. Se [JACKPOT3_IO.md](machine/delar/nollpunkt/JACKPOT3_IO.md) och [kopplingsunderlag](machine/delar/sensorer/KOPPLING_CORE_V0.md). Ingen maskinkonfiguration eller motor-rörelse får ändras av detta beslut.

## D015 — Jackpot3 från Elecrow
**Status:** **köpt 2026-09-03**

Controller är **Elecrow Jackpot3 `CQA240812C2`**.

- checkout: controller 69,44 € efter rabatt + DDP Economy 14,11 € = 83,55 €
- faktisk bankdebitering: **937 kr**
- DDP valdes för att undvika separat tull-/transportörshantering
- beslutet är nu stängt; Jackpot2-fallbacken är inte längre aktiv

Laser är fortfarande uppskjuten och var inte skälet till köpet.
