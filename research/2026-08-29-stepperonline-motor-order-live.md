---
research_date: 2026-08-29
scope: live purchase verification for the five LR4 stepper motors from StepperOnline Germany
status: recommendation-ready
decision_state: exact 5-pack remains the motor choice; Germany warehouse and item price are verified, but Sweden freight is only exposed at checkout and must not be invented
price_basis: fresh StepperOnline product pages crawled 2026-08-26 to 2026-08-29; final shipping/VAT total requires Sweden checkout
region: Sweden / Germany warehouse
sources_checked:
  - StepperOnline exact 5-pack product page
  - StepperOnline exact single-motor product page
  - StepperOnline warehouse policy/about page
  - StepperOnline Germany-stock PSU reference for consolidation sanity check
supersedes: price/stock assumptions in earlier motor research while preserving the same chosen model
---

# StepperOnline motor order — live verification

## Chosen item remains correct

StepperOnline bundle:
- shop model: **`5-17HS19-2004S1`**
- contains 5 × manufacturer motor `17HS19-2004S1`
- NEMA17, 42×42×48 mm
- 59 Ncm / 83.55 oz-in
- 2.0 A/phase
- 1.8°
- 5 mm D shaft
- 24 mm shaft length
- 1 m cable
- 4-pin 2.54 mm Harwin female connector

Fresh product page:
- observed price **€38.13 / 5-pack**
- observed stock **200** on the indexed page
- selectable ship-from locations include **Germany**
- gross listed shipment weight **2.10 kg**

Source:
- https://www.stepperonline.nl/5st-nema-17-bipolair-59ncm-83-55oz-in-2a-42x48mm-4-draden-met-1m-kabel-aansluiting-5-17hs19-2004s1

## Germany warehouse is the correct route

StepperOnline states that its Germany warehouse serves EU customers with local delivery/returns and avoids customs/VAT-import formalities associated with ordering from China.

Source:
- https://www.stepperonline.nl/over-ons

**Checkout rule:** explicitly select **Germany** before judging the total. Do not accidentally accept China because it happens to be the page default/first option.

## Five-pack vs five single motors

The same exact single motor is currently listed around:
- €8.75 each at qty 1
- €8.34 each at qty 5

Five singles at the qty-5 tier would be roughly:
- 5 × €8.34 = **€41.70**

The dedicated five-pack at €38.13 therefore saves about:
- **€3.57**

with no spec compromise.

Source:
- https://www.stepperonline.nl/nema-17-bipolair-59ncm-83-55oz-in-2a-42x48mm-4-draden-met-1m-kabel-aansluiting-17hs19-2004s1

So the bundle remains the rational SKU.

## Sweden shipping remains a checkout-only unknown

The public/indexed product and warehouse pages do **not** expose a reliable Sweden-specific freight price for this exact 2.10 kg Germany-warehouse bundle.

Therefore this file deliberately does not estimate freight.

Before order:
1. choose Germany warehouse
2. set destination Sweden
3. record shipping + VAT-inclusive final total
4. reject any checkout path that silently changes ship-from to China

## Should we add a PSU just to share the German shipment?

A fresh StepperOnline product page does show a generic `S-250-24`:
- 24 V
- 10 A / 250 W
- €18.96
- Germany is selectable

Source:
- https://www.stepperonline.nl/250w-24v-10a-115-230v-schakelende-voeding-stepper-motor-cnc-router-kits-s-250-24

But this is **not a reason to add it**:
- 250 W is unnecessary for Jackpot3/LR4
- it is an open-frame mains supply requiring enclosure
- our PSU research is prioritizing a cleaner/smaller safe 24 V supply
- adding an oversized PSU merely to amortize freight is false consolidation

So the StepperOnline order remains **motors only** unless checkout reveals a genuinely needed exact part from the same Germany warehouse.

## Buy threshold / decision

Motor specification and seller are effectively locked.

**Ready to order when Germany→Sweden checkout freight is known and reasonable.**

No further alternative-motor research is likely to be worth the time unless:
- this five-pack disappears from Germany stock, or
- delivered price rises materially.
