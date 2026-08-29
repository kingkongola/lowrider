---
research_date: 2026-08-29
scope: LR4 permanent strut plates and sacrificial spoilboard for the 650×1250 build
status: recommendation-ready
decision_state: bootstrap on printed temp struts, then self-cut permanent struts from 5–6 mm MDF/hardboard offcut; use removable ~12 mm MDF spoilboard over a structural table/cassette rather than making MDF structural
price_basis: observed Swedish retail prices 2026-08-29; offcuts/local pickup preferred; re-check local stock before buying
region: Sweden / Gävle-oriented sourcing
sources_checked:
  - current V1 Engineering LR4 documentation
  - V1 Engineering forum LR4 builds 2025–2026
  - Hornbach Sweden MDF/hardboard pricing
  - Beijer Sweden MDF pricing
  - Bauhaus Sweden MDF pricing
supersedes: generic BOM lines for 'spoilboard' and 'material to permanent strut plates'
---

# Spoilboard + permanent strut plates

## 1. Current V1E bootstrap method is exactly what we should use

Current LR4 documentation includes **4 printed Temp Strut** parts at only 15% infill and explicitly says the machine is intended to be assembled with these temporary plates, then used to cut its own permanent strut plates.

Current V1E instructions say permanent plates should be:
- rigid material
- **6.35 mm / 1/4 inch or thinner**
- common choices: MDF, hardboard, plastic
- metal is premium and unnecessary

V1E's current 'Making the Strut plates' section is unusually explicit:
- use MDF or similarly rigid material
- **do not use 1/4-inch plywood; it is too soft**

Source:
- https://docs.v1e.com/lowrider/

A 2026 V1E discussion reinforces the intended Pareto workflow: use the four printed temporary struts first; Ryan/V1E describes them as working roughly **90% as well**, then cut the real plates after the machine is running.

Source:
- https://forum.v1e.com/t/lowrider-v4/53926?page=3

## 2. Permanent strut recommendation for our machine

Our calculator-locked `strut_length` is **819 mm** for the 650×1250 usable build.

Source:
- `research/2026-08-29-geometry-650x1250.md`

### Preferred material

**5–6 mm MDF** is the clean default.

Real LR4 build discussions specifically favour 6 mm MDF over 6 mm plywood. A 2025 LR4 build chose 6 mm MDF; another user recommendation was simply '6mm MDF' for the finished plates.

Sources:
- https://forum.v1e.com/t/ratrider-lr4-build-in-the-uk/48329?page=3
- https://forum.v1e.com/t/lr4-another-build-near-nijmegen/47176

### Hardboard is also legitimate

V1E explicitly lists hardboard as a standard option. Community builds have used thin hardboard successfully; a 2026 discussion treats 5–6.35 mm as the easy path but thinner hardboard is not automatically invalid.

Sources:
- https://docs.v1e.com/lowrider/
- https://forum.v1e.com/t/material-for-strut-plates/44748
- https://forum.v1e.com/t/strut-plate-details/53046

### Do not buy a full 6 mm sheet just for two struts

Current retail references:
- Hornbach MDF 6×1220×2440: **395 SEK**
- Beijer MDF 6×1220×2440: **473.30 SEK**
- Hornbach hardboard 2.7×1220×2440: around **139 SEK**

Sources:
- https://www.hornbach.se/p/mdf-skiva-6x1220x2440mm/7650693/
- https://www.beijerbygg.se/privat/sv/produkter/byggmaterial/byggskivor/mdf/mdf-board-12x1220x2440-2-98m2-60-ski-pall-900142713
- https://www.hornbach.se/c/byggmaterial-tra-fonster-dorrar/skivmaterial/S16715/

The permanent plates are narrow parts about 819 mm long, so paying ~400–470 SEK for almost 3 m² of 6 mm MDF solely to make them is poor value.

**Procurement rule:** use printed temp struts first. Once LR4 is alive, find a local 5–6 mm MDF/hardboard offcut large enough for the generated front and bottom plates, then let the LR4 cut them itself.

Likely sources:
- saw-service offcut bin
- cabinet/kitchen shop scrap
- furniture/carpentry offcuts
- leftovers from another project

