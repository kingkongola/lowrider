# Order optimization matrix — 2026-08-30

Goal: minimize total landed cost, not simply order count.

Objective:
`parts + shipping + taxes/import + expected wrong-part/reorder cost + small handling penalty per extra order`

Hard rule: do not change a locked technical spec only to reduce package count.

## Mechanical bundle candidates

| Part group | Required | LaskaKit | Roboter-Bausatz | Notes |
|---|---:|---:|---:|---|
| Smooth idler | 6 × 5 mm bore / 10 mm belt | LA190008E ~€1.86 ea | RBS12910 ~€1.49 ea at qty 6 | Both match |
| T8 lead screw | 1 × T8×8 400 mm | LA190032A ~€8.15 | RBS12872 €10.85 incl 1 brass nut | Both match; RBS bundle includes one nut |
| Brass nut | 2 total | LA190033A ~€1.31 ea | RBS12872 includes 1 + RBS12749 €1.67 | Both match T8×8 / 2 mm pitch / 8 mm lead |
| 5→8 coupler | 2 | LA190031 ~€1.81 ea | RBS10595 €1.75 ea | Both match |
| GT2 belt | ≥4409 mm continuous as 999/1705/1705 | LaskaKit direct product pages show conflicting/stale stock; 2 m/5 m not reliable enough to build plan around | RBS12747, 10 mm rubber + fiberglass, 5 m ≈ €11.25 | RBS currently cleanest verified source |
| GT2 drive pulley | 3 × 16T / 5 mm / 10 mm belt | no verified exact LaskaKit consolidation candidate | RBS12867, exact, currently ~€0.88–1.25 ea depending live sale/tier | RBS clearly wins |
| Sweden freight | — | €8.93 GLS | €14.99 DHL | fixed published rates |

### Mechanical conclusion

If LaskaKit is used for mechanics, belt + 16T still require another source/order. That loses the €6.06 shipping advantage very quickly.

Roboter-Bausatz can supply **all six mechanical line groups in one order**. Even with higher €14.99 Sweden shipping, this is currently the strongest consolidated mechanical basket.

Approximate RBS basket before shipping, using current retail/tier prices:
- 6 idlers: ~€8.94
- T8×8 400 + 1 nut: €10.85
- extra nut: €1.67
- 2 couplers: €3.50
- 5 m belt: €11.25
- 3 drive pulleys: ~€2.64–3.75
- merchandise: ~€38.85–39.96
- Sweden freight: €14.99
- landed before any payment-specific surprises: **~€53.84–54.95**

This eliminates the previous LaskaKit + separate belt + Allegro structure.

## Electronics / electrical matrix

| Part group | Preferred | Why not move it? |
|---|---|---|
| HDR-60-24 | DigiKey | exact Mean Well, known source |
| 10 × Omron SS-3GL13PT | DigiKey | exact switch is locked; do not replace with generic/other Omron merely for consolidation |
| 16 × 608-2RS | DigiKey | already helps shipping threshold and exact 8×22×7 spec |
| Wago 221-413 | DigiKey | genuine parts, tiny marginal shipping cost inside basket |
| M20 glands | DigiKey | already in same mains basket |
| TE Faston | DigiKey `A27824-ND` | ordinary DigiKey stock; avoid Marketplace duplicate |
| M12 LV gland | DigiKey `AIO-CSM12` | exact 3–6.5 mm range fits ~4.8 mm cable and usefully pushes basket above shipping threshold |
| 24 V 2-core cable | DigiKey or local, whichever is cheaper without creating an order | generic spec; must not justify a separate LaskaKit order |
| Endstop cable | DigiKey or local, whichever is cheaper without creating an order | generic 2/3-core low-voltage cable; no need for separate seller |

Current DigiKey basket estimate from live prices: **~641 kr incl VAT** after adding AIO-CSM12. DigiKey publishes free Sweden shipping at **≥615 kr**, 170 kr below. Checkout remains authoritative, but the basket now clears the published threshold on its displayed total without filler.

## Supplier matrix — remaining unique parts

| Supplier | Unique/strong reason to exist | Current state | Consolidation verdict |
|---|---|---|---|
| Roboter-Bausatz | complete mechanical bundle | strong | KEEP — replaces LaskaKit + belt seller + Allegro |
| DigiKey | PSU + exact Omron + bearings + mains small parts | strong | KEEP |
| StepperOnline Germany | exact 5-pack 5-17HS19-2004S1 | ~$41.90 / ~€41 class, Germany warehouse | KEEP unless identical motors appear materially cheaper elsewhere |
| Elecrow | Jackpot3 CQA240812C2 | $76.99 | KEEP — unique board |
| VEVOR | 0700C 800 W / 65 mm router | unique chosen router | KEEP |
| SUNLU | 6 kg ordinary PLA bulk | ~€9.99–11.99/kg depending live variant; free shipping to most EU stated | KEEP unless Swedish delivered filament beats it |
| Sorotec | L1S.M.0317 commissioning cutters | €3.70 ea, 3 needed | QUESTION — separate freight may dominate €11.10 merchandise |
| CEM/eBay | genuine KEDU KJD12-14 with correct actuator | exact safety-critical provenance | KEEP unless same exact genuine variant can join another order |
| Motonet | Ø30×1.5 tubes local pickup | physical inspection valuable | LOCAL, not shipping-order problem |
| Biltema | enclosure/donor lead, local | buy after dry-fit | LOCAL |
| used table/material | local | physical inspection | LOCAL |

## Order-count scenarios

### Old fragmented plan
- LaskaKit
- separate GT2 belt
- Allegro pulleys
- DigiKey
- StepperOnline
- Elecrow
- VEVOR
- SUNLU
- Sorotec
- KEDU

≈ **10 shipped orders**, before local purchases.

### Current optimized baseline
1. **Roboter-Bausatz** — entire mechanical bundle
2. **DigiKey** — electronics/electrical small parts + absorb generic cable if sensible
3. **StepperOnline Germany** — motors
4. **Elecrow** — Jackpot3
5. **VEVOR** — router
6. **SUNLU** — PLA
7. **KEDU/CEM** — NVR/machine stop
8. **Sorotec only if its delivered total beats a suitable cutter absorbed elsewhere**

= **7 mandatory shipped orders + 0/1 cutter order**.

Local purchases (Motonet/Biltema/table/deck/spoilboard) are not treated as shipping orders.

## Biggest remaining optimization opportunity

**Sorotec** is the obvious next target. Merchandise is only €11.10 for three cutters, so a separate international freight charge can dominate. Search for an equivalent 3.175 mm single-flute upcut cutter from Roboter-Bausatz, VEVOR, Amazon Prime Sweden, or another already-needed supplier. Only eliminate Sorotec if geometry/quality remains suitable for commissioning.

The other remaining suppliers are mostly genuinely unique: Jackpot3, router, motors, KEDU, filament bulk and the DigiKey electronics basket. Further package-count reduction is likely to have diminishing returns or increase component risk.