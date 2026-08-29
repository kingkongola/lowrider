---
research_date: 2026-08-29
last_updated_at: 2026-08-29
scope: consolidated current order graph after component-level LR4 sourcing research
status: recommendation-ready
decision_state: core machine hardware and PLA are product-locked or threshold-locked; remaining work is mainly checkout totals, table/base, first cutter/workholding and machine mains enclosure/distribution hardware
price_basis: only prices already verified in dated research files; unknown checkout freight/import is left unknown rather than estimated
region: Sweden / EU
sources_checked:
  - BOM.md
  - research/2026-08-29-laskakit-final-mechanical-cart.md
  - research/2026-08-29-final-psu-endstop-wiring-cart.md
  - research/2026-08-29-stepperonline-motor-order-live.md
  - research/2026-08-29-jackpot3-order.md
  - research/2026-08-29-vevor-0700c-router.md
  - research/2026-08-29-steel-tubes-gavle.md
  - research/2026-08-29-16t-bearings-orphan-cart.md
  - research/2026-08-29-final-nvr-estop.md
  - research/2026-08-29-dewalt-tool-socket.md
  - research/2026-08-29-pla-bulk.md
supersedes: null
---

# Current purchase-ready order graph

This file is a status/index, not the evidence source for individual parts. Follow the dated research file for exact SKU, caveats and source URLs.

## Already paid / owned

### HaWiWe — CLOSED
Paid total: **€165.50 incl €8 shipping**.

Covers:
- aluminium XZ plates
- 4 × MGN12H 150 mm rails
- LR4 screw/nut set
- Elaire/Makita-style 1/8 in collet

### Already owned
- DeWalt DXV30SAPTA-class shop-vac, image strongly matches exact DXV30SAPTA
- TPU filament
- old FTX ventilation unit for possible secondary air handling
- 3D printer, so cyclone/adapters/dust-shoe components should be printed where rational

## Order 1 — LaskaKit: READY EXCEPT CHECKOUT VARIANTS

Core mechanical order:
- 6 × `LA190008E` smooth GT2 idlers, 10 mm belt / 5 mm bore
- 1 × `LA190032A` T8×8 400 mm rod
- 2 × `LA190033A` T8×8 brass nuts
- 2 × `LA190031` 5→8 mm couplers
- preferred 1 × `LA190013C` 5 m / 10 mm fiberglass GT2 belt
- fallback 3 × `LA190013B` 2 m if 5 m variant unavailable

Low-voltage additions:
- 10 m `LA150151A` 26 AWG 3-core endstop cable
- ~1 m UL2464 20 AWG cable, explicitly choose 2-core
- endstop board connectors:
  - loose 2-pin DuPont housing + `LA217002` sockets if a suitable crimper is owned
  - otherwise `LA150090` pre-crimped pigtail set

Expected delivered with 5 m belt:
- **~€49–50** with loose connector/crimper route
- **~€55** with pre-crimped pigtails

Fallback 3×2 m belt adds ~€6.89.

Checkout checks:
- 5 m belt stock
- 2-core PSU cable selected visibly
- connector route
- GLS Sweden still €8.93

## Order 2 — DigiKey: PURCHASE-READY

- 1 × Mean Well `HDR-60-24`, DigiKey `1866-2249-ND`
- 10 × Omron `SS-3GL13PT`, DigiKey `SW768-ND`

5 are installed; 5 spares add only ~32 SEK at qty-10 pricing.

Current expected delivered:
- **~495 SEK** including current 170 SEK small-order freight

Do not add filler merely to reach free shipping.

## Order 3 — StepperOnline Germany: PRODUCT-READY / FREIGHT CHECKOUT

- five-pack `5-17HS19-2004S1`
- 59 Ncm / 83.55 oz-in / 2 A NEMA17
- Germany warehouse must remain selected

Observed goods price:
- **€38.13**

Unknown:
- Germany→Sweden freight

Keep this motors-only unless another exact required part genuinely ships from the same German warehouse.

## Order 4 — VEVOR EU: PURCHASE-READY

Exact router:
- VEVOR `0700C`
- SKU `YXKXBJ710W65AH7WLV2`
- product ID `010235793217`
- 800 W
- 65 mm
- 10k–30k rpm

Observed official EU price:
- **€83.99**

Current VEVOR EU policy gives free standard shipping to Sweden for this product class.

Arrival gate:
- test already-paid Elaire collet seating/runout before cutting

## Order 5 — Jackpot3 / Elecrow: PRODUCT-READY / LANDED COST CHECKOUT

- Jackpot3
- Elecrow SKU `CQA240812C2`
- observed **$76.99**
- in stock at last verification

At checkout record:
- Sweden shipping
- VAT/IOSS treatment
- delivery method

Do not downgrade to Jackpot2: it lacks PWM and conflicts with future laser use.

Assume Elecrow board needs flashing/configuration after arrival.

## Order 6 — PLA: RECOMMENDATION-READY

