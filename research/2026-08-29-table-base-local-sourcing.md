---
research_date: 2026-08-29
last_updated_at: 2026-08-29
scope: Pareto table/base sourcing for locked ~650x1250 LR4 geometry, focused on Gävle/Sandviken used market and low-effort new fallback
status: recommendation-ready
confidence: high-on-geometry-and-buy-rules-medium-on-current-individual-listings
machine_target: LowRider V4, ~650x1250 usable, ~1000x1620 practical CNC top
region: Gävle / Sandviken / Sweden
price_basis: current/recent Blocket category counts and Swedish retail references observed 2026-08-29; individual used listings change quickly and must be checked live before pickup
sources_checked:
  - current/recent Blocket Gävle/Gävleborg table categories
  - Kinnarps Gävle showroom used/clearance furniture
  - Relovie Gävleborg used-table listings
  - local/new 180x90 steel-leg dining-table references
  - Jula workbench/sawhorse fallback prices
  - Byggmax 45x95 timber price guidance
  - existing locked LR4 geometry and TABLE.md
supersedes: generic 'find a used dining/conference table' without buy thresholds
---

# Table/base — local Pareto sourcing

## Decision

**First choice is a used rectangular dining/conference table around 1800×900 or 1800×1000 mm with a stiff steel/wood underframe and a structurally sound top.**

Do not build a dedicated underframe until this route has genuinely failed.

Why this is unusually good for our geometry:
- practical LR4 cassette/top target: ~**1620×1000 mm**
- on a **1800×900** table, the CNC layer has only **50 mm overhang per long side** and is 90 mm inset from each short end
- on a **1800×1000** table, the CNC layer fits completely within the table width

A 50 mm supported-sheet overhang is trivial if the overlay/deck is sensible. Therefore 180×90 is not a compromise that needs a custom welded frame; it is almost ideal.

## The actual hack: let the used table do the bulk structural work

Instead of building a torsion box immediately:

```text
LR4 rails / belts
        |
1000 x 1620 screw-on CNC geometry/deck layer
        |
existing used 1800 x 900/1000 tabletop
        |
existing stiff table underframe
```

The cheap overlay layer only needs to:
- give us the required ~1000 mm CNC width
- create one known removable machine datum/top
- provide convenient mounting for LR4 hardware

The used tabletop below supplies most of the bending stiffness.

### Overlay material

If the used top is already strong and flat-ish:
- **11 mm OSB** is enough as a cheap screw-on geometry/deck layer
- 12 mm construction plywood is the nicer premium option

The overlay is screwed/bolted on, **not glued**.

This matters for future conversion: the whole router top can later be removed and replaced without destroying the underframe. 'Plasma-ready later' therefore means a reversible top interface now, not building a water tray/slat system before the router works.

## Used-table target hierarchy

### Tier A — ideal

- 1750–1900 mm long
- **900–1050 mm deep**
- rectangular
- four legs with aprons/crossrails OR a commercial conference-table T-frame with a longitudinal beam
- steel underframe strongly preferred but solid traditional wood apron construction is fine
- top ~20+ mm particleboard/MDF/laminate/solid wood is fine; cosmetic damage is irrelevant
- height roughly 700–760 mm

### Tier B — still good

- 1600–1800 long
- 850–900 deep
- stiff underframe

A 1600×900 base only leaves ~10 mm top overhang at each short end and 50 mm at each side. Still mechanically easy.

### Tier C — opportunistic/bootstrap only

- 1600×800
- strong office desk/table base

The 1000 mm CNC deck would overhang ~100 mm each long side. This is still solvable with a stiff overlay but is less inherently stable than 900–1000 depth.

Do not prefer Tier C merely because the table is free if a good 180×90 table is available cheaply.

## Avoid even when cheap

- glass tops
- folding banquet tables with loose hinges
- ping-pong folding mechanisms unless only the underframe is exceptionally rigid and almost free
- central single-pedestal dining tables that twist/rack easily
- very thin hairpin-leg tables with no apron/cross-bracing
- extendable tables whose centre mechanism introduces play
- expensive electric sit/stand desks merely for height adjustment

### Height-adjustable/electric desk verdict

Not useful enough to pay for.

The LR4 does not benefit meaningfully from changing table height while cutting, while electric desk frames add:
- columns/sliders
- potential lateral play
- usually only ~600–800 mm base depth
- extra weight/cost/electronics

Use one only if a large commercial frame is extremely cheap and demonstrably rigid. Do not seek one deliberately.

## Price thresholds

The used market is liquid enough that we should be patient rather than buy new.

Recent/current Blocket search pages show dozens of matbord/skrivbord in Gävle and hundreds of table/chair listings in the broader local category. Exact individual listings move too quickly for indexed search to be treated as current stock, but supply is clearly not scarce.

### Buy rules

**0–400 SEK:** buy quickly if dimensions and racking test pass.

**400–700 SEK:** normal Pareto target for a solid 180×90/100 table. Good buy.

**700–1000 SEK:** only if it is clearly a high-quality commercial conference underframe/top with excellent geometry and zero wobble.

**>1000 SEK:** normally reject and wait/build fallback.

Reason: new alternatives start appearing around ~2,000 SEK, and a simple DIY/sawhorse bootstrap can be built for well under that. There is no reason to pay furniture-shop prices for a sacrificial CNC base.

## Current market/retail references

### Perfect geometry but absurd price — useful benchmark only

Kinnarps Gävle currently shows a Skandiform Aplomb conference table:
- **1800×1000 mm**
- black top
- in Gävle
- clearance price **14,200 SEK** for the table

This proves 180×100 commercial conference geometry is common, but obviously is not a CNC buy at that price.

Source:
- https://www.kinnarps.se/showrooms/gavle/

### Used commercial-market price reference

Relovie Gävleborg currently includes a used white conference table 100×140 cm around **874 SEK**. It is too short for us but shows the used-commercial market can sit below 1,000 SEK.

Source:
- https://relovie.com/k/hem-inredning/mobler/bord/i/gavleborg

### New 180×90 ceiling reference

Current Swedish retail examples with steel legs/MDF tops around the desired 180×90 format include roughly:
- Venture Home Sanford 180×90: ~2,096 SEK
- Venture Home Fiona 180×90: ~2,418 SEK

These are not recommended purchases. They simply prove that paying >1,000 SEK for a random used table is weak economics.

Sources:
- https://rorfokus.se/produkt/ovalt-matbord-venture-home-sanford/
- https://rorfokus.se/produkt/rektangulart-matbord-venture-home-fiona/

## Physical five-minute inspection test

Before loading a used table:

1. **grab one short-end corner and shove sideways**
   - tabletop should not visibly parallelogram/rack relative to feet
2. **push diagonally across opposite corners**
   - no loose clicking/joint motion
3. sight along the top
   - modest bow can be shimmed/surfaced; severe twist is annoying
4. inspect leg attachment
   - bolts/apron/crossbeam good
   - four tiny wood screws into chipboard bad
5. measure actual top width/depth
6. check underside for a place to bolt/screw the CNC overlay and later shelves
7. ignore scratches/ugliness

A cosmetically destroyed office/conference table can be a better CNC base than a beautiful dining table.

## Mobility — do not let wheels delay first cuts

Default for first build:
- use the table's normal fixed feet/legs
- shim/level as needed
- prove machine first

Then add mobility only if the real garage workflow shows we need it.

### Cheap later options

Four ordinary brake casters are cheap but leave the machine resting on wheels. Current Jula 75 mm brake casters are ~59.90 SEK each and 50 kg rated each, but this is a convenience solution rather than the precision ideal.

A more Pareto later hack is:
- fixed/level feet carry the table in use
- two fixed wheels mounted slightly above floor on one short end
- lift the opposite short end a little, wheelbarrow-style, to move the table

That can provide mobility for ~100–200 SEK without making four wheel swivels part of the cutting support.

Do not buy mobility hardware until the chosen underframe is physically known.

Source/reference:
- https://www.jula.se/catalog/bil-och-garage/transport/slapfordon/transporthjul/

## New/DIY fallback if no used table appears

### Bootstrap fallback A — two steel sawhorses

Jula currently has steel sawhorses around 149–199 SEK each; some adjustable models are 199 SEK on current promotion.

Two sawhorses + a simple longitudinal 45×95 frame + deck can get the LR4 running for roughly the same order as a mediocre used table.

But disadvantages are real:
- higher working height
- less integrated storage
- more assembly
- likely worse racking unless braced

This is why it is fallback, not first choice.

Sources:
- https://www.jula.se/catalog/bygg-och-farg/forvaring/bankar-och-bockar/arbetsbockar/
- https://www.byggmax.se/hus-och-bygg/virke/trareglar

### New workbench fallback — generally poor value

Current examples:
- 120×50 heavy steel workbench: ~1,999 SEK but far too narrow/short
- 200×90 workshop bench: ~3,499 SEK

These confirm that a used dining/conference table is the right economic niche for this machine.

Sources:
- https://www.jula.se/catalog/bygg-och-farg/forvaring/bankar-och-bockar/arbetssbankar/arbetsbank-024777/
- https://www.jula.se/catalog/bygg-och-farg/forvaring/bankar-och-bockar/arbetssbankar/arbetsbank-006423/

## Search terms

Search locally for all of these rather than only 'CNC bord':
- matbord 180
- matbord 180x90
- konferensbord
- mötesbord
- kontorsbord
- skrivbord 180
- arbetsbord
- bord bortskänkes
- kontorsmöbler

A seller may not know/care about exact model. Geometry and stiffness matter more than brand.

## Current recommendation

**Wait for/buy a used 180×90 or 180×100 stiff table at roughly <=700 SEK.**

Then:
1. keep its top and underframe
2. screw a removable ~1000×1620 OSB/ply CNC deck on top
3. mount LR4 geometry to that deck
4. use removable MDF spoilboard over the cutting zone
5. do not glue anything structural to the furniture base
6. only add wheels/feet after real use shows what movement pattern is needed

This is lower cost, lower build effort and likely more rigid than building a dedicated wooden furniture base before the CNC runs.
