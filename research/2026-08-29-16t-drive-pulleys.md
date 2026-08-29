---
researched_at: 2026-08-29
scope: 3 x GT2 16T drive pulleys for 10 mm belt, 5 mm motor bore
status: researched-not-ordered
confidence: high-on-spec-medium-on-supplier
machine_target: LowRider V4, ~650x1250 mm usable area
constraints:
  - exact LR4 geometry only
  - avoid 6 mm belt variants
  - optimize delivered cart cost, not unit price
sources_checked:
  - Hellas Digital Greece
  - Anodas Lithuania
  - Allegro Poland
  - Swedish/general web search
observed_prices_are_time_sensitive: true
---

# Research: remaining 16T drive pulleys

Scope is intentionally limited to the three motor pulleys still missing from the leading LaskaKit mechanical cart.

## Exact LR4 requirement

Need 3 pulleys with all of the following:
- GT2 / 2 mm pitch
- 16 teeth
- 5 mm motor-shaft bore
- designed for **10 mm belt**
- aluminum is fine
- grub-screw locking preferred

The common 16T/5 mm pulley for 6 mm belt is **wrong** even though the tooth count and bore are correct.

## Candidate A — Hellas Digital `070.0051`

Verified product:
- code `070.0051`
- GT2
- 16T
- 5 mm bore
- 10 mm belt width
- listed in stock
- observed price **€1.61 incl VAT each**
- 3 parts = **€4.83**

Source:
- https://www.hellasdigital.gr/go-create/3d-printing/accessories/gt2-16t-bore-5mm-width-10mm-pulley/?sl=en

Hellas Digital shipping page confirms DHL Express is available and final international cost is calculated at checkout. Their €3.50–4 domestic courier rates must **not** be assumed to apply to Sweden.

Source:
- https://www.hellasdigital.gr/shipping/?sl=en

**Assessment:** best raw unit price, but do not create a Greece shipment for €4.83 of pulleys unless checkout shipping is unusually cheap or other required items can be added.

## Candidate B — Allegro Poland `GT2-16T-5B_10mm_K`

Verified listing:
- product code `GT2-16T-5B_10mm_K`
- 16T
- 10 mm belt
- 5 mm bore
- 11 mm toothed running width
- aluminum
- **two locking grub screws**
- observed price **7.20 PLN each**
- listing had multiple recent sales and 5.0 rating at time of observation

Sources:
- https://allegro.pl/produkt/napedowe-kolo-zebate-gt2-na-pasek-10mm-walek-5mm-16t-cnc-druk-3d-ceec4f7d-f776-4e22-bf35-a76392e738d6
- https://allegro.pl/oferta/napedowe-kolo-zebate-gt2-na-pasek-10mm-walek-5mm-16t-cnc-druk-3d-18355347606

**Assessment:** technically excellent commodity candidate, and the dual grub screws are desirable. Sweden shipping still needs checkout verification.

## Candidate C — Anodas `AN-18925`

Verified product:
- product code `AN-18925`
- 16T
- 10 mm belt
- 5 mm bore
- aluminum
- M2 adjustment/set screw
- observed price **€3.00 each**
- 3 = €9.00 before shipping

Source:
- https://www.anodas.lt/en/16t-sprocket-for-gt2-10mm-belt-5mm-bore

**Assessment:** exact and credible, but unit price is higher than Hellas/Allegro and shipping economics are still unknown.

## Swedish/Amazon result

No Swedish/Amazon.se listing was found in indexed search that could be confidently verified as the exact combination **16T + 5 mm bore + 10 mm belt** at a delivered price beating the EU candidates.

Do not substitute a search-result bundle unless the selected option is manually verified. The dominant traps remain:
- 6 mm belt width
- 20T instead of 16T
- 6.35 or 8 mm bore

## Current purchase strategy

The leading LaskaKit cart already covers:
- 5 m correct 10 mm fiberglass GT2 belt
- 6 smooth idlers
- 400 mm Tr8x8 rod
- 2 T8x8 nuts
- 2 flexible 5→8 couplers

Therefore these three pulleys are a **small orphan line item**.

Best strategy:
1. do not split the good LaskaKit cart just to chase pulleys
2. at final checkout, first test Allegro/Hellas Sweden shipping
3. if shipping is disproportionate, buy a slightly more expensive exact 3-pack from Amazon/EU marketplace instead
4. tolerate roughly **50–100 SEK extra component cost** if it avoids another €10–20 parcel

## Decision state

- specification: **LOCKED**
- supplier: **OPEN**
- best raw price: Hellas Digital
- best mechanical listing so far: Allegro dual-grub-screw part
- purchase should wait until final cart consolidation / Sweden shipping is known
