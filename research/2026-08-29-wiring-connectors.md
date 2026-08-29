---
research_date: 2026-08-29
scope: LR4 motor wiring, endstop wiring and connector strategy for selected StepperOnline motors + Jackpot3
status: recommendation-ready
decision_state: defer stepper extensions; dry-fit the selected 1 m motor leads first; build/buy endstop wiring separately
price_basis: observed web prices/specifications on 2026-08-29; re-check at checkout
region: Sweden / EU
sources_checked:
  - V1 Engineering LR4 documentation
  - V1 Engineering Jackpot3 documentation
  - V1 Engineering wiring/endstop products
  - StepperOnline exact 17HS19-2004S1 product page
  - V1E forum LR4 wiring discussions 2024-2026
  - Farnell Sweden cable catalogue
  - LaskaKit connector/cable catalogue
supersedes: null
---

# Research: wiring + connectors

Scope intentionally limited to:
- stepper motor leads/extensions
- endstop wiring
- board-side connectors

## Verified baseline from V1E

V1E's standard LR4 kit uses:
- 3 × stepper extension looms
- each V1 extension is 1.5 m, 22 AWG, six conductors so motor + endstop wiring can be routed together
- 5 × endstop wires
- controller mounted on the **YZ_Min** side is recommended because it makes wiring easiest
- extensions are specifically called out from **YZ_Max** and from the **Core** back to the controller

V1's current endstop plug kit for LowRider uses:
- 5 sets
- 1200 mm wire length
- 2-pin pre-crimped DuPont-style board connector
- switch end is left for small spade/crimp connection

Sources:
- https://docs.v1e.com/lowrider/
- https://www.v1e.com/products/wiring-kit-1
- https://www.v1e.com/products/endstop-plug

## Important optimization caused by our selected motors

Selected motors: StepperOnline `17HS19-2004S1` / 5-pack `5-17HS19-2004S1`.

Exact product page verifies each motor already has:
- **1 m motor cable**
- **4-pin 0.1 inch / 2.54 mm Harwin female connector** at the cable end
- wire/pin order listed as blue, red, green, black in current forum testing of this exact motor

Jackpot3 uses:
- **open 2.54 mm male headers** for stepper outputs, explicitly chosen to fit more plug styles

Therefore the selected StepperOnline motor plug is mechanically compatible with the Jackpot3's open 2.54 mm stepper header and does not require a JST conversion just to connect to the controller.

Sources:
- https://www.stepperonline.nl/5st-nema-17-bipolair-59ncm-83-55oz-in-2a-42x48mm-4-draden-met-1m-kabel-aansluiting-5-17hs19-2004s1
- https://docs.v1e.com/electronics/jackpot3/
- https://forum.v1e.com/t/new-lowrider-control-issue/50909/5

## Do we actually need three 1.5 m extensions?

Maybe not.

This is a project-specific inference, not a V1E standard recommendation.

Our current usable X target is 650 mm. V1's calculator gives an X strut length of roughly 819 mm (`ceil(650 + 169)`). With the controller in the recommended YZ_Min bay:
- YZ_Min motors are local and clearly do not need extra stepper extension
- YZ_Max is roughly one gantry width away; the selected motors already provide 1000 mm cable
- Core X travel is only ~650 mm usable and its selected motor also has 1000 mm cable

The stock V1 extension recommendation assumes the generic/V1 motor lead arrangement and is designed to cover much larger machines, including full-sheet builds. V1 forum users note the 1.5 m extensions are slightly longer than needed even on a full-sheet LR4 when routed conventionally.

Because our motors unusually include a full 1 m lead, **buying three additional 1.5 m motor extensions now risks paying for cable we do not need.**

### Decision

**Do not buy stepper extension cables yet.**

When the motors and printed gantry exist:
1. Mount Jackpot3 in the recommended first bay at YZ_Min.
2. Route the native 1 m StepperOnline cables exactly as the V1 docs show.
3. Move Core and Z through full travel.
4. Require a relaxed service loop and zero connector strain at every extreme.
5. Only extend whichever motor lead actually fails this test.

This preserves V1's strain-relief requirement while exploiting the 1 m cables we are already paying for.

Sources supporting routing/length context:
- https://docs.v1e.com/lowrider/
- https://forum.v1e.com/t/advice-on-wiring-lengths/46760

## Endstop wiring is separate and still required

The five Omron `SS-5GL2` switches selected in the previous research do not eliminate the need for wiring.

Jackpot3 input behavior:
- inputs are active-low
- signal `S` is activated by connection to ground `G`
- V1 CNC standard is **Normally Closed (NC)** endstop wiring
- Jackpot3 endstop plug is a **2-pin** connection in normal LR4 use

