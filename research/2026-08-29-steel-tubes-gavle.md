---
research_date: 2026-08-29
scope: source LR4 steel rails locally/within Sweden for locked-candidate 650×1250 geometry
status: recommendation-ready
decision_state: target one 6 m length of 32×2 mm EN10305-3 precision steel tube; local Gävle steel merchant is preferred if price is normal because it can cut exact lengths and eliminates long-goods freight
price_basis: public web pages rarely expose retail price for this industrial product; obtain/verify quote before purchase
region: Gävle / Sweden
sources_checked:
  - V1 Engineering LR4 rail specification
  - V1 Engineering current calculator
  - Handelsstål i Gävle / Uppsala Handelsstål
  - Stålgruppen
  - BE Group Sweden
  - EN10305-3 tolerance references
  - Gerdmans pre-cut steel-tube reference
supersedes: null
---

# Research: LR4 steel rails — Gävle / Sweden

## Exact material need for 650×1250 mm machine

From the current calculator using the purchased 6.0 mm HaWiWe XZ plates:
- 2 × **816 mm** X rails
- 1 × **1505 mm** Y rail
- finished total = **3137 mm**

A little stock must be allowed for saw kerf and end cleanup.

## Material specification

V1E accepts round steel rails with:
- OD 29.5, 30 or **32 mm**
- OD tolerance ±0.2 mm
- wall >=1.3 mm
- steel / stainless / DOM steel

V1E explicitly discourages paying for very thick walls or solid rod because the added mass gives little useful rigidity.

Recommended Swedish commodity specification:

**32×2 mm welded precision steel tube, EN10305-3, E220/E235 class or equivalent.**

Why:
- exactly one of V1E's supported ODs
- 2 mm wall exceeds the 1.3 mm minimum without becoming pointlessly heavy
- precision-tube standard gives controlled OD and straightness
- much cheaper than decorative stainless in normal industrial channels

## Tolerance sanity check

Published EN10305-3 dimensional tables put 32 mm OD precision tube within a diameter-tolerance class that is inside V1E's ±0.2 mm requirement (commonly ~±0.15 mm for this diameter range in the referenced table/version).

This is much safer than buying a random nominal “32 mm pipe” whose actual OD may be a plumbing nominal size such as 33.7 mm.

Do **not** buy 33.7 mm EN10255/EN10217 pipe: 33.7 mm is outside the LR4 supported 32 mm geometry.

## Leading source: Handelsstål i Gävle AB

Local identifiable metal supplier:
- Handelsstål i Gävle AB
- Trutvägen 4, 803 09 Gävle
- 026-495 99 00
- Mon–Fri 07–16

Their own site states:
- Gävle location is a steel/metal supplier
- well-stocked range; missing material can commonly be obtained within 1–2 days
- they cut steel, profiles and **tubes to requested dimensions** with bandsaws
- Gävle is part of the same operation as Uppsala Handelsstål and is a Tibnor distribution partner

Sources:
- https://www.ua-handelsstal.se/
- https://www.ua-handelsstal.se/kontakt/
- https://www.ua-handelsstal.se/tjanster/kapning/

### What to ask for

Quote request should be precise:

> 1 st rundsvetsat precisionsstålrör 32×2 mm, EN10305-3, gärna E220/E235, kapa till 1505 + 816 + 816 mm. Jag behöver ytterdiameter 32,0 mm inom ±0,2 mm. Vad kostar material + tre bitar/kapning inkl moms för privatkund?

This avoids being sold 33.7 mm plumbing/structural pipe.

### Best-case procurement

If they will sell roughly the required ~3.14 m plus cutting, buy only that.

If they only sell full mill lengths, buy **one 6 m bar**, not three bars. One 6 m length easily yields all three rails and leaves ~2.85 m useful spare.

Because the shop is local, full-length transport can also be solved by having them cut it before pickup.

## National reference 1 — Stålgruppen

Stålgruppen lists exact:
- **32×2 mm**
- EN10305-3
- 6 m stock length
- 1.48 kg/m
- 8.88 kg per 6 m bar
- indicated 1–2 day availability

This proves the exact specification is a standard Swedish steel-stock item.

Source:
- https://www.stalgruppen.se/stallager/ror/precstalror/32x2

Public indexed page does not expose a trustworthy retail delivered price, so it is a specification/availability benchmark rather than current cart winner.

## National reference 2 — BE Group

BE Group lists exact product:
- `Prec stålrör E220/E235 EN10305-3 32x2 mm 6.0 m`
- article **1202106605**
- 32.00 mm OD
- 2.00 mm wall
- ~1.47–1.48 kg/m
- E220/E235
- EN10305-3

Source:
- https://www.begroup.se/produkter/ror/svetsade-precisionsstalror/runda-e220-235/prec-stalror-e220-e235-en10305-3-32x2-mm-6-0-m

Again, long-goods delivery economics mean this is primarily a benchmark unless local pickup/quote beats Handelsstål Gävle.

## Rejected shortcut — generic/pre-cut 32×2 support tubes

Gerdmans sells 32×2 steel support tubes with free shipping in 500/800/1000/1200/1500 mm lengths.

This looks tempting, but the LR4 Y rail needs **1505 mm**. Their 1500 mm part is 5 mm too short for the exact calculator geometry, and the product is not documented as EN10305-3 precision tube.

Do not shrink or distort the machine simply to use these commodity pallet supports.

## Price target

No reliable consumer quote was exposed online for local 32×2 EN10305-3 stock, so do not invent a SEK target as fact.

Economic logic:
- required steel mass is only ~4.64 kg for the finished rails
- even a full 6 m bar is only ~8.9 kg
- raw material is commodity steel, so **long-goods freight/cutting/minimum-order charges are likely to dominate**, not steel value

Therefore local pickup/cutting is strongly preferred even if the per-metre steel price is somewhat higher than an online merchant.

## Recommendation

1. Formally lock 650×1250 usable geometry.
2. First quote **Handelsstål i Gävle** for exact 32×2 EN10305-3 cut to 1505/816/816 mm.
3. Ask both price for exact cut quantity and price for a full 6 m bar cut into those pieces.
4. Compare only if their quote is unexpectedly high; Stålgruppen and BE Group are verified specification fallbacks.
5. Do not buy stainless unless ordinary precision steel sourcing becomes strangely expensive. It has no meaningful value advantage for this LR4.
