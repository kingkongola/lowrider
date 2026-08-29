---
research_date: 2026-08-29
scope: final LaskaKit mechanical cart after locking 650×1250 LR4 geometry
status: recommendation-ready
decision_state: LaskaKit is the recommended cart for 6 smooth idlers + complete T8 Z drive + couplers + GT2 belt; use 5 m belt if checkout confirms stock, otherwise 3×2 m segments
price_basis: fresh indexed prices/stock observed 2026-08-29; LaskaKit pages have one conflicting 5 m belt stock signal, so checkout must decide belt variant
region: Sweden / EU
sources_checked:
  - LaskaKit exact product pages
  - LaskaKit fresh CNC category pages
  - LaskaKit Sweden shipping table
  - locked LR4 geometry file
supersedes: cart-level conclusions in 2026-08-29-gt2-drive.md and 2026-08-29-t8-z-drive.md
---

# Final LaskaKit mechanical cart

## Geometry now removes the belt uncertainty

Locked machine calculations:
- X belt: **999 mm**
- Y belts: **1705 mm ×2**
- exact total: **4409 mm**

Source:
- `research/2026-08-29-geometry-650x1250.md`

This means either:
- **1×5 m continuous roll**, cut into the three required pieces, or
- **3×2 m rolls**, one per belt segment

Both are mechanically valid because LR4 uses three separate open belt sections; no individual belt needs to exceed 1705 mm.

## Recommended cart lines

### 1. Smooth idlers — 6 pcs

LaskaKit / POWGE `LA190008E`:
- smooth GT2 idler
- 5 mm bearing/bore
- for **10 mm belt**
- current observed price **€1.87 each**
- fresh indexed stock around **76–98 pcs** depending page crawl

Need 6:
- **~€11.22**

Source:
- https://www.laskakit.cz/en/powge--kladka-gt2--hladka--s-loziskem-5-mm--pro-remen-10mm/

Important: nearby `LA190008C` / other variants are for 6 mm belt. Do not substitute by code similarity.

## 2. T8 Z rod — 1 pc

LaskaKit `LA190032A`:
- T8×8
- 400 mm
- 4-start / 8 mm lead
- stainless 304
- fresh indexed price around **€8.15–8.19**
- fresh stock signal around **5–14 pcs** depending crawl

Need 1.

Cut once near centre to obtain roughly two ~199 mm Z screws after kerf, comfortably above V1E's 145 mm minimum.

Source:
- https://www.laskakit.cz/en/trapezova-tyc-t8x8-400mm/

## 3. T8×8 brass nuts — 2 pcs

LaskaKit `LA190033A`:
- brass
- T8×8
- 4-start
- current observed price **~€1.31–1.32 each**
- stock available in current indexed pages

Need 2:
- **~€2.64**

Source:
- https://www.laskakit.cz/en/matice-pro-trapezovou-tyc-t8x8--mosaz/

Do **not** buy `LA190033B`: that is T8×2 and wrong for LR4.

## 4. Flexible 5→8 mm couplers — 2 pcs

LaskaKit `LA190031`:
- aluminium 6061
- 5 mm → 8 mm
- 19 mm OD
- 25 mm long
- 4×M3 clamping screws
- current observed price **~€1.81–1.83 each**
- in stock

Need 2:
- **~€3.66**

Source:
- https://www.laskakit.cz/en/pruzna-spojka-hlinikova-sviraci-5x8mm/

## 5A. Preferred GT2 belt — 1×5 m

LaskaKit `LA190013C`:
- GT2
- 10 mm wide
- 5 m
- fiberglass reinforced
- current category price **~€7.81**

Source:
- https://www.laskakit.cz/en/remen-gt2-5m-se-skelnym-vlaknem-10mm/

### Stock warning

There is a live-index inconsistency:
- the older individual product crawl says **currently unavailable**
- a much fresher category crawl (2 days old) shows `LA190013C` **in stock, 18 pcs**, €7.81

Therefore treat stock as **checkout-verification required**, not as definitely available/unavailable.

## 5B. No-wait belt fallback — 3×2 m

LaskaKit `LA190013B`:
- GT2
- 10 mm
- 2 m
- fiberglass
- fresh category listing shows **in stock**
- current observed price around **€4.90 each**

Need 3 if the 5 m roll is unavailable:
- **~€14.70**

Source:
- https://www.laskakit.cz/en/3d-printing-cnc-machines/page-2/

Cut plan:
- roll 1 → 999 mm X belt; large spare remains
- roll 2 → 1705 mm Y belt
- roll 3 → 1705 mm Y belt

Cost penalty vs 5 m roll:
- about **€6.89** extra

That is roughly the price of eliminating belt-stock dependency and leaves ~1.59 m total spare belt.

## Shipping to Sweden

LaskaKit's published current table:
- **GLS Sweden: €8.93**

All international shipments dispatch from their Czech base.

Source:
- https://www.laskakit.cz/en/shipping-and-payment/

## Delivered-cart estimates

### Preferred cart with 5 m belt

Approx parts:
- 6 idlers: €11.22
- T8 rod: €8.19
- 2 nuts: €2.64
- 2 couplers: €3.66
- 5 m belt: €7.81

Parts subtotal: **~€33.52**

+ published Sweden GLS: €8.93

Estimated delivered: **~€42.45** before any checkout rounding/price changes.

### Fallback cart with 3×2 m belt

Replace €7.81 belt with ~€14.70:

Parts subtotal: **~€40.41**

+ €8.93 shipping

Estimated delivered: **~€49.34**.

## Items deliberately NOT added

### Endstops
LaskaKit has cheap switches, but not the exact V1E baseline Omron `SS-3GL13PT`. Do not compromise the actuator geometry just to fill this cart.

### 16T drive pulleys
LaskaKit's nearby 16T variants found are for 6 mm belt. Wrong. The LR4 requires 3×16T / 5 mm bore / **10 mm belt**.

### 608 bearings
No verified LaskaKit line gives enough cart advantage over a cheap commodity 20-pack elsewhere.

### Touch probe
LaskaKit sells a cheap touch probe (~€4), but it is optional and not necessary to commission the machine. Do not add optional parts merely because shipping is already paid.

### Energy chain
Not required by the current LR4 wiring/hose architecture.

## Purchase status

**Recommendation-ready, but not placed.**

At checkout:
1. add exact SKUs above
2. try `LA190013C` 5 m first
3. if unavailable, decide whether waiting is worthwhile; otherwise use 3× `LA190013B`
4. confirm GLS Sweden remains €8.93
5. confirm T8 rod remains in stock — this is the lowest-stock core item observed

This cart is now sufficiently resolved that further research is unlikely to save meaningful money unless another vendor happens to bundle the missing 16T pulleys as well.
