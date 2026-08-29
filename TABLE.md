# Bord / underrede

Bordet ska inte behandlas som en eftertanke. Det är en del av maskinen, men vi ska inte överbygga det innan LowRider fungerar.

## Låst/nästan låst geometri

Nuvarande byggmål är **650 × 1250 mm användbar arbetsyta** med de köpta 6,0 mm HaWiWe XZ-plattorna.

Aktuell V1E-kalkyl ger:
- minimum bord: **941 × 1563 mm**
- praktiskt mål för CNC-kassett/top: cirka **1000 × 1620 mm**
- strut length: **819 mm**
- rör: **816 / 816 / 1505 mm**
- GT2-rem totalt: **4409 mm**, så 5 m räcker

Detaljer och formler:
- `research/2026-08-29-geometry-650x1250.md`

## Krav

- plant/styvt nog för trä, plywood, XPS och lätt aluminium
- lätt att dammsuga och våttorka eftersom samma garage används för motorarbete
- ska kunna flyttas undan praktiskt
- under skärning ska lasten stå på fasta/ställbara fötter, inte mjuka hjul
- dammslang/kablar ska kunna hängas utan att dra i gantry/Z
- mitten/spoilboarden ska vara utbytbar så bordet inte låser framtida användning
- plasma är **inte** ett nuvarande byggkrav, men en utbytbar mittsektion gör en framtida metall-/vattenbordsinsats möjlig utan att vi bygger för plasma nu

## Grundidé: underrede + CNC-kassett

Separera två funktioner:

1. **Underrede** — bär vikten, ger höjd, förvaring och mobilitet.
2. **CNC-kassett/top** — håller LR4:s exakta geometri, rails/belts och den utbytbara mitten.

Det gör att vi kan återanvända ett billigt begagnat bord/underrede utan att låta dess bordsskiva definiera CNC-precisionen.

Skiss:

```text
     permanent CNC-top / kassett ~1000×1620
┌────────────────────────────────────┐
│ permanent LR4 rail/belt structure  │
│  ┌──────────────────────────────┐  │
│  │ removable structural center │  │
│  │ + removable 12 mm MDF       │  │
│  │   spoilboard                │  │
│  └──────────────────────────────┘  │
│ permanent LR4 rail/belt structure  │
└────────────────────────────────────┘
                  ↓
        stabilt underrede / ben
```

Den permanenta ytterramen håller maskingeometrin. Mittdelen är förbruknings-/funktionsyta.

## Alternativ

### A. Begagnat konferens-/matbordsunderrede + egen CNC-top

**Nuvarande favorit.**

Bra typstorlek är ungefär 160–180 cm långt och 80–100 cm brett. Ett tungt metallunderrede kan vara nästan gratis jämfört med att bygga en möbel från nytt virke.

Fördelar:
- mycket mindre byggjobb
- ofta stabilare ben/stålram än billigt DIY-underrede
- kan kompletteras med vår egen exakt dimensionerade CNC-top
- hyllor för dammsugare/cyklon/controller kan byggas under senare

Kontrollera före köp:
- glapp i ben/fogar
- diagonal styvhet
- faktisk fri bredd mellan ben
- om underredet klarar en top som eventuellt överhänger några cm
- total höjd efter CNC-top
- om befintlig bordsskiva är styv nog att återanvända som structural deck

### B. Pingisbord

**Bevisligen möjligt men inte förstahandsval.** Det finns aktuella LR4-byggen på pingisbord och V1E-communityn nämner uttryckligen gamla pingisbord som en bootstrap-lösning.

Nackdelar för vårt bygge:
- ett fullstort pingisbord är cirka 2,74 × 1,525 m och därmed mycket större än vår planerade maskin
- tunna pingisbordsskivor kan vara skeva/warpy
- fällbara underreden kan ha mer glapp än vi vill ha
- tar onödigt garageutrymme

Intressant om:
- ett fås gratis/nästan gratis
- underredet är riktigt bra
- bordet kan kapas/återanvändas snarare än användas intakt

### C. Egen enkel ram + skivor

Bra om inget vettigt begagnat dyker upp.

V1E visar att mycket enkla bord fungerar. Maskinen kan bootstrappas på sågbockar/2×4 och skiva och sedan fräsa delar till ett bättre bord.

Fördelar:
- exakt rätt yttermått
- lätt att bygga för hjul/fötter/förvaring
- billigt om material finns hemma

Nackdel:
- nytt virke/skivmaterial blir snabbt dyrare än ett begagnat stabilt underrede
- risk att lägga mycket tid på bordet innan CNC:n ens kör

### D. Torsionsbox

Tekniskt bästa träbaserade topplösningen om vi senare vill maximera planhet/styvhet.

