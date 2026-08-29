---
research_date: 2026-08-29
scope: 14× 608-2RS bearings and 5× LR4 endstops
status: recommendation-ready
decision_state: exact V1E-style Omron SS-3GL13PT preferred; bearing supplier still open
price_basis: observed web prices on 2026-08-29; re-check at checkout
region: Sweden / EU
sources_checked:
  - V1 Engineering current limit-switch product page
  - V1 Engineering LR4 community replacement threads
  - DigiKey Sweden
  - LaskaKit
  - Swedish bearing retailers
  - Tradera / marketplace references
supersedes: earlier version of this file and PROCUREMENT.md assumption that SS-5GL2 is the exact default
---

# Research: bearings + endstops

Scope intentionally limited to:
- 14 × 608-2RS bearings
- 5 × LR4 homing/endstop switches

## 1. Endstops — important correction

### Verified V1E baseline: Omron `SS-3GL13PT`

The current V1E limit-switch product page identifies the Omron part as **`SS-3GL13PT`**. A January 2026 LR4 replacement thread also explicitly says this is the commonly used replacement part number.

Verified characteristics:
- Omron `SS-3GL13PT`
- SPDT snap-action microswitch
- simulated roller lever actuator
- 3 A at 125 VAC / 3 A at 30 VDC class
- chassis mount
- quick-connect terminals around 0.110 in / 2.8 mm
- IP40
- usable NC or NO

Sources:
- https://www.v1e.com/products/limit-switch-endstop
- https://forum.v1e.com/t/endstop-where-to-order/52822
- https://www.digikey.se/en/products/detail/omron-electronics-inc-emc-div/SS-3GL13PT/664729

### DigiKey price reference

Observed 2026-08-29:
- DigiKey Sweden `SS-3GL13PT`
- 48k+ stock in indexed result
- 8.04 SEK ex VAT / **10.05 SEK incl VAT each** at qty 1
- 5 pcs ≈ **50.25 SEK incl VAT** before order freight

The exact switch is cheap enough that there is little reason to substitute a geometrically different no-name part merely to save tens of SEK.

### `SS-5GL2` is an alternative/mod, not the baseline

Earlier research incorrectly promoted Omron `SS-5GL2` as the exact standard LR4 switch.

`SS-5GL2` is a legitimate small Omron true roller-wheel switch, and community users have deliberately used it. That can be attractive because the thin lever on the stock-style switch may bend or detach.

However, this is an **actuator-geometry change**, not the current V1E baseline. Recent LR4 discussions also show that generic roller-switch substitutions can fail physically even when the body looks similar.

Therefore:
- default / reference build: **SS-3GL13PT**
- optional deliberate community alternative: **SS-5GL2**

Do not mix the two in procurement notes.

### LaskaKit consolidation check

LaskaKit `LA215004` is listed as a genuine Omron plain-lever switch at about €0.99, but it is **not** the V1E `SS-3GL13PT` simulated-roller geometry.

LaskaKit's own product discussion includes a request for an `SS-5GL2` roller-lever version and points to a different generic roller switch, confirming `LA215004` is not an exact substitute.

Source:
- https://www.laskakit.cz/en/omron-koncovy-spinac-pakovy-5a-125vac/

### Endstop decision

**Recommendation-ready:** buy 5 × exact **Omron `SS-3GL13PT`** for the baseline build.

Do not add LaskaKit's cheap plain-lever switch merely to consolidate freight.

Supplier remains open because the switches themselves cost only ~50 SEK at DigiKey and small-order freight can dominate. They should ideally ride in the same electronics order as PSU/connectors/other genuinely needed electrical parts.

## 2. 608-2RS bearings

### Verified LR4 requirement

Quantity:
- **14 × 608-2RS**

Exact type:
- 8 mm ID
- 22 mm OD
- 7 mm width
- rubber seals both sides (`2RS`)

Do not silently substitute `608ZZ`. Metal shields are not equivalent to rubber seals, and the dusty garage makes the V1E-specified 2RS form particularly sensible.

### Swedish specialist price references

Observed examples:
- Remlagret SKF 608-2RS: ~37 SEK each
- Kullager.se economy 608-2RS: ~18.75 SEK each
- RS PRO 608-2RS: ~111.41 SEK incl VAT per 5-pack

These are valid products but poor whole-machine value compared with a decent commodity 20-pack.

Sources:
- https://www.remlagret.se/products/608-2rs-skf-kullager-8x22x7
- https://www.kullager.se/kullager-608-2rs-8x22x7
- https://se.rs-online.com/web/p/linjara-lager/2612600

### Commodity 20-pack references

Observed Swedish marketplace evidence has shown exact 20 × 608-2RS / 8×22×7 packs around **150–170 SEK** plus low/free shipping depending listing.

A known Amazon-market candidate is TIMESETL 20-pack 608-2RS, ASIN **`B07X5T7DGS`**, exact 8×22×7 with double rubber seals. A reliable current Amazon.se price was not exposed by indexing, so this is a search key, **not an approved live offer**.

### Bearing decision

**Specification locked; supplier intentionally open.**

Target buy:
- 1 × 20-pack `608-2RS`
- exact 8×22×7 mm
- double rubber seals
- ordinary chrome/bearing steel is fine
- six spares are useful

Target delivered price:
- **~120–200 SEK / 20 pcs**

Do not pay SKF/industrial-retailer pricing for this LR4 role.

## Cart-level implication

Current likely architecture:
- **LaskaKit mechanical cart:** GT2 idlers + 5 m belt + T8 rod + T8 nuts + 5→8 couplers
- **Endstops:** exact `SS-3GL13PT`, ideally added to the electronics/PSU cart
- **608 bearings:** Prime/Swedish commodity 20-pack when an exact 2RS offer is ≤~200 SEK delivered

This is a good example of the procurement rule: consolidate only when the substitute remains technically equivalent.

## Next research slice

Optimize the electronics cart around:
- PSU candidate
- 5 × `SS-3GL13PT`
- required endstop terminals/pigtails/cable
- only genuinely mandatory small electrical parts

Goal: determine whether a DigiKey/RS/Farnell cart reaches economical shipping without buying filler.