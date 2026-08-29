---
researched_at: 2026-08-29
scope: machine mains power, emergency stop / NVR, controller PSU interaction
status: researched-not-ordered
confidence: medium-high
machine_target: LowRider V4, ~650x1250 mm usable area
constraints:
  - dust-prone garage
  - VEVOR 0700C router ~800 W
  - Jackpot3 controller at 24 VDC
  - prefer low complexity and low delivered cost
  - emergency stop should stop both router and motion if practical
sources_checked:
  - V1 Engineering Jackpot3 docs
  - V1 Engineering 24 V PSU page
  - Farnell Sweden
  - DigiKey
  - RS Sweden
  - Kew Online / KJD17-D2 reference
observed_prices_are_time_sensitive: true
---

# Research: machine power + stop architecture

This slice intentionally covers only the 230 V machine-power architecture and stop behavior. It does **not** specify the complete electronics enclosure yet.

## Electrical facts from V1E

Jackpot3 accepts **9–24 VDC** and requires at least about **19 W**. V1E's normal LowRider supply is **24 V / 2.5 A / 60 W or larger**.

Jackpot3 has a revised power plug/socket rather than the old screw-terminal power input. The board has no need for a mains supply inside its printed board box.

Sources:
- https://docs.v1e.com/electronics/jackpot3/
- https://www.v1e.com/products/24v-power-supply

## Important design goal

A useful stop should remove energy from **both**:
1. the 24 V motion controller / steppers, and
2. the 230 V router.

Stopping only Jackpot3 while leaving the router spinning is not the preferred machine-level stop architecture.

## Candidate architecture A — NVR machine switch upstream of both router and PSU

A no-volt-release (NVR) machine switch is attractive because it combines:
- machine ON/OFF switching
- power-failure dropout
- mandatory manual restart after power returns
- sufficient current rating for router + 24 V PSU

### Strong EU candidate: E-Switch KJD17 series

Farnell Sweden lists `KJD17-22413-112` / `KJD17-21413-112` class devices with:
- DPST
- 230 VAC
- 16 A
- industrial pushbutton construction
- IP54
- electromagnetic no-voltage-release behavior
- automatic dropout on mains failure, so the machine does not unexpectedly restart

Observed Farnell price for `KJD17-22413-112`: **134.04 SEK ex VAT** (~167.55 SEK incl VAT) before final cart/shipping.

DigiKey also lists KJD17 variants around **133–150 SEK incl VAT** depending exact variant/market.

Sources:
- https://se.farnell.com/e-switch/kjd17-22413-112/pb-switch-dpst-16a-230v-panel/dp/4051018
- https://se.farnell.com/e-switch/kjd17-21413-112/pb-switch-dpst-16a-230v-panel/dp/4051016
- https://www.digikey.se/en/products/detail/e-switch/KJD17-21413-112/4028288

### Load margin

Approximate running load:
- VEVOR 0700C router: ~800 W => ~3.5 A at 230 V nominal
- 24 V / 60–100 W controller PSU: <0.5 A mains-side nominal

Total nominal running current remains far below a 16 A KJD17 rating.

This gives much more switching margin than small 230 V emergency-stop contact blocks rated only around 4–6 A in AC-15 service.

## Candidate architecture B — enclosed KJD17-D2 with separate mushroom emergency stop

A known complete workshop-machine solution is `KJD17-D2`:
- 220–240 V
- 16 A
- NVR start/stop
- separate emergency-stop button
- two NC emergency contact blocks rated 12 A / 250 V on the referenced product
- complete enclosure around 80×115×90 mm

Observed reference price: **£15.90** from Kew Online before Sweden shipping/import handling.

This is functionally very attractive, but the verified seller found is UK-based. Post-Brexit Sweden delivery economics are therefore currently worse/less predictable than buying an EU-distributed KJD17 switch.

Source:
- https://www.kewonline.net/store/product/a-nvr-no-volt-release-stopstart-emergency-stop-switch-kjd17-d2

## Candidate architecture C — generic panel mushroom directly switching mains

Rejected as first choice.

A certified mushroom can switch mains, but the good industrial units become surprisingly expensive. For example, RS PRO emergency-stop modules are properly rated/certified, but an individual unit is often far more expensive than the KJD17 NVR approach.

A cheap generic 22 mm mushroom from marketplace sellers can claim 10 A / 230–440 V, but switching ratings, positive-opening behavior and build quality are harder to trust.

Therefore **do not optimize the machine stop by buying the cheapest red mushroom button**.

Sources:
- https://se.rs-online.com/web/p/emergency-stop-push-buttons/2420839
- https://se.rs-online.com/web/p/nodstoppknappar/2420837

## PSU implication

This research changes the PSU preference slightly.

### Cleaner architecture

If we use an **external 24 V brick** such as Mean Well `GST60A24-P1J`, the mains side can remain extremely simple:

`wall -> NVR machine switch -> two switched 230 V outlets -> router + 24 V brick`

Advantages:
- no open 230 V PSU terminals inside the CNC electronics enclosure
- one machine switch removes power from both router and controller
- easier to keep mains wiring physically separate from Jackpot3/endstop wiring
- easier service/replacement

### Cheaper architecture

Using `LRS-100-24` remains electrically good and cheaper, but then its exposed mains terminals require a proper enclosed mains section. That partly erodes its ~50–100 SEK price advantage once enclosure, terminals and extra wiring are counted.

**Updated decision rule:** prefer the external `GST60A24-P1J` if delivered total remains within roughly **100–150 SEK** of the complete, safely-enclosed `LRS-100-24` solution.

## What is actually needed in the mains box

For a minimal build using external 24 V brick:
- 1 × industrial NVR machine switch, DPST, 230 V, >=10 A; KJD17 16 A is leading candidate
- grounded 3-core incoming flex + strain relief
- protective earth continuity to downstream sockets / any metal enclosure
- 2 switched grounded outlets (or an equivalent properly enclosed output arrangement)
- insulated enclosure / panel suitable for the switch and terminals

Not automatically needed:
- DIN rail
- contactor
- separate relay
- separate internal 230 V fuse, provided the selected devices are correctly rated and supplied from a normally protected Swedish socket circuit; final wiring still follows component requirements
- 24 V case fan unless Jackpot3 thermal testing shows a need

V1E states case fans are optional; if used they are normally 24 V and hardwired to board input power.

Source:
- https://docs.v1e.com/electronics/jackpot3/

## Current recommendation

**Leading architecture:**

Use a 16 A, 230 V **NVR machine switch upstream of both router and controller PSU**. This is simpler and more useful than a low-voltage-only E-stop.

Preferred sourcing direction:
1. EU-distributed E-Switch KJD17 from Farnell/DigiKey if a suitable guarded/large-stop physical actuator is confirmed.
2. KJD17-D2 complete NVR + mushroom enclosure only if final delivered Sweden cost is competitive.
3. Avoid no-name standalone mushroom switches merely to save tens of SEK.

## Remaining verification before order

- inspect exact KJD17-21413 vs 22413 actuator/guard geometry and choose the version easiest to hit quickly
- check whether an EU seller has a complete enclosed KJD17-D2-equivalent at sensible delivered price
- price the final switched outlet/enclosure arrangement
- compare total system cost for `GST60A24-P1J + simple NVR box` versus `LRS-100-24 + larger mains/electronics enclosure`

No machine-power parts should be ordered from this file alone until those four points are resolved.
