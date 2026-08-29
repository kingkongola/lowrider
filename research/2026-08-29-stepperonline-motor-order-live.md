---
research_date: 2026-08-29
scope: live purchase verification for the five LR4 stepper motors from StepperOnline Germany
status: recommendation-ready
decision_state: exact 5-pack remains the motor choice; Germany item price is verified; keep this order motors-only because suitable PSU consolidation is not available from the same Germany route
price_basis: fresh StepperOnline product pages crawled 2026-08-26 to 2026-08-29; final Germany-to-Sweden freight requires checkout
region: Sweden / Germany warehouse
sources_checked:
  - StepperOnline exact 5-pack product page
  - StepperOnline exact single-motor product page
  - StepperOnline warehouse policy/about page
  - StepperOnline S-250-24 and HDR-60-24 pages for consolidation sanity check
supersedes: price/stock assumptions in earlier motor research while preserving the same chosen model
---

# StepperOnline motor order — live verification

## Chosen item

StepperOnline bundle **`5-17HS19-2004S1`**:
- 5 × `17HS19-2004S1`
- NEMA17, 42×42×48 mm
- 59 Ncm / 83.55 oz-in
- 2.0 A/phase
- 1.8°
- 5 mm D shaft
- 24 mm shaft length
- 1 m cable
- 4-pin 2.54 mm female connector

Fresh product page:
- observed price **€38.13 / five-pack**
- observed stock around 200
- Germany selectable as ship-from
- shipment weight ~2.10 kg

Source:
- https://www.stepperonline.nl/5st-nema-17-bipolair-59ncm-83-55oz-in-2a-42x48mm-4-draden-met-1m-kabel-aansluiting-5-17hs19-2004s1

## Germany warehouse

Use the Germany warehouse for EU delivery/returns and to avoid China-import handling.

Source:
- https://www.stepperonline.nl/over-ons

Checkout must explicitly remain on Germany before the order is accepted.

## Five-pack beats five singles

Same exact single motor was around €8.34 each at qty 5:
- five singles ~€41.70
- five-pack €38.13
- bundle saves ~€3.57

Source:
- https://www.stepperonline.nl/nema-17-bipolair-59ncm-83-55oz-in-2a-42x48mm-4-draden-met-1m-kabel-aansluiting-17hs19-2004s1

## Sweden freight

Public product pages do not expose a reliable Sweden-specific total for this 2.10 kg Germany shipment.

Do not estimate it.

Checkout procedure:
1. Germany warehouse
2. destination Sweden
3. record shipping + VAT-inclusive final total
4. reject a checkout path that silently moves shipment to China

## PSU consolidation check — explicitly rejected

### Generic S-250-24

StepperOnline has a cheap 24 V / 10 A / 250 W `S-250-24` with Germany selectable, but it is not appropriate cart optimization:
- much more power than LR4/Jackpot3 needs
- open-frame mains terminals
- would require enclosure/safety work

Do not buy it merely to amortize motor freight.

### Mean Well HDR-60-24

A StepperOnline `HDR-60-24` listing was also checked because that is now our preferred PSU model.

The product route checked did **not** expose a useful Germany ship-from option; it effectively led to China rather than allowing the PSU to ride with the German motor pack.

Therefore do not assume that the very low StepperOnline headline price can be combined with the Germany motor shipment.

Current PSU plan is instead:
- Mean Well `HDR-60-24` from DigiKey together with exact Omron endstops

See:
- `research/2026-08-29-final-psu-endstop-wiring-cart.md`

## Final decision

StepperOnline order = **five motors only**, unless checkout later reveals another already-required exact part from the **same Germany warehouse**.

Ready to place once Germany→Sweden freight is visible and reasonable.

No more alternative-motor research is justified unless Germany stock disappears or delivered price rises materially.