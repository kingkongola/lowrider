---
research_date: 2026-08-29
last_updated_at: 2026-08-30
scope: separate rigid collection container for the 3D-printed cyclone upstream of the existing DeWalt shop-vac
status: recommendation-ready-with-physical-gate
decision_state: use a cheap rigid steel ash bucket/can with lid as first candidate, but do not assume steel alone makes it vacuum-safe; gasket + printed cyclone flange + controlled vacuum/deformation test required before use
price_basis: observed web prices 2026-08-29; local pickup preferred
region: Sweden
sources_checked:
  - Jula
  - Hornbach Sweden
  - Swedish packaging/drum suppliers
  - DeWalt DXV30SAPTA nominal sealed-pressure specification from project research
supersedes: generic '20–40 L rigid container' wording in earlier cyclone notes and the earlier over-strong assumption that a steel ash can largely removes collapse risk
---

# Cyclone collection container

## Clarification

The user's existing DeWalt has a metal tank. That stays downstream as the vacuum.

The cyclone needs a **second, separate collection can** before the DeWalt so chips drop out before air reaches the vacuum:

`cyclone -> collection can -> DeWalt`

## What the container actually needs

- roughly 15–30 L is enough for this compact LR4
- rigid enough to tolerate the **actual shop-vac vacuum**, including a partial blockage
- removable lid
- lid can be made airtight with foam/rubber gasket
- enough flat area in lid to bolt the printed cyclone/flange
- metal preferred for stiffness and easier static bonding

It does **not** need:
- food approval
- UN certification
- stainless steel
- wheels
- commercial dust-collector branding

## Critical audit correction — steel does not automatically mean vacuum-safe

The likely DeWalt model has a published sealed-pressure figure around **15 kPa**. Pressure acts over the whole projected lid area.

For a roughly 34 cm diameter lid:
- area ≈ 0.091 m²
- 15,000 Pa × 0.091 m² ≈ **1,360 N**
- equivalent total force ≈ **139 kgf**

That does **not** mean 139 kg sits at one point; it is distributed pressure. But it explains why even a metal pail with a relatively flat/thin lid can dish, buckle or suddenly deform if the inlet is blocked.

Therefore the earlier reasoning “steel can largely removes implosion concern” was too strong.

### Acceptance gate

A candidate collection can is not approved merely because it is steel.

After the cyclone/lid is assembled airtight:
1. run the vacuum with normal open flow and inspect lid/walls
2. progressively restrict the cyclone inlet briefly while standing clear of the lid
3. stop immediately if lid/walls visibly dish, oil-can, crease or make structural noises
4. do not perform a prolonged fully blocked test just to prove a point
5. if the container deforms, reinforce/use a stiffer drum or add an appropriate vacuum-relief path before CNC use

A small leak is not an acceptable 'safety valve' because it also hurts separation performance and is uncontrolled.

## Best cheap retail lead: steel ash bucket

### Jula Anslut ash bucket

Current listing:
- 20 L
- powder-coated steel
- 34 cm diameter
- 38 cm high
- 2.06 kg
- **199 SEK**

Source:
- https://www.jula.se/catalog/bygg-och-farg/varme-och-ventilation/kaminer-och-oppna-spisar/spisredskap/askhink-391055/

Jula also has sheet-metal ash-bucket lids in this product family, but current indexed lid compatibility is not clean enough to assume a specific lid SKU fits `391055`. Verify physically/in-store before buying the pair.

The bucket remains a good **candidate**, not a pre-approved pressure vessel.

### Hornbach ash-bucket alternatives

Current Swedish Hornbach search shows:
- 15 L oval galvanized metal ash bucket with lid around **159 SEK**
- 10 L black metal ash bucket with lid around 399 SEK

Source:
- https://www.hornbach.se/c/varme-ventilation/kaminer-eldstader/kamintillbehor/eldstall-askhinkar/S17306/

The cheap 15 L galvanized option is interesting if its lid has enough usable flat area for the cyclone flange **and passes the physical vacuum/deformation test**.

## Why a normal ash bucket may still be enough

The cyclone lid will be modified anyway:
- drill/cut one opening
- bolt printed cyclone/flange through lid
- add closed-cell foam or rubber gasket around lid rim
- optionally add simple toggle/latch clamps if the original lid is loose

A suitably ribbed/stiff metal bucket can therefore still be the cheapest solution. The audit correction is only that its structural adequacy must be demonstrated rather than inferred from material alone.

## Special steel drum benchmark

Commercial 20–30 L steel packaging drums exist and are structurally better candidates, e.g. UN-rated paint/chemical drums. But Swedish suppliers tend to sell them as industrial packaging, often with minimum quantities or quote-based pricing.

Example:
- Tara Pac 20 L metal pail, 1.2 kg, metal construction, but industrial MOQ 528 pcs
- specialist 30 L steel drums exist but are not obviously rational single-unit retail purchases

Sources:
- https://www.tarapac.com/forpackningar/platemballage/produkt/plathink-20-l-pail-o-285/
- https://lekatrading.com/sv/produkt/fat/30-liters-stalfat-bundlat-blatt-sv002/

So the industrial-drum route is overkill unless a used/free stiff drum appears locally or the cheap ash bucket fails the vacuum test.

## Airtightness strategy

Do not require the purchased bucket itself to be perfectly airtight.

Make the assembly airtight ourselves:
1. self-adhesive closed-cell foam/weatherstrip around lid rim
2. printed wide mounting flange under/over cyclone base
3. M4/M5 bolts + washers through lid
4. silicone/PU sealant only where needed
5. if lid lifts under normal vacuum, add 2–3 cheap toggle clamps

Important: clamps solve lid sealing/lift, **not** inadequate panel stiffness against external pressure.

## Static strategy

With a steel can:
- electrically bond can to the grounding conductor/hose spiral strategy
- scrape paint under the bond washer if necessary so the connection reaches bare metal
- do not rely on the printed PLA cyclone itself for conductivity
- continuity-test the bond after final assembly

## Current purchase rule

**Do not buy a special cyclone container online yet.**

First check:
1. garage/home for an existing metal bucket/can with removable lid
2. local Jula/Hornbach for a 15–20 L steel ash bucket around **159–199 SEK**
3. inspect lid/wall stiffness before modifying it
4. build/gasket the assembly
5. perform controlled vacuum/deformation test
6. only spend more if the cheap container deforms or is impossible to seal safely

Target candidate cost: **0–200 SEK**, plus a few SEK of gasket/sealant/bolts.

The important optimization is no longer “cheapest steel bucket wins”; it is **cheapest container that remains structurally stable at the real vacuum and seals well enough for separation**.
