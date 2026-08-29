---
research_date: 2026-08-29
last_updated_at: 2026-08-29
scope: compact 230 V enclosure/distribution around KJD12 NVR, Mean Well HDR-60-24, existing DeWalt auto-start vacuum and VEVOR 0700C
status: recommendation-ready
confidence: high-on-architecture-medium-on-final-enclosure-fit
machine_target: LowRider V4 ~650x1250 mm, Sweden, dry garage/workshop
region: Sweden
price_basis: current Swedish retail pages observed 2026-08-29; store stock must be checked before pickup
sources_checked:
  - Mean Well HDR-60-24 datasheet/current DigiKey dimensions
  - KEDU KJD12 reference dimensions
  - Biltema IP65 norm enclosures and junction boxes
  - Clas Ohlson GDS Electric IP65 DIN enclosures as fallback/reference
  - Biltema 3G1.5 extension lead and 6.3 mm Faston terminals
  - Jula M20 IP68 cable glands and Wago 221-413
  - existing DeWalt DXV30SAPTA tool-socket research
supersedes: previous preference for Clas Ohlson 36-9846 as the compact enclosure
---

# Compact 230 V machine enclosure / distribution

## Decision

Do **not** build a large contactor cabinet.

Baseline is a small portable-machine enclosure containing only:
- KJD12 NVR / emergency-stop switch
- Mean Well `HDR-60-24`
- three simple mains distribution junctions
- strain-relieved mains input and switched DeWalt output

The VEVOR router remains plugged into the DeWalt's 2450 W-rated auto-start tool socket.

Topology:

```text
wall
  |
  |  moulded Schuko plug + 3G1.5 lead
  v
KJD12 NVR / stop  [switches L + N]
  |
  +---- switched L/N ----> HDR-60-24 ---- 24 VDC ----> Jackpot3
  |
  +---- switched L/N ----> moulded Schuko female ----> DeWalt DXV30SAPTA [AUTO]
                                                     |
                                                     +--> VEVOR 0700C 800 W

PE: wall plug ------------------------------------------------> DeWalt female socket
    (protective earth does NOT pass through KJD12)
```

The HDR-60-24 is Class II / double-insulated and does not need a PE connection.

## Why one normal extension lead is a useful hack

Rather than buying separate loose Schuko plug + socket hardware, use one approved **3G1.5 mm², 16 A extension lead** as donor cable:
- retain the factory-moulded male plug for machine input
- retain the factory-moulded female socket for the DeWalt output
- trim cable lengths to suit the table
- any suitable offcut can provide short internal 1.5 mm² jumpers

Current cheap reference:
- Biltema article `46-3610`
- 3 m
- `H05VV-F 3G1.5`
- 250 V / 16 A
- **59.90 SEK**

Source:
- https://www.biltema.se/hem/jul/jul-i-koket/skarvsladd-jordad-3-m-2000055051

For this dry indoor garage/table application H05VV-F is sufficient if protected from mechanical abuse.

## Enclosure — Biltema is now the Pareto default

Biltema norm enclosure:
- article **`35-0065`**
- 4 DIN modules
- **IP65**
- integrated DIN rail
- halogen-free plastic
- **120 × 160 × 90 mm**
- observed price **99.90 SEK**

Source:
- https://www.biltema.se/bygg/elinstallationer/normcentraler/normkapsling-4-moduler-2000066035

This is essentially the same external size class as the previously selected Clas Ohlson 3–5-module box (120×160×90 mm), but about **50 SEK cheaper** and already includes the DIN rail needed by HDR-60-24.

### Why not Biltema's ordinary cheap junction boxes?

Biltema also has very cheap IP65 junction boxes:
- 88×88×53 mm: 64.90 SEK
- 100×100×70 mm: 84.90 SEK
- 200×155×80 mm: 199 SEK

Sources:
- https://www.biltema.se/bygg/elinstallationer/eldosor/kopplingsdosa-ip65-88-x-88-mm-2000065979
- https://www.biltema.se/bygg/elinstallationer/eldosor/kopplingsdosa-ip65-100-x-100-mm-2000065980
- https://www.biltema.se/bygg/elinstallationer/eldosor/kopplingsdosa-ip65-200-x-155-mm-2000065982

The two small boxes are too cramped for HDR + KJD12 + safe wire bend/routing. The large 200×155 box has space but **no included DIN rail** and costs twice the 4-module norm enclosure. Therefore it is not actually the cheaper complete solution.

