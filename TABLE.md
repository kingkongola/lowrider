# Bord / underrede

Bordet ska inte behandlas som en eftertanke. Det är en del av maskinen, men vi ska inte överbygga det innan LowRider fungerar.

## Låst geometri

Byggmål: **650 × 1250 mm användbar arbetsyta** med de köpta 6,0 mm HaWiWe XZ-plattorna.

Aktuell V1E-kalkyl ger:
- minimum bord: **941 × 1563 mm**
- praktiskt mål för CNC-top/deck: cirka **1000 × 1620 mm**
- strut length: **819 mm**
- rör: **816 / 816 / 1505 mm**
- GT2-rem totalt: **4409 mm**, så 5 m räcker

Detaljer:
- `research/2026-08-29-geometry-650x1250.md`

## Ny huvudstrategi: begagnat 180×90/100 bord + avtagbar CNC-deck

**Det här är nu förstavalet.**

Sök ett fult men vridstyvt begagnat mat-/konferens-/kontorsbord ungefär:
- **1800×900 mm — mycket bra**
- **1800×1000 mm — idealiskt**
- 1600–1800 × 850–1000 mm kan fungera om underredet är bra

Vår praktiska CNC-top är ~1620×1000 mm.

På ett 1800×900-bord:
- CNC-decken sticker bara **50 mm ut per långsida**
- CNC-decken ligger **90 mm innanför varje kortände**

Det är därför inte nödvändigt att bygga ett eget möbelunderrede eller torsionsbord från början.

### Pareto-lager

```text
LR4 rails / belts
        |
removable ~1000 x 1620 CNC deck
        |
existing used 1800 x 900/1000 tabletop
        |
existing stiff table underframe
```

Bordets befintliga skiva gör huvuddelen av styvhetsjobbet. Den avtagbara CNC-decken skapar rätt maskinbredd/geometri och blir ett reversibelt gränssnitt.

Om befintlig bordsskiva är strukturellt bra:
- **11 mm OSB** räcker som billig screw-on CNC deck
- ~12 mm konstruktionsplywood är premiumalternativet

Deck ska **skruvas/bultas, inte limmas**.

Det är tillräcklig framtidsmodularitet: om plasma blir aktuellt senare kan hela router-toppen tas bort/bytas utan att vi bygger vattenbord/slats nu.

Detaljer och marknadsresearch:
- `research/2026-08-29-table-base-local-sourcing.md`

## Prisregler för begagnat

- **0–400 kr:** köp snabbt om mått + rackingtest passerar
- **400–700 kr:** normal Pareto-zon; ett bra 180×90/100 bord är ett bra köp
- **700–1000 kr:** endast om det är ett tydligt högkvalitativt kommersiellt konferensunderrede med perfekt geometri och noll glapp
- **>1000 kr:** normalt nej; vänta eller bygg bootstrap-fallback

Lokala Blocket-sökningar visar gott om bord i Gävle/Gävleborg, så det finns ingen anledning att betala möbelbutikspris för ett CNC-underrede.

Aktuella nyprisreferenser för 180×90 med MDF/stål ligger runt ~2100–2400 kr, medan ett kommersiellt 1800×1000 Kinnarps/Skandiform-konferensbord i Gävle ligger på absurda 14 200 kr. Vi behöver geometrin/styvheten, inte varumärket.

## Vad vi ska köpa

Prioritera:
- rektangulärt 175–190 cm långt
- 90–105 cm djupt
- ~70–76 cm högt
- stålrams-/konferensunderrede eller traditionellt stabilt träunderrede med sarg
- kosmetiskt slitage är positivt om det sänker priset
- bordsskiva ~20+ mm MDF/spån/laminat/solid wood är okej

Bra underredestyper:
- fyra ben + ordentlig sarg/tvärstag
- kommersiellt T-ben/konferensstativ med långsgående balk
- kraftigt traditionellt matbord med mekaniskt starka hörn

## Undvik

- glasskiva
- rangliga fällbord
- tunn hairpin-design utan sarg
- glappande utdrags-/förlängningsmekanism
- central enkel piedestal som vrider sig lätt
- pingisbordsmekanismer om de inte är nästan gratis och ovanligt stabila
- höj-/sänkbart elbord bara för funktionens skull

### Höj- och sänkbart skrivbord

Inte värt att aktivt söka.

Det ger ingen viktig CNC-funktion men tillför ofta:
- två glidande pelare
- mer möjlighet till sidoglapp
- endast 60–80 cm basdjup
- extra vikt/elektronik/kostnad

Ett stort kommersiellt elstativ är okej endast om det dyker upp löjligt billigt och är dokumenterat styvt.

## Femminutersprov före köp

