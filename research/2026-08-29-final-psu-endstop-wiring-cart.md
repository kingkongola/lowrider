---
research_date: 2026-08-29
scope: final procurement strategy for LR4 24 V PSU, exact endstops and low-voltage/endstop wiring
status: recommendation-ready
decision_state: buy Mean Well HDR-60-24 plus 10 exact Omron SS-3GL13PT from DigiKey; add endstop and short 24 V cable to the existing LaskaKit order; solder endstops COM+NC; do not create a separate cable order
price_basis: fresh web prices and stock observed 2026-08-29; final tax/shipping/variant totals must be rechecked at checkout
region: Sweden / EU
sources_checked:
  - V1 Engineering Jackpot3 documentation
  - V1 Engineering LowRider/endstop documentation and current forum reports
  - DigiKey Sweden exact HDR-60-24 and SS-3GL13PT listings and Swedish freight policy
  - LaskaKit UL2464 cable and DuPont connector listings
  - StepperOnline warehouse/product pages
supersedes: research/2026-08-29-electronics-cart-ss3gl13pt.md
---

# Final PSU + endstop + wiring cart

## Decision summary

The cleanest current order graph is **two already-needed carts**, not a new third electronics/cable seller:

1. **DigiKey:** Mean Well `HDR-60-24` + 10 × exact Omron `SS-3GL13PT`.
2. **Existing LaskaKit mechanical order:** add endstop cable, a short heavier 24 V cable and board-side connector parts/pigtails.

StepperOnline remains **motors only**. Its `HDR-60-24` listing does not currently provide a useful Germany-warehouse consolidation path; do not move the PSU there simply to share freight.

## 1. PSU — lock Mean Well HDR-60-24

Chosen PSU:
- manufacturer: Mean Well
- model: **`HDR-60-24`**
- output: **24 VDC / 2.5 A / 60 W**
- DIN-rail form factor
- universal 85–264 VAC input
- 4 kV isolation
- 90 % efficiency listed
- no minimum load

Current DigiKey:
- DigiKey part: **`1866-2249-ND`**
- ordinary DigiKey inventory: thousands in stock
- observed price approximately **194.20 SEK ex VAT / 242.75 SEK incl VAT** on the fresh English Swedish-market listing; another recent localized crawl showed a few SEK lower, so checkout is authoritative.

Source:
- https://www.digikey.se/en/products/detail/mean-well-usa-inc/HDR-60-24/7703804

### Why HDR beats the previous candidates here

Compared with `LRS-100-24`:
- correct 60 W class rather than unnecessary 100+ W
- DIN-rail enclosure/touch-protected terminal layout is easier to integrate safely
- avoids an exposed open-frame mains PSU inside the machine

Compared with `GST60A24-P1J` external brick:
- substantially cheaper in current Swedish sourcing
- the machine is already heading toward a proper NVR/control enclosure, so DIN rail is not an architectural burden
- no barrel-plug handling is needed

This supersedes the earlier provisional preference for the GST brick.

## 2. Endstops — exact Omron SS-3GL13PT

V1 Engineering's own endstop product identifies:
- Omron **`SS-3GL13PT`**
- SPDT simulated-roller lever
- 3 A at 125 VAC / 3 A at 30 VDC
- small quick-connect tabs; soldering is explicitly acceptable

V1's Jackpot3 documentation uses **Normally Closed (NC)** endstop wiring.

Sources:
- https://www.v1e.com/products/limit-switch-endstop
- https://docs.v1e.com/electronics/jackpot3/

Current DigiKey exact listing:
- DigiKey part: **`SW768-ND`**
- tens of thousands in stock
- qty 1: **8.04 SEK ex VAT / 10.05 SEK incl VAT**
- qty 10: **6.618 SEK ex VAT each**, approximately **82.73 SEK incl VAT for 10**

Source:
- https://www.digikey.se/en/products/detail/omron-electronics-inc-emc-div/SS-3GL13PT/664729

