# LowRider V4

Det här repot är bara för att få den köpta **LowRider V4** färdigbyggd och körklar.

## Syfte

Hålla reda på:
- vad som redan är köpt
- vad som saknas
- slutliga mått
- byggordning
- beslut som påverkar bygget
- avbockning fram till första fungerande fräsning

## Aktuellt

- **LowRider V4 är slutligt vald.** PrintNC/IndyMill är inte längre aktiva maskinalternativ för detta bygge.
- HaWiWe-order med XZ-plattor, linjärskenor, skruvsats och Makita/Elaire 1/8"-spännhylsa är **betald**: 165,50 € inklusive 8,00 € frakt.
- Arbetsytan är nu **låst till 650 × 1250 mm användbart område** med köpta 6,0 mm HaWiWe XZ-plattor.
- Exakt LR4-geometri är dokumenterad: **816 / 816 / 1505 mm rör**, **819 mm struts**, **999 / 1705 / 1705 mm remsegment**, minimum bord **941 × 1563 mm**, praktisk CNC-deck cirka **1000 × 1620 mm**.
- Bordets huvudstrategi är ett styvt begagnat **180×90/100 cm** bord med befintlig skiva + avtagbar ~1000×1620 CNC-deck. Ingen torsionsbox eller specialbyggt underrede före första körningen.
- Dammhantering är en del av grundbygget eftersom CNC:n delar garage med motorarbete.
- Laser är ett senare projekt, tidigast 2027. Plasma ingår inte i nuvarande scope.
- Målet är att få maskinen körklar i god tid före Halloween 2026.

## Filer

- [CHECKLIST.md](CHECKLIST.md) — det som återstår, i byggordning
- [BOM.md](BOM.md) — köpt / saknas / behöver verifieras
- [DECISIONS.md](DECISIONS.md) — endast beslut som påverkar detta bygge
- [BUILD_LOG.md](BUILD_LOG.md) — vad som faktiskt gjorts
- [SOURCING.md](SOURCING.md) — aktuella konkreta köpvägar
- [PROCUREMENT.md](PROCUREMENT.md) — aktuell order-/kundvagnsarkitektur och inköpsordning
- [TABLE.md](TABLE.md) — bords-/underredesarkitektur och köpgränser
- [research/](research/) — daterad evidens och historiska alternativ; nyare research supersederar äldre när de krockar

## Aktuell arbetsordning

1. Slutför live checkout för små orphan-delar: 16T-remhjul och 608-2RS.
2. Placera de redan produktlåsta orderna när checkout-totalerna håller: Motonet/LaskaKit/StepperOnline/DigiKey/VEVOR/Elecrow/SUNLU/Sorotec.
3. Hitta och fysiskt kontrollera ett begagnat 180×90/100-bord; köp helst ≤700 kr om rackingtestet passerar.
4. Börja printa rätt LR4-delar i vanlig styv PLA.
5. Bygg avtagbar CNC-deck + spoilboard och integrera dammhantering.
6. Montera, konfigurera, kalibrera och göra första riktiga fräsningen.

Broad alternative research ska inte återöppna redan låsta komponenter utan ett konkret problem med pris, lager eller kompatibilitet.