1. Ta tag i ett hörn och skjut bordet i sidled. Det ska inte parallellogramma/racka synligt.
2. Tryck diagonalt mellan motsatta hörn. Inga klick/lösa fogar.
3. Sikta längs skivan. Liten båge går att hantera; grov twist är irriterande.
4. Kontrollera beninfästning/sarg/tvärbalk.
5. Mät faktisk längd och djup.
6. Titta under skivan efter enkla fästpunkter för CNC-deck och framtida hylla.
7. Ignorera repor och ful färg.

## Structural deck + spoilboard

Håll isär funktionerna:

1. **used table/top** — bulk stiffness/support
2. **removable ~1000×1620 CNC deck** — machine geometry/interface
3. **removable MDF spoilboard** — consumable cutting surface

### CNC deck

Prioritetsordning:
1. 11 mm OSB om bordsskivan under är stark
2. 12 mm konstruktionsplywood om merkostnaden är liten eller vi vill ha bättre skruvhållning

Ny deck behöver inte vara självbärande som ett ensamt bord; befintlig top stöttar den nästan helt. På 180×90-bord är bara 50 mm per sida utkragat.

### Spoilboard

Nuvarande Pareto-target är **cirka 12 mm MDF**, löstagbar.

Den behöver bara täcka arbetsområdet plus rimlig marginal, inte hela 1000×1620-decken. Arbetsantagande ~700×1300 mm tills stöd/fästpunkter är ritade.

## Permanenta strut plates

Bygg först på V1E:s printade temp-struts och låt LR4 fräsa sina permanenta struts.

För slutdelarna:
- 5–6 mm MDF förstaval
- hardboard okej
- max 6,35 mm
- inte 1/4" plywood enligt aktuella LR4-instruktioner
- köp helst offcut

Se:
- `research/2026-08-29-spoilboard-strut-plates.md`

## Mobilitet

**Låt inte hjul försena första spånet.**

Första version:
- fasta bordben/fötter
- shim/level vid behov

Om bordet faktiskt måste flyttas ofta efter att maskinen används:

### billigast men sämre slutstöd
- 4 bromsade länkhjul
- fungerar men maskinen står fortfarande på hjul

### bättre Pareto-hack
- fasta fötter bär maskinen vid fräsning
- två fasta hjul monteras på ena kortsidan några mm ovanför golvet
- lyft motsatt kortsida lite och rulla bordet som en skottkärra

Det ger mobilitet utan att hjulen är en del av precisionsstödet och kan göras billigt.

Köp ingen hjullösning innan det verkliga bordet är valt.

## DIY/bootstrap fallback om fynd uteblir

### Två arbetsbockar + ram/deck

Jula har stålbockar runt 149–199 kr/st. Två bockar + enkel 45×95-ram + skiva kan få maskinen igång billigt.

Men jämfört med ett begagnat 180×90-bord får vi:
- mer byggjobb
- ofta högre arbetshöjd
- sämre integrerad förvaring
- behov av diagonalstagning

Alltså fallback, inte förstaval.

Nya färdiga verkstadsbänkar är ännu sämre ekonomiskt: nuvarande 120×50/200×90-bänkar ligger ungefär 2000–3500 kr och passar ändå sämre än ett billigt gammalt konferens-/matbord.

## Damm som bordskrav

Bordet ska göra dammhanteringen lätt:
- plats under/bredvid för befintlig DeWalt + printad cyklon
- cyklon helst nära mitten av långsidan så befintlig 2,1 m slang kan räcka
- möjlighet till enkel slangbom/upphängning
- släta avtorkningsbara ytor
- möjlighet till transparent PVC/plastgardin runt smutszonen
- inga textilier som permanent dammreservoar
- gammalt FTX kan senare provas för sekundärt undertryck/filtrering, aldrig råspån

## Lokala söktermer

Sök inte bara på “CNC-bord”. Sök:
- matbord 180
- matbord 180x90
- konferensbord
- mötesbord
- kontorsbord
- skrivbord 180
- arbetsbord
- bord bortskänkes
- kontorsmöbler

Märke är nästan irrelevant. Geometri och vridstyvhet är allt.

## Nuvarande riktning

**Köp ett stabilt begagnat 180×90 eller 180×100 bord för helst ≤700 kr. Behåll dess befintliga skiva. Skruva en avtagbar ~1000×1620 OSB/ply CNC-deck ovanpå och använd separat löstagbar ~12 mm MDF-spoilboard. Bygg inte ett dedikerat underrede eller torsionsbox före första körningen.**

Referenser:
- `research/2026-08-29-table-base-local-sourcing.md`
- `research/2026-08-29-structural-center-cassette.md`
- `research/2026-08-29-spoilboard-strut-plates.md`
- https://docs.v1e.com/lowrider/
- https://forum.v1e.com/t/lowrider-v4-new-build-bootstrapped-torsion-box-table/53192
- https://forum.v1e.com/t/lowrider-v4/53926
- https://forum.v1e.com/t/ping-pong-table-lr4/54091