A whole 6 mm sheet becomes rational only if its remaining area has another planned use.

## 3. Spoilboard is a different job from the structural table

Do not make the sacrificial MDF board responsible for table rigidity.

The current table architecture should remain:

`rigid underframe / CNC cassette -> structural central support/deck -> removable sacrificial MDF spoilboard`

This preserves the future removable-center concept and prevents resurfacing/replacing the spoilboard from disturbing rail/belt geometry.

A 2026 V1E table discussion makes the same useful distinction: plywood/OSB can provide structural screw-holding below, while MDF is used as the replaceable spoilboard above.

Source:
- https://forum.v1e.com/t/new-lr4-build-considering-table-options-portable/52576

## 4. Spoilboard thickness — 12 mm is the current Pareto target

For this compact machine, **~12 mm MDF** is a good first sacrificial layer if the layer underneath is structural and flat.

Why not 18–19 mm by default:
- extra thickness does not stiffen the CNC if the cassette underneath is already rigid
- it reduces available Z clearance
- it weighs/costs more
- the spoilboard is intended to be consumed and replaced

Why not very thin 3–6 mm:
- little surfacing life
- worse screw-holding for temporary workholding
- easier to locally distort

Current Swedish price references:
- Hornbach MDF 12×1220×2440: **449 SEK**
- Bauhaus MDF 12×1220×2440: **479 SEK**
- Beijer MDF 12×1220×2440: **651.91 SEK**

Sources:
- https://www.hornbach.se/c/byggmaterial-tra-fonster-dorrar/skivmaterial/mdf-skivor/S16716/
- https://www.bauhaus.se/mdf-skiva-12x1220x2440mm
- https://www.beijerbygg.se/privat/sv/produkter/byggmaterial-traprodukter/byggmaterial/byggskivor/mdf/mdf-board-12x1220x2440-2-98m2-60-ski-pall-900142713

These are full-sheet references, not a recommendation to order a full sheet online. Local cut-to-size/offcut economics may be better.

## 5. Spoilboard size for our build

Exact minimum LR4 table footprint is **941×1563 mm**, while the usable cutting area is **650×1250 mm** and practical table target ~1000×1620 mm.

The sacrificial board does **not** need to cover the entire 1000×1620 table if side rail/belt structure remains outside it.

Preferred concept:
- removable central spoilboard covering at least the **650×1250 usable zone**, with some modest margin
- final outside size determined only after the CNC cassette rail/belt supports are detailed
- likely order of magnitude around **700×1300 mm**, not a full 1000×1620 skin

The ~700×1300 figure is a design allowance, not a V1E-required dimension. Do not cut it until the table frame is laid out.

## 6. Workholding implication

MDF is excellent sacrificial material but mediocre for repeatedly holding wood screws.

Therefore the structural layer below should permit better workholding later:
- plywood/OSB/solid framing beneath the MDF, or
- threaded inserts/T-nuts in planned locations, or
- replaceable fixture strips/inserts

For first cuts, simple screws directly into MDF are fine. Do not build a complicated T-track grid before using the machine.

## 7. Recommended bootstrap sequence

1. print the four V1E temporary struts
2. assemble LR4 with temp struts
3. use a simple flat sacrificial MDF setup for first tests
4. generate the exact permanent strut SVG with `strut_length = 819 mm`
5. obtain a cheap/free 5–6 mm MDF/hardboard offcut
6. cut the two permanent plates on the LR4 itself
7. install permanent struts and re-square
8. once the modular table/cassette is final, fit a removable ~12 mm MDF spoilboard to its centre

This minimizes pre-CNC precision work and deliberately uses the machine to finish its own structure.

## Decision

- **Permanent struts:** self-cut after commissioning; 5–6 mm MDF preferred; hardboard acceptable; no 1/4-inch plywood.
- **Strut material purchase now:** none. Seek offcut later.
- **Spoilboard:** removable ~12 mm MDF central insert over structural support.
- **Do not make MDF spoilboard structural.**
- **Do not buy full sheets solely because they are easy to find online; optimize local/offcut usage first.**
