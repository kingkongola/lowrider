---
research_date: 2026-08-29
scope: remaining orphan mechanical items: 3× GT2 16T 5mm/10mm pulleys and 14× 608-2RS bearings
status: recommendation-ready
decision_state: do not distort larger carts to absorb these cheap items; buy 16T from a verified low-cost EU/Choice source and 608 as a separate 20-pack with low/free shipping; exact final sellers remain checkout-dependent
price_basis: observed prices 2026-08-29; international shipping/variant selection must be verified before order
region: Sweden / EU / low-value marketplace fallback
sources_checked:
  - Allegro exact 16T pulley listing
  - Allegro EU/Sweden international shipping documentation
  - AliExpress indexed current 10mm-width pulley packs
  - Allegro 608-2RS commodity/premium references
  - previous Swedish 608 research
supersedes: assumption that 16T and 608 must necessarily share one seller
---

# 16T pulleys + 608 bearings: orphan-item strategy

## Why these should not drive the whole order graph

After the LaskaKit cart is resolved, two cheap mechanical families remain:
- 3 × GT2 drive pulley
- 14 × 608-2RS bearings

Both are commodity items. Forcing another otherwise-worse cart merely to consolidate them can easily cost more than one small shipment.

The objective is now:
- exact variant
- low delivered cost
- no counterfeit/geometry surprises

not absolute minimum parcel count.

## 1. Exact 16T requirement

Locked LR4 spec:
- **16 teeth**
- GT2 / 2 mm pitch
- for **10 mm belt**
- **5 mm bore**
- aluminium
- 3 required
- two radial set screws preferred

## Allegro exact candidate — strongest fully specified current listing

Offer/product:
- manufacturer code `GT2-16T-5B_10mm_K`
- 16T
- 10 mm belt
- 5 mm bore
- tread width 11 mm
- aluminium
- **2 set screws included**
- observed price **7.20 PLN each**
- listing showed 18 pcs available
- seller `NsCNC`, business/Super Seller, 99.8% shown

Need 3:
- **21.60 PLN in parts**

Source:
- https://allegro.pl/oferta/napedowe-kolo-zebate-gt2-na-pasek-10mm-walek-5mm-16t-cnc-druk-3d-18355347606

### Sweden shipping caveat

Allegro officially supports DHL/DPD international shipping from Poland to Sweden **when the seller enables that method**.

Current Allegro help lists maximum seller-set Sweden prices around:
- DHL Sweden: up to **53.99 PLN**
- DPD Sweden: up to **56.99 PLN**

These are platform maxima, not proof that this exact NsCNC offer ships to Sweden or what checkout will charge.

Sources:
- https://help.allegro.com/en/sell/c/dhl-international-delivery-options
- https://help.allegro.com/en/sell/a/allegro-dpd-courier-international-shipping-from-poland-to-the-european-union-LR80YA872fw

**Buy condition:** use Allegro only if Sweden can actually be selected on this exact seller/order and delivered total stays sensible.

## AliExpress / Choice fallback — potentially even cheaper

Fresh indexed listing, product ID `1005012977561121`:
- 5 pcs aluminium GT2 pulleys
- selectable 16T / 20T
- selectable 5 / 6.35 / 8 mm bore
- title explicitly includes fit for **10 mm belt width**
- observed headline around **US$6.62 / 5 pcs** before variant-specific price/shipping

Source reference:
- https://www.pricearchive.org/aliexpress.com/item/1005012977561121

This is economically attractive because buying 5 gives two useful spares.

But marketplace variant risk is high. **Do not order from the headline alone.** Checkout variant must visibly resolve to:
- 16T
- 5 mm bore
- 10 mm belt width
- quantity 5

Also verify Swedish VAT/Choice shipping in checkout.

A second current 2-piece listing exists under product ID `1005006189009543`, also advertising 16/20T, multiple bores and GT2-10 mm compatibility, but again exact variant pricing must be checked.

## Previous EU shop candidates remain valid

Known exact alternatives:
- Hellas Digital `070.0051`: ~€1.61 each
- Anodas `AN-18925`: ~€3 each

The issue is not part price but standalone shipping.

Therefore use them only if another purchase from those sellers appears.

## 2. 608-2RS requirement

Locked spec:
- 608-2RS
- **8×22×7 mm**
- rubber seals both sides
- 14 required

Preferred procurement quantity:
- **20 pcs**, leaving 6 spares

Target delivered cost from prior research:
- roughly **<=180 SEK**

## Allegro proves bearings themselves are extremely cheap

Current examples:
- generic/MW `608 2RS`, exact 8×22×7: **2.00 PLN each**, 4.93/5 across 183 ratings on the indexed offer
- TCT 608 2RS exact 8×22×7: around **1.10 PLN each** in another indexed offer
- ZVL 608 2RSR: around 5 PLN each
- NSK premium 608 2RS: around 9.85 PLN each

Sources:
- https://allegro.pl/oferta/lozysko-kulkowe-zwykle-mw-608-2rs-8x22x7mm-17809698450
- https://allegro.pl/oferta/608-2rs-lozysko-kulkowe-8x22x7-mm-608-2rsr-608-rs-tct-5665261914
- https://allegro.pl/oferta/lozysko-kulkowe-608-2rsr-zvl-8x22x7-2rs-rs-gumki-8413722125

At 2 PLN each, even 20 bearings are only 40 PLN in parts. Shipping dominates.

## Do not buy premium NSK/SKF for LR4 guide bearings

The bearings are simple rolling guide elements in this machine. V1E specifies 608-2RS, not precision-brand bearings.

A premium NSK example at ~9.85 PLN each would make 14 bearings ~138 PLN before shipping — several times the commodity cost with no meaningful LR4 payoff.

## Can Allegro combine pulleys + bearings?

No same-seller 608 listing from `NsCNC` was verified in this research pass.

Therefore do not assume Allegro can consolidate these items. If checkout/seller catalogue later reveals exact 608-2RS from NsCNC at sensible cost, great; otherwise keep bearings separate.

## Amazon Prime role

Amazon remains a good likely channel for the **20-pack 608-2RS**, because free Prime delivery can beat extremely low overseas item price plus international freight.

However, no current Amazon.se ASIN was verified end-to-end in this pass. Do not record an unverified Amazon variant as approved.

## Decision tree

### 16T pulleys
1. Check exact Allegro `GT2-16T-5B_10mm_K` Sweden checkout.
2. Compare delivered total against a verified AliExpress Choice 5-pack with exact 16T/5mm/10mm variant.
3. If both shipping routes are poor, use Hellas/Anodas only when another order can share freight.

### 608 bearings
1. Look for a verified Amazon Prime 20-pack exact `608-2RS 8×22×7` around <=180 SEK delivered.
2. Otherwise use a low-cost EU/Allegro commodity seller if Sweden delivery keeps total below target.
3. Do not pay SKF/NSK premium.

## Current conclusion

**These items are intentionally allowed to remain separate orphans.**

A 50–150 SEK shipping difference here is smaller than the risk/cost of contaminating the already-good LaskaKit cart with wrong variants or premium parts.
