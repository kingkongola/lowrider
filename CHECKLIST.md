# Checklist

## 1. Beställningar — nu

- [ ] Allegro / `4Makers_pl`: 6× smooth idler `KSG1020T`, 5×1 m fiberglass GT2 `GT210WS1M`, 3× 16T/5mm/10mm drive pulley, 2× `SPE5X8`, 1× standard Tr8×8 brass nut `NAKMOS8L`; verifiera Sverige + faktisk frakt
- [ ] **ta bort** 4Makers `TR8X2 400MM` ur korgen: fel 2 mm lead och dessutom märkt ny med defekt
- [ ] Allegro / `ABC-RC_pl`: 1× `THSL-400-8D`, T8×8 400 mm + bronsmutter, offer `17625893658`; verifiera Sverige + faktisk frakt
- [ ] innan betalning på Allegro: kontrollera att remraden är qty 5 och fortfarande säger sammanhängande stycke; kontrollera att det bara ligger **1 extra mutter** från 4Makers
- [ ] DigiKey-korg exakt enligt `PROCUREMENT.md`; kontrollera 0 kr frakt och ingen Marketplace-rad
- [ ] StepperOnline `5-17HS19-2004S1` fempack från Germany warehouse; läs Sverige-frakt i checkout
- [x] Elecrow Jackpot3 `CQA240812C2` — köpt 2026-09-03, **937 kr faktiskt debiterat**, DDP Economy
- [ ] VEVOR EU 0700C `YXKXBJ710W65AH7WLV2`; välj Sverige som destination och läs slutpris
- [ ] 3 × eSUN PLA Basic Black 1,75 mm / 1 kg från 3DJake; baseline 559 kr inkl standardfrakt

**Roboter-Bausatz är blockerad. LaskaKit är fallback, inte en order vi lägger nu.**

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
- [ ] kapa remmen först när routing verifierats; målsegment 999 / 1705 / 1705 mm
- [ ] montera 16T/rem/idlers
- [ ] montera VEVOR i 65 mm mount
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
- [ ] dry-fit VEVOR-kabel
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
- [ ] första samtidiga DeWalt + VEVOR: kontrollera att 10 A-gruppen håller; utred bara om den faktiskt löser

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
