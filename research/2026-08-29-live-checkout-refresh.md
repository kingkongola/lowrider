---
research_date: 2026-08-29
last_updated_at: 2026-08-29
scope: live availability/price refresh for orphan parts and first purchase-ready LR4 carts after canonical repo reconciliation
status: recommendation-ready
decision_state: orphan specs unchanged; 608 Swedish 2x8 fallback remains viable only if Tradera combines freight; Motonet tube and LaskaKit core cart are still live and correctly specified; StepperOnline motors and DigiKey HDR/Omron are also still in stock at expected prices
price_basis: live/indexed retailer pages checked 2026-08-29; checkout shipping/combined freight remains authoritative
region: Sweden / EU
sources_checked:
  - Tradera Motion_And_Rotaion current 608 listing
  - Allegro exact 16T listing/search
  - Motonet exact 88-7123 product page
  - LaskaKit current POWGE/CNC/cable pages
  - StepperOnline current five-pack page
  - DigiKey current HDR-60-24 and Omron SS-3GL13PT pages
supersedes: null
---

# Live checkout refresh — 2026-08-29

Purpose: verify that the already-locked procurement plan is still actionable. This is not a new architecture pass.

## 1. 608-2RS — current Swedish fallback still live

Current Tradera business seller `Motion_And_Rotaion` has a live exact listing:
- model: `608-2RS`
- dimensions: **8×22×7 mm**
- double rubber seal
- set of **8**
- price: **79 SEK**
- displayed Sweden freight: **39 SEK**
- seller advertises 3-day samfrakt window

Current listing checked:
- https://www.tradera.com/item/2510/747330721/608-2rs-skateboard-inline-skate-scooter-8-ball-bearings-blue-rubber-sealed

Two packs would provide 16 bearings, enough for 14 installed + 2 spare.

Conditional combined total if one freight charge applies:
- 79 + 79 + 39 = **197 SEK delivered**

**Decision:** buy this route if combined checkout visibly confirms <=200 SEK. Do not assume samfrakt before seeing the combined total.

A 20-pack <=200 SEK remains slightly better because it leaves 6 spares, but no reason exists to delay the build indefinitely for exactly 20 if the 16-pack route checks out at 197 SEK.

## 2. GT2 16T / 5 mm / 10 mm — spec unchanged

The exact Allegro family remains indexed for:
- GT2 / 2 mm pitch
- **16T**
- **5 mm bore**
- **10 mm belt**
- two grub screws

Preferred product code remains `GT2-16T-5B_10mm_K`.

Raw price remains low enough that **Sweden freight is the only meaningful variable**.

**Decision:** keep existing threshold: buy 3 if delivered total is <=150–180 SEK. If Allegro Sweden shipping is disproportionate, use an exact Choice/EU fallback rather than changing the spec.

## 3. Motonet rails — exact product still listed

Motonet Sweden currently lists:
- article **`88-7123`**
- round tube **Ø30×1.5 mm**
- length **2000 mm**
- price **from 189 SEK each**

Source:
- https://www.motonet.se/produkt/rundror-o-30-x-15-mm-2-m?product=88-7123

Need two:
- goods price **378 SEK**

This still satisfies the V1E nominal OD/wall requirement on paper.

**Physical gate remains mandatory:** measure OD and inspect straightness/dents before cutting or treating the purchase as accepted machine rails.

## 4. LaskaKit — core cart currently healthy

Fresh current/indexed LaskaKit state:

### Smooth idlers
`LA190008E`
- smooth GT2 idler
- 5 mm bearing/bore
- for 10 mm belt
- **in stock: 76 pcs** at current check
- **€1.87 incl VAT each**

Need 6.

### 5 m GT2 belt
`LA190013C`
- 5 m
- 10 mm
- fiberglass reinforced
- **in stock: 18 pcs**
- **€7.81 incl VAT**

This confirms the preferred one-roll route is currently available. No need to use 3×2 m fallback while this state holds.

### T8×8 rod
`LA190032A`
- 400 mm
- T8×8 / 4-start
- stainless 304
- current indexed stock remains available
- current English page price around **€8.15 incl VAT**

### T8×8 brass nuts
`LA190033A`
- exact T8×8 / 4-start
- current indexed stock available
- **€1.31 incl VAT each**

Need 2.

### 5→8 couplers
`LA190031`
- current category page shows **in stock: 19 pcs**
- **€1.83 incl VAT each**

Need 2.

### Endstop cable
`LA150151A`
- UL2464 26 AWG, 3×0.14 mm²
- current stock hundreds of metres
- from **€0.58/m**

Buy 10 m as planned.

### 20 AWG low-voltage cable
LaskaKit UL2464 20 AWG family remains in stock, hundreds of metres.

Still select **2-core** visibly in product UI before adding; indexed page does not safely map suffix to conductor count.

**LaskaKit conclusion:** product availability currently supports placing the preferred cart. The limiting questions are only exact checkout shipping and connector-route choice, not component availability.

## 5. StepperOnline motors — unchanged and live

Current five-pack:
- `5-17HS19-2004S1`
- **€38.13** on the European/NL storefront
- stock shown: **200**
- Germany warehouse remains offered as a ship-from option

Electrical/mechanical spec remains exactly the locked one:
- 59 Ncm / 83.55 oz-in
- 2 A
- 42×42×48 mm
- 5 mm D-shaft
- 24 mm shaft
- 1 m cable

**Decision:** keep motors-only Germany-warehouse order. Final Sweden freight remains checkout-only.

## 6. DigiKey HDR + Omron — unchanged and live

### Mean Well HDR-60-24
Current DigiKey Sweden:
- part `1866-2249-ND`
- **5828 in stock**
- **194.20 SEK ex VAT / 242.75 SEK incl VAT** at qty 1

### Omron SS-3GL13PT
Current DigiKey Sweden:
- part `SW768-ND`
- **48,048 in stock**
- qty 1: 8.04 SEK ex VAT
- qty 10 tier: **6.618 SEK ex VAT each**

The planned 1×HDR + 10×Omron cart therefore remains rational. No reason to reopen PSU or endstop alternatives.

## Current action state

### Can be acted on immediately
- Motonet tube: inspect/reserve/pick up if local stock exists
- LaskaKit cart: preferred components are currently available
- StepperOnline motor five-pack: current listing/warehouse path exists
- DigiKey HDR + Omron: high stock, expected price band intact

### Needs one checkout fact before definitive buy call
- Tradera 608: combined freight for two 8-packs
- Allegro 16T: Sweden-delivered total
- StepperOnline: Germany→Sweden freight
- LaskaKit: Sweden GLS final checkout total/2-core cable variant

## Recommendation

Do not spend another pass comparing alternative components.

The practical next move is to enter the carts in this order:
1. Tradera 2×8 608 and confirm whether total is <=200 SEK
2. Allegro 3×16T and record Sweden-delivered total
3. LaskaKit exact cart, preserving 5 m belt while stock is available
4. StepperOnline Germany motor cart
5. DigiKey HDR + 10 Omron

If the first two marketplace checkouts exceed their thresholds, switch only the seller — not the locked specification.