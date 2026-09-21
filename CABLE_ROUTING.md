# Kabeldragning och verkliga kabellängder — LowRider 4

**Status 2026-09-21: kaplängd ej verifierad.** För vår arbetsyta 650 × 1250 mm och Jackpot3 på YZ_Min finns **inget av V1E angivet exakt X-brytarkabelmått**. Tidigare förslag 250 cm var en oprövad uppskattning och har dragits tillbaka som kapinstruktion. Mata kabel från 10 m-rullen genom Core i LR-08 och fastställ faktisk längd i LR-16; om 250 cm redan är kapat, behåll biten och prova räckvidden innan vidare kapning.

## Vad finns och vad är faktiskt känt?

| Kabel/del | Köpt längd/antal | Användning eller status |
|---|---|---|
| 5 × STEPPERONLINE 17HS19-2004S1 | **1 m fast motorkabel per motor** | Y0, Y1, Z0, Z1, X. Ändra inte motorernas fasta kablar. |
| Tensility 30-00377 | **10 m 3×26 AWG** totalt | Fem normalt slutna brytare (COM + NC, två aktiva ledare per brytare; isolera oanvänd ledare). En sammanlagd längd, **inte 10 m per brytare**. Kontrollera flexibilitet i den rörliga slingan. |
| Molex KK 2,54 mm 2-polig pigtails | **3 × 150 mm** | Kontaktförsörjning enligt BOM; matchning mot fysisk Jackpot3-ingång och antal behöver verifieras, särskilt eftersom fem brytare används. |
| Tensility 30-00416 | **3 m 2×20 AWG** totalt | Tidigare tänkt lång 24 V-slinga. Efter D016 behövs bara en kort HDR→Jackpot3-förbindelse på balken. Validera kabelarea, anslutningssätt och verklig ström innan användning. |
| 230 V till HDR och KATSU | Inget slutligt ruttmått | Rörlig kabelväg och beröringsskydd/PE/dragavlastning verifieras separat innan nätanslutning. Ingen kapning eller inkoppling enbart med detta dokument. |

