# El, belysning och övervakningsstopp — arbetsläge 2026-11-10

**Status:** SSOT för nya elkraft- och LED-krav på den faktiska LowRider V4. Detta är ett planeringsunderlag, **inte** ett godkänt 230 V-kopplingsschema, en säkerhetsklassad stoppkrets eller en färdig CAD/montering. Elektrisk detaljprojektering och fysisk verifiering återstår. Låsta D013/D016/D020/D021 i `DECISIONS.md` gäller där de är relevanta. Mjukvarans övervaknings- och stoppolicy ägs av [cnc/verktygsovervakning](https://github.com/kingkongola/cnc/blob/main/docs/verktygsovervakning.md).

## Verifierat, valt och osäkert — blanda inte ihop

| Del | Fakta/status | Anmärkning |
| --- | --- | --- |
| Fräs | KATSU 101750, 220–240 V AC, 710 W; köpt | Egen nätlast, inget 24 V-tillbehör |
| Maskinmatning | Mean Well HDR-60-24, 24 V DC/2,5 A/**60 W**; köpt/mottaget | Till Jackpot3 + fem stegmotorer. Ingen reserverad LED-effekt kan antas utan mätning |
| LED | **BRIMETI COB, 5 m, 24 V, 4000 K, 320 LED/m, vald för 145 kr enligt användaren** | Angiven effekt **10 W/m**, angivet utbyte **100 lm/W**, dvs ungefär **1 000 lm/m**. Säljaruppgifter, ej uppmätta; CRI och faktisk stripbredd ska verifieras på den mottagna varan. Faktisk debitering och mottagning ej verifierade |
| Ursprunglig RGB-list | 12 V, ca 10 m, Tuya, 12 V/1 A-adapter | Vid maximalt rött mätte användaren 12,2 V vid matning och 8,6 V längst bort; stora längdförluster och otillräckligt arbetsljus. Inte vald till CNC |
| Altec Lansing | Äldre **17 V**-aggregat | Användaren har redan klippt kabeln; inte valt som CNC-försörjning |
| Laptopladdare | Användaren har en märkt ca **150 W**, misstänkt 20 V | Utspänning, effekt och kontakt måste läsas på exakt exemplar. Möjlig separat Pi-försörjning via 20→5,1 V, om verifierad |
| Elsparkcykelladdare | Användaren tror sig ha en laddare märkt "24 V" | Output ej känd. En 24 V nominell batteriladdare kan lämna högre spänning; inte vald innan etikett har kontrollerats |
| Regulatorer | **10 × LM2596** köpta enligt BOM | Buck/sänkande, **inte** boost; verklig termisk kontinuerlig kapacitet ska verifieras |
| Pi/kamera | Pi Zero 2 WH + Camera Module 3 Standard beställda | Pi behöver stabil reglerad ca 5,1 V med korrekt marginal; kameran matas via Pi |
| Servo/prob | Spektrum SPMS664 ca 6,0–7,4 V; BLTouch/CR Touch-prob avses 5 V | Exakt probvariant och 5 V-/signalkoppling ska identifieras. Servot ska ha egen 6 V-regulator och inte störa Pi |

## Geometriskt krav — tre COB-remsor under X-balken

**Användarens riktning:** **en remsa lodrätt nedåt, två riktade framåt** (i Y-led relativt maskinen). Denna asymmetri är avsiktlig; byt inte mot ”en fram, en bak” utan nytt beslut. Riktningen är bestämd men **exakta gradtal och fästens koordinater är inte bestämda**.

- Börja med testvinklar `0°`, `+25°`, `+50°` från lodlinjen, **endast för prov**, så att två främre remsor inte belyser precis samma zon. Fastställ verkliga vinklar efter prov av kamera och arbetsyta. Kontrollera att ”framåt” är entydigt i CAD-koordinaterna.
- Maskinens X-rör är 816 mm; faktisk nyttjbar fästräcka på strut, skruvpositioner och hinder måste **mätas**, inte antas vara 816 mm. Tre remsor på exempelvis 0,8 m vardera skulle bli cirka **2,4 m/24 W**, inte hela rullens 50 W.
- **Äldre tryckta fästen är inte 3-vägsfästen för denna geometri.** Doug Josephs skruvade klips håller platta 24 V COB-lister mot undersidan; Jonathan Jones har underbalkshållare; Jason Yeager har separat framåtvinklat kanalclips. Inga av dem är verifierade för `0°/+25°/+50°`, vår strut eller Brimeti-bredd. Kalla dem referenser, **inte printklar lösning**.
- **Föredragen konstruktion att testa:** tre korta aluminiumprofiler/-band som leder bort LED-värme, fixerade med utbytbara 3D-printade vinkelhållare som använder befintliga strutskruvar om möjligt. Separera aluminiumets kylning från plastens bärfunktion; limma inte 10 W/m direkt mot PLA/PETG. Kontrollera materialtemperatur, diffusering, åtkomst och spånexponering.
- **Fysiska grindar före STL för drift:** mät faktisk COB-bredd och kapsteg, strutplattans geometri/tjocklek och skruvlägen; kontrollera rör, Core/kamera, servoarm, dammsko och full X/Y/Z-rörelse. Gör en liten provbit/klips och jämför skugga/reflexer i kamerabilder innan alla fästen printas.
- **Forumreferenser:** [Doug Josephs raka klips](https://forum.v1e.com/t/design8studios-lowrider-4-cnc-upgrading-full-size-lr3-lr4/45723/64), [Jonathan Jones LR4-hållare](https://forum.v1e.com/t/new-lr4-build-in-catalunya/48215/131), [Jason Yeagers vinklade LED-kanal](https://forum.v1e.com/t/fluidnc-led-musings/46566/135).

## Kraftdomäner och stopp — principer, inte kopplingsorder

1. **Maskin:** befintlig Mean Well 24 V/60 W matar Jackpot3/stegmotorer; KATSU är separat 230 V-last. Fysiskt nåbar maskinstopp-/NVR-kedja med manuell återställning enligt D013 ska finnas och verifieras oberoende av Wi-Fi/Pi/smartrelä.
2. **Övervakning:** Pi/kamera ska vara **på en matning som ligger utanför maskinstoppets brytna gren**, så att den kan fortsätta observera, logga och signalera efter automatiskt/fysiskt stopp. Det äldre schemat `machine/delar/sensorer/KOPPLING_CORE_V0.md` visar Pi på maskinens 24 V och är **inte giltigt som matningsbeslut** för detta nya krav. Oberoende matning betyder inte batteribackup vid totalt nätavbrott.
3. **Automatisk extraskyddsfunktion:** användarens önskemål är att avvikelse från bild/ljud/vibration ska kunna leda till **automatisk frånkoppling av KATSU och maskin från huset**, exempelvis via Shelly som komplement till fysiskt maskinstopp. Varken reläval, elinstallation, motorlastdimensionering, bekräftad frånkoppling, watchdog/heartbeat, återställningssekvens eller sensorpolicyn är färdig. En Wi-Fi-/Pi-begäran får inte förväxlas med oberoende säkerhetsklassat nödstopp.
4. **LED:** matar man hela rullen blir den uppgivna lasten 50 W vid 24 V (ca 2,1 A). Om bara tre ca 0,8 m-längder används blir det cirka 24 W. Välj aggregat **efter faktisk klipplängd**. Testa återanvändning av elsparkcykel-/laptopmatning först efter utspänningsverifiering. **Inget extra aggregat eller boost är beslutat/köpt.**
5. **Servo/prob:** separata reglerade matningar med korrekt referens till Jackpot. Risk för oavsiktlig bakmatning från övervakningens matning till avstängd Jackpot/prob måste undersökas. Raspberry Pi får inte kopplas direkt till 24 V. Regulatorer, förgrening, säkringar, signaljord och stör/immunitetskrav dimensioneras och provas innan inkoppling.
6. **Stoppbeteende:** hård strömbrytning kan låta Z falla medan KATSU varvar ned. Mät och riskbedöm fall/eftergång; ingen automatisk återstart, och fräsbyte kräver fysisk frånkoppling. Sensorförlust och felstopp ska vara synliga för användaren. Fjärrövervakning gör inte obevakad fräsning säker i sig.

## Närmast återstående arbete

- Kontrollera faktisk Brimeti-profilbredd och den verkliga X-strutens underkant och skruvar.
- Gör 3D-montageutkast med **riktning ned/fram/fram**, provvinklar justerbara; en provklips först, sedan belysnings-/kameratest.
- Läs outputmärkning på befintlig 24 V-kandidat och 150 W-laddare; mät/bedöm effekt innan köp av boost/PSU.
- Specificera separat övervakningsmatning, två stoppvägar, förväntat stoppbeteende, kabelskydd och återstartsspärr. Samordna med `cnc/docs/verktygsovervakning.md`; ändra inte aktiv FluidNC.

**Öppet:** ingen elkoppling, CAD-vinkel eller inköpslista är genom detta dokument godkänd för drift.
