---
research_date: 2026-08-29
scope: reuse of owned DeWalt DXV30SAPTA 48 mm × 2.1 m hose on LR4 instead of buying 2.5-inch hose
status: recommendation-ready
decision_state: test/reuse the existing DeWalt hose first; design dust-shoe and cyclone adapters around measured hose cuffs; buy larger 2.5-inch hose only if real movement/suction/static testing justifies it
price_basis: owned hose = zero incremental cost; only short stationary cyclone-to-vac connection may need material
region: Sweden / maker-built
sources_checked:
  - DeWalt DXV30SAPTA manual
  - Jula DXV30SAPTA page
  - current V1 Engineering LR4 documentation
  - V1E hose-fit / 48–50 mm dust-shoe discussions
supersedes: default assumption that a new 2.5-inch moving hose must be purchased
---

# Reuse the owned 48 mm DeWalt hose first

## Known vacuum/hose data

Very likely owned vacuum: DeWalt `DXV30SAPTA`.

Manual/Jula specification:
- 1050 W
- 15 kPa seal pressure
- 37.8 L/s airflow
- 30 L metal tank
- **48 mm × 2.1 m hose**

Sources:
- https://www.jula.se/catalog/hem-och-hushall/stad-och-kladvard/dammsugare/grovdammsugare/grovdammsugare-015478/
- https://www.bauhaus.se/media/pdf/1163387A.pdf

## Why 48 mm is not automatically too small

The current LR4 BOM links a nominal 2.5-inch / ~70 mm OD hose, but V1E history and current community designs show that ~48–50 mm hose is a legitimate dust-shoe size:

- earlier V1E Makita dust shoe was explicitly designed around **~48 mm OD vacuum hose**
- V1E forum users routinely print tapered adapters for smaller hoses
- a 2025 LR4 community dust collector/shoe was designed specifically for a **50 mm hose**
- users report good results with high-static-pressure shop-vac systems and roughly 2-inch-class moving hose

Sources:
- https://forum.v1e.com/t/confused-about-vacuum-hose-sizes/41411
- https://forum.v1e.com/t/dust-collector-shoe-for-easy-tool-change/49079
- https://forum.v1e.com/t/lowrider-v3-in-maryland-klipper-4x8/41660?page=7

Therefore the nominal 2.5-inch BOM hose is a good default, not a reason to discard a suitable zero-cost 48 mm DeWalt hose.

## First-choice setup

Try:

`LR4 dust shoe -> existing DeWalt 48 mm × 2.1 m hose -> printed cyclone -> separate metal collection can -> SHORT stationary 48–50 mm link -> DeWalt vacuum`

### Dust-shoe connection

Do not buy a universal reducer.

When the hose is available:
1. measure the actual hard cuff and flexible hose OD/ID with calipers
2. select/remix a 48–50 mm LR4/Makita-style dust-shoe connector or print a short tapered adapter
3. use a small taper/interference fit or magnetic/threaded printed connector
4. strain-relieve hose at the LR4 core so the dust shoe does not carry hose weight

A printed adapter is standard practice in the V1E community.

## Is 2.1 m long enough?

For the current practical table around **1.0 × 1.62 m**, 2.1 m is potentially enough if cyclone placement is designed around the hose rather than putting the separator arbitrarily on the floor at one end.

### Best placement

Mount the cyclone/collection can:
- under or just outside the **middle of a long side** of the table
- fairly high under the table rather than on the floor
- with the hose entering from above/side without a sharp 180° bend

Geometric sanity check for a ~1.0 × 1.62 m table:
- horizontal straight-line distance from long-side midpoint to opposite far corner ≈ 1.29 m
- adding roughly 0.4–0.5 m vertical offset gives straight-line distance around 1.35–1.4 m
- that leaves roughly **0.7 m of a 2.1 m hose** for curvature/slack/support

This is not a guarantee because the hose must follow the moving LR4 without pulling, but it is enough to make **reuse-first** the rational experiment.

### Dry-fit acceptance test

Before buying any moving hose:
1. temporarily locate cyclone inlet at proposed under-table midpoint
2. attach/hold the 2.1 m DeWalt hose at the moving core/dust-shoe location
3. move LR4 manually to all four corners and Z extremes
4. verify no tension, kinking or table-edge snagging
5. verify hose can be supported by a simple overhead/gantry support

If it passes, buy no moving hose.

If it fails only by ~20–40 cm, first reconsider cyclone position/support before buying a whole new hose.

## Short cyclone-to-vacuum link

Reusing the DeWalt hose on the moving side means the cyclone outlet still needs a connection to the vacuum inlet.

This is stationary and should be kept **very short**.

Cheap options:
- short 50 mm flexible hose offcut
- short smooth 50 mm waste/vent pipe if dimensions suit
- printed large-radius/tapered duct section
- second-hand/offcut vacuum hose

Because this section does not move, weight and flexibility barely matter.

Do not spend hundreds on a second premium hose for a 20–50 cm stationary connection.

## Static strategy with the stock DeWalt hose

The stock hose is not documented as ESD/antistatic in the checked manual.

V1E explicitly warns that non-conductive vacuum hoses can accumulate static and recommends adding a grounding conductor if a steel-ribbed hose is not used.

Source:
- https://docs.v1e.com/lowrider/

Reuse-first static plan:
- add a light bare/grounding conductor along or through the hose as V1E recommends
- terminate it at a deliberate ground point
- bond the separate metal cyclone collection can as part of the same static-control strategy
- keep controller wiring physically separated from the hose/static path

Because XPS is a likely material, static behaviour should be observed during initial foam tests.

## Performance trade-off: 48 mm vs 2.5-inch

A larger 2.5-inch moving hose has lower flow resistance and more cross-sectional area, so it remains the performance upgrade if needed.

However:
- the DeWalt itself is designed around 48 mm hose
- the vacuum's published performance is specified with that class of hose
- shop-vacs provide relatively high static pressure
- LR4 source-capture occurs at a small dust shoe rather than a 100 mm woodworking hood

Therefore there is no good reason to spend money and add a heavier/bulkier hose before testing the owned 48 mm hose.

## Buy/no-buy decision

### Buy no new moving hose initially

Use the existing DeWalt hose unless one of these happens during dry-fit/test cuts:
- it physically cannot reach without pulling the gantry
- it is too stiff/heavy for reliable movement
- it kinks in the required bends
- source capture is clearly inadequate despite a good dust shoe and clean cyclone/filter
- static is troublesome enough that a steel-wire hose is a cleaner fix than adding grounding conductor

### If upgrade becomes necessary

Then buy the V1E-style **flexible 2.5-inch / ~70 mm OD steel-ribbed groundable hose**, but only the minimum length required by the measured table routing.

## Current cost impact

Potential moving-hose purchase: **0 SEK**.

Likely incremental hose-interface costs:
- printed adapters: a few SEK of PLA
- short stationary cyclone→vac link: cheap/offcut/printed
- grounding wire: negligible if already in workshop stock

This is now the dust-hose Pareto baseline.
