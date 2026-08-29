---
research_date: 2026-08-29
scope: machine mains power, emergency stop / NVR and controller PSU interaction
status: recommendation-ready
decision_state: use HDR-60-24 inside the eventual machine control/NVR enclosure; machine-level stop must remove energy from router and controller; final E-stop switching hardware remains open
price_basis: observed web prices 2026-08-29; re-check before purchase
region: Sweden / EU
sources_checked:
  - V1 Engineering Jackpot3 documentation
  - Mean Well HDR-60-24 current distributor data
  - E-Switch KJD17 datasheet
  - Farnell and DigiKey Sweden
  - ABB emergency-stop catalogue
  - KJD17-D2 reference
supersedes: prior version of this file where GST60A24-P1J remained the preferred PSU architecture
---

# Machine power + stop architecture

## Electrical baseline

Jackpot3 accepts 9–24 VDC and V1 normally uses a 24 V / 2.5 A / 60 W-class supply for LowRider.

Source:
- https://docs.v1e.com/electronics/jackpot3/

## PSU is now locked separately

Chosen controller PSU:
- Mean Well **`HDR-60-24`**
- 24 V / 2.5 A / 60 W
- DIN rail
- universal mains input

Current DigiKey part:
- `1866-2249-ND`

See:
- `research/2026-08-29-final-psu-endstop-wiring-cart.md`

### Why this changes the enclosure architecture

The old comparison treated an external `GST60A24-P1J` brick as attractive because it removed exposed mains terminals from the CNC electronics.

That is no longer the best current procurement/design trade:
- `HDR-60-24` is enclosed/touch-protected DIN equipment rather than an open-frame LRS supply
- it is substantially cheaper in the current Swedish sourcing path
- a machine-level NVR/stop enclosure is required anyway if router and motion are to shut down together

Therefore the controller PSU should live inside that eventual control/power enclosure rather than creating a separate desktop-brick architecture.

## Machine-level stop goal

A useful machine stop must remove energy from both:
1. Jackpot3 / steppers, and
2. the 230 V router.

Stopping motion while leaving the router energized is not the desired finished design.

Approximate nominal mains load remains modest:
- router ~800 W, about 3.5 A at 230 V nominal
- 60 W controller supply, well under 0.5 A mains-side nominal

This is comfortably below a 16 A machine-switch class, but component utilization ratings and switching duties still matter.

## NVR/no-volt release remains required

The finished machine should not automatically restart after a mains interruption.

Leading NVR family remains E-Switch KJD17.

Relevant variants:
- `KJD17-21413-112`: guarded Off-On NVR
- `KJD17-22413-112`: guarded Off-On NVR with remote-trip function

The remote-trip version is interesting for later enclosure/guard interlocks.

## Remote trip is not the E-stop by itself

Do not treat the KJD17 A1/remote-trip loop as the sole emergency-disconnect architecture.

Remote trip is useful for an interlock, but the final large emergency mushroom should participate in a credible circuit that de-energizes the machine switching element / upstream power path rather than merely sending a low-authority signal.

## Candidate architecture

Current preferred functional layout:

`230 V wall -> proper emergency disconnect/switching path -> NVR -> switched router + HDR-60-24 -> Jackpot3`

This gives:
- router and controller on the same machine-level shutdown path
- no automatic restart after mains loss
- simple 24 V DIN PSU integration
- possible future guard/interlock use

## E-stop hardware remains intentionally open

Earlier research identified a credible ABB mushroom reference:
- ABB `CE3T-10R-02`, `1SFA619500R1051`
- red twist-release mushroom
- 2 NC
- industrial/certified pilot-device family

But a pilot device's contacts must not automatically be assumed suitable to interrupt the full router load directly. A conventional industrial pattern is to use the safety contact to de-energize an appropriately rated switching element.

A complete NVR + mushroom station remains attractive if a credible EU product with clear ratings can be found cheaply.

## What is locked vs open

Locked:
- PSU = **HDR-60-24**
- NVR/no-restart behavior required
- machine shutdown must remove power from router + controller together
- do not use a cheap unverified marketplace mushroom as the sole safety device
- do not call the KJD17 remote-trip input alone a finished E-stop

Open:
- exact final NVR + mushroom + contactor/switching product combination
- exact enclosure/outlet arrangement
- whether a credible complete station beats building the power box from DIN components

## Procurement sequencing

Do not let the unfinished E-stop box block the low-voltage electronics orders.

Order HDR-60-24 with the exact endstops as documented in the final electronics cart. The HDR integrates cleanly into any of the plausible final machine-power architectures.

Then solve the mains/NVR/E-stop enclosure as its own final safety block before routine CNC use.