### Buy 10 even though the machine needs 5

LR4 requires five installed endstops.

Buying 5 at the qty-1 price:
- ~50.25 SEK incl VAT

Buying 10 at the qty-10 price:
- ~82.73 SEK incl VAT

Five useful spares therefore add only about **32.48 SEK**.

This is not threshold-filler buying. Current V1 forum reports explicitly describe bent/detached lever arms during the learning/build phase, so five spares for ~32 SEK are a sensible low-cost reliability stock.

Source:
- https://forum.v1e.com/t/endstop-where-to-order/52822

## 3. DigiKey cart economics

Current Swedish freight rule:
- free shipping at **615 SEK or more**
- **170 SEK** shipping below 615 SEK
- Marketplace goods do not count toward ordinary free-shipping calculation

Source:
- https://www.digikey.se/sv/help-support/delivery-information/delivery-time-and-cost

Recommended base cart, conservative current prices:
- 1 × HDR-60-24: ~242.75 SEK incl VAT
- 10 × SS-3GL13PT: ~82.73 SEK incl VAT
- merchandise: **~325.48 SEK**
- freight: **170 SEK**
- estimated delivered: **~495.48 SEK**

Using only five endstops would be roughly ~463 SEK delivered, so the extra five exact spares cost only ~32.5 SEK in the final cart.

### Free-shipping threshold rule

Do **not** buy random filler to reach 615 SEK.

At checkout, however, it is rational to test one scenario:
- if adding cable/components we genuinely need makes the cart cross 615 SEK for less than the 170 SEK freight being removed, compare the final total
- otherwise leave those cheap items in the already-planned LaskaKit order

Default remains the LaskaKit cable route below because its marginal shipping cost is effectively zero.

## 4. Endstop cable — add to LaskaKit order

LaskaKit `LA150151A`:
- UL2464 / LIYY
- **26 AWG, 3 × 0.14 mm²**
- unshielded
- flexible copper multicore
- current price from about **€0.58/m**
- hundreds of metres shown in stock

Source:
- https://www.laskakit.cz/en/connecting-cables/

Use only two of the three conductors for each endstop; the third is simply unused/spare.

### Quantity

V1's own LowRider endstop kit uses:
- 5 × 1200 mm = **6 m total**

Source:
- https://www.v1e.com/products/endstop-plug

Buy **10 m** rather than exactly 6 m:
- approximate material cost **€5.80**
- gives routing/service-loop margin
- leaves useful spare signal cable
- adds essentially no new shipping because LaskaKit is already an intended mechanical order

26 AWG is electrically more than adequate for NC endstop signal current. The important requirements here are flexible stranded copper, reliable termination and strain relief.

## 5. Board-side connectors

Jackpot3 exposes 2.54 mm header connections for endstops. Two practical LaskaKit routes exist.

### If a suitable DuPont crimper is already available

Add:
- 2-pin 2.54 mm DuPont housings from LaskaKit's `LA217000...` family
- female crimp sockets **`LA217002`**, currently ~€0.03 each

Source:
- https://www.laskakit.cz/en/connectors/

Suggested quantity:
- 10 × 2-pin housings
- 20 × female sockets

The spare count costs cents and makes rework painless.

Do not record a specific 2-pin housing suffix until the checkout dropdown visibly confirms the two-position variant; the family code alone is not enough evidence for the suffix mapping.

### If no DuPont crimper is already available

Do **not** buy a dedicated crimp tool just for five plugs.

LaskaKit `LA150090`:
- 40 × pre-crimped 2-pin female-to-female leads
- 70 cm
- current observed ~**€6.10–6.12**
- in stock

Source:
- https://www.laskakit.cz/en/propojovaci-kabely-f-f-40ks-2pin-samice-samice--70cm/

