---
research_date: 2026-08-30
scope: live line-by-line checkout audit after physical/system audit
status: current procurement evidence
region: Sweden / EU
---

# Live cart audit — 2026-08-30

Goal: verify every remaining purchase is the right exact part and physically compatible with this LR4. Checkout-only freight/tax stays explicitly unresolved.

## Known constraints

- Printer: **Bambu Lab P1S, 256×256×256 mm**. V1E's 200×200×190 mm minimum is already satisfied. No printer-capability gate remains; only correct LR4 variant, slicer preview and a small `Z_Stub`/`Z_Nut` fit print.
- Garage circuit: **10 A**. If the owned DeWalt is confirmed as DXV30SAPTA, rated input powers are about 1050 W vacuum + 800 W router + <=60 W controller PSU = ~1.91 kW, equivalent to ~8.3 A real power at 230 V. This is not a guaranteed RMS-current measurement; startup, power factor and other loads still matter.

### VEVOR 6.5 A text checked

VEVOR's 220–240 V EU product page repeats marketing text saying “6.5A motor”, but the same 6.5 A wording is used for the 120 V / 800 W US version. 800 W / 120 V is ~6.7 A, making this strongly indicative of reused 120 V marketing copy rather than a verified 230 V current rating.

The actual 0700C manual lists:
- 120 V / 60 Hz **or** 220–240 V / 50 Hz
- 800 W
- 10,000–30,000 rpm

It does not state 6.5 A for the EU version. Therefore the project does **not** use 6.5 A as the EU router current. The 10 A circuit is still close enough to require a staged real-world load test.

## LaskaKit — GREEN except board-side connector choice

Current live status:
- `LA190008E` — smooth GT2 idler, 5 mm bearing hole, for 10 mm belt — in stock
- `LA190032A` — T8×8 400 mm rod — in stock
- `LA190033A` — T8×8 brass nut — in stock
- `LA190031` — 5→8 mm flexible coupling — in stock
- `LA190013C` — 5 m / 10 mm fiberglass GT2 belt — **in stock now**; prefer this over 3×2 m fallback
- `LA150151A` — 26 AWG 3-core endstop cable — in stock
- UL2464 20 AWG 2-core cable — available; nominal OD about 4.8 mm
- published GLS Sweden shipping: €8.93

Use the 20 AWG cable with a broad relaxed moving loop. UL2464/PVC does not itself prove drag-chain/continuous-flex rating.

Board-side endstop pigtails/connectors remain needed. Elecrow's five two-wire terminal plugs are not evidence that the five endstop header connectors are included.

## StepperOnline Germany — GREEN / checkout shipping only

Exact motor pack:
- `5-17HS19-2004S1`
- five NEMA17 motors
- 59 Ncm, 2 A
- 5 mm D-shaft, 24 mm shaft
- 1 m cable
- Germany warehouse selectable
- current product in stock

Germany warehouse supports Sweden. Keep this order motors-only.

## DigiKey — GREEN after two corrections

Exact ordinary DigiKey-stock cart:
- Mean Well `HDR-60-24` / `1866-2249-ND` ×1
- Omron `SS-3GL13PT` / `SW768-ND` ×10
- `608-2RS-W/CHEVRONSRI2` / `1995-1010-ND` ×16
- Wago `221-413` ×3
- Altech `5309 720/SET` M20, 5–12 mm ×2 for 3G1.5 mains in/out
- TE Connectivity `3-350820-2` **DigiKey `A27824-ND`** ×10
- Amphenol `AIO-CSM12` M12, 3–6.5 mm, IP68 ×1 for the ~4.8 mm 24 V cable

### Faston duplicate listing trap

`3-350820-2` appears twice at DigiKey:
- **correct:** `A27824-ND`, ordinary DigiKey stock, single-piece ordering
- **wrong route:** `5831-3-350820-2-ND`, Marketplace, minimum 1000 and separate shipping may apply

Use `A27824-ND`.

### 24 V gland resolved

`AIO-CSM12`:
- 3–6.5 mm cable range
- M12×1.5
- IP68
- panel nut + sealing nut included

This fits the nominal ~4.8 mm LaskaKit cable and removes the previous LV-gland orphan.

### Current price sanity check

