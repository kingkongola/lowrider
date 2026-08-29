---
research_date: 2026-08-29
scope: electronics cart optimization after correcting LR4 endstop to SS-3GL13PT
status: recommendation-ready
decision_state: do not force DigiKey free-shipping threshold with filler; keep PSU and endstop sourcing separable until final checkout
price_basis: observed web prices on 2026-08-29; re-check at checkout
region: Sweden / EU
sources_checked:
  - V1 Engineering Jackpot3 documentation and 2026 forum wiring threads
  - DigiKey Sweden
  - Farnell Sweden
  - RS Sweden
  - Mouser Europe
supersedes: research/2026-08-29-electronics-cart.md where endstop cart assumptions used the older switch candidate
---

# Research: electronics cart after exact endstop correction

## Scope

Only these questions are answered here:
- should PSU + 5× exact `SS-3GL13PT` be one distributor order?
- is it rational to fill DigiKey's free-shipping threshold with wiring/connectors?
- what does Jackpot3 actually require at its power input?

## Verified Jackpot3 power facts

Current Jackpot3 documentation:
- accepts 9–24 VDC
- minimum required power about 19 W
- V1E's normal LR4 supply is 24 V / 2.5 A / 60 W class
- Jackpot3 uses a newer removable plug/socket power connector rather than the old Jackpot screw terminals
- the board ships with the mating screw-terminal plugs; user strips PSU wires and clamps them into the supplied plug, preferably with ferrules

A June 2026 LR4 build thread explicitly confirms that a round DC plug on a PSU can simply be cut off and the wires stripped into the supplied Jackpot3 connector.

Sources:
- https://docs.v1e.com/electronics/jackpot3/
- https://forum.v1e.com/t/jackpot-3-plug-type-for-24v-input-power/53181
- https://forum.v1e.com/t/new-build-in-east-tn-lr4/53962

### Consequence

The output connector style of a desktop PSU is **not** a compatibility blocker. A Mean Well `GST60A24-P1J` can have its 5.5×2.1 mm barrel plug cut off and the 24 V conductors terminated in the Jackpot3-supplied plug.

Do not buy an unnecessary barrel-to-Jackpot adapter.

## DigiKey freight economics

DigiKey Sweden currently states:
- free delivery at **615 SEK or more**
- **170 SEK** delivery fee below 615 SEK
- Marketplace products do not count toward the free-shipping threshold and may have separate freight

Source:
- https://www.digikey.se/sv/help-support/delivery-information/delivery-time-and-cost

## Exact endstops at DigiKey

`SS-3GL13PT`:
- ~10.05 SEK incl VAT each at qty 1
- 5 pcs ≈ **50.25 SEK incl VAT**
- tens of thousands shown in stock

Source:
- https://www.digikey.se/en/products/detail/omron-electronics-inc-emc-div/SS-3GL13PT/664729

## PSU candidates at DigiKey

### `LRS-100-24`

Observed:
- **178.25 SEK incl VAT**
- 24 V / 4.5 A / 108 W
- thousands in ordinary DigiKey stock

Source:
- https://www.digikey.se/sv/products/detail/mean-well-usa-inc/LRS-100-24/7705008

This is a normal DigiKey-stock item and therefore works normally toward shipping thresholds.

### `GST60A24-P1J`

Observed fresh DigiKey page:
- ~224.63 SEK incl VAT on one current listing
- 24 V / 2.5 A / 60 W
- current fresh page showed **0 ordinary stock** and Marketplace inventory

An older indexed Swedish page showed ordinary stock and ~214.53 SEK incl VAT, so inventory state is time-sensitive.

Because Marketplace products are excluded from DigiKey's free-shipping calculation, **do not design the cart around GST60A24-P1J being a DigiKey threshold filler unless ordinary stock returns**.

Source:
- https://www.digikey.se/en/products/detail/mean-well-usa-inc/GST60A24-P1J/7703715

## Wiring / terminal filler check

