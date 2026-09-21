# Arbetsordrar — LowRider 4

**Version 2026-09-21.** Delbara kvällspass på cirka 45–60 minuter. Ordning och beroenden är vägledning; välj ett pass vars förutsättningar finns. **Status i denna fil är inte automatisk:** allt är initialt *ej verifierat*, även om användaren kan ha börjat med något. Rapportera faktisk status innan vi markerar en order klar. Remhjulen är mottagna 2026-09-21; de ska ändå kontrolleras fysiskt i LR-02.

**Så använder vi systemet:** välj `LR-xx`, utför arbetet, skicka tillbaka ID + `klar | delvis | blockerad` + faktiska mått/foton/avvikelser. Jag granskar och uppdaterar `WORK_ORDERS.md`, `CHECKLIST.md` och `BUILD_LOG.md` vid behov efter din rapport. Webbsidans lokala markeringar skickas inte automatiskt hit. Tider är uppskattningar, inte tidskrav. Om det behövs mer tid, avbryt vid ett säkert mellanläge och dela upp arbetet.

**Säkerhet:** använd originalmanualen för rätt monteringsriktning. 230 V-planen måste verifieras av kompetent person före anslutning; gör ingen nätspänningsinstallation bara utifrån en arbetsorder. Fräsen ska vara urkopplad vid mekanik- och motorprov. Dokumentet ersätter inte [BOM](BOM.md), [DECISIONS](DECISIONS.md) eller [AUDIT](AUDIT.md). [Illustrerad guide](https://kingkongola.github.io/lowrider/) · [V1E original](https://docs.v1e.com/lowrider/).

## Översikt

| ID | Arbetsorder | Tid | Förutsättningar | Status i SSOT |
|---|---|---:|---|---|
| LR-01 | Sortera 3D-utskrifterna | 60 min | Inga | Ej verifierad |
| LR-02 | Inventera alla mekanikpaket | 60 min | Inga | Ej verifierad |
| LR-03 | Mät rören – kapa inte än | 45 min | Inga | Ej verifierad |
| LR-04 | Kontrollera bordets styvhet | 60 min | Inga | Ej verifierad |
| LR-05 | Provlägg maskinen på bordet | 60 min | LR-04 | Ej verifierad |
| LR-06 | Kapa och grada stålrören | 60 min | LR-03 | Ej verifierad |
| LR-07 | Core: lager och verktygsfäste | 60 min | LR-01, LR-02 | Ej verifierad |
| LR-08 | Core: motor, brytare och idlers | 60 min | LR-07 | Ej verifierad |
| LR-09 | Montera YZ_Min | 60 min | LR-01, LR-02 | Ej verifierad |
| LR-10 | Montera YZ_Max | 60 min | LR-01, LR-02 | Ej verifierad |
| LR-11 | Färdigställ Z och bakhjulen | 60 min | LR-09, LR-10 | Ej verifierad |
| LR-12 | Bygg balk med temporära stag | 60 min | LR-01, LR-06 | Ej verifierad |
| LR-13 | Förena balk, Core och YZ | 60 min | LR-08, LR-11, LR-12 | Ej verifierad |
| LR-14 | Slutplacera remhållare och Y-skena | 60 min | LR-05, LR-13 | Ej verifierad |
| LR-15 | Trä och spänn tre remmar | 60 min | LR-14 | Ej verifierad |
| LR-16 | Planera kablar, slang och elplacering | 60 min | LR-13 | Ej verifierad |
| LR-17 | Bygg dammskons mekaniska del | 60 min | LR-01 | Ej verifierad |
| LR-18 | Planera cyklon och uppsamlingskärl | 60 min | Inga | Ej verifierad |
| LR-19 | Jackpot3: installation och konfiguration | 60 min | LR-02 | Ej verifierad |
| LR-20 | Koppla och prova fem brytare | 60 min | LR-19, LR-16 | Ej verifierad |
| LR-21 | Första försiktiga motorprov | 60 min | LR-15, LR-19, LR-20 | Ej verifierad |
| LR-22 | Kontrollera 230 V-upplägg och maskinstopp | 60 min | LR-16 | Ej verifierad |
| LR-23 | Torrkör hela rörelseområdet | 60 min | LR-21, LR-22, LR-16 | Ej verifierad |
| LR-24 | Gör CAM för första provskärningen | 60 min | LR-23, LR-17 | Ej verifierad |
| LR-25 | Första lilla skärprovet | 60 min | LR-24, LR-18 | Ej verifierad |
| LR-26 | Generera permanenta stagplattor | 60 min | LR-25 | Ej verifierad |
| LR-27 | Fräs permanenta stagplattor | 60 min | LR-26 | Ej verifierad |
| LR-28 | Byt till permanenta stag | 60 min | LR-27 | Ej verifierad |
| LR-29 | Planfräs offerskivan | 60 min | LR-28 | Ej verifierad |
| LR-30 | Slutkalibrera och säkerhetskopiera | 60 min | LR-28, LR-29 | Ej verifierad |

## Arbetskort

### LR-01 — Sortera 3D-utskrifterna

**Tid:** cirka 60 min · **Fas:** Förberedelser · **Beroenden:** Inga · **Status:** ej verifierad

**Ta fram:** De utskrivna delarna från samtliga plattor, manualen, märkpenna och lådor.

1. Lägg ut utskrifterna och sortera i Core, YZ_Min, YZ_Max, balk, bord/remmar, damm och Jackpot3-box.
2. Kontrollera mot manualens deltabell att rätt 30 mm-rörvarianter och Makita/65 mm-fäste finns.
3. Räkna fyra temporära stag (Temp Strut, avsett 15 % infill); bedöm hål, bryggor och delarna från den förskjutna utskriften.
4. Fotografera grupperna och skriv en kort lista över saknade eller tveksamma delar.

**Godkänt när:** Delarna är identifierade; alla osäkra delar är noterade, inte förutsatta godkända.

**Återrapportera:** Antal Temp Strut, saknade/tveksamma delar och foton.

**Bildguide:** [Svenska manualen, kapitel 1](https://kingkongola.github.io/lowrider/#0).

### LR-02 — Inventera alla mekanikpaket

**Tid:** cirka 60 min · **Fas:** Förberedelser · **Beroenden:** Inga · **Status:** ej verifierad

**Ta fram:** HaWiWe, LaskaKit, DigiKey, eBay-remhjul och BOM.

1. Kontrollera HaWiWe: två XZ-plattor, fyra MGN12H 150 mm, skruvsats och Elaire-hylsa.
2. Räkna 608-lager (16 köpta), sex idlers, fem motorer och T8 400 mm med kopplingar och mässingsmuttrar.
3. Kontrollera de tre mottagna 16T-remhjulen: 16 tänder, 5 mm hål, passning för 10 mm GT2-rem. Fotografera närbild och märkning.
4. Inventera Omron-brytare, Jackpot3, HDR-60-24 och kabeldelar; skriv en avvikelselista utan att köpa dubbelt.

**Godkänt när:** En fysisk avprickning mot BOM. Oklara mått och antal står som ej verifierade.

**Återrapportera:** Foton på remhjul, uppmätt hål/tandantal samt avvikelser från BOM.

**Bildguide:** [Svenska manualen, kapitel 1](https://kingkongola.github.io/lowrider/#0).

### LR-03 — Mät rören – kapa inte än

**Tid:** cirka 45 min · **Fas:** Förberedelser · **Beroenden:** Inga · **Status:** ej verifierad

**Ta fram:** Båda Motonet-rören, skjutmått, måttband, rak kant och märkpenna.

1. Mät ytterdiameter på flera ställen i två riktningar per rör.
2. Kontrollera synlig krokighet genom att rulla mot plant underlag och granska ytan.
3. Mät faktisk användbar längd och markera hypotetiska kap på 1505 respektive 816 + 816 mm.
4. Rapportera måtten och vänta med kapning vid osäker passning eller rakhet.

**Godkänt när:** OD, rakhet, verkliga längder och kapplan dokumenterade.

**Återrapportera:** OD-intervall, uppmätt längd, rakhet och foto på kapmarkeringar.

**Bildguide:** [Svenska manualen, kapitel 1](https://kingkongola.github.io/lowrider/#0).

### LR-04 — Kontrollera bordets styvhet

**Tid:** cirka 60 min · **Fas:** Förberedelser · **Beroenden:** Inga · **Status:** ej verifierad

**Ta fram:** Köpt bordsskiva 180 × 100 cm, befintligt underrede, måttband och rätkant.

1. Kontrollera ben, sarg, tvärstag och infästningar. Tryck på varje hörn och notera eventuell vridning eller glapp.
2. Mät bordshöjd och planhet i flera riktningar; dokumentera den största observerade avvikelsen.
3. Fotografera undersidan och visa var Y-styrskena och remhållare kan skruvas.
4. Om underredet är instabilt: identifiera exakt vad som behöver åtgärdas innan du bygger om.

**Godkänt när:** Antingen godkänt för provlayout eller blockerat med en konkret åtgärdslista.

**Återrapportera:** Bilder, bordshöjd, planhetsavvikelse och eventuellt glapp.

**Bildguide:** [Svenska manualen, kapitel 1](https://kingkongola.github.io/lowrider/#0).

### LR-05 — Provlägg maskinen på bordet

**Tid:** cirka 60 min · **Fas:** Förberedelser · **Beroenden:** LR-04 · **Status:** ej verifierad

**Ta fram:** Bord, tejp, måttband och Y-styrskenans/remhållarnas printade delar.

1. Markera preliminär ytterfootprint 941 × 1563 mm på 1000 × 1800 mm-skivan.
2. Välj sida för maskinens enda Y-styrskena; märk båda remsträckorna och Y_Min/Y_Max.
3. Provlägg clips och remhållare; kontrollera kantmarginaler och underredets skruvzoner.
4. Fotografera layout och notera faktiska marginaler. Borra inte förrän monterad maskin provpassats.

**Godkänt när:** Dokumenterad och mätbar provlayout utan permanenta hål.

**Återrapportera:** Översiktsfoto, fyra kantmarginaler och eventuella konflikter.

**Bildguide:** [Svenska manualen, kapitel 6](https://kingkongola.github.io/lowrider/#5).

### LR-06 — Kapa och grada stålrören

**Tid:** cirka 60 min · **Fas:** Mekanik · **Beroenden:** LR-03 · **Status:** ej verifierad

**Ta fram:** Verifierade rör, kapverktyg, gradare/fil, måttband och skyddsglasögon.

1. Kontrollmät samtliga kapmarkeringar och spänn röret utan att deformera det.
2. Kapa 1505 mm samt två längder 816 mm enligt verifierad kapplan.
3. Grada utsida och insida och avlägsna metallspån.
4. Mät färdiga längder och kontrollera rakheten igen.

**Godkänt när:** Tre raka rör med dokumenterade faktiska längder och släta ändar.

**Återrapportera:** Slutmått för alla tre rör och foto på ändarna.

**Bildguide:** [Svenska manualen, kapitel 4](https://kingkongola.github.io/lowrider/#3).

### LR-07 — Core: lager och verktygsfäste

**Tid:** cirka 60 min · **Fas:** Mekanik · **Beroenden:** LR-01, LR-02 · **Status:** ej verifierad

**Ta fram:** 1 × printad Core; **8 × 608-2RS (DigiKey)**; **8 × M8×40 sexkantsskruvar + 8 × M8 nyloc (HaWiWe)**; 4 × M5 nyloc + 4 tillhörande M5-fästskruvar ur HaWiWe (M5×30 finns i satsen, provpassa mot verkligt fäste); 4 korta bitar PLA-filament; rätt printat Makita/65 mm-fäste; lämplig nyckel för M8 samt skruvverktyg.

1. Sortera ut de 8 lagren (inte alla 16 köpta), 8 M8×40 och 8 M8 nyloc. Lägg fram i fyra par om 2. Kontrollera att varje 608-lager rullar fritt före montering. V1E-bilder: `ca.jpg`, `cb.jpg`, `cc.jpg`, `cd.jpg`.
2. Montera först **6 lager med 6 M8×40 + 6 M8 nyloc** i tre par enligt `ca`–`cc`; för varje skruv genom lagrets innerhål åt exakt den riktning bilden visar, och dra bara an utan att klämma lagret. Montera sista **2 lager + 2 M8×40 + 2 M8 nyloc** enligt `cd`; lämna just dessa två övre spännskruvar lösa tills Core sitter på rören.
3. Ta fram **4 M5 nyloc, 4 korta filamentbitar och 4 fästskruvar M5** ur HaWiWe-satsen. Sätt muttrarna med nylondelen åt rätt håll enligt `cf`–`ch`, lås med filament och klipp jäms. Montera printat Makita/65 mm-fäste enligt `ci`–`cj`; provpassa skruvlängden (M5×30 finns i satsen, exakt längd visas inte uttryckligen i originaltexten) och dra jämnt utan att spräcka plasten.
4. Slutkontroll: räkna 8 monterade lager + 8 M8×40 + 8 M8-låsmuttrar, och 4 infångade M5-låsmuttrar med korrekt fäste. De första 6 lageraxlarna ska sitta an, de sista 2 vara lösa; alla lager ska snurra utan nyper. Fotografera Core från båda håll.

**Godkänt när:** Exakt 8 lager, 8 M8×40, 8 M8 nyloc, 4 M5 nyloc och rätt Makita/65 mm-fäste monterade. Sex lageraxlar endast åtdragna till anliggning; två övre spännskruvar kvar lösa. Lager snurrar fritt och fästskruvar har kontrollerad längd.

**Återrapportera:** Bekräfta antal 8/8/8 + 4 M5 och verklig skruvlängd till verktygsfästet. Skicka två foton på Core, gärna ett av `cd`-paret. Ange om någon ficka, passning eller lagerrörelse är tveksam.

**Bildguide:** [Svenska manualen, kapitel 2](https://kingkongola.github.io/lowrider/#1).

### LR-08 — Core: motor, brytare och idlers

**Tid:** cirka 60 min · **Fas:** Mekanik · **Beroenden:** LR-07 · **Status:** ej verifierad

**Ta fram:** X-motor, ett verifierat 16T-remhjul, X-brytare, kabel, idlers och skruvar.

1. Dra och märk X-brytarkabeln enligt originalbilderna; montera brytaren försiktigt.
2. Rikta 16T-remhjulet med Cores inbyggda guide. Dra stoppskruven mot axelns plana sida först.
3. Montera motorn och förbered X-remmen utan att kapa på chans.
4. Montera idlers så att de roterar mycket fritt; fotografera monteringen.

**Godkänt när:** Core komplett nog för balken; remhjul i linje och brytarkabel märkt.

**Återrapportera:** Foton på remhjul och brytare; fria idlers; kvarvarande avvikelser.

**Bildguide:** [Svenska manualen, kapitel 2](https://kingkongola.github.io/lowrider/#1).

### LR-09 — Montera YZ_Min

**Tid:** cirka 60 min · **Fas:** Mekanik · **Beroenden:** LR-01, LR-02 · **Status:** ej verifierad

**Ta fram:** YZ_Min, tillhörande XZ-platta, två MGN12, Y-/Z-motor, brytare och hjul.

1. Märk Y0- och Z0-kablar enligt maskinens faktiska orientering.
2. Montera Z-brytare, Y-motor med verifierat 16T-remhjul och främre hjul enligt bilderna.
3. Montera Y-brytare med rätt armriktning; skydda armen mot bänkkanten.
4. Rengör rälsbäddarna, montera skenor och XZ-platta löst och prova glidningen under stegvis åtdragning.

**Godkänt när:** Min-sidans skenor och vagn rör sig lätt; eventuellt kvarvarande Z-/bakhjulsarbete tydligt noterat.

**Återrapportera:** Foton på orientering, fri rörelse och vad som inte hanns med.

**Bildguide:** [Svenska manualen, kapitel 3](https://kingkongola.github.io/lowrider/#2).

### LR-10 — Montera YZ_Max

**Tid:** cirka 60 min · **Fas:** Mekanik · **Beroenden:** LR-01, LR-02 · **Status:** ej verifierad

**Ta fram:** YZ_Max, motsvarande XZ-platta, två MGN12, motorer, brytare och hjul.

1. Märk Y1- och Z1-kablar och verifiera spegelvänd orientering mot manualen.
2. Montera Z-brytare, Y-motor med verifierat 16T-remhjul, framhjul och Y-brytare.
3. Rensa skenbäddar; montera skenor och XZ-platta, dra stegvis och provför över hela rörelsen.
4. Notera eventuella delar som återstår innan båda sidornas Z-mekanik kan slutföras.

**Godkänt när:** Max-sidans skenor och vagn rör sig lätt; fel eller oavslutade moment dokumenterade.

**Återrapportera:** Foton på orientering, fri rörelse och avvikelser.

**Bildguide:** [Svenska manualen, kapitel 3](https://kingkongola.github.io/lowrider/#2).

### LR-11 — Färdigställ Z och bakhjulen

**Tid:** cirka 60 min · **Fas:** Mekanik · **Beroenden:** LR-09, LR-10 · **Status:** ej verifierad

**Ta fram:** Båda YZ-sidor, Z_Stub, Z_Nut, T8-spindel, 5→8-kopplingar och bakhjul.

1. Montera Z-motorernas kopplingar och T8-mutter enligt originalbilderna.
2. Montera båda bakhjulen; kontrollera plan anliggning och att plasten inte kläms.
3. Montera Z_Stub vinkelrätt mot skruven; vrid Z för hand och kontrollera att det inte kärvar.
4. Ställ Z-brytarna så att de utlöser före mekaniskt ändläge. Mät därefter fysisk längd för varje T8-del; kapa bara efter verifierad frigång.

**Godkänt när:** Båda Z-sidor går utan bindning och brytarna når sina lägen; spindellängder dokumenterade.

**Återrapportera:** Bilder, brytarmarginal, uppmätta T8-längder och eventuell bindning.

**Bildguide:** [Svenska manualen, kapitel 3](https://kingkongola.github.io/lowrider/#2).

### LR-12 — Bygg balk med temporära stag

**Tid:** cirka 60 min · **Fas:** Mekanik · **Beroenden:** LR-01, LR-06 · **Status:** ej verifierad

**Ta fram:** Två 816 mm-rör, Brace-delar, X-remspännare och fyra Temp Strut.

1. Fördela änd-Brace och övriga Brace på två X-rör enligt manualen.
2. Montera X-remspännarens mutter och kontrollera riktningen.
3. Montera fyra temporära stag i rätt orientering, två fram och två undertill.
4. Dra försiktigt och kontrollera rakhet och att inga rör sticker ut ur ändklämmorna.

**Godkänt när:** Rak temporär balk med rätt stag och ingen skadad print.

**Återrapportera:** Översiktsfoto, rörändar och notering om stagpassning.

**Bildguide:** [Svenska manualen, kapitel 4](https://kingkongola.github.io/lowrider/#3).

### LR-13 — Förena balk, Core och YZ

**Tid:** cirka 60 min · **Fas:** Mekanik · **Beroenden:** LR-08, LR-11, LR-12 · **Status:** ej verifierad

**Ta fram:** Färdig Core, temporär balk, två YZ-enheter, vinkel och måttband.

1. Montera YZ_Max i balken, skjut försiktigt på Core och avsluta med YZ_Min.
2. Känn efter glapp i Core och justera spännskruvarna minimalt endast vid behov.
3. Kontrollera att nedre X-röret inte vidrör XZ-plattorna.
4. Grovnivellera Z; mät bredd på YZ-plattorna fram och bak (heel–toe) och justera till lika mått.

**Godkänt när:** Core rullar fritt över hela X och båda sidor har dokumenterade fram-/bakmått.

**Återrapportera:** Foto hel maskin, mätta fram-/bakmått, eventuell kontakt/bindning.

**Bildguide:** [Svenska manualen, kapitel 5](https://kingkongola.github.io/lowrider/#4).

### LR-14 — Slutplacera remhållare och Y-skena

**Tid:** cirka 60 min · **Fas:** Mekanik · **Beroenden:** LR-05, LR-13 · **Status:** ej verifierad

**Ta fram:** Bord, sammanbyggd maskin, skena, Y-clips/remhållare och skruvar.

1. Ställ maskinen på bordet och kontrollera de preliminära 941 × 1563 mm-markeringarna mot faktisk geometri.
2. Kontrollera att enda Y-styrskenan blir rak och parallell med vald bordskant.
3. Markera, förborra och montera Y-styrskenans clips och remhållarna enligt V1E. Max 300 mm mellan clipsens centrum.
4. Kontrollera att stoppskruvarna möter respektive brytararm före mekaniskt stopp.

**Godkänt när:** Fasta styr-/remreferenser på bordet utan kollisioner eller brytararm som kan passera stopp.

**Återrapportera:** Översiktsfoto, kontroll av rälsens rakhet och stoppskruvar.

**Bildguide:** [Svenska manualen, kapitel 6](https://kingkongola.github.io/lowrider/#5).

### LR-15 — Trä och spänn tre remmar

**Tid:** cirka 60 min · **Fas:** Mekanik · **Beroenden:** LR-14 · **Status:** ej verifierad

**Ta fram:** 3 verifierade 16T-remhjul, idlers, 5 m GT2/10 mm-rem, Y-/X-remfästen.

1. Kontrollera att samtliga remhjul och idlers sitter i linje innan remmen kapas.
2. Trä två Y-remmar och X-remmen enligt respektive bild; verifiera verklig längd innan definitiv kapning.
3. Fäst remändarna och spänn försiktigt enligt originalets riktvärde, inte hårdare.
4. För X och Y sakta för hand och kontrollera remspårning och frigång.

**Godkänt när:** Tre remmar i korrekt läge; inga idlers nyper och ingen rem vandrar.

**Återrapportera:** Verkliga kaplängder, foto på alla remvägar och eventuell avvikelse.

**Bildguide:** [Svenska manualen, kapitel 6](https://kingkongola.github.io/lowrider/#5).

### LR-16 — Planera kablar, slang och elplacering

**Tid:** cirka 60 min · **Fas:** El och damm · **Beroenden:** LR-13 · **Status:** ej verifierad

**Ta fram:** Jackpot3, HDR-60-24, KATSU, befintlig DeWalt-slang och rörlig balk.

1. Prova placeringen av Jackpot3 på balkens YZ_Min-sida.
2. Prova möjlig placering av HDR-60-24 på balken, utan nätspänningsinkoppling. Identifiera behov av kapsling, PE och dragavlastning.
3. Lägg ut fräskabel, tänkt matning till HDR, motor-/brytarkablar och dammsugarslang samtidigt.
4. Flytta maskinen för hand till rörelseextremerna. Fotografera där kablar/slang riskerar att sträckas eller fastna.

**Godkänt när:** En fysisk kabelplan och en lista över osäkerheter; inga exponerade 230 V-plintar planeras.

**Återrapportera:** Foton från fyra hörn och eventuella konflikter. Ingen spänningssättning.

**Bildguide:** [Svenska manualen, kapitel 7](https://kingkongola.github.io/lowrider/#6).

### LR-17 — Bygg dammskons mekaniska del

**Tid:** cirka 60 min · **Fas:** El och damm · **Beroenden:** LR-01 · **Status:** ej verifierad

**Ta fram:** Dust shoe-utskrifter, befintlig TPU, KATSU-fästet, slang och måttband.

1. Inventera delarna till dust shoe och prova sammanpassning utan fräs igång.
2. Bedöm om befintlig TPU har lämplig böjlighet för borstlisten; provprinta vid behov.
3. Prova slangens passform och rörelsefrigång vid KATSU-fästet.
4. Fotografera passning och notera om någon adapter behövs; köp inte ny slang innan detta test.

**Godkänt när:** Dust shoe provmonterad eller tydlig lista på verkligt saknade delar.

**Återrapportera:** Foton på infästning, TPU-resultat och slangens dimension.

**Bildguide:** [Svenska manualen, kapitel 7](https://kingkongola.github.io/lowrider/#6).

### LR-18 — Planera cyklon och uppsamlingskärl

**Tid:** cirka 60 min · **Fas:** El och damm · **Beroenden:** Inga · **Status:** ej verifierad

**Ta fram:** Befintlig DeWalt, cyklonmodell/utskrift, föreslagen 15–30 l behållare och slang.

1. Läs av DeWalt-modellens typskylt och fotografera den.
2. Kontrollera cyklondelarnas passning och anslutningsdiameter mot slangen.
3. Kontrollera kandidat till uppsamlingskärl och lock; säkerställ att behållaren är avsedd att tåla undertrycket.
4. Skissa eller provlägg slangvägen och vilka delar som faktiskt behöver köpas eller skrivas ut.

**Godkänt när:** Kända anslutningsmått, behållarstatus och konkret åtgärdslista.

**Återrapportera:** Typskylt, slangmått, foton och uppgift om behållaren.

**Bildguide:** [Svenska manualen, kapitel 7](https://kingkongola.github.io/lowrider/#6).

### LR-19 — Jackpot3: installation och konfiguration

**Tid:** cirka 60 min · **Fas:** Styrning · **Beroenden:** LR-02 · **Status:** ej verifierad

**Ta fram:** Jackpot3, data-USB-C, FAT32-microSD, dator och aktuell V1E-konfiguration.

1. Kontrollera kretskortets modell CQA240812C2 och eventuella transportsynliga skador.
2. Inventera dataförande USB-C och microSD; notera om något saknas.
3. Jämför V1E:s aktuella testade FluidNC-version och LR4/Jackpot3-konfiguration; säkerhetskopiera eventuell befintlig config.
4. Utför endast tillverkarens avsedda flash-/konfigurationssteg med frånkopplade motorer och fräs; dokumentera uppstartsmeddelanden.

**Godkänt när:** Versioner och config dokumenterade; enheten startar utan kända konfigurationsfel, eller specifikt fel rapporterat.

**Återrapportera:** Firmware/WebUI-version, status för config, eventuella felmeddelanden. Inga hemliga nätverksuppgifter.

**Bildguide:** [Svenska manualen, kapitel 8](https://kingkongola.github.io/lowrider/#7).

### LR-20 — Koppla och prova fem brytare

**Tid:** cirka 60 min · **Fas:** Styrning · **Beroenden:** LR-19, LR-16 · **Status:** ej verifierad

**Ta fram:** 5 × Omron SS-3GL13PT, lågspänningskablar och aktuell Jackpot3/LR4-kopplingsbild.

1. Anslut COM + NC för varje brytare enligt rätt Jackpot3-schema; verifiera pinout på levererat kort.
2. Märk X, Y0, Y1, Z0, Z1 tydligt och kontrollera kabeldragningen.
3. Med fräsen frånkopplad: använd FluidNC:s statusfunktion och aktivera en brytare åt gången.
4. Dokumentera vilken status som ändras; felsök innan någon homing om signalerna är fel.

**Godkänt när:** Fem brytare reagerar var för sig i rätt ingång; kontakter är dragavlastade.

**Återrapportera:** Tabell X/Y0/Y1/Z0/Z1 med utslag ja/nej och eventuella fel.

**Bildguide:** [Svenska manualen, kapitel 8](https://kingkongola.github.io/lowrider/#7).

### LR-21 — Första försiktiga motorprov

**Tid:** cirka 60 min · **Fas:** Styrning · **Beroenden:** LR-15, LR-19, LR-20 · **Status:** ej verifierad

**Ta fram:** Fem motorer, avlastade kablar, fri maskin och möjlighet att direkt bryta styrningen.

1. Kontrollera att fräsen är urkopplad, verktyget borttaget och rörelsevägen fri.
2. Verifiera motoranslutningar enligt Jackpot3-konfigurationen; justera inte motorledningarna med matning inkopplad.
3. Jogg 1 mm i taget och kontrollera X+, Y+ och Z+ var för sig.
4. Om riktningen stämmer, prova korta rörelser och därefter homing under uppsikt med fungerande brytare.

**Godkänt när:** Riktningar, motorpar och homing antingen verifierade eller blockering dokumenterad. Ingen skärning.

**Återrapportera:** Status per axel och brytare, ljud/bindning och eventuella fel.

**Bildguide:** [Svenska manualen, kapitel 8](https://kingkongola.github.io/lowrider/#7).

### LR-22 — Kontrollera 230 V-upplägg och maskinstopp

**Tid:** cirka 60 min · **Fas:** Elsäkerhet · **Beroenden:** LR-16 · **Status:** ej verifierad

**Ta fram:** Verklig NVR-enhet om köpt, HDR-60-24, tillhörande tillverkardokumentation och kapsling.

1. Dokumentera NVR-modell och märkning eller att enheten ännu inte är köpt.
2. Verifiera att lösningen ger beröringsskydd för HDR:s nätplintar samt mekaniskt säker infästning på balken.
3. Gå igenom skyddsjord, kabeltyp, kabelgenomföring och dragavlastning med en elkunnig person.
4. Låt behörig/kompetent person utföra och verifiera faktisk 230 V-koppling. Testa återstartsskydd med fräsen frånkopplad när anläggningen är färdig.

**Godkänt när:** Antingen verifierad säker installation med dokumenterat maskinstopp eller spärrad elinstallation med exakt åtgärd.

**Återrapportera:** Modell, kapslingsfoto, verifieringsstatus och eventuella öppna säkerhetsfrågor.

**Bildguide:** [Svenska manualen, kapitel 9](https://kingkongola.github.io/lowrider/#8).

### LR-23 — Torrkör hela rörelseområdet

**Tid:** cirka 60 min · **Fas:** Driftsättning · **Beroenden:** LR-21, LR-22, LR-16 · **Status:** ej verifierad

**Ta fram:** Monterad maskin, kabeldragning, slang, fungerande stopp och tydlig fri yta.

1. Med fräsen urkopplad, börja från homad maskin och testa små rörelser.
2. Kör stegvis X/Y över tillgängligt område och Z genom avsett område; kontrollera slang och samtliga kablar.
3. Notera remvandring, mekaniskt kärvande, hinder och utrymme vid alla fyra hörn.
4. Avbryt vid konflikt och dokumentera exakt position före åtgärd.

**Godkänt när:** Alla rörelseextremer prövade utan drag i kablar, slang eller mekaniska hinder.

**Återrapportera:** Resultat för varje hörn och Z-extremer, foton vid eventuella problem.

**Bildguide:** [Svenska manualen, kapitel 10](https://kingkongola.github.io/lowrider/#9).

### LR-24 — Gör CAM för första provskärningen

**Tid:** cirka 60 min · **Fas:** Fräsning · **Beroenden:** LR-23, LR-17 · **Status:** ej verifierad

**Ta fram:** 3,175 mm-fräs, fungerande dammuppsamling, billig trä-/skummaterialbit och CAM.

1. Välj ett enkelt litet provjobb. Kontrollera fräshylsans passning och verktygets uppspänning med fräsen urkopplad.
2. Välj material och försiktiga skärdata enligt verktygets rekommendationer; skriv ut eller visa förhandsgranskad verktygsbana.
3. Säkerställ att klämmor, skruvar och nollpunkt ligger utanför banan.
4. Gör en simulering och luftkörning med fräsen avstängd. Börja inte skära om NVR/damm/infästning saknas.

**Godkänt när:** Förhandsgranskad och luftkörd liten verktygsbana, färdig för skärning.

**Återrapportera:** Filnamn, verktyg/material, beräknat djup och notering om nollpunkt.

**Bildguide:** [Svenska manualen, kapitel 10](https://kingkongola.github.io/lowrider/#9).

### LR-25 — Första lilla skärprovet

**Tid:** cirka 60 min · **Fas:** Fräsning · **Beroenden:** LR-24, LR-18 · **Status:** ej verifierad

**Ta fram:** Godkänd CAM, fräs, material, inspänning, NVR och fungerande dammhantering.

1. Kontrollera arbetsstyckets infästning, verktyg och kablar en sista gång.
2. Starta dammhantering och gör ett kort skärprov under ständig uppsikt.
3. Mät enkel detalj samt verkligt Z-djup efter körningen.
4. Dokumentera eventuella avvikelser innan någon större fräsning.

**Godkänt när:** Litet fräsprov och mått dokumenterade; inga kollisioner.

**Återrapportera:** Foto på skärningen, verktyg, material, X/Y/Z-avvikelse.

**Bildguide:** [Svenska manualen, kapitel 10](https://kingkongola.github.io/lowrider/#9).

### LR-26 — Generera permanenta stagplattor

**Tid:** cirka 60 min · **Fas:** Fräsning · **Beroenden:** LR-25 · **Status:** ej verifierad

**Ta fram:** V1E:s strutgenerator, CAD/CAM, 5–6 mm MDF/hårdboard och uppmätta balkmått.

1. Kontrollera våra mått mot verklig balk. Använd strut_length=819 och front_wing_size=30 endast om de fortfarande matchar.
2. Generera främre och undre stagplatta; spara fil och skärmlägg måtten.
3. Importera i millimeter och kontrollera riktning, materialtjocklek, hålbild och passform.
4. Planera hål före ytterkontur, hållflikar och säker fastspänning. Kör simulering utan att skära.

**Godkänt när:** Två verifierade CAM-jobb som matchar verklig balk och material.

**Återrapportera:** Generatorvärden, materialtjocklek, CAD-skärmdump och filnamn.

**Bildguide:** [Svenska manualen, kapitel 10](https://kingkongola.github.io/lowrider/#9).

### LR-27 — Fräs permanenta stagplattor

**Tid:** cirka 60 min · **Fas:** Fräsning · **Beroenden:** LR-26 · **Status:** ej verifierad

**Ta fram:** Verifierat CAM, skivmaterial, fungerande dammhantering och maskinstopp.

1. Fäst materialet utan skruvar i verktygsbanan.
2. Fräs hål och ytterkontur för första plattan under uppsikt; kontrollera passformen utan tvång.
3. Om passformen stämmer, fräs andra plattan. Om tiden inte räcker: rapportera en platta klar, en återstår.
4. Märk fram/undersida och dokumentera slutmått.

**Godkänt när:** Båda permanenta stagplattor färdiga och passningen verifierad, annars delvis klar.

**Återrapportera:** Foton, slutmått och eventuell återstående platta.

**Bildguide:** [Svenska manualen, kapitel 10](https://kingkongola.github.io/lowrider/#9).

### LR-28 — Byt till permanenta stag

**Tid:** cirka 60 min · **Fas:** Slutkontroll · **Beroenden:** LR-27 · **Status:** ej verifierad

**Ta fram:** Två färdiga plattor, maskinen med temporära stag och V1E:s bytesbilder.

1. Ta av och samla X/Y-remmarna så att de inte fastnar.
2. Byt ut de fyra temporära stagen mot främre och undre permanenta plattan i manualens ordning.
3. Återmontera Core och dra förband jämnt utan att klämma ihop Brace-delarna.
4. Kontrollera heel–toe fram/bak och Z:s fria rörelse. Om tiden tar slut: låt maskinen strömlös och rapportera läget.

**Godkänt när:** Permanenta plattor på plats, men kalibrering och återtest återstår i separat order.

**Återrapportera:** Foton på de två plattorna, heel–toe-mått och mekanisk status.

**Bildguide:** [Svenska manualen, kapitel 10](https://kingkongola.github.io/lowrider/#9).

### LR-29 — Planfräs offerskivan

**Tid:** cirka 60 min · **Fas:** Slutkontroll · **Beroenden:** LR-28 · **Status:** ej verifierad

**Ta fram:** Cirka 12 mm MDF-offerskiva, fräsverktyg, dammhantering och planfräsningsjobb.

1. Fäst den löstagbara offerskivan och verifiera mekaniken efter stagbytet.
2. Kontrollera att hela verktygsbanan ryms och att spännelement är utanför banan.
3. Planfräs i kontrollerade pass under uppsikt utan att skära i bordet.
4. Mät eller kontrollera resultatets jämnhet och fotografera. Om jobbet tar mer än en timme, dela återstående yta i nästa pass.

**Godkänt när:** Offerskivan planfräst i avsett arbetsområde eller tydligt återstående område dokumenterat.

**Återrapportera:** Avverkat djup, täckt yta, foton och eventuell kvarvarande yta.

**Bildguide:** [Svenska manualen, kapitel 10](https://kingkongola.github.io/lowrider/#9).

### LR-30 — Slutkalibrera och säkerhetskopiera

**Tid:** cirka 60 min · **Fas:** Slutkontroll · **Beroenden:** LR-28, LR-29 · **Status:** ej verifierad

**Ta fram:** Mätverktyg, fungerande maskin, originalets kalibreringssteg och config-backup.

1. Mät en känd X/Y-förflyttning och justera steps_per_mm endast utifrån faktiska mätningar.
2. Mät båda diagonalerna i en markerad rektangel och korrigera Y-homing/pull-off vid behov.
3. Jämför Z-nivå mellan sidorna, prova ett enkelt kalibreringsprov och dokumentera resultatet.
4. Spara fungerande config.yaml utanför styrenheten och notera aktuellt maskintillstånd.

**Godkänt när:** X/Y, diagonaler och Z dokumenterade; config säkerhetskopierad.

**Återrapportera:** Kommenderad/uppmätt sträcka, två diagonaler, Z-avvikelse och backupstatus.

**Bildguide:** [Svenska manualen, kapitel 10](https://kingkongola.github.io/lowrider/#9).
