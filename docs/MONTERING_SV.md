# LowRider 4 – svensk monteringsguide för vårt bygge

**Utgåva:** 2026-09-21 · **Status:** arbetsguide. Bocka inte av kontroller förrän de faktiskt är gjorda.

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
| Remmar | GT2 10 mm; planerat **999 / 1705 / 1705 mm**, **kapa först efter provdragning** |
| Motorer | 5 × STEPPERONLINE `17HS19-2004S1` |
| Styrenhet | **Elecrow Jackpot3 `CQA240812C2`**, mottagen; rätt Jackpot3-låda |
| Matning | Mean Well `HDR-60-24`, 24 V; planerat **på rörlig balk** tillsammans med Jackpot3, efter skydds- och infästningskontroll |
| Gränslägesbrytare | 5 × Omron `SS-3GL13PT`, normalt slutna (NC), anslut COM + NC |
| Handöverfräs | KATSU `101750`, 710 W, cirka 65 mm; Makita/65 mm-fäste |
| Fräsfäste/verktyg | Makita/Elaire 1/8-tumshylsa; provpassa före start |

**Placering efter omprövning (D016):** NVR/maskinstopp är fast och lättåtkomligt på bordet; Jackpot3 och vårt Mean Well HDR-60-24 planeras på balken enligt V1E:s princip. Vårt DIN-aggregat är inte automatiskt lämpligt för oskyddad balkmontering. Kontrollera beröringsskydd för nätplintar, jordning, kapsling, infästning och dragavlastning före anslutning. Köp inte alternativa komponenter bara för att V1E:s bilder visar en annan aggregatmodell.

**Läge 2026-09-21:** Alla tre 16T-remhjul har kommit fram enligt användaren; kontroll av deras tekniska mått kvarstår. Användaren har rapporterat utskrift av platta 14/14. Komplett utskriftsinventering, slutlig rör-OD och bordets styvhet är ännu inte markerade som fysiskt verifierade.

## 0. Förbered arbetsplatsen – före första skruven