V1E-communityn rekommenderar ofta torsionsbox men säger samtidigt att den **inte behövs för att komma igång**. En vanlig väg är att starta enkelt och låta LR4 fräsa sitt eget slutliga torsionsbord.

För vår relativt lilla maskin kan en tunn/lätt torsionskassett bli attraktiv efter driftsättning.

## Mobilitet

Föredragen princip:
- fyra riktiga fasta/ställbara fötter bär bordet vid fräsning
- hjul används bara för transport

Bra lösningar:
- infällbara arbetsbänkshjul som lyfts ned med fotpedal
- separat hjulram som avlastas när maskinen ställs på fötter
- låsbara hjul endast som budgetstart; inte ideal som slutligt precisionsstöd

V1E-byggare rapporterar att rullbara LR4-bord är mycket praktiska för att komma åt baksidan och flytta maskinen undan.

## Structural deck + spoilboard + utbytbar mitt

Håll isär tre funktioner:

1. **outer cassette/frame** — håller rails/belts i rätt relation
2. **structural center deck** — bär arbetsstycket
3. **MDF-spoilboard** — förbrukningsyta som planfräses och byts

### Structural deck: köp inget innan underredet är valt

Prioritetsordning:

1. **Återanvänd befintlig bordsskiva** om den är tillräckligt styv. Kostnad 0 kr.
2. **11 mm OSB** är värdefallback om ny skiva behövs; färsk svensk referens ~239 kr för 1197×2500.
3. **12 mm konstruktionsplywood** är premiumsteget; ~399 kr för 1200×2500, bättre skruvhållning och trevligare vid upprepad demontering.

Se:
- `research/2026-08-29-structural-center-cassette.md`

### Spoilboard: löstagbar ~12 mm MDF

Nuvarande Pareto-target är **cirka 12 mm MDF** över den strukturella mitten.

Skälen:
- tillräckligt med material för planfräsning och skruvfastsättning
- billigare/lättare än 18–19 mm
- strukturen ska komma från lagret under, inte från spoilboarden
- enkelt att byta när den är slut

Den behöver bara täcka arbetsområdet plus rimlig marginal, inte hela 1000×1620-kassetten. Storleksordning **~700×1300 mm** är ett arbetsantagande; slutmåttet tas först när ytterram och stöd är ritade.

### Permanenta strut plates

Bygg först på V1E:s fyra printade temp-struts och låt sedan LR4 fräsa sina egna permanenta struts.

För slutdelarna:
- 5–6 mm MDF förstaval
- hardboard är okej
- max 6,35 mm
- **inte 1/4" plywood** enligt aktuella LR4-instruktioner
- köp helst offcut; full 6 mm MDF-skiva kostar omkring 395–473 kr och är onödig endast för två smala 819 mm-delar

Se:
- `research/2026-08-29-spoilboard-strut-plates.md`

## Damm som bordskrav

Bordet ska göra dammhanteringen lätt, inte svår:
- plats under eller bredvid för befintlig DeWalt + printad cyklon
- slanganslutning på en bestämd sida
- möjlighet till svängarm/slangbom ovanför
- släta/avtorkningsbara ytor nära CNC:n
- möjlighet till enkel transparent PVC-/plastgardin runt smutszonen
- inga onödiga tyg-/filtlösningar som blir permanenta dammreservoarer
- gamla FTX-aggregatet kan senare utvärderas för sekundärt undertryck/luftfiltrering, aldrig råspån

## Referenser från V1E-communityn

- Aktuell LR4-dokumentation och bootstrap med temp-struts:
  https://docs.v1e.com/lowrider/
- Bootstrap med gammalt pool-/pingisbord/köksbord eller sågbockar:
  https://forum.v1e.com/t/lowrider-v4-new-build-bootstrapped-torsion-box-table/53192
- Aktuell diskussion där enkla bord och MDF-spoilboard diskuteras:
  https://forum.v1e.com/t/lowrider-v4/53926
- Ping Pong Table LR4:
  https://forum.v1e.com/t/ping-pong-table-lr4/54091
- Rullbart LR4-bord:
  https://forum.v1e.com/t/making-my-small-lowrider-4-a-bigger-lowrider-4/52857
- V1E:s full-size table base, med förvaring och locking/folding wheel-tänk:
  https://forum.v1e.com/t/full-size-lowrider-table-base/51361

## Nuvarande riktning

**Sök först ett billigt/gratis stabilt begagnat matbords- eller konferensbordsunderrede. Återanvänd dess top om den är strukturellt bra; bygg annars billig OSB/plywood-center. Lägg en separat löstagbar ~12 mm MDF-spoilboard ovanpå.**

Bygg inte en avancerad torsionsbox före första körningen. LR4 är uttryckligen byggd för att kunna bootstrapas och sedan förbättra sina egna delar.
