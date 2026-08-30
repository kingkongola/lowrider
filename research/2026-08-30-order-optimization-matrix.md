# Order optimization matrix — 2026-08-30

Goal: minimize total landed cost, not simply order count.

Objective:
`parts + shipping + taxes/import + expected wrong-part/reorder cost + small handling penalty per extra order`

Hard rule: do not change a locked technical spec only to reduce package count.

## Mechanical bundle candidates

| Part group | Required | LaskaKit | Roboter-Bausatz | Notes |
|---|---:|---:|---:|---|
| Smooth idler | 6 × 5 mm bore / 10 mm belt | LA190008E ~€1.86 ea | RBS12910 ~€1.49 ea at qty 6 | Both match |
| T8 lead screw | 1 × T8×8 400 mm | LA190032A ~€8.15 | RBS12872 €10.85 incl 1 brass nut | Both match |
| Brass nut | 2 total | LA190033A ~€1.31 ea | RBS12872 includes 1 + RBS12749 €1.67 | Both match |
| 5→8 coupler | 2 | LA190031 ~€1.81 ea | RBS10595 €1.75 ea | Both match |
| GT2 belt | ≥4409 mm | stock unreliable | RBS12747, 10 mm rubber + fiberglass, 5 m ≈ €11.25 | RBS cleanest verified source |
| GT2 drive pulley | 3 × 16T / 5 mm / 10 mm belt | no verified exact consolidation | RBS12867 ~€0.88–1.25 ea | RBS wins |
| Sweden freight | — | €8.93 GLS | €14.99 DHL | published rates |

### Mechanical conclusion

Roboter-Bausatz supplies all six mechanical groups in one order. Approximate merchandise ~€39–40 + €14.99 freight = **~€54–55**.

This replaces LaskaKit + separate belt + Allegro.

## Electronics / electrical matrix

| Part group | Preferred | Reason |
|---|---|---|
| HDR-60-24 | DigiKey | exact Mean Well |
| 10 × Omron SS-3GL13PT | DigiKey | exact locked switch |
| 16 × 608-2RS | DigiKey | exact 8×22×7; helps basket |
| Wago 221-413 | DigiKey | genuine, no marginal freight |
| M20 glands | DigiKey | same mains basket |
| TE Faston | DigiKey `A27824-ND` | avoid Marketplace duplicate |
| M12 LV gland | DigiKey `AIO-CSM12` | fits ~4.8 mm cable |
| 24 V 2-core | DigiKey/local | generic; must not create extra international order |
| Endstop cable | DigiKey/local | generic; same rule |

Current DigiKey basket ~641 kr incl VAT before optional cables. Public free-shipping threshold 615 kr; checkout authoritative.

## NVR / machine-stop matrix

The previous plan over-weighted exact KEDU provenance.

**Real requirement:** 230 V no-voltage-release/no-restart switch with suitable current rating, clear stop actuator and documented terminals.

| Route | Observed price | Shipping/order effect | Verdict |
|---|---:|---|---|
| Clas Ohlson KJD12 230 V / 10 A | 299 kr | local/Swedish | viable if physical actuator/terminal arrangement is suitable |
| Amazon.se KEDU KJD12-14 result | ~281 kr | potentially low/Prime; checkout-gated | strong candidate |
| CEM genuine KEDU KJD12-14 | low item price but international freight | creates dedicated order | **not baseline** unless delivered total unexpectedly wins |

Conclusion: **NVR should not create an international special order by default.** Exact CEM/KEDU is a quality option, not a project dependency.

## Cutter matrix

Technical target for first LR4 work: 3.175 mm shank/diameter, single-flute upcut, carbide, ~9 mm cutting length.

| Supplier | Candidate | Technical match | Order effect | Verdict |
|---|---|---|---|---|
| Sorotec | `L1S.M.0317`, €3.70 | exact | separate international order for €11.10 merchandise if buying 3 | technically best, economically poor to order now |
| Roboter-Bausatz | searched current catalogue | no suitable 3.175 single-flute found | would have been ideal consolidation | no |
| VEVOR | current 1/8 kit | 2-flute, not equivalent | could join router order | reject as spec substitution |
| Makera EU | 1/8 Spiral O single flute, €5.99 | suitable family | still separate order | does not solve order count |
| marketplace/eBay generics | various | uncertain geometry/quality | separate order | not worth replacing known-good Sorotec solely for package count |

Conclusion: **defer cutter purchase**. Keep Sorotec as technical first choice, but place no Sorotec order in the current batch. When cutting is imminent, combine the order with any additional cutters actually needed (e.g. later long plywood cutter), or re-evaluate a current absorbed source then.

## Supplier matrix after optimization

| Supplier | Reason | Verdict |
|---|---|---|
| Roboter-Bausatz | complete loose mechanical bundle | KEEP |
| DigiKey | electronics/electrical small parts | KEEP |
| StepperOnline Germany | exact motor five-pack | KEEP |
| Elecrow | unique Jackpot3 | KEEP |
| VEVOR | chosen 0700C router | KEEP |
| SUNLU | bulk PLA | KEEP if Sweden checkout holds |
| NVR via local/Amazon | machine stop | LOCAL/LOW-FRICTION; no special EU order baseline |
| Sorotec | cutters | DEFER |
| Motonet | tubes | LOCAL |
| Biltema | enclosure/cable | LOCAL |
| used table/material | physical local purchase | LOCAL |

## Order-count scenarios

### Old fragmented plan
~10 shipped orders before local purchases.

### Current optimized current-batch baseline
1. Roboter-Bausatz — mechanics
2. DigiKey — electronics/electrical
3. StepperOnline Germany — motors
4. Elecrow — Jackpot3
5. VEVOR — router
6. SUNLU — PLA

NVR comes from local/Amazon unless a special-order delivered price clearly wins.
Sorotec is deferred until cutting is imminent.

= **6 main shipped orders now**, not 7–10.

## Next optimization targets

1. exact StepperOnline Sweden landed cost
2. DigiKey vs local for generic 24 V/endstop cable
3. Elecrow landed cost
4. SUNLU Sweden checkout
5. Roboter-Bausatz checkout + confirmation that 5 m belt is one continuous piece
6. NVR choose later from cheapest documented local/Amazon route once enclosure layout is known

Further package reduction should only happen if it reduces landed cost without weakening spec.