Current Pareto default:
- **SUNLU ordinary PLA**
- **6 × 1 kg normal spools**
- Mix & Match bulk tier
- current advertised 6-roll tier from **€9.19/kg**
- approximate six-roll subtotal **€55.14** / ~614 SEK at the 2026-08-29 reference FX
- SUNLU states free shipping to most EU regions

Why this beats the €39.99 5 kg giant spool as default:
- ordinary spool handling
- individual sealed rolls
- deliberate colour mix
- no heavy-spool holder side project
- only ~€15 raw-material premium

Suggested split:
- 4–5 rolls main colour
- 1–2 rolls accent colour

Fallback:
- Creality Soleyin Ultra 6 kg, €59, if the currently sold-out combo returns

Absolute cheapest:
- SUNLU 5 kg giant spool ~€39.99 if single-colour and large-spool handling is intentionally accepted

Checkout gate:
- explicitly ordinary PLA
- Europe/Sweden destination
- 6-roll discount actually applied
- free/low shipping holds

## Local pickup — Motonet: NEAR PURCHASE-READY

- 2 × Motonet `88-7123`
- round steel tube Ø30×1.5 mm × 2 m
- **189 SEK each = 378 SEK**

Cut:
- bar 1 -> 1505 mm
- bar 2 -> 816 + 816 mm

Before payment:
- inspect for bow/dents
- measure OD at several points

## NVR / emergency stop: DECISION-READY

Preferred:
- genuine KEDU KJD12
- 230 V
- DPST / 2 pole
- 16 A class
- NVR/no-restart
- emergency-stop cover/button

Choose an explicitly genuine KEDU if all-in <=500 SEK.

Swedish fallback:
- IKH `XW026-1`
- KJD12 10/16A 57×35 emergency-stop listing
- ~357 SEK + service-point shipping from 125 SEK
- **~482 SEK indicative delivered**
- IKH page does not explicitly state KEDU manufacturer

### Machine-power topology

DXV30SAPTA manual gives **2450 W max connected-tool load**.

VEVOR is 800 W, so baseline:

`wall -> KJD12 -> [HDR-60-24 + DeWalt AUTO]`

`VEVOR -> DeWalt tool socket`

No separate vacuum-trigger relay required.

## Cheap orphan 1 — 16T pulleys

Need 3 exact:
- GT2 2 mm
- 16T
- 5 mm bore
- 10 mm belt

Preferred exact listing:
- Allegro `GT2-16T-5B_10mm_K`
- 7.20 PLN each
- 2 set screws

Buy if 3 delivered are <=150–180 SEK.

Fallback:
- AliExpress Choice 5-pack only if checkout visibly resolves 16T / 5 mm / 10 mm and <=120–150 SEK delivered.

## Cheap orphan 2 — 608-2RS

Need 14, buy 20.

- 608-2RS
- 8×22×7 mm
- double rubber seal

First check:
- active Swedish Tradera 608 seller
- historical exact 20-pack benchmark 170 + 10 SEK freight

Buy current exact 20-pack if <=200 SEK delivered.

Fallback:
- 2×10 cheap exact Allegro packs if Sweden freight wins

Amazon Prime is opportunistic only; no current exact Amazon.se 20-pack was verified.

## Dust hardware: MOSTLY BUILD, NOT BUY

Owned DeWalt eliminates a new vacuum.

Plan:
- print dust shoe
- use owned TPU for V1E bristles if ~95A
- test existing 48 mm ×2.1 m hose first
- print proven cyclone
- small rigid steel collection container
- print measured adapters
- hose support/boom
- old FTX only as possible secondary enclosure/fine-air system

Likely bought dust item:
- ~15–20 L steel ash bucket/container if nothing suitable already exists, benchmark ~160–200 SEK

## Still genuinely open

### Table/base
- stable used dining/conference-table base
- CNC cassette ~1000×1620 mm
- reuse suitable tabletop as structural deck if possible
- otherwise OSB/plywood deck + removable ~12 mm MDF spoilboard

### First cutter(s)
- 3.175 mm single-flute upcut
- short general/learning cutter first
- long cutter only for 18–19 mm plywood

### Workholding / small consumables
- first clamps/screws strategy
- threadlocker
- heatshrink/cable ties as needed

### 230 V enclosure/distribution
- compact enclosure/panel around KJD12 and HDR
- strain relief
- appropriately rated machine distribution/outlets and mains cable
- PE continuity
- no exposed live terminals

## Order-placement sequence

1. Motonet tubes — inspect locally
2. LaskaKit — lower-stock T8/belt components
3. StepperOnline motors — Germany warehouse
4. DigiKey HDR + Omron
5. VEVOR router
6. Jackpot3 Elecrow
7. SUNLU PLA when checkout holds ~€55–60 / ~100–110 SEK/kg
8. orphan 16T + 608 under thresholds
9. table/spoilboard material after used-base decision

This sequence prioritizes stock/wrong-variant risk rather than technical assembly order.