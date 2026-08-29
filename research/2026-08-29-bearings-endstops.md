---
research_date: 2026-08-29
scope: 14× 608-2RS bearings and 5× LR4 endstops
status: recommendation-ready
decision_state: exact Omron endstop model preferred; bearing supplier still open
price_basis: observed web prices on 2026-08-29; re-check at checkout
region: Sweden / EU
sources_checked:
  - V1 Engineering LR4 hardware kit/docs
  - Omron official SS-series data
  - Farnell Sweden
  - RS Sweden
  - LaskaKit
  - Mouser Sweden
  - Motedis Sweden
  - Swedish bearing retailers
supersedes: null
---

# Research: bearings + endstops

Scope intentionally limited to:
- 14 × 608-2RS bearings
- 5 × endstop switches

## LR4 baseline

V1E's current LR4 hardware kit explicitly contains:
- **14 × 608-2RS**
- an **endstop kit with 5 Omron switches**

Sources:
- https://www.v1e.com/products/lowrider-v4-hardware-kit
- https://docs.v1e.com/lowrider/

## Endstops

### Exact V1E-style switch: Omron SS-5GL2

Verified specifications:
- Omron `SS-5GL2`
- subminiature snap-action switch
- hinge roller lever
- SPDT
- solder terminals
- body 19.8 × 10.6 × 6.4 mm
- roller 4.8 × 3.2 mm
- operating force max 0.49 N
- operating position ~14.5 mm (Omron/DigiKey data)
- mechanical life ~30 million operations

Sources:
- https://www.fa.omron.co.jp/product/item/SS-5GL2/
- https://omronfs.omron.com/en_US/ecb/products/pdf/en-ss.pdf
- https://www.digikey.com/en/products/detail/aratas-formerly-omron-components/SS-5GL2/137204

### Best Swedish exact-model source found: Farnell Sweden

Farnell Sweden currently indexes the **exact `SS-5GL2`**, order code `103445`:
- observed price: **23.13 SEK ex VAT each**
- 5 pcs = **115.65 SEK ex VAT / ~144.56 SEK incl VAT**
- listing showed the exact 0.49 N hinge-roller model

Source:
- https://se.farnell.com/en-SE/c/switches-relays/switches?brand=omron-electronic-components

Important: Farnell delivery messaging varies by product/cart threshold, so final shipping must be checked in checkout. Do not assume the single product-page banner is the final delivered cost.

### RS Sweden exact-model reference

RS `682-2660`, Omron `SS-5GL2`:
- 5-pack observed **109.90 SEK incl VAT**
- technically excellent
- RS current delivery policy: online orders below **750 SEK ex VAT** pay **119 SEK** freight; above that threshold delivery is free

Therefore RS is **not** automatically the cheapest source for this one item despite the lower switch price. It becomes interesting only if a larger RS cart naturally crosses the freight threshold.

Sources:
- https://se.rs-online.com/web/p/mikrobrytare/6822660
- https://se.rs-online.com/web/content/support/alla-artiklar/leverans

### LaskaKit generic alternative — very cheap, but not identical

LaskaKit `LA215019`, datasheet part `M140T01-AE0505A`:
- **€0.25 each**
- same body dimensions: 19.8 × 10.6 × 6.4 mm
- same 4.8 mm roller diameter
- SPDT, solder terminals
- operating force 0.59 N
- operating position 15.5 ±1.5 mm
- mechanical life 1,000,000 cycles

Compared with exact Omron:
- body envelope is essentially the same
- actuator/travel characteristics are **not identical**
- Omron OP ~14.5 mm vs generic 15.5 ±1.5 mm
- Omron 0.49 N vs generic 0.59 N
- Omron has much higher stated mechanical life

Sources:
- https://www.laskakit.cz/en/mikrospinac-s-pakou-a-kladkou-10t85-5a-250vac/
- https://www.laskakit.cz/user/related_files/10t85__.pdf

### Endstop decision

**Prefer the exact Omron `SS-5GL2`.**

Reason: the saving from the LaskaKit clone is only around a hundred-ish SEK at whole-machine scale, while V1E explicitly uses Omron and homing repeatability / physical trigger geometry is not a good place to introduce an avoidable variant.

Supplier is not fully locked until cart-level freight is known. Current leading channels:
1. Farnell Sweden exact `SS-5GL2`
2. RS exact 5-pack if another RS purchase makes freight economical

Do **not** substitute `SS-5GL2-F` just because it is in stock: it is the lower-force 0.16 N variant, not the exact standard `SS-5GL2`.

## 608-2RS bearings

### Required specification

- 608-2RS
- 8 mm ID
- 22 mm OD
- 7 mm width
- rubber seals both sides
- 14 required

V1E does not specify SKF/precision-premium bearings. These are commodity guide bearings in this application.

### Premium/local options are poor value

Observed references:
- SKF 608-2RS at Remlagret: ~37 SEK each → ~518 SEK for 14
- Clas Ohlson SKF: ~69.90 SEK each → obviously excessive for this use
- RS PRO 608-2RS: around 23–28 SEK each / packs around 111 SEK for five depending SKU → still much more than commodity sources

Sources:
- https://www.remlagret.se/products/608-2rs-skf-kullager-8x22x7
- https://www.clasohlson.com/se/Kullager-SKF-608-2RSH%2C-8x22x7mm/p/51-3030
- https://se.rs-online.com/web/p/linjara-lager/2612600

### Motedis proves the commodity price floor — but shipping kills a standalone order

Motedis Sweden lists exact **608 2RS 8×22×7 mm** at roughly **6.3–6.5 SEK incl VAT each**.

That means:
- 14 bearings ≈ 90 SEK in parts
- 20 bearings ≈ 129 SEK in parts

But Motedis Sweden accessory-only shipping is currently roughly **338–361 SEK**, so a standalone bearing order is irrational.

Sources:
- https://www.motedis.se/en/Bearing-Shop/Ball-bearing
- https://www.motedis.se/se/frakt-returer%3A_%3A1.html

### Farnell consolidation trap

Farnell has cheap 608-sized `MP-608-ZZ`, but **ZZ is metal-shielded, not 2RS rubber-sealed**. Do not substitute it merely to consolidate the Farnell cart.

Source:
- https://se.farnell.com/multicomp-pro/mp-608-zz/deep-groove-bearing-8x22x7mm-steel/dp/4692052

### Bearing decision

**Specification locked; supplier intentionally open.**

Target purchase:
- preferably **20 × 608-2RS** so there are six spares
- target delivered price: roughly **<=180 SEK**
- use Amazon/marketplace/commodity supplier only when exact 8×22×7 and 2RS are verified
- do not pay SKF/RS premium for this application
- do not create a 300+ SEK freight charge to save 80 SEK on the bearings themselves

No current indexed Amazon.se result could be verified end-to-end, so no Amazon ASIN is being recorded as approved yet.

## Cart-level implication

This slice changes the likely cart architecture:

- **LaskaKit mechanical cart:** keep GT2 idlers/belt + T8 rod/nuts + 5→8 couplers; do **not** add generic endstops merely for consolidation.
- **Endstops:** exact Omron from Farnell or RS depending final freight/cart.
- **Bearings:** wait for a cheap exact 20-pack that can ride with another order or has low/free shipping.

Potential later optimization: Farnell carries both exact Omron `SS-5GL2` and Mean Well `LRS-100-24`. Their combined cart is worth checking together with wiring/connectors because crossing Farnell's live free-shipping threshold may make that a strong electronics cart. Do not assume threshold until checkout is verified.
