---
research_date: 2026-08-30
scope: live line-by-line checkout audit after physical/system audit
status: current procurement evidence
region: Sweden / EU
---

# Live cart audit — 2026-08-30

Goal: verify every remaining purchase is the right exact part and physically compatible with this LR4. Checkout-only freight/tax stays explicitly unresolved.

## Known constraints corrected during audit

- Printer: **Bambu Lab P1S, 256×256×256 mm**. V1E's 200×200×190 minimum is already satisfied. No printer-capability gate remains; only file/variant/testfit control.
- Garage circuit: **10 A**, but this is already empirically proven with a welder. Plasma has tripped it. Therefore the 800 W router + DeWalt plan is not treated as an open electrical problem; normal first-run sanity check is enough unless the breaker actually trips.

## VEVOR 6.5 A text checked

VEVOR's 220–240 V product page repeats “6.5A motor”, but the same text appears on the 120 V / 800 W version, where 6.5–6.7 A is numerically plausible. The 0700C manual lists 220–240 V / 50 Hz and 800 W for the EU version and does not state 6.5 A.

Conclusion: do **not** use 6.5 A as the EU router current rating.

## LaskaKit — GREEN except GT2 belt and board-side connector choice

Current live status:
- `LA190008E` smooth GT2 idler — available
- `LA190032A` T8×8 400 mm — available
- `LA190033A` T8×8 brass nut — available
- `LA190031` 5→8 mm flexible coupling — available
- `LA150151A` endstop cable — available
- UL2464 20 AWG 2-core — available, nominal OD ~4.8 mm

### Important stock correction — GT2 belt

An older category crawl indicated `LA190013C` 5 m / 10 mm fiberglass GT2 in stock. Opening the **direct product page** showed it as **currently unavailable/sold out**. The 2 m 10 mm alternative on that same direct page was also unavailable.

Direct product status supersedes the stale category result. Remove the belt from the LaskaKit cart for now; do not change belt specification.

## GT2 belt replacement — resolved by specification

Exact required belt:
- GT2 / 2 mm pitch
- 10 mm width
- rubber/neoprene body
- fiberglass tensile cord, not steel
- continuous segments 999 / 1705 / 1705 mm

### Current best verified EU value: Roboter-Bausatz `RBS12747`

Live product page:
- open GT2 belt
- 10 mm width
- 2 mm pitch
- rubber with fiberglass weave/core
- sold as meterware
- immediately available
- qty 5 tier: **€2.25/m**, so 5 m = **€11.25 before freight**

Five continuous metres are sufficient for the exact 4409 mm total with ~591 mm margin. Checkout/order note must confirm that qty 5 meterware is supplied continuously rather than five pre-cut 1 m pieces; the product wording strongly implies running meterware, but the physical delivered length matters.

### Other exact alternatives

- V1E's current official belt link resolves to Amazon ASIN `B097T4DFM6` (SeekLiny), documented elsewhere as 10 m, GT2/2 mm, 10 mm, rubber + fiberglass. User has Prime, but Sweden offer/Prime status and landed price are checkout-only.
- Technobots `6002-591`: 5 m, 10 mm, 2 mm pitch, fiberglass reinforced, live in stock; UK friction makes it secondary.
- Roboter-Bausatz also has premium Gates/PowerGrip `RBS14041`, exact 10 mm fiberglass GT2 but ~€11/m. Technically excellent but unnecessary unless the cheap `RBS12747` has a checkout/continuous-length issue.

## StepperOnline Germany — GREEN

Exact `5-17HS19-2004S1` five-pack:
- 59 Ncm / 2 A
- 5 mm D-shaft / 24 mm shaft
- 1 m cable
- Germany warehouse available

Sweden freight checkout-only.

## DigiKey — GREEN after two corrections

Exact ordinary DigiKey-stock cart:
- Mean Well `HDR-60-24` ×1
- Omron `SS-3GL13PT` ×10
- exact 608-2RS ×16
- Wago `221-413` ×3
- Altech M20 5–12 mm ×2
- TE `3-350820-2` **DigiKey `A27824-ND`** ×10
- Amphenol `AIO-CSM12`, M12 / 3–6.5 mm / IP68 ×1

Faston duplicate trap:
- correct `A27824-ND` = ordinary DigiKey stock
- wrong route `5831-3-350820-2-ND` = Marketplace/MOQ 1000 risk

`AIO-CSM12` directly fits the nominal ~4.8 mm 24 V cable and removes the small-gland orphan.

Approx current merchandise sanity: ~641 SEK incl VAT after adding the M12 gland. DigiKey shipping threshold remains checkout-authoritative; buy no filler.

## Jackpot3 / Elecrow — GREEN

- `CQA240812C2`
- current $76.99 / in stock in latest audit
- needs LR4 FluidNC/config flashing
- package does not list microSD

Commissioning inventory:
- data USB-C
- simple FAT32 microSD >2 GB, preferably Class 4/6 if none already exists

## GT2 16T — GREEN

Allegro `GT2-16T-5B_10mm_K`:
- 16T
- 5 mm bore
- for 10 mm belt
- dual grub screws
- live ~7.20 PLN each in latest audit

Need 3.

## Sorotec — GREEN

`L1S.M.0317`:
- 3.175 mm dia/shank
- single flute
- 9 mm cutting length
- ~€3.70 each
- available in latest audit

Three are correct for commissioning + 5–6 mm struts.

## SUNLU — GREEN if checkout holds

Ordinary PLA. Need ~2.7 kg for LR4; 6×1 kg bulk order remains rational if Sweden-delivered cost stays near 100–110 SEK/kg.

## KEDU — GREEN family, checkout freight only

Preferred target: genuine **KEDU KJD12-14**:
- 230 V / 50 Hz option
- 2-pole NVR
- 15 A AC-3 / 18 A AC-1 family rating
- 6.3×0.8 Faston
- IP54
- red mushroom/yellow cover accessory

CEM direct/eBay is a concrete current source. Finished homemade circuit still described as NVR/machine stop, not claimed safety-rated e-stop system.

## 10 A circuit conclusion

No special pre-commissioning electrical investigation is justified by current evidence. The 10 A circuit already operates the user's welder; only the plasma cutter has been known to trip it. This materially lowers concern for the 800 W router + shop-vac combination.

At first combined run: simply observe whether the breaker holds. If it does, stop researching the issue. If it trips, investigate actual load/circuit then. Never up-fuse without verifying the fixed wiring.

## Current order status

**Ready by specification; checkout/fright remains:**
- LaskaKit without belt
- Roboter-Bausatz `RBS12747` 5 running metres, pending continuous-length + Sweden freight checkout
- StepperOnline Germany
- DigiKey with `A27824-ND` + `AIO-CSM12`
- VEVOR 0700C
- Elecrow Jackpot3
- SUNLU ordinary PLA
- Sorotec cutters
- Allegro 16T
- CEM/eBay KJD12-14

**Physical, not web, validation remains:**
- Motonet tubes
- used table
- VEVOR/Elaire collet/runout
- DeWalt nameplate
- full-travel cable/hose routing