Cut five pigtails short and solder/splice them to the long `LA150151A` runs. This is mechanically simple and still cheaper than buying a special precision crimper solely for the CNC.

## 6. Switch-side termination — solder COM + NC

Default:
- solder one conductor to **COM**
- solder one conductor to **NC**
- heatshrink each terminal
- add cable strain relief so repeated motion cannot flex the solder joint

Do not buy 2.8 mm / 0.110-inch spade terminals unless detachable switch ends are specifically desired.

Reasons:
- V1 explicitly allows soldering
- common automotive mini-spades are often sized for larger conductor cross-sections than our endstop cable
- solder + heatshrink avoids another variant/crimp-quality failure mode

V1's official plug kit also illustrates that the LowRider uses five 1200 mm two-wire runs and that the small switch-end terminal must be matched carefully.

Source:
- https://www.v1e.com/products/endstop-plug

## 7. Short 24 V PSU -> Jackpot3 cable

Do **not** use the 26 AWG endstop cable for the PSU output.

LaskaKit also sells UL2464 20 AWG / 0.52 mm² flexible tinned-copper multicore cable:
- family `LA150187A` ... `LA150187D`
- selectable **2-core** version exists
- 2-core OD ~4.8 mm
- current price from about **€0.99–1.00/m**
- current stock shown

Source:
- https://www.laskakit.cz/en/ul2464-20awg-liyy-0-52-mm2-nestineny-vicezilovy-kabel--cerny/

Add **1 m of the explicitly selected 2-core variant** at checkout.

The page exposes several suffixes but does not reliably map suffix→core-count in the indexed HTML, so do not guess the suffix. Select `2 cores` visibly in the product UI before adding.

This cable is only the low-voltage 24 V output from HDR-60-24 to Jackpot3. Mains-side wiring belongs to the separate NVR/control-enclosure design and is not specified by this file.

## 8. Stepper motor cables remain unchanged

Selected StepperOnline motors already have 1 m factory leads and 2.54 mm female connectors.

Do not buy the standard three V1 stepper extensions yet. Dry-fit the compact 650×1250 machine first, then extend only the runs that cannot retain a relaxed service loop at full travel.

The StepperOnline order stays motors-only; adding a China-only PSU listing to a Germany motor shipment would be false consolidation.

## Checkout-ready order graph

### DigiKey
- 1 × Mean Well `HDR-60-24` / `1866-2249-ND`
- 10 × Omron `SS-3GL13PT` / `SW768-ND`
- target current delivered total: **~495 SEK**

### Existing LaskaKit order — additions
- 10 m × `LA150151A`, 26 AWG 3-core endstop cable: ~€5.80
- 1 m × `LA150187...`, **select 2-core**, 20 AWG PSU-output cable: ~€1
- board connectors:
  - if crimper exists: 2-pin housings + `LA217002` sockets, roughly <€1 total
  - if no crimper: `LA150090` pre-crimped 2-pin F/F set, ~€6.1

No separate cable shipment is needed.

## Locked decisions

- PSU: **Mean Well HDR-60-24**
- endstop: **Omron SS-3GL13PT**
- installed endstops: 5
- procurement quantity: **10**
- wiring mode: **NC, COM + NC**
- switch termination: **solder + heatshrink** by default
- endstop cable: **10 m LaskaKit LA150151A**
- PSU-output cable: ~1 m LaskaKit UL2464 **20 AWG 2-core** selected in dropdown
- no stepper extensions until dry-fit

## Remaining uncertainty before placing orders

Only checkout details remain:
1. confirm current DigiKey HDR price and 170 SEK freight
2. briefly test whether adding genuinely needed items can cross 615 SEK more cheaply than paying freight; reject filler buying
3. choose 2-core version of LaskaKit 20 AWG cable visibly in dropdown
4. decide board-end connector route based on whether a suitable DuPont crimper is already owned

No further alternative-PSU or alternative-endstop research is justified unless these exact products materially change price/stock.