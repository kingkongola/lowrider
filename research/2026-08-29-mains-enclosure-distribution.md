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
  - Clas Ohlson GDS Electric IP65 DIN enclosures
  - Biltema 3G1.5 extension lead and 6.3 mm Faston terminals
  - Jula M20 IP68 cable glands and Wago 221-413
  - existing DeWalt DXV30SAPTA tool-socket research
supersedes: generic open question for 230 V enclosure/distribution in purchase-ready-order-graph
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

This avoids DIY mains plug/socket termination and gives known 16 A cable/ends cheaply.

Current cheap reference:
- Biltema article `46-3610`
- 3 m
- `H05VV-F 3G1.5`
- 250 V / 16 A
- **59.90 SEK**

Source:
- https://www.biltema.se/hem/jul/jul-i-koket/skarvsladd-jordad-3-m-2000055051

For this dry indoor garage/table application H05VV-F is sufficient if protected from mechanical abuse. If the machine is later used wet/outdoors, replace this with an appropriate H07RN-F/IP44 lead instead.

## Enclosure candidate — compact Pareto default

Clas Ohlson GDS Electric norm enclosure:
- article `36-9846`
- 3–5 DIN modules
- **IP65**
- integrated DIN rail
- 120 × 160 × 90 mm external
- halogen-free plastic
- **149.90 SEK** observed

Source:
- https://www.clasohlson.com/se/GDS-Electric-normkapsling-3-5-moduler%2C-IP65/p/36-9846

### Fit sanity check

HDR-60-24 dimensions:
- 52.5 × 90 × 54.5 mm
- standard DIN rail TS-35

Source:
- https://www.digikey.se/en/products/detail/mean-well-usa-inc/HDR-60-24/7703804
- Mean Well `HDR-60` datasheet

Typical genuine KEDU KJD12 reference dimensions:
- mounting plate roughly 86–88 × 55–56 mm
- depth behind plate ~35 mm
- approximate panel hole around 40 × 60 mm on one common KJD12 form

Sources:
- https://charnwood.net/product/on-off-switch/
- KEDU KJD12 dimensional datasheet / Macma reference

A 120 × 90 mm enclosure end/side face is therefore geometrically large enough for the KJD12 faceplate, while the HDR occupies only 52.5 mm of DIN width.

**However:** KJD12 has several mechanical variants and the exact moulding/cable-entry layout of the enclosure matters. Do not cut the box from nominal dimensions alone.

Before purchase/cutting:
1. have the exact KJD12 in hand
2. make a cardboard/paper cutout for its body/faceplate
3. dry-place the real HDR-60-24 on the DIN rail
4. verify terminal/wire bend clearance
5. only then cut the KJD12 opening

If the 3–5-module enclosure feels cramped, move one size up rather than forcing it:
- Clas Ohlson 8-module IP65 enclosure `36-1815`
- 190 × 150 × 90 mm
- **249 SEK**

Source:
- https://www.clasohlson.com/se/Normkapsling-IP65%2C-8-moduler/p/36-1815

Extra cost is only ~99 SEK, so cramped mains wiring is never worth preserving the smaller box.

## Mains distribution inside the box

After KJD12, switched L and N each need to feed two loads:
- HDR-60-24
- DeWalt output lead

PE only connects:
- input PE
- DeWalt output PE

Three `Wago 221-413` three-conductor connectors are therefore sufficient:
- switched L: KJD12 output + HDR L + DeWalt-output L
- switched N: KJD12 output + HDR N + DeWalt-output N
- PE: input PE + DeWalt-output PE, third port unused

Wago 221-413 rating/current reference:
- flexible/solid conductors through 4 mm² class
- 32 A / 450 V class

Cheap local reference:
- Jula article `001480`
- 12-pack Wago 221-413
- **129 SEK**

Source:
- https://www.jula.se/catalog/el-och-belysning/elinstallation/installationsmateriel/kopplingslister-och-kopplingsklammor/kopplingsklammor-001480/

Only three are used; the remaining nine are useful general workshop stock. If genuine 221-413 are already owned, buy none.

## KJD12 terminals

KJD12 commonly uses 6.3 × 0.8 mm Faston tabs.

Use correctly crimped insulated female 6.3 mm receptacles matching the actual conductor area.

Cheap current reference:
- Biltema helisolerad 6.3 mm female Faston
- article `44-0020`
- 1.5–2.5 mm²
- **24.90 SEK / 10** on current catalogue

Do not solder directly onto the mains switch tabs; use proper removable crimp terminals.

## Cable entries / strain relief

Use real cable glands for the two 3G1.5 mains pigtails rather than relying on a loose hole/membrane.

Current reference:
- Jula/Rutab M20
- article `402070`
- IP68
- 2-pack
- **39.90 SEK**

Source:
- https://www.jula.se/catalog/el-och-belysning/elinstallation/installationsmateriel/kabelgenomforing/forskruvningar-402070/

The small 24 V cable to Jackpot3 can use an existing appropriately sized sealed enclosure entry if it provides real strain relief; otherwise add a smaller gland when the actual cable OD is known.

## Extra fuse / breaker?

No separate DIN MCB is part of the Pareto baseline.

Reason:
- the machine is a plug-connected appliance on an already protected Swedish branch circuit
- KJD12 / 3G1.5 / DeWalt path are all 10–16 A class
- HDR-60-24 includes its own electronic protection functions

Adding another generic 16 A MCB inside the box does not materially improve protection when the upstream circuit is already 10/16 A and would mainly add cost/space.

If later a smaller branch fuse is wanted specifically for auxiliary electronics, design it intentionally; do not add a duplicate breaker by habit.

## Estimated enclosure/distribution cost

Excluding the already separately budgeted **KJD12** and **HDR-60-24**:

- small IP65 DIN enclosure: 149.90 SEK
- 3 m 3G1.5 extension lead donor: 59.90 SEK
- 2 × M20 glands: 39.90 SEK
- Wago 221-413 12-pack: 129 SEK
- 6.3 mm insulated female Faston pack: ~24.90 SEK

Total if buying everything new:
- **~404 SEK**

If genuine Wagos/Faston/crimp supplies already exist in the workshop, the actual incremental cost can be closer to **~250 SEK**.

If the 8-module enclosure is needed instead of the compact one, add ~99 SEK.

## Safety / commissioning gate

This is mains voltage. The architecture is intentionally simple, but assembly quality matters more than cleverness.

Before energising:
- follow KJD12 terminal numbering/datasheet; never infer line/load from wire colour
- switch L and N through the two KJD12 poles as designed
- PE remains continuous and unswitched to the DeWalt output
- use correct crimp tooling for Faston terminals
- no bare copper/live terminal accessible with enclosure closed
- real strain relief on every cable
- continuity-test PE from wall-plug earth to female-socket earth
- verify no L/N-to-PE short
- verify KJD12 no-volt release before connecting router
- verify DeWalt AUTO operation with a small/test load before the router

If there is any uncertainty about mains assembly/testing, have the finished box checked/wired by someone competent with 230 V equipment. This is not a fixed-building-installation design guide.

## Decision

**Pareto baseline:**
- GDS Electric 3–5 module IP65 enclosure
- KJD12 on a side/end face after physical template check
- HDR-60-24 on included DIN rail
- donor 3 m 3G1.5 extension lead provides moulded input/output connectors
- Wago branch distribution
- M20 glands
- insulated 6.3 mm Faston terminals

Only move to the 8-module enclosure if the real dry-layout is cramped.