**V1E:** [LR4 Core Assembly](https://docs.v1e.com/lowrider/#core-assembly) anger minst **140 mm fri ledning för eventuell touchplate** vid Core. Det är **inte** ett mått för X-brytaren. [Wire Routing](https://docs.v1e.com/lowrider/#wire-routing) anger förlängningar på Core och YZ_Max-sidan, full Z- och X-rörelse samt dragavlastade skarvar, men **inte exakta kapmått för vår maskinstorlek**. V1E:s BOM har tre motorkabelförlängningar som typkonfiguration.

## Mätprotokoll – fylls efter fysisk provmontering, före kapning

| Ledning | Start → slut / faktisk väg | Köpt ledning | Mätt rutt inkl. rörelsemarginal | Slutlig längd | Funktion godkänd |
|---|---|---|---|---|---|
| X motor | Core → med Core till X_Max → avlastad mitt på balken → Jackpot3 YZ_Min | fast 1 m + ev. förlängning | — | — | ☐ |
| X NC | X-brytare → Cores tunnel → avlastad rörlig slinga via balkens mitt → Jackpot3 | mata från 10 m 3×26 AWG utan kapning vid LR-08 | prova fullt X-slag | ej fastställd | ☐ |
| Y0 motor | YZ_Min → kabelkanal → Jackpot3 | fast 1 m | — | — | ☐ |
| Y0 NC | YZ_Min-brytare → kabelkanal → Jackpot3 | ur 10 m 3×26 AWG | — | — | ☐ |
| Z0 motor | Z0 → YZ_Min-kanal → balk, med Z i full höjd → Jackpot3 | fast 1 m | — | — | ☐ |
| Z0 NC | Z0-brytare → samma Z-rörliga kanal → Jackpot3 | ur 10 m 3×26 AWG | — | — | ☐ |
| Y1 motor | YZ_Max → balk/stag → Jackpot3 YZ_Min | fast 1 m + ev. förlängning | — | — | ☐ |
| Y1 NC | YZ_Max-brytare → balk/stag → Jackpot3 | ur 10 m 3×26 AWG | — | — | ☐ |
| Z1 motor | Z1 → YZ_Max-kanal → balk/stag → Jackpot3 | fast 1 m + ev. förlängning | — | — | ☐ |
| Z1 NC | Z1-brytare → YZ_Max-kanal → balk/stag → Jackpot3 | ur 10 m 3×26 AWG | — | — | ☐ |
| HDR → Jackpot3 | Båda på balken, kort avlastad DC-rutt | ur 3 m 2×20 AWG endast om lämpad | — | — | ☐ |
| KATSU 230 V | Fast matning → hela Y-slaget → balk → hela X-slaget → fräs | befintlig fräskabel | — | — | ☐ |
| HDR 230 V | Fast NVR → hela Y-slaget → skyddad HDR-plint på balken | ännu inte valt | — | — | ☐ |
| Dammsugarslang | Dammuppsamling → avlastning → hela Y-/X-slaget → shoe | befintlig slang | — | — | ☐ |

**Praktisk ruttkontroll (projektmetod, inte V1E:s kapmått):**

1. **Vid LR-08 (Core):** mata en fri ände från rullen 3×26 AWG genom tunneln och märk `X`. Montera X-brytaren med **COM + NC** efter kontroll av faktisk kontakt och isolera oanvänd tredje ledare. **Kapa inte kabeln vid Core.** Låt den följa den kommande mjuka slingan till Jackpot3 på balken. Om 250 cm redan har kapats, behåll den biten och verifiera räckvidden. Valfri touchplate har en separat kabel med V1E:s minst 140 mm fri längd nära Core.
2. **Vid LR-09/10 (YZ):** dra Y- och Z-brytarkablarna genom avsedda kanaler innan hjul och skenor blockerar åtkomsten; märk `Y0/Z0` respektive `Y1/Z1`. Behåll sammanhängande längd/reserv. Prova Z genom hela slaget innan du fixerar ledningarna.
3. **Vid LR-13/16 (full maskin):** placera Jackpot3 på YZ_Min; lägg kablar längs riktig väg. Flytta Core till **X_Min och X_Max**, båda Z-sidorna till sina ytterlägen och balken genom **hela Y-slaget**. Lägg med fräskabel och slang i samma prov, och identifiera avlastade fixpunkter. Kabel ska vara fri även när maskinen går mot hörnen. V1E visar att X-ledningar går via Core och fästs ungefär mitt på balken.
4. **Mät och dokumentera varje ledning separat.** Lämna en mjuk service-/rörelsemarginal vid anslutningar och kopplingar – **cirka 10–15 cm kan vara en praktisk startpunkt, men är inte ett fast V1E-mått och måste anpassas efter rutt och böjradie.** För kort kabel eller stum förbindelse är inte godkänt. Fäst ledningar med avlastning före kontakt/skarv; motorförlängningar får inte bära draglast. Kablar som upprepat böjs måste vara avsedda för det.
5. **Kapning:** mät den faktiska kabelvägen vid monterad maskin, inklusive mjuk rörelseslinga och dragavlastning, **innan** X-brytarens ledning lossas från 10 m-rullen. Fördela sedan återstående kabel mellan de andra brytarna efter verklig routing, inte en antagen 7,5 m-rest. Överlängd kan förvaras dragavlastad på balken. Komplettera BOM endast vid faktiskt underskott.
6. **230 V:** bara planera mekanisk kabelväg i detta steg. Kabeltyp, PE, kapsling, dragavlastning, NVR och anslutning ska kontrolleras separat av elkunnig person. Den köpta lågspänningskabeln används inte för 230 V.

## Återrapport från LR-16

Skicka bilder på Jackpot3:s placering och kabelvägarna. Ange **vilken X-kabellängd som faktiskt räcker** genom fullt X-slag och om någon annan ledning är för kort eller behöver förlängning. Om 250 cm redan har kapats, ange om den biten fungerar. Överlängd får ligga dragavlastad.