Original six lines: about **494.48 SEK ex VAT / 618.10 SEK incl VAT** at current displayed tiers. Adding `AIO-CSM12`: about **513.17 SEK ex VAT / 641.46 SEK incl VAT**.

DigiKey states free Sweden shipping at order value >=615 SEK and 170 SEK below it, but the public help page does not clearly state whether the threshold is applied before or after VAT. Checkout is authoritative. Do not buy filler if freight remains.

## Jackpot3 / Elecrow — GREEN / landed cost checkout-only

Exact:
- Elecrow `CQA240812C2`
- current $76.99
- in stock
- requires flashing for LR4

Package text lists controller board, five two-wire terminal plugs and six adhesive heatsinks. It does **not** list a microSD card.

Commissioning dependencies:
- data-capable USB-C cable
- FAT32 microSD >2 GB, preferably Class 4/6 per V1E, if one is not already owned
- current V1E-tested FluidNC + correct LR4 config before motor motion

## GT2 16T pulley — GREEN exact part / Sweden freight checkout-only

Allegro exact offer is live:
- `GT2-16T-5B_10mm_K`
- GT2 / 2 mm pitch
- 16 teeth
- 5 mm bore
- for 10 mm belt
- current 7.20 PLN each

Need 3. Do not substitute LaskaKit's indexed 16T pulley because that one is for 6 mm belt.

## Sorotec cutters — GREEN

Exact `L1S.M.0317`:
- 3.175 mm diameter and shank
- single flute
- 9 mm cutting length
- 38 mm overall
- current €3.70 each
- immediately available / 2–3 days

Three remain the commissioning choice. They are intentionally not the future 18–19 mm plywood cutter.

## SUNLU PLA — GREEN if Sweden checkout holds

Official ordinary PLA bulk page currently shows:
- MOQ 6 kg
- 6-roll tier from €9.19/kg
- 1 kg normal rolls
- Europe shipping option

Keep **ordinary PLA** unless a concrete reason appears to switch formulation.

## KEDU machine stop — GREEN by specification; freight checkout-only

The exact family can now be narrowed to **genuine KEDU KJD12-14**.

KEDU's KJD12-14 datasheet verifies:
- 18 A AC-1 / **15 A AC-3** under EN60947/TÜV column
- 220–240 V coil option; order code `V3` is 230 V / 50 Hz
- Faston 6.3×0.8 mm
- IP54
- accessory `A3` is the emergency-stop button + waterproof cover

CEM Elettromeccanica's current listing is genuine KEDU, bipolar, mushroom emergency-stop actuator, 6.3×0.8 Faston, EN60947, VDE/TÜV and IP54. CEM's own eBay listing identifies the manufacturer part as **KJD12-14**.

Therefore preferred purchase target is:
- **KEDU KJD12-14**
- 230 V / 50 Hz
- 2-pole NVR
- red mushroom/yellow cover
- 15 A AC-3 family rating
- 6.3×0.8 Faston

CEM direct/eBay are current concrete sources; Sweden freight remains checkout-only.

Terminology remains deliberately conservative: this is the machine's **NVR/maskinstopp**. The project does not claim that the finished homemade circuit is a safety-rated emergency-stop system merely because the actuator is sold as an emergency-stop accessory.

## 10 A circuit consequence

The 10 A garage group is not currently a reason to abandon the 800 W router + DeWalt plan. Commissioning is staged:
1. identify B10/C10/etc and shared loads
2. confirm actual DeWalt model/nameplate
3. run DeWalt alone
4. run controller + DeWalt AUTO + router unloaded
5. test normal cutting with no other heavy loads on the group
6. if nuisance trips occur, solve circuit/load architecture rather than changing protection blindly

## Current order status

**Ready by specification; only checkout total remains:**
- LaskaKit
- StepperOnline Germany
- Elecrow Jackpot3
- SUNLU ordinary PLA
- Sorotec cutters
- Allegro 16T
- CEM/eBay genuine KEDU KJD12-14

**Ready by specification; checkout plus SKU discipline:**
- DigiKey — use `A27824-ND`, add `AIO-CSM12`

**Must be physically inspected rather than web-researched further:**
- Motonet tubes
- actual used table
- VEVOR/Elaire collet/runout after arrival
- DeWalt model label
- 10 A circuit behaviour under actual combined load
