---
research_date: 2026-08-29
last_updated_at: 2026-08-29
scope: Jackpot3 controller sourcing for Sweden, exact Elecrow SKU, current stock, firmware state, and import economics
status: recommendation-ready
confidence: high-on-product-medium-on-final-delivered-total
decision_state: Jackpot3 remains the controller choice; buy from Elecrow direct unless final Sweden checkout/import route is unexpectedly poor; do not downgrade to Jackpot2 because future laser/PWM is a real planned use
price_basis: official Elecrow/V1E pages observed 2026-08-29; Elecrow shipping is checkout-only and their published terms place tax/import responsibility on buyer
region: Sweden / China-direct vs US
observed_price:
  Elecrow_USD: 76.99
  V1E_USD: 75.99
  approximate_Elecrow_SEK_at_2026_08_29_reference_fx_before_shipping_import: 737.44
sources_checked:
  - Elecrow exact Jackpot3 product page
  - Elecrow V1 Engineering storefront
  - Elecrow shipping/import terms
  - V1 Engineering Jackpot3 product page and documentation
  - V1 Engineering Jackpot2 product/docs
  - V1 Engineering forum European Elecrow reports
  - Tullverket Sweden current low-value import/VAT rules effective 2026-07-01
supersedes: previous checkout-unknown Jackpot3 note while preserving Elecrow as preferred supplier
---

# Jackpot3 — Sweden purchase plan

## Decision

**Controller stays Jackpot3.**

Preferred source:
- **Elecrow direct**

Exact Elecrow identity:
- product: Jackpot3 CNC Controller
- SKU: **`CQA240812C2`**
- observed price: **$76.99**
- availability: **in stock**
- listed product weight: **300 g**

Official page:
- https://www.elecrow.com/jackpot3-cnc-controller.html

Elecrow current V1 Engineering storefront contains only three V1 items and Jackpot3 is the only current controller product shown in stock, so there is no useful V1-specific filler to add merely to amortize freight.

Source:
- https://www.elecrow.com/store/V1EngineeringInc

## What is included

Elecrow exact page states:
- 1 × Jackpot3 board
- 5 × two-wire terminal plugs
- 6 × self-adhesive heat sinks
- six integrated TMC2226 stepper drivers
- integrated ESP32

No separate drivers or ESP32 should be bought.

Jackpot3 hardware also provides:
- 7 inputs
- 4 selectable 5 V / line-voltage outputs
- **full PWM on the 5 V output mode**
- USB-C
- RJ11 expansion/pendant socket
- MicroSD
- FluidNC / GRBL-compatible control

Sources:
- https://www.elecrow.com/jackpot3-cnc-controller.html
- https://docs.v1e.com/electronics/jackpot3/

## Elecrow board must be flashed

This is now explicit rather than inferred.

Elecrow's current Jackpot3 page says:
- **“You will need to flash them”**

V1E US store, by contrast, states its board is pre-flashed/programmed for LowRider V4.

So the Elecrow saving comes with a small setup step:
1. connect with a data-capable USB-C cable
2. install the V1E-tested FluidNC version using current docs
3. upload LowRider V4 `config.yaml` and associated V1 config/macros
4. verify board operation before connecting the full machine

This is not a reason to pay transatlantic V1E shipping; it is a normal documented setup task.

Sources:
- https://www.elecrow.com/jackpot3-cnc-controller.html
- https://www.v1e.com/products/jackpot3-cnc-controller
- https://docs.v1e.com/electronics/jackpot3/

## Why not Jackpot2 to save $22 headline price?

Current V1E Jackpot2:
- headline sale price **$55**
- 6 integrated TMC2226 drivers
- but V1E explicitly states **NO PWM** on its outputs because of a design mistake
- the product page says it is not intended as the normal newbie/default controller

Sources:
- https://www.v1e.com/products/the-jackpot2-cnc-controller
- https://docs.v1e.com/electronics/jackpot2/

For this project, laser is intentionally deferred to 2027 rather than abandoned. Jackpot3's full 5 V PWM output therefore prevents a future controller workaround/replacement.

The ~$22 raw board saving is not compelling because:
- Jackpot2 is US-store sourced rather than the direct Elecrow international route found for Jackpot3
- international freight/import can erase much of the headline difference
- missing PWM is a real future limitation for our planned use

**Keep Jackpot3.**

## V1E US store comparison

V1E current price:
- **$75.99**
- essentially identical board headline price
- pre-flashed for LR4

V1E itself directs international buyers to Elecrow for more direct/lower shipping.

Source:
- https://www.v1e.com/products/jackpot3-cnc-controller

Therefore US store is fallback only if Elecrow checkout behaves badly.

## Sweden import treatment — important after 1 July 2026

Elecrow's current terms say:
- taxes/import duties are **not included in shipping cost**
- buyer is responsible for import taxes/duties

Sources:
- https://www.elecrow.com/shippinginfo
- https://www.elecrow.com/terms-and-condition

Tullverket current rules for online purchases shipped from outside the EU:
- Swedish VAT is always due; normally **25 %** for this type of product
- for goods worth €150 or less, from **1 July 2026** there is also a temporary **€3 customs charge per goods line/item**
- VAT is calculated on product value + freight + customs charge
- carrier declaration/administration fee may also be added
- if a seller uses IOSS, VAT can be collected at checkout instead, but the current Elecrow public policy does not provide evidence sufficient to assume IOSS for this order

Sources:
- https://www.tullverket.se/privat/panatet/handlapanatet/tullverketsguidefornathandelutanforeu/vadaravgiftenpaminvara.4.153f8c8c16ffad23c221cb2.html
- https://www.tullverket.se/privat/panatet/handlapanatet/tullraknarenvadaravgiftenpaminvara/omtullarochavgifternarduhandlarpanatet/nytullavgiftfranden1juli2026.4.5dd2f9d519e1cbdf1a071f.html

### Consequence

Do **not** budget Jackpot as merely $76.99 ≈ 737 SEK.

Even before Elecrow freight and carrier handling, Swedish VAT + the new low-value customs charge push the real landed cost materially above the headline board price.

The exact final number cannot be honestly fixed until Elecrow checkout reveals:
- shipping method/cost
- whether Swedish VAT is collected at checkout
- whether an IOSS/tax line appears

## Why Elecrow still wins provisionally

Despite the import overhead:
- V1E US store has essentially the same board price and is also outside the EU
- V1E explicitly recommends Elecrow to international users to save on shipping
- current European user reports confirm successful Jackpot3 deliveries and responsive replacement handling

A March 2026 German user reported a damaged Jackpot3 from Elecrow; Elecrow supplied a return label and replacement from China quickly. That is useful evidence that the low-cost route is not necessarily unsupported.

Source:
- https://forum.v1e.com/t/mpcnc-primo-germany-cologne/53656

## Checkout rule

At actual Elecrow checkout record:
1. SKU remains `CQA240812C2`
2. board price remains about $76.99
3. destination = Sweden
4. shipping method + cost
5. whether VAT is collected
6. any tax/IOSS wording
7. delivery estimate

Then compare with V1E US checkout only if Elecrow freight/tax handling is unexpectedly bad.

Do not add unrelated Elecrow electronics merely to dilute shipping.

## Buy status

**Product and supplier are recommendation-ready. Final delivered total remains checkout-gated.**

No further controller-model research is justified unless:
- Elecrow goes out of stock
- Sweden checkout produces an unexpectedly high all-in price
- the 2027 laser requirement is intentionally dropped
