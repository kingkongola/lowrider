# Kabeldragning och verkliga kabellängder — LowRider 4

**Status 2026-09-21: måttprotokoll, inte en verifierad kaplista.** Mått avser vårt bygge: arbetsyta 650 × 1250 mm, två X-rör 816 mm, Y-rör 1505 mm, Jackpot3 på balken vid YZ_Min. **Inga individuella kaplängder har mätts fysiskt.** Ange aldrig siffror som om de vore verifierade innan LR-16 är genomförd.

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
| X NC | X-brytare → Cores tunnel → samma rörliga rutt → Jackpot3 | ur 10 m 3×26 AWG | — | — | ☐ |
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

1. **Vid LR-08 (Core):** trä X-brytarens 3-ledarkabel genom Core medan brytaränden fortfarande är tillgänglig; märk `X`. **Kapa inte till slutlängd**, och krimpa inte den slutliga kortkontakten innan Core kan nå båda X-ändarna. Montera ingen touchplate i grundbygget om den inte används.
2. **Vid LR-09/10 (YZ):** dra Y- och Z-brytarkablarna genom avsedda kanaler innan hjul och skenor blockerar åtkomsten; märk `Y0/Z0` respektive `Y1/Z1`. Behåll sammanhängande längd/reserv. Prova Z genom hela slaget innan du fixerar ledningarna.
3. **Vid LR-13/16 (full maskin):** placera Jackpot3 på YZ_Min; lägg kablar längs riktig väg. Flytta Core till **X_Min och X_Max**, båda Z-sidorna till sina ytterlägen och balken genom **hela Y-slaget**. Lägg med fräskabel och slang i samma prov, och identifiera avlastade fixpunkter. Kabel ska vara fri även när maskinen går mot hörnen. V1E visar att X-ledningar går via Core och fästs ungefär mitt på balken.
4. **Mät och dokumentera varje ledning separat.** Lämna en mjuk service-/rörelsemarginal vid anslutningar och kopplingar – **cirka 10–15 cm kan vara en praktisk startpunkt, men är inte ett fast V1E-mått och måste anpassas efter rutt och böjradie.** För kort kabel eller stum förbindelse är inte godkänt. Fäst ledningar med avlastning före kontakt/skarv; motorförlängningar får inte bära draglast. Kablar som upprepat böjs måste vara avsedda för det.
5. **Först efter godkänt rörelseprov:** bestäm faktiskt kapmått för var och en av de fem NC-brytarkablarna och eventuella kompatibla motorförlängningarna. Mät total åtgång av 10 m-rullen **innan första biten kapas**. Om det inte räcker: uppdatera BOM och komplettera, inte skarva godtyckligt i rörlig del.
6. **230 V:** bara planera mekanisk kabelväg i detta steg. Kabeltyp, PE, kapsling, dragavlastning, NVR och anslutning ska kontrolleras separat av elkunnig person. Den köpta lågspänningskabeln används inte för 230 V.

## Återrapport från LR-16

Skicka bild på Jackpot3:s placering, en översikt av varje kabelväg och tabell med **mätt ruttlängd** för alla fem motorer och fem brytare. Ange X/Z/Y-extremernas frigång och vilka förlängningar som faktiskt behövs. Då kan de tomma slutlängdsfälten fastställas och SSOT uppdateras utan gissningar.
