# Sidotornet: print, montering, koppling och provkörning

**Källa till sanning för hur sensorenheten sitter ihop och sitter fast.** Framtagen 2026-11-11 genom simulering i CAD: varje skruv är kontrollerad med verktygets verkliga form i den ordning delarna monteras ([kontroll_montage.py](kontroll_montage.py), alla steg GODKÄND). **Inget är provat på riktiga delar.** Status och avbockning ägs av [CHECKLIST.md](../../../CHECKLIST.md); kopplingens pinnar av [KOPPLING_CORE_V0.md](KOPPLING_CORE_V0.md); stoppkedjan av [EL_BELYSNING_OCH_STOPP.md](../../EL_BELYSNING_OCH_STOPP.md).

## Så sitter allt fast

Principen: **ingenting i Core eller verktygsfästet ändras.** Tornet återanvänder V1E:s två M5-skruvar och är bara klämt mellan skallen och verktygsfästets öra. Allt inne i tornet skruvas i plasten med förborrade hål där skruven formar sin egen gänga (PETG tål det; samma metod genom hela tornet).

| Förband | Fästelement | Antal | Hur | Varför |
| --- | --- | --- | --- | --- |
| **Tornet → maskinen** | M5 insex (DIN 912), **befintlig längd + 16 mm**, smal bricka DIN 433 (Ø9) under skallen, medelstark gänglåsning (blå), **0,4–0,5 Nm med momentskruvmejsel**, märkfärgsstreck över skallen | 2 | Genom tornets platta och distans, verktygsfästets öra, in i Core som i dag. Den nedre nås genom kanalen Ø9,4 ovanför servot | Core sitter bakom örat; skallen är på tornets sida. Distansen sitter i örats försänkning, så formen håller läget och klämkraften kan vara låg: PETG kryper över ca 18 MPa; 0,8 Nm överskrider det när gänglåsningen sänker friktionen (`berakning_sidotorn.py`, granskning issue #2). Märkfärgen visar om en skruv vridit sig |
| Servot → tornet | M3 × 10, formar gänga i Ø2,6 | 4 | Framifrån genom öronen | Bakom ramen är det massivt; en mutter får inte plats (rättat 2026-11-11, var Ø3,4 frigångshål) |
| Stoppdelarna → ramen | M3 × 20, försänkt skalle | 4 | Efter servot, framifrån | Stoppen stod framför servot och hindrade det att sättas in (rättat 2026-11-11). Ett trasigt stopp printas om utan nytt torn |
| Armen + hornet → servoaxeln | **M3 × 10** i stället för servots mittskruv, genom armens botten (4,0 mm) och hornets fläns (1,7 mm) | 1 | Hornet i armens formficka, paketet på axeln, skruven utifrån (insex 2,5) | Fickan tar vridmomentet, skruven klämmer allt. Samma gängdjup som fabriksskruven (4,3 mm), kan inte bottna. Provas först för hand: går den inte lätt är axeln 4-40 |
| CR Touch → armen | M3 × 6 ur kitet, underifrån genom öronen (1,8 mm) in i armfoten | 2 | Skallen sitter i CR Touchens urtag vid kroppen, som Creality avsett | Ingen hylsa (beslut 2026-11-11): hylsan gick inte att montera |
| Magneten | Ø6 × 3 neodym, droppe cyanoakrylatlim | 1 | Bakifrån i parkeringsstoppet | Utan lim kan den dras ur mot armens stålskruv |
| Magnetens motpart | M3 stålskruv i armens bula | 1 | Skruvdjupet ställer hållkraften | Provas med vibration (fas 4) |
| Kameran + kameralocket | M3 × 10 genom lockets hål, skallen trycker lockets öra mot kortkanten | 2 | Underifrån; tornet av maskinen. Locket först, sedan skruvarna (insex 2,5) | Locket täcker kortet mot spån; bara objektivet syns (2026-11-11). M3 × 10 får 9 mm gänga. Kameran kan inte servas med tornet monterat |
| ADXL345 | M3 × 10 + printad bricka | 2 | Från panelsidan, innan Pi:n sitter | Styvt mot plattan vid övre M5, för att mäta fräsens vibration |
| Pi Zero 2 WH | Tappar (nedre hålen) + **M2.5 × 20 genom panelen** (övre hålen) | 2 | Skruvarna håller både Pi:n och panelen; sätet ger exakt djup | Rättat 2026-11-11: de gamla övre panelpelarna stod i Pi:ns väg |
| LM2596 A och B | Fickor + panelens fingrar | — | Skruvas inte | |
| Mikrofonen | Ram på panelen + ring av skumtejp | — | Ljudhålet tätat mot panelens hål | Annars hör den tornets inre |
| Kopplingskort | Hålkort ca 9 × 23 mm, VHB-tejp | 1 | Framväggen x 39–47, z 112–135 | Jordpunkt, servokontakt, kondensator |
| Sidopanelen | M3 × 8 i tornets pelare + de två M2.5 ovan | 4 + 2 | Utifrån | |
| Tornkabeln | Buntband runt bryggorna vid utgången | 2 | | Dragavlastning: ledarna i tornet får aldrig bära kabelns vikt |
| microSD-springan | Kaptontejp över springan | 1 | Utifrån | Håller kortet på plats mot vibration och stänger springan mot damm |
| CR Touch-kabeln vid navet | Fri ögla minst 40 mm, böjradie minst 15 mm, buntband på armen och vid skenan | 2 | | Kabeln förlängs ca 20 mm när armen vrids 150° (`berakning_sidotorn.py`) |
| LED-fästet | Befintliga M5/Brace i understruten | 2 per segment | | D022 |

**M5-längden:** skruva ur en av V1E:s skruvar och mät den. Ny längd = gammal + 16 mm (tornets platta och distans är 16,3 mm), avrundat till standardlängd så att muttern i Core får full gängning utan att skruven bottnar.

## Print (PETG, simulerat 2026-11-11)

| Platta | Fil | Tid | Vikt | Läge |
| --- | --- | --- | --- | --- |
| Tornet | `print/sidotorn-torn.json` | ca 5,6 h | 126 g | Upp och ned; ingen plan baksida finns. Stöd utanpå svepet, vid servoramen och delvis i elektronikrummet: plocka varsamt kring Pi-distanserna |
| Smådelar | `print/sidotorn-smadelar.json` | ca 1,6 h | 27 g | Panel yttersida ned, arm som ritad, 2 stoppdelar, 2 byglar (en reserv), 3 brickor, kameralocket |

PETG eftersom regulatorerna och Pi:n värmer upp det slutna tornet. **Printas först efter grind G2** (måtten från bänkproven införda). Exporten görs om då: `python sidotorn.py --ut UT && python utskrift_slutdelar.py --fran UT --ut print/sidotorn-slutdelar`.

## Montering i ordning

Ordningen följer av vad som skymmer vad. Tornet monteras komplett på bänken och sätts på maskinen sist.

1. **Rensa printen.** Stöd ut ur elektronikrummet, kamerafickan och M5-kanalen. Kontrollera att kanalen är fri hela vägen (en M5-skruv ska glida igenom).
2. **Löd allt som ska lödas, utanför tornet** (ledningslistan nedan): Pi:ns stift, ADXL, mikrofon, LM2596-modulerna, kopplingskortet. Krymp varje lödpunkt. Mät spänningarna på regulatorerna innan något kopplas till dem.
3. **Magneten** i den övre stoppdelens ficka med en droppe lim. Låt torka.
4. **Kameran** med CSI-kabeln redan i kameran. Lägg tornet upp och ned på bänken, så ligger kortet kvar på tapparna av egen tyngd. Lägg **kameralocket** rakt på (öronen in i skruvhålen, objektivet genom mitthålet) och skruva två M3 × 10 genom lockets hål. För upp kabeln i CSI-rummet och vik den två gånger 45°.
5. **ADXL** med två M3 × 10 och brickor från panelsidan.
6. **Kopplingskortet** på framväggen.
7. **LM2596 A och B** i fickorna.
8. **Pi:n**: CSI-kabeln i Pi:ns kontakt först, sedan rakt in på tapparna. **Inget microSD-kort i** ännu.
9. **Servot** in framifrån genom ramen, fyra M3 × 10. **Kabeln kommer ut ur servons kortsida närmast axeln** (uppmätt 2026-11-12: tätning 10 mm bred och 3,5 mm utstickande, 2,6 mm från ryggen; kabel 4 mm bred; kontakt 14 × 7,8 × 2,8 mm). Tätningen glider i ett band i sidoväggen, öppet mot fronten, så servon går in med kabeln på. **Lägg sedan in kabeln genom slitsen på panelsidan** (på högkant, den lägger sig platt i kanalen) upp i elektronikrummet; kontakten läggs direkt i rummet och träs aldrig genom kanalen (den kan inte vrida sig runt hörnet, granskning 2026-11-13). Vidare till kopplingskortet. Kabeln är minst ca 200 mm (användaren 2026-11-13); ca 100 behövs, överskottet viks ihop i rummet.
9b. **Stoppdelarna** mot ramens framsida, två M3 × 20 var. Magneten är redan limmad i den övre.
10. **Ändlägena (fas 4.8 i checklistan):** hornet i armens ficka, paketet på axeln så att armen står mitt i rörelsen vid 1500 µs, sedan M3 × 10 genom armen. CR Touch med kitets två M3 × 6 underifrån; kabeln i armens spår.
11. **Panelen**: mikrofonens ledningar med en servicebåge, fyra M3 × 8 och två M2.5 × 20. Inget skramlar.
12. **microSD** in utifrån genom springan i bakväggen. Ett kort som ska bytas dras ut med en pincett.
13. **På maskinen, armen utfälld:** den övre M5 rakt utifrån, den nedre genom kanalen. Bricka, blå gänglåsning, 0,4–0,5 Nm med momentskruvmejsel; plasten får inte tryckas ihop.
14. **Tornkabeln** ut bakåt, buntband vid bryggorna, sedan längs X-vägen till balken enligt [CABLE_ROUTING.md](../../../CABLE_ROUTING.md).

## Miljökrav: värme och damm

**Värme:** luften i tornet högst 50 °C vid 35 °C i garaget; Pi:ns processor under 80 °C (där den börjar strypa). Beräkning: ca 48 °C vid toppeffekt 4 W ([berakning_sidotorn.py](berakning_sidotorn.py)). Verifieras med en timmes körning där `vcgencmd measure_temp` loggas.

**Damm:** inga öppningar mot fräsen. Panelens slitsar vänder bort från fräsen (X max-sidan), kabelutgången och SD-springan vetter mot Core; springan tejpas. Mikrofonen har dammnät. CR Touchens stift är ute bara vid mätning, och proben sitter parkerad högt när fräsen går (ingen hylsa, beslut 2026-11-11); självtest före varje mätning. **Linsen** sticker ut 2,6 mm och har inget glas framför: armspärren stoppar om bilden blir oskarp (smuts), och linsen rengörs med blåsbälg, inte trasa. Verifieras med ett dammprov under fräsning.

## Kopplingskortet

Hålkort ca 9 × 23 mm, 2,54 mm delning, VHB-tejp på framväggen. Uppifrån och ned: 3-polig stiftlist för servot (signal, +6 V, GND), kondensator 470–1000 µF/10 V liggande, fem lödpunkter för CR Touch-kabeln, en jordskena längs ena långsidan som enda jordpunkt. Ledningslistan nedan säger vad som går till varje punkt.

## Kabelväg ut ur tornet

Tornkabeln följer X-motorns kabel till balkens mitt (CABLE_ROUTING.md); längd = X-motorkabelns + 0,3 m. Böjradie minst 10 × kabelns diameter i rörliga delar. Kontrolleras med snöre och full X-rörelse (fas 5.3) och med ett cykelprov.

## Ledningslista inne i tornet

Längder = rak väg i CAD + 30 %. Kapa längre hellre än kortare. Alla skarvar lödda och krympta; inga instickskontakter utom vid servot och CR Touchen, så att de kan bytas.

| Från | Till | Ledare | Längd ca |
| --- | --- | --- | --- |
| Tornkabel 1, +24 V övervakning | LM2596 A IN+ | 1 | 75 mm |
| Tornkabel 2, +24 V maskin | LM2596 B IN+ | 1 | 105 mm |
| Tornkabel 3, GND | Kopplingskortets jordpunkt; därifrån A IN−, B IN−, Pi GND (stift 6) | 4 | 65 mm |
| LM2596 A OUT+ (5,1 V) | Pi stift 2 | 1 | 45 mm |
| Pi stift 4 (5,1 V) | Kopplingskortet → CR Touch +5 V | 1 | 55 mm |
| LM2596 B OUT+ (6 V) | Kopplingskortet: servokontaktens +, kondensator 470–1000 µF | 1 | 30 mm |
| Tornkabel 4, servosignal | Kopplingskortet: servokontaktens signal | 1 | 65 mm |
| Servot (egen kabel) | Kopplingskortet, 3-polig stiftlist | — | ca 100 mm av servots kabel |
| CR Touch (kitets kabel, kapas) | Kopplingskortet: +5 V, GND, styrning (tornkabel 5), kontakt (tornkabel 6), kontaktjord (tornkabel 7) | 5 | ca 90 mm i tornet |
| Pi stift 1, 9, 19, 21, 23, 24 | ADXL: VCC, GND, SDA (MOSI), SDO (MISO), SCL, CS | 6 | 55 mm |
| Pi stift 12, 17, 34, 35, 38 + L/R | INMP441: SCK, VDD, GND, WS, SD; L/R till GND på kortet | 5 | **120 mm** (panelen ska kunna öppnas) |
| Pi stift 16, 22, 20 | Tornkabel 8, 9, 10 (OK-puls, startknapp, jord) | 3 | 75 mm |

Ledare: 0,25 mm² (AWG 24) flertrådig för matning, 0,14 mm² (AWG 26) räcker för signaler. Kopplingskortet är **enda** jordpunkten i tornet, så att servots strömstötar inte går genom Pi:ns jord.

## Provkörning (stegvis strömsättning)

Varför stegvis: ett fel ska bara kunna skada en del, och du ska veta vilken.

1. **Tornet på bänken, ingen last:** 24 V in på tornkabel 1 och 2 från en labbkälla eller nätdelen. Mät 5,1 V och 6,0 V på kopplingskortet. Strömmen utan last under 30 mA.
2. **Pi:n startar** (inget annat inkopplat än det lödda): `/status` svarar, `throttled=0x0`.
3. **Kamera, ADXL, mikrofon:** `/bild.jpg`, `/adxl?s=2`, `/ljud?s=2` enligt `cnc/pi/README.md`.
4. **Servot med ESP32:n** på signalledaren: ändlägen, magneten, servot släpper utan puls.
5. **CR Touch med ESP32:n:** ut, in, självtest, kontaktsignal.
6. **Stopplådan på 24 V** enligt bänkprovet i el-underlaget, innan 230 V.
7. **På maskinen, fräsen avstängd:** full rörelse i X, Y och Z; kabeln får inte sträckas.
8. **Jackpot:** konfigförslaget och makrona ([probstyrning](../../probstyrning/README.md)), `arm_ut`, `arm_in`, `?` med stiftet intryckt.
9. **Armspärren** lär sig båda lägena; täckt lins ger stopp.
10. **Stoppkedjan på riktigt:** grön knapp → KATSU kan startas; `POST /stopp` → KATSU stannar och Jackpot larmar; nödstopp → samma; dra ur Pi:ns matning → samma.
11. **Mätning på spill** (fas 7 i checklistan).

## Fynd från simuleringen 2026-11-11 (rättade i CAD)

| Fynd | Följd om det inte rättats | Rättning |
| --- | --- | --- |
| Den nedre M5-skallen gömd bakom servokåpan | Tornet gick inte att skruva fast | Rak verktygskanal Ø9 ovanför servot |
| Servots skruvhål Ø3,4 utan plats för mutter | Servot hade suttit löst | Förborrade Ø2,6 för M3 |
| microSD-kortet pekade in i bakväggen | Pi:n gick inte att sätta i med kort | Springa i bakväggen; kortet byts utifrån |
| Övre panelpelarna i Pi:ns väg | Pi:n gick inte att sätta i | Pi:n skruvas med M2.5 genom panelen; pelarna borta |
| Buntbandsbryggorna över ADXL-skruven | Skruven gick inte att nå | Bryggorna kortade |
| Ingen plats för skarvar och jordpunkt | Lösa skarvar i tornet | Kopplingskort på framväggen |