### Fit sanity check

HDR-60-24 dimensions:
- 52.5 × 90 × 54.5 mm
- standard DIN rail TS-35

Typical KJD12 reference dimensions are roughly 86–88 × 55–56 mm faceplate, with ~35 mm depth behind panel depending variant.

A 120×160×90 mm enclosure is plausible, but the exact KJD12 variant should be physically dry-fitted before cutting.

Before cutting:
1. have exact KJD12 in hand
2. clip HDR-60-24 onto the real DIN rail
3. make a paper/cardboard KJD12 template
4. verify terminal and wire-bend clearance
5. only then cut the switch opening

If cramped, do not force it. Biltema also sells a **12-module IP65** norm enclosure:
- article `35-0067`
- 225×200×110 mm
- integrated DIN rail
- **229 SEK**

Source:
- https://www.biltema.se/bygg/elinstallationer/normcentraler/normkapsling-12-moduler-2000054143

That is the clean fallback and is still cheaper than many dedicated control cabinets.

## Mains distribution inside the box

After KJD12, switched L and N each feed:
- HDR-60-24
- DeWalt output lead

PE connects:
- input PE
- DeWalt output PE

Three `Wago 221-413` three-conductor connectors are sufficient:
- switched L: KJD12 output + HDR L + DeWalt-output L
- switched N: KJD12 output + HDR N + DeWalt-output N
- PE: input PE + DeWalt-output PE, third port unused

Jula reference:
- article `001480`
- 12-pack genuine Wago 221-413
- **129 SEK**

Source:
- https://www.jula.se/catalog/el-och-belysning/elinstallation/installationsmateriel/kopplingslister-och-kopplingsklammor/kopplingsklammor-001480/

If genuine Wagos are already in workshop stock, buy none.

## KJD12 terminals

KJD12 commonly uses 6.3×0.8 mm Faston tabs.

Use properly crimped insulated female 6.3 mm receptacles matching actual conductor area.

Biltema reference:
- article `44-0020`
- 1.5–2.5 mm²
- **24.90 SEK / 10**

Do not solder directly to mains switch tabs.

## Cable entries / strain relief

Use real cable glands for the 3G1.5 leads.

Jula/Rutab M20 reference:
- article `402070`
- IP68
- 2-pack
- **39.90 SEK**

Source:
- https://www.jula.se/catalog/el-och-belysning/elinstallation/installationsmateriel/kabelgenomforing/forskruvningar-402070/

The 24 V cable to Jackpot3 can use a correctly sized smaller gland once actual cable OD is known.

## Extra fuse / breaker?

No separate DIN MCB is part of the Pareto baseline.

The machine is plug-connected to an already protected branch circuit; adding a generic duplicate 16 A MCB does not materially improve the baseline system.

## Updated incremental cost

Excluding separately budgeted **KJD12** and **HDR-60-24**:

- Biltema 4-module IP65 DIN enclosure: **99.90 SEK**
- Biltema 3 m 3G1.5 extension lead: **59.90 SEK**
- Jula M20 glands: **39.90 SEK**
- Wago 221-413 12-pack: **129 SEK**
- 6.3 mm insulated Faston pack: **24.90 SEK**

Total if all must be bought:
- **~354 SEK**

If genuine Wagos/Faston supplies already exist:
- roughly **~200 SEK** incremental for enclosure + donor lead + glands

Moving to Biltema's 12-module enclosure adds about 129 SEK over the 4-module box.

## Safety / commissioning gate

Before energising:
- follow exact KJD12 terminal numbering/datasheet
- switch L and N through the intended two poles
- keep PE continuous and unswitched to the DeWalt output
- use correct crimp tooling
- no exposed live parts with enclosure closed
- real strain relief on every cable
- continuity-test PE
- verify no L/N-to-PE short
- verify KJD12 no-volt release before connecting router
- verify DeWalt AUTO with a test load first

If uncertain about mains assembly/testing, have the finished portable machine box checked/wired by someone competent with 230 V equipment.

## Decision

**Pareto baseline is now Biltema-heavy:**
- Biltema `35-0065` 4-module IP65 DIN enclosure — 99.90 SEK
- KJD12 in panel after physical fit check
- HDR-60-24 on included DIN rail
- Biltema 3 m 3G1.5 donor extension lead
- Wago branch distribution
- M20 glands
- insulated 6.3 mm Faston

Use Biltema `35-0067` 12-module box only if the real component dry-fit proves the small box uncomfortable.
