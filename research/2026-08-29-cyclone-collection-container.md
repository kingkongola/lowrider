---
research_date: 2026-08-29
scope: separate rigid collection container for the 3D-printed cyclone upstream of the existing DeWalt shop-vac
status: recommendation-ready
decision_state: use a cheap rigid steel ash bucket/can with lid and add our own gasket + printed cyclone flange; avoid special dust drums unless a free/cheap used drum appears
price_basis: observed web prices 2026-08-29; local pickup preferred
region: Sweden
sources_checked:
  - Jula
  - Hornbach Sweden
  - Swedish packaging/drum suppliers
supersedes: generic '20–40 L rigid container' wording in earlier cyclone notes
---

# Cyclone collection container

## Clarification

The user's existing DeWalt has a metal tank. That stays downstream as the vacuum.

The cyclone needs a **second, separate collection can** before the DeWalt so chips drop out before air reaches the vacuum:

`cyclone -> collection can -> DeWalt`

## What the container actually needs

- roughly 15–30 L is enough for this compact LR4
- rigid enough to tolerate shop-vac vacuum
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

### Hornbach ash-bucket alternatives

Current Swedish Hornbach search shows:
- 15 L oval galvanized metal ash bucket with lid around **159 SEK**
- 10 L black metal ash bucket with lid around 399 SEK

Source:
- https://www.hornbach.se/c/varme-ventilation/kaminer-eldstader/kamintillbehor/eldstall-askhinkar/S17306/

The cheap 15 L galvanized option is especially interesting if its lid has enough usable flat area for the cyclone flange.

## Why a normal ash bucket is enough

The cyclone lid will be modified anyway:
- drill/cut one opening
- bolt printed cyclone/flange through lid
- add closed-cell foam or rubber gasket around lid rim
- optionally add simple toggle/latch clamps if the original lid is loose

Therefore paying hundreds extra for a purpose-built airtight dust drum is unnecessary unless the cheap bucket proves too flexible or awkward to seal.

## Special steel drum benchmark

Commercial 20–30 L steel packaging drums exist and are structurally ideal, e.g. UN-rated paint/chemical drums. But Swedish suppliers tend to sell them as industrial packaging, often with minimum quantities or quote-based pricing.

Example:
- Tara Pac 20 L metal pail, 1.2 kg, metal construction, but industrial MOQ 528 pcs
- specialist 30 L steel drums exist but are not obviously rational single-unit retail purchases

Sources:
- https://www.tarapac.com/forpackningar/platemballage/produkt/plathink-20-l-pail-o-285/
- https://lekatrading.com/sv/produkt/fat/30-liters-stalfat-bundlat-blatt-sv002/

So the industrial-drum route is overkill unless a used/free drum appears locally.

## Airtightness strategy

Do not require the purchased bucket itself to be perfectly airtight.

Make it airtight ourselves:
1. self-adhesive closed-cell foam/weatherstrip around lid rim
2. printed wide mounting flange under/over cyclone base
3. M4/M5 bolts + washers through lid
4. silicone/PU sealant only where needed
5. if lid lifts under vacuum, add 2–3 cheap toggle clamps

This is simpler than searching for a rare perfect drum.

## Static strategy

With a steel can:
- electrically bond can to the grounding conductor/hose spiral strategy
- scrape paint under the bond washer if necessary so the connection reaches bare metal
- do not rely on the printed PLA cyclone itself for conductivity

## Current purchase rule

**Do not buy a special cyclone container online.**

First check:
1. garage/home for an existing metal bucket/can with removable lid
2. local Jula/Hornbach for a 15–20 L steel ash bucket around **159–199 SEK**
3. only spend more if those are physically too flimsy or impossible to gasket

Target container cost: **0–200 SEK**, plus a few SEK of gasket/sealant/bolts.

That keeps the complete printed separator plausibly around only a few hundred SEK including hose interfaces, rather than 1,299 SEK for DeWalt's ready-made separator.
