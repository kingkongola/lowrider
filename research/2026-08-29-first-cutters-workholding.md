---
research_date: 2026-08-29
last_updated_at: 2026-08-29
scope: first LR4 cutting tools and minimum useful workholding for commissioning and early wood/foam projects
status: recommendation-ready
confidence: high
machine_target: LowRider V4 ~650x1250, VEVOR 0700C, already-purchased 1/8 in / 3.175 mm Elaire collet
region: Sweden / EU
price_basis: current EU/Sorotec/V1E/JB CNC listings observed 2026-08-29; shipping must be checked at checkout where noted
sources_checked:
  - V1 Engineering current forum advice from Ryan/vicious1
  - V1 Engineering 1/8 single-flute product and extra-long references
  - Sorotec 1-flute 1/8 tools and Sweden shipping table
  - JB CNC Sweden upcut end-mill catalogue
  - EU long 3.175 mm single-flute references from DeluxCNC/Makera
  - V1E workholding/spoilboard discussions 2024-2026
supersedes: generic 'buy at least one 1/8 single flute' BOM line
---

# First cutters + minimal workholding

## Decision summary

Do **not** buy an assorted router-bit starter kit and do **not** build a T-track/insert-nut workholding system before the machine has made first cuts.

Commissioning baseline:
- **3 × short 3.175 mm single-flute upcut carbide cutters**
- ordinary screws directly into the MDF spoilboard for early workholding
- printed sacrificial clamps/cams only when a real job needs them
- buy one long 25–32 mm single-flute only when 18–19 mm plywood through-cuts become an actual job

This follows the current V1E Pareto advice: Ryan states that he uses single-flute upcut cutters about 99% of the time and recommends buying the specific tool needed rather than a variety pack.

Source:
- https://forum.v1e.com/t/lowrider-v4/53926/10

## 1. First cutter geometry

Preferred baseline:
- shank: **3.175 mm / 1/8 in**
- cutting diameter: ~3.0–3.175 mm
- **single flute**
- **upcut spiral**
- solid carbide
- short cutting edge, roughly 9–12 mm

Why short first:
- stiffer than a 25–32 mm cutter
- more forgiving while squaring/tramming/testing the machine
- ideal for XPS, plastics, thin MDF and the ~6 mm permanent strut plates
- less likely to snap from beginner setup mistakes

The already-purchased Elaire 1/8 collet is exactly the right interface for this class.

## 2. Recommended buy-now cutter: Sorotec Edition L1S.M.0317

Sorotec `L1S.M.0317`:
- diameter: **3.175 mm**
- shank: **3.175 mm**
- single flute
- upcut / spiral family
- cutting/spiral length: **9 mm**
- overall length: 38 mm
- solid carbide
- immediately available on current listing
- observed price: **€3.70 each**

Source:
- https://www.sorotec.de/shop/End-Mill-Single-Flute-Sorotec-Edition---3-175-mm.html?language=en

Sorotec describes this 'Edition' line as the same quality obtained by large direct-manufacturer quantities at a lower price.

### Buy quantity

Buy **3 pieces** initially:
- parts: 3 × €3.70 = **€11.10**

Current Sorotec Sweden shipping table:
- Sweden / SE, up to 0.5 kg: **€8.30**

Source:
- https://www.sorotec.de/shop/info/shipping---returns.html

Expected standalone delivered total:
- **~€19.40** before any destination VAT rounding

This is roughly the cost of one modest router-bit purchase locally and leaves two spares if the first cutter is broken during setup.

### Why not buy 10 immediately?

Current V1E/community advice supports having cheap spare single-flutes while learning, but there is no need to inventory 10 before confirming feeds, collet/runout and our actual project mix.

Three is enough to absorb beginner mistakes without turning tooling into another speculative stockpile.

## 3. Swedish local alternative — JB CNC

JB CNC in Gislaved sells 1-flute carbide upcut tooling with 3.175 mm shanks.

Current catalogue examples:
- 2 mm diameter / 17 mm cutting length / 3.175 mm shank: ~49.5 SEK and in stock
- 3.175 mm diameter version exists around ~90 SEK but current category view showed **sold out** during this check

Sources:
- https://www.jbcnc.se/en/cutting-tools-c-76/up-cut-end-mills-c-158/1-flute-carbide-upcut-endmill-2mm-l-p-1401
- https://www.jbcnc.se/en/cutting-tools-c-76/up-cut-end-mills-c-158/

JB CNC ships from Sweden but calculates freight only in checkout.

Use JB CNC opportunistically if:
- the exact 3.175 mm cutter returns to stock, and
- another Swedish CNC item naturally shares the shipment.

