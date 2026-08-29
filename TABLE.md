# Bord / underrede

Bordet är en del av maskinen, men ska inte överbyggas före första fungerande LR4.

## Låst geometri

Byggmål: **650 × 1250 mm användbar arbetsyta** med köpta 6,0 mm HaWiWe XZ-plattor.

Aktuell V1E-kalkyl ger:
- minimum bord: **941 × 1563 mm**
- praktisk CNC-top/deck: cirka **1000 × 1620 mm**
- strut-input: **819 mm**
- rör: **816 / 816 / 1505 mm**
- GT2 totalt: **4409 mm**, så 5 m räcker

Se `research/2026-08-29-geometry-650x1250.md`.

## Huvudstrategi: begagnat styvt bord + avtagbar CNC-deck

**180 cm längd är inte ett krav.** Det verkliga kravet kommer från minimum 1563 mm bordslängd och vår praktiska ~1620 mm deck.

Prioritera därför:
- **160×90 cm — fungerar**, om edge-support-testet nedan passerar
- **170×90 cm — mycket bra**
- **180×90 cm — mycket bra och vanligt fyndmått**
- **160–180 × 90–100 cm — huvudspann**
- 85–105 cm djup kan fungera om underredet/decken ger korrekt kantstöd

På 90 cm djup sticker ~1000 mm CNC-decken ut cirka 50 mm per långsida. Det är geometriskt okej men **inte bara kosmetiskt överhäng**: V1E:s Y-rail/belt clips använder ytterkanten som referens och maskinen belastar samma kantzon.

```text
LR4 rail / wheels / belt clips
        |
removable ~1000 x 1620 CNC deck
        |
existing used tabletop + local edge support as needed
        |
existing stiff table underframe
```

Bordets befintliga skiva gör huvuddelen av styvhetsjobbet. CNC-decken skapar rätt geometri och ett reversibelt maskinlager.

## Fysisk regel för 90 cm-bord

Om ett 1000 mm deck överhänger ett 900 mm bord ungefär 50 mm per långsida:

- rail-/wheel-/belt-clip-zonen får inte ligga på en lös fjädrande OSB-kant
- tryck hårt nedåt i hela maskinens långkantsspår: ingen synlig lokal flex som ändrar rail/wheel-höjd
- belt/Y-clips måste få säker infästning; 11 mm OSB ensam i fri kant ska inte antas räcka för upprepad belastning
- lägg vid behov underliggande trälist/blockning, bredare stöd eller genomgående bultning mot den befintliga bordsskivan/underredet
- gör den slutliga kantdetaljen först när det faktiska begagnade bordet finns

Detta gör **180×90 fortfarande till ett mycket bra köp**; vi tar bara bort antagandet att 50 mm överhäng automatiskt är strukturellt färdigt.

### Deck

Om befintlig top är strukturellt bra:
- **11 mm OSB** är billig förstahandslösning
- ~12 mm konstruktionsplywood är premiumalternativ

Deck ska **skruvas/bultas, inte limmas**.

Separat löstagbar ~12 mm MDF används som spoilboard över arbetszonen. Spoilboard ska inte bära rail/belt-strukturen.

## Prisregler

- **0–400 kr:** köp snabbt om mått + rackingtest passerar
- **400–700 kr:** normal Pareto-zon
- **700–1000 kr:** endast tydligt högkvalitativt/styvt kommersiellt underrede
- **>1000 kr:** normalt nej

## Vad vi söker

Prioritera:
- rektangulärt **160–180 cm långt**
- helst **90–100 cm djupt**
- ~70–76 cm högt
- fyra ben + ordentlig sarg/tvärstag, eller kommersiellt T-ben med långsgående balk
- strukturellt frisk top; kosmetiskt slitage är irrelevant
- enkel undersida att skruva/bulta CNC-deck och eventuell kantblockning/hylla i

Undvik:
- glasskiva
- rangliga fällbord
- hairpin-ben utan sarg
- glappande utdragsmekanism
- enkel central piedestal med vridglapp
- höj-/sänkbart elbord bara för funktionens skull

## Femminutersprov före köp

1. Skjut ett hörn hårt i sidled — inget synligt parallellogram/racking.
2. Tryck diagonalt mellan motsatta hörn — inga klick/lösa fogar.
3. Sikta längs skivan — liten båge okej, grov twist dålig.
4. Kontrollera beninfästning/sarg/tvärbalk.
5. Mät faktisk L×D×H.
6. Kontrollera undersidan för deck- och kantstödsinfästning.
7. Ignorera repor och ful färg.

## Efter köp — innan rail/belt clips monteras

1. Lägg/provskruva decken.
2. Markera V1E:s exakta 941 × 1563 mm ytterfootprint på decken.
3. Kontrollera att båda långsidornas rail/wheel/belt-zoner har fast stöd.
4. Lägg lokal blockning om decken fjädrar eller skruvinfästningen annars bara hamnar i tunn fri kant.
5. Kontrollera att KJD12-box, DeWalt/cyklon och kabel-/slangväg kan placeras utan att maskinens rörelseområde blockeras.

## Mobilitet

Låt inte hjul försena första spånet.

Första version:
- fasta ben/fötter
- shim/level vid behov

Om verklig användning visar behov senare är två fasta hjul några mm ovan golvet på ena kortsidan fortfarande favorit-hacket: lyft andra änden och rulla bordet som en skottkärra.

## Damm och el som bordskrav

Bordet ska ge:
- plats under/bredvid för befintlig DeWalt + printad cyklon
- möjlighet till slangbom/dragavlastning
- plats för fast KJD12/HDR-box där stoppet är direkt nåbart från normal operatörsplats
- kabelväg från fast box till rörlig beam utan skarpa kanter/snags
- avtorkningsbara ytor
- möjlighet till enkel plastgardin runt CNC-zonen

## Nuvarande riktning

**Köp ett stabilt begagnat 160–180 × helst 90–100 cm bord för helst ≤700 kr. Behåll dess befintliga skiva. Skruva en avtagbar ~1000×1620 OSB/ply CNC-deck ovanpå, med lokal kantblockning där verklig konstruktion kräver det, och använd separat löstagbar ~12 mm MDF-spoilboard.**

180×90/100 är fortfarande ett mycket bra fynd, men inte ett artificiellt sökkrav.

Referenser:
- `AUDIT.md`
- `research/2026-08-29-table-base-local-sourcing.md`
- `research/2026-08-29-table-live-candidates.md`
- `research/2026-08-29-global-cart-optimization.md`
- https://docs.v1e.com/lowrider/