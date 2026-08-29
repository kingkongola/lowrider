---
research_date: 2026-08-29
last_updated_at: 2026-08-29
scope: consolidated current order graph after component-level LR4 sourcing research
status: recommendation-ready
decision_state: most core machine hardware is now product-locked; remaining work is mainly checkout totals, PLA retry, table/base, first cutter/workholding and a few commodity orphan items
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
- DeWalt DXV30SAPTA-class shop-vac, likely exact DXV30SAPTA; image strongly matches
- TPU filament
- old FTX ventilation unit for possible secondary air handling
- 3D printer, therefore cyclone/adapters/dust-shoe components should be printed where rational

## Order 1 — LaskaKit: READY EXCEPT CHECKOUT VARIANTS

Core mechanical order:
- 6 × `LA190008E` smooth GT2 idlers, 10 mm belt / 5 mm bore
- 1 × `LA190032A` T8×8 400 mm rod
- 2 × `LA190033A` T8×8 brass nuts
- 2 × `LA190031` 5→8 mm couplers
- preferred 1 × `LA190013C` 5 m / 10 mm fiberglass GT2 belt
- fallback 3 × `LA190013B` 2 m if 5 m variant is unavailable

Low-voltage additions:
- 10 m `LA150151A` 26 AWG 3-core endstop cable
- ~1 m UL2464 20 AWG cable, explicitly choose **2-core** in product dropdown
- endstop board connectors:
  - loose 2-pin DuPont housing + `LA217002` sockets if a suitable crimper is already owned
  - otherwise `LA150090` pre-crimped pigtail set

Expected delivered total with preferred 5 m belt:
- **~€49–50** with loose connectors/crimper route
- **~€55** with pre-crimped pigtails

Fallback 3×2 m belt adds about **€6.89**.

Checkout-only checks:
- 5 m belt actual stock
- 2-core cable selected, not guessed by suffix
- connector route
- GLS Sweden still €8.93

## Order 2 — DigiKey: PURCHASE-READY

- 1 × Mean Well `HDR-60-24`, DigiKey `1866-2249-ND`
- 10 × Omron `SS-3GL13PT`, DigiKey `SW768-ND`

Why 10 switches:
- 5 installed
- 5 spares cost only ~32 SEK extra at qty-10 pricing

Current expected delivered total:
- **~495 SEK** including current 170 SEK small-order freight

Do not add filler merely to reach free-shipping threshold.

## Order 3 — StepperOnline Germany: PRODUCT-READY / FREIGHT CHECKOUT

- 1 × five-pack `5-17HS19-2004S1`
- five exact 59 Ncm / 83.55 oz-in / 2 A NEMA17 motors
- Germany warehouse must remain selected

Observed goods price:
- **€38.13**

Still unknown:
- exact Germany→Sweden freight

Do not move PSU/couplers into this cart via China inventory just to fake consolidation.

## Order 4 — VEVOR EU: PURCHASE-READY

Exact router only:
- VEVOR `0700C`
- SKU `YXKXBJ710W65AH7WLV2`
- product ID `010235793217`
- 800 W
- 65 mm body
- 10k–30k rpm

Observed official EU price:
- **€83.99**

Current VEVOR EU policy provides free standard shipping to Sweden for this product class.

Arrival gate:
- physically test already-paid Elaire collet seating/runout before cutting

## Order 5 — Jackpot3 / Elecrow: PRODUCT-READY / LANDED COST CHECKOUT

Exact controller:
- Jackpot3
- Elecrow SKU `CQA240812C2`
- observed **$76.99**
- in stock at last check

Must record at checkout:
- Sweden shipping
- whether VAT/IOSS is collected
- delivery method

Do not downgrade to Jackpot2 merely to save ~$22; Jackpot2 lacks PWM and conflicts with the planned future laser use.

Assume Elecrow board needs flashing/configuration after arrival.

## Local pickup — Motonet: NEAR PURCHASE-READY

- 2 × Motonet `88-7123`
- round steel tube Ø30×1.5 mm × 2 m
- **189 SEK each = 378 SEK**

Cut plan:
- bar 1 -> 1505 mm
- bar 2 -> 816 + 816 mm

Before payment:
- inspect both tubes for obvious bow/dents
- measure OD around several points; target nominal 30 mm and within V1E tolerance

