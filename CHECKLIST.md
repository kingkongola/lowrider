# Checklist

## 1. Inventera köpta delar
- [x] HaWiWe-order dokumenterad
- [x] HaWiWe-order betald
- [x] Markera exakt vad som täcks av skruvsatsen
- [ ] När paketet kommer: fysisk inventering mot BOM

## 2. Geometri / bord
- [x] Lås arbetsyta: **650 × 1250 mm**
- [x] Verifiera aktuell LR4-kalkylator med köpta 6,0 mm XZ-plattor
- [x] Lås maskingeometri: rör **816 / 816 / 1505 mm**, strut **819 mm**, rem **999 / 1705 / 1705 mm**
- [x] Lås minimum bord: **941 × 1563 mm** och praktisk CNC-deck cirka **1000 × 1620 mm**
- [x] Välj huvudarkitektur: styvt begagnat 180×90/100-bord + avtagbar CNC-deck
- [ ] Hitta/köp faktiskt begagnat bord och gör femminuters rackingtest
- [ ] Mät faktisk bordshöjd och underrede
- [ ] Kontrollera totalhöjd och frigång för slang/kablar på det valda bordet
- [ ] Köp/inspektera Motonet-rör och kapa först efter fysisk kontroll av OD/rakhet

## 3. Köp/ordna det som saknas
- [ ] PLA, cirka 2,7 kg behövs; nuvarande plan 6 × 1 kg SUNLU ordinary PLA om checkout håller
- [ ] Jackpot3
- [ ] 5 × StepperOnline `17HS19-2004S1`
- [ ] LaskaKit-korg: idlers, 5 m GT2-rem, T8, muttrar, kopplingar och lågspänningskablage
- [ ] 3 × exakta GT2 16T / 5 mm / 10 mm remhjul
- [ ] 14 × 608-2RS; köp 16–20 enligt aktuell checkout, exact 8×22×7 / 2RS
- [ ] DigiKey: Mean Well `HDR-60-24` + 10 × Omron `SS-3GL13PT`
- [ ] VEVOR 0700C 800 W router
- [ ] genuin KEDU KJD12/NVR eller dokumenterad fallback enligt research
- [ ] kompakt IP65 el-kapsling + nätfördelningssmåsaker efter fysisk dry-fit av KJD12/HDR
- [ ] bordsmaterial/CNC-deck efter valt begagnat bord
- [ ] ~12 mm MDF-spoilboard
- [ ] 3 × Sorotec `L1S.M.0317` för commissioning
- [ ] kabelhantering
- [ ] arbetsstyckesfastsättning — börja med skruv/tabs i spoilboard, inget T-track-kit nu

## 4. Dammhantering — grundkrav
- [ ] Välj/printa LR4 dust shoe
- [x] Grovdammsugare/shop-vac finns: DeWalt, sannolikt DXV30SAPTA
- [ ] Printa cyklonavskiljare
- [ ] Ordna separat styv 15–30 l uppsamlingsbehållare
- [ ] Testa befintlig DeWalt 48 mm × 2,1 m slang innan ny slang köps
- [ ] Bygg slangupphängning/dragavlastning som inte belastar gantry/Z
- [ ] Planera enkel avtorkningsbar avskärmning/gardin runt CNC-zonen
- [ ] Verifiera att lösningen fångar trä/XPS-spån innan regelbunden användning i motorverkstaden

## 5. Förbered delar
- [ ] Säkerställ rätt LR4-version på alla printade delar
- [ ] Print kompletta LR4-deluppsättningen i vanlig styv PLA
- [ ] Kontrollera printade delar och hårdvara
- [ ] Bootstrap med printade temp-struts
- [ ] Fräs permanenta 819 mm strut plates ur 5–6 mm MDF/hardboard

## 6. Bygg bord
- [ ] Montera avtagbar ~1000×1620 CNC-deck på valt bord; skruva/bulta, inte limma
- [ ] Montera rail/belt-geometri korrekt
- [ ] Montera löstagbar ~12 mm MDF-spoilboard
- [ ] Lägg till sarg/skydd utan att störa rörelsen
- [ ] Integrera slang-/dammhantering utan att begränsa arbetsområdet
- [ ] Lägg inte tid/pengar på hjul före verkligt behov; fasta ben/fötter först

## 7. Montera maskinen
- [ ] Montera gantry
- [ ] Montera Y-delar
- [ ] Montera remmar
- [ ] Montera Z
- [ ] Montera router/spindel
- [ ] Provpassa köpt Elaire 1/8"-collet i VEVOR 0700C
- [ ] Kontrollera collet-säte och runout innan riktig fräsning
- [ ] Kontrollera fri rörelse över hela slaget
- [ ] Rikta/squara maskinen

## 8. Elektronik
- [ ] Montera Jackpot3
- [ ] Koppla motorer
- [ ] Koppla 5 endstops som NC, COM + NC
- [ ] Dry-fit motorernas 1 m-kablar; köp extension endast där service-loop saknas
- [ ] Ordna dragavlastning och kabelhantering
- [ ] Montera säker maskinmatning/NVR och nödstopp
- [ ] Verifiera motorriktning
- [ ] Verifiera homing/squaring

## 9. Driftsättning
- [ ] Torrkör utan fräs
- [ ] Plana spoilboard
- [ ] Kontrollera X/Y-mått
- [ ] Kontrollera diagonaler/squareness
- [ ] Kontrollera Z-djup
- [ ] Fräs kalibreringsbit
- [ ] Spara fungerande grundinställningar

## 10. Första riktiga jobb
- [ ] Enkel testbit i skum eller billigt trä
- [ ] Plywood
- [ ] Halloween-gravsten/XPS när dammhanteringen är verifierad
- [ ] Massivt trä
- [ ] Dokumentera feeds/speeds som faktiskt fungerar

## Senare — inte nu
- [ ] Laser tidigast 2027
- [ ] Lång 3,175 mm plywoodfräs först när ett faktiskt 18–19 mm genomskärningsjobb finns
- [ ] T-track / insert-grid / vacuum-table endast efter verkligt behov
