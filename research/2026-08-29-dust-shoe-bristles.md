---
research_date: 2026-08-29
scope: LR4 dust shoe skirt/bristles and whether TPU must be purchased
status: recommendation-ready
decision_state: user already owns TPU; if spool is ~95A, print V1E-style TPU bristles as first choice; craft foam remains fallback
price_basis: already-owned TPU means zero incremental purchase cost; V1E TPU set $5 reference only
region: Sweden / maker-built
sources_checked:
  - user-provided existing TPU inventory
  - V1E LR4 dust-shoe discussions
  - V1E TPU bristle product
  - V1E community TPU-free dust-shoe solution
  - V1E traditional-bristle discussion
supersedes: earlier version of this file that treated TPU as a possible future purchase
---

# LR4 dust shoe + bristles

## Updated local inventory

The user **already owns TPU filament**.

Therefore there is no reason to buy TPU for the LR4 dust shoe. The only remaining check is the spool's hardness/durometer.

- if approximately **95A**: use it for the standard V1E bristles
- if substantially softer/harder or unlabeled: print a small test section first; craft foam remains a zero/low-cost fallback

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

## Pareto fallback — 1 mm craft foam

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

This is now a fallback rather than the bootstrap default because TPU is already on hand.

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

1. check the owned TPU spool label for durometer
2. if ~95A, print the standard V1E bristles first
3. print the current Makita/65-mm LR4 dust shoe in ordinary PLA
4. adapt its hose inlet to the actual measured DeWalt 48 mm hose cuff
5. test dust capture in wood/XPS
6. use 1 mm craft foam only if the owned TPU is unsuitable or the foam geometry proves more convenient

## Procurement consequence

Immediate mandatory purchase for bristles: **none**.

TPU purchase: **removed from BOM**.
