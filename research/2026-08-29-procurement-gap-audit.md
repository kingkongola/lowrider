---
research_date: 2026-08-29
last_updated_at: 2026-08-29
scope: current mandatory LR4 procurement gap audit after component-by-component research
status: recommendation-ready
decision_state: most major components are now locked; remaining work is checkout verification plus a small set of orphan/safety/table items
price_basis: dated research files under research/; all observed prices/stock must be rechecked at checkout
region: Sweden / EU
sources_checked:
  - BOM.md
  - TABLE.md
  - PROCUREMENT.md
  - current dated files under research/
  - V1 Engineering LR4 docs/calculator
supersedes: earlier version of this gap audit that still treated geometry, PSU, tubes and dust architecture as unresolved
---

# Procurement gap audit — current state

Purpose: show only what is actually still unresolved and stop re-researching decisions that are already good enough.

## A. Done / already owned

### Paid HaWiWe order
- 6 mm aluminium XZ plates
- 4 × MGN12H 150 mm rails
- LR4 screw/nut set
- Elaire/Makita-style `MRP-1250` 1/8 in collet
- paid total: **€165.50 incl €8 shipping**

### Existing useful equipment
- DeWalt wet/dry vacuum, very likely `DXV30SAPTA`
- old FTX ventilation unit for possible secondary enclosure/ambient-air duty
- TPU filament for stock LR4 dust-shoe bristles if durometer is suitable (~95A)

## B. Product/specification locked — checkout only

### Jackpot3 controller
- **Jackpot3** remains selected
- preferred source: Elecrow
- exact SKU: `CQA240812C2`
- observed: **$76.99**, in stock, 300 g
- requires flashing when bought from Elecrow
- no verified current EU reseller found

Still needed:
- Elecrow Sweden shipping
- VAT/import/IOSS treatment in checkout
- resulting all-in landed total

File: `research/2026-08-29-jackpot3-order.md`

### Router
- exact **VEVOR 0700C**
- SKU `YXKXBJ710W65AH7WLV2`
- product ID `010235793217`
- 800 W / 65 mm / 10,000–30,000 rpm / 220–240 V
- observed official VEVOR EU price **€83.99**
- current VEVOR EU policy implies free Sweden shipping

State: **purchase-ready; only final Sweden checkout/coupon verification remains**.

File: `research/2026-08-29-vevor-0700c-router.md`

### Motors
- StepperOnline 5-pack `5-17HS19-2004S1`
- 59 Ncm / 83.55 oz-in
- 2 A
- 48 mm body
- 24 mm 5 mm D-shaft
- 1 m lead / 2.54 mm connector
- observed €38.13 / 5-pack
- Germany warehouse selectable

Still needed:
- exact Germany→Sweden checkout freight

File: `research/2026-08-29-stepperonline-motor-order-live.md`

### PSU + endstops
- Mean Well **`HDR-60-24`**, 24 V / 2.5 A / 60 W
- exact Omron **`SS-3GL13PT`**
- buy 10 switches, install 5, keep 5 spares
- current DigiKey planned delivered cart ~495 SEK class

State: **recommendation-ready**.

File: `research/2026-08-29-final-psu-endstop-wiring-cart.md`

## C. Mechanical cart locked

### Geometry
Locked/current target:
- usable area ~650×1250 mm
- tubes: 816 / 816 / 1505 mm
- X belt 999 mm
- Y belts 1705 / 1705 mm
- total GT2 need 4409 mm
- strut ~819 mm
- minimum table ~941×1563 mm; practical cassette around ~1000×1620 mm

File: `research/2026-08-29-geometry-650x1250.md`

### LaskaKit cart
Recommended cluster:
- 6 × smooth 10 mm GT2 idlers
- 1 × 400 mm T8×8 rod
- 2 × T8×8 brass nuts
- 2 × 5→8 mm couplers
- 5 m 10 mm fiberglass GT2 belt if stock confirms; otherwise 3×2 m
- 10 m endstop signal cable
- ~1 m 20 AWG 2-core 24 V cable
- board-side pigtails/connectors as needed

Base mechanical cart:
- ~€42.45 delivered with 5 m belt before added low-cost cable
- ~€49.34 with 3×2 m belt fallback before added cable

State: **checkout-ready**.

