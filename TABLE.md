# Bord / underrede

Bordet är en del av maskinen, men ska inte överbyggas före första fungerande LR4.

## Låst geometri

Byggmål: **650 × 1250 mm användbar arbetsyta** med köpta 6,0 mm HaWiWe XZ-plattor.

Aktuell V1E-kalkyl ger:
- minimum bord: **941 × 1563 mm**
- praktisk CNC-top/deck: cirka **1000 × 1620 mm**
- strut: **819 mm**
- rör: **816 / 816 / 1505 mm**
- GT2 totalt: **4409 mm**, så 5 m räcker

Se `research/2026-08-29-geometry-650x1250.md`.

## Huvudstrategi: begagnat styvt bord + avtagbar CNC-deck

**180 cm längd är inte ett krav.** Det verkliga kravet kommer från minimum 1563 mm bordslängd och vår praktiska ~1620 mm deck.

Prioritera därför:
- **160×90 cm — fullt fungerande**; ~10 mm decköverhäng per kortände
- **170×90 cm — mycket bra**
- **180×90 cm — mycket bra och vanligt fyndmått**
- **160–180 × 90–100 cm — huvudspann**
- 85–105 cm djup kan fungera om underredet är bra

På 90 cm djup sticker ~1000 mm CNC-decken bara ut 50 mm per långsida.

```text
LR4 rails / belts
        |
removable ~1000 x 1620 CNC deck
        |
existing used tabletop
        |
existing stiff table underframe
```

Bordets befintliga skiva gör huvuddelen av styvhetsjobbet. CNC-decken skapar rätt geometri och ett reversibelt maskinlager.

### Deck

Om befintlig top är strukturellt bra:
- **11 mm OSB** är billig förstahandslösning
- ~12 mm konstruktionsplywood är premiumalternativ

Deck ska **skruvas/bultas, inte limmas**.

Separat löstagbar ~12 mm MDF används som spoilboard över själva arbetsområdet.

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
- enkel undersida att skruva/bulta CNC-deck och senare hylla i

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
6. Kontrollera undersidan för fästpunkter.
7. Ignorera repor och ful färg.

## Mobilitet

Låt inte hjul försena första spånet.

Första version:
- fasta ben/fötter
- shim/level vid behov

Om verklig användning visar behov senare är två fasta hjul några mm ovan golvet på ena kortsidan fortfarande favorit-hacket: lyft andra änden och rulla bordet som en skottkärra.

## Damm som bordskrav

Bordet ska ge:
- plats under/bredvid för befintlig DeWalt + printad cyklon
- möjlighet till slangbom/dragavlastning
- avtorkningsbara ytor
- möjlighet till enkel plastgardin runt CNC-zonen

## Nuvarande riktning

**Köp ett stabilt begagnat 160–180 × helst 90–100 cm bord för helst ≤700 kr. Behåll dess befintliga skiva. Skruva en avtagbar ~1000×1620 OSB/ply CNC-deck ovanpå och använd separat löstagbar ~12 mm MDF-spoilboard.**

180×90/100 är fortfarande ett bra fynd, men inte längre ett artificiellt sökkrav.

Referenser:
- `research/2026-08-29-table-base-local-sourcing.md`
- `research/2026-08-29-table-live-candidates.md`
- `research/2026-08-29-global-cart-optimization.md`
- https://docs.v1e.com/lowrider/
