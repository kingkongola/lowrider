---
research_date: 2026-08-29
last_updated_at: 2026-08-29
scope: remaining orphan mechanical items: 3× GT2 16T 5mm/10mm pulleys and 14× 608-2RS bearings
status: recommendation-ready
decision_state: exact Allegro 16T listing is still live at 7.20 PLN each but Sweden freight remains checkout-gated; current Swedish Tradera seller has live exact 8-packs of 608-2RS at 79 SEK + 39 SEK shipping, making 2×8 a viable <=200 SEK route if samfrakt charges only one shipment; a 20-pack <=200 SEK remains preferred
price_basis: observed prices 2026-08-29; marketplace shipping and current listing state must be verified at checkout
region: Sweden / EU / marketplace fallback
sources_checked:
  - V1 Engineering current LR4 BOM
  - Allegro exact 16T pulley product and live offer
  - Allegro exact 608-2RS listings/search results
  - Allegro Sweden international shipping documentation
  - targeted Amazon.se exact-variant searches
  - current Tradera Motion_And_Rotaion 608-2RS listings
  - Fyndiq exact 20-pack reference
  - AliExpress indexed 10mm-width pulley packs
supersedes: earlier assumption that Amazon Prime would probably be the 608 winner
---

# Final orphan strategy: 16T pulleys + 608-2RS

These are intentionally cheap orphan items. Their low item value must not distort the already-good LaskaKit/DigiKey/StepperOnline carts.

## Live refresh — 2026-08-29

### 16T Allegro listing is still live

Exact product/listing remains visible:
- manufacturer/product code: `GT2-16T-5B_10mm_K`
- GT2 / 2 mm pitch
- **16T**
- **5 mm bore**
- **10 mm belt**
- 11 mm running width
- aluminium
- **2 locking grub screws**
- observed current price: **7.20 PLN each**
- recent sales visible on the product page

Need 3, so raw parts price is **21.60 PLN**.

Sources:
- https://allegro.pl/produkt/napedowe-kolo-zebate-gt2-na-pasek-10mm-walek-5mm-16t-cnc-druk-3d-ceec4f7d-f776-4e22-bf35-a76392e738d6
- https://allegro.pl/oferta/napedowe-kolo-zebate-gt2-na-pasek-10mm-walek-5mm-16t-cnc-druk-3d-18355347606

**Still unresolved:** the displayed delivery on Allegro is not a trustworthy Sweden-delivered quote. Final Sweden freight must be obtained in checkout. The existing buy threshold therefore stands: **buy 3 if total delivered is roughly <=150–180 SEK**.

A second exact Allegro offer (`17384423503`) is also currently indexed at **8.99 PLN each**, 16T / 5 mm / 10 mm / two set screws. It is a useful fallback if the preferred seller cannot ship to Sweden economically.

### 608 Swedish seller is currently live

Current Tradera business seller `Motion_And_Rotaion` has fresh exact listings for:
- `608-2RS`
- **8×22×7 mm**
- double rubber seal
- hardened/chrome steel
- set of **8 bearings**
- **79 SEK**
- **39 SEK Sweden shipping** shown on the listing
- samfrakt window: **3 days**

Current example:
- https://www.tradera.com/item/2510/747330721/608-2rs-skateboard-inline-skate-scooter-8-ball-bearings-blue-rubber-sealed

The listing was published 2026-08-27 and was still buy-now active when checked 2026-08-29.

Two 8-packs provide **16 bearings**, enough for 14 installed + 2 spare.

Potential total if the seller's samfrakt combines the two packs under one 39 SEK shipment:
- 2 × 79 + 39 = **197 SEK delivered**

That is inside the existing <=200 SEK threshold, but **197 SEK is conditional until the combined checkout visibly confirms one 39 SEK freight charge**. Do not assume samfrakt mathematics without checkout.

A 20-pack <=200 SEK delivered remains the preferred format because it gives 6 spares. Fresh targeted search did not reproduce a current 20-pack from this seller, so the live 2×8 route is now a legitimate fallback rather than waiting indefinitely for exactly 20.

## 1. 16T drive pulleys

### Locked LR4 requirement

V1E current BOM calls for:
- 3 × pulley
- GT2 / 2 mm pitch
- **16 teeth**
- **10 mm belt**
- **5 mm bore**

Source:
- https://docs.v1e.com/lowrider/

### Preferred exact part: Allegro `GT2-16T-5B_10mm_K`

Verified product:
- 16T
- 5 mm bore
- for 10 mm GT2 belt
- 11 mm tread width
- aluminium
- **2 set screws included**
- observed 2026-08-29 price **7.20 PLN each**

Need 3:
- parts = **21.60 PLN**

This remains the strongest exact-spec listing because the geometry is explicit rather than inferred from a variant title.

