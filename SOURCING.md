# Sourcing plan — current 2026-08-30

Mål: rätt variant, låg total kostnad inklusive frakt och så få beställningar som ekonomiskt rimligt. `PROCUREMENT.md` är kanonisk orderöversikt; `AUDIT.md` är kanonisk fysisk kontroll.

## Låst

- LowRider V4, **650×1250 mm**
- deck ~**1000×1620 mm**
- rails **Ø30×1,5 mm** → 30 mm-printvariant
- Bambu Lab **P1S** → printkapacitet redan löst
- Jackpot3
- VEVOR 0700C 800 W / 65 mm
- Mean Well HDR-60-24
- Omron SS-3GL13PT
- StepperOnline `5-17HS19-2004S1`
- garagegrupp **10 A**, praktiskt beprövad med svets; CNC är inte en öppen elfråga

## Redan betalt

HaWiWe **165,50 € inkl 8 € frakt**:
- 6,0 mm XZ plates
- 4 × MGN12H 150 mm
- LR4 screw set
- Elaire/Makita-style 1/8" collet

## Aktuella köpvägar

### Motonet — rör
- 2 × `88-7123`, Ø30×1,5×2000 mm
- mät OD/rakhet innan köp/kapning
- kapa 1505 / 816 / 816

### LaskaKit — mekanik + lågspänning, **utan GT2-rem just nu**
- 6 × `LA190008E` smooth idlers
- 1 × `LA190032A` T8×8 400 mm
- 2 × `LA190033A` T8×8 brass nuts
- 2 × `LA190031` 5→8 couplers
- 10 m `LA150151A` endstop cable
- 3 m UL2464 20 AWG / ~0,52 mm² 2-core
- board-side endstopkontakter/pigtails efter crimperläge

LaskaKits direkta produktsida visar nu både 5 m- och 2 m-versionen av 10 mm fiberglass GT2 som slut. Äldre kategoridata var stale.

### GT2-rem — ny separat rad

Krav:
- GT2 / 2 mm pitch
- **10 mm bred**
- gummi/neopren
- **glasfiberkord, inte stål**
- kontinuerliga segment minst 999 / 1705 / 1705 mm

**Nuvarande bästa verifierade EU-värde:** Roboter-Bausatz `RBS12747`:
- 10 mm
- GT2 / 2 mm
- gummi + glasfiber
- meterware
- live i lager
- **€2,25/m vid 5 m = €11,25 före frakt**

Alternativ:
- V1E:s egen Amazon-länk/SeekLiny ASIN `B097T4DFM6`, 10 m / 10 mm / fiberglass — Sverige/Prime checkout måste verifieras
- Technobots `6002-591`, 5 m / 10 mm fiberglass — exakt men UK-frakt/import gör den sekundär

### StepperOnline Germany — motorer
- 1 × fempack `5-17HS19-2004S1`
- Germany warehouse, live i lager
- frakt till Sverige checkout-gated

### DigiKey — konsoliderad korg
- HDR-60-24 ×1
- Omron `SS-3GL13PT` ×10
- exact 608-2RS ×16
- Wago 221-413 ×3
- Altech M20 5–12 mm ×2
- TE `3-350820-2` ×10 — **använd DigiKey `A27824-ND`, inte Marketplace-dubbletten**
- Amphenol `AIO-CSM12` ×1 — M12 / 3–6,5 mm / IP68 för ~4,8 mm 24 V-kabel

Senaste sanitetssumma ~641 kr inkl moms med LV-glanden. DigiKey-frakt är fortfarande checkout-gated; köp ingen filler.

### VEVOR EU — router
- exakt 0700C, SKU `YXKXBJ710W65AH7WLV2`
- 220–240 V / 800 W / 65 mm
- provpassa Elaire-collet + kontrollera runout

### Elecrow — Jackpot3
- `CQA240812C2`, live $76.99/in stock i senaste kontroll
- flasha/configurera för LR4
- microSD listas inte; inventera hemma
- data-USB-C inventeras hemma

### SUNLU — PLA
- ordinary PLA
- ca 2,7 kg behövs; bulkplan 6×1 kg om Sverige-checkout håller ~100–110 kr/kg

### Sorotec — första frässtål
- 3 × `L1S.M.0317`
- 3,175 mm single flute / 9 mm skärlängd
- live €3,70/st i senaste kontroll

### Allegro — 16T orphan
- 3 × `GT2-16T-5B_10mm_K`
- exact 16T / 5 mm bore / 10 mm belt
- live ~7,20 PLN/st i senaste kontroll

### KEDU — NVR/maskinstopp
- **genuine KEDU KJD12-14**
- 230 V / 50 Hz
- 2-polig NVR
- röd svamp/gul kåpa
- 6,3×0,8 Faston
- KJD12-14-familjen verifierad **15 A AC-3 / 18 A AC-1**
- CEM/eBay är konkret aktuell källa; Sverige-frakt checkout-gated

### Biltema — elbox
- `35-0065` 4-modul först efter fysisk KJD12/HDR dry-fit
- `35-0067` större fallback
- `46-3610` 3 m 3G1,5 donor cord om faktisk in+ut-längd räcker

## Bord

- begagnat styvt **160–180 × helst 90–100 cm**
- helst ≤700 kr
- befintlig skiva kvar
- avtagbar ~1000×1620 deck + ~12 mm MDF-spoilboard
- 90 cm bord kräver lokalt stöd/infästning under ~50 mm decköverhäng i LR4:s kantzon

## Ska inte köpas ännu

- stepperextensioner före dry-fit
- routerförlängning före full-travel dry-fit
- microSD/USB-C före inventering
- Jackpot-fläkt före faktiskt behov
- extra collet
- lång plywoodfräs
- T-track/vacuum-table
- ny vac/slang före DeWalt-test

## Nästa sourcingarbete

1. checkout Roboter-Bausatz 5 m `RBS12747` och jämför landad kostnad mot V1E Amazon-ASIN med Prime
2. checkout Allegro 16T
3. checkout låsta huvudkorgar
4. fysisk Motonet-rörkontroll
5. faktiskt begagnat bord

Bred komponentjakt är avslutad om inget konkret pris-/lager-/passformsproblem uppstår.