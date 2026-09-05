# Checklist

## 1. Beställningar — nu

- [x] LaskaKit mekanikkärna — köpt 2026-09-03 för **444 kr faktiskt debiterat**: 6× `LA190008E`, 1× `LA190032A`, 2× `LA190031`, 1× `LA190013C`; GLS Sweden ingick
- [ ] 2 × **T8×8 brass nut, 4-start / 8 mm lead** — ersättningsköp krävs; HKGY01-order annulleras efter säljarens out-of-stock-besked och eBay visar `The cancellation is pending`
- [x] 3 × GT2/2GT drive pulley **16T / 5 mm bore / 10 mm belt / 2 mm pitch** — köpt via eBay/POWGE 2026-09-03, **72 kr faktiskt debiterat**, fri frakt och importavgifter inkluderade
- [x] DigiKey — köpt 2026-09-03 för **986,98 kr faktiskt debiterat**: PSU, endstops, 608-lager, Wago, glands, Faston, kablage och board-pigtails
- [x] 5 × STEPPERONLINE `17HS19-2004S1` — köpt via Amazon.se 2026-09-03, **608,37 kr visat orderpris**, Prime/fri frakt
- [x] Elecrow Jackpot3 `CQA240812C2` — köpt 2026-09-03, **937 kr faktiskt debiterat**, DDP Economy
- [x] KATSU `101750` router — köpt via Amazon.se 2026-09-03, **620,00 kr visat orderpris**, Prime/fri frakt
- [ ] 3 × eSUN PLA Basic Black 1,75 mm / 1 kg från 3DJake; baseline 559 kr inkl standardfrakt

**Roboter-Bausatz och Allegro är blockerade av faktisk svensk checkout. DMW-spåret är ersatt av eBay/POWGE. VEVOR-routerspåret är stängt; KATSU 101750 är köpt. HKGY01-muttrarna är inte längre ett aktivt köp.**

## 2. Lokalt / fysiskt

- [ ] Motonet: inspektera 2 × `88-7123` Ø30×1,5×2000; köp bara om OD/rakhet håller
- [ ] kapa rör först därefter: 1505 / 816 / 816
- [ ] hitta styvt begagnat bord 160–180 × helst 90–100 cm, helst ≤700 kr
- [ ] femminuters rackingtest + mät höjd/underrede
- [ ] planera lokal kantblockning om 1000 mm deck överhänger 90 cm bord

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

## 5. Bord/deck

- [ ] bygg avtagbar ~1000×1620 structural deck
- [ ] skruva/bulta, inte permanentlimma mot bordet
- [ ] stöd LR4:s rail/wheel/belt-clip-zon vid överhäng
- [ ] montera löstagbar ~12 mm MDF-spoilboard
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
- [ ] kablar bredvid, inte över kort/antenn
- [ ] flasha V1E:s då aktuellt testade FluidNC + rätt LR4-config
- [ ] koppla motorer
- [ ] första jogg 1 mm
- [ ] koppla 5 endstops NC via COM+NC
- [ ] verifiera varje endstopstatus
- [ ] kom ihåg: home/auto-square, inte runtime hard limits

## 9. NVR/elbox + full travel

- [ ] välj NVR efter faktisk variant/schema; Clas Ohlson KJD12 230 V/10 A är aktiv kandidat
- [ ] dry-fit NVR + HDR innan kapsling/håltagning låses
- [ ] placera stoppet direkt nåbart
- [ ] dry-fit 3 m 24 V-rutt
- [ ] dry-fit KATSU-kabel
- [ ] dry-fit motor/endstop
- [ ] montera vac-hose samtidigt
- [ ] kör manuellt alla fyra hörn + Z-extremer
- [ ] inga sträckta ledningar/snagg/kink/kontaktlast
- [ ] slutlig dragavlastning först efter godkänt full-travel-test

## 10. 230 V verifiering

- [ ] följ exakt terminalschema
- [ ] PE kontinuerlig/oswitchad
- [ ] kontrollera kabel-OD mot glands
- [ ] inga åtkomliga live-delar med boxen stängd
- [ ] kontinuitetstesta PE
- [ ] verifiera ingen L/N→PE-kortslutning
- [ ] verifiera NVR/no-restart med router frånkopplad
- [ ] första samtidiga DeWalt + KATSU: kontrollera att 10 A-gruppen håller; utred bara om den faktiskt löser

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

- [ ] Sorotec/extra fräsorder när första verkliga fräsbehoven är kända
- [ ] router-/stepperförlängning endast om dry-fit kräver
- [ ] T-track/insert-grid/vacuum-table efter erfarenhet
- [ ] laser tidigast 2027
- [ ] plasma utanför detta bygge
