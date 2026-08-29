---
research_date: 2026-08-29
scope: cyclone/pre-separator for existing DeWalt shop-vac and LR4 dust system
status: recommendation-ready
decision_state: do not buy DeWalt DXVCS003 by default; leading value candidate is Dust Commander DLX ESD MKII if Sweden shipping is reasonable; CLC is cheaper fallback; exact container and adapters remain open
price_basis: observed web prices on 2026-08-29; re-check Sweden shipping and stock at checkout
region: Sweden / EU
sources_checked:
  - Jula DeWalt DXVCS003
  - Dust Commander CLC
  - Dust Commander DLX ESD MKII
  - Dust Commander HD
  - current likely DeWalt DXV38SPTA specifications
supersedes: null
---

# Cyclone separator research

## Existing vacuum context

User already owns a DeWalt Jula wet/dry vacuum, very likely `DXV38SPTA`:
- 48 mm × 2.1 m hose
- 42.5 L/s airflow
- 17 kPa seal pressure
- 38 L tank

This is not yet label-confirmed, so model-specific adapter purchases wait for physical confirmation.

## Option A — DeWalt DXVCS003 from Jula: easiest, not cheapest

Jula current listing:
- model `DXVCS003`
- **1,299 SEK**
- complete cyclone + 38 L stainless steel tank + wheels
- includes hose
- 48 mm connections
- claimed up to **99.5 %** particle/dust separation
- intended for most wet/dry vacs

Source:
- https://www.jula.se/catalog/hem-och-hushall/stad-och-kladvard/dammsugare/grovdammsugartillbehor/dammavskiljare-027616/

### Assessment

Pros:
- almost plug-and-play with a 48 mm DeWalt vacuum
- rigid metal container, no collapse problem
- large 38 L capacity
- local warranty/return, no adapter guessing on stationary side

Cons:
- **1,299 SEK is expensive** for a passive cyclone+drum
- adds another large 43.5 × 43.5 × 55 cm wheeled object to the garage
- does not inherently solve the LR4 moving-hose 2.5-inch / static issue

**Verdict:** premium convenience fallback, not default Pareto choice.

## Option B — Dust Commander CLC: cheap functional baseline

Dust Commander `CLC`, SKU `DUST-CLC`:
- **€35.90** observed
- in stock
- polypropylene cyclone made in Europe
- claimed **99 %** separation
- inlet/outlet: **55 mm OD / 50 mm ID**
- 310 mm high
- includes mounting kit and 32/35 mm adapters
- designed for workshop/household shop-vacs, not 100 mm chip collectors

Source:
- https://dust-commander.com/collections/cyclone-filters-separators/products/dust-commander-clc

At the 2026-08-29 EUR reference (~11.13 SEK), raw cyclone cost is roughly **400 SEK** before Sweden shipping/container.

### Container note

Dust Commander explicitly recommends a strong steel drum. Plastic buckets can collapse under shop-vac vacuum if inlet is blocked; their optional anti-crush relief valve is €6.

A rigid reused steel drum/container could make this a very cheap system.

## Option C — Dust Commander DLX ESD MKII: current Pareto favourite

Dust Commander `DLX ESD MKII`:
- **€45.90** observed
- in stock
- 30 % glass-filled polyamide
- explicitly **antistatic / ESD**
- surface resistance <1E6 ohm/sq claimed
- >98 % dust separation claimed
- professional shop-vac cyclone class
- manufactured in Europe

Source:
- https://dust-commander.com/collections/cyclone-filters-separators/products/dust-commander-dlx-esd-mk2

Raw cyclone price is roughly **510 SEK** at the same EUR reference before shipping/container.

### Why the extra €10 is relevant here

This machine may cut XPS and V1E already warns about static in vacuum hose systems. An ESD cyclone does not magically ground a non-conductive entire hose network, but it removes one major insulating component and is a sensible place to spend ~€10 extra rather than improvising later.

**Current preferred cyclone:** DLX ESD MKII, provided Sweden-delivered total remains sensible.

## Option D — Dust Commander HD: overkill

Dust Commander `HD`:
- €109.90
- steel construction
- >99 % claimed efficiency
- 50 mm ports
- max flow around 240–300 m³/h depending current/revision datasheet

Technically excellent, but raw cost is already around the Jula DeWalt complete unit before a drum is added.

Not justified for the LR4 unless abrasive construction dust becomes a major separate use case.

## System architecture recommendation

Preferred arrangement:

`LR4 dust shoe -> light/flexible 2.5-inch groundable moving hose -> cyclone -> short stationary adapter/hose -> DeWalt 48 mm inlet`

Why:
- moving hose can be selected for flexibility/static rather than DeWalt compatibility
- cyclone protects DeWalt filter
- stationary side can cheaply use a printed/tapered adapter from ~50/55 mm cyclone to 48 mm DeWalt
- user's 3D printer makes odd hose diameters a trivial adapter problem

## Container strategy

Do not automatically buy a special dust drum.

First look for already-owned / near-free rigid container:
- steel paint/chemical drum with lid
- small steel ash/industrial bin
- rigid sealed metal bucket

Target size around **20–40 L** for this compact CNC. Huge 60–75 L units waste floor space.

Important: thin plastic buckets may implode at ~17 kPa vacuum under blockage. If plastic is used, add anti-collapse reinforcement or a vacuum relief valve.

## Current ranking

1. **Dust Commander DLX ESD MKII** — best match if delivered cyclone price remains roughly <=600–700 SEK and a cheap rigid container is available.
2. **Dust Commander CLC** — cheapest proven branded cyclone if ESD premium/shipping becomes unattractive.
3. **DeWalt DXVCS003** — 1,299 SEK plug-and-play fallback if we decide convenience is worth ~600–800 SEK extra.
4. **Dust Commander HD / larger professional separators** — unnecessary.

## Before ordering

- confirm actual DeWalt model/48 mm port from rating plate
- calculate Sweden shipping for CLC vs DLX ESD MKII
- check home/garage inventory for a rigid 20–40 L container
- then compare complete delivered cyclone system, not cyclone head alone
