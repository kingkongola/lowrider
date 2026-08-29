---
research_date: 2026-08-29
scope: LR4 dust-system architecture: dust shoe, hose size, vacuum type, cyclone, hose support and static mitigation
status: recommendation-ready
decision_state: use the already-owned DeWalt shop-vac as primary extractor after cyclone; official-style 2.5 in moving hose + grounded hose + gantry strain relief; old FTX is a secondary-air-handling candidate only
price_basis: no final product cart yet; shop-vac is already owned
region: Sweden / EU
sources_checked:
  - current V1 Engineering LR4 documentation
  - V1 Engineering LR4 forum builds 2024–2026
  - LR4 dust-hose management threads
  - user-provided existing DeWalt shop-vac and old FTX inventory
supersedes: generic earlier dust-collection notes and any new-shop-vac purchase plan
---

# LR4 dust system architecture

This is a required subsystem for this build, not an optional future upgrade.

## 0. Existing hardware changes the plan

Already owned:
- DeWalt wet/dry grovdammsugare/shop-vac, originally about 2,500 SEK from Jula; exact model to identify
- old FTX heat-recovery ventilation unit; exact model/airflow to identify

**Do not buy a new vacuum.** The DeWalt is already in the product class that best suits an LR4 dust shoe.

The FTX is not a substitute for source extraction. It may later provide enclosure underpressure, purge or ambient filtration after primary dust capture.

## 1. Hose size — use the LR4-native 2.5 in class

Current V1E LR4 documentation specifies:
- **2.5 in vacuum hose**
- approximately **70 mm outside diameter** in the referenced hose class
- steel-ribbed hose is preferred/easy to ground

Source:
- https://docs.v1e.com/lowrider/

LR4 user reports confirm the current dust shoe is designed around the **2.5 in hose class**. Several users report 2.5 in hose fitting into the shoe but being slightly loose depending on the exact hose OD/print tolerance.

Sources:
- https://forum.v1e.com/t/dust-hose-to-shoe-attachment-lowrider-4/46895
- https://forum.v1e.com/t/lr4-vac-hose-fit-to-dust-shoe-boot/53006
- https://forum.v1e.com/t/lr4-dust-hose-management/48151

### Practical rule

Do not buy a smaller 40 mm / 1.5 in hose merely because it is common locally. It can be adapted and people do it, but it creates a needless restriction/adapter when the LR4 design already supports 2.5 in.

Do not put a 4 in hose directly on the moving LR4 either. That adds bulk/mass and can interfere with movement. If a future large dust collector is used, transition to 4 in **after the moving 2.5 in section**.

## 2. Vacuum type — existing DeWalt shop-vac is the Pareto default

For the 2.5 in moving hose and small router dust shoe, the V1E community consistently treats a shop-vac / wet-dry vacuum as a very good match.

A current 2026 LR4 discussion specifically notes that a shop-vac can be preferable to a big dust collector here because of its **higher air velocity / higher static pressure** through the smaller hose.

Source:
- https://forum.v1e.com/t/lowrider-v4/53926

### Recommendation

Baseline architecture:

`dust shoe -> short/flexible 2.5 in moving hose -> cyclone -> existing DeWalt shop-vac`

No vacuum purchase should occur until the DeWalt's exact model and port size have been checked.

## 3. Cyclone — strongly recommended

LR4 users running shop-vacs commonly place a cyclone before the vacuum.

Main benefit:
- most chips/dust drop into the cyclone bucket
- shop-vac filter loads much more slowly
- suction stays more consistent
- emptying becomes easier

A 2026 LR4 user describes shop-vac + cyclone as the preferred arrangement; another build uses a cyclone inline with a shop-vac successfully.

Sources:
- https://forum.v1e.com/t/lowrider-v4/53926?page=2
- https://forum.v1e.com/t/lr-3-lr-4-upgrade-in-appalachia-va/46123

Exact cyclone brand is **not locked**. Cheap bucket-top/Chinese cyclone designs may be perfectly adequate; product optimization comes later.

## 4. Hose flexibility matters more than premium branding

The moving LR4 section sees tight bends and must travel over the whole machine.

A 2026 LR4 user explicitly warns that the hose needs to be **very flexible** because of the tight turns.

Source:
- https://forum.v1e.com/t/lowrider-v4/53926?page=2

