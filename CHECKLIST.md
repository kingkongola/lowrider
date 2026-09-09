# Checklist

## 1. Beställningar — nu

- [x] LaskaKit mekanikkärna — köpt 2026-09-03 för **444 kr faktiskt debiterat**
- [x] 4 × **T8×8 brass nut, 2 mm pitch / 4-start / 8 mm lead** — Amazon.se/euroharry, **101,76 kr visat orderpris**
- [x] 3 × GT2/2GT drive pulley **16T / 5 mm bore / 10 mm belt / 2 mm pitch** — eBay/POWGE, **72 kr**
- [x] DigiKey — PSU, endstops, 608-lager, Wago, glands, Faston, kablage och pigtails, **986,98 kr**; **mottaget/hämtat 2026-09-09**
- [x] 5 × STEPPERONLINE `17HS19-2004S1` — Amazon.se, **608,37 kr visat orderpris**
- [x] Elecrow Jackpot3 `CQA240812C2` — **937 kr**
- [x] KATSU `101750` router — Amazon.se, **620,00 kr visat orderpris**
- [x] **3 kg PLA 1,75 mm från PrintOnion** — **426 kr**
- [x] **2 × Motonet-rör** — köpt 2026-09-07 för **340 kr totalt**; planerad spec Ø30×1,5×2000 mm

**Kärnmekanik, elektronik, router, filament och rör är nu köpta/beställda.**

## 2. Lokalt / fysiskt

- [ ] räkna av DigiKey-paketets innehåll mot BOM före montering
- [ ] verifiera de köpta Motonet-rörens faktiska OD/rakhet/längd före kapning
- [ ] kapa rör först därefter: 1505 / 816 / 816
- [ ] hitta styvt begagnat **180×90 cm** bord, helst ≤700 kr; 180×100 cm är jackpot
- [ ] femminuters rackingtest + mät höjd/underrede
- [ ] markera 941×1563 mm footprint och planera smal lokal kantbreddning eftersom 900 mm bord är cirka 41 mm för smalt totalt

## 3. När HaWiWe anländer

- [ ] kontrollera transportskada
- [ ] kontrollera fyra produktgrupper: XZ-plattor, 4 rails, screw set, collet
- [ ] provmontera M3×10 mot 6,0 mm XZ/MGN-block; inget bottnar/binder

## 4. Prints

- [ ] hämta senaste LR4-filer
- [ ] verifiera **30 mm** på alla railberoende delar
- [ ] verifiera **Makita/65 mm** tool mount
- [ ] provprinta `Z_Stub` + `Z_Nut`
- [ ] kontrollera passning
- [ ] granska slicer bridges/unsupported geometry
- [ ] printa komplett LR4-sats + rätt Jackpot3 board box
- [ ] printa bootstrap temp-struts
- [ ] generera permanenta struts `819`, `front_wing_size=30`

## 5. Bord / spoilboard

- [ ] använd den befintliga styva bordsskivan direkt som strukturell maskinbas
- [ ] köp **inte** hel OSB/ply-deck om inte verkligt behov uppstår
- [ ] bygg bara smal lokal kantbreddning/rail-support för 90 cm bord efter dry-fit
- [ ] montera löstagbar ~12 mm MDF-spoilboard över arbetszonen
- [ ] inget T-track före faktiskt behov

## 6. Mekanik

- [ ] montera gantry/Y/Z
- [ ] kapa T8 efter verklig assembly-check, cirka 150–160 mm ×2
- [ ] kontrollera lätt Z-rörelse utan binding
- [ ] kapa 5 m-remmen först när routing verifierats; målsegment 999 / 1705 / 1705 mm
- [ ] montera 16T/rem/idlers
- [ ] montera KATSU `101750` i Makita/65 mm mount
- [ ] provpassa Elaire-collet
- [ ] kontrollera runout
- [ ] kontrollera fri manuell rörelse över hela slaget
- [ ] squara maskinen

## 7. Damm

- [ ] bekräfta DeWalt-typskylt
- [ ] printa LR4 dust shoe
- [ ] prova befintlig TPU till bristles
- [ ] printa cyklon
- [ ] ordna 15–30 l styv behållare
- [ ] vakuumtesta behållare/lock kontrollerat
- [ ] testa befintlig DeWalt-slang innan ny slang köps
- [ ] bygg slangavlastning
- [ ] lös statisk jordväg före XPS/reguljär MDF/trä-drift

## 8. Controller/lågspänning

- [ ] inventera data-USB-C
- [ ] inventera FAT32 microSD >2 GB
- [ ] när Jackpot3 anländer: kontrollera transportskada/korrekt kort
- [ ] montera Jackpot3 luftigt på rörlig beam/YZ_Min-sida
- [ ] flasha V1E:s då aktuellt testade FluidNC + rätt LR4-config
- [ ] koppla motorer
- [ ] första jogg 1 mm
- [ ] koppla 5 endstops NC via COM+NC
- [ ] verifiera varje endstopstatus

## 9. NVR/elbox + full travel

- [ ] välj NVR efter faktisk variant/schema; Clas Ohlson KJD12 230 V/10 A är aktiv kandidat
- [ ] dry-fit NVR + HDR innan kapsling/håltagning låses
- [ ] placera stoppet direkt nåbart
- [ ] dry-fit 3 m 24 V-rutt
- [ ] dry-fit KATSU-kabel
- [ ] dry-fit motor/endstop
- [ ] montera vac-hose samtidigt
- [ ] kör manuellt alla fyra hörn + Z-extremer
- [ ] slutlig dragavlastning först efter godkänt full-travel-test

## 10. 230 V verifiering

- [ ] följ exakt terminalschema
- [ ] PE kontinuerlig/oswitchad
- [ ] kontrollera kabel-OD mot glands
- [ ] inga åtkomliga live-delar med boxen stängd
- [ ] kontinuitetstesta PE
- [ ] verifiera ingen L/N→PE-kortslutning
- [ ] verifiera NVR/no-restart med router frånkopplad

## 11. Driftsättning

- [ ] torrkör utan fräs
- [ ] verifiera full driven travel
- [ ] plana spoilboard
- [ ] kontrollera X/Y-mått + diagonaler
- [ ] kontrollera Z-djup
- [ ] fräs kalibreringsbit
- [ ] spara fungerande config-backup
- [ ] första enkla jobb i billigt material

## Senare — inte nu

- [ ] hel deck/torsionsbox endast om det faktiska bordet visar att det behövs
- [ ] Sorotec/extra fräsorder när första verkliga fräsbehoven är kända
- [ ] router-/stepperförlängning endast om dry-fit kräver
- [ ] T-track/insert-grid/vacuum-table efter erfarenhet
- [ ] laser tidigast 2027
- [ ] plasma utanför detta bygge
