# LowRider V4

Det här repot är bara för att få den köpta **LowRider V4** färdigbyggd och körklar.

## Syfte

Hålla reda på:
- vad som redan är köpt
- vad som saknas
- slutliga mått
- byggordning
- beslut som påverkar bygget
- fysisk integrationskontroll fram till första fungerande fräsning

## Aktuellt

- **LowRider V4 är slutligt vald.** PrintNC/IndyMill är inte längre aktiva maskinalternativ för detta bygge.
- HaWiWe-order med XZ-plattor, linjärskenor, skruvsats och Makita/Elaire 1/8"-spännhylsa är **betald**: 165,50 € inklusive 8,00 € frakt.
- Arbetsytan är **låst till 650 × 1250 mm användbart område** med köpta 6,0 mm HaWiWe XZ-plattor.
- Exakt LR4-geometri är verifierad: **816 / 816 / 1505 mm rör**, **819 mm strut-input**, **999 / 1705 / 1705 mm remsegment**, minimum bord **941 × 1563 mm**, praktisk CNC-deck cirka **1000 × 1620 mm**.
- Rörspåret är **Ø30×1,5 mm stål**, vilket innebär att alla dimensionsberoende LR4-printar ska vara **30 mm-varianten**.
- 3D-skrivaren är **Bambu Lab P1S, 256×256×256 mm byggvolym**. Den klarar V1E:s LR4-minimum; byggvolym/skew är därför inte en öppen projekt-gate. Kvar är endast rätt filvariant, slicer-preview och ett litet passningsprov innan hela satsen printas.
- Bordets huvudstrategi är ett styvt begagnat **160–180 × helst 90–100 cm** bord med befintlig skiva + avtagbar ~1000×1620 CNC-deck. På 90 cm djupa bord ska deckens cirka 50 mm långsidesöverhäng få verkligt stöd/infästning i LR4:s kantzon.
- Dammhantering är en del av grundbygget eftersom CNC:n delar garage med motorarbete.
- Garagegruppen är **10 A**. Om DeWalt verkligen är DXV30SAPTA blir nominell CNC-last ungefär 1050 + 800 + max 60 W = ~1,91 kW / ~8,3 A vid 230 V. Det ryms nominellt men lämnar liten marginal för andra laster och motorstart; faktisk grupp, övriga laster och uppstart testas innan drift.
- Elarkitekturen är fast KJD12/HDR-box + rörlig Jackpot3 på beam. Det gör **24 V-ledningen och routerkabeln till rörliga maskinkablar**; längd och dragavlastning avgörs med full-travel dry-fit.
- KJD12 behandlas som **NVR/maskinstopp med röd stoppkåpa**, inte som verifierad safety-rated E-stop.
- Laser är ett senare projekt, tidigast 2027. Plasma ingår inte i nuvarande scope.
- Målet är att få maskinen körklar i god tid före Halloween 2026.

## Filer

- [AUDIT.md](AUDIT.md) — oberoende system-/fysisk revision och bygg-gates
- [CHECKLIST.md](CHECKLIST.md) — det som återstår, i byggordning
- [BOM.md](BOM.md) — köpt / saknas / behöver verifieras
- [DECISIONS.md](DECISIONS.md) — endast beslut som påverkar detta bygge
- [BUILD_LOG.md](BUILD_LOG.md) — vad som faktiskt gjorts
- [SOURCING.md](SOURCING.md) — aktuella konkreta köpvägar
- [PROCUREMENT.md](PROCUREMENT.md) — aktuell order-/kundvagnsarkitektur och inköpsordning
- [TABLE.md](TABLE.md) — bords-/underredesarkitektur och köpgränser
- [research/](research/) — daterad evidens och historiska alternativ; kanoniska toppnivåfiler supersederar äldre research när de krockar

## Aktuell arbetsordning

1. Slutför checkout för den enda verkliga mekaniska orphan-delen: **3 × GT2 16T / 5 mm / 10 mm**.
2. Placera de redan produktlåsta orderna när checkout-totalerna håller: Motonet/LaskaKit/StepperOnline/DigiKey/VEVOR/Elecrow/SUNLU/Sorotec/KEDU.
3. Hitta och fysiskt kontrollera ett begagnat **160–180 × helst 90–100 cm** bord; köp helst ≤700 kr om racking- och kantstödstest passerar.
4. Printa senaste LR4-delarna i **30 mm-variant**, med Makita/65 mm tool mount, på P1S.
5. Bygg avtagbar CNC-deck + spoilboard och integrera damm/el/kabelrörelse.
6. Montera och gör gemensamt full-travel-test med slang + alla rörliga kablar innan slutlig kabelinfästning/remspänning.
7. Flasha Elecrow Jackpot3 med V1E:s aktuellt testade FluidNC + LR4-config, konfigurera, kalibrera och gör första riktiga fräsningen.
8. Före regelbunden körning: verifiera 10 A-gruppen med faktisk DeWalt/router/PSU-last och att inga andra relevanta laster på samma grupp orsakar överlast/nuisance trips.

Broad alternative research ska inte återöppna redan låsta komponenter utan ett konkret problem med pris, lager, kompatibilitet eller fysisk integration.