File: `research/2026-08-29-laskakit-final-mechanical-cart.md`

### Steel rails — newly solved
New first choice:
- Motonet `88-7123`
- round steel tube **Ø30×1.5 mm ×2 m**
- 2 pcs
- observed **189 SEK each = 378 SEK total**
- V1E nominal OD/wall requirements are met

Cut plan:
- stick A → 1505 mm
- stick B → 816 + 816 mm

Only physical acceptance remains:
- actual OD ~29.8–30.2 mm
- straight / undented

State: **local purchase-ready if physical stock passes inspection**.

File: `research/2026-08-29-steel-tubes-gavle.md`

## D. Dust system is largely solved, not a major shopping gap

Architecture:
- print LR4 dust shoe
- print TPU bristles using already-owned TPU if suitable
- reuse existing DeWalt 48 mm ×2.1 m hose first
- print cyclone first
- use separate rigid 15–30 L metal collection container
- cyclone → DeWalt shop-vac
- simple hose support/strain relief
- evaluate FTX only for secondary enclosure/ambient-air use

Still open:
- exact metal collection bucket/container
- final printed cyclone STL/geometry and adapters after hose dimensions are physically measured
- static grounding details
- simple wipeable curtain/enclosure material

No new vacuum purchase is needed.

## E. Remaining true procurement gaps

### 1. 3 × GT2 16T drive pulleys
Exact requirement:
- 16T
- 2 mm pitch
- 5 mm bore
- for 10 mm belt

Verified candidates:
- Allegro exact two-set-screw part
- AliExpress/Choice possible 5-pack if exact variant can be validated
- Hellas/Anodas EU fallbacks

State: **cheap orphan item; seller/checkout still open**.

### 2. 20-pack 608-2RS bearings
Need 14 installed; buy 20.
- 8×22×7 mm
- rubber-sealed 2RS
- commodity quality is sufficient

Amazon Prime remains opportunistic but no current Amazon.se variant has been verified end-to-end.

State: **seller open**.

### 3. Machine mains NVR / emergency stop
Principles are locked:
- no-volt release / no automatic restart
- router and controller power should stop together
- do not treat a flimsy marketplace mushroom as the sole safety device

Leading low-cost hardware families:
- KEDU/KJD NVR solution
- complete NVR + mushroom station if a credible EU source wins

State: **final product/seller still open**.

### 4. First cutters
Strategy locked:
- 3.175 mm single-flute upcut as the default
- buy a few cheap learning cutters rather than a huge mixed starter set
- long cutter only when 18–19 mm plywood through-cuts are actually needed

State: **exact low-cost seller/cart still open**.

### 5. PLA final checkout
Current price leader:
- SUNLU ordinary PLA large 5 kg spool around €39.99 when EU/Sweden terms hold

Alternative:
- Creality Soleyin Ultra bulk when stocked

State: **final colour/spool-format/Sweden checkout open**.

### 6. Table/underframe
Architecture is locked but the used physical base is intentionally opportunistic:
- stable used dining/conference-table base first
- LR4-specific ~1000×1620 top/cassette
- reuse existing top as structural deck if suitable
- otherwise cheap OSB or plywood structural deck
- removable ~12 mm MDF spoilboard

State: **find actual used base; do not buy new structural sheet prematurely**.

## F. Conditional / deliberately deferred

### Stepper extensions
Do not buy yet.

Selected motors have 1 m leads. Dry-fit first and extend only runs that lack a relaxed service loop at full travel.

### Laser
2027 project. Jackpot3 preserves PWM capability but no laser hardware is part of current build.

### Plasma
No current hardware. Table architecture merely avoids blocking a future removable plasma centre cassette.

## Current priority from here

1. Close **16T pulleys + 608 bearings**.
2. Close **NVR / emergency-stop station**.
3. Close **PLA + first cutters**.
4. Check out the already-resolved big carts: VEVOR, Jackpot3, motors, DigiKey, LaskaKit.
5. Pick up Motonet tubes if physical stock passes OD/straightness check.
6. Find the used table base.
7. Produce final order scenarios: cheapest correct / recommended Pareto / fewest parcels.

At this point, broad alternative-component research has sharply diminishing returns. Most remaining work is checkout validation and small orphan-item consolidation rather than architecture selection.
