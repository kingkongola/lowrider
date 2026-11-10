# Aktuellt arbete och verifieringsstatus

**Uppdaterad 2026-11-10.** Detta är den aktuella arbetslistan. Äldre byggchecklista är [arkiverad](docs/arkiv/2026-11-09-status-och-sensorunderlag.md). Orapporterade kontroller nedan är inte godkända; genomförda byggmoment ska inte beställas eller göras om bara för att ett gammalt arbetskort är obockat.

## Sensorenhet — vad är faktiskt klart?

| Delsteg | Status och källa |
| --- | --- |
| Electrokit-leverans | **Mottagen.** Innehåll och övriga leveranser: [PROCUREMENT.md](PROCUREMENT.md). |
| Servots rörelseomfång | **Verifierat och tillräckligt.** [Bänkprovet](CALIBRATION.md#2026-11-10--fällservots-rörelseomfång-verifierat-på-bänk) stänger denna osäkerhet. |
| Sidotorn, panel, arm, BLTouch-hylsa och distanser | **Ritade.** Senaste konstruktionsspåret och exportgränsen beskrivs i [CAD-underlaget](machine/delar/sensorer/README.md). |
| Digital kontroll av senaste modellen | Lokala STL-exporter finns och kontrollerades för tät, sammanhängande geometri. De äldre automatiska GitHub-testerna gäller ett annat konstruktionsspår. Ny export från aktuell källa och printkontroll återstår före utskrift. |
| Verkliga komponentmått och passningar | Inte rapporterat verifierade mot sidotornet. BLTouch är ännu inte hämtad enligt senaste rapport. |
| Printberedning | Ett litet kamerafickeprov är exporterat från aktuell källa, printkontrollerat och skivat. [Jobb och provförfarande](print/README.md). Hela sidotornets utskriftsleverans återstår. |
| Provprint och fysisk montering | Inte rapporterat utförda för sidotornet. |
| Jackpot3-styrning, kamera och accelerometer | Inte rapporterat driftsatta i sensorenheten. Valda pinnar är ett konstruktionsbeslut, inte ett utfört kopplingsprov. |
| Kamerakalibrering och BLTouch-mätning | Inte fysiskt verifierade. |

## Nästa arbete — inför första provprint

1. **Provpassningens mått:** jämför de mottagna kamera-/Pi-korten, flatkabelns kontakter och LM2596-modulerna med CAD. Mät servots fästöron och hur dess servoarm/horn ska fästas i den printade armen. Hämta BLTouch och kontrollera dess kropp, hål, kontakt och stift innan arm/hylsa låses. Resultat förs i [mätloggen](CALIBRATION.md), måttändringar i CAD-källan.
2. **Kontrollera belysningens eftermontering och exportera senaste sidotornet:** verifiera plats för LED, lödanslutningar och senare åtkomst innan huvudtornet printas, enligt [belysningsförslaget](machine/KAMERA_ANHALL.md#eftermontering--förslag-diskuterat-2026-11-10-ej-färdig-konstruktion). Tydlig lista över utskriftsdelar och antal finns i [CAD-underlaget](machine/delar/sensorer/README.md). Referensmodeller av elektronik och kablar ska inte bli utskriftsdelar.
3. **Första passningsprovet är berett:** skriv ut [kamerafickeprovet](print/README.md) och prova mot mottagen kamera. Välj därefter små provbitar för Pi, regulatorer och servo där en trång passning kan tvinga fram omprint av hela tornet. Varje jobb ska printkontrolleras, skivas och förhandsvisas före utskrift.
4. **Provprinta och montera för hand:** kontrollera skruvåtkomst, komponenthållning, kabelböjar och armens frigång. Detta kräver inte att hela kameramjukvaran är färdig.
5. **Efter passningsprov:** skriv ut resterande delar och ställ in den monterade armens två pulsvärden. Prova magnetparkering, rörelse och strömbortfall. Servots redan godkända rörelseomfång behöver inte utredas på nytt.

KW11-/Omron-armbrytare och deras hållare ingår inte, enligt D020. Se [inkopplingsprovet](machine/delar/nollpunkt/INKOPPLING_OCH_PROV.md) inför senare el- och funktionsprov; det är ett provförfarande, inte en andra statuslista.

## Grundmaskin — kvarstående dokumenterade kontroller

- [ ] Z-nivå efter permanenta struts och planfräst offerskiva; ännu inte loggad som godkänd i [CALIBRATION.md](CALIBRATION.md).
- [ ] Ytterligare squaringkontroll efter offerskivearbetet som begärdes i byggloggen. Den tidigare godkända mätningen ska inte raderas; se mätloggen.
- [ ] Full X/Y/Z-rörelse med slang och kablar, därefter slutlig dragavlastning och uppmätta kabelkaplängder i [CABLE_ROUTING.md](CABLE_ROUTING.md).
- [ ] Cyklonens färdigställande, behållare, ventil-/vakuumprov och jordväg för dammhanteringen: senaste loggade status finns i [BUILD_LOG.md](BUILD_LOG.md). Senare slutrapport saknas.

Dessa punkter hindrar inte fristående provprint av sensordelar. Maskinrörelser och probning kräver sitt eget verifierade förfarande.