Original: [utskrifter, geometri och montering](https://docs.v1e.com/lowrider/).

- [ ] Sortera HaWiWe: två 6 mm XZ-plattor, **4 × MGN12H 150 mm**, skruvsats och 1/8-tumshylsa. Provpassa M3×10 i skena/lagerblock/platta: ingenting ska bottna eller kärva.
- [ ] Inventera DigiKey-paketet mot [BOM](../BOM.md). Kontrollera 608-2RS-lager, mikrobrytare, kablar och anslutningar.
- [ ] Kontrollera utskrifterna: **30 mm-varianter**, Makita/65 mm-verktygsfäste, Jackpot3-låda, samtliga fyra temporära stag. Särskilt `Z_Stub`, `Z_Nut`, YZ-delarnas bryggor och Dust Skirt: inga skadade hål eller allvarliga överhängsfel.
- [ ] De tre 16T-remhjulen är mottagna 2026-09-21. Kontrollera tandantal, 5 mm axelhål och passning för 10 mm GT2-rem innan montering.
- [ ] Ordna handverktyg, skjutmått, rätvinkel, måttband, liten rak linjal, märkpenna och märkningstejp. Använd handverktyg för skruvförbanden; dra inte sönder printarna med skruvdragare.
- [ ] Kontrollera bordets underrede för glapp och vridning. Markera **941 × 1563 mm** minsta footprint, samt utrymme för två Y-remmar och kabelslinga. Skruva inte i skivan innan layouter och rörelsezoner stämmer.
- [ ] Mät verklig ytterdiameter, rakhet och användbar längd hos Motonet-rören **före kapning**. Kapa först efter kontroll till 816 + 816 + 1505 mm och grada ändarna.

**Stoppregel:** Om en rördel är fel diameter, om printade passningar är skadade eller om en skena binder utan belastning: rätta detta innan du bygger in felet. Den tidigare observerade cirka 0,20 mm utskriftsförskjutningen är inte i sig ett bevis för felaktig funktion; provmontera och kontrollera berörda hål/passningar.

## 1. Montera Core (X-vagnen)

Originalbilder: [Core Assembly](https://docs.v1e.com/lowrider/#core-assembly).

1. **Lageraxlarna, bild `ca.jpg`–`cc.jpg`:** Ta fram **8 × 608-2RS (8×22×7 mm)** från DigiKey, **8 × M8×40 sexkantsskruvar** och **8 × M8 nyloc** från HaWiWe. Montera de första **tre paren (6 lager, 6 skruvar och 6 muttrar)**, två i taget enligt `ca.jpg`, `cb.jpg` och `cc.jpg`. Sätt ett lager i varje visad ficka och för varje M8-skruv genom lagrets 8 mm innerhål **åt det håll bilden visar**; montera en M8-låsmutter per skruv. Dra bara an tills skruvhuvudena ligger an. **Inget lager får nypa och ingen plast får deformeras.**
2. **Sista paret, bild `cd.jpg`:** montera resterande **2 lager + 2 M8×40 + 2 M8 nyloc** i bildens övre justerlägen. Dessa två är också lageraxlar, men fungerar dessutom som **Core-spännskruvar** mot X-rören. **Lämna båda lösa** tills Core har satts på balken; ingen slutlig spänning nu. Totalt i Core: **8 lager, 8 M8×40 och 8 M8 nyloc**. De återstående sex 608-lagren av V1E:s totalt 14 monteras senare i YZ-hjulen; två av dina 16 inköpta är reserv.
3. **Verktygsfästets muttrar, bilder `ce.jpg`–`ch.jpg`:** ta fram **4 × M5 nyloc** från HaWiWe och fyra korta PLA-filamentbitar. Tryck i en mutter per hål med nylondelen åt det håll `cf.jpg` visar. För in filamentet genom låshålen så att muttern hålls kvar; på motsatt sida vinklas filamentänden åt andra hållet (`cg.jpg`). Klipp alla fyra filamentbitar **jäms med Core**.
4. **Verktygsfästet, bilder `ci.jpg`–`cj.jpg`:** placera det printade **Makita/65 mm-fästet** plant mot Core och använd de **4 M5-fästskruvarna från HaWiWe-satsen** (satsen innehåller M5×30). Kontrollera faktisk gängingrepp och att skruvarna inte bottnar; originaltexten anger fyra skruvar, men specificerar inte uttryckligen deras längd för varje verktygsfäste. Starta alla fyra för hand utan att knuffa ut muttrarna, och dra sedan jämnt utan att spräcka plasten. **Köp inga andra skruvar innan dessa provpassats.**
5. Dra X-brytarens kabel och eventuell framtida probkabel genom avsedda tunnlar. Märk **X** på själva kabeln, inte bara på kontakten.
6. Rikta X-motorns 16T-remhjul med den inbyggda mätguiden på Core. Dra först stoppskruven mot motoraxelns plana sida, sedan den andra. Använd gänglåsning enligt V1E. Montera motorn och lägg i X-remmen när manualen anger det.
7. Montera löphjulen (*idlers*). Deras skruvar ska nå låsmuttern men **inte klämma lagren**.

**Kontroll A – godkänd Core:** alla lager roterar fritt; rätt fäste sitter plant; X-brytarkabeln är skyddad; de två övre spännskruvarna är fortfarande lösa; remhjul sitter i linje. Använd inte Core för att bedöma den observerade utskriftsförskjutningen förrän den rullar på riktiga rör.

## 2. Montera YZ_Min och YZ_Max (balkens två ändar)

Originalbilder: [YZ Plate Assemblies](https://docs.v1e.com/lowrider/#yz-plate-assemblies).

1. Märk motor- och brytarkablar före dragning. Framifrån maskinen används normalt vänster **Y0/Z0** och höger **Y1/Z1**. Kontrollera sidorna mot originalbilderna och aktuell LR4-konfiguration; byt inte etiketter för att få en felkopplad motor att gå åt rätt håll.
2. Fäst Z-brytaren på dess printade hållare med M2,5-skruvarna. **Brytararmen ska vara vänd enligt V1E:s bild**; för kabeln genom kanalen. Börja med Z-stoppet i lågt läge, justering sker senare.
3. Placera Y-motorns 16T-remhjul med YZ-plattans inbyggda måttguide; dra stoppskruven på axelns plana sida först. Montera motor och främre hjul, rikta deras ytterytor mot varandra på plan yta och dra jämnt.
4. Lägg Y-remmen genom remhjul och idlers såsom originalet visar. Den ska ligga korrekt i samtliga hjul, utan sneddragning. **Mät innan definitiv kapning.**
5. Montera Y-brytaren med armen utåt för standardläget **Y-min**. Skydda den utskjutande armen när plattan läggs på bordet – den böjs lätt.
6. Dra Z-motorkabeln genom plattan. Montera Z-motor och 5→8 mm-koppling enligt måttguiden; axelns plana sida får första stoppskruven.
7. Rensa skenornas printade bäddar från små plastklumpar. Skruva dit MGN12-skenorna löst; fäst XZ-plattan i vagnarna; dra sedan skenorna stegvis. **För XZ-plattan genom hela rörelsen efter varje åtdragning**. Lossa och dra om vagnarnas skruvar om det hjälper rörelsen.
8. Montera T8-skruv och T8×8-mässingsmutter enligt bilderna. Kontrollera full frigång och lägg på en liten mängd lämplig lätt smörjning. Montera Z_Stub – dessa ska vara vinkelräta mot gängspindeln. Lämna tvärspännskruvarna ute enligt originalet om de inte behövs.
9. Montera de bakre hjulen på båda YZ-sidorna enligt originalbilderna. Kontrollera att hjuldelarnas ytterytor ligger i plan; dra skruvarna utan att deformera plasten. Justera sedan Z-brytarna så att de utlöses **innan** vagnarna når sina mekaniska övre stopp.
10. **Kapa inte 400 mm T8-spindeln i två lika delar av slentrian.** Mät nödvändig frigång och fästlängd i den fysiska uppbyggnaden; cirka 150–160 mm per sida är vårt arbetsmål, inte verifierat kapmått.

**Kontroll B – båda sidor:** när gängspindeln vrids för hand ska XZ-plattan gå jämnt utan punkt där den nyper; två sidors montage är spegelriktiga, inte två identiska kopior; alla fem brytarkablar kan identifieras. Om Z nyper: undersök skenans bädd, parallellitet, vagnarnas skruvar och Z_Stub före hårdare åtdragning.

## 3. Bygg balken med temporära stag

Originalbilder: [Beam Assembly](https://docs.v1e.com/lowrider/#beam-assembly).

1. Lägg ut **två X-rör à 816 mm** och fördela `Brace` enligt V1E:s bilder. Kontrollera särskilt att de kraftigare änd-`Brace` har rätt placering. Rör ska inte skjuta ut förbi ändklämmorna.
2. Montera X-remmens spännarm och dess mutter enligt originalets riktning.
3. Sätt i **fyra printade Temp Strut, 15 % infill**: två fram och två undertill, med respektive orientering och hålbild enligt originalbilderna.
4. Dra stag-/rörklämmorna **försiktigt**: de ska bara börja gripa. Det är inte meningen att pressa ihop plastklämmorna eller låsa rören genom mycket stor skruvkraft.

**Kontroll C – balk:** båda rören är raka och parallella; ändstagen sitter rätt; inget rör sticker ut; printarna har inga sprickor. Detta är ett *temporärt* monteringsläge – fräs de permanenta stagplattorna senare med själva maskinen.

## 4. Sätt ihop huvudmaskinen och kontrollera geometrin

Originalbilder: [Main Assembly](https://docs.v1e.com/lowrider/#main-assembly).

1. Fäst **YZ_Max** i balken. Skjut därefter försiktigt på Core utan att klämma en enda kabel. Avsluta med **YZ_Min**.
2. Justera de två övre Core-skruvarna i mycket små steg **endast om Core glappar**. Den ska rulla längs hela X utan att nypa vid stagpunkterna. För hård spänning riskerar att spräcka Core.
3. Kontrollera att **nedre X-röret inte ligger an mot någon XZ-metallplatta**. Vid kontakt: stoppa och undersök rörlängd och balkens geometri.
4. Ställ balken ungefär vågrätt genom att vrida Z-skruvarna för hand. Mät avståndet mellan **YZ-plattornas** främre respektive bakre sidor (*heel–toe*). Mät inte mellan hjulfästena. Måtten ska vara så lika du kan få dem; justera tillfälliga stag/änd-`Brace` innan fortsatt montering.

**Kontroll D:** Core går friktionsfritt, båda Z-sidorna kan höjas och sänkas utan bindning, och fram-/bakmått är lika inom mätosäkerheten. Fotografera gärna måtten och notera dem i byggloggen.

## 5. Montera bordets Y-styrning och remmar

Originalbilder: [Belts](https://docs.v1e.com/lowrider/#belts).

1. Kontrollera bordets underrede en gång till. Lägg ut maskinen på den köpta **1800 × 1000 mm**-skivan och provmarkera den kalkylerade yttre rem-/styrningslayouten **941 × 1563 mm**. Lägg inte till någon gammal 90 cm-kantbreddning.
2. Montera **den enda Y-styrskenan** som rak referens, parallellt med vald bordskant. Den andra sidan har Y-rem men ingen andra styrskena. Y-remhållare och `Y_Clip` använder samma yttre referens. Förborra så att plastdelarna ligger plant. Avstånd mellan Y-clips: **högst 300 mm centrum–centrum**.
3. Börja med de två Y_Max-hållarna och de första/sista clipsen, fördela övriga clips jämnt, montera Y_Min-hållare och deras justerskruvar. Kontrollera att brytararmarna möter Y-min-stoppskruvarna **innan** mekaniskt stopp.
4. Lägg rem runt M3-låsskruvar, genom remhjul och idlers. Dra båda Y-remmarna lagom sträckta. V1E anger omkring **7 lbf ≈ 31 N** som riktvärde; det ska inte kännas som en gitarrsträng. Börja hellre för löst än för hårt.
5. Montera X-remmen på motsvarande sätt. Flytta Core **långsamt för hand** och kontrollera att remmen ligger rätt hela vägen.
6. Kontrollera att inget av Y-stoppens skruvar kan passeras av brytararmen; en passerad skruv kan knäcka armen.

**Kontroll E:** ingen rem vandrar på ett löphjul; fram/bak återkommer Y-brytarnas armar till samma mekaniska referens; skivan/underredet rör sig inte när maskinen belastas lätt. Spänn inte hårdare för att ”lösa” ett geometrifel.

## 6. Kabeldragning – vår placering skiljer sig från originalet

Originalbilder: [Wire Routing](https://docs.v1e.com/lowrider/#wire-routing) och [Jackpot3 Wiring](https://docs.v1e.com/electronics/jackpot3/#wiring).

- **Rörligt:** Jackpot3 i rätt printad låda på balkens YZ_Min-sida. Lämna fri luft runt kort och antenn. Dra ledare bredvid, inte ovanpå, kortet. Dragavlasta allt innan kablarna lämnar lådan.
- **Fast:** 230 V NVR/maskinstopp placeras lättåtkomligt på bordet. **Rörligt:** Jackpot3 och, efter lämplig kapslings-/infästningskontroll, Mean Well HDR-60-24 på balken. Kontrollera att inga nätspänningsförande plintar är åtkomliga.
- **Mellan fast och rörligt:** nätmatningen till HDR-60-24 och fräsens kabel behöver säker rörlig dragning och dragavlastning. Anslut Jackpot3 till HDR med kort 24 V-kabel på balken. Den redan köpta 3 m 2×20 AWG-kabeln är reserv; dra inte en lång 24 V-slinga utan behov.
- **Balk/Core:** märk varje motor-/brytarkabel, fäst förlängningsskarvar utan draglast och låt Core kunna nå både X-ändar. Låt dammsugarslangens upphängning ta slangens vikt, inte Z-vagnen.

**Full-travel-kontroll innan permanenta buntband:** prova samma montage samtidigt med HDR:s nätmatning, kort 24 V-förbindelse, motor-/brytarkablar, fräsens nätkabel och dammsugarslang. Kör för hand till alla fyra hörn och Z:s båda ytterlägen. Inget får sträckas, vikas hårt, falla i remmarna eller dra i en kontakt.

## 7. Jackpot3: lågspänning och programvara

Original: [Jackpot3 – Initial Setup, Tests och Firmware](https://docs.v1e.com/electronics/jackpot3/).

1. Kontrollera kortets märkning mot **Elecrow Jackpot3 `CQA240812C2`** och att 24 V är **frånkopplat** innan någon kontakt flyttas. Använd inte Jackpot 1/2:s kopplingsbild eller konfigurationsfil.
2. **Inventera** dataförande USB-C-kabel och ett microSD-kort större än 2 GB, FAT32. Köp bara det som faktiskt saknas.
3. Hämta den **för tillfället V1E-testade** FluidNC-versionen, WebUI-versionen och *Jackpot3 + LowRider 4*-konfigurationspaketet från ovanstående källor. Dokumentationen anger vid guideupprättandet FluidNC **3.9.9** och WebUI **V3**; kontrollera på nytt före installation. Ett kort från Elecrow ska **inte antas vara förkonfigurerat** bara för att V1E säljer färdigflashade kort.
4. Om installation behövs: **bryt huvudmatningens 24 V innan USB-C ansluts** och följ V1E:s webbaserade installation. Ladda sedan upp rätt `config.yaml` och de makron som hör till samma paket. Spara en kopia av filerna före egna ändringar.
5. Koppla de fem motorerna och fem normalt slutna brytarna enligt den aktuella **Jackpot3-LR4-kopplingsbilden**. För varje mikrobrytare används **COM + NC**, och respektive signal/jord ska stämma med märkt ingång. Gissa inte stiftordning eller motorns par utifrån kabelfärg.
6. Slå på endast styrningens matning. Fräsens nätkontakt ska vara urdragen och ingen fräs sitta monterad. Anslut enligt dokumentationen till **FluidNC**-nätet och öppna **http://192.168.0.1** om standardåtkomst fortfarande gäller.
7. Kontrollera `$SS` (uppstartsmeddelanden). Testa var och en av brytarna med `$Limits` i terminalen; avsluta med `!`. Verifiera att rätt ingång ändrar status när du trycker på rätt brytare. **Brytarna används för homing/autosquaring, inte som garanterade stopp under körning.**
8. Joggning: börja med **1 mm**. Sett framifrån: X+ höger, Y+ bortåt och Z+ upp från arbetsytan. Stoppa vid fel riktning och bryt **både 24 V och USB** innan motoranslutningar ändras; verifiera rätt kontakt/config före ny provkörning. Testa sedan axlar var för sig med större men fortsatt fria rörelser.
9. När alla riktningar och brytare verifierats: prova homing med fri rörelseväg, beredd att bryta matning om något går fel. Ändra `pulloff_mm` först utifrån uppmätt avvikelse; spara ändringen i konfigurationen och enligt V1E:s WebUI-makro, starta om och verifiera att inställningen finns kvar.

**Kontroll F – styrning:** rätt modell, fungerande start utan konfigurationsfel, fem identifierade motorer och fem verifierade brytare, 1 mm-rörelser i rätt riktning. **Inga påhittade pin-nummer eller firmwarevärden** skrivs in i den här guiden; aktuell V1E-konfig och kortets märkning är facit.

## 8. 230 V, maskinstopp och damm – separat säkerhetsgräns

Se [AUDIT](../AUDIT.md) och [CHECKLIST](../CHECKLIST.md). Detta är vår projektspecifika elarkitektur; inte en del av V1E:s standardschema.

- **NVR är ännu en vald funktionsprincip, inte verifierad inkoppling.** Välj faktisk 230 V-enhet efter dess terminalschema och märkström. Placera stoppet direkt nåbart. Skydda aggregatets nätspänningsplintar även på balken; kapsling, genomföringar, infästning och dragavlastning dimensioneras efter de verkliga delarna.
- Skyddsjord (PE) ska vara obruten och inte gå genom NVR-brytaren. Kontrollera PE-kontinuitet och att ingen kortslutning finns mellan L/N och PE före spänningssättning. Låt en elkunnig fackperson kontrollera nätspänningsinkopplingen om du inte kan verifiera koppling och mätningar själv.
- Prova NVR:s *no-restart*-funktion **med fräsen frånkopplad**: efter avbrott får återkommen nätspänning inte starta lasten automatiskt. Kalla inte lösningen ett säkerhetsklassat nödstopp.
- Provpassa KATSU-hylsan och kontrollera synlig excentricitet/mät runout innan skärande körning. Dra ur kontakten vid fräsbyte.
- Bygg dust shoe, avlastad slang, cyklon och styv behållare. Kontrollera behållaren med kontrollerat vakuumtest. Verifiera statisk jordväg innan återkommande MDF-/trä-/XPS-arbeten.

**Stoppregel:** Ingen körning med roterande verktyg om kabelslingan, fräsens infästning, stoppfunktionen eller arbetsstyckets fastspänning är oklar.

## 9. Första rörelserna, måttkontroll och permanenta stag

Original: [Initial Calibration](https://docs.v1e.com/lowrider/#initial-calibration) · [Making the Strut plates](https://docs.v1e.com/lowrider/#making-the-strut-plates) · [Temp to Custom Strut Plates](https://docs.v1e.com/lowrider/#temp-to-custom-strut-plates).

1. **Torrkör utan fräs först.** Verifiera hela driven rörelsevägen och kablarnas/slangens frigång. Kör sedan enkla, små provjobb i billigt material under uppsikt när säkerhetskontrollerna är godkända.
2. **Kalibrera mått.** Mät en känd lång X- eller Y-förflyttning, helst märken nära varsin ände. Vid fel: nytt `steps_per_mm = gammalt steps_per_mm × (begärd sträcka / uppmätt sträcka)`. Justera värdena för X/Y enligt V1E och kontrollera resultatet med ny mätning. Ändra inte andra motorinställningar godtyckligt.
3. **Räta upp Y.** Gör fyra tydliga markeringar som en rektangel, mät båda diagonalerna och justera Y-sidornas homing/pull-off enligt V1E. V1E beskriver under 1 mm diagonalskillnad som mycket bra på stor maskin; anpassa kontrollstorleken till vår mindre arbetsyta. Mät om efter varje ändring.
4. **Nivellera Z.** Jämför fräshöjd mot bordet nära båda ändar; mät flera gånger och justera respektive Z-brytares `pulloff_mm`. Spara och kontrollera efter omstart. Detta måste upprepas när permanenta stag monterats.
5. Generera de två permanenta stagplattorna med **`strut_length=819` och `front_wing_size=30`**. Använd fram- och bottenplatta; 5–6 mm styv MDF/hårdboard, **högst 6,35 mm**. Kontrollera CAD/SVG mot vår geometri. Importera med **millimeter** och verifiera orientering i CAM; V1E:s EstlCAM-exempel roterar ritningen 90°.
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
| Delarna blir systematiskt för små | Börja med känd förflyttning och remkalibrering; anta inte att mer remspänning löser allt |
| Första fräsningen tar ojämnt djup | Kontrollera Z-nivå, inspänning och behov av planfräst offerskiva |

## Byggjournal – fyll i, anta inte

| Grind | Datum / resultat |
|---|---|
| A Core klar | ☐ |
| B YZ-sidor går lätt | ☐ |
| C temporär balk klar | ☐ |
| D heel–toe och Core | ☐ |
| E Y-styrning/remmar | ☐ |
| F Jackpot3, motorer och brytare | ☐ |
| NVR/PE och full-travel | ☐ |
| G permanenta stag och kalibrering | ☐ |

Skriv faktiska mått, problem och ändrade beslut i [BUILD_LOG](../BUILD_LOG.md) eller [CHECKLIST](../CHECKLIST.md). **Den här guiden dokumenterar hur vi ska bygga; den uppdaterar inte automatiskt fysisk leverans- eller kontrollstatus.**