Therefore prioritize:
1. 2.5 in class / compatible OD
2. flexible enough not to pull the gantry
3. smooth enough internally to avoid needless pressure loss
4. groundable/steel spiral if possible
5. price

Do not choose a very stiff industrial hose just because it looks more durable.

## 5. Strain relief — the dust shoe must not carry hose load

This is critical.

Forum advice for LR4 explicitly says to **attach/support the hose at the gantry/core** instead of allowing hose tension to act on the dust shoe friction fit.

Once the hose is supported at the gantry, very little load remains at the shoe and loose-fit complaints become much easier to solve.

Source:
- https://forum.v1e.com/t/how-do-i-secure-the-hose-to-the-core/52229

### Recommended routing for this compact table

Use two stages:

1. **local strain relief at LR4 core/gantry**
   - printed hose holder / hook
   - leaves a short relaxed loop down to the dust shoe

2. **overhead swing/bungee/roller support** for the remaining moving hose
   - simple hinged swing arm, ceiling cord/rollers, or similar
   - should carry hose weight and prevent catching table edges

LR4 owners successfully use simple swing arms, ceiling rollers and magnetic connectors; no expensive drag chain is required for the vacuum hose.

Sources:
- https://forum.v1e.com/t/lr4-dust-hose-management/48151
- https://forum.v1e.com/t/lowrider-4-dust-collection-from-ceiling/48843
- https://forum.v1e.com/t/lr-3-lr-4-upgrade-in-appalachia-va/46123

## 6. Dust-shoe connection — adapter is normal, not a problem

Nominal “2.5 in hose” dimensions vary by manufacturer. LR4 users have found hoses 1–2 mm loose in the printed dust shoe.

Do not redesign the whole system for this.

Preferred fixes:
- print a short measured adapter
- add a threaded/magnetic quick-disconnect
- minor compliant strip/weatherseal if only a tiny fit correction is needed

Most important: remove hose tension from the shoe first.

## 7. Static electricity — ground the hose

Current V1E documentation explicitly warns that static can build in the vacuum hose and potentially damage control electronics.

V1E guidance:
- steel-ribbed hose: ground the metal rib at one end
- non-conductive hose: a grounding conductor can be run with/through the hose and grounded appropriately

Source:
- https://docs.v1e.com/lowrider/

### Build implication

For this garage, where XPS is also a likely material, choose a **steel-spiral / groundable hose if the price is sensible**. That simultaneously addresses the earlier XPS-static concern.

Do not rely on spraying the XPS with chemicals as the primary static strategy.

## 8. FTX role — secondary only

The old FTX unit may be useful if its model/airflow/filter setup is suitable.

Potential roles:
- draw a small continuous airflow from a curtain enclosure to create underpressure
- recirculate garage air through a large prefilter/fine filter as an ambient cleaner
- purge dirty enclosure air after a job

Do **not** feed raw router chips/XPS debris through the FTX heat exchanger/fans. Primary capture remains dust shoe + cyclone + DeWalt.

## 9. Enclosure/curtain remains separate

The dust shoe is the first line of defence, not the only line.

Because this CNC shares space with mechanical/engine work, the later table design should still allow an **easy-wipe transparent curtain or local enclosure** around the CNC zone.

This file does not choose the curtain material/product yet.

## Locked architecture

For product research, assume:

- official/current LR4-compatible dust shoe for 65 mm Makita-style router mount
- **2.5 in flexible vacuum hose**, preferably clear/groundable steel spiral
- hose strain-relieved at the LR4 core/gantry
- simple overhead support/swing arm
- **cyclone separator + bucket/container**
- **existing DeWalt shop-vac / wet-dry vacuum**
- hose static grounding from day one
- old FTX evaluated only for secondary fine-air / underpressure duty
- wipeable CNC-zone curtain/enclosure added as table subsystem

## Next procurement block

Do not research a new vacuum. Instead:
1. identify DeWalt model/port from the label
2. optimize cyclone + bucket
3. optimize the minimum necessary 2.5 in flexible steel-ribbed hose and adapters for our ~1.0×1.62 m table
4. identify FTX model and airflow before deciding whether a separate enclosure/ambient fan is needed

Optimization objective: reuse owned equipment first, then spend only on the missing interfaces/primary separator.
