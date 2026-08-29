---
research_date: 2026-08-29
scope: mandatory LR4 procurement gap audit after component-by-component research
status: recommendation-ready
decision_state: separate purchase-ready rows from dimension-gated and still-unresearched rows; next priority is freeze 650x1250 geometry because it unlocks tubes, belt and table
price_basis: observed prices from dated research files; all prices/stock must be re-checked at checkout
region: Sweden / EU
sources_checked:
  - BOM.md
  - CHECKLIST.md
  - PROCUREMENT.md
  - dated files under research/
  - V1 Engineering LR4 docs/calculator
supersedes: null
---

# Procurement gap audit

Purpose: stop re-researching already solved rows and expose exactly what still blocks ordering/building.

## A. Already purchased / paid

- HaWiWe aluminium XZ plates, 6 mm
- 4 × MGN12H 150 mm linear rails
- LR4 screw set
- Elaire/Makita-style MRP-1250 1/8 in / 3.175 mm collet

Status: **done; physical inventory when parcel arrives**.

## B. Specification and preferred product essentially locked

### Motors
- 5-pack StepperOnline `5-17HS19-2004S1`
- 59 Ncm / 83.55 oz-in, 2 A, 1.8°, 48 mm body, 24 mm shaft
- Germany warehouse candidate

State: **purchase-ready after final delivered-price/warehouse checkout check**.

### Router
- exact VEVOR `0700C`
- SKU `YXKXBJ710W65AH7WLV2`
- product ID `010235793217`
- 800 W, 65 mm, 10,000–30,000 rpm, 220–240 V

State: **purchase-ready after Sweden checkout/coupon check**. Do not substitute 710 W model.

### Controller
- Jackpot3
- Elecrow is the leading international purchase route unless final V1E delivered cost unexpectedly wins

State: **product locked; final shipping/tax checkout still needed**.

### Endstops
- 5 × Omron `SS-3GL13PT` baseline V1E-style switch
- earlier `SS-5GL2` baseline assumption is superseded; it is an optional geometry mod, not default

State: **specification locked; supplier/cart open**.

### Z drive / GT2 commodity cluster
Leading LaskaKit cart:
- 6 × correct smooth idlers for 10 mm GT2 / 5 mm bore
- 5 m fiberglass 10 mm GT2 belt
- 1 × 400 mm Tr8x8 4-start rod, cut into two Z screws
- 2 × matching T8x8 brass nuts
- 2 × flexible 5→8 mm couplers

State: **strong recommendation, but hold until machine size is formally frozen and final stock/shipping is rechecked**.

### PLA
Current price leader:
- SUNLU regular PLA 5 kg large spool around €39.99 when Europe/Sweden shipping terms hold
- approximate raw price ~89 SEK/kg at 2026-08-29 reference FX

Alternative when colour flexibility matters:
- Creality Soleyin Ultra bulk around ~109 SEK/kg when bulk packs are actually in stock

State: **product family recommendation-ready; colour/format and Sweden checkout still open**.

## C. Exact specification known, supplier/cart still open

### 16T drive pulleys
Need 3 ×:
- GT2 / 2 mm pitch
- 16T
- 5 mm bore
- for 10 mm belt

Verified candidates exist at Hellas Digital, Anodas and Allegro. Item cost is tiny; shipping dominates.

State: **orphan-cart problem**.

### 608-2RS bearings
Need 14; preferred purchase quantity 20 for spares.
- 8×22×7 mm
- rubber seals both sides
- commodity quality is sufficient
- target delivered total <= ~180 SEK

State: **supplier/cart open**.

### PSU
Two valid architectures remain:
1. external Mean Well `GST60A24-P1J` 24 V / 2.5 A / 60 W — cleaner mains architecture
2. Mean Well `LRS-100-24` — cheaper raw PSU but needs safe enclosure for exposed mains terminals

Rule: prefer the external brick if its complete delivered premium over the safely enclosed LRS solution is only ~100–150 SEK.

State: **supplier/cart + complete-system price still open**.

### Main stop / NVR
Leading Pareto architecture:
- genuine KEDU `KJD12`, 230 V, NVR/no-restart, emergency-stop cover

State: **architecture selected; Sweden-delivered seller and final enclosure/output arrangement still open**.

## D. Dimension-gated — do not order until 650×1250 is formally frozen

### Steel rails/tubes
V1E accepted rail OD:
- 29.5, 30 or 32 mm ±0.2 mm
- steel/stainless/DOM
- wall >=1.3 mm

Current likely Swedish choice: precision steel tube around 32×2 mm if locally inexpensive.

Final cut lengths must come from current LR4 calculator after work area freeze.

### Belt
Existing research calculates ~4.409 m total for 650×1250, making a 5 m roll sufficient. This becomes orderable only when that work area is formally frozen.

### Table
Current concept:
- reuse a stable used dining/conference-table base if economical
- own rigid CNC top/cassette
- removable/replaceable centre/spoilboard architecture
- wheels only for movement; machine rests on stable feet when cutting

Final dimensions follow the calculator plus practical edge protection.

## E. Mandatory but insufficiently optimized/researched

These still deserve their own small research blocks:

1. **steel tube supplier + actual cut lengths + delivered/local pickup cost**
2. **dust system**: shop-vac, cyclone, hose diameter/length, dust shoe interface, hose support, static mitigation
3. **first tooling**: exact 1/8 in single-flute cutter(s), preferably sensible starter set without junk bundle
4. **strut-plate material**: cheap/stable <=6.35 mm material and how to make the first permanent set
5. **table material/base sourcing** after dimensions are frozen
6. **workholding**: minimum useful clamps / screw strategy for first jobs
7. **small electrical/mechanical consumables**: endstop wire, connectors, cable sleeve/ties, threadlocker, M4 table screws; buy only after cart consolidation

## F. Cable-extender correction

BOM currently lists 3 stepper extension cables as unconditional. Research indicates the selected StepperOnline motors already include 1 m leads and our machine is much smaller than a full-sheet LR4.

Therefore treat motor extensions as **conditional**, not automatically mandatory:
- assemble/dry-route with final controller position
- verify full X/Y/Z travel with strain relief
- buy extensions only where necessary

Endstop wiring remains required separately.

## Priority order from here

1. **Freeze 650×1250 geometry using the current calculator and the purchased 6 mm XZ plates.**
2. Once frozen, convert LaskaKit cart from recommendation to buy-ready and derive exact steel tube lengths/table footprint.
3. Resolve the orphan 16T pulleys + 608 bearings by cart consolidation.
4. Resolve PSU + KJD12/NVR as a complete safe mains system, not isolated components.
5. Research dust collection as a separate mandatory subsystem.
6. Only then produce final cart scenarios: cheapest correct / Pareto / fewest parcels.
