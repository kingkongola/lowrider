---
research_date: 2026-08-29
last_updated_at: 2026-08-29
scope: source LR4 steel rails locally/within Sweden for locked 650×1250 geometry
status: recommendation-ready
decision_state: Motonet Ø30×1.5 mm ×2 m round steel tube, article 88-7123, is now the leading Pareto choice; buy 2 lengths if local stock/straightness/actual OD check passes
price_basis: Motonet Swedish product page observed 2026-08-29; 189 SEK per 2 m length; store availability must be checked in Motonet UI before pickup
region: Gävle / Sweden
sources_checked:
  - V1 Engineering current LR4 rail specification
  - locked LR4 geometry research
  - Motonet Sweden article 88-7123
  - Motonet Finland matching article/product identity
  - Handelsstål i Gävle / Uppsala Handelsstål
  - Stålgruppen
  - BE Group Sweden
supersedes: previous preference for quoted/cut 32×2 mm EN10305-3 precision tube
---

# LR4 rails — Motonet 30 mm is now the first choice

## Exact material need

For the locked ~650×1250 mm usable-area build with the purchased 6.0 mm HaWiWe plates:
- 2 × **816 mm** X rails
- 1 × **1505 mm** Y rail
- finished total = **3137 mm**

## V1E rail requirement

Current V1 Engineering LR4 documentation accepts:
- **29.5 mm, 30 mm or 32 mm OD**
- actual OD within approximately ±0.2 mm of the chosen nominal
- wall thickness **at least 1.3 mm**
- steel / stainless / DOM steel
- aluminium and carbon fibre are explicitly not acceptable

V1E also states that very thick walls/solid rods add mass and cost for little useful rigidity.

Source:
- https://docs.v1e.com/lowrider/

## Motonet exact candidate

Motonet Sweden:
- product: **Rundrör Ø30 × 1.5 mm, 2 m**
- article: **88-7123**
- product identity / model: 4011894
- nominal OD: **30 mm**
- wall: **1.5 mm**
- length: **2000 mm**
- listed weight: **2.095 kg per 2 m**
- observed price: **189 SEK each**
- reserve-and-pickup workflow exists; exact Gävle stock is store-selector dependent and not exposed in the public crawl

Sources:
- https://www.motonet.se/produkt/rundror-o-30-x-15-mm-2-m?product=88-7123
- matching Finnish Motonet product: https://www.motonet.fi/tuote/huonekaluputki-o30-x-15-mm-2-m-pyorea?product=88-7123

The listed mass is consistent with ordinary steel tubing of this geometry, and the matching Motonet catalogue places the item in the furniture/steel tube family. It is not the nearby aluminium item `75-00228`.

## Why it fits LR4 directly

- 30 mm is one of V1E's explicit supported rail diameters.
- 1.5 mm wall exceeds V1E's 1.3 mm minimum.
- no special 32 mm print geometry is needed; print/use the **30 mm LR4 rail variant**.
- two retail 2 m lengths are enough for the entire compact machine.

The only specification not published tightly enough by Motonet is **actual OD tolerance/straightness**, so inspect before final cutting.

## Exact two-stick cut plan

Buy **2 × 2000 mm**.

Stick A:
- cut **1505 mm** Y rail
- nominal remainder ~495 mm before kerf/end cleanup

Stick B:
- cut **816 mm** X rail
- cut **816 mm** X rail
- combined = 1632 mm
- nominal remainder ~368 mm before kerf/end cleanup

Total stock:
- 4000 mm

Required finished rails:
- 3137 mm

Total nominal spare/waste:
- ~863 mm minus saw kerfs/end cleanup

This is materially cleaner than buying a 6 m industrial bar.

## Cost

Observed Motonet price:
- 2 × 189 SEK = **378 SEK** total material

If available for local reserve/pickup, there is effectively no long-goods freight problem.

That makes Motonet the new Pareto winner unless a local steel merchant quotes substantially less than 378 SEK including cutting.

## In-store acceptance test

Before buying/cutting, preferably bring calipers and do a quick practical check:

1. Measure OD in several places and rotations.
   - target nominal: 30.0 mm
   - LR4 requirement: approximately 29.8–30.2 mm for the 30 mm variant
2. Roll/sight the tube or place against a known straight reference.
   - reject obviously bowed/dented lengths
3. Inspect the bearing-running surface.
   - minor cosmetic finish is fine
   - reject deep dents, heavy seam damage or severe rust
4. Confirm the label/article is **88-7123**, not aluminium `75-00228` or square tube `88-7124`.

A Motonet review on the same product identity also reports that the tube held its dimensions and was not crooked/rusty, which is encouraging but not a replacement for checking the two physical pieces we buy.

## 30 mm vs previous 32×2 precision-tube plan

### Motonet 30×1.5

Pros:
- only **378 SEK total** at current price
- exactly enough using two 2 m sticks
- retail purchase, no quote/minimum-order friction
- likely local pickup
- explicitly valid V1E OD and wall thickness

Cons:
- no published precision-tube tolerance standard
- must physically check actual OD/straightness

### 32×2 EN10305-3 from steel merchant

Pros:
- formally controlled precision-tube dimensions/tolerance
- easy to specify exact cut lengths professionally

Cons:
- quote/minimum-order friction
- usually 6 m stock
- likely more expensive for this tiny material requirement
- gives no meaningful LR4 performance advantage if the Motonet tubes are straight and in tolerance

## Recommendation

**Buy the Motonet 30×1.5 mm steel tubes if the physical pieces pass the simple caliper/straightness check.**

Order/pickup quantity:
- **2 × Motonet 88-7123**

Then cut:
- 1505 mm
- 816 mm
- 816 mm

No reason remains to pursue 32×2 EN10305-3 unless Motonet local stock is absent or the actual tubes are measurably out of tolerance/bent.
