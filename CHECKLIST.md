# Aktuellt arbete och verifieringsstatus

**Uppdaterad 2026-11-11.** Detta är den aktuella arbetslistan. Äldre byggchecklista är [arkiverad](docs/arkiv/2026-11-09-status-och-sensorunderlag.md). Orapporterade kontroller nedan är inte godkända; genomförda byggmoment ska inte beställas eller göras om bara för att ett gammalt arbetskort är obockat.

## LED-belysning – aktuellt beslut 2026-11-10 (D022)

- [x] **Valt komponent-/funktionsval:** BRIMETI COB 24 V / 4000 K / 8 mm / 320 LED/m; **G4-lampor utgår**. Rulle 5 m, uppgivet 10 W/m; 145 kr med Prime enligt användaren. Faktisk betalning/mottagning ej bekräftad.
- [x] Parametrisk **build123d-lågprofil** i [`machine/delar/led/tre_vinklar.py`](machine/delar/led/tre_vinklar.py): horisontell understrut, 3 × LED-riktningar med **provvinklar 0°/15°/35° och 9 mm hyllbredd för 8 mm LED**, och **hård Z-budget 6,65 mm för enbart fästet** under plattan. **Både felvända 90°-CAD:n och tidigare ~21 mm nedsänkta pelarversionen är ogiltiga.**
- [ ] Verifiera build123d-export i CI och att rätt STEP/STL ligger i aktuell artefakt; inga gamla STL/STEP.
- [ ] Kontrollera att aktuell CAD-export från build123d innehåller **rundade hörn och 0,2 mm hyllkantfas i **den nya 1,6 mm tunna hyllan****, inte bara den äldre kantiga modellen. Provprinta en ny export, inte tidigare uppladdad STL/STEP.
- [ ] Kontrollera **längsgående kantstag från lägre sidan av 15°-/35°-hyllorna upp mot 0,9 mm överdel**, anslutning mot central skruvad bas och böjstyvhet vid fria ändar; kontrollera att stagen är bakom ljusytorna. Kontrollera verkligt CAD-intrång **≤6,65 mm för själva fästet relativt understrutten** och mät separat LED-listens/tejpens tillkommande Z och verklig maskinfrigång med fräs/dammsko/arbetsstycke. Provprinta **ett** PETG-fäste; kontrollera två M5/Brace-låspunkter (56 mm c/c), skruvgrepp och hel XYZ-frigång innan full montering.
- [ ] Prova kort LED-sektion på PETG, 24 V och fullt ljus: yttemperatur, tejpens vidhäftning och kamerans skuggor/reflexer. **Aluminiumprofil är inte ett beslutat inköp.**
- [ ] Planera **3 × parallella lödda LED-grenar**, isolerade lödpunkter och dragavlastning, och en gemensam tvåledarmatning på balken. Prova först befintlig passage/kant; **om borrning krävs**, märk en enda genomföring efter kontroll av platta, M5/Brace, båda sidor och full XYZ, avgrada och skydda kabeln. Ingen hålposition eller diameter beslutad.
- [ ] Verifiera befintliga aggregat och dimensionera separat matning för installerad LED-längd; Pi/övervakningen ska fortsatt fungera efter maskinstopp. El-/stoppkrav: [`machine/EL_BELYSNING_OCH_STOPP.md`](machine/EL_BELYSNING_OCH_STOPP.md).

## Hela projektets återstående arbete

Grundmaskinen är byggd och har fräst. Det återstående arbetet gäller dess slutkontroller samt sensorenhetens konstruktion, montage, driftsättning och verifierade användning. En beredd provprint eller fungerande offlinekod betyder inte att hela sensorkedjan är klar.

| Arbetsblock | Vad återstår? |
| --- | --- |
| Konstruktion och passning | Prova mottagna komponenter och hornets nya M3-infästning. Provpassa CR Touch-fästet. Provprinta ett LED-fäste enligt D022. Därefter bered alla slutdelars utskrifter. Detaljer nedan. |
| Print och montage | Skriv ut och montera torn, panel, arm, hylsa och distanser. Kontrollera maskininfästning, skruvar, kabelböjar, hela armrörelsen, hårda stopp, magnetparkering och beteende utan servomatning. |
| Matning och verklig sensorinhämtning | Ställ/prova regulatorerna med last, färdigställ ledningar och dragavlastning. Starta Pi, prova kamera och överföring till värddatorn samt ADXL345. Kopplingsägare: [KOPPLING_CORE_V0.md](machine/delar/sensorer/KOPPLING_CORE_V0.md). |
| CR Touch och verktygsmätare | Verifiera CR Touch-anslutningen, genomför den elektriska provordningen, ta fram/granska komplett maskinkonfiguration, prova arm och stift via Jackpot och därefter kontrollerad kontaktmätning. Verifiera upprepbarhet, avstånd till verktygscentrum och att den andra proben inte kan ge fel mätresultat. [Provförfarande](machine/delar/nollpunkt/INKOPPLING_OCH_PROV.md). |
| Kamera till användbar mätning | Prova egen belysning, låst fokus och verkliga stillbilder. Gör kalibreringsunderlaget, knyt bilden till verifierad stillastående maskinposition, mät XY-fel vid avsedda höjder och prova konturer/öppningar på verkligt trä. Kod finns; fysisk noggrannhet och sammanhängande maskinflöde är inte verifierade. [Fysisk metod](machine/KAMERA_ANHALL.md), [mjukvaruläge](https://github.com/kingkongola/cnc/blob/main/docs/kamera-kod.md). |
| Ljud och vibration | Bekräfta INMP441-leverans och placering, prova faktisk insamling från mikrofon/ADXL345 och jämför med riktiga fräsjobb. Simulatorer bevisar inte att verkliga avvikelser upptäcks. Detta behöver inte blockera första kamera-/probversionen. |
| Grundmaskinens avslut | Bekräfta de dokumenterade kontrollerna för kalibrering, kabel-/slangrörelse, dammhantering och el/maskinstopp enligt avsnittet nedan. Saknad slutrapport är inte bevis på att delarna saknas eller måste byggas om. |

**Utbyggnad efter första fungerande kamera-/probversionen:** verklig bildsammanfogning när en bild inte räcker; prov av optiska skruvbrickor (ännu inte CAD-ritade), Y-anhåll och materialindexering; samt eventuell vidare modell av arbetsstyckets form och historik. Dessa delar är inte färdiga genom offlineprototyperna. Kontinuerlig 2,5D-skanning och AI-/matningsautomatik är inte krav för aktuell mekanik; återupptas endast vid konkret nytta enligt [kameraunderlaget](machine/KAMERA_ANHALL.md) och [mjukvarans avgränsning](https://github.com/kingkongola/cnc/blob/main/docs/kamera-kod.md).

## Sensorenhet — vad är faktiskt klart?

| Delsteg | Status och källa |
| --- | --- |
| Electrokit-leverans | **Mottagen.** Innehåll och övriga leveranser: [PROCUREMENT.md](PROCUREMENT.md). |
| Probmodell och tillgång | **CR Touch Auto Leveling Kit tillgängligt**, enligt användaren. Ersätter tidigare antagen BLTouch; se [PROCUREMENT.md](PROCUREMENT.md). |
| Servots rörelseomfång | **Verifierat och tillräckligt.** [Bänkprovet](CALIBRATION.md#2026-11-10--fällservots-rörelseomfång-verifierat-på-bänk) stänger denna osäkerhet. |
| Sidotorn, panel, arm, probhylsa och distanser | **CR Touch-anpassad CAD finns. Fysisk passning inte verifierad.** Senaste konstruktionsspåret och exportgränsen beskrivs i [CAD-underlaget](machine/delar/sensorer/README.md). |
| Digital kontroll av senaste modellen | Färska CR Touch-exporter med källmanifest och separata CAD-/maskinkontroller. Tredjepartsreferensens begränsningar redovisas i [CAD-underlaget](machine/delar/sensorer/README.md); äldre GitHub-tester gäller ett annat konstruktionsspår. |
| Verkliga komponentmått och passningar | Hornets A–I-mått är [rapporterade](CALIBRATION.md#2026-11-10--servohornets-nav-första-måtten). Formad ficka med M3-bygel finns i CAD och har ett litet provjobb. Glapp, skruvgrepp, verklig spetsform och hela montaget ska provpassas. Övriga komponenters passning mot sidotornet och CR Touchens kropp/kontakt är fortfarande inte verifierade. |
| Belysning | D022: COB-list under horisontell understrut, se LED-avsnittet ovan. Tornets lampdocka och G4-bärare har utgått ur printplanen. |
| Printberedning | Kamera-, CR Touch- och hornprov (lampdockprovet har utgått enligt D022) har egna jobb och källmanifest. [Jobb och provförfarande](print/README.md). Hela sidotornets slutliga utskriftsleverans återstår. |
| Provprint och fysisk montering | Inte rapporterat utförda för sidotornet. |
| Jackpot3-styrning, kamera och accelerometer | Inte rapporterat driftsatta i sensorenheten. Valda pinnar är ett konstruktionsbeslut, inte ett utfört kopplingsprov. |
| Kamerakalibrering och CR Touch-mätning | Inte fysiskt verifierade. |

## Nästa arbete — inför första provprint

1. **Prova horninfästningen:** skriv ut den lilla fickan och M3-bygeln och prova med originalhornet samt två befintliga M3×10. Kontrollera klämväg, skruvgrepp och glapp enligt [provförfarandet](print/README.md#servohorn--ficka-och-m3-bygel). Hornets A–I-mått är rapporterade; fysisk passning är nästa steg. Jämför även mottagna kamera-/Pi-kort, flatkabelkontakter, LM2596-moduler och servots fästöron mot CAD. Resultat förs i [mätloggen](CALIBRATION.md), måttändringar i CAD-källan.
2. **Utgått enligt D022, printas inte:** ~~Prova den nya lampdockan:~~ verifiera styrtapp och skruvgrepp med den lilla kalla provplattan. Lampbäraren kan ändras efter lampval utan att kamerafästet ritas om; verkliga sockeladaptrar, temperatur och kabelåtkomst är kvar enligt [CAD-underlaget](machine/delar/sensorer/README.md). Referensmodeller av elektronik, lampor och kablar ska inte bli utskriftsdelar.
3. **Övriga passningsprov:** skriv ut [kamerafickeprovet och CR Touch-provet](print/README.md) och prova mot mottagna komponenter. Välj därefter små provbitar för Pi, regulatorer och servo där en trång passning kan tvinga fram omprint av hela tornet. Varje jobb ska printkontrolleras, skivas och förhandsvisas före utskrift.
4. **Provprinta och montera för hand:** kontrollera skruvåtkomst, komponenthållning, kabelböjar och armens frigång. Detta kräver inte att hela kameramjukvaran är färdig.
5. **Efter passningsprov:** skriv ut resterande delar och ställ in den monterade armens två pulsvärden. Prova magnetparkering, rörelse och strömbortfall. Servots redan godkända rörelseomfång behöver inte utredas på nytt.

KW11-/Omron-armbrytare och deras hållare ingår inte, enligt D020. Se [inkopplingsprovet](machine/delar/nollpunkt/INKOPPLING_OCH_PROV.md) inför senare el- och funktionsprov; det är ett provförfarande, inte en andra statuslista.

## Grundmaskin — kvarstående dokumenterade kontroller

- [ ] Z-nivå efter permanenta struts och planfräst offerskiva; ännu inte loggad som godkänd i [CALIBRATION.md](CALIBRATION.md).
- [ ] Ytterligare squaringkontroll efter offerskivearbetet som begärdes i byggloggen. Den tidigare godkända mätningen ska inte raderas; se mätloggen.
- [ ] Full X/Y/Z-rörelse med slang och kablar, därefter slutlig dragavlastning och uppmätta kabelkaplängder i [CABLE_ROUTING.md](CABLE_ROUTING.md).
- [ ] Cyklonens färdigställande, behållare, ventil-/vakuumprov och jordväg för dammhanteringen: senaste loggade status finns i [BUILD_LOG.md](BUILD_LOG.md). Senare slutrapport saknas.
- [ ] Bekräfta slutligt utförande/prov av kapsling, dragavlastning och maskinstopp/NVR (återstartsskydd, som hindrar automatisk start efter strömavbrott). Någon slutrapport för dessa elkontroller har inte hittats i genomgången. Kraven ägs av [AUDIT.md](AUDIT.md); detta är inte en uppgift om att installationen faktiskt saknas.

Dessa punkter hindrar inte fristående provprint av sensordelar. Maskinrörelser och probning kräver sitt eget verifierade förfarande.
