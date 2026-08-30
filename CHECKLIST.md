# Checklist

## 1. Mottagning av köpta delar
- [x] HaWiWe-order dokumenterad
- [x] HaWiWe-order betald
- [x] Markera exakt vad som täcks av skruvsatsen
- [ ] När HaWiWe-paketet kommer: normal mottagningskontroll — kontrollera transportskada och att de fyra beställda produktgrupperna finns med; ingen separat BOM-inventering krävs
- [ ] Provmontera M3×10 mot 6,0 mm XZ-plattor/MGN-block och kontrollera att inget bottnar eller binder

## 2. Geometri / bord
- [x] Lås arbetsyta: **650 × 1250 mm**
- [x] Verifiera aktuell LR4-kalkylator med köpta 6,0 mm XZ-plattor
- [x] Lås maskingeometri: rör **816 / 816 / 1505 mm**, strut-input **819 mm**, rem **999 / 1705 / 1705 mm**
- [x] Lås minimum bord: **941 × 1563 mm** och praktisk CNC-deck cirka **1000 × 1620 mm**
- [x] Välj huvudarkitektur: styvt begagnat 160–180 × helst 90–100 cm bord + avtagbar CNC-deck
- [ ] Hitta/köp faktiskt begagnat bord och gör femminuters rackingtest
- [ ] Mät faktisk bordshöjd och underrede
- [ ] Om deck överhänger långsidan: verifiera lokal bärighet/infästning under LR4:s rail-/wheel-/belt-clip-zon; lägg blockning/list eller genomgående infästning vid behov
- [ ] Kontrollera totalhöjd och frigång för slang/kablar på det valda bordet
- [ ] Köp/inspektera Motonet-rör och kapa först efter fysisk kontroll av OD/rakhet

## 3. Köp/ordna det som saknas
- [ ] PLA: cirka 2,7 kg krävs för LR4; nuvarande bulkplan 6 × 1 kg SUNLU ordinary PLA om checkout håller
- [ ] Jackpot3
- [ ] 5 × StepperOnline `17HS19-2004S1`
- [ ] LaskaKit-korg: 6 idlers, T8×8, muttrar, kopplingar och lågspänningskablage — **rem exkluderad så länge direkt produktsida visar slut**
- [ ] GT2-rem separat: minst segment **999 / 1705 / 1705 mm**, GT2/2 mm, **10 mm bred, gummi + glasfiber, ingen stålcord**. Första checkout-kandidat är V1E:s egen Amazon-länk/SeekLiny ASIN `B097T4DFM6` (10 m); Technobots `6002-591` 5 m är verifierad fallback
- [ ] Köp **3 m** UL2464 20 AWG / ~0,52 mm² tvåledare för fast HDR-box → rörlig Jackpot; kapa först efter full-travel dry-fit
- [ ] 1 × Amphenol `AIO-CSM12`, M12 / 3–6,5 mm / IP68 som dragavlastning för ~4,8 mm 24 V-kabel
- [ ] 3 × exakta GT2 16T / 5 mm / 10 mm remhjul
- [ ] DigiKey: Mean Well `HDR-60-24`, 10 × Omron `SS-3GL13PT`, 16 × 608-2RS, Wago, M20, **A27824-ND Faston** och `AIO-CSM12` enligt `PROCUREMENT.md`
- [ ] Verifiera DigiKey-frakten i checkout; köp ingen filler
- [ ] VEVOR 0700C 800 W router
- [ ] genuin **KEDU KJD12-14**, 230 V/50 Hz, NVR + röd stoppkåpa; verifiera exakt levererad variant
- [ ] kompakt IP65 el-kapsling efter fysisk dry-fit av KJD12/HDR
- [ ] bordsmaterial/CNC-deck efter valt begagnat bord
- [ ] ~12 mm MDF-spoilboard
- [ ] 3 × Sorotec `L1S.M.0317` för commissioning
- [ ] kabelhantering
- [ ] arbetsstyckesfastsättning — börja med skruv/tabs i spoilboard, inget T-track-kit nu
- [ ] Inventera **microSD >2 GB, FAT32, helst Class 4/6**; köp enkelt 4–32 GB endast om inget lämpligt finns
- [ ] Inventera/verifiera **data-kapabel USB-C-kabel** för Jackpot-flashing

