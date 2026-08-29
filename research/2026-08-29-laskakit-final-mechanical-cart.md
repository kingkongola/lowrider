---
research_date: 2026-08-29
scope: final LaskaKit cart after locking 650×1250 LR4 geometry, including mechanical parts and low-voltage wiring additions
status: recommendation-ready
decision_state: LaskaKit is the recommended cart for 6 smooth idlers + T8 Z drive + couplers + GT2 belt plus endstop/24V low-voltage cable; use 5 m belt if checkout confirms stock, otherwise 3×2 m
price_basis: fresh indexed prices/stock observed 2026-08-29; checkout is authoritative for belt variant, 20AWG core-count variant and shipping
region: Sweden / EU
sources_checked:
  - LaskaKit exact mechanical product pages
  - LaskaKit current cable and DuPont connector catalogue
  - LaskaKit Sweden shipping table
  - locked LR4 geometry and final electronics/wiring research
supersedes: cart-level conclusions in 2026-08-29-gt2-drive.md and 2026-08-29-t8-z-drive.md
---

# Final LaskaKit cart

## Geometry

Locked belt segments for the 650×1250 machine:
- X: **999 mm**
- Y: **1705 mm ×2**
- total: **4409 mm**

Source: `research/2026-08-29-geometry-650x1250.md`.

Therefore either one 5 m roll or three independent 2 m rolls are mechanically valid.

## Mechanical lines

### 1. Smooth idlers — 6 pcs

LaskaKit / POWGE `LA190008E`:
- smooth GT2 idler
- 5 mm bore
- for 10 mm belt
- ~€1.87 each
- need 6: **~€11.22**

Source:
- https://www.laskakit.cz/en/powge--kladka-gt2--hladka--s-loziskem-5-mm--pro-remen-10mm/

Do not substitute nearby 6 mm-belt variants.

### 2. T8×8 rod — 1 pc

`LA190032A`:
- T8×8
- 400 mm
- 4-start / 8 mm lead
- stainless 304
- ~€8.19

Cut near centre for two ~199 mm Z screws.

Source:
- https://www.laskakit.cz/en/trapezova-tyc-t8x8-400mm/

### 3. T8×8 brass nuts — 2 pcs

`LA190033A`:
- brass
- T8×8 / 4-start
- ~€1.32 each
- **~€2.64** total

Source:
- https://www.laskakit.cz/en/matice-pro-trapezovou-tyc-t8x8--mosaz/

Do not buy `LA190033B`; that is T8×2.

### 4. Flexible couplers — 2 pcs

`LA190031`:
- 5 mm -> 8 mm
- aluminium
- 19 mm OD × 25 mm long
- ~€1.83 each
- **~€3.66** total

Source:
- https://www.laskakit.cz/en/pruzna-spojka-hlinikova-sviraci-5x8mm/

### 5A. Preferred GT2 belt — 1×5 m

`LA190013C`:
- GT2
- 10 mm wide
- fiberglass reinforced
- ~€7.81

Source:
- https://www.laskakit.cz/en/remen-gt2-5m-se-skelnym-vlaknem-10mm/

Stock indexing has conflicted between an older unavailable page and a fresher in-stock category page. Verify at checkout.

### 5B. Fallback belt — 3×2 m

`LA190013B`:
- GT2
- 10 mm
- fiberglass
- ~€4.90 each
- need 3: **~€14.70**

One 2 m roll per 999 / 1705 / 1705 mm segment.

Source:
- https://www.laskakit.cz/en/3d-printing-cnc-machines/page-2/

## Low-voltage wiring additions

These additions eliminate a separate cable order.

### 6. Endstop cable — 10 m

`LA150151A`:
- UL2464 / LIYY
- 26 AWG
- 3 × 0.14 mm²
- unshielded flexible copper multicore
- current ~€0.58/m

Buy **10 m: ~€5.80**.

Only two cores are used for the NC endstop circuit; third core remains spare.

Source:
- https://www.laskakit.cz/en/connecting-cables/

### 7. HDR-60-24 -> Jackpot3 cable — 1 m

LaskaKit UL2464 20 AWG / 0.52 mm² multicore family `LA150187A...D`:
- stranded tinned copper
- unshielded
- selectable core count including 2-core
- current price from ~€0.99–1.00/m

Buy **1 m, select 2 cores visibly in the product UI**.

The indexed HTML does not prove which suffix maps to 2-core, so do not guess the suffix.

Source:
- https://www.laskakit.cz/en/ul2464-20awg-liyy-0-52-mm2-nestineny-vicezilovy-kabel--cerny/

### 8A. Endstop board connectors if a DuPont crimper is already owned

LaskaKit:
- 2.54 mm DuPont housing family `LA217000...`, from ~€0.03
- female crimp socket `LA217002`, ~€0.03

Suggested:
- 10 × 2-position housings
- 20 × `LA217002` sockets

Select 2-position housing in checkout; suffix mapping is not locked from indexed data.

Source:
- https://www.laskakit.cz/en/connectors/

### 8B. If no DuPont crimper is owned

Use `LA150090` instead:
- 40 × pre-crimped 2-pin F/F leads
- 70 cm
- ~€6.10–6.12
- current stock available

Cut five short pigtails and splice/solder to the long endstop cable.

Source:
- https://www.laskakit.cz/en/propojovaci-kabely-f-f-40ks-2pin-samice-samice--70cm/

## Shipping to Sweden

Previously verified LaskaKit table:
- GLS Sweden **€8.93**

Source:
- https://www.laskakit.cz/en/shipping-and-payment/

Because this shipment is already required for the mechanical parts, the wiring's **marginal freight is effectively zero** unless checkout changes the shipping class/price.

## Cart totals

### Mechanical baseline with 5 m belt

- parts: ~€33.52
- shipping: €8.93
- delivered baseline: **~€42.45**

### Add wiring with existing DuPont crimper

Add approximately:
- 10 m endstop cable: €5.80
- 1 m 20 AWG 2-core: ~€1.00
- housings/contacts: roughly <€1

Expected total becomes roughly **€49–50 delivered**, subject to checkout.

### Add wiring without DuPont crimper

Use `LA150090` (~€6.1) instead of loose housings/contacts.

Expected total becomes roughly **€55 delivered** with the preferred 5 m belt.

### Belt fallback effect

If 5 m belt is unavailable, add approximately **€6.89** to either total by using 3×2 m rolls.

## Deliberately not added

- exact Omron endstops: buy from DigiKey, not substitute LaskaKit switches
- 16T drive pulleys: nearby verified LaskaKit options are wrong width; keep separate orphan source
- 608 bearings: commodity 20-pack remains separate
- touch probe: optional
- energy chain: not required
- stepper extensions: dry-fit factory 1 m motor leads first

## Purchase status

**Recommendation-ready, not placed.**

Checkout sequence:
1. add `LA190008E` ×6
2. add `LA190032A` ×1
3. add `LA190033A` ×2
4. add `LA190031` ×2
5. try `LA190013C` ×1; fallback to `LA190013B` ×3 if unavailable
6. add `LA150151A` ×10 m
7. add 1 m of the UL2464 20 AWG family with **2-core variant explicitly selected**
8. choose board connector route based on whether a suitable DuPont crimper is already owned
9. verify GLS Sweden and final total

This is now both the mechanical cart and the low-voltage wiring cart.