Do not create a separate local shipment just because the shop is Swedish if Sorotec delivered is cheaper.

## 4. Long cutter for 18–19 mm plywood — intentionally deferred

A short 9 mm flute cannot through-cut 18 mm plywood even with multiple Z passes because the unfluted shank would eventually rub the slot.

For full-depth sheet work, later buy:
- 3.175 mm shank
- 3–3.175 mm cutting diameter
- single flute upcut/O-flute
- **at least ~22–25 mm actual cutting length**

V1E's own extra-long reference is:
- 1/8 in shank/diameter
- 55 mm overall
- **32 mm depth of cut**
- specifically proven by users on 3/4 in plywood

Sources:
- https://forum.v1e.com/t/which-endmill-for-100x-20mm-holes-in-1-thick-stock/53132
- https://forum.v1e.com/t/what-to-buy/52175

EU candidates exist without US shipping:
- DeluxCNC single-flute 3.175 mm with **25 mm cutting length**, €9.90, current stock observed
- Makera O-flute variants with 3.175 mm shank and 25/32 mm length options around €8–12 depending seller/variant

Sources:
- https://deluxcnc.eu/en/premium/634-single-flute-carbide-end-mill-short-3175mm-lc17mm.html
- https://www.mybotshop.de/Makera-Spiral-O-Single-Flute-Bit-1-8-Shank_3
- https://www.reichelt.com/de/en/cnc-spiral-o-single-flute-bit-1-8-shank-3-175-x-32-mm-makera-10169-p385169.html

### Decision

**Do not order the long cutter now.**

First machine jobs can be:
- foam
- surfacing/test cuts
- thin MDF/hardboard
- permanent ~6 mm struts
- shallow pockets/engraving

When the first 18–19 mm plywood profile job is actually queued, pick the best current 25–32 mm EU cutter and buy 1–2.

This avoids learning on the least rigid cutter we own.

## 5. Do not buy a variety pack

V1E's variety pack contains useful specialist geometries (ball nose, V-bit, downcut etc.), but Ryan's current advice is simply to buy the tools needed for actual jobs; single-flute upcut handles the overwhelming majority of his normal work.

Source:
- https://forum.v1e.com/t/lowrider-v4/53926/10

Therefore no:
- V-bit before a sign/carving job needs it
- ball nose before 3D relief work
- compression/downcut before surface-finish requirements justify it
- large 1/4 in tooling before the machine is commissioned

## 6. Minimum workholding — spend zero first

Current V1E community advice is very simple: **plain MDF spoilboard works and screwing directly into it works.** T-track, insert grids and vacuum beds are optional upgrades, not commissioning requirements.

Sources:
- https://forum.v1e.com/t/spoil-board-hold-down-options/44404
- https://forum.v1e.com/t/best-way-to-spend-150-bucks-upgrading-the-bed-what-clamps-do-i-pick/53714
- https://forum.v1e.com/t/spoilboard-holding-replacing/54046

### First-job workholding hierarchy

1. **screw workpiece/sacrificial tabs directly into MDF spoilboard** where screw positions are safely outside toolpaths
2. for stock where visible screw holes are unacceptable, use sacrificial edge strips/tabs around the stock and screw those down
3. print simple low-profile cam/edge clamps when a repeat job appears
4. only build dogs/insert grid/T-track after actual usage shows what spacing/system would help

### Safety rule

CAM/toolpath must know where every screw/clamp is.

A carbide cutter hitting a screw is not an acceptable 'sacrificial' event.

Keep hold-down hardware:
- outside profile paths, or
- below known safe Z depth, with explicit clearance

## 7. What not to buy yet

- T-track
- threaded-insert grid
- aluminium clamp kit
- vacuum table
- dedicated toe-clamps
- large endmill assortment
- 1/4 in tooling assortment
- surfacing bit before spoilboard surfacing becomes necessary

All can be added later with essentially zero lock-in.

## Initial spend

Recommended immediate tooling spend:
- 3 × Sorotec `L1S.M.0317`: €11.10
- Sweden postage: €8.30
- total: **~€19.40**

Workholding immediate spend:
- **0 SEK** if ordinary suitable wood screws are already in workshop stock
- otherwise buy only a small box of ordinary screws suitable for the chosen spoilboard thickness

## Purchase status

**Short cutters: purchase-ready.**

**Long plywood cutter: intentionally deferred.**

**Workholding system: intentionally no purchase before first cuts.**

This minimizes both cost and premature fixture-system decisions while still giving three proper cutters to commission the machine with.
