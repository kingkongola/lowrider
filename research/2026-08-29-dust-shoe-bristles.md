---
research_date: 2026-08-29
scope: LR4 dust shoe skirt/bristles and whether TPU must be purchased
status: recommendation-ready
decision_state: use official/current Makita-style LR4 dust shoe geometry; TPU 95A is preferred standard but 1 mm craft foam is a validated zero/low-cost fallback, so TPU purchase is not a build blocker
price_basis: V1E TPU set $5 reference; local material price not yet needed
region: Sweden / maker-built
sources_checked:
  - V1E LR4 dust-shoe discussions
  - V1E TPU bristle product
  - V1E community TPU-free dust-shoe solution
  - V1E traditional-bristle discussion
supersedes: null
---

# LR4 dust shoe + bristles

## Baseline

Use the current LR4 Makita/65-mm-router dust-shoe family as the baseline for the VEVOR 0700C.

The dust shoe itself is printable in normal rigid filament. The flexible skirt/bristles are a separate replaceable insert.

## Standard V1E solution — TPU 95A

V1E sells/uses **TPU 95A** bristles for LR4 dust shoes.

Current V1E reference:
- standard and extra-long variants
- extra-long listed as 32 mm
- one set = two pieces
- $5 per printed set

Source:
- https://www.v1e.com/products/tpu-bristles-for-the-lr4-dust-shoes

Community consensus around the stock geometry also points to **95A TPU**. The thin wall geometry makes the finished bristles much softer than a solid 95A part would suggest.

Source:
- https://forum.v1e.com/t/tpu-durometer-for-dust-shoe-bristles/46713

### Length matters

Do not simply make very long bristles.

Ryan/V1E notes that overly long TPU fingers can:
- get sucked into the vacuum
- contact the cutter
- drag on the workpiece/router and hurt accuracy

Stock/standard bristles were designed around normal endmill stickout and roughly up-to-17-mm-class DOC; 32 mm is already near the long end of practical community variants.

Source:
- https://forum.v1e.com/t/longer-tpu-bristles-for-lr4-dust-shoes/46083

## Excellent Pareto fallback — 1 mm craft foam

A documented LR4 community solution avoids TPU entirely:
- use **1 mm craft foam**
- press it into the stock dust-shoe skirt slot
- use a piece of PLA filament on the outside to wedge/retain the foam in the groove
- cut the foam into flexible fingers with scissors/knife

Reported advantages:
- cheap
- easy
- replaceable
- uses the existing shoe geometry

Source:
- https://forum.v1e.com/t/tpu-free-lr4-dust-shoe/45906

### Assessment

This is an unusually good bootstrap solution for us.

It means **do not buy a whole TPU spool just to finish the CNC**.

If 1 mm craft foam is already at home or can be bought for a few tens of SEK, the machine can be commissioned with it and upgraded to printed TPU later only if needed.

## Traditional commercial brush strip — not preferred

A later LR4 discussion specifically reports that conventional CNC brush strips are often too long/stiff for this compact shoe. The TPU fingers are much more compliant and less likely to snag the workpiece.

Source:
- https://forum.v1e.com/t/dust-shoe-with-traditional-bristles/52019

Therefore do not buy a roll of standard nylon dust-shoe brush just because it looks professional.

## Interaction with our 48 mm DeWalt hose

The current official LR4 dust-shoe family accepts up to roughly 70 mm OD hose depending version, but a 48–50 mm connection is straightforward:
- use a 48/50 mm remix if one matches the selected Makita shoe
- or print a short tapered insert/adapter into the stock port

A current LR4 community shoe has explicitly been designed around a 50 mm hose.

Source:
- https://forum.v1e.com/t/dust-collector-shoe-for-easy-tool-change/49079

So the dust shoe does not force us to buy 2.5-inch hose.

## First-build recommendation

1. print the current Makita/65-mm LR4 dust shoe in ordinary PLA
2. adapt its hose inlet to the actual measured DeWalt 48 mm hose cuff
3. bootstrap skirt with **1 mm craft foam** if available
4. test dust capture in wood/XPS
5. only then decide whether to buy a small amount/spool of TPU 95A and print stock bristles

## Procurement consequence

Immediate mandatory purchase for bristles: **none**.

Possible later purchase:
- TPU 95A only if foam wears badly, suction is poor, or the stock snap-in bristle convenience is worth it

This keeps dust collection functional from day one without adding another filament order merely for a small flexible part.
