---
research_date: 2026-08-30
scope: live line-by-line checkout audit after physical/system audit
status: current procurement evidence
region: Sweden / EU
---

# Live cart audit — 2026-08-30

Goal: verify that every remaining purchase is the right exact part, in stock where visible, and physically compatible with the actual LR4 build. Checkout-only freight/tax stays explicitly unresolved.

## Known project constraints corrected before checkout

- Printer is **Bambu Lab P1S, 256×256×256 mm**. V1E's 200×200×190 mm minimum is therefore already satisfied. No separate printer-capability gate remains; only correct LR4 variant, slicer preview and a small `Z_Stub`/`Z_Nut` fit print remain sensible.
- Garage circuit is **10 A**, not 16 A. If the owned DeWalt is confirmed as DXV30SAPTA, nominal simultaneous load is about 1050 W vacuum + 800 W router + <=60 W controller PSU = ~1.91 kW / ~8.3 A at 230 V. That is below 10 A continuously but leaves limited margin for other loads and startup transients. Do not up-fuse as a workaround; test the real circuit and identify breaker characteristic/shared loads.

## LaskaKit — GREEN, except board-side connector choice

Current live status:
- `LA190008E` — smooth GT2 idler, 5 mm bearing hole, for 10 mm belt — in stock
- `LA190032A` — T8×8 400 mm rod — in stock
- `LA190033A` — T8×8 brass nut — in stock
- `LA190031` — 5→8 mm flexible coupling — in stock
- `LA190013C` — 5 m / 10 mm fiberglass GT2 belt — **in stock now**; this is preferred over the 3×2 m fallback
- `LA150151A` — 26 AWG 3-core endstop cable — in stock
- UL2464 20 AWG 2-core cable — available; nominal OD about 4.8 mm
- published GLS Sweden shipping: €8.93

Keep the 20 AWG cable only if routing can use a broad relaxed moving loop. UL2464/PVC does not itself prove drag-chain/continuous-flex rating.

Board-side endstop pigtails/connectors remain needed. The five two-wire terminal plugs listed with Elecrow Jackpot3 are not evidence that the five endstop header connectors are included; do not delete this BOM line.

## StepperOnline Germany — GREEN / checkout shipping only

Exact motor pack:
- `5-17HS19-2004S1`
- five NEMA17 motors
- 59 Ncm
- 2 A
- 5 mm D-shaft
- 24 mm shaft
- 1 m cable
- Germany warehouse selectable
- current product in stock

Germany warehouse supports Sweden. Shipping total is cart/checkout-only. Keep this order motors-only.

## DigiKey — GREEN after two corrections

Exact ordinary DigiKey-stock cart:
- Mean Well `HDR-60-24` / `1866-2249-ND` ×1
- Omron `SS-3GL13PT` / `SW768-ND` ×10
- `608-2RS-W/CHEVRONSRI2` / `1995-1010-ND` ×16
- Wago `221-413` ×3
- Altech `5309 720/SET` M20 5–12 mm ×2 for 3G1.5 mains in/out
- TE Connectivity `3-350820-2` **DigiKey `A27824-ND`** ×10
- Amphenol `AIO-CSM12` M12, 3–6.5 mm, IP68 ×1 for the ~4.8 mm 24 V cable

### Correction 1 — Faston duplicate listing trap

`3-350820-2` appears twice at DigiKey:
- **correct:** `A27824-ND`, ordinary DigiKey stock, single-piece ordering, large stock
- **wrong route:** `5831-3-350820-2-ND`, Marketplace, minimum 1000 and separate shipping may apply

Always use `A27824-ND`.

### Correction 2 — move the missing 24 V gland into this cart

`AIO-CSM12`:
- 3–6.5 mm cable range
- M12×1.5
- IP68
- includes panel nut and sealing nut
- large DigiKey stock

This directly fits the nominal ~4.8 mm LaskaKit 20 AWG 2-core cable and removes the prior unresolved 'small LV gland' orphan line.

### Current price sanity check

Using current displayed ex-VAT prices/tiers for the original six lines gives about **494.48 SEK ex VAT / 618.10 SEK incl VAT**. Adding `AIO-CSM12` adds about 18.69 SEK ex VAT, for roughly **513.17 SEK ex VAT / 641.46 SEK incl VAT**.

