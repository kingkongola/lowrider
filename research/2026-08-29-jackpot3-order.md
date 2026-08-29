---
research_date: 2026-08-29
scope: Jackpot3 controller sourcing for Sweden
status: recommendation-ready
decision_state: Elecrow remains preferred international source; exact Sweden checkout total must be verified before order
price_basis: observed web prices on 2026-08-29; shipping/tax must be re-checked in checkout
region: Sweden / China-direct vs US
sources_checked:
  - Elecrow V1 Engineering store
  - V1 Engineering product page and Jackpot3 documentation
  - V1 Engineering forum, European Elecrow reports
  - Elecrow shipping/tax policy
  - Swedish Customs / Tullverket
supersedes: null
---

# Research: Jackpot3 purchase / delivery economics

## Required controller

The selected controller remains **Jackpot3**.

Current V1E/Elecrow facts:
- 6 integrated TMC2226 drivers
- ESP32 / Wi-Fi
- 7 inputs
- four selectable 5 V / input-voltage outputs
- full PWM capability on 5 V outputs, useful for future laser
- 9–24 VDC input

Source:
- https://docs.v1e.com/electronics/jackpot3/

## Elecrow direct

Current V1 Engineering seller page on Elecrow:
- **Jackpot3 CNC controller: USD 76.99**
- in stock on current indexed seller page
- the V1 Engineering Elecrow store currently has only three products; the other two shown products are out of stock, so there is no obvious useful LR4 item to add merely for consolidation

Source:
- https://www.elecrow.com/store/V1EngineeringInc

### Important firmware difference

V1E's own US store states its Jackpot3 is **pre-flashed/programmed for LowRider V4** and includes:
- 1 × Jackpot3 board
- 5 × plugs
- 6 × heat sinks
- no USB cable

A December 2025 V1E forum report from a European Elecrow buyer states that **Elecrow boards were not flashed** and needed the normal V1E Jackpot3 installation procedure.

Therefore assume Elecrow unit may require flashing/config upload unless its current checkout/product description explicitly states otherwise.

This is not a hardware disadvantage; it is a setup step.

Sources:
- https://www.v1e.com/products/jackpot3-cnc-controller
- https://forum.v1e.com/t/setting-up-jackpot-3/52509

## Why Elecrow is still the preferred international route

V1E's own Jackpot3 page explicitly directs international users to Elecrow to save on shipping.

European community evidence is positive:
- December 2025 European user described Elecrow shipping as fast/easy
- March 2026 German buyer reported a damaged board, received a return label quickly, and replacement arrived from China two days later
- earlier European Jackpot direct-buy reports describe Elecrow as well packaged and economically much better than US shipping

Sources:
- https://www.v1e.com/products/jackpot3-cnc-controller
- https://forum.v1e.com/t/setting-up-jackpot-3/52509
- https://forum.v1e.com/t/mpcnc-primo-germany-cologne/53656

## Shipping cost cannot be fixed from public pages

Elecrow calculates shipping from:
- destination
- parcel weight
- selected shipping method

The partner-seller material says global shipping can start very low, but that is not a guaranteed Sweden price for this specific board.

**Do not record a guessed delivered price.** Exact Sweden shipping must be read from checkout immediately before ordering.

Source:
- https://www.elecrow.com/Elecrow_partner_seller_Sell_DIY_Eletronics_online

## Sweden tax / customs warning — important in 2026

Elecrow's published terms state that taxes and import duties are **not included in shipping cost** and the buyer is responsible for them unless checkout explicitly handles them.

Swedish Customs states that for goods sent from outside the EU:
- import VAT is always due; normally 25% for this type of goods
- from **1 July 2026**, goods valued at €150 or less also generally incur a **€3 customs charge per item** under the new low-value rule
- carrier administration/declaration charges can also occur
- if a seller uses IOSS, VAT can instead be collected at checkout

Therefore the true Elecrow cost is not merely `USD 76.99 + displayed freight` unless checkout explicitly shows Swedish VAT/IOSS treatment.

Sources:
- https://www.elecrow.com/shippinginfo
- https://www.elecrow.com/terms-and-condition
- https://www.tullverket.se/privat/panatet/handlapanatet/tullverketsguidefornathandelutanforeu/vadaravgiftenpaminvara.4.153f8c8c16ffad23c221cb2.html
- https://www.tullverket.se/privat/panatet/handlapanatet/tullraknarenvadaravgiftenpaminvara/omtullarochavgifternarduhandlarpanatet/nytullavgiftfranden1juli2026.4.5dd2f9d519e1cbdf1a071f.html

## US V1E store comparison

Current V1E store price:
- **USD 75.99**

The board price is effectively the same as Elecrow, but V1E itself says international buyers can save on shipping through Elecrow.

Historical European reports for direct US Jackpot purchases show shipping/processing/VAT dominating the purchase, so the US store should be treated as fallback rather than default for Sweden.

Source:
- https://www.v1e.com/products/jackpot3-cnc-controller

## Do we add anything else to Elecrow?

Current answer: **probably no**.

The V1 Engineering Elecrow storefront currently exposes:
- Jackpot3 — available
- custom V1 ESP32 — out of stock
- old Jackpot — out of stock

Jackpot3 already integrates its ESP32 and six drivers. We do not need extra stepper drivers or ESP32 modules.

Adding unrelated Elecrow electronics just to amortize freight violates the cart-optimization rule.

## Decision

**Preferred supplier: Elecrow direct**, subject to a final Sweden checkout check.

At checkout record:
1. board price
2. shipping method / cost
3. whether Swedish VAT is collected at checkout
4. whether any IOSS/tax line appears
5. delivery estimate

Then compare all-in expected cost to V1E US store only if Elecrow shipping/tax treatment is unexpectedly poor.

### Buy / no-buy threshold

No artificial SEK threshold is locked yet because the exact freight and VAT treatment are unknown. The board itself at USD 76.99 is the right price class; the decision should be based on **all-in Sweden cost**, not headline price.

## Setup note after arrival

Assume Elecrow board may need initial flashing:
- follow current Jackpot3 V1E docs
- load LowRider V4 config
- verify firmware/config before connecting full machine

Do not count a USB cable as included.