---
research_date: 2026-08-29
scope: whether the LR4 shop-vac cyclone can be 3D printed instead of purchased
status: recommendation-ready
decision_state: yes; print-first is the new Pareto default, using a proven single-stage cyclone or Thien-style separator plus a separate rigid steel collection container upstream of the DeWalt; commercial cyclone remains fallback
price_basis: filament near ~100 SEK/kg target; actual printed cost depends on model mass and print time
region: Sweden / maker-built
sources_checked:
  - MakerWorld proven printed cyclone designs
  - functional-print user reports
  - J. Phil Thien separator references
  - Carbide3D community cyclone discussion
supersedes: default assumption in 2026-08-29-cyclone-separator.md that a commercial Dust Commander head should be purchased
---

# 3D-printed cyclone separator for LR4

## Short answer

**Yes. A shop-vac cyclone is an excellent 3D-print candidate.**

There are no moving parts, the geometry is printable, and multiple maker designs have long-term user reports showing successful separation of sawdust and even fine drywall/ash-type dust.

Examples:
- Nikodem Bartnik's large printed cyclone has many published makes/ratings; users report it works well and print profiles around 11–13 h are available.
- A custom two-stage printed cyclone has been used for months to keep drywall dust out of a shop-vac filter.
- Thien-style separators have extensive long-term DIY evidence and can be built with only a printed lid/inlet/outlet rather than a full printed cone.

Sources:
- https://makerworld.com/en/models/434034-big-cyclone-separator-for-a-vacuum-cleaner
- https://www.reddit.com/r/functionalprint/comments/1ctkjwb/i_3d_printed_a_two_stage_cyclone_separator_for/
- https://www.jpthien.com/cy.htm
- https://community.carbide3d.com/t/how-to-build-a-99-efficient-cyclone-dust-collector/1972

## Important architecture clarification

The existing DeWalt shop-vac already has a **metal tank**. That is not the container discussed below.

A cyclone separator needs a **separate collection container upstream of the vacuum**:

`LR4 -> cyclone -> separate collection can -> DeWalt shop-vac`

The purpose is that almost all chips/dust fall into the separate can before the air reaches the DeWalt. The DeWalt's own metal tank should therefore stay nearly empty/clean during normal CNC use.

The implosion warning applies only to a possible thin **cyclone collection bucket**, not to the DeWalt's metal tank.

## Economics

A commercial branded cyclone head previously researched costs roughly:
- Dust Commander CLC: €35.90
- Dust Commander DLX ESD MKII: €45.90
- DeWalt complete separator at Jula: 1,299 SEK

A printed cyclone typically consumes only a fraction of a kilogram to perhaps around 1 kg depending on model/scale. With our filament target near **100 SEK/kg**, the printed plastic cost is therefore usually **tens of SEK rather than hundreds**.

The separate collection container is needed either way, so that cost does not favour the commercial cyclone head.

## Recommended architecture

For this LR4:

`LR4 dust shoe -> flexible ~2.5 in moving hose -> PRINTED CYCLONE -> separate rigid steel 15–30 L collection container -> short adapter/hose -> existing DeWalt shop-vac`

This becomes the new default to test before buying a commercial cyclone.

## Which printed approach?

### Option A — proven single-stage printed cyclone: recommended first test

Advantages:
- compact
- true tangential cyclone geometry
- simple system
- readily customized ports for our hose dimensions
- published designs have successful user feedback

The Bartnik large cyclone is a good reference starting point rather than designing fluid geometry from scratch.

Source:
- https://makerworld.com/en/models/434034-big-cyclone-separator-for-a-vacuum-cleaner

### Option B — Thien-style bucket separator

This can be even cheaper in filament because most of the separator is the bucket/lid; the printed components only form inlet/outlet and possibly a baffle support.

Long-term DIY reports show strong separation performance, and Thien's own small-shop design used short runs of 2.5 in hose successfully.

Sources:
- https://www.jpthien.com/cy.htm
- https://www.jpthien.com/smf/index.php?topic=1210.0

Advantage: very easy to repair/change geometry.

Disadvantage: performance is more sensitive to baffle geometry and bucket setup; a conventional printed cyclone is more straightforward to reproduce from a proven model.

