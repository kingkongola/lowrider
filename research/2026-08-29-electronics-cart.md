---
research_date: 2026-08-29
scope: cart-level comparison for 24 V PSU + exact Omron SS-5GL2 + endstop cable; identify next consolidation target
status: exploring
decision_state: do not place Farnell/DigiKey electronics order yet; next compare required safety/control-box parts to reach rational freight threshold
price_basis: observed Sweden web prices on 2026-08-29; prices exclude VAT where explicitly stated; re-check checkout
region: Sweden
sources_checked:
  - Farnell Sweden
  - DigiKey Sweden
  - RS Sweden
supersedes: null
---

# Research: electronics cart economics

This slice exists because isolated line-item prices are misleading once freight thresholds are included.

Current needed items under consideration:
- 24 V PSU
- 5 × exact Omron `SS-5GL2`
- ~6 m endstop wire (unless sourced cheaply elsewhere)

## Farnell cart

### Mean Well LRS-100-24

Farnell order code `2815968`:
- 24 V / 4.5 A / 108 W
- observed web price around **240.72-247.81 SEK ex VAT** depending current page crawl
- hundreds in stock

Source:
- https://se.farnell.com/mean-well/lrs-100-24/power-supply-ac-dc-24v-4-5a/dp/2815968

### Exact Omron SS-5GL2

Farnell order code `103445`:
- exact `SS-5GL2`
- observed **23.13 SEK ex VAT each**
- 5 × = **115.65 SEK ex VAT**

Source:
- https://se.farnell.com/en-SE/c/switches-relays/switches?brand=omron-electronic-components

### 22 AWG 2-core cable

Verified technically good candidate:
- Alpha Wire `B954021`
- 2 core
- 22 AWG / ~0.32 mm²
- stranded tinned copper
- observed ~30.95 SEK/m at 5+ m

6 m ≈ **185.70 SEK ex VAT**.

Source:
- https://se.farnell.com/c/cable-wire-cable-assemblies/multicore-cable?brand=alpha-wire&no-of-cores=2core

### Approximate Farnell subtotal

Using 240.72 PSU price:
- PSU: 240.72 ex VAT
- 5 Omron: 115.65 ex VAT
- 6 m cable: 185.70 ex VAT
- subtotal: **542.07 SEK ex VAT**
- incl 25% VAT: **~677.59 SEK**

This makes the cable surprisingly expensive: ~232 SEK incl VAT just to obtain ~6 m of endstop wire.

### Farnell freight ambiguity

Farnell's current Swedish site is internally inconsistent:
- current product/banner pages say free standard delivery on orders **500 SEK and over**
- a help delivery page still says free over **850 SEK ex VAT**, otherwise 135 SEK
- site-wide messaging explicitly says the minimum order value was recently lowered from 850 to 500 SEK

Inference: the 850 SEK help text may be stale, but **checkout must be treated as authoritative**. Do not build the optimization on presumed free freight.

Sources:
- https://se.farnell.com/flexibla-leveransalternativ
- https://se.farnell.com/en-SE/help-delivery-information
- https://se.farnell.com/

## DigiKey cart

### Mean Well LRS-100-24

DigiKey `1866-3314-ND`:
- observed **142.60 SEK ex VAT / 178.25 incl VAT**
- 3814 in stock on observed page

Source:
- https://www.digikey.se/sv/products/detail/mean-well-usa-inc/LRS-100-24/7705008

### Exact Omron SS-5GL2

DigiKey current filter result:
- exact `SS-5GL2`
- observed **24.27 SEK ex VAT each**
- 5 = 121.35 ex VAT / ~151.69 incl VAT
- large stock shown

Source:
- https://www.digikey.se/en/products/filter/limit-switches/198

### DigiKey subtotal before freight

- PSU incl VAT: ~178.25 SEK
- 5 switches incl VAT: ~151.69 SEK
- subtotal: **~329.94 SEK incl VAT**

Current DigiKey Sweden freight policy:
- free shipping >= **615 SEK**
- **170 SEK** shipping below 615 SEK

Thus PSU + switches as a standalone order becomes roughly **~499.94 SEK delivered**, before endstop cable.

Source:
- https://www.digikey.se/sv/help-support/delivery-information/delivery-time-and-cost

## RS reference

RS Sweden freight remains:
- 119 SEK online shipping
- free only above 750 SEK ex VAT

This keeps RS less attractive for a small exact-Omron-only order even when its line-item switch price looks low.

Source:
- https://se.rs-online.com/web/content/support/alla-artiklar/leverans

## Cart-level conclusion

### Do not buy expensive endstop cable merely to trigger free freight

Farnell's Alpha Wire is excellent cable, but paying ~232 SEK incl VAT for ~6 m of low-current endstop wire is unnecessary when ordinary flexible 22-24 AWG stranded copper will perform the job.

Therefore:
- do **not** use the Farnell cable as artificial cart filler
- source cheap proper copper endstop cable locally/Amazon/commodity seller unless a later consolidated cart makes the premium effectively free

### DigiKey is now a strong electronics-cart candidate

DigiKey's underlying part cost for genuine Mean Well + exact Omron is excellent, but the order is ~285 SEK short of its current 615 SEK free-shipping threshold.

Rather than paying 170 SEK freight immediately, the next research slice should check **real required control/safety electronics** that can legitimately share this order, e.g.:
- emergency-stop / main disconnect components
- fused mains inlet / fuse holder if using LRS-100-24
- terminal blocks / strain relief / cable glands
- suitable 24 V enclosure fan if needed
- low-voltage distribution/connectors

If ~285 SEK of genuinely required parts can be sourced competitively from DigiKey, free freight would effectively convert the 170 SEK delivery fee into useful machine hardware.

This is preferable to buying unnecessary wire or random spares just to cross a threshold.

## Decision

**No electronics order yet.**

Next small procurement slice: design the minimal safe **power/control box** around Jackpot3 + LRS/GST PSU, then price only the parts that are actually required. Use those results to decide whether DigiKey, Farnell, or another EU seller becomes the electronics cart.
