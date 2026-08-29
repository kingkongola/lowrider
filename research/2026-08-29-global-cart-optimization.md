---
research_date: 2026-08-29
last_updated_at: 2026-08-29
scope: global cart optimization across all remaining LR4 purchases after assembly-manual audit
status: recommendation-ready
decision_state: consolidate HDR, Omron, 608 bearings, Wago, M20 glands and Faston terminals into DigiKey to cross free-shipping threshold with only genuinely needed parts; keep LaskaKit mechanical/wiring cart intact; keep motors-only StepperOnline Germany; 16T remains orphan checkout item; no threadlocker purchase
price_basis: current indexed prices checked 2026-08-29; checkout totals remain authoritative
region: Sweden / EU
sources_checked:
  - DigiKey Sweden exact HDR-60-24, SS-3GL13PT, 608-2RS, Wago 221-413, Altech M20 glands, TE Ultra-Fast 250 terminals and delivery threshold
  - LaskaKit current mechanical/wiring cart
  - StepperOnline current Germany-warehouse motor listing
  - VEVOR 0700C
  - Elecrow Jackpot3
  - current exact Allegro 16T listing
  - current KEDU KJD12 EU listings
supersedes: DigiKey ~495 SEK HDR+Omron-only cart and separate Tradera/Jula 608/Wago/gland plan
---

# Global cart optimization — 2026-08-29

## Principle

Optimize delivered build cost, not isolated component prices. Move small required parts into already-needed carts when that removes a shipping charge without creating variant risk.

## Main improvement: DigiKey becomes the electrical + bearing consolidation cart

### Exact cart

1. Mean Well `HDR-60-24` ×1
   - current incl-VAT reference: ~242.75 SEK
2. Omron `SS-3GL13PT` ×10
   - qty-10 current incl-VAT total: ~82.73 SEK
3. Mechatronics Bearing Group `608-2RS-W/CHEVRONSRI2` ×16
   - exact 8×22×7 mm, two contact seals
   - qty-10 tier applied; ~180 SEK incl VAT for 16
   - 14 installed + 2 spare
4. Wago `221-413` ×3
   - ~27.5 SEK incl VAT total
5. Altech `5309 720/SET` M20×1.5 IP68 cable gland ×2
   - 5–12 mm cable OD, locknut included
   - ~40.65 SEK incl VAT total
6. TE Connectivity `3-350820-2` Ultra-Fast 250 fully insulated female receptacle ×10
   - 6.35×0.8 mm / 0.250×0.032 in
   - 14–16 AWG
   - ~48.1 SEK incl VAT at qty-10 tier

Expected cart total: roughly **622 SEK incl VAT**.

DigiKey Sweden free-shipping threshold is **615 SEK**. Therefore this cart gets free delivery instead of paying the prior 170 SEK small-order freight.

### What this replaces

Remove from separate/local shopping:
- Tradera/Fyndiq/Kullager.se 608 purchase
- Jula Wago pack
- Jula M20 gland pack
- Biltema Faston pack

This is a genuine cart optimization, not filler buying: every added line is already required, except that quantities include modest useful spares.

## LaskaKit remains correctly consolidated

Keep together:
- 6× exact smooth 10 mm GT2 idlers
- 1× T8×8 400 mm rod
- 2× T8×8 brass nuts
- 2× 5→8 couplers
- 1× 5 m 10 mm fiberglass GT2 belt
- 10 m endstop cable
- ~1 m 20 AWG 2-core PSU-output cable
- board-side connector/pigtail solution

Do not move bearings or Wago here merely to reduce parcel count; DigiKey now has better total economics.

## StepperOnline remains motors-only

Keep 5-pack `5-17HS19-2004S1` from Germany warehouse. Germany warehouse explicitly ships to Sweden.

Do not add China-only parts to this cart.

## 16T pulleys remain the only real mechanical orphan

Need 3× exact:
- GT2
- 16T
- 5 mm bore
- 10 mm belt

Preferred exact Allegro part remains `GT2-16T-5B_10mm_K`, dual grub screws. Buy if Sweden-delivered total is <=150–180 SEK. If freight is poor, change seller only, not spec.

DigiKey's indexed 16T pulley is a 6 mm-belt part and is wrong for LR4, so it must not be added merely to consolidate.

## Local carts after consolidation

### Motonet
- only the two Ø30×1.5×2000 mm tubes
- inspect OD/straightness before accepting

### Biltema
Likely remaining useful combined pickup:
- IP65 4-module enclosure `35-0065`
- 3 m grounded 3G1.5 donor extension cord `46-3610`

Wago, cable glands and Faston terminals are no longer needed from local stores if DigiKey cart is used.

## KJD12

A current genuine KEDU KJD12 EU listing exists at CEM Elettromeccanica for €14.90 incl VAT:
- KEDU branded
- bipolar
- emergency-stop mushroom/cover
- 15 A / 230 V
- IP54
- 6.3×0.8 Faston terminals
- VDE/TUV approvals

Shipping to Sweden is not exposed in indexed content, so final delivered price remains checkout-gated. Compare this exact genuine EU part against the ~482 SEK Swedish IKH fallback. If EU delivered total is materially below 500 SEK, genuine KEDU wins.

## Threadlocker

No threadlocker purchase. Existing threadlocker will be used. User believes one bottle is Loctite 270. Do not add Loctite to any cart.

## Table correction

180 cm is not required. Locked minimum LR4 table length is 1563 mm and practical removable deck is ~1620 mm.

Therefore the used-base target should be:
- **160–180 cm long**
- preferably 90–100 cm deep
- 160×90 is valid if the table is stiff; the ~1620 mm deck only overhangs ~10 mm at each short end
- 170×90 is excellent
- 180×90/100 remains convenient/common, not mechanically required

## Current optimized parcel architecture

1. HaWiWe — already paid
2. Motonet — rails, local pickup
3. LaskaKit — mechanical + low-voltage wiring
4. StepperOnline Germany — motors only
5. DigiKey — HDR + Omron + 608 + Wago + M20 glands + Faston, ~622 SEK / free shipping
6. VEVOR — router
7. Elecrow — Jackpot3
8. SUNLU — PLA
9. Sorotec — commissioning cutters
10. Allegro/other exact source — 3×16T orphan
11. KEDU seller — KJD12
12. Biltema — enclosure + donor power cord
13. used local table + deck/spoilboard material

Further parcel reduction is not itself a goal. Only consolidate again if it lowers delivered total without weakening exact-spec confidence.