### Option C — two-stage / multi-cyclone

Technically interesting and user reports show good fine-dust results, including drywall dust.

But it adds:
- pressure loss
- print time
- more geometry
- more opportunities for leaks

Not Pareto for our router as a first separator. Use only if a simple cyclone demonstrably lets too much fine dust through.

Source:
- https://www.reddit.com/r/functionalprint/comments/1ctkjwb/i_3d_printed_a_two_stage_cyclone_separator_for/

## Print material

### PLA is acceptable for a first/probably permanent unit

The cyclone sees vacuum pressure and abrasion, but not significant heat in normal shop-vac service.

Use:
- ordinary quality PLA
- roughly 3–4+ walls
- enough top/bottom layers for airtightness
- moderate infill; wall construction matters more than filling the whole body solid

Published dust-system adapters are successfully used in PLA, and printed cyclones are commonly produced in PLA/PETG.

### PETG is a reasonable alternative

Pros:
- tougher around hose fittings and accidental knocks
- slightly less brittle

Cons:
- not necessary merely because it is a cyclone
- likely costs more than our bulk PLA

**Recommendation:** use the same ordinary PLA bought for the LR4 unless the chosen model specifically has thin snap features.

## Airtightness matters

Cyclone performance suffers from leaks.

Build rules:
- print with multiple walls
- seal multi-part joints with silicone/PU sealant or gasket
- use a foam/rubber gasket between cyclone and drum lid
- keep adapters short and smooth
- avoid unnecessary 90° elbows; user feedback on printed cyclone systems notes multiple sharp bends reduce airflow

Source:
- https://www.reddit.com/r/functionalprint/comments/1ctkjwb/i_3d_printed_a_two_stage_cyclone_separator_for/

## Separate collection container

Preferred:
- rigid steel roughly 15–30 L
- lid that can be gasketed/sealed
- cyclone mounts through the lid with a printed flange and gasket

This container sits **before the DeWalt**. It is not the DeWalt tank.

A thin plastic collection bucket can collapse if the hose blocks; this is why steel is preferred. With a steel collection can this concern largely disappears.

## Static / XPS issue

Important limitation: **ordinary PLA is electrically insulating**. A printed cyclone does not provide the ESD advantage of the commercial Dust Commander DLX ESD.

Therefore the static strategy must be system-level:
- use a groundable steel-wire/spiral moving hose where practical
- bond/ground the metal hose spiral
- use a metal collection can and bond it to the chosen grounding strategy
- keep electronics physically separated from dust hose discharge/static paths

Do not assume “conductive-looking” carbon filament solves grounding; most conductive filaments have much higher resistance than metal conductors and are not a substitute for a proper grounding conductor.

A commercial ESD cyclone remains a fallback if static proves troublesome, but paying ~€46 before testing a printed cyclone is not Pareto.

## Port sizes for our build

Do not commit to somebody else's hose sockets blindly.

After the DeWalt model is physically confirmed, measure with calipers:
- LR4 moving hose actual ID/OD
- DeWalt inlet/hose fitting actual OD/ID

Then modify/print adapters or the cyclone itself so:
- machine side is around the LR4 2.5 in class
- vacuum side mates directly/with a short taper to the DeWalt 48 mm-class connection

This is one area where owning a 3D printer makes a commercial “universal fitting” unnecessary.

## Recommended experiment

Before buying a commercial separator:

1. choose a proven conventional cyclone STL/reference design
2. adapt inlet/outlet to our actual hose dimensions
3. print in cheap ordinary PLA
4. mount airtight on a separate rigid steel collection can
5. vacuum a known mass of sawdust/XPS crumbs
6. inspect what reaches the DeWalt tank/filter
7. check suction subjectively or with a simple differential-pressure/manometer test if desired
8. if performance is good, stop researching commercial cyclones

## Decision

**New default: 3D-print the cyclone first.**

Commercial ranking becomes fallback only:
1. printed proven cyclone / custom adapters — first choice
2. Dust Commander DLX ESD — buy only if printed system has static/durability/performance problems
3. DeWalt DXVCS003 — convenience option, not value option

This is exactly the sort of component the existing 3D printer should eliminate from the purchase list.
