# Bord / underrede

Bordet ska inte behandlas som en eftertanke. Det är en del av maskinen, men vi ska inte överbygga det innan LowRider fungerar.

## Krav

- dimensioneras först efter att slutlig LR4-arbetsyta är fryst i aktuell kalkylator
- nuvarande mål: ungefär **650 × 1250 mm arbetsyta**
- plant/styvt nog för trä, plywood, XPS och lätt aluminium
- lätt att dammsuga och våttorka eftersom samma garage används för motorarbete
- ska kunna flyttas undan praktiskt
- under skärning ska lasten stå på fasta/ställbara fötter, inte mjuka hjul
- dammslang/kablar ska kunna hängas utan att dra i gantry/Z
- mitten/spoilboarden bör vara utbytbar så bordet inte låser framtida användning
- plasma är **inte** ett nuvarande byggkrav, men en utbytbar mittsektion gör en framtida metall-/vattenbordsinsats möjlig utan att vi bygger för plasma nu

## Grundidé: underrede + CNC-kassett

Separera två funktioner:

1. **Underrede** — bär vikten, ger höjd, förvaring och mobilitet.
2. **CNC-kassett/top** — håller LR4:s exakta geometri, rails/belts och spoilboard.

Det gör att vi kan återanvända ett billigt begagnat bord/underrede utan att låta dess bordsskiva definiera CNC-precisionen.

Skiss:

```text
     permanent CNC-top / kassett
┌─────────────────────────────┐
│ LR4-sida / rail / belt      │
│ ┌─────────────────────────┐ │
│ │                         │ │
│ │   UTBYTBAR MITTSEKTION  │ │
│ │   + MDF spoilboard      │ │
│ │                         │ │
│ └─────────────────────────┘ │
│ LR4-sida / rail / belt      │
└─────────────────────────────┘
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

V1E visar att mycket enkla bord fungerar. Maskinen kan bootstrappas på sågbockar/2×4 och MDF/OSB och sedan fräsa delar till ett bättre bord.

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

## Spoilboard och utbytbar mitt

Håll isär:
- strukturell top/kassett
- **MDF-spoilboard**, som ska kunna planfräsas och bytas

MDF är lämpligt som spoilboard eftersom det är plant och lätt att plana. Det behöver inte betyda att hela bordet måste byggas av MDF.

Utbytbar mitt kan göras med exempelvis:
- skruvad bärskiva i plywood/OSB
- MDF-spoilboard ovanpå
- definierade referens-/stödpunkter i ytterramen

Detta gör även drop-table/tjocka arbetsstycken enklare senare.

## Damm som bordskrav

Bordet ska göra dammhanteringen lätt, inte svår:
- plats under eller bredvid för shop-vac + cyklon
- slanganslutning på en bestämd sida
- möjlighet till svängarm/slangbom ovanför
- släta/avtorkningsbara ytor nära CNC:n
- möjlighet till enkel transparent PVC-/plastgardin runt smutszonen
- inga onödiga tyg-/filtlösningar som blir permanenta dammreservoarer

## Referenser från V1E-communityn

- Bootstrap med gammalt pool-/pingisbord/köksbord eller sågbockar:
  https://forum.v1e.com/t/lowrider-v4-new-build-bootstrapped-torsion-box-table/53192
- Aktuell diskussion där shop-vac + cyklon rekommenderas och torsionsbox ses som bra men inte nödvändig:
  https://forum.v1e.com/t/lowrider-v4/53926
- Ping Pong Table LR4:
  https://forum.v1e.com/t/ping-pong-table-lr4/54091
- Rullbart LR4-bord:
  https://forum.v1e.com/t/making-my-small-lowrider-4-a-bigger-lowrider-4/52857
- V1E:s full-size table base, med förvaring och locking/folding wheel-tänk:
  https://forum.v1e.com/t/full-size-lowrider-table-base/51361

## Nuvarande riktning

**Sök först ett billigt/gratis stabilt begagnat matbords- eller konferensbordsunderrede. Bygg sedan en egen LR4-specifik top/kassett ovanpå.**

Bygg inte en avancerad torsionsbox före första körningen om vi inte hittar en mycket enkel/billig väg. Maskinen kan först köras på en enklare top och senare hjälpa till att bygga sin egen bättre top.

Exakt topmått och rör/rem-längder låses först efter LR4-kalkylatorn.