This supersedes the previous default of sourcing 32×2 EN10305 tube from a steel merchant.

## NVR / emergency stop: DECISION-READY, SELLER CHECK REMAINS

Preferred device class:
- genuine KEDU KJD12
- 230 V
- DPST / 2 pole
- 16 A class
- NVR/no-restart
- emergency-stop cover/button

Preferred if genuine KEDU all-in <=500 SEK.

Verified domestic fallback:
- IKH Sweden `XW026-1`
- KJD12 10/16A 57×35, emergency-stop listing
- ~357 SEK + service-point shipping from 125 SEK
- **~482 SEK indicative delivered**
- IKH page does not explicitly state KEDU manufacturer, so explicitly branded KEDU wins at same total

### Machine power topology now simplified

DXV30SAPTA manual explicitly gives **2450 W maximum connected-tool load**.

VEVOR is only 800 W, so baseline is:

`wall -> KJD12 -> [HDR-60-24 + DeWalt in AUTO mode]`

and

`VEVOR -> DeWalt tool socket`

No separate vacuum trigger relay is needed.

## Cheap orphan 1 — 16T pulleys

Need 3:
- GT2 2 mm
- 16T
- 5 mm bore
- 10 mm belt

Preferred exact listing:
- Allegro `GT2-16T-5B_10mm_K`
- 7.20 PLN each
- 2 set screws

Buy if 3 delivered to Sweden are roughly <=150–180 SEK.

Fallback:
- verified AliExpress Choice 5-pack only if checkout explicitly shows 16T / 5 mm / 10 mm and delivered total <=120–150 SEK.

## Cheap orphan 2 — 608-2RS

Need 14, buy 20.

Specification:
- 608-2RS
- 8×22×7 mm
- double rubber seal

First check:
- active Swedish Tradera 608 seller
- historical exact 20-pack benchmark: 170 + 10 SEK shipping

Buy an active exact 20-pack if <=200 SEK delivered.

Fallback:
- 2×10 cheap exact packs from Allegro if Sweden freight wins

Amazon Prime is opportunistic only; no current exact Amazon.se 20-pack was verified.

## Dust hardware: MOSTLY BUILD, NOT BUY

Already owned DeWalt removes the shop-vac purchase entirely.

Current plan:
- print dust shoe
- use owned TPU for V1E bristles if ~95A
- dry-fit existing 48 mm × 2.1 m DeWalt hose before buying another moving hose
- print a proven cyclone
- mount on a small rigid steel collection container
- print hose adapters to actual measured diameters
- support hose from gantry/overhead
- evaluate old FTX only for secondary fine-air/enclosure duty

Current likely bought dust item:
- ~15–20 L rigid steel ash bucket/container if no suitable container already exists, roughly ~160–200 SEK benchmark

## Still genuinely open

These remain worth researching/deciding; most other core hardware is now solved:

### PLA
- need ~2.7 kg to print machine; buy 4–6 kg
- ordinary stiff PLA
- prior leader SUNLU 5 kg bulk around 100 SEK/kg class
- current live-search backend failed during latest retry; **do not update price until fresh checkout/search succeeds**

### Table/base
- search for stable cheap used dining/conference-table base
- CNC cassette ~1000×1620 mm
- reuse suitable tabletop as structural deck if possible
- otherwise OSB/plywood deck + removable ~12 mm MDF spoilboard

### First cutter(s)
- 3.175 mm single-flute upcut
- short learning/general cutter first
- long cutter only when 18–19 mm plywood requires it

### Workholding / small consumables
- first clamps/screws strategy
- threadlocker
- heatshrink/cable ties as actually needed
- machine-level mains enclosure/distribution hardware around KJD12/HDR

## Order-placement sequence

Best practical sequence once ready to spend:

1. Motonet tubes — local, inspect first
2. LaskaKit — some lower-stock T8/belt components
3. StepperOnline motors — Germany warehouse
4. DigiKey HDR + Omron
5. VEVOR router
6. Jackpot3 Elecrow
7. orphan 16T + 608 when thresholds are met
8. PLA when fresh bulk deal is verified
9. table/spoilboard material only after used-base decision

This order is about avoiding stock loss and wrong-variant risk, not technical build order.