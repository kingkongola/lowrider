# Aktuellt arbete och verifieringsstatus

**Uppdaterad 2026-11-10.** Detta är den aktuella arbetslistan. Äldre byggchecklista är [arkiverad](docs/arkiv/2026-11-09-status-och-sensorunderlag.md). Orapporterade kontroller nedan är inte godkända; genomförda byggmoment ska inte beställas eller göras om bara för att ett gammalt arbetskort är obockat.

## Hela projektets återstående arbete

Grundmaskinen är byggd och har fräst. Det återstående arbetet gäller dess slutkontroller samt sensorenhetens konstruktion, montage, driftsättning och verifierade användning. En beredd provprint eller fungerande offlinekod betyder inte att hela sensorkedjan är klar.

| Arbetsblock | Vad återstår? |
| --- | --- |
| Konstruktion och passning | Prova mottagna komponenter, mät servohornet och färdigställ dess koppling till armen. Provpassa CR Touch-fästet och lampdockan; välj/mät lampor och socklar för den separata bäraren. Därefter bered alla slutdelars utskrifter. Detaljer nedan. |
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
| Verkliga komponentmått och passningar | Servohornets navmått och två breddmått är [rapporterade](CALIBRATION.md#2026-11-10--servohornets-nav-första-måtten); tjocklek, hållägen och montage återstår. Formad ficka med justerbar klämning är konstruktionsprincip, ännu inte färdig CAD. Komponenternas passning mot sidotornet är inte verifierad. CR Touchens kropp, kontakt och frigång behöver kontrolleras mot CAD innan probdelarna slutprintas. |
| Belysningens eftermontering | Fast lampdocka och separat bärare finns i CAD. Digitalt kontrollerade gränssnitt och servicebana; sockeladaptrar, vald lampa, ledningar, värme och ljusbild återstår. Bäraren är utkast. |
| Printberedning | Kamerafickeprov, CR Touch-prov med armfot/hylsa och kallt lampdockprov har egna jobb och källmanifest. [Jobb och provförfarande](print/README.md). Hela sidotornets slutliga utskriftsleverans återstår. |
| Provprint och fysisk montering | Inte rapporterat utförda för sidotornet. |
| Jackpot3-styrning, kamera och accelerometer | Inte rapporterat driftsatta i sensorenheten. Valda pinnar är ett konstruktionsbeslut, inte ett utfört kopplingsprov. |
| Kamerakalibrering och CR Touch-mätning | Inte fysiskt verifierade. |

## Nästa arbete — inför första provprint

1. **Provpassningens mått:** jämför de mottagna kamera-/Pi-korten, flatkabelns kontakter och LM2596-modulerna med CAD. Mät servots fästöron och hur dess servoarm/horn ska fästas i den printade armen. Provpassa den tillgängliga CR Touchens kropp, hålbild, kontakt och stift mot den nya CR Touch-geometrin innan arm/hylsa slutgodkänns. Resultat förs i [mätloggen](CALIBRATION.md), måttändringar i CAD-källan.
2. **Prova den nya lampdockan:** verifiera styrtapp och skruvgrepp med den lilla kalla provplattan. Lampbäraren kan ändras efter lampval utan att kamerafästet ritas om; verkliga sockeladaptrar, temperatur och kabelåtkomst är kvar enligt [CAD-underlaget](machine/delar/sensorer/README.md). Referensmodeller av elektronik, lampor och kablar ska inte bli utskriftsdelar.
3. **Passningsproven är beredda:** skriv ut [kamerafickeprovet och CR Touch-provet](print/README.md) och prova mot mottagna komponenter. Välj därefter små provbitar för Pi, regulatorer och servo där en trång passning kan tvinga fram omprint av hela tornet. Varje jobb ska printkontrolleras, skivas och förhandsvisas före utskrift.
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
