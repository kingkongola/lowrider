# Build log

## 2026-08-29 — initial design/procurement pass

- Privat GitHub-repo skapat för LowRider V4-bygget.
- Maskinvalet avslutat: LowRider V4.
- HaWiWe-order lagd och betald: 165,50 € inklusive 8,00 € frakt.
- Arbetsytan låst till 650 × 1250 mm.
- Exakt geometri: rör 816 / 816 / 1505 mm, strut 819, GT2 999 / 1705 / 1705 mm, minimum bord 941 × 1563 mm, deck ~1000×1620 mm.

## 2026-08-29 — oberoende system-/fysisk audit

- 24 V-rutten korrigerades till 3 m marginal + full-travel dry-fit.
- alla diameterberoende prints = 30 mm; strut `819` + `front_wing_size=30`.
- 90 cm bord godkändes med explicit kantstöd.
- KJD12 benämns NVR/maskinstopp, inte safety-rated E-stop.
- statisk jordning blev gate.

## 2026-08-30 — commissioning-audit

- T8 400 mm kapas efter assembly-check; ~150–160 mm ×2.
- microSD + data-USB-C inventeras före köp.
- endstops = home/auto-square, inte runtime hard limits.

## 2026-08-30 — sourcingoptimering

- DigiKey absorberade lågspänningskablar för att undvika separat order.
- PLA-behovet korrigerades till cirka 2,7 kg → köp 3 kg, inte 6 kg.

## 2026-09-03 — HaWiWe skickat + full repo reconciliation

- HaWiWe har skickat den redan betalda ordern.
- En tydlig kanonisk hierarki infördes: `PROCUREMENT.md` är enda ordermatrisen; BOM innehåller specs/kvantiteter; sourcing innehåller evidens; audit innehåller fysiska gates.
- Clas Ohlson KJD12 230 V/10 A verifierades till 299 kr som enkel NVR-kandidat.

## 2026-09-03 — verkliga kostnader + Jackpot3 köpt

- HaWiWe faktisk bankdebitering: **1 853 kr**.
- Jackpot3 `CQA240812C2` köpt från Elecrow: **937 kr** faktiskt debiterat.
- `COSTS.md` skapades som kanonisk ledger; SEK-debitering är facit framåt.

## 2026-09-03 — mekanik och commodity sourcing

- LaskaKit-order: 6 idlers, T8×8 400 mm, 2 kopplingar, 5 m GT2 10 mm; **444 kr** faktiskt debiterat.
- eBay/POWGE: 3 × 16T / 5 mm / 10 mm drive pulley; **72 kr** faktiskt debiterat.
- DigiKey: PSU, endstops, lager och el/lågspänningssmådelar; **986,98 kr** faktiskt debiterat.
- Amazon: 5 × STEPPERONLINE `17HS19-2004S1` samt KATSU `101750` beställda.

## 2026-09-05 — HKGY01 T8×8-muttrar annulleras

- eBay-säljaren meddelade out of stock och bad köparen annullera.
- **67 kr** ligger kvar i kostnadsloggen tills återbetalningen verifierats.

## 2026-09-05 — T8×8-muttrar ersättningsköpta via Amazon

- Amazon.se/euroharry: 4 × flänsad T8-mässingsmutter, Ø8 mm, 2 mm pitch, 4-start, 8 mm lead.
- Visat orderpris: **101,76 kr**.

## 2026-09-06 — 3 kg PLA köpt från PrintOnion

- **3 kg PLA 1,75 mm** köpt från PrintOnion för **426 kr**.
- Filamentbehovet för basbygget är stängt.
- Bordstrategin förenklades: ett styvt 180×90-bord använder sin egen skiva som maskinbas; ingen full extra deck som standard.

## 2026-09-07 — Motonet-rör köpta

- **2 stålrör** för LR4 köpta på Motonet för **340 kr totalt**.
- Planerad spec är `88-7123`, Ø30×1,5×2000 mm.
- Rörsourcingen är stängd; **kapa inte ännu**.
- Före kapning ska faktisk OD, rakhet och längd verifieras. Därefter målkapning: **1505 / 816 / 816 mm**.
- Verifierat faktiskt debiterat projektbelopp var då **5 125,98 kr**; aktiv committed cost exklusive HKGY01-annulleringen **6 389,11 kr**.

## 2026-09-09 — DigiKey-paket mottaget

- DigiKey-paketet hämtat/mottaget.
- Ordern innehåller PSU, endstops, 608-lager, Wago, glands, Faston, lågspänningskablage och board-pigtails enligt BOM.
- Leveransstatus ändrad till **RECEIVED**.
- Nästa gate är att räkna av innehållet mot BOM före montering; mottaget betyder ännu inte att varje del är fysisk-verifierad.

## 2026-09-10 — T8×8-mässingsmuttrar mottagna

- Amazon.se/euroharry-paketet med **4 × flänsad T8-mässingsmutter** mottaget i postlådan.
- Spec enligt beställningen: Ø8 mm, 2 mm pitch, 4-start, 8 mm lead.
- 2 används i LR4 och 2 blir reserv.
- Leveransstatus ändrad till **RECEIVED**.

## 2026-09-10 — alla hittills lagda köp debiterade

- Användaren bekräftade att **samtliga hittills lagda inköp är debiterade**.
- Amazon-orderna flyttades därför från väntande/committed till faktiskt betalt i `COSTS.md`.
- Debiterade Amazon-belopp enligt tidigare dokumenterade SEK-orderbelopp: motorer **608,37 kr**, KATSU **620,00 kr**, euroharry T8-muttrar **101,76 kr**.
- **Brutto faktiskt debiterat hittills: 6 456,11 kr.**
- **Aktiv faktisk projektkostnad exklusive HKGY01-order som väntar återbetalning: 6 389,11 kr.**

## 2026-09-18 — Jackpot3 mottagen

- Elecrow Jackpot3 `CQA240812C2` har kommit fram och är fysiskt mottagen.
- Leveransstatus ändrad till **RECEIVED**.

## 2026-09-19 — Bordsköp, remhjulsspårning och utskriftsläge

- Användaren rapporterade att begagnad **180×100 cm bordsskiva köpts för 300 kr**. Underredets skick/styvhet är ännu inte dokumenterat; ingen 90 cm-kantbreddning ska planeras.
- eBay/POWGE **3 × 16T-remhjul, redan köpta för 72 kr, är ännu inte mottagna**. eBay: importklarering 11 sep; senaste visade händelse `RECEIVED BY LMC / DEFRAA` 12 sep. Avvakta leverans och köp inte igen.
- Användaren printar **platta 10 av 14**.
- Permanent strut-plan enligt V1E: 4 printade temporära struts (15 % infill) vid montering; LR4 fräser sedan egna front-/bottenstruts ur 5–6 mm MDF/hardboard (max 6,35 mm). Generatorinställningar `strut_length=819`, `front_wing_size=30`.
- Betald brutto inklusive bordsskivan: **6 756,11 kr**. Aktiv kostnad exklusive annullerad eBay-order (67 kr) som väntar återbetalning: **6 689,11 kr**.

## 2026-09-21 — Tre 16T-remhjul mottagna

- Användaren bekräftar att **samtliga 3 × eBay/POWGE-remhjul** har kommit fram.
- Tidigare leveransblockerare för X/Y-remdrivning är därmed undanröjd. Verifiera fysisk variant: 16 tänder, 5 mm motoraxelhål och passning för 10 mm GT2-rem.
- Ingen ytterligare kostnad: **72 kr är redan bokförda** i `COSTS.md`. Denna leverans innebär inte att montering eller dimensionkontroll är utförd.

## 2026-09-21 — Verktygsfästet saknar bekräftad utskrift

- Användaren påpekade att den tidigare 14-plåtsplanen inte uttryckligen uppmanade till utskrift av ett Makita/65 mm-verktygsfäste.
- V1E:s separata Makita 701 Tool Mount and Dust Shoe är listad utanför huvuddelarna. **Vi vet inte om fästet fysiskt finns eller saknas; ingen fullständig inventering har återrapporterats.**
- Ny arbetsorder LR-00 kontrollerar rätt variant för KATSU 101750 (cirka 65 mm), startar separat utskrift vid behov och godkänner passning. LR-07 får inte förutsätta att fästet redan finns. Ingen ytterligare inköpskostnad är bekräftad.

## 2026-09-21 — Core omprintad; kabelmått saknades i arbetsordrar

- Användaren bekräftar att **hela Core är omprintad** och att nya utskriften **inte har den tidigare cirka 0,20 mm förskjutningen**. Gamla defekten är historik, inte ett aktivt fel; nya delen ska fortfarande vanlig passningskontrolleras.
- Arbetsordrarna saknade kaplängder för fem NC-brytare och motorförlängningar. Infört mätprotokoll `CABLE_ROUTING.md`: V1E har inget generellt exakt kapmått för vårt 650×1250-bygge. Mät respektive sträcka efter provmontering med X/Z/Y i rörelseextremer, dokumentera och kapa först då. Explicit V1E-mått för eventuell touchplate är minst 140 mm fri ledning vid Core.
- Köpta lager/motorer/kablar oförändrade, inga nya köp antagna.

## 2026-09-21 — Rättelse: X-brytarens 250 cm var inte verifierat

- Efter att kapmåttet 250 cm skrivits in i arbetsordrar och illustrerad guide granskades V1E:s originaltext. Originalet specificerar **ingen exakt längd för X-brytarens kabel** för vår maskinstorlek; endast minst 140 mm för *valfri touchplate* vid Core.
- **250 cm har dragits tillbaka som bindande kapinstruktion.** Mata kabeln från befintlig 10 m-rulle genom Core vid LR-08, prova hela X-slaget med avlastad kabelväg till Jackpot3 vid LR-16 och kapa först när faktisk längd är känd. Om användaren redan har kapat 250 cm, behåll biten och kontrollera räckvidden.
- Ändring synkad till `docs/MONTERING_SV.md`, `docs/index.html`, `docs/work-orders.json`, `WORK_ORDERS.md`, `CABLE_ROUTING.md`, `CHECKLIST.md` och `AUDIT.md`. Ingen fysisk kapning eller mätning är bekräftad.

## 2026-09-21 — Bekräftat mekaniskt passningsfel: X-brytarkabel

- Användaren har faktiskt provat den levererade **Tensility 30-00377, 3×26 AWG med cirka 4 mm svart mantel**: **den går inte genom Cores kabeltunnel**. Detta är inte längre en hypotetisk kontroll. Vårt kabelval var dåligt avstämt mot Core.
- Inget har kapats enligt användaren. Praktisk åtgärd att prova utan nytt inköp: avlägsna den svarta ytterkappan **bara över den korta trånga kanalens faktiska längd**, låt två individuellt isolerade ledare passera om de går fritt, behåll svart mantel på den yttre rörliga delen, ge mantelavslutningen dragavlastning och skydd mot skav. Ingen skadad ledarisolering får användas. Om detta inte fungerar skyddat: tunnare flexibel tvåledarkabel eller säker alternativ extern rutt.
- Kontrollera att den mantlade kabeln inte heller kolliderar med YZ-kanalerna innan någon kompletteringsorder görs. Endstopens slutliga längder och kontaktdon återstår att verifiera.


## 2026-09-29 – dokumentgranskning inför kapning och bygge

Svenska manualen och webbtexten har granskats mot V1E:s aktuella LR4-kalkylator, monteringsmanual, Jackpot3-dokumentation och Mean Wells HDR-underlag. Rörgeometrin bekräftad i kalkylatorkoden. Ovillkorlig T8-kapning till 150 mm återtagen till fysisk provpassning enligt D014; remmarginal och sågspår förtydligade. Kabelrullens fördelning och arbetsordningen rättad, inklusive LR-16 före LR-15 och LR-22 före LR-21. Separat granskningsprotokoll: [AUDIT_2026-09-29.md](AUDIT_2026-09-29.md).

Detta är dokumentändringar, inte rapport om utfört bygge. Inga fysiska kontroller, inköp eller leveranser har bockats av. Ändringarna är ännu inte publicerade på GitHub Pages.

## 2026-10-04 — kalibrering inleds

- Maskinen styrs över Wi-Fi (192.168.50.184, FluidNC 3.9.9). Hard limits på för alla fem brytare, soft limits X/Y/Z, travel 642/1240/98 mm, homad (användarens rapport 2026-10-03, bekräftad via config).
- Config-baslinje sparad i `machine/`. Kalibreringsprotokoll och logg i `CALIBRATION.md`; ordning steps/mm → squaring → Z-nivå.
- Kalibrering utförd (detaljer i `CALIBRATION.md`): X 50,0835 och Y 50,2054 steps/mm verifierade mot mätning; X-homing `mpos_mm` 2,99 (avrundning gav 2,995 mm); Y motor0 pulloff 6,2 / motor1 4,0 → diagonalskillnad 4,0 → 1,6 mm; Z-nivå uppskjuten. Controllern föll en gång tillbaka på Default-profil under sessionen (orsak ej fastställd; omstart räckte).

## 2026-10-07 — Offerskiva fastskruvad, fräsar mottagna

- Användaren rapporterar att **offerskivan är fastskruvad** på bordet. Material, tjocklek och kostnad ej rapporterade. Inte planfräst.
- **Fräsar har kommit med posten.** Typ, skaftdiameter, leverantör och kostnad ej rapporterade; bokförs i `COSTS.md` först när beloppet är känt.
- Ordning framåt oförändrad: litet skärprov (LR-24/25) → permanenta struts (LR-26/27/28) → planfräs offerskivan (LR-29) → Z-nivå och ny squaring (LR-30). Planfräsning före stagbytet görs inte, eftersom bytet ändrar balkens läge.

## 2026-10-07 — front_wing_size rättad

- `front_wing_size` är flikens utstick per sida på den främre stagplattan (plattan blir 67,5 + 2 × värdet mm hög), inte rördiametern. Generatorns kommentar: 8,0 för 32 mm-rör, **10,8 för 30 mm-rör**, 11,5 för 29,5 mm-rör. Tidigare `30` (ovan, 2026-08/09) var fel och är ersatt med **10,8** i alla aktuella filer. Bottenplattan har fast 5,5 i generatorn; dogbone 3,5 för 1/8"-fräs.
- Användaren rapporterar att **6,00 mm MDF är fastskruvad ovanpå offerskivan** inför stagplattorna. Fräsning ej utförd.

## 2026-10-16 — cyklon vald och utskrift påbörjad

- Jämförda modeller (MakerWorld): White Ghost kompakt (11 h, 5,0/85), VSC HF (23,4 h, 0,6 mm-nozzle, ingen ventil), Nanodesigner tvåstegs (50,9 h) och **eifelbiker med undertrycksventil** (18,7 h, 5,0/37, TPU-packningsprofil 1,7 h).
- **Vald: eifelbiker.** Skäl: inbyggd justerbar undertrycksventil löser kollapsrisken i uppsamlingskärlet (se `research/2026-08-29-cyclone-collection-container.md`), färdig TPU-packningsprofil, passar 30 l lockfat. Licens: MakerWorld Exclusive (personligt bruk).
- Användaren rapporterar att utskriften är påbörjad. Inte verifierad klar.
- Slangens ID är mätt till **46 mm** (rättat från 38 mm i BOM/CHECKLIST); dammskoadaptern `slangadapter_46mm` är printad (cnc-repot). Egna 46 mm-stosar till cyklonens portar återstår.
- Kvar: behållare (material, lockdiameter), slangens ytterdiameter, kontroll av insatser/skruvar/fjäder, vakuumtest av behållare och ventilinställning, statisk jordväg.

## 2026-10-22 — Offerskivan har en ofräst grop

- Användaren rapporterar att planfräsningen inte nådde en yta ungefär stor som A4 på offerskivan. **Rättat samma dag: det var en kulle, max ~0,25 mm, inte en grop**; 0,7 mm planfräsning (`plan07`) tar den. Trolig orsak enligt användaren: bordet är ojämnt (se CALIBRATION.md 2026-10-04, "bordet är inte plant") och offerskivan följer det. Gropens djup och läge ej uppmätt.
- Z-nivå (steg 3) ej gjord. Före tillverkning: mät gropen, välj djupare planfräsning eller shims under offerskivan, planfräs om, sedan Z-nivå och ny squaring.
- Användaren rapporterar att **de permanenta stagen (front/botten) är monterade** och att **dammsugningen är monterad**. Full X/Y/Z-rörelse med slangen ej verifierad; cyklonens status ej rapporterad.
- Plan: planfräs offerskivan ytterligare **0,7 mm** så att gropen tas, sedan Z-nivå (steg 3) och ny squaring. Planfilen görs om med `cnc plana` (filen `Planfras_offer_075` från 2026-10-15 är byggd före nuvarande postprocessor).
- Offerskivan var 9 mm MDF från början och har planats två gånger tidigare (0,5 mm per gång eller ~2 mm totalt, osäkert), plus 0,7 mm i dag (`plan07`). **Verklig tjocklek okänd och går inte att mäta vid kanten** (en ofräst ram runt den planade ytan). Användaren: styrhålen får gå så djupt fräsen räcker, även igenom offerskivan.
- **Planfräsning `plan07` klar 2026-10-22** (Ø22 planfräs, ratt 3, F1500, 0,7 mm). Användaren: ytan är plan nu, kullen borta. Ingen mätning med linjal/mätur rapporterad. Kvar: Z-nivå (steg 3) och ny squaring.

## 2026-11-10 — Servots rörelseomfång godkänt för BLTouch-armen

- Fristående bänkprov med ESP32-S3 slutfört efter rättning av provprogrammets pulsupplösning. Användaren godkänner servots rörelseomfång för sidotornets arm; denna konstruktionsosäkerhet är stängd.
- Provvärden, observationer och rättad källkod: [mätloggen](CALIBRATION.md#2026-11-10--fällservots-rörelseomfång-verifierat-på-bänk). Monterad arm och Jackpot-styrning återstår att prova.

## 2026-11-10 — Leverans och dokumentation konsoliderad

- Användaren rapporterar att Electrokit-order har kommit. Leveransraderna är uppdaterade i [PROCUREMENT.md](PROCUREMENT.md); faktiskt debiterat belopp är fortfarande inte bekräftat.
- BLTouch finns hos grannen för möjlig hämtning; ingen genomförd hämtning eller fysisk provpassning rapporterad.
- README leder till ägarfilerna, CHECKLIST äger aktuell arbetsstatus, sensorunderlaget skiljer sidotorn från äldre modulbygge, och ersatta brytarkrav hänvisar till D020. Äldre statuslistor och underlag bevaras i [arkivet](docs/arkiv/2026-11-09-status-och-sensorunderlag.md).

## 2026-11-10 — Första kamerafickeprovet printberett

- Ett litet passningsprov har skurits direkt ur aktuell torngeometri, med sparat källmanifest. Exporten är giltig och sammanhängande; `printa skiva` godkänner slutplattan utan kontrollfel eller varningar. Förhandsvisningen ur g-koden är granskad.
- Plattan innehåller endast kamerafickeprovet. PLA, 0,20 mm lager och trädstöd; beräknat cirka 16 minuter och 5,4 g. [Jobb och provförfarande](print/README.md). Utskrift eller fysisk passning är inte rapporterad.
- Granskningen visar att armens frigångshål vid servoaxeln inte är en färdig infästning i servohornet. Det återstår före armens slutprint; servots godkända rörelseomfång påverkas inte.

## 2026-11-10 — Proben tillgänglig, modell korrigerad till CR Touch

- Användaren uppgav att proben nu är tillgänglig och att kitet heter **CR Touch Auto Leveling Kit**. Det ersätter tidigare antagande om BLTouch hos grannen. Aktuell tillgång ägs av [PROCUREMENT.md](PROCUREMENT.md).
- CAD och kopplingsunderlag har markerats som ännu inte verifierade för CR Touch. Ingen geometri, utskriftsfil, fysisk inkoppling eller maskinkonfiguration har ändrats genom modelluppgiften.

## 2026-11-10 — CR Touch-anpassning i CAD och provplatta

- Crealitys standardkit och specifikationer undersökta; källor och skillnaden mellan tillverkaruppgifter och tredjeparts-CAD sparade i [CR Touch-underlaget](research/2026-11-10-crtouch-anpassning.md).
- Sidotornets BLTouch-låda ersatt med separat CR Touch-kropp/stift från källangiven STEP. Armfot och kabel-/kontaktutrymme ändrade, skyddshylsa omritad med åtkomst till skruvarna. Servoaxel, hålrad och nominellt parkeringsläge behållna. En liten plastöverlappning vid parkeringsstoppet rättad genom att korta magnetbulan.
- Exakt CAD-kontroll i 2° steg visar inga nya geometriska intrång i de testade gränssnitten. Prob, hylsa och kontaktkuvert går fria från CAD-tornet även med avståndsgränsen för mellanlägen. Tredjepartsmodellens egna små skruvhuvudavvikelser lämnas uttryckligen som fysisk kontroll, inte som godkänd passning.
- Ny [provplatta](print/crtouch-passning.json): armfot och hylsa, cirka 20 minuter och 7 g PLA, utan stöd. Printkontrollen har inga fel och en varning för små bryggytor. Förhandsvisning ur g-koden granskad. Ingen utskrift eller fysisk provpassning rapporterad.
- Kopplingsplanen uppdaterad till CR Touch och nominellt 5,0 V till Pi/prob. Ingen fysisk anslutning, regulatorjustering eller maskinkonfiguration utförd.

## 2026-11-10 — Lampdocka, separat bärare och servohornsbild

- Användaren visar ett enarmat servohorn med tre hål och centrumskruv. Exakta nav-/hålmått saknas; infästningen till den printade armen lämnas därför öppen. De tre lösa ringdelarnas funktion är inte säkert identifierad från bilden.
- Tornet har fått två blinda skruvfästen och en asymmetrisk styrtapp för en separat lampmodul. En G4-bärare är CAD-modellerad som utkast, med utbytbara sockeladaptrar. Lamp-/sockelformerna är reserverat utrymme; verkliga delar, matning, värme och ljusbild återstår att verifiera. Kameran behöver inte lossas för den prövade servicestudien.
- Exakta CAD-kontroller av delmöten, skruvåtkomst och armsvep passerar. Arm, prob, hylsa och kontaktkuvert går fria från lampmodulen även mellan de kontrollerade 2°-lägena enligt avståndsgränsen. Demontering med utfälld arm prövas separat som stickprov. Avgränsningar och rapporter ägs av [CAD-underlaget](machine/delar/sensorer/README.md).
- Ett tangentmöte vid lampbossen rättades till överlappande gods så att exporterad tornmesh är tät. Dockprovet fick massiv rygg för stödfria lager, utan att fylla huvudtornets elektronikrum. Kallt dock-/fotprov är kontrollerat och skivat: cirka 8 minuter och 2,6 g PLA, utan stöd eller kontrollvarningar. [Jobb och provförfarande](print/README.md#lampdocka--kallt-skruv--och-styrprov). Ingen fysisk print eller passning rapporterad.
- Tidigare lokala Lowrider-committar pushade till `sidotorn-v2` och de två dokumentationscommittarna till `cnc/main` efter användarens godkännande. De åtta ocommittade CNC-kodfilerna ingick inte.

## 2026-11-10 — Första hornmåtten och formad infästningsficka

- Användaren rapporterar navets A-/B-mått enligt det annoterade fotot; värden och definitioner finns endast i [mätloggen](CALIBRATION.md#2026-11-10--servohornets-nav-första-måtten).
- Användaren förtydligar att det befintliga hornet ska passa i en formad ficka i den printade armen och påpekar hornets avsmalning. Detta är konstruktionsavsikten; fickan är ännu inte modellerad. Två breddmått, armens tjocklek, hållägen och monterad höjd återstår före slutlig CAD och provpassning.

## 2026-11-10 — Hornets avsmalning och krav på klämning

- Användaren rapporterar C och D enligt bilden med breddmått vid mittenhålet och yttersta hålet. C rättades direkt; aktuella värden och definitioner finns i [mätloggen](CALIBRATION.md#2026-11-10--servohornets-nav-första-måtten).
- Användaren kräver att infästningen kläms fast så att några tiondelars mätfel inte lämnar glapp. Principen är ficka och skruvad bygel med sneda kontaktytor, fast anliggning och kvarvarande klämväg. Detta är ännu inte modellerat eller fysiskt verifierat; konstruktionskraven ägs av [CAD-underlaget](machine/delar/sensorer/README.md).

## 2026-11-11 — Hornficka med befintliga M3-typer och liten provplatta

- Återstående hornmått rapporterade 2026-11-10; [mätloggen](CALIBRATION.md#2026-11-10--servohornets-nav-första-måtten) äger värdena. Användaren förtydligade att klämning var ett förslag, medan stabil och glappfri infästning är funktionskravet. M2 saknas och nytt fraktköp avvisades.
- Formad ficka och separat kilbygel modellerade för två M3×10 som formar gängor i plast. Originalhornet behålls utan uppborrning. Metodjämförelse och begränsningar finns i [infästningsunderlaget](research/2026-11-10-servohorn-infastning.md).
- Bygeln placerad på fri sida, magnetkontaktens skruv bakom hornet. Stödskenor och kabelspår anpassade; förstärkningen kortad för frigång mot dammkjolen. CAD-kontrollerna passerar 81 måttkombinationer, monteringens stickprov, magnetficka och svep mot torn/servo/lampmodul. Detta bevisar inte fysisk klämkraft, plastgängornas hållfasthet eller glapp.
- Färska stickprov mot maskinreferenserna hittar inga intrång för arm, prob, hylsa, bygel eller deras skruvkuvert. Tornets prövade referensöverlappningar är noll och magnetens skyddshud mäts digitalt till 0,6 mm. Rapport och källfingeravtryck finns vid [CR Touch-provet](print/crtouch-passning/kontroll-maskin-manifest.json); kabel och komponentpassningar kräver fortfarande verkligt montage.
- Hornprovet är printkontrollerat och skivat: cirka 13 minuter, 4,7 g PLA, 0,20 mm lager och styrkeprofil. CR Touch-provet är omskivat mot aktuell export: cirka 20 minuter, 7,1 g, två varningar för små bryggytor och inga fel. Förhandsvisningarna ur g-koden granskade. [Jobb och provförfarande](print/README.md). Ingen utskrift eller fysisk passning rapporterad.

## 2026-11-11 — Skyddshylsan utgår; CR Touchen direkt i armfoten

- Användarens beslut efter [CR Touch-prov 1](CALIBRATION.md#2026-11-11--cr-touch-prov-1-underkänt-hylsan-går-inte-att-montera): ingen hylsa. Kitets M3×6 underifrån genom öronen (1,8 mm uppmätt) in i armfoten; hålavstånd 17,5 mm uppmätt. Tillägg i [D020](DECISIONS.md).
- Hylsan borttagen ur export, kontroller, printjobb och dokument; täckningsmatrisens rad markerad som utgången och dess underkända prov behålls som historik. Alla kontroller i sidotornets CI passerar lokalt. Negativtest: ett 2 mm för högt slutläge underkänns; vägen in kan utan hylsa inte längre krocka och bevisar därför lite.
- Nytt CR Touch-prov: bara foten, cirka 5 minuter och 1,6 g PLA. Ingen utskrift eller fysisk passning rapporterad. Hornprov 1 är fortfarande underkänt.

## 2026-11-11 — Kameraprov godkänt; kameralock ritat

- Användaren: kamerafickan passade "som en handske" ([Kameraprov 1](CALIBRATION.md)). Första godkända fysiska provet i täckningsmatrisen.
- Användarens önskan: bara objektivet ska synas underifrån. Nytt **kameralock** (`kameralock()` i `sidotorn.py`): platta under fickan med hål för objektivet och skallarna, pelare upp till ett öra under varje M3-skalle. Samma två M3 × 10, nu 9 mm gänga. Plattans ovansida följer tornets sluttande undersida vid fickans vänstra kant. Tornet är oförändrat.
- CAD-kontroller: inget intrång i torn, kort, tappar, skallar eller objektiv; locket rakt upp 15 mm fritt; skruvarna nåbara (insex 2,5); omgivningskontrollen mot skanningen GODKÄND lokalt. Negativtest: 0,2 mm för brett öra underkänns. Öronen behöver stöd vid print.
- Provjobb `print/kameralock-prov` (PLA, ca 5 min, 1,2 g); locket också på `sidotorn-smadelar`. Ingen utskrift rapporterad.

## 2026-11-11 — Horninfästningen omgjord: formficka och M3×10 genom armen

- Hornprov 1 böjde hornet för att provbiten satt mellan servot och hornet (användaren). Användaren underkände kilbygeln som konstruktion: en liten kil med två skruvar höll hornet med friktion.
- Ny lösning efter beprövad praxis: hornet i en formficka med 0,15 mm spel, servots mittskruv (Ø3 × 6, uppmätt) ersatt av M3×10 genom 4,0 mm armbotten; samma gängdjup som fabriksskruven (4,3 mm). Inga M2.
- Magnetens stålskruv låg i hornets insättningsväg och flyttades 26,5 mm ut; utsidan provades först men krockade med undre verktygsfästet i alla tio lägen. Parkeringsstoppet följer armens verkliga kant. Magnetens säkerhet mot 1 g ökade till 11,7.
- Alla CI-kontroller och omgivningskontrollen GODKÄND. Ny platta `print/sensorprov-2` (PETG, ca 1 h): arm, kameralock och stoppdelar. Ingen utskrift rapporterad; mittskruvens gänga (M3/4-40) inte provad.

## 2026-11-11 — Krossribbor i hornfickan

- Användaren frågade om glapp. Sju krossribbor (Ø1 mm, 0,2 mm överlapp, infasning) i fickan i stället för lim: de plattas till när hornet trycks in. Väggarna har kvar 0,15 mm spel.
- `kontroll_horn.py` prövar väggar och ribbor separat: väggarna fria, varje ribba 0,1–0,5 mm³ krossvolym. Negativtest: ribbor utan överlapp och med 0,6 mm överlapp underkänns. Alla kontroller och omgivningskontrollen GODKÄND. `sensorprov-2` omskivad: ca 1,0 h, 10 g PETG.

## 2026-11-12 — Alla delar mottagna

- Användaren: "allt har kommit". Mottagna enligt användaren: INMP441 och KW11-3Z-N (10-pack, reservdelar), utöver Electrokit-ordern och CR Touch. Ägare: PROCUREMENT.md och BOM.md.
- Inte verifierat: antal och modell post för post, funktion, passning och kortdebitering (COSTS.md oförändrad). Övervakningens andra nätdel (HDR-60-24) är fortfarande inte beställd.
- Nästa mätsteg: skjutmått på de köpta delarna (INMP441, COB-listens bredd, ADXL, Pi) så N-rutorna i täckningsmatrisen kan bli A.

## 2026-11-12 — sensorprov-2 utskriven

- Användaren: plattan `print/sensorprov-2` (PETG, styrka) är klar. Innehåll: arm, kameralock, stopp-nedre, stopp-ovre, skruvprov, LED-segment.
- Inga provresultat rapporterade än; ingen matrisruta ändras förrän de är det. Servohorn/fastsättning står kvar som underkänd (gamla provet).
- **Rättelse:** COB-listen (LED) har inte kommit; den ströks ur listan över mottagna. Mät COB-kortets bredd när den kommer.
