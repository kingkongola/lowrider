# Bord / underrede

Bordet är en del av maskinen, men ska inte överbyggas före första fungerande LR4.

## Låst geometri

Byggmål: **650 × 1250 mm användbar arbetsyta** med köpta 6,0 mm HaWiWe XZ-plattor.

Aktuell V1E-kalkyl ger:
- minimum ytterfootprint: **941 × 1563 mm**
- strut-input: **819 mm**
- rör: **816 / 816 / 1505 mm**
- GT2 totalt: **4409 mm**, så 5 m räcker

Se `research/2026-08-29-geometry-650x1250.md`.

## Huvudstrategi: rejält begagnat bord, ingen full extra deck som baseline

**Ett styvt begagnat bord med frisk skiva används direkt som maskinens strukturella bas.** En separat ~1000×1620 OSB/ply-deck är inte längre baseline och ska inte köpas automatiskt.

Detta ligger i linje med praktisk V1E-community-praxis: en vanlig robust bordsskiva/workbench kan vara själva underlaget och en spoilboard läggs ovanpå arbetsområdet. En separat torsionsbox/deck är en premiumlösning när bordet i sig inte är tillräckligt plant/styvt eller när särskild geometri krävs.

Prioritera:
- **180×90 cm — huvudmål och vanligt fyndmått**
- **180×100 cm — ännu enklare eftersom full bredd ryms direkt**
- **160–180 × 90–100 cm — fungerar om längd och kantzon löses**

### Viktig detalj för 180×90

Vår kalkylerade minimum-bredd är **941 mm**. Ett 900 mm djupt bord saknar alltså cirka **41 mm totalt** i bredd, inte 100 mm.

Lös detta med **smal lokal kantbreddning/rail-support**, ungefär 20–25 mm per långsida om symmetrisk layout passar, eller asymmetriskt efter faktisk LR4-layout. Det ska göras först när bordet och maskindelarna finns fysiskt.

```text
LR4 rail / wheels / belt clips
        |
smal lokal kantbreddning där 900 mm bord inte räcker
        |
befintlig styv bordsskiva = strukturell maskinbas
        |
löstagbar MDF-spoilboard endast över arbetszonen
```

Poängen är att **inte** lägga en hel extra OSB-skiva ovanpå ett redan bra bord bara för att vinna 41 mm bredd.

## Spoilboard

Separat löstagbar ~12 mm MDF används som spoilboard över arbetszonen.

Spoilboarden:
- skyddar bordsskivan när fräsen går igenom materialet
- kan planfräsas och bytas när den är utsliten
- behöver inte täcka hela bordsskivan
- ska inte bära LR4:s rail/belt-struktur

## När behövs ändå separat deck?

Inför endast separat deck/torsionsbox om det verkliga bordet visar sig:
- ha för vek eller skev skiva
- sakna säker infästning för rail/belt-zoner
- vara olämpligt att modifiera
- behöva en avtagbar maskinmodul av andra praktiska skäl

Det är då en lösning på ett verifierat problem, inte ett standardköp.

## Prisregler för bord

- **0–400 kr:** köp snabbt om mått + rackingtest passerar
- **400–700 kr:** normal Pareto-zon
- **700–1000 kr:** endast tydligt högkvalitativt/styvt kommersiellt underrede
- **>1000 kr:** normalt nej

## Vad vi söker

Prioritera:
- rektangulärt **180×90 cm** i första hand
- 180×100 cm är jackpot
- ~70–76 cm högt
- fyra ben + ordentlig sarg/tvärstag, eller kommersiellt T-ben med långsgående balk
- strukturellt frisk top; kosmetiskt slitage är irrelevant
- enkel undersida för lokal kantbreddning, kabel/slang och eventuell hylla

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
6. Kontrollera undersidan för lokal rail-/kantstödsinfästning.
7. Ignorera repor och ful färg.

## Efter köp — innan rail/belt clips monteras

1. Markera V1E:s exakta **941 × 1563 mm** ytterfootprint relativt bordsskivan.
2. Kontrollera var rail/wheel/belt-zonerna hamnar på det faktiska bordet.
3. På 900 mm djup: bygg bara den lokala breddning som behövs för att nå korrekt och styvt stöd.
4. Montera spoilboard över arbetszonen.
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

**Köp ett rejält begagnat 180×90 cm bord för helst ≤700 kr och använd dess befintliga skiva direkt som maskinbas. Lös endast den cirka 41 mm totala breddbristen med smal lokal kantbreddning efter dry-fit. Lägg en separat löstagbar ~12 mm MDF-spoilboard över arbetsområdet. Köp ingen hel OSB/ply-deck om det inte uppstår ett konkret behov.**

Referenser:
- `AUDIT.md`
- `research/2026-08-29-table-base-local-sourcing.md`
- `research/2026-08-29-table-live-candidates.md`
- `research/2026-08-29-global-cart-optimization.md`
- https://docs.v1e.com/lowrider/
- V1E forum: LowRider V4 bootstrapping/table discussions
