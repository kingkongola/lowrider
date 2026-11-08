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

- **Första iterationen är en plan 2D-homografi vid en definierad kamerahöjd och materialyta**, inte fullständig 3D-kameramodell. Testa mot olika Z-höjder innan höjdkompensation eller avancerad kalibrering byggs. BLTouch är senare en möjlig källa till uppmätt material-Z men löser inte kamerans perspektiv automatiskt.

- Ett plant **utskrivet A4 ChArUco-mönster**, i faktisk 100 % skala och kontrollerat med skjutmått i **båda** riktningar, fastsatt på MDF eller annat plant underlag. Papprets placering måste också vara **geometriskt relaterad till maskinens XY**, t.ex. via oberoende kända maskinmarkeringar eller en inmätt fixtur. Bara A4 utan relation till verktygsaxeln räcker inte för verktygsoffset.
- Ta bilder från flera kända maskin-XY/Z med stillastående Core och definierad fokusposition. Kontrollera kamerans verkliga fokusavstånd och bildfält när den levererats, särskilt vid låg Z. Autofokus får inte tyst ändra optiken under en kalibrerad mätserie.
- Kamera och fäste måste vara mekaniskt stela i förhållande till Core; fri passage från verktygsfästet, dammsko, probe/servoarm, kabelkedjor, anhåll och material vid högt/lågt Z. Ingen CAD-/kollisionsanalys eller realvärde för offset rapporteras som verifierad.
- Dokumentera mätta offset, kalibrerings-ID och fysisk montering när de finns. För noggrannhet krävs verifierat maskinläge; den befintliga *kontrollhomingen* upptäcker vissa tappade steg **efter etapp**, den är **inte encoderstyrning**.

## Fysiska nästa steg

1. Inventera Camera Module 3-standard eller Wide samt vilket beräkningskort och kabeldragning som ska användas (inget ytterligare inköp är här beslutat).
2. Provmontera kartongattrapp/3D-printat tillfälligt fäste och mät kameras möjliga avstånd till materialplan samt full verktygs-/dammsko-/probe-kollision.
3. Provpassa låg Y-list och trimreserve utan att låsa MPos eller skruvposition; granska överhäng/säker stödning för 2,4 m lång skiva.
4. Provframställ en plan A4-kalibreringstavla med uppmätt X/Y och registrering mot verktygsaxeln; samla stillbilder på ett känt plan och verifiera precisionen. Bygg inte full 3D-modell före mätbehov.
