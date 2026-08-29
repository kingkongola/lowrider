---
research_date: 2026-08-29
scope: first cutting tools for LR4 with already-purchased 1/8-inch Elaire collet
status: recommendation-ready
decision_state: do not buy a variety pack; start with 3.175 mm-shank single-flute upcut cutters, cheap spares for learning plus one quality/stiff short cutter; add extra-long single-flute only when 18–25 mm sheet profiling is needed
price_basis: observed web prices 2026-08-29; exact Amazon Sweden purchase listing still needs checkout verification
region: Sweden / EU
sources_checked:
  - V1 Engineering current endmill products
  - V1 Engineering forum 2025–2026 LR4 advice
  - Sorotec Germany
  - LaskaKit Czech Republic
  - indexed Amazon/HQMaster/Genmitsu references
supersedes: generic BOM line saying only 'at least one 1/8 single-flute endmill'
---

# First endmills for this LR4

## 1. Tool family is effectively decided

Ryan/V1E's current 2026 advice is unusually clear:
- do **not** buy a variety pack merely because you are starting
- buy the tools needed for the jobs
- he uses **single-flute upcut bits ~99% of the time**
- V-bits/ball nose are added only for carving/3D work

V1E's standard 1/8 single-flute page describes it as the one general-purpose endmill to buy if choosing only one.

Sources:
- https://forum.v1e.com/t/lowrider-v4/53926/10
- https://www.v1e.com/products/1-8-single-flute

This aligns perfectly with the already-paid Elaire 1/8-inch / 3.175 mm collet.

## 2. First tool: short/stiff 3 mm-class single flute

For:
- first foam cuts
- calibration
- thin plywood/MDF
- permanent strut plates up to 6.35 mm
- plastics
- later cautious aluminium work

use a **short single-flute upcut carbide cutter** rather than an extra-long bit.

Why:
- less stickout = less deflection
- much harder to snap from beginner mistakes
- suitable for the thin strut plates
- V1E users successfully cut aluminium with standard 1/8 single-flute cutters

### Good EU quality reference: Sorotec `L1S.0317`

Verified current specification:
- solid carbide
- single flute
- upcut
- cutting diameter **3.175 mm**
- shank **3.175 mm**
- spiral/flute length 9 mm
- overall length 38 mm
- suitable for wood, plastics, Styrodur/XPS and soft aluminium
- observed price **€5.50 incl German VAT**, before Sweden shipping

Source:
- https://www.sorotec.de/shop/End-Mill-Single-Flute--3-175mm.html

This is a useful quality benchmark, but not necessarily worth a separate international shipment for one cutter.

## 3. Cheap sacrificial learning cutters are rational

A current 2026 LR4 thread explicitly recommends buying very cheap 1/8 single-flute upcut mills — roughly a ten-pack — so beginner mistakes do not destroy expensive cutters.

Source:
- https://forum.v1e.com/t/lowrider-v4/53926

This is appropriate because early CNC mistakes can include:
- wrong Z zero
- cutting spoilboard/screws
- bad feeds/speeds
- forgotten clamps
- bad toolpath

### Search target for Amazon/marketplace

Exact target for a cheap pack:
- 1/8 inch / **3.175 mm shank**
- cutting diameter around 3.0–3.175 mm
- **single flute / O-flute / spiral upcut**
- carbide
- preferably 10–17 mm cutting length for the learning pack

Known product families with these specs include HQMaster and Genmitsu, but a Sweden-specific Prime listing/price was not reliably indexed enough today to lock an ASIN.

Do not buy a 'CNC bit set' unless the selected variant is genuinely single-flute upcut.

## 4. LaskaKit cutter-set trap

LaskaKit carries `LA190009B`, a ten-piece 1.5–3.175 mm carbide 'milling drill' set for about €15.2.

It has:
- 3.175 mm shanks
- assorted cutting diameters
- 37 mm overall length

But the listing does **not** establish that these are the 3 mm-class single-flute spiral upcut cutters recommended by V1E. It is an assorted milling-drill set, not our target tool geometry.

Source:
- https://www.laskakit.cz/en/sada-10-frezovacich-vrtaku-1-5-3-175mm/

**Do not add it to the LaskaKit mechanical cart merely to consolidate shipping.**

## 5. Long cutter for 18–25 mm plywood is a different tool

A standard short 9–15 mm flute cutter cannot profile all the way through 18–19 mm plywood.

V1E's current extra-long reference:
- 1/8 inch diameter
- 1/8 inch / 3.175 mm shank
- **55 mm overall length**
- **32 mm depth of cut / cutting length**
- $3.49 reference price
- explicitly intended for wood/plastics; V1E advises staying away from aluminium with the extra-long version

A 2026 user reports using it successfully for 3/4-inch maple plywood.

Sources:
- https://www.v1e.com/collections/all
- https://forum.v1e.com/t/which-endmill-for-100x-20mm-holes-in-1-thick-stock/53132

### Important principle

Do not use the 32 mm long cutter as the everyday tool merely because it reaches everything.

Longer stickout increases leverage/deflection. Current LR4 troubleshooting reports also show long bits becoming much less forgiving when feeds/DOC are aggressive.

Use:
- **short cutter whenever the job allows**
- long cutter only for thick sheet profile work

## 6. Aluminium

The ordinary short 1/8 single-flute is the correct family to start with later.

Recent LR4/V1E examples use it successfully on aluminium. A May 2026 LR4 example used:
- V1E 1/8 single flute
- 200 mm/min feed
- 150 mm/min plunge
- ~20k rpm
- 0.5 mm DOC
- ramp/ease-down

These are an existence proof, not universal settings for our machine.

Source:
- https://forum.v1e.com/t/lr3-lr4-conversion-going-forward-slowly/54004

Do not use the extra-long 32 mm wood/plastic cutter for aluminium.

## 7. Recommended starter inventory

Before first cuts, target:
- **3–10 cheap short 3.175 mm-shank single-flute upcut cutters** for learning/general work
- optionally **1 higher-quality short single-flute** as a known-good reference cutter
- **1 extra-long 22–32 mm cutting-length single-flute** only before first 18–19 mm plywood profile job

Not needed now:
- 1/4-inch tooling
- ball nose
- V-bit
- compression bit
- surfacing bit
- large variety pack

Those can be bought when a real project demands them.

## Procurement status

**Tool type is locked; supplier is not.**

Best procurement path:
1. watch Amazon.se/Prime for a genuine cheap HQMaster/Genmitsu-style 3.175 mm single-flute upcut multipack
2. if no sensible Prime deal appears, combine quality cutters with another Germany/EU order rather than paying a separate shipment for a €5 cutter
3. do not let cutter sourcing delay machine assembly — any verified 3.175 mm carbide single-flute upcut in the right length can make the first cuts