Sources:
- https://docs.v1e.com/electronics/jackpot3/
- https://forum.v1e.com/t/limit-switch-plugs/54032

### Practical DIY endstop loom

A clean local-EU build can use:
- ~6 m total of flexible **2-core stranded copper** cable, 22-24 AWG class
- five 2-pin 2.54 mm DuPont-style female connectors/pigtails at Jackpot3
- solder + heatshrink directly to the Omron switch terminals, or correctly sized small female spade terminals

V1's own LR4 endstop set uses 5 × 1.2 m = 6 m total, so 6 m is a sensible procurement quantity and leaves the individual runs to be cut to actual routing length.

For endstop signal current, 24-26 AWG is electrically sufficient; V1/community generally uses/recommends 22 or 24 AWG stranded copper for robust machine wiring. Avoid CCA (copper-clad aluminium).

Sources:
- https://www.v1e.com/products/endstop-plug
- https://forum.v1e.com/t/wiring-touchplate-sourcing-correct-parts/51712
- https://forum.v1e.com/t/new-build-lr3/36163

## Candidate sources / cart implications

### Farnell

Farnell has suitable 2-core copper cable by the metre. One verified example:
- Alpha Wire `B954021`
- 2 core
- 22 AWG / ~0.32 mm²
- tinned copper
- flexible PVC cable
- observed ~32.02 SEK/m at 1 m quantity, ~30.95 SEK/m at 5+

Six metres would therefore be roughly 186 SEK ex VAT before considering cart freight. This is technically excellent but not a cheap commodity-wire choice.

It may become rational **only if** Farnell is already selected for exact Omron endstops + Mean Well PSU and the cable helps cross a useful shipping threshold.

Source:
- https://se.farnell.com/c/cable-wire-cable-assemblies/multicore-cable?brand=alpha-wire&no-of-cores=2core

### LaskaKit

Useful connector items:
- 2.54 mm DuPont housings from ~€0.03
- crimp pins ~€0.03
- 70 cm 2-pin female-female cable `LA150058`, 26 AWG, ~€0.58, but current listing was out of stock / restock pending
- bulk 40-piece 70 cm 2-pin F/F set `LA150090`, €6.11, in stock when observed, but gross overkill for five endstops

LaskaKit is already the leading mechanical cart. Tiny housings/pins can be added essentially for free if we decide to crimp our own, but buying an unnecessary 40-cable set purely for consolidation is not optimal.

Sources:
- https://www.laskakit.cz/en/dupont-konektor/
- https://www.laskakit.cz/en/propojovaci-kabel-f-f--70cm-2pin-2-54/
- https://www.laskakit.cz/en/propojovaci-kabely-f-f-40ks-2pin-samice-samice--70cm/

## Connector/crimping recommendation

Do not buy an expensive dedicated crimping tool solely for this LowRider if it can be avoided.

Preferred order of operations:
1. use the StepperOnline motors' factory 2.54 mm connectors directly on Jackpot3
2. dry-fit native 1 m motor leads before buying extensions
3. for endstops, use cheap pre-crimped 2-pin DuPont pigtails and splice/solder them to flexible 2-core cable, or use an existing suitable DuPont crimper if already available
4. solder + heatshrink at Omron switches is acceptable and avoids tiny spade-terminal sourcing
5. secure every connector mechanically so repeated gantry motion does not load the contact

The V1 community repeatedly describes the factory V1 extension cables as convenient mainly because tiny connector crimping is annoying, not because there is special signalling electronics in the cable.

Sources:
- https://forum.v1e.com/t/electronic-and-tools-sourcing-helping-a-begginer/44093
- https://forum.v1e.com/t/where-to-buy-end-stop-wiring/50179

## Decision summary

**Locked/near-locked:**
- StepperOnline motor's factory 4-pin 2.54 mm connector is compatible with Jackpot3's open stepper headers.
- Mount controller at YZ_Min as V1 recommends.
- Endstops are wired NC to Jackpot3 S/G.
- Endstop cable should be flexible stranded copper, not CCA.

**Recommendation:**
- **do not order the three standard stepper extensions yet**; exploit the selected motors' native 1 m cables and dry-fit first.
- plan a simple five-run endstop loom using ~6 m of 2-core 22-24 AWG copper + 2-pin DuPont pigtails.

**Still open:**
- cheapest sensible source for ~6-10 m of flexible 2-core copper cable
- whether cable is cheapest as Amazon/local commodity purchase or worthwhile inside the final Farnell electronics cart

This is a deliberate example of cart optimization: the motor choice changes what wiring we actually need, so blindly copying the standard BOM would likely create unnecessary purchases.
