# LowRider 4 – svensk monteringsguide för vårt bygge

**Utgåva:** 2026-09-29 · **Status:** källgranskad arbetsguide; fysisk verifiering återstår. Bocka inte av kontroller förrän de faktiskt är gjorda.

Den här guiden följer V1 Engineerings monteringsordning och kompletterar den med vår faktiska BOM, svenska förklaringar, kontrollpunkter och avvikelser. **Ha alltid originalbilderna öppna:** [V1E:s LowRider 4-manual](https://docs.v1e.com/lowrider/). De visar exakt orientering av skruvar, muttrar, ledare och printade delar. Detta är inte en ersättning för tillverkarens instruktioner eller ett bevis på att maskinen är färdigmonterad.

Källor: [V1E LR4](https://docs.v1e.com/lowrider/) · [V1E Jackpot3](https://docs.v1e.com/electronics/jackpot3/) · [V1E FluidNC-konfigurationer](https://github.com/V1EngineeringInc/FluidNC_Configs/releases) · våra [DECISIONS](../DECISIONS.md), [BOM](../BOM.md), [CHECKLIST](../CHECKLIST.md), [AUDIT](../AUDIT.md) och [TABLE](../TABLE.md). Projektspecifika värden nedan kommer från SSOT, inte från standardmaskinens exempelvärden. Kontrollera dokumentationens senaste version före firmware-/konfigurationsändringar.

## Snabböversikt: just vår maskin

| Del | Vårt val eller mått |
|---|---|
| Modell och tänkt arbetsyta | LowRider V4; 650 × 1250 mm |
| Bord | Köpt skiva 1800 × 1000 mm; underredet ännu inte godkänt |
| Rör | Ø30 × 1,5 mm; längder **816, 816, 1505 mm** efter verklig mätning |
| Temporär balk | **4 × Temp Strut, 15 % infill** |
| Permanenta stagplattor | `strut_length=819`, `front_wing_size=30`; 5–6 mm styv MDF/hårdboard, högst 6,35 mm |
| Remmar | GT2 10 mm. V1E-kalkylatorns längder **X 999 / Y 1705 / Y 1705 mm**. Projektets grovkapmått är **X minst 1029 / Y minst 1735 / Y minst 1735 mm** (30 mm reserv per rem). Överskott putsas efter provning och spänning. Se *Kapplan* i kapitel 0 |
| T8-spindel | **150 mm per sida är ett provmått**, inte kapklar instruktion. Provpassa på båda YZ-sidorna innan 400 mm-spindeln kapas; se kapitel 0 |
| Kablar | Motorkablar (1 m) kapas **aldrig**; behov och längd för förlängningar till X, Y1 och Z1 bestäms vid provdragning. Brytarkablar kapas vid Jackpot3 efter *mät-och-märk* i kapitel 6 |
| Motorer | 5 × STEPPERONLINE `17HS19-2004S1` |
| Styrenhet | **Elecrow Jackpot3 `CQA240812C2`**, mottagen; rätt Jackpot3-låda |
| Matning | Mean Well `HDR-60-24`, 24 V; planerat **på rörlig balk** tillsammans med Jackpot3, efter skydds- och infästningskontroll |
| Gränslägesbrytare | 5 × Omron `SS-3GL13PT`, normalt slutna (NC), anslut COM + NC |
| Handöverfräs | KATSU `101750`, 710 W, cirka 65 mm; Makita/65 mm-fäste |
| Fräsfäste/verktyg | Makita/Elaire 1/8-tumshylsa; provpassa före start |

**Placering efter omprövning (D016):** NVR/maskinstopp är fast och lättåtkomligt på bordet; Jackpot3 och vårt Mean Well HDR-60-24 planeras på balken enligt V1E:s princip. Vårt DIN-aggregat är inte automatiskt lämpligt för oskyddad balkmontering. Kontrollera beröringsskydd för nätplintar, jordning, kapsling, infästning och dragavlastning före anslutning. Köp inte alternativa komponenter bara för att V1E:s bilder visar en annan aggregatmodell.

**Läge 2026-09-21:** Alla tre 16T-remhjul har kommit fram enligt användaren; kontroll av deras tekniska mått kvarstår. Användaren har rapporterat utskrift av platta 14/14. **Det separat listade Makita/65 mm-verktygsfästet är inte verifierat utskrivet** och ska kontrolleras/slic:as separat före moment 1.4 (LR-00). Även Jackpot3-box, komplett utskriftsinventering, slutlig rör-OD och bordets styvhet är ännu inte fysiskt verifierade.

## 0. Förbered arbetsplatsen – före första skruven

Original: [utskrifter, geometri och montering](https://docs.v1e.com/lowrider/).

**Läs detta före kapning:** måtten gäller 650 × 1250 mm arbetsyta, 30 mm-printar och **6,0 mm XZ-plattor**. Kalkylatorn är omkontrollerad 2026-09-29. Det bekräftar ritningsmåtten, inte dina fysiska delar. Tidigare formulering om ovillkorlig T8-kapning till 150 mm är återtagen.

**Arbetsordning:** mekanik → bordets styrning → provdra kablar/slang (kapitel 6) → slutspänn remmar → kontrollera nätmatning och stopp (kapitel 8) → motorprov (kapitel 7) → provskärning. Med egen kabelrulle används dragtråd i kanaler som annars blir oåtkomliga; inga kabellängder gissas.

**Kvar före godkänt bygge:** T8-provpassning, Core-kabelns passning, fem kompletta brytaranslutningar, eventuella motorförlängningar, bord/printar/fräsfäste samt nätmatning/stopp och dammhantering. Se [granskningsprotokollet](../AUDIT_2026-09-29.md).

- [ ] Sortera HaWiWe: två 6 mm XZ-plattor, **4 × MGN12H 150 mm**, skruvsats och 1/8-tumshylsa. Provpassa M3×10 i skena/lagerblock/platta: ingenting ska bottna eller kärva.
- [ ] Inventera DigiKey-paketet mot [BOM](../BOM.md). Kontrollera 608-2RS-lager, mikrobrytare, kablar och anslutningar.
- [ ] Kontrollera utskrifterna: **30 mm-varianter**, samtliga fyra temporära stag, och separat Makita/65 mm-verktygsfäste samt Jackpot3-låda. **OBS:** dessa två specialdelar ingår inte verifierat i de 14 grundplattorna. Kontrollera/förbered fästet via [V1E:s separat publicerade Makita 701 Tool Mount and Dust Shoe](https://www.printables.com/model/1033926-makita-701-tool-mount-and-dust-shoe-for-the-lowrid) (arbetsorder LR-00); kontrollera rätt fäste för KATSU-husets cirka 65 mm. Granska `Z_Stub`, `Z_Nut`, YZ-bryggor och Dust Skirt för skadade hål/överhäng.
- [ ] De tre 16T-remhjulen är mottagna 2026-09-21. Kontrollera tandantal, 5 mm axelhål och passning för 10 mm GT2-rem innan montering.
- [ ] Ordna handverktyg, skjutmått, rätvinkel, måttband, liten rak linjal, märkpenna och märkningstejp. Använd handverktyg för skruvförbanden; dra inte sönder printarna med skruvdragare.
- [ ] Kontrollera bordets underrede för glapp och vridning. Markera **941 × 1563 mm** minsta footprint, samt utrymme för två Y-remmar och kabelslinga. Skruva inte i skivan innan layouter och rörelsezoner stämmer.
- [ ] Mät verklig ytterdiameter, rakhet och användbar längd hos Motonet-rören **före kapning**. För 30 mm-varianten anger V1E 30,0 ±0,2 mm OD och minst 1,3 mm vägg; vårt rörval är 1,5 mm vägg. Kapa först efter kontroll till 816 + 816 + 1505 mm och grada ändarna.
- [ ] Kontrollera att även de mindre printdelarna i V1E:s printlista finns: 8 remhållardelar (`Y_Belt_MinF/MinB/MaxF/MaxB`, `Y_Belt_Max_Lock`, `Y_Belt_Min_Lock`, `Y_Belt_Min_Tension`, `Y_Belt_Max_Tension`), `X_Belt`, `ZStop_Min/Max`, 2 × `Z_Nut`, `Z_Stub_Min/Max`, `Brace` + `Brace_Max`, `Hose_Hook`, `Hose_Holder_Hook`, 2 × `Hose_Holder_Shorty` och `Y_Clip`. **Ändbracen (`Brace_Max` och en `Brace`) ska vara utskrivna med 60 % infill.** `Hose_Hook`-delarna behövs redan vid kabeldragningen i kapitel 6. Y_Clip-antal: mät avståndet mellan första och sista clip, dela med 300 mm, avrunda uppåt och lägg till 1 – för vår 1505 mm Y-skena blir det cirka 6–7 st.
- [ ] **Kapa de tre remmarna** enligt kapplanen nedan och märk dem `Y0`, `Y1` och `X`. Y-remmarna behövs redan i kapitel 2 (steg 4) och X-remmen i kapitel 1 (steg 6).
- [ ] **Förbered T8-provpassningen** enligt kapplanen. Montera först YZ-sidornas skenor, motorer, kopplingar och Z-fästen; verifiera längden på båda sidor före kapning och slutmontage i kapitel 2 steg 8.

**Stoppregel:** Om en rördel är fel diameter, om printade passningar är skadade eller om en skena binder utan belastning: rätta detta innan du bygger in felet. **Core är omprintad utan den tidigare rapporterade cirka 0,20 mm förskjutningen**; använd den nya delen och kontrollera dess vanliga lager- och fästpassningar.

### Kapplan – rör, remmar och kablar

| Vad | Råvara | Kapa till | Varför just detta mått | När |
|---|---|---|---|---|
| X-rör | Motonet Ø30×1,5 | **2 × 816 mm** | V1E-kalkylator för 650 × 1250 mm | Före kapitel 3 |
| Y-rör | Motonet Ø30×1,5 | **1 × 1505 mm** | V1E-kalkylator | Före kapitel 5 |
| Y-rem ×2 | 5 m GT2 10 mm | **minst 1735 mm vardera** | V1E: Y-rör + 200 = 1705 mm. +30 mm reserv som putsas bort efter spänning | Före kapitel 2 steg 4 |
| X-rem | samma rulle | **minst 1029 mm** | V1E: stag 819 + 180 = 999 mm. +30 mm reserv | Före kapitel 1 steg 6 |
| Remrest | samma rulle | cirka 500 mm över | 5000 − 1735 − 1735 − 1029 = 501 mm | Spara |
| T8-spindel | 400 mm T8×8 | **Ej kapklar: prova 150 mm per sida** | V1E anger 145 mm eller längre. D014 kräver fysisk kontroll; 5 mm extra bevisar inte frigång | Efter sidornas provmontage, före slutmontage i kapitel 2 steg 8 |
| Stegmotorkablar | 1 m fast | **Kapas inte** | Prova räckvidden; förläng där det behövs | Kapitel 6 |
| Brytarkablar ×5 | 10 m 3×26 AWG | **Mät och märk vid Jackpot3**, kapa sedan | Kapstället beror på den verkliga vägen. Metod i kapitel 6 | Efter kapitel 4, före kapitel 7 |

**Så kapar du remmarna**

1. **Mät hela rullen och markera alla tre bitar innan första klippet.** Grovkapplanen kräver nominellt 4499 mm, plus eventuell avrundning till tandmellanrum. Om markeringarna inte ryms: **STOPP**, gör om fördelningen före kapning. V1E:s beräknade sammanlagda längd är 4409 mm; under det räcker rullen inte till de beräknade måtten. Minska inte marginalen automatiskt.
2. Rulla ut remmen på ett bord med tänderna nedåt. Mät från den raka änden med måttband och markera med en tejpbit. Kapa **Y-remmarna först** och därefter X-remmen.
3. Kapa rakt över med vass sax. Om måttstrecket träffar en tand: välj nästa tandmellanrum så att biten blir lite **längre**, inte kortare. Anteckna verkliga längder; GT2 har 2 mm tanddelning.
4. **Undvik onödiga veck och vridningar.** Den avsedda ändöglan runt M3 görs senare enligt V1E:s låsning; detta är inte ett förbud mot den monteringen. Rulla varje bit löst och märk den med tejp: `Y0`, `Y1`, `X`.
5. De extra 30 mm är vår kapmarginal, inte ett V1E-krav. Fördela den över ändarna och lämna överskottet tills båda ändlås, hela rörelsen och remspänningen har provats. Putsa bara svans utanför låsningen; lämna flera tänder och lite justermån (kapitel 5).

**Så verifierar och kapar du T8-spindeln**

1. Gör kapitel 2 steg 2–7 på båda sidorna och förbered `Z_Nut`/`Z_Stub`. Håll allt strömlöst. Prova den okapade spindeln **på en sida i taget på bänken**, med fri plats ovanför; märk 150 mm från fabriksänden som provgräns. Den långa stången får inte kollidera eller belasta montaget snett.
2. Sätt fabriksänden på rätt djup i kopplingen enligt kapitel 2. Vrid för hand genom avsett Z-slag. Kontrollera att muttern har fullt gängingrepp även vid högsta läget, att den tänkta änden inte kolliderar med något och att Z-brytaren utlöser före mekaniskt stopp. Kontrollera samma sak på andra sidan. Om detta inte går att verifiera: **kapa inte**; dokumentera mått och foton först. 150–160 mm i D014 är ett arbetsmål, inte en garanti.
3. Skriv upp godkänd färdig längd för respektive sida. Ta ur stången innan sågning. Markera från respektive fabriksände; sågspåret ska hamna i mittbiten som blir över. Två färdiga 150 mm-delar ger **100 mm minus två sågspår** i rest, inte ett bestämt 95 mm-mått.
4. Skruva en reservmutter över kapmärket så att den sitter på den del som ska behållas. Spänn stången skyddat utan att skada gängorna. Såga utanför måttstrecket och fila till färdigt mått; en liten avgradningsfas ska inte ta bort flera millimeter längd.
5. Skruva muttern över den avgradade änden utan våld, avlägsna spån och prova full muttergång. Fabriksänden sätts i kopplingen. Upprepa för andra sidan och kontrollera åter Z-slag och ändlägesfrigång. Använd ögonskydd vid kapning/avgradning.

**Rörkapning:** från ett 2000 mm-rör tas 1505 mm; från det andra tas två färdiga 816 mm-bitar. Mät andra biten från den nya, rensade änden efter första kapningen – markera inte bara 816 och 1632 mm utan hänsyn till sågspåret. Såga på spillsidan, grada och mät om båda ändar. De två X-rören ska ha samma färdiga längd. 819 mm är stagets inmatningsmått och får inte användas som rörmått.

## 1. Montera Core (X-vagnen)

Originalbilder: [Core Assembly](https://docs.v1e.com/lowrider/#core-assembly).

1. **Lageraxlarna, bild `ca.jpg`–`cc.jpg`:** Ta fram **8 × 608-2RS (8×22×7 mm)** från DigiKey, **8 × M8×40 sexkantsskruvar** och **8 × M8 nyloc** från HaWiWe. Montera de första **tre paren (6 lager, 6 skruvar och 6 muttrar)**, två i taget enligt `ca.jpg`, `cb.jpg` och `cc.jpg`. Sätt ett lager i varje visad ficka och för varje M8-skruv genom lagrets 8 mm innerhål **åt det håll bilden visar**; montera en M8-låsmutter per skruv. Dra bara an tills skruvhuvudena ligger an. **Inget lager får nypa och ingen plast får deformeras.**
2. **Sista paret, bild `cd.jpg`:** montera resterande **2 lager + 2 M8×40 + 2 M8 nyloc** i bildens övre justerlägen. Dessa två är också lageraxlar, men fungerar dessutom som **Core-spännskruvar** mot X-rören. **Lämna båda lösa** tills Core har satts på balken; ingen slutlig spänning nu. Totalt i Core: **8 lager, 8 M8×40 och 8 M8 nyloc**. De återstående sex 608-lagren av V1E:s totalt 14 monteras senare i YZ-hjulen; två av dina 16 inköpta är reserv.
3. **Verktygsfästets muttrar, bilder `ce.jpg`–`ch.jpg`:** ta fram **4 × M5 nyloc** från HaWiWe och fyra korta PLA-filamentbitar. Tryck i en mutter per hål med nylondelen åt det håll `cf.jpg` visar. För in filamentet genom låshålen så att muttern hålls kvar; på motsatt sida vinklas filamentänden åt andra hållet (`cg.jpg`). Klipp alla fyra filamentbitar **jäms med Core**.
4. **Verktygsfästet, bilder `ci.jpg`–`cj.jpg`:** **STOPP om det separata Makita/65 mm-fästet saknas; gör LR-00 först.** Placera det faktiskt utskrivna och provpassade **Makita/65 mm-fästet** plant mot Core och använd de **4 M5-fästskruvarna från HaWiWe-satsen** (satsen innehåller M5×30). Kontrollera faktisk gängingrepp och att skruvarna inte bottnar; originaltexten anger fyra skruvar, men specificerar inte uttryckligen deras längd för varje verktygsfäste. Starta alla fyra för hand utan att knuffa ut muttrarna. Dra alla fyra nästan i botten och dra sedan **de vänstra skruvarna fullt först**, både uppe och nere (V1E:s ordning). Dra ordentligt, men utan att spräcka plasten. Om fräsen senare behöver trammas räcker det oftast med ett par lager tejp som mellanlägg under fästet. **Köp inga andra skruvar innan dessa provpassats.**
5. **Två separata kablar genom Core – touchplate är planerad:** V1E:s bilder `ck.jpg`–`cm.jpg` visar **touchplate-ledningen** först. Vi vill använda touchplate senare: planera plats för en separat **tunn, flexibel, isolerad touchplate-kabel** med minst **140 mm fri längd** vid Core enligt originalet. Bilderna `co.jpg`–`cq.jpg` visar sedan en **annan kabel** till X-gränslägesbrytaren (COM + NC). Brytaren monteras med de små M2,5-skruvarna **med armen öppnande nedåt**. Dra skruvarna i botten, men varsamt, så att gängorna i plasten inte dras sönder. Märk ledarna så fort de kommit igenom, och kontrollera krimp/lödning med en kontinuitetsmätning. **Koppla aldrig touchplate till brytaren och dela inte brytarledarna med touchplate.** Den inköpta svarta Tensility `30-00377` (3×26 AWG, cirka Ø4 mm) har användaren provat: **manteln går inte genom Cores tunnel**. Ingen av kablarna behöver slutkapas nu. **Om touchplate-kabeln inte finns ännu:** montera lagren/muttrarna, men lämna kabeltunneln åtkomlig; sätt eventuellt en tunn dragtråd genom den så att en framtida kabel kan träs utan att demontera. Dra inte in den för tjocka manteln. När både touchplate- och X-brytarkabelns verkliga ytterdimensioner är kända: prova att båda får plats samtidigt utan att nypas eller skavas. Om inte, välj en skyddad yttre kabelväg eller tunnare ledning. Ledningar ska vara isolerade och avlastade, särskilt där de lämnar Core.
6. Rikta X-motorns 16T-remhjul med den inbyggda remguiden på Cores baksida. Dra först stoppskruven mot motoraxelns plana sida, sedan den andra. Använd gänglåsning enligt V1E. Montera motorn med M3-skruvar. **Lägg i den grovkapade X-remmen (minst 1029 mm, märkt `X`) redan nu**, runt remhjulet. V1E rekommenderar det eftersom det sparar arbete senare. Ändarna fästs i kapitel 5. Dra alla ledare tillsammans uppåt bakom motorn, utan att de kläms, och fäst dem överst på Core.
7. Montera löphjulen (*idlers*). Tryck in M5-muttrarna med en flat skruvmejsel eller spetstång. Skruva i M5-skruvarna genom hålen i Cores ovansida. De ska bara nå in i låsmutterns nylondel – **inte klämma lagren**. Löphjulen ska rotera helt fritt, och X-remmen ska gå mellan dem och remhjulet.

**Kontroll A – godkänd Core:** använd den nya omprintade Core. Alla lager roterar fritt; rätt fäste sitter plant; X-brytarkabeln är skyddad; de två övre spännskruvarna är fortfarande lösa; remhjul sitter i linje. **Den tidigare utskriftsförskjutningen får inte finnas i delen som används.**

## 2. Montera YZ_Min och YZ_Max (balkens två ändar)

Originalbilder: [YZ Plate Assemblies](https://docs.v1e.com/lowrider/#yz-plate-assemblies).

1. Märk motor- och brytarkablar före dragning. Märk ledarna, inte kontakterna, så att kontakterna fortfarande passar i Jackpot3 och etiketten syns utan att du drar ur något. Framifrån maskinen används normalt vänster **Y0/Z0** och höger **Y1/Z1**. Kontrollera sidorna mot originalbilderna och aktuell LR4-konfiguration. Byt inte etiketter för att få en felkopplad motor att gå åt rätt håll. **Varje motorkabel är 1 m från fabrik och kapas aldrig.** Prova kanalpassningen med en kort kabelände. Lägg sedan en **märkt dragtråd per brytare** genom de kanaler som blir svåra att nå. Dra inte fem kablar från samma rulle samtidigt; de separata längderna mäts och kapas en i taget i kapitel 6 när maskinen är sammanbyggd. En redan kapad kabel får användas efter räckviddsprov.
2. Fäst Z-brytaren på hållaren `ZStop_Min`/`ZStop_Max` med M2,5-skruvarna. **Armen ska peka bort från den plana sidan**, enligt V1E:s bild. Muttern trycks in från YZ-plattans framsida. För kabeln genom kanalen och hela vägen ut genom plattans underkant. Fäst Z-stoppet löst med en M5-skruv och mutter i **lågt läge**. Det justeras i steg 9.
3. Placera Y-motorns 16T-remhjul med YZ-plattans inbyggda guide. Dra stoppskruven mot axelns plana sida först och använd gänglås. Motorn ska sitta på den **fasade sidan (brytarsidan)**, med kabeln närmast kanalen, och kabeln ska gå in på hålets bredare del. Fäst motorn löst med två M3. Bygg framhjulet med skruvhuvudena utåt eller nedåt och dra de stora skruvarna utan att klämma plasten. Framhjulet fäster med de två sista M3-skruvarna i motorn, och sedan dras alla fyra. Lägg delarna på ett plant bord med hjulen utanför kanten, så att YZ-plattans och hjulets ytterytor ligger i plan innan du drar.
4. Tryck in båda M5-muttrarna för löphjulen och håll dem på plats med M5-skruvarna tills vidare. **Y-remmen:** ta den grovkapade remmen (minst 1735 mm, `Y0` respektive `Y1`) och lägg den runt remhjulet. En pincett eller liten skruvmejsel hjälper. Ta gärna ur M5-skruvarna igen så går det lättare. Sätt tillbaka löphjul och M5-skruvar så att remmen går *löphjul → remhjul → löphjul*. Skruvarna ska sitta, men varken plasten eller lagren får klämmas. En droppe lätt olja i löphjulens lager förlänger livslängden. Remmen följer med maskinen, och dess ändar fästs på bordet först i kapitel 5. Tills dess hänger de löst. **Vik dem inte skarpt.**
5. Montera Y-brytaren med M2,5 och **armen utåt** för standardläget **Y-min** (bakre brytarläget är bara för hemkörning mot Y-max och kräver ändrad konfig). Skydda den utskjutande armen när plattan läggs på bordet – den böjs lätt. Trä ledarna i *wire keeper* en i taget, **först de tunna brytarledarna och sist motorkablarna**, som håller de andra på plats. Bänd inte i fliken; tryck in ledarna med en insexnyckel eller skruvmejsel. Ta bort eventuell strumpa på motorkablarna. Alla ledare ska till plattans baksida och ut genom spåret där, en i taget, och buntas sedan. **Kontrollera att vår Ø4 mm-brytarkabel ryms i kanalerna** (den ryms inte i Core). Tvinga den inte.
6. Dra Z-motorkabeln ut genom den bakre kanalen. Notera från vilken sida den går in i hålet. Montera 5→8 mm-kopplingen med guiden på YZ-plattans ovansida, på **den minsta, yttersta linjen**. Z-motorn ska sitta på brytarsidan. Stoppskruven mot den plana sidan dras först, med gänglås. Starta alla fyra M3-skruvar innan du drar någon av dem.
7. Rensa skenbäddarna från plastklumpar genom att skrapa med skenans vassa kant. Skruva dit MGN12-skenorna löst, så att skruvhuvudena ligger strax under skenans yta. Se upp för skruvhuvuden som sitter snett. Fäst XZ-plattan i vagnarna med M3: **XZ_Max har det stora hålet, XZ_Min har spåret upptill.** Dra sedan skenorna stegvis och **för XZ-plattan genom hela rörelsen efter varje åtdragning**. Lossa och dra om vagnarnas skruvar till sist, eftersom det ofta ger jämnare gång.
8. **T8 (längd först fysiskt verifierad och sedan kapad enligt kapitel 0):** stick in fabriksänden i kopplingen **ända ner tills den ligger an mot motoraxeln**. Dra båda stoppskruvarna, med gänglås. Smörj spindeln lätt. Tryck in mässingsmuttern i `Z_Nut` och fäst den med 1–2 M3. Använd tång vid trång passning. Skruva på den på spindeln **med mässingssidan nedåt**. `Z_Stub` får två dolda M5-muttrar som trycks i botten; en M5 genom XZ-plattan kan dra dem på plats. Fäst `Z_Stub` med två M5. **Z_Stub ska vara vinkelrät mot spindeln.** Vrid muttern upp och ned med fingrarna, med lätt tryck på metallplattan: den ska gå lätt. Lämna tvärspännskruvarna ute; de flesta använder dem inte.
9. Bygg bakhjulen med skruvhuvudena utåt eller nedåt. **Förgänga låsmuttern på skruven en eller två gånger** innan montering, så att nylonet mjukas upp. Tryck in den dolda M5-muttern, och om du känner motstånd: kontrollera att den inte går snett. Hjuldelarnas ytterytor ska ligga i plan, annars står balken snett mot bordet. Justera till sist Z-brytarna så att de utlöses **strax innan lagervagnarna når det övre stoppet**, på båda sidor. Mät utlösningsläget från en fast punkt, så går Z-nivelleringen snabbare senare.
10. Slutmontera inte steg 8 med obekräftad T8-längd. Prova först på en sida i taget enligt kapitel 0; en 400 mm-spindel kan inte slutmonteras på båda sidor samtidigt.

**Kontroll B – båda sidor:** när gängspindeln vrids för hand ska XZ-plattan gå jämnt utan punkt där den nyper; två sidors montage är spegelriktiga, inte två identiska kopior; alla fem brytarkablar kan identifieras. Om Z nyper: undersök skenans bädd, parallellitet, vagnarnas skruvar och Z_Stub före hårdare åtdragning.

## 3. Bygg balken med temporära stag

Originalbilder: [Beam Assembly](https://docs.v1e.com/lowrider/#beam-assembly).

1. Lägg ut **två X-rör à 816 mm**. Ändbracen (`Brace_Max` och en `Brace`, 60 % infill) placeras där de temporära stagen ska sitta. Övriga `Brace` fördelas med **lika avstånd** och snäpps fast på rören. Rören får inte sticka ut förbi ändbracen: yttermåttet över bracen ska stämma med stagmåttet **819 mm**.
2. Tryck in X-remspännarens mutter **helt i botten** i ändbracen. Använd gärna skruven för att dra den på plats, och **skruva sedan ur skruven igen**. Den används när X-remmen spänns i kapitel 5.
3. Sätt i **fyra printade Temp Strut, 15 % infill**: två fram och två undertill, med respektive orientering och hålbild enligt originalbilderna.
4. Dra stag-/rörklämmorna **försiktigt**: de ska bara börja gripa. Det är inte meningen att pressa ihop plastklämmorna eller låsa rören genom mycket stor skruvkraft. Enligt V1E ska rören fortfarande gå att vrida om man tar i. Rören bär ingen sidolast, och överdragning skapar bara problem.

**Kontroll C – balk:** båda rören är raka och parallella; ändstagen sitter rätt; inget rör sticker ut; printarna har inga sprickor. Detta är ett *temporärt* monteringsläge – fräs de permanenta stagplattorna senare med själva maskinen.

## 4. Sätt ihop huvudmaskinen och kontrollera geometrin

Originalbilder: [Main Assembly](https://docs.v1e.com/lowrider/#main-assembly).

1. Fäst **YZ_Max** i balken med tre skruvar. Håll skruven med mejseln, dra muttern med nyckel, och dra bara tills förbandet sitter – krossa inget. Skjut därefter försiktigt på Core utan att klämma en enda kabel. Avsluta med **YZ_Min**.
2. Justera de två övre Core-skruvarna i mycket små steg **endast om Core glappar**. Den ska rulla längs hela X utan att nypa vid stagpunkterna. För hård spänning riskerar att spräcka Core.
3. Kontrollera att **nedre X-röret inte ligger an mot någon XZ-metallplatta**. Vid kontakt: stoppa och undersök rörlängd och balkens geometri.
4. Ställ balken ungefär vågrätt genom att vrida Z-skruvarna för hand. Mät avståndet mellan **YZ-plattornas** främre respektive bakre sidor (*heel–toe*). Mät inte mellan hjulfästena. Måtten ska vara så lika du kan få dem; justera tillfälliga stag/änd-`Brace` innan fortsatt montering.

**Kontroll D:** Core går friktionsfritt, båda Z-sidorna kan höjas och sänkas utan bindning, och fram-/bakmått är lika inom mätosäkerheten. Fotografera gärna måtten och notera dem i byggloggen.

## 5. Montera bordets Y-styrning och remmar

Originalbilder: [Belts](https://docs.v1e.com/lowrider/#belts).

**Gör kabel-/slangprovet i kapitel 6 före steg 4–7 nedan.** Remmarna är redan trädda i vagnarna, men ändarna behöver ännu inte vara fastspända.

1. Kontrollera bordets underrede en gång till. Lägg ut maskinen på den köpta **1800 × 1000 mm**-skivan och provmarkera layouten. **941 mm** är yttermåttet tvärs över (X) från remhållarnas ytterkant på ena sidan till ytterkanten på andra sidan. **1563 mm** är yttermåttet på längden (Y), från Y_Max-hållarnas ytterkant till Y_Min-hållarnas ytterkant. Lägg inte till någon gammal 90 cm-kantbreddning. Rita gärna en centrumlinje för skruvhålen längs bordet.
2. Montera **den enda Y-styrskenan** som rak referens, parallellt med vald bordskant. När den väl sitter är det skenan som är referensen. Den andra sidan har Y-rem men ingen andra styrskena. Y-remhållare och `Y_Clip` använder samma yttre referens. Förborra så att plastdelarna ligger plant; en extra vässad blyertspenna märker ut hålen. Clipsen har cirka ±1,5 mm spel. Avstånd mellan Y-clips: **högst 300 mm centrum–centrum**.
3. Montera först båda Y_Max-hållarna och de första/sista clipsen direkt intill remhållarna i båda ändar. Mät sedan luckan och fördela övriga clips jämnt. Sätt clipsen på skenan och skruva fast ett i taget mot en rak kant (bordskant eller vattenpass). **Skruva i en M3 helt i båda Y_Min-hållarna**: den är grovjustering för Y-squaring. Y_Min-hållarna är snabbkopplingar, så maskinen kan lyftas av bordet. Ställ in Y-stoppskruven så att brytaren utlöser **strax innan** maskinen når änden. V1E får cirka 4 mm extra rörelse efter utlösning.
4. **Y-remmarna (1735 mm):** lägg remänden runt en M3 och dra i remmen så att skruven sätter sig och låser remmen. Remänden ska sticka igenom med några tänder, likadant för alla remmar. Förbered Y_Max-spännaren genom att sänka muttern och sätta i skruven, med **nyloc närmast den smala änden**. Lås remmen med M3 på samma sätt. **Här bestämmer du var på remmen M3-slingan hamnar, och det ger grundspänningen.** Det kan ta ett par försök. Kontrollera att remmen ligger på remhjulet och i båda löphjulen. V1E:s riktvärde för längsgående remkraft är **cirka 31 N (7 lbf)**; det är inte en instruktion att hänga 3,2 kg mitt på remmen eller ett skruvmoment. Remmen ska vara sträckt men går inte att knäppa som en gitarrsträng. Börja hellre för löst än för hårt: delarna går sönder långt innan remmen gör det. Gör likadant på andra sidan.
5. **X-remmen (1029 mm, redan i Core):** linda ena änden runt en M3, nyp remmen mot metallplattan (XZ) medan du matar in den, och tryck ned remmen och skruven i botten med en skruvmejsel. Lägg andra änden i X-remspännaren (`X_Belt`) och ställ in rätt avstånd. Flytta Core **långsamt för hand** och kontrollera att remmen ligger rätt på remhjul och löphjul. Använd samma försiktiga riktvärde för längsgående remkraft; dra inte åt för att kompensera för sned geometri.
6. Kontrollera att inget av Y-stoppens skruvar kan passeras av brytararmen; en passerad skruv kan knäcka armen. Om armen missar kan du böja ut fliken lite så att den tar tidigare.
7. **Putsa remändarna:** först när alla tre remmar är rätt spända, efter en kort provkörning för hand, kapar du överskottet så att det sticker ut några tänder förbi varje M3-lås. Spara remresten (cirka 500 mm). Anteckna den slutliga fria remlängden i byggjournalen.

**Kontroll E:** ingen rem vandrar på ett löphjul; fram/bak återkommer Y-brytarnas armar till samma mekaniska referens; skivan/underredet rör sig inte när maskinen belastas lätt. Spänn inte hårdare för att ”lösa” ett geometrifel.

## 6. Kabeldragning – vår placering skiljer sig från originalet

Originalbilder: [Wire Routing](https://docs.v1e.com/lowrider/#wire-routing) och [Jackpot3 Wiring](https://docs.v1e.com/electronics/jackpot3/#wiring). **Kap- och mätprotokoll för vårt bygge:** [CABLE_ROUTING.md](../CABLE_ROUTING.md).

**Ordning:** V1E drar kablarna *innan* remmarna fästs. Core-kablarna och slangen är mycket lättare att prova i båda ytterlägena innan X-remmen är låst (kapitel 5 steg 5). Gör provdragningen här före kapitel 5:s slutliga remspänning.

- **Jackpot3-lådan:** i rätt printad låda på balkens YZ_Min-sida, i första facket, som ger enklast dragning och åtkomst till SD-kortet. Lämna fri luft runt kort och antenn. Dra ledare bredvid, aldrig ovanpå, kortet eller antennen. Överskott buntas på lådans sidor, inte i den. Dragavlasta allt innan kablarna lämnar lådan.
- **Aggregatet på balken:** 230 V NVR/maskinstopp placeras fast och lättåtkomligt på bordet. **Rörligt:** Jackpot3 och, efter lämplig kontroll av kapsling och infästning, Mean Well HDR-60-24 på balken. V1E:s bild av ett annat aggregat på hose hooks är **inte en monteringsanvisning för vårt DIN-aggregat**. HDR ska fästas och ventileras enligt sin installationsmanual, även under första provet. Kontrollera att inga nätspänningsförande plintar är åtkomliga. Anslut Jackpot3 till HDR med kort 24 V-kabel på balken, med lite arbetsmån. Den redan köpta 3 m 2×20 AWG-kabeln är reserv; dra inte en lång 24 V-slinga utan behov.
- **YZ-sidornas kablar:** ställ **balken i högsta Z-läget** och dra kablarna från YZ-plattorna in i balken. Fäst dem vid varje brace med buntband eller tejp, överst eller underst på bracen. Kör balken upp och ned: kablarna ska ha slack i alla lägen. **Förlängningar behövs från YZ_Max (Y1, Z1) och från Core (X)** i V1E:s standardbygge, eftersom motorkablarna inte når över hela balken till Jackpot3. Bekräfta på en minut vid provdragningen: når 1 m-kontakten inte Jackpot3 med marginal i ytterläget, behövs förlängning. Köp efter det provet. V1E:s BOM listar tre motorförlängningar; **exakt längd för vårt bygge är inte verifierad**. Välj efter uppmätt underskott och matcha både kontakt och ledarordning. Kontrollera kontakttypen innan du köper. Vik ledarna vid skarven så att själva kontakten ligger rak, tejpa så att dragkraften tas av tejpen och inte av kontakten, och märk både skarven och förlängningens ände. Dra fram till Jackpot3 och koppla in. **Överlängd på motorkablar kapas inte:** dra all slack till balkens bortersta fack, vik den fram och tillbaka och bunta ihop den.
- **Core-kablarna och slangen:** flytta Core ända till **X_Max** (YZ_Max-plattan). Fäst kablarna i första läget överst på Core. Sätt i `Hose_Hook`-delarna: de långa där slangen rör sig, de korta på mitt- och ändbrace. Lämna en **liten slinga vid X_Max** och fäst kablarna vid bracen strax förbi balkens mitt. Därifrån går de in i balken med övriga kablar till Jackpot3. Buntas enklast ihop med fräsens nätkabel, med lite lös kabel vid fräsen för justering i fästet. Slangen kopplas till dammskon och upp till det andra fästhålet ovanpå Core, och fästs sedan vid mittbracen och hose hook. Kablarna går **under** slangen vid mittläget, aldrig över, och fästs mot slangen strax efter varje hose hook. En halv vridning av bunten får den att spåra rätt. Kontrollera att Core når båda ändar utan att dra i något och att slangen inte faller över fram- eller bakkanten.
- **Mellan fast och rörligt:** nätmatningen till HDR-60-24 och fräsens kabel behöver säker rörlig dragning och dragavlastning, antingen tillsammans med slangen eller som en enda skarvsladd in i balken (V1E:s tips). Låt slangupphängningen ta slangens vikt, inte Z-vagnen.

### Var kapar jag brytarkablarna? – mät och märk

Det här avsnittet gäller enbart de fem brytarkablarna. Kort 24 V-kabel och eventuell touchplate-ledning mäts separat; motorkablarna lämnas hela. Kapstället är alltid **vid Jackpot3-änden** och bestäms med maskinen monterad, i det läge där ledningen behöver som mest längd. V1E anger inga kapmått, eftersom de beror på den verkliga kabelvägen. Därför står inget fast mått här. **En rulle har bara en fri ände:** använd dragtrådarna från Core/YZ-montaget och färdigställ en kabel i taget. Mät först alla fem rutter med snöre inklusive slingor, anslutningar och marginal; kontrollera att summan ryms i kvarvarande kabel. Börja sedan med X:

1. **Brytaränden först:** anslut COM + NC vid brytaren, isolera den tredje ledaren och märk kabeln (`X`, `Y0`, `Y1`, `Z0`, `Z1`) i båda ändar. Låt andra änden sitta kvar på rullen.
2. **Ställ maskinen i det läge som kräver mest kabel:** för `X` står Core vid **X_Max**, längst från Jackpot3. För `Y0/Z0/Y1/Z1` står balken i **högsta Z-läget**.
3. **Lägg kabeln längs den slutliga vägen:** den ska vara fäst vid varje brace, med `X` i slingan vid Core enligt punkten ovan. Den ska ligga slakt men utan onödiga öglor.
4. **Vid Jackpot3:** för fram kabeln till sin ingång och lägg till cirka **10–15 cm arbetsmån**. Det är en startpunkt, inte garanterad marginal; anpassa efter böjradie, dragavlastning och eventuell pigtail. **Sätt en tejpflagga där. Där kapar du.**
5. **Kontrollera före kap:** flytta till motsatt ytterläge (Core vid X_Min, balken i lägsta Z) och sedan tillbaka. Ingenting får spännas, och kabeln får inte nå remmarna. Kapa först därefter och fortsätt med nästa ledning från rullen.
6. **Anteckna** den kapade längden i [CABLE_ROUTING.md](../CABLE_ROUTING.md).

**Rimlighetskontroll, inte kapmått:** de tre långa ledningarna (X, Y1, Z1) går ungefär över hela balken (stagmått 819 mm) plus uppgång och slinga. Y0 och Z0 är korta, eftersom Jackpot3 sitter på samma sida. Detta bevisar inte att 10 m räcker: kontrollera summan av de fem uppmätta längderna innan rullen fördelas. Om 250 cm redan är kapat till X: prova om biten räcker enligt punkt 2–5 innan du kapar mer.

**Kontakter vid Jackpot3:** stegmotoruttagen är öppna stifthuvuden med 2,54 mm delning (V1E). Kontrollera brytaringångarnas kontakttyp på själva kortet. BOM innehåller bara **3 × 2-poliga 150 mm-pigtails för fem brytare**. Bestäm hur de två sista ska anslutas (krimpkontakt eller pigtail) innan kapitel 7. Det är en öppen punkt, inte löst.

**Full-travel-kontroll innan permanenta buntband:** prova samma montage samtidigt med HDR:s nätmatning, kort 24 V-förbindelse, motor-/brytarkablar, fräsens nätkabel och dammsugarslang. Kör för hand till alla fyra hörn och Z:s båda ytterlägen. Inget får sträckas, vikas hårt, falla i remmarna eller dra i en kontakt.

## 7. Jackpot3: lågspänning och programvara

Original: [Jackpot3 – Initial Setup, Tests och Firmware](https://docs.v1e.com/electronics/jackpot3/).

1. Kontrollera kortets märkning mot **Elecrow Jackpot3 `CQA240812C2`**. **Både 24 V och USB ska vara frånkopplade innan någon motor-/brytarkontakt flyttas.** Innan vårt HDR-aggregat spänningssätts ska kapitel 8:s nätmatningskontroll vara godkänd; firmware kan förberedas via USB enligt V1E. Använd inte Jackpot 1/2:s kopplingsbild eller konfigurationsfil.
2. **Inventera** dataförande USB-C-kabel och ett microSD-kort större än 2 GB, FAT32. Köp bara det som faktiskt saknas.
3. Hämta den **för tillfället V1E-testade** FluidNC-versionen, WebUI-versionen och *Jackpot3 + LowRider 4*-konfigurationspaketet från ovanstående källor. Dokumentationen anger vid guideupprättandet FluidNC **3.9.9** och WebUI **V3**; kontrollera på nytt före installation. Ett kort från Elecrow ska **inte antas vara förkonfigurerat** bara för att V1E säljer färdigflashade kort.
4. Om installation behövs: **bryt huvudmatningens 24 V innan USB-C ansluts** och följ V1E:s webbaserade installation. Ladda sedan upp rätt `config.yaml` och de makron som hör till samma paket. Spara en kopia av filerna före egna ändringar. Kontrollera konfigurationens rörelse- och homingsträckor mot vår mindre maskin och faktiskt Z-slag; en standardfil kan avse ett större bygge. Arbetsytan 650 × 1250 mm är inte i sig ett verifierat värde för varje `max_travel_mm`. Dokumentera verkliga gränser innan större joggningar eller homing; prova inte en fullstor standardrörelse på chans.
5. Koppla de fem motorerna och fem normalt slutna brytarna enligt den aktuella **Jackpot3-LR4-kopplingsbilden**. För varje mikrobrytare används **COM + NC**, och respektive signal/jord ska stämma med märkt ingång. Gissa inte stiftordning eller motorns par utifrån kabelfärg.
6. Låt den som verifierar nätinstallationen kontrollera 24 V-utgångens verkliga spänning och polaritet utan Jackpot3 anslutet; märkningen ensam är inte en mätning. Höj inte spänningen över Jackpot3:s angivna 24 V för att få mer motorkraft. Bryt matningen före anslutning. Slå sedan på endast styrningens verifierade matning. Fräsens nätkontakt ska vara urdragen och ingen fräs sitta monterad. Anslut enligt dokumentationen till **FluidNC**-nätet och öppna **http://192.168.0.1** om standardåtkomst fortfarande gäller.
7. Kontrollera `$SS` (uppstartsmeddelanden). Testa var och en av brytarna med `$Limits` i terminalen; avsluta med `!`. Verifiera för varje brytare både vila, tryck och återgång på rätt ingång; notera kopplingen X/Y0/Y1/Z0/Z1. Ingen homing om en ingång redan är utlöst eller inte återgår. **Brytarna används för homing/autosquaring, inte som garanterade stopp under körning.**
8. Joggning: börja med **1 mm**. Sett framifrån: X+ höger, Y+ bortåt och Z+ upp från arbetsytan. Stoppa vid fel riktning och bryt **både 24 V och USB** innan motoranslutningar ändras; verifiera rätt kontakt/config före ny provkörning. Testa sedan axlar var för sig med större men fortsatt fria rörelser.
9. När alla riktningar och brytare verifierats: prova homing med fri rörelseväg, beredd att bryta matning om något går fel. Ändra `pulloff_mm` först utifrån uppmätt avvikelse; spara ändringen i konfigurationen och enligt V1E:s WebUI-makro, starta om och verifiera att inställningen finns kvar.

**Kontroll F – styrning:** rätt modell, fungerande start utan konfigurationsfel, fem identifierade motorer och fem verifierade brytare, 1 mm-rörelser i rätt riktning. **Inga påhittade pin-nummer eller firmwarevärden** skrivs in i den här guiden; aktuell V1E-konfig och kortets märkning är facit.

## 8. 230 V, maskinstopp och damm – separat säkerhetsgräns

Se [AUDIT](../AUDIT.md) och [CHECKLIST](../CHECKLIST.md). Detta är vår projektspecifika elarkitektur; inte en del av V1E:s standardschema.

- **NVR är ännu en vald funktionsprincip, inte verifierad inkoppling.** Välj faktisk 230 V-enhet efter dess terminalschema och märkström. Placera stoppet direkt nåbart. Skydda aggregatets nätspänningsplintar även på balken; kapsling, genomföringar, infästning och dragavlastning dimensioneras efter de verkliga delarna.
- **HDR-60-24 är klass II och har ingen PE-plint.** Anslut inte slangjord till −V, en godtycklig skruv eller DIN-skenan. Följ [Mean Wells datablad](https://www.meanwell.com/Upload/PDF/HDR-60/HDR-60-SPEC.PDF) och [HDR-installationsmanual](https://www.meanwell.com/Upload/PDF/HDR%20DIN%20rail%20power%20supply.pdf): rätt DIN-infästning, monteringsriktning och ventilation (5 mm på sidorna, 40 mm över och 20 mm under). Behörig/kompetent person verifierar nätinstallationen och eventuell separat jordpunkt; en enkel summermätning bevisar inte elsäkerhet.
- Skyddsjord (PE), där den används i installationen, ska vara obruten och inte gå genom NVR-brytaren. Kontrollera PE-kontinuitet och att ingen kortslutning finns mellan L/N och PE före spänningssättning. Låt en elkunnig fackperson verifiera nätspänningsinkopplingen före första spänningssättning.
- Prova NVR:s *no-restart*-funktion **med fräsen frånkopplad**: efter avbrott får återkommen nätspänning inte starta lasten automatiskt. Kalla inte lösningen ett säkerhetsklassat nödstopp.
- Provpassa KATSU-hylsan och kontrollera synlig excentricitet/mät runout innan skärande körning. Dra ur kontakten vid fräsbyte.
- **Jorda slangen:** V1E kräver att dammslangen jordas i ena änden, annars byggs statisk laddning upp som kan skada styrkortet. Vår poolslang leder inte. V1E:s lösning för icke-ledande slang är en oisolerad tråd genom slangen, fäst i ena änden och jordad i den andra. Låt elkunnig person bedöma en separat jordpunkt och mekanisk infästning så att tråden inte kan sugas in eller fastna. HDR är ingen jordpunkt.
- Bygg dust shoe, avlastad slang, cyklon och styv behållare. Kontrollera behållaren med kontrollerat vakuumtest. Verifiera statisk jordväg innan återkommande MDF-/trä-/XPS-arbeten.

**Stoppregel:** Ingen körning med roterande verktyg om kabelslingan, fräsens infästning, stoppfunktionen eller arbetsstyckets fastspänning är oklar.

## 9. Första rörelserna, måttkontroll och permanenta stag

Original: [Initial Calibration](https://docs.v1e.com/lowrider/#initial-calibration) · [Making the Strut plates](https://docs.v1e.com/lowrider/#making-the-strut-plates) · [Temp to Custom Strut Plates](https://docs.v1e.com/lowrider/#temp-to-custom-strut-plates).

1. **Torrkör utan fräs först.** Lägg ett skyddande offermaterial under de första genomskärningarna redan nu; slutlig planfräsning görs senare. Kontrollera CAM-enheter (mm), arbetsnollpunkt, säker Z-höjd, maxdjup och hela verktygsbanan inklusive klämmor i en luftkörning. KATSU startas/stoppas manuellt i detta bygge; ett M3/M5-kommando är inget bevis på att fräsen startar/stannar. Verifiera hela driven rörelsevägen och kablarnas/slangens frigång. Kör sedan enkla, små provjobb i billigt material under uppsikt när säkerhetskontrollerna är godkända.
2. **Kalibrera mått.** (Protokoll och logg: [`CALIBRATION.md`](../CALIBRATION.md).) Mät en känd lång X- eller Y-förflyttning, helst märken nära varsin ände. Vid fel: nytt `steps_per_mm = gammalt steps_per_mm × (begärd sträcka / uppmätt sträcka)`. Justera värdena för X/Y enligt V1E och kontrollera resultatet med ny mätning. Ändra inte andra motorinställningar godtyckligt.
3. **Räta upp Y.** Gör fyra tydliga markeringar som en rektangel, mät båda diagonalerna och justera Y-sidornas homing/pull-off enligt V1E. V1E beskriver under 1 mm diagonalskillnad som mycket bra på stor maskin; anpassa kontrollstorleken till vår mindre arbetsyta. Mät om efter varje ändring.
4. **Nivellera Z.** Jämför fräshöjd mot bordet nära båda ändar; mät flera gånger och justera respektive Z-brytares `pulloff_mm` (aldrig under 4 mm; godkänt under 0,5 mm skillnad mellan sidorna). Spara och kontrollera efter omstart. Detta måste upprepas när permanenta stag monterats.
5. Generera de två permanenta stagplattorna med **`strut_length=819` och `front_wing_size=30`**. Använd fram- och bottenplatta; 5–6 mm styv MDF/hårdboard, **högst 6,35 mm**. Kontrollera CAD/SVG mot vår geometri. Importera med **millimeter**. Generatorn gör plattan cirka 0,5 mm kortare avsiktligt; skala inte upp den för att kompensera. **Långsidan måste ligga längs Y:** cirka 819 mm ryms inte i våra 650 mm X. Verifiera hela verktygsbanans yttergränser, med fräsradie och hållflikar, inom faktiskt provat rörelseområde innan start.
6. Fräs **en platta i taget** och kontrollera måtten innan nästa. Hål före ytterkontur; skär yttersidan av konturen och lämna hållflikar så detaljen inte lossnar. Kontrollera verklig materialtjocklek, nollpunkt och att skruvar/klämmor ligger utanför verktygsbanan.
7. Byt plattor enligt V1E: ta av och bind undan X- och Y-remmar; ta bort de fyra temporära stagen; lossa/lyft Core enligt originalbilderna; montera främre permanent platta, återmontera Core och montera nedre plattan. Dra först alla skruvar löst och därefter jämnt. **Kläm inte ihop Brace-delarna.**
8. Gör om heel–toe-mätningen fram/bak på YZ-plattorna; kontrollera även övre/nedre bredd och fri Z-rörelse. Sätt åter remmarna och verifiera Y-stoppens läge, diagonal och Z-nivå igen.
9. Montera löstagbar **cirka 12 mm MDF-offerskiva** på arbetszonen och planfräs den *först nu*, med den färdiga balken. Kontrollera därefter X/Y-mått, Z-djup och ett enkelt kalibreringsprov. Spara den fungerande `config.yaml` utanför kortet.

**Kontroll G – färdig maskin:** kalibreringsprovet håller avsedda mått, Z går fritt, båda remmarna ligger rätt, fräsens kabel och slangen fungerar över hela arbetsytan, och offerskivan är planfräst. Maskinen är inte godkänd enbart för att den går att jogga.

## Arbetsordrar för kvällspass

Välj ett cirka en timme långt pass i [arbetsordersystemet](https://kingkongola.github.io/lowrider/#ordrar) eller [WORK_ORDERS.md](../WORK_ORDERS.md). Varje order har eget ID, beroenden och rapportmall. Lokal status på webbsidan uppdaterar inte SSOT förrän användaren rapporterat resultatet.

## Snabb felsökning vid montering

| Symtom | Kontrollera först |
|---|---|
| Ett 608-lager eller en idler går trögt | För hårt dragen lageraxel; lager snett i sitt säte |
| Core rullar ryckigt över stagpunkterna | Övre spännskruvar för hårt dragna; rörparallellitet |
| Z kärvar på en sida | Skenbädd, skenornas inbördes riktning, vagnskruvar, vinkeln hos `Z_Stub` |
| Maskinen vill dra snett när den är avstängd | Skillnad i fram-/bakbredd (heel–toe), ändstag och rörlängd |
| Y-brytarens arm missar stoppskruven | Y_Min-hållarens läge; risk att armen passerar och böjs |
| Jogg går åt fel håll | Stoppa och bryt all matning; jämför kontakt/config med V1E:s *Jackpot3*-schema |
| Brytare verkar inte fungera | Korrekt COM/NC, rätt fysisk ingång och utslag i `$Limits` |
| Wi-Fi svagt eller intermittent | Antenn skymd av kablar eller för mycket ledare över Jackpot3 |
| En rem räcker inte till M3-låset | Kontrollera först remväg, ändöglor, spännarens läge och bordets layout. 1735/1029 mm innehåller extra marginal; en kortare bit är inte automatiskt oanvändbar. Skarva inte drivremmen. Om den fortfarande inte räcker behövs en hel ny bit av rätt 10 mm GT2-rem |
| Delarna blir systematiskt för små | Börja med känd förflyttning och remkalibrering; anta inte att mer remspänning löser allt |
| Första fräsningen tar ojämnt djup | Kontrollera Z-nivå, inspänning och behov av planfräst offerskiva |

## Byggjournal – fyll i, anta inte

| Grind | Datum / resultat |
|---|---|
| Remmar kapade (Y0 / Y1 / X, mm) | ☐ |
| T8 kapad (2 × mm) | ☐ |
| A Core klar | ☐ |
| B YZ-sidor går lätt | ☐ |
| C temporär balk klar | ☐ |
| D heel–toe och Core | ☐ |
| E Y-styrning/remmar | ☐ |
| F Jackpot3, motorer och brytare | ☐ |
| Brytarkablar kapade (X / Y0 / Y1 / Z0 / Z1, cm) | ☐ |
| NVR/PE och full-travel | ☐ |
| G permanenta stag och kalibrering | ☐ |

Skriv faktiska mått, problem och ändrade beslut i [BUILD_LOG](../BUILD_LOG.md) eller [CHECKLIST](../CHECKLIST.md). **Den här guiden dokumenterar hur vi ska bygga; den uppdaterar inte automatiskt fysisk leverans- eller kontrollstatus.**