## 4. Dammhantering — grundkrav
- [ ] Välj/printa LR4 dust shoe som passar **65 mm Makita-formatet**
- [x] Grovdammsugare/shop-vac finns: DeWalt, sannolikt DXV30SAPTA
- [ ] Bekräfta DeWalt-typskylt innan modellens AUTO/tool-socket-effekt eller ~15 kPa sealed pressure används som faktum
- [ ] Printa cyklonavskiljare
- [ ] Ordna separat styv 15–30 l uppsamlingsbehållare; **stål är kandidat, inte garanti mot buckling/implosion**
- [ ] Efter tät montering: vakuumtesta behållare/lock kontrollerat; stoppa vid synlig deformation/knäppning
- [ ] Testa befintlig DeWalt 48 mm × 2,1 m slang innan ny slang köps
- [ ] Bygg slangupphängning/dragavlastning som inte belastar gantry/Z
- [ ] Lös statisk jordning med definierad PE-punkt eller groundable hose; HDR-60-24 är **inte** jordpunkt
- [ ] Verifiera jordkontinuitet innan XPS eller regelbunden trä/MDF-fräsning
- [ ] Planera enkel avtorkningsbar avskärmning/gardin runt CNC-zonen
- [ ] Verifiera att lösningen fångar trä/XPS-spån innan regelbunden användning i motorverkstaden

## 5. Förbered printade/flat parts
- [x] Skrivare: **Bambu Lab P1S, 256×256×256 mm** — tillräcklig; ingen separat byggvolym/skew-gate
- [ ] Provprinta `Z_Stub` + `Z_Nut` och kontrollera passning innan hela satsen
- [ ] Säkerställ senaste LR4-version på alla printade delar
- [ ] Säkerställ uttryckligen **30 mm rail-variant** på alla diameterberoende delar före slicning
- [ ] Säkerställ **Makita/65 mm tool-mount-variant** för VEVOR 0700C
- [ ] Använd högsta aktuella versionsnummer på versionsmärkta filer
- [ ] Granska bridges/unsupported geometry i slicer-preview innan de långa printarna
- [ ] Print kompletta LR4-deluppsättningen i vanlig styv PLA inklusive Jackpot3 board box
- [ ] Kontrollera printade delar och hårdvara
- [ ] Bootstrap med 4 printade temp-struts
- [ ] Generera permanenta struts med `strut_length=819` och `front_wing_size=30`; generatorns ~0,5 mm mindre slutmått är avsiktligt
- [ ] Fräs permanenta strut plates ur 5–6 mm MDF/hardboard

## 6. Bygg bord
- [ ] Montera avtagbar ~1000×1620 CNC-deck på valt bord; skruva/bulta, inte limma
- [ ] Säkerställ stöd/infästning i ytterkanterna där Y-rail, wheels och belt clips arbetar
- [ ] Montera rail/belt-geometri korrekt; belt holders/Y clips använder ytterkanten som referens
- [ ] Montera löstagbar ~12 mm MDF-spoilboard i arbetszonen
- [ ] Lägg till sarg/skydd utan att störa rörelsen
- [ ] Integrera slang-/dammhantering utan att begränsa arbetsområdet
- [ ] Lägg inte tid/pengar på hjul före verkligt behov; fasta ben/fötter först

## 7. Montera maskinen
- [ ] Montera gantry
- [ ] Montera Y-delar
- [ ] Kapa T8×8 först när fysisk assembly kan mätas; sikta ungefär **150–160 mm ×2**
- [ ] Montera T8 fullt sittande i koppling mot motoraxel och kontrollera lätt Z-rörelse utan binding
- [ ] Montera remmar
- [ ] Montera Z
- [ ] Montera VEVOR i 65 mm Makita-format tool mount
- [ ] Provpassa köpt Elaire 1/8"-collet i VEVOR 0700C
- [ ] Kontrollera collet-säte och runout innan riktig fräsning
- [ ] Kontrollera fri mekanisk rörelse över hela slaget
- [ ] Rikta/squara maskinen