The exact Omron has 0.110 in / 2.8 mm quick-connect tabs, but V1E explicitly allows either:
- soldered wires, or
- small 2.8 mm female spade terminals

A good DigiKey terminal candidate is TE `60894-2`:
- female 0.110 in / 2.79 mm
- 18–22 AWG
- ~7.53 SEK ex VAT each at qty 1
- ~6.36 SEK ex VAT each at qty 10

Ten would cost roughly **80 SEK incl VAT**.

Source:
- https://www.digikey.se/en/products/detail/te-connectivity-amp-connectors/60894-2/385260

DigiKey also sells 2-conductor 22 AWG cable by length, but the indexed useful candidate is roughly 11.7 SEK incl VAT per ordered unit/foot. Buying ~6 m merely to push the cart toward free freight is worse value than ordinary flexible low-voltage cable from a cheaper/local source.

Source:
- https://www.digikey.se/en/products/detail/encore-wire/C6348A-46-10/2761061

### Decision on endstop terminations

Do **not** buy expensive quick-disconnects purely as freight filler.

For the LR4 baseline, either:
1. solder the two conductors directly to COM/NC and use heatshrink / strain relief, or
2. buy inexpensive correct 2.8 mm female terminals elsewhere when they naturally fit another order.

Both are technically valid. Soldering is the cheapest and avoids another connector failure point.

## Cart math

### DigiKey with open-chassis PSU

Approximate mandatory-item subtotal:
- `LRS-100-24`: ~178 SEK incl VAT
- 5 × `SS-3GL13PT`: ~50 SEK incl VAT
- subtotal: **~228 SEK**

This is far below the 615 SEK free-freight threshold.

Adding ~80 SEK of premium quick-connects and expensive distributor cable solely to chase free freight is not rational. The extra items would cost roughly as much as, or more than, simply accepting freight / sourcing elsewhere.

### External-brick route

Farnell currently lists `GST60A24-P1J` around **269.35 SEK ex VAT (~337 SEK incl VAT)** with the product page advertising free standard delivery on that item.

RS currently lists the same PSU around **250.90 SEK incl VAT** but its live page advertises free delivery only above the current order threshold; a standalone order therefore needs final freight checked.

Sources:
- https://se.farnell.com/mean-well/gst60a24-p1j/ac-dc-power-supply-24v-2-5a/dp/2815916
- https://se.rs-online.com/web/p/acdc-adaptrar/8808414

Farnell also carries exact `SS-3GL13PT`, but those switches currently show US stock and a **200 SEK per-order delivery charge**, so combining them with the Farnell PSU does not automatically create a good cart.

Source:
- https://se.farnell.com/omron-electronic-components/ss-3gl13pt/microswitch-roller-lever-spdt/dp/7300189

Mouser has both exact switches and `GST60A24-P1J`, but the PSU page explicitly states it is restricted to OEM/EMS/design customers in EU/UK, so it is not counted as a reliable consumer route.

## Current procurement decision

**Do not order this electronics slice yet.**

Current rules:
1. Do not fill DigiKey to 615 SEK with unnecessary premium cable/terminals.
2. Keep `GST60A24-P1J` as the preferred clean PSU architecture if delivered premium remains modest.
3. Keep `LRS-100-24` as the cheap fallback if the external brick's delivered price becomes too high.
4. Buy exact `SS-3GL13PT`; do not compromise actuator geometry to save freight.
5. If DigiKey becomes the unavoidable standalone endstop source, consider buying **10 switches rather than 5**: the qty-10 unit price is lower and five spare levers/switches are genuinely useful, while freight is unchanged. This should still be compared against other exact-model EU sources at checkout.

## Next research slice

Do not spend more time trying to game distributor thresholds yet. The higher-value next step is to research one of the remaining mandatory blocks:
- exact Jackpot3 purchase/delivery economics from Elecrow, or
- exact VEVOR 0700C current Sweden price/delivery, or
- final PLA bulk deal around 100 SEK/kg.

Those are larger line items and can change the total build cost more than saving tens of SEK on endstop terminals.