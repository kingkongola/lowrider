# Sensorenhet till V1E LowRider V4 – build123d

**Status 2026-11-09:** parametrisk, separat demonterbar **sensortillsats på befintlig Core/verktygshållare**. Det här är INTE själva V1E-Core och inga originaldelar ändras. Nya delar utgår från [befintlig build123d-servoarm C](../nollpunkt/fallarm_c.py), men den gamla cylindriska proben är **ersatt av BLTouch-geometri i konceptet**. Ingen maskin-CAD är fysiskt validerad.

**Gällande kod:** [core_enhet.py](core_enhet.py). **[Senaste gröna GitHub-CI och levererad STL/STEP/GLB](https://github.com/kingkongola/lowrider/actions/workflows/core-build123d.yml)**. Äldre [core_sensorer_v0.scad](core_sensorer_v0.scad) är **ersatt/legacy** och ska **inte** användas för nya utskrifter, trots att äldre test-STL-filer kan finnas i historik. CAD medges inte bara för att trianguleringen lyckas.

## Monteringsprincip: en enhet, elva unika CAD-delar (12 utskrifter)

| Del | Roll | Byt utan att demontera |
| --- | --- | --- |
| `rygg` | Bärande platta; nyttjar **två befintliga M5 på verktygsfästet**, samma koordinater som arm C | Ingen original-Core behöver modifieras |
| `kabellock` | Skruvat, avtagbart lock över **6×3 mm** kabelspår och tre serviceutgångar | Servo, kamera och Pi |
| `servokassett` | Separat demonterbar ram för SPMS664 | Kamera, Pi, rygg |
| `bltouch_arm` | Separat utbytbar arm för lodrät BLTouch vid mätning | Kamerakassett/Pi |
| `kw11_hallare` (2 ×) | **Två likadana justerbara hållare** på servokassettens egna fästöglor; två lägesgivare men en CAD-fil | Kamera, Pi och övriga maskinen |
| `kamerakassett` | Egen triangulerad, styv infästning med M2-hålbild **21×12,5 mm** | Servokassett/Pi |
| `pi_lada` | Utbytbar, fläktlös kapsling för Pi Zero 2 WH, **58×23 mm M2.5** | Kamera/servo; dockan sitter kvar |
| `pi_lock` | Avtagbart lock för Pi; inga snäpphakar | Rygg och kamera |
| `pi_dock` | Egen hållare mellan bärplattan och Pi-kapslingens fästöglor | Servo/kamera |
| `accel_bricka` | Småskruvad, styvt kopplad ADXL345-bärare med distanser bort från kabelkåpan | Andra sensorer |
| `mikrofon_bricka` | Egen M2.5-skruvad INMP441-pod på **Pi-lådans utsida**, akustiskt hål | Pi-kortet kan sitta kvar; hela lådan får dock tas loss vid lådbyte |

**Konstruktionsregel:** kamera och dess fäste får inte flytta sig när servot demonteras. Inget är limmat eller ihopgjutet mellan funktionerna. Bärplattan använder två hål ur befintlig C-modell: M5-centra Y43,95 / Z64,25 respektive Y43,95 / Z125,25 i projektets *M-ram*; **inte nytt borrmönster på den riktiga Core-delen**. Huvudkabelkanalen är öppningsbar medan maskinankarna sitter kvar. Servons flexkabel kräver separat, ännu inte uppmätt serviceslinga.

## Vad som är verifierat med kod

[GitHub Actions: Modular Core-enhet (build123d)](https://github.com/kingkongola/lowrider/actions/workflows/core-build123d.yml) använder build123d 0.10.0 och kompatibelt OCP, exporterar 11 × STL + 11 × STEP. Den testar:
- alla 11 STL är **slutna vattentäta sammanhängande mesh-kroppar** med positiv volym;
- de tolv fysiska delarna i monteringsmodellen har **inga volumetriska BRep-överträdelser mot varandra** i monterade lägen;
- en **BLTouch-body-attrapp + arm** sveps över 0 till −90° i **15°-steg** och kontrolleras mot våra andra CAD-moduler och ritad SPMS664; inga BRep-skärningar i provsvepet;
- Core, Makita-tool mounts, dammsko, dammskokjol och SPMS664-kropp i befintliga STL refereras. **Ytavstånd till dessa är endast sampling/screening**, inte en exakt mesh-kollisionskontroll. Rapport i `montage-granskning.json`.
- **Sensorenhet-på-Core.glb** genereras som interaktiv färgkodad 3D-scen med separata objekt. Även `core-koncept.png` finns i artefakten.

**VIKTIGT: Detta är CAD-validering, inte driftsäker eller industrimässigt färdig konstruktion.** Monteringshålen från gamla C-versionen måste kontrolleras på faktisk maskin. De faktiska Core-/verktygsfäste-STL är referensgeometri; gamla transformen från [kontroll_c.py](../nollpunkt/kontroll_c.py) används och behöver kontrolleras mot verkligt montage. Ordet ”passar” får inte hävdas utifrån dessa tester.

## Kända P0-kvarstår innan BLTouch-armen får printas för drift

1. **Två separata hårda mekaniska stopp** (utfällt och infällt), samt korrekt aktivering av **2 × QUARKZMAN KW11-3Z-N**. De två justerbara små brytarfästena är nu ritade och har klarat CAD-kontroll mot våra delar. **Rullspakens aktiveringspunkter, motgående kammar och hårdstoppen är ännu INTE konstruerade eller verifierade.** Brytarna får aldrig bära stoppkraften. Se [ANDLAGEN.md](../nollpunkt/ANDLAGEN.md). `Omron SS-3GL13PT` behålls till original-LowRidern.
2. Fysiskt **servohorn i metall**, faktisk servosplines, BLTouch-infästningsskruvar, 3D-printtoleranser och kabeldragning på rörliga armen ingår **inte** i det gröna svepet. Tidigare C-version hade cirka 1 mm frigång till servo och 3,4 mm till dammskokjol enligt annan modell. De värdena är inte giltiga för den nya.
3. **BLTouch** i koden använder preliminärt 18 mm hålavstånd, 36,3 mm kropp och **45,7 mm till utfälld stiftspets** enligt tillverkarritning. Faktisk BLTouch-version och dess skruvskallar, utsticket för in-/utfällt stift, kroppens kontakt/hus och hela probe-kabeln måste mätas och modelleras. Proben får inte träffa fräs, dammsko, golv, offerskiva eller sig själv i något läge.
4. Kamerans **200 mm CSI-flex** får inte vikas/skavas eller vara sträckt vid service. Rita fysisk port-/snäpporientering och dragavlastning när delarna är på plats. Pi-kapslingen har kabelöppning och är **inte spåntät/IP-klassad**. Nätaggregatregulator, skydd, elkoppling och GPIO fastställs separat i [KOPPLING_CORE_V0.md](KOPPLING_CORE_V0.md).
5. Kontroll av **verklig filmaskin, dammskokjol, all Z-position**, och framför allt hur monteringsskruvarna nås när systemet sitter på Core. Utskriftsorientering, stödstrukturer, skruvtyp/längd, insatser och printmaterial är inte slutligt validerade.

## Nytt 2026-11-09: två identiska, justerbara KW11-hållare

- **Köpt:** 10 × QUARKZMAN KW11-3Z-N från Amazon.se för 92,94 kr med fri Prime-frakt; beräknad leverans **lördag 2026-11-14**. Se [PROCUREMENT.md](../../../PROCUREMENT.md). Beställda, inte mottagna.
- **CAD som kod:** [kw11_faste.py](kw11_faste.py), en fasad hållare med **två M2-långhål** för osäker KW11-hålbild **8,5–9,5 mm**, och två M3-långhål med cirka ±2 mm finjustering. **Antal utskrifter: 2 × `kw11_hallare.stl`.** Den befintliga **servokassetten** har fått två korta monteringsöron; inga nya hål på V1E Core eller på kamera-/Pi-delarna. Hållarna kan bytas utan att flytta kameran.
- **CAD-grind:** [grön GitHub Actions-körning](https://github.com/kingkongola/lowrider/actions/runs/42616662416) gav 11 separata STL + 11 STEP och BRep utan modellöverlapp för de 2 hållarna, övriga moduler och förenklat BLTouch-svep. Detta testar **inte** brytarnas faktiska hus, rullspak, klickväg, ledaranslutningar eller de ännu saknade hårdstoppen. De nya fästena är **mått-/passningsprototyper**, inte driftsklara ändlägen.
- **Provrutin efter leverans:** mät kropp, hålavstånd, pinnarnas läge och spakens verkliga tillslags-/återgångsväg. Skruva fast en lös brytare i en lös printad hållare först. Ta reda på hur två åtskilda mekaniska stopp ska byggas så att brytarna bara läser läget; använd aldrig brytarspaken som stopp.

### KW11-mått från den köpta QUARKZMAN-listningen (9 november)

Användarens **nya Amazon-bild av exakt beställd KW11-3Z-N** anger **20 mm** längd, **20 mm** rullspak, **Ø5 mm** rulle och **4 mm** utstick på tre stift märkta `NC` (vänster), `NO` (mitten), `C` (höger) sett från bildsidan. Den visar även en vertikal pil märkt **16 mm**, men illustrationen är inte skalenlig och anger **inget c-c-avstånd mellan skruvhålen**. Siffrorna är alltså säljarens uppgifter, inte verifierade toleranser.

CAD-referensen i [kw11_faste.py](kw11_faste.py) skiljer uttryckligen detta från **nominella mått hämtade från andra KW11-3Z-varianter**: kropp 20 × 6,4 × 10,2 mm och skruvhålsavstånd 9,5 mm. `kw11_hallare` har slitsar i stället för att låsa detta till en icke verifierad variant. Varken leverans, faktisk monteringshålbild eller rullens tillslagspunkt är uppmätt. Brytaren är en **lägesgivare**; hårdstopp måste konstrueras separat.

## 2026-11-09 – funktionsgranskning av KW11-rullarnas lägen

**Fynd efter en geometrisk falsifiering:** i [CAD-kontrollen](granska_montage.py) ligger det modellerade rullhjulet som närmast **18,98 mm från rörlig servoarm i infällt läge** och **12,00 mm i utfällt läge**, när armen sveps i 15°-steg över 0 till −90°. Modellerna är nominella för QUARKZMAN KW11-familjen, inte uppmätta exemplar. Dessa stora luckor är dock tillräckliga för att visa att **nuvarande placering inte bekräftar något ändläge utan omkonstruktion**.

**Beslut:** behåll [en standardhållare i `kw11_faste.py`](kw11_faste.py) (2 × print), men **lås inte dess två placeringar på servokassetten** och kalla aldrig brytarnas funktion klar. Först placera rullhjul och lägeskammar där armen faktiskt kan aktivera dem i var sitt hårdstopp, därefter kontrollera att den andra brytaren är öppen under hela rörelsen. Hårdstoppen ska överföra lasten i print/metalldel, **inte via KW11-rullspaken**. Servoarmens metallhorn, kabel och dammsko måste ingå. Helst gemensam utbytbar cam på armen, utan något beroende till kamerafästet, men geometrin ska bestämmas av riktig kollisionskontroll och mätta brytare – **inte av ett förhandsval av koncept**.

**Tillåten provprint före leverans:** 1 × separat `kw11_hallare.stl` som *hål-/skruvpassningsprov*, inte ett driftsklart ändläge. Ingen automatisk fällning eller G38 är aktiverad. CAD:s gröna STL/STEP-test är en **export-/meshgrind**, inte en funktionsgrind för rullbrytare.

## Innan leverans och första provprint

**Kan granskas nu:** ladda ner senaste GitHub Actions-artefakten, öppna `sensorenhet-pa-core.glb` i en 3D-visare (moduler kan visas/döljas), eller STEP i Fusion. Kontrollera att layout, kabelkanal, kortens portåtkomst och konturer är rimliga.

**Provprint med låg risk om du accepterar sannolika justeringar:** `pi_lada`, `pi_lock`, `kabellock`, `kamerakassett`, för snabb passningskontroll när hårdvaran kommer. Ingen av dessa ska monteras på körande LowRider före den verkliga grinden. **Vänta med `bltouch_arm`, `servokassett` och alla maskininfästningar** för drift tills P0 ovan är löst. Meddelande om ”vattentätt STL” betyder inte klar att köra maskinen.

**Fläkt:** inte med i v0. Pi ska bara fotografera; datorn sköter tyngre OpenCV. Mät Pi-temp och verklig termisk throttling under kamerajobb först, och bygg om kapsling/ventilation endast vid observerat behov.

Original V1E Core ska förbli omodifierad. Denna sensorenhet är ett löstagbart tillbehör och får inte skapa driftberoende till maskinens grundfunktion.

## Sidotorn v2 (utkast 2026-11-09, ej printat, ej verifierat)

`sidotorn.py` ritar torn, arm och BLTouch-attrapp i build123d, `granska_sidotorn.py` kontrollerar dem mot V1E-delar och skanning. Tornet ersätter inte `core_enhet.py` innan det är godkänt.

**Krav från användaren:** bilderna sys ihop, så varje punkt ska synas i någon bild. Servo och dammsko får synas och maskas bort. Täckning ända ut till gränserna gäller upp till ca 50 mm material; tjockare kantfall görs manuellt.

| Sak | Utkast |
|---|---|
| Lins, rakt ned | 94 mm ut från balken, 53 mm längs balken mot X max, 130 mm över fräsens referensnivå |
| Beräknade bilder, 8 mm överlapp | 40 på 18 mm skiva, 63 på 50 mm |
| Dolt hörn vid X min och ena Y-gränsen | 0 mm vid 18 mm, 16 mm vid 50 mm |
| Hårda stopp | Armens två sidor mot fasta block i tornet, utfällt 0 grader och parkerat -140 grader |
| Ljus | Två urtag för diffuserade LED runt linsen; inget köps före bildprov enligt `../../KAMERA_ANHALL.md` |

**Skanningen i fräsramen:** `p_ny = R p + T` (mm) rättar 5,9 graders lutning i tidigare inpassning, så att bordet ligger plant:

```text
R = [[ 0.99453476, -0.02082188, -0.10230862],
     [ 0.02132634,  0.99976520,  0.00383939],
     [ 0.10220465, -0.00600027,  0.99474530]]
T = [5.9986, -1.4491, -3.7767]
```

**Mätt i skanningen, homad:** offerskivan ligger z = -87,5 mm (±2 mm), alltså 111,5 mm under CAD-kjolens underkant.

**Kvar:** KW11-brytare, Pi-kapsling och kabelväg, verklig servohorn och fästskruvar. Brytarlägen, kortets hålbild och servomått ska mätas mot levererade delar.