## 8. Elektronik / fysisk kabelintegration
- [ ] Montera Jackpot3 i rätt board box på rörlig beam/YZ_Min-sida
- [ ] Dra kablar **bredvid**, inte över Jackpot3 eller dess antenn; avlasta anslutningar innan kablar lämnar boxen
- [ ] Lämna fri luftväg; köp ingen fläkt innan verkligt behov visas
- [ ] Elecrow-kort: flasha V1E:s aktuellt testade FluidNC + rätt LR4-konfiguration **innan driven rörelse/homing**
- [ ] Verifiera data-kapabel USB-C före flashing
- [ ] Verifiera FAT32 microSD om det ska användas för G-code
- [ ] Koppla motorer; verifiera coil-pair/connector-orientering
- [ ] Första motortest 1 mm i taget; vänd motorplugg endast helt spänningslöst om riktning är fel
- [ ] Koppla 5 endstops som NC, COM + NC
- [ ] Verifiera att varje endstop ändrar status korrekt
- [ ] **Kom ihåg:** standard-endstops är bara aktiva under homing, inte runtime hard limits/kollisionsskydd
- [ ] Dry-fit motorernas 1 m-kablar; köp endast de förlängningar som faktiskt behövs
- [ ] Placera fast KJD12/HDR-box så KJD12 är direkt nåbar från normal operatörsplats
- [ ] Dry-fit 24 V-kabel från fast HDR-box till rörlig Jackpot; ingen kontakt får bära kabeldrag
- [ ] Om 24 V-kabeln måste böjas snävt repetitivt i kabelkedja: byt till uttryckligt continuous-flex-kabel innan slutmontage
- [ ] Dry-fit VEVOR:s nätkabel längs samma rörliga system; använd förlängning endast om verklig räckvidd kräver det
- [ ] **Före slutliga clips/remspänning:** kör Core/gantry manuellt till alla fyra hörn + Z-extremer med dammsugarslang, routerkabel, 24 V, stepper- och endstopkablar samtidigt monterade
- [ ] Verifiera inga sträckta ledningar, snäva böjar, snag-punkter eller kabel som kan falla i rörelsezonen
- [ ] Ordna all dragavlastning först efter godkänt full-travel-test
- [ ] Montera KJD12 NVR/maskinstopp; kalla den inte säkerhetsklassad E-stop utan separat verifiering
- [ ] Verifiera homing/squaring och endstop-status

## 9. 230 V / känd 10 A garagegrupp
- [x] Garagegruppen är **10 A** och praktiskt beprövad med svets; plasma har däremot kunnat lösa säkringen
- [ ] Bekräfta DeWalt-typskylt för modellunika data
- [ ] Dry-fit faktisk KJD12-14 + HDR i kapslingen innan håltagning; använd större kapsling om terminal-/böjradie blir trång
- [ ] Följ exakt terminalschema för den KJD12-14-variant som faktiskt levereras
- [ ] KJD12 bryter avsedda L/N-poler; PE förblir kontinuerlig/oswitchad till DeWalt-uttaget
- [ ] Kontrollera faktisk 3G1,5-kabel-OD mot M20-glandens 5–12 mm spann
- [ ] Inga åtkomliga spänningsförande delar med boxen stängd
- [ ] Kontinuitetstesta PE och verifiera ingen L/N→PE-kortslutning före energisering
- [ ] Verifiera NVR/no-restart-funktionen med router frånkopplad
- [ ] Vid första samtidiga DeWalt + VEVOR-körningen: vanlig sanity-check att gruppen håller. **Ingen separat elutredning om inget faktiskt problem uppstår**
- [ ] Uppsäkra aldrig gruppen som workaround utan kontroll av fasta installationen

## 10. Driftsättning
- [ ] Torrkör utan fräs
- [ ] Verifiera full rörelse ännu en gång under driven jogg, börja 1 mm i taget
- [ ] Plana spoilboard
- [ ] Kontrollera X/Y-mått
- [ ] Kontrollera diagonaler/squareness
- [ ] Kontrollera Z-djup
- [ ] Fräs kalibreringsbit
- [ ] Spara fungerande grundinställningar/config-backup

## 11. Första riktiga jobb
- [ ] Enkel testbit i skum eller billigt trä
- [ ] Plywood
- [ ] Halloween-gravsten/XPS först när damm + statisk jordning är verifierade
- [ ] Massivt trä
- [ ] Dokumentera feeds/speeds som faktiskt fungerar

## Senare — inte nu
- [ ] Laser tidigast 2027
- [ ] Lång 3,175 mm plywoodfräs först när ett faktiskt 18–19 mm genomskärningsjobb finns
- [ ] T-track / insert-grid / vacuum-table endast efter verkligt behov