### Sweden shipping rule

Allegro can support international delivery when the seller/route enables it, but the exact seller/order freight to Sweden must be checked in checkout.

Do not accept an international freight charge that makes three tiny pulleys absurdly expensive.

**Buy rule:** if delivered total for 3 exact Allegro pulleys is roughly <=150–180 SEK, buy and stop optimizing.

### AliExpress / Choice fallback

Indexed 5-pack candidates exist with selectable:
- 16T
- 5 mm bore
- 10 mm belt width

Previously identified product ID: `1005012977561121`, headline around US$6.62 before variant-specific checkout.

Marketplace variant selection is the main risk. Checkout must visibly resolve to:
- 16T
- 5 mm bore
- 10 mm belt width
- qty 5

If exact variant + Swedish VAT/Choice shipping is around <=120–150 SEK delivered, it beats a badly-shipped Allegro order.

### EU-shop fallbacks

Still exact but useful only if freight can be shared:
- Hellas Digital `070.0051`, ~€1.61 each
- Anodas `AN-18925`, ~€3 each

Do not create a €15 shipment for €5 of pulleys.

## 2. 608-2RS bearings

### Locked requirement

- 608-2RS
- **8×22×7 mm**
- rubber seal both sides
- 14 installed
- preferred procurement quantity: **20**

V1E uses these as simple guide bearings. Premium SKF/NSK is not justified.

## Swedish Tradera route — current first choice to test

Current live exact 8-pack from `Motion_And_Rotaion`:
- 79 SEK / 8
- 39 SEK Sweden shipping shown
- 3-day samfrakt window
- exact 608-2RS / 8×22×7 / double rubber seal

**Checkout rule:** add two exact 8-packs. If combined checkout is **<=200 SEK delivered**, 16 bearings are sufficient and this is a good buy even though it yields only 2 spares.

If a current exact 20-pack from the same/another Swedish seller appears at **<=200 SEK delivered**, prefer the 20-pack.

Why the Swedish route is attractive:
- domestic shipping
- no variant/import ambiguity
- exact dimensions/seal spec
- total is already near our target band

## Allegro fallback for bearings

Current Allegro search results show exact generic 608-2RS / 8×22×7 in 10-packs around **9–10 PLN per 10-pack**. Two 10-packs are therefore cheap in parts, but international freight dominates.

Do not use displayed Polish domestic Smart/delivery prices as Sweden-delivered totals.

If a seller ships two exact 10-packs to Sweden cheaply enough to beat the confirmed Tradera checkout, Allegro wins. Otherwise domestic Tradera is simpler.

### Quality tier

Generic commodity 608-2RS is acceptable for LR4.

Named low/mid-cost brands are also fine if the delivered premium is tiny, but no benefit justifies paying several times more.

## Amazon Prime — no longer the assumed winner

Repeated targeted Amazon.se searches have not verified a current exact listing end-to-end as:
- sufficient quantity
- 608-2RS
- 8×22×7
- rubber seals both sides
- current Swedish delivered price around our threshold

Prime is welcome if an exact listing appears, but gets no priority merely because Prime exists.

## Rejected Swedish option

Fyndiq has an exact 20-pack around:
- 309 SEK
- +29 SEK freight

Correct spec, poor value.

Source:
- https://fyndiq.se/produkt/20-st-608-2rs-kullager-lagerstal-lager-8x22x7mm-d-256fc72ef6e24828/

## Checkout decision tree

### 16T
1. Put exact Allegro `GT2-16T-5B_10mm_K` ×3 in a Sweden checkout.
2. If delivered <=150–180 SEK: buy.
3. If seller/freight is bad, try exact second Allegro offer or exact AliExpress Choice 5-pack.
4. Choice wins only if 16T / 5 mm / 10 mm is visibly selected and <=120–150 SEK delivered.
5. Hellas/Anodas only if freight is shared with another real purchase.

### 608
1. Put **2× current Tradera 8-pack** in cart.
2. If samfrakt gives combined delivered **<=200 SEK**, buy 16 and stop optimizing.
3. Prefer a current exact 20-pack instead if one appears <=200 SEK delivered.
4. Otherwise price 2×10 exact packs on Allegro including actual Sweden delivery.
5. Amazon Prime only if an exact current quantity is actually verifiable around <=180–200 SEK delivered.
6. Reject ~338 SEK Fyndiq and premium SKF/NSK pricing.

## Final status

The specs and thresholds are locked. Fresh live checks confirm the preferred Allegro 16T part still exists and produce a currently actionable Swedish 608 route.

Remaining work is **checkout**, not more architecture research:
- Allegro: actual Sweden total for 3 pulleys
- Tradera: actual combined total for 2×8 bearings

These parts do not justify further broad sourcing unless either checkout fails the threshold.