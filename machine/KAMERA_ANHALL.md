# Core-kamera, Y-anhåll och kalibrering – fysisk design (ej monterat)

**2026-11-08 · Status: konstruktionsunderlag och öppna kontroller – INGEN verifierad montering.**

Program/mätlogik och användarflöde ägs av [cnc/docs/kamera-arbetsflode.md](https://github.com/kingkongola/cnc/blob/main/docs/kamera-arbetsflode.md), [kameraindexering 0033](https://github.com/kingkongola/cnc/blob/main/docs/beslut/0033-dubbelring-kameraindexering.md) och [kalibreringsutredning 0034](https://github.com/kingkongola/cnc/blob/main/docs/beslut/0034-kamerakalibrering-z.md). Detta dokument äger endast fysisk konstruktion och maskinbegränsningar.

## Beslut och tänkt funktion

- Kameran för arbetsstyckesregistrering, indexering och framtida oregelbunden nesting är **Raspberry Pi Camera Module 3 på den rörliga Core**. Hårdvaran är enligt användaren beställd (exakt variant och mottagning bekräftas i `PROCUREMENT.md`). Ingen Tapo krävs för dessa arbetsflöden.
- Även vid en full geometrisk kamerakalibrering behöver en **känt mätt materialyta/plan** finnas för metrisk pixel-till-XY. Befintlig/planerad **BLTouch** kan efter fysisk verifiering användas för ytplanets Z eller trepunktsplan – kameran blir inte därmed en full 3D-skanner.
- **Y-anhållet:** användaren vill skjuta fram mycket långa skivor, t.ex. 2,4 m, mot en list **längs maskinens Y** utan obligatoriskt kortsidesanslag. En låg skruvad list kan monteras ungefär parallellt och rätas med befintligt `cnc anslag trimma`. Färdigtrimmad arbetskant ska ligga **så nära minsta verkligt användbara X** som möjligt; om listen står längre i negativ X skapas onödigt materialspill, i positiv X försvinner fräsbredd. **Exakt läge är EJ valt**.
- Skruvhuvuden måste vara försänkta och fria från fräsbanor; förlägg skruvarna på listens yttersida, aldrig i skärsvängen. Mät verkligt minsta Core-/dammsko-/kameraunderrede-X, fräsradie och motsvarande höjd/Z-svep före borrning. En lista vid X-min kan ändå kollidera med dammskon på tunna ämnen.
- Välj i första hand **låg, löstagbar/segmenterad list** med fri skivförflyttning i Y och gott stöd för långa ämnen. Kontrollera med den verkliga maskinen, med spindeln avstängd, över aktuella X/Y/Z och med hela verktygskedjan monterad.
- Befintliga historiska beslut om **två linjalanslag** i `cnc/docs/beslut/0002-fast-horn.md` och `0015-listorna-ar-linjaler.md` finns kvar; användaren har nu också uttryckt behov av **endast Y-list** för valfri Y-position. Fysisk ombyggnad/val av lösning återstår.

## Indexeringsmarkör

- Två grunda koncentriska gravyrspår runt samma **mekaniska styrhål på arbetsstycket**. Lägg i spill där det är säkert och återanvänd befintlig fräs/operation om möjligt. Exempeldiametrar på spårens centrumlinjer Ø12/Ø20 mm runt Ø6/Ø8 mm indexeringshål, ej fysiskt testade.
- Vid skivförflyttning: mekaniska pinnar bibehålls först; kamera jämför optisk förflyttning i passiv shadow mode. Ringen måste vara åtkomlig för kamera både före och efter förflyttningen. **En markör mäter inte oberoende vridning**; listans raka anliggning måste verifieras eller minst två åtskilda referenser användas.

## Kalibreringsfixtur – vald första metod, ej fysisk kalibrering

- **Valt för första iterationen: 2D-bildanalys med Z-kompensation.** Ta bilder av ett plant kalibreringsmönster vid flera kända **kamera–materialavstånd**. Utgå inte från en enda 2D-homografi som antas giltig vid alla Z. Kalibreringen ska ge metrisk pixel→XY för ett **känt arbetsplan på aktuell höjd**, med uppmätt osäkerhet.
- Ett plant **utskrivet A4 ChArUco-mönster**, utskrivet utan skalning och kontrollerat med skjutmått i **båda** riktningar, fästs på MDF eller annat plant underlag. Knyt tavlans XY till verifierade maskinkoordinater via oberoende referens/fixtur; ett godtyckligt placerat papper räcker inte för fräscentrums koordinater.
- Ta bilder från flera **kända MPos X/Y/Z** med stillastående Core. Kontrollera kamera/objektivets verkliga avstånd, bildfält och fokusområde vid leverans. Håll fokus definierat/låst per kalibrerad serie; förändrad fokusposition kan kräva ny kalibrering eller verifierad profil.
- **BLTouch avses ge materialytans Z** när prob, servoarm, elektrisk anslutning, offset och precision fysiskt är verifierade. Kamerans relativa höjd över materialet bestäms av Core-Z och det uppmätta ytplanet. Innan dess kan känd Z för provskivan användas. BLTouch mäter inte av sig själv full 3D-yta och kompenserar inte för optiskt perspektiv utan kalibreringen ovan.
- Kamerafästet ska vara styvt relativt Core, med säker frigång för dammsko, fräs, Y-anhåll, probe och kablar i hela relevant X/Y/Z. Fysiska offset/plan och verifierad modell finns ännu inte.
- Kontrollhoming är inte en kontinuerlig encoder; verifierad maskinposition för bildtagning får inte antas om steg kan ha tappats.

## Fysiska nästa steg

1. Inventera Camera Module 3-standard eller Wide samt vilket beräkningskort och kabeldragning som ska användas (inget ytterligare inköp är här beslutat).
2. Provmontera kartongattrapp/3D-printat tillfälligt fäste och mät kameras möjliga avstånd till materialplan samt full verktygs-/dammsko-/probe-kollision.
3. Provpassa låg Y-list och trimreserve utan att låsa MPos eller skruvposition; granska överhäng/säker stödning för 2,4 m lång skiva.
4. Provframställ kontrollmätt, maskinregistrerad A4-kalibreringstavla; samla bilder vid **flera kända Z-avstånd** och verifiera Z-kompenserad XY-mätning innan användning. Ingen full 3D-skanning.
