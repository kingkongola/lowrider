---
research_date: 2026-08-29
last_updated_at: 2026-08-29
scope: remaining orphan mechanical items: 3× GT2 16T 5mm/10mm pulleys and 14× 608-2RS bearings
status: recommendation-ready
decision_state: keep these as orphan commodity purchases; use exact Allegro 16T if Sweden checkout is sensible, otherwise exact AliExpress Choice fallback; for 608 first check the active Swedish Tradera seller for a current 20-pack around <=200 SEK delivered, otherwise use low-cost EU/Allegro; do not force either item into a worse larger cart
price_basis: observed prices 2026-08-29; marketplace shipping and current listing state must be verified at checkout
region: Sweden / EU / marketplace fallback
sources_checked:
  - V1 Engineering current LR4 BOM
  - Allegro exact 16T pulley product
  - Allegro exact 608-2RS listings/search results
  - Allegro Sweden international shipping documentation
  - targeted Amazon.se exact-variant searches
  - Tradera Swedish 608-2RS seller/listings
  - Fyndiq exact 20-pack reference
  - AliExpress indexed 10mm-width pulley packs
supersedes: earlier assumption that Amazon Prime would probably be the 608 winner
---

# Final orphan strategy: 16T pulleys + 608-2RS

These are now intentionally treated as cheap orphan items. Their low item value means they must not distort the already-good LaskaKit/DigiKey/StepperOnline carts.

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

### Best fully verified part: Allegro `GT2-16T-5B_10mm_K`

Current exact product:
- 16T
- 5 mm bore
- for 10 mm GT2 belt
- 11 mm tread width
- aluminium
- **2 set screws included**
- observed price **7.20 PLN each**

Need 3:
- parts = **21.60 PLN**

Source:
- https://allegro.pl/oferta/napedowe-kolo-zebate-gt2-na-pasek-10mm-walek-5mm-16t-cnc-druk-3d-18355347606

This remains the strongest exact-spec listing because the geometry is explicitly stated rather than inferred from a variant title.

### Sweden shipping rule

Allegro supports DHL/DPD delivery from Poland to Sweden when the seller enables it, but the exact seller/order freight must be checked in checkout.

Do not accept an international freight charge that makes three tiny pulleys absurdly expensive.

**Buy rule:** if delivered total for 3 exact Allegro pulleys is roughly <=150–180 SEK, just buy them and stop optimizing.

### AliExpress / Choice fallback

Current indexed 5-pack candidates exist with selectable:
- 16T
- 5 mm bore
- 10 mm belt width

A previously identified 5-pack product ID is `1005012977561121`, headline around US$6.62 before variant-specific checkout.

This can be even better because two spare pulleys are useful.

But marketplace variant selection is the risk. Checkout must visibly resolve to:
- 16T
- 5 mm bore
- 10 mm belt width
- qty 5

If exact variant + Swedish VAT/Choice shipping is around <=120–150 SEK delivered, it beats a badly-shipped Allegro order.

### EU-shop fallbacks

Still exact but only useful if freight can be shared:
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

## Swedish Tradera route — current first check

A Swedish business seller, `Motion_And_Rotaion` / related earlier seller identity, has repeatedly listed exact:
- 608-2RS
- 8×22×7 mm
- double rubber seal
- chrome/hardened steel

A verified 20-pack listing was:
- **170 SEK**
- **10 SEK Sweden shipping**
- total **180 SEK delivered**

Source/reference:
- https://www.tradera.com/item/301813/723643685/20st-608-2rs-ball-bearing-8x22x7mm-608-2rs-rubber-sealed

That exact 20-pack page is an older listing and must not be described as currently active. However, the same seller family is still visibly active in August 2026 selling fresh 608-2RS sets with the same exact 8×22×7 specification.

Therefore the new practical rule is:

**First check the seller's current inventory for a 20-pack. If exact 20-pack is <=200 SEK delivered from Sweden, buy it.**

Why this is attractive:
- domestic shipping
- no variant/import ambiguity
- exact dimension/seal spec
- six useful spares
- total already inside our previous target band

## Allegro fallback for bearings

Fresh Allegro search results show exact generic 608-2RS / 8×22×7 in 10-packs around:
- ~9.4–10.2 PLN per 10-pack

So two 10-packs can be only ~20 PLN in parts. Freight dominates.

Examples/search evidence:
- https://allegro.pl/listing?string=%C5%82o%C5%BCysko+kryte+8+22+608rs

If a seller ships two exact 10-packs to Sweden cheaply enough, this can beat Tradera. But do not assume Polish domestic 'with delivery' prices apply to Sweden.

### Quality tier

Generic commodity 608-2RS is acceptable for LR4.

Named low/mid-cost Polish/European brands such as CX, KINEX or CODEX are also fine if the delivered premium is tiny, but no benefit justifies paying several times more.

## Amazon Prime — no longer the assumed winner

Repeated targeted Amazon.se searches still failed to verify a current exact listing end-to-end as:
- 20 pcs
- 608-2RS
- 8×22×7
- rubber seals both sides
- current Swedish price/availability

Legacy ASIN `B07X5T7DGS` remains **unverified and not approved**.

Prime is still welcome if an exact current listing appears, but it no longer gets priority merely because Prime exists.

## Rejected current Swedish option

Fyndiq has a current exact 20-pack around:
- 309 SEK
- +29 SEK freight

It is correct specification but poor value versus the historical/current Swedish Tradera seller pricing and cheap EU commodity sources.

Source:
- https://fyndiq.se/produkt/20-st-608-2rs-kullager-lagerstal-lager-8x22x7mm-d-256fc72ef6e24828/

## Checkout decision tree

### 16T
1. Try exact Allegro `GT2-16T-5B_10mm_K` ×3.
2. If Sweden delivered <=150–180 SEK: buy.
3. If freight is bad, verify exact AliExpress Choice 5-pack 16T/5mm/10mm.
4. Buy the Choice pack if <=120–150 SEK delivered with VAT and exact variant visibly selected.
5. Hellas/Anodas only if freight is shared with another real purchase.

### 608
1. Check current Tradera inventory from the active Swedish 608 seller.
2. If exact 20-pack 608-2RS / 8×22×7 is <=200 SEK delivered: buy.
3. Otherwise price 2×10 exact packs on Allegro including Sweden delivery.
4. Amazon Prime only if an exact current 20-pack is actually verifiable around <=180–200 SEK delivered.
5. Reject Fyndiq at ~338 SEK delivered and reject SKF/NSK premium.

## Final status

The specs and thresholds are now locked. What remains is only live checkout/listing state.

These parts do **not** justify more architecture research. They should be bought opportunistically under the thresholds above while the larger carts are being placed.