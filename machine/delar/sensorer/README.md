# Sensorenhet till V1E LowRider V4 – build123d

**Status 2026-11-09:** parametrisk, separat demonterbar **sensortillsats på befintlig Core/verktygshållare**. Det här är INTE själva V1E-Core och inga originaldelar ändras. Nya delar utgår från [befintlig build123d-servoarm C](../nollpunkt/fallarm_c.py), men den gamla cylindriska proben är **ersatt av BLTouch-geometri i konceptet**. Ingen maskin-CAD är fysiskt validerad.

**Gällande kod:** [core_enhet.py](core_enhet.py). **[Senaste gröna GitHub-CI och levererad STL/STEP/GLB](https://github.com/kingkongola/lowrider/actions/workflows/core-build123d.yml)**. Äldre [core_sensorer_v0.scad](core_sensorer_v0.scad) är **ersatt/legacy** och ska **inte** användas för nya utskrifter, trots att äldre test-STL-filer kan finnas i historik. CAD medges inte bara för att trianguleringen lyckas.

## Monteringsprincip: en enhet, tio separata delar

| Del | Roll | Byt utan att demontera |
| --- | --- | --- |
| `rygg` | Bärande platta; nyttjar **två befintliga M5 på verktygsfästet**, samma koordinater som arm C | Ingen original-Core behöver modifieras |
| `kabellock` | Skruvat, avtagbart lock över **6×3 mm** kabelspår och tre serviceutgångar | Servo, kamera och Pi |
| `servokassett` | Separat demonterbar ram för SPMS664 | Kamera, Pi, rygg |
| `bltouch_arm` | Separat utbytbar arm för lodrät BLTouch vid mätning | Kamerakassett/Pi |
| `kamerakassett` | Egen triangulerad, styv infästning med M2-hålbild **21×12,5 mm** | Servokassett/Pi |
| `pi_lada` | Utbytbar, fläktlös kapsling för Pi Zero 2 WH, **58×23 mm M2.5** | Kamera/servo; dockan sitter kvar |
| `pi_lock` | Avtagbart lock för Pi; inga snäpphakar | Rygg och kamera |
| `pi_dock` | Egen hållare mellan bärplattan och Pi-kapslingens fästöglor | Servo/kamera |
| `accel_bricka` | Småskruvad, styvt kopplad ADXL345-bärare med distanser bort från kabelkåpan | Andra sensorer |
| `mikrofon_bricka` | Egen M2.5-skruvad INMP441-pod på **Pi-lådans utsida**, akustiskt hål | Pi-kortet kan sitta kvar; hela lådan får dock tas loss vid lådbyte |

**Konstruktionsregel:** kamera och dess fäste får inte flytta sig när servot demonteras. Inget är limmat eller ihopgjutet mellan funktionerna. Bärplattan använder två hål ur befintlig C-modell: M5-centra Y43,95 / Z64,25 respektive Y43,95 / Z125,25 i projektets *M-ram*; **inte nytt borrmönster på den riktiga Core-delen**. Huvudkabelkanalen är öppningsbar medan maskinankarna sitter kvar. Servons flexkabel kräver separat, ännu inte uppmätt serviceslinga.

## Vad som är verifierat med kod

[GitHub Actions: Modular Core-enhet (build123d)](https://github.com/kingkongola/lowrider/actions/workflows/core-build123d.yml) använder build123d 0.10.0 och kompatibelt OCP, exporterar 10 × STL + 10 × STEP. Den testar:
- alla 10 STL är **slutna vattentäta sammanhängande mesh-kroppar** med positiv volym;
- de tio modulerna har **inga volumetriska BRep-överträdelser mot varandra** i monterade lägen;
- en **BLTouch-body-attrapp + arm** sveps över 0 till −90° i **15°-steg** och kontrolleras mot våra andra CAD-moduler och ritad SPMS664; inga BRep-skärningar i provsvepet;
- Core, Makita-tool mounts, dammsko, dammskokjol och SPMS664-kropp i befintliga STL refereras. **Ytavstånd till dessa är endast sampling/screening**, inte en exakt mesh-kollisionskontroll. Rapport i `montage-granskning.json`.
- **Sensorenhet-på-Core.glb** genereras som interaktiv färgkodad 3D-scen med separata objekt. Även `core-koncept.png` finns i artefakten.

**VIKTIGT: Detta är CAD-validering, inte driftsäker eller industrimässigt färdig konstruktion.** Monteringshålen från gamla C-versionen måste kontrolleras på faktisk maskin. De faktiska Core-/verktygsfäste-STL är referensgeometri; gamla transformen från [kontroll_c.py](../nollpunkt/kontroll_c.py) används och behöver kontrolleras mot verkligt montage. Ordet ”passar” får inte hävdas utifrån dessa tester.

## Kända P0-kvarstår innan BLTouch-armen får printas för drift

1. **Två hårda mekaniska stopp** (utfälld och infälld), och styrda **Omron SS-3GL13PT ×2** med justerbara lägen. Omron får inte vara själva hårdstoppet. Se [ANDLAGEN.md](../nollpunkt/ANDLAGEN.md). Ännu **inte** inritat/färdigdimensionerat i den nya armen.
2. Fysiskt **servohorn i metall**, faktisk servosplines, BLTouch-infästningsskruvar, 3D-printtoleranser och kabeldragning på rörliga armen ingår **inte** i det gröna svepet. Tidigare C-version hade cirka 1 mm frigång till servo och 3,4 mm till dammskokjol enligt annan modell. De värdena är inte giltiga för den nya.
3. **BLTouch** i koden använder preliminärt 18 mm hålavstånd, 36,3 mm kropp och **45,7 mm till utfälld stiftspets** enligt tillverkarritning. Faktisk BLTouch-version och dess skruvskallar, utsticket för in-/utfällt stift, kroppens kontakt/hus och hela probe-kabeln måste mätas och modelleras. Proben får inte träffa fräs, dammsko, golv, offerskiva eller sig själv i något läge.
4. Kamerans **200 mm CSI-flex** får inte vikas/skavas eller vara sträckt vid service. Rita fysisk port-/snäpporientering och dragavlastning när delarna är på plats. Pi-kapslingen har kabelöppning och är **inte spåntät/IP-klassad**. Nätaggregatregulator, skydd, elkoppling och GPIO fastställs separat i [KOPPLING_CORE_V0.md](KOPPLING_CORE_V0.md).
5. Kontroll av **verklig filmaskin, dammskokjol, all Z-position**, och framför allt hur monteringsskruvarna nås när systemet sitter på Core. Utskriftsorientering, stödstrukturer, skruvtyp/längd, insatser och printmaterial är inte slutligt validerade.

## Innan leverans och första provprint

**Kan granskas nu:** ladda ner senaste GitHub Actions-artefakten, öppna `sensorenhet-pa-core.glb` i en 3D-visare (moduler kan visas/döljas), eller STEP i Fusion. Kontrollera att layout, kabelkanal, kortens portåtkomst och konturer är rimliga.

**Provprint med låg risk om du accepterar sannolika justeringar:** `pi_lada`, `pi_lock`, `kabellock`, `kamerakassett`, för snabb passningskontroll när hårdvaran kommer. Ingen av dessa ska monteras på körande LowRider före den verkliga grinden. **Vänta med `bltouch_arm`, `servokassett` och alla maskininfästningar** för drift tills P0 ovan är löst. Meddelande om ”vattentätt STL” betyder inte klar att köra maskinen.

**Fläkt:** inte med i v0. Pi ska bara fotografera; datorn sköter tyngre OpenCV. Mät Pi-temp och verklig termisk throttling under kamerajobb först, och bygg om kapsling/ventilation endast vid observerat behov.

Original V1E Core ska förbli omodifierad. Denna sensorenhet är ett löstagbart tillbehör och får inte skapa driftberoende till maskinens grundfunktion.