DigiKey states free Sweden shipping at order value >=615 SEK and 170 SEK below it, but the public help page still does not explicitly state whether the threshold is applied before or after VAT. Therefore **checkout remains authoritative**. Do not buy filler if checkout still charges freight; reconsider genuinely required consolidation instead.

## Jackpot3 / Elecrow — GREEN / landed cost checkout-only

Exact:
- Elecrow `CQA240812C2`
- current $76.99
- in stock
- requires flashing for LR4

Package text lists controller board, five two-wire terminal plugs and six adhesive heatsinks. It does **not** list a microSD card.

Commissioning dependencies:
- data-capable USB-C cable
- simple FAT32 microSD >2 GB, preferably Class 4/6 per V1E, if one is not already owned
- current V1E-tested FluidNC + correct LR4 config before motor motion

## GT2 16T pulley — GREEN exact part / Sweden freight checkout-only

Allegro exact offer is live:
- manufacturer code `GT2-16T-5B_10mm_K`
- GT2 / 2 mm pitch
- 16 teeth
- 5 mm bore
- for 10 mm belt
- current 7.20 PLN each
- 18 shown available in current crawl

Need 3. This is exactly the mechanical orphan spec. Do not substitute LaskaKit's currently available 16T part because their indexed 16T is for **6 mm belt**.

## Sorotec cutters — GREEN

Exact `L1S.M.0317`:
- 3.175 mm diameter
- 3.175 mm shank
- single flute
- 9 mm spiral/cutting length
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
- site says free shipping to most EU regions, but Sweden checkout remains authoritative

Keep **ordinary PLA**, not a random cheaper matte/special formulation, unless a concrete reason appears to switch. P1S makes standard 1 kg spool handling trivial.

## KEDU machine stop — YELLOW, one final variant check remains

Known electrical requirement is now clearer because garage supply is 10 A.

Primary evidence:
- genuine KEDU `KJD12-10ZF`: 230 V / 50 Hz, 2-pole, NVR, 16 A AC-1, **10 A AC-3**, EN60947, IP54, 6.3×0.8 Faston
- KEDU `KJD12-14` family has documented variants around **15 A AC-3** / 18 A AC-1
- CEM Elettromeccanica sells a genuine KEDU KJD12 at €14.90 incl VAT with explicit mushroom emergency-stop actuator, bipolar switching, EN60947, VDE/TUV, IP54 and headline max 15 A/230 V, but its listing does not explicitly separate AC-1 from AC-3

For our ~8.3 A nominal load, a genuine 10 A AC-3 KJD12 is nominally adequate, but the best purchase is a specific unit that combines:
1. 230 V / 50 Hz NVR coil
2. 2-pole switching
3. easy-hit red mushroom/stop cover
4. explicit motor/AC-3 rating >=10 A
5. 6.3×0.8 mm Faston or otherwise matching planned wiring

Do not buy merely because the product title says KJD12 or '15A'. Physical label/datasheet for the delivered variant wins.

## 10 A circuit consequence

The circuit is not a reason to abandon the current 800 W router + DeWalt plan. It is, however, close enough that commissioning should be staged:
1. identify B10/C10/etc and shared loads
2. run DeWalt alone
3. run controller + DeWalt AUTO + router with no cutting load
4. test normal cutting while no other heavy loads share the circuit
5. if nuisance trips occur, solve circuit/load architecture rather than changing protection blindly

## Current order status

**Ready by specification; only checkout total remains:**
- LaskaKit
- StepperOnline Germany
- Elecrow Jackpot3
- SUNLU ordinary PLA
- Sorotec cutters
- Allegro 16T

**Ready by specification; checkout plus one SKU discipline:**
- DigiKey — use ordinary stock `A27824-ND`, add `AIO-CSM12`

**One product/variant decision still worth resolving before purchase:**
- KEDU KJD12 exact variant with emergency actuator + explicit AC-3 >=10 A

**Must be physically inspected rather than web-researched further:**
- Motonet tubes
- actual used table
- VEVOR/Elaire collet/runout after arrival
- DeWalt model label
