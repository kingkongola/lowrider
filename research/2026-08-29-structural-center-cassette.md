---
research_date: 2026-08-29
scope: structural deck/center cassette underneath the removable MDF spoilboard
status: recommendation-ready
decision_state: reuse a suitable used-table top first; if a new structural sheet is needed, 11 mm OSB is the value default and 12 mm construction plywood the modest premium; do not buy until underframe/table is chosen
price_basis: observed Swedish retail prices 2026-08-29; local pickup/offcuts preferred
region: Sweden / Gävle-oriented sourcing
sources_checked:
  - V1 Engineering 2026 table discussions
  - Hornbach Sweden OSB and construction plywood pricing
supersedes: any assumption that MDF spoilboard itself should provide table structure
---

# Structural center cassette under the spoilboard

## Goal

Separate three jobs:

1. **outer CNC cassette/frame** — preserves LR4 rail/belt geometry
2. **structural center deck** — supports workpiece and spoilboard without sagging
3. **sacrificial MDF spoilboard** — gets surfaced, screwed into and eventually replaced

This separation is important for the future removable-center concept.

## V1E material guidance

A current 2026 LR4 discussion says table structure may use **plywood, MDF, or OSB**, while the spoilboard should definitely be **MDF**.

Another 2026 table discussion specifically notes a practical advantage of a plywood/OSB structural layer below MDF: MDF is mediocre at holding repeated screws, so the tougher underlying sheet helps with workholding.

Sources:
- https://forum.v1e.com/t/lowrider-v4/53926
- https://forum.v1e.com/t/new-lr4-build-considering-table-options-portable/52576

## First choice — reuse the top that comes with the used table

If the chosen dining/conference/work table has a reasonably stiff intact top, **do not replace it automatically**.

It does not need CNC-level flatness by itself because:
- the LR4's outer rail/belt geometry belongs to our own cassette/frame
- the spoilboard can be shimmed/supported and then surfaced by the CNC

Checks:
- no large local sag/soft hollow-core damage
- enough screw-holding or ability to through-bolt our cassette
- no rocking or large twist in the underframe
- top material survives being cut/modified for a removable center if we choose that route

This can make structural-deck material cost **0 SEK**.

## New-sheet fallback A — 11 mm OSB: value default

Current Hornbach reference:
- OSB 11×1197×2500 mm
- **239 SEK**
- ~79.85 SEK/m²

Source:
- https://www.hornbach.se/c/byggmaterial-tra-fonster-dorrar/skivmaterial/S16715/

One sheet is large enough to cut a roughly 1000×1620 mm structural top/cassette skin if required, with useful remainder.

Pros:
- cheapest serious structural sheet found
- good screw holding compared with MDF
- perfectly adequate when supported by a frame/ribs
- cheap enough to replace/modify later

Cons:
- rough surface
- not as dimensionally pretty/flat as good plywood
- edges shed chips; seal or cover exposed areas if needed

The rough surface is largely irrelevant if a removable MDF spoilboard sits above it.

## New-sheet fallback B — 12 mm construction plywood: small premium

Current Hornbach reference:
- construction plywood 12×1200×2500 mm
- **399 SEK**
- ~133 SEK/m²

Source:
- https://www.hornbach.se/c/byggmaterial-tra-fonster-dorrar/skivmaterial/plywood/konstruktionsplywood/S29654/

Premium over the full OSB sheet: about **160 SEK**.

Pros:
- better screw holding
- cleaner edges
- generally nicer to bolt/modify repeatedly
- useful if center cassette will be removed/reinstalled often

Cons:
- costs ~67% more than the OSB sheet
- no need to pay this premium merely for a sacrificial surface

## What not to do

### Do not use 12–19 mm MDF as the only structural deck just because the spoilboard is MDF

MDF is excellent for surfacing but:
- poorer repeated screw holding
- heavier
- moisture-sensitive edges
- structural material gets consumed if spoilboard and deck are combined

Keep the sacrificial layer separate.

### Do not buy a sheet before the used underframe/table is known

A free/cheap conference table may already include exactly the structural top we need. Buying OSB or plywood today can create a redundant 2.5 m sheet in the garage.

## Interaction with future removable center / plasma conversion

The rail/belt supports should stay on the **outer cassette/frame**.

The center can then be one removable assembly:

```text
router mode:
outer LR4 cassette
└── removable structural center deck (existing top / OSB / plywood)
    └── removable 12 mm MDF spoilboard

future alternate mode:
outer LR4 cassette stays untouched
└── center deck/spoilboard removed
    └── different insert can occupy the opening
```

No plasma-specific hardware is needed now; the only requirement is to avoid gluing the central MDF permanently into the rail/belt structure.

## Current material ranking

1. **Reuse existing used-table top** if structurally suitable — 0 SEK.
2. **11 mm OSB ~239 SEK** — value fallback.
3. **12 mm construction plywood ~399 SEK** — spend +160 SEK if repeated removal/screw holding or better handling justifies it.
4. MDF as structural-only layer — not preferred.

## Buy condition

Do not order any structural deck sheet until the actual underframe/table has been selected and measured.

Then choose the cheapest route that gives:
- support spacing small enough to prevent sag
- independent outer LR4 geometry
- removable center
- removable MDF spoilboard
