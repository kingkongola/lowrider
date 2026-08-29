---
research_date: 2026-08-29
scope: LR4 motor wiring, exact endstop wiring and connector strategy for selected StepperOnline motors + Jackpot3
status: recommendation-ready
decision_state: dry-fit native 1 m stepper leads before extensions; buy 10 m LaskaKit LA150151A for endstops; wire exact Omron SS-3GL13PT NC using COM+NC; use cheap 2.54 mm board connectors/pigtails
price_basis: observed web prices/specifications 2026-08-29; re-check at checkout
region: Sweden / EU
sources_checked:
  - V1 Engineering LR4 documentation
  - V1 Engineering Jackpot3 documentation
  - V1 Engineering endstop/endstop-plug products
  - StepperOnline exact 17HS19-2004S1 product page
  - V1E forum LR4 wiring discussions
  - LaskaKit current cable/connector catalogue
supersedes: earlier conclusions in this same file where exact cable source remained open and one stale SS-5GL2 reference remained
---

# LR4 wiring + connectors

## Stepper motor leads

Selected motors: StepperOnline `17HS19-2004S1`, five-pack `5-17HS19-2004S1`.

Each selected motor already has:
- 1 m factory lead
- 4-pin 2.54 mm female connector

Jackpot3 uses open 2.54 mm male stepper headers, so no JST conversion is required merely to connect these motors.

Sources:
- https://www.stepperonline.nl/5st-nema-17-bipolair-59ncm-83-55oz-in-2a-42x48mm-4-draden-met-1m-kabel-aansluiting-5-17hs19-2004s1
- https://docs.v1e.com/electronics/jackpot3/

### Extension decision

Do **not** buy the three standard V1 stepper extensions yet.

Our machine is only ~650×1250 usable and the motors already include unusually long 1 m leads. Mount Jackpot3 at the recommended YZ_Min side, route all factory leads, exercise full X/Y/Z travel and buy extensions only for runs that cannot retain a relaxed service loop.

This is a project-specific optimization, not a claim that V1's standard wiring kit is wrong for generic/full-sheet builds.

## Exact endstops

Correct switch is **Omron `SS-3GL13PT`**.

The older `SS-5GL2` mention in a previous revision of this file was stale and is explicitly corrected here.

V1 Engineering's product page identifies `SS-3GL13PT`; Jackpot3 documentation specifies **Normally Closed (NC)** endstop wiring.

Sources:
- https://www.v1e.com/products/limit-switch-endstop
- https://docs.v1e.com/electronics/jackpot3/

Machine quantity:
- 5 installed

Planned procurement:
- 10 exact switches from DigiKey because the qty-10 discount makes five spares cost only ~32 SEK extra in the planned cart

See:
- `research/2026-08-29-final-psu-endstop-wiring-cart.md`

## Endstop cable — now resolved

V1's own LowRider endstop plug kit uses:
- 5 runs
- 1200 mm each
- two-wire DuPont-style board end

Total V1 reference length is therefore **6 m**.

Source:
- https://www.v1e.com/products/endstop-plug

### Chosen cable

LaskaKit `LA150151A`:
- UL2464 / LIYY
- 26 AWG
- 3 × 0.14 mm²
- unshielded
- flexible copper multicore
- current observed price around **€0.58/m**
- current stock in the hundreds of metres

Source:
- https://www.laskakit.cz/en/connecting-cables/

Buy **10 m** and use two of the three cores.

Why 10 m:
- only ~€5.80 in material
- ample routing/service-loop margin over V1's 6 m baseline
- useful spare for rework/sensors
- rides inside the already-planned LaskaKit mechanical shipment, so no extra parcel

26 AWG is electrically ample for endstop signal current; flexible stranded copper and good strain relief matter more here than conductor size.

## Board-side 2.54 mm connectors

### If a suitable DuPont crimper is already owned

LaskaKit currently has:
- DuPont housing family `LA217000...`, 2.54 mm, from ~€0.03
- female socket/contact **`LA217002`**, ~€0.03 each

Source:
- https://www.laskakit.cz/en/connectors/

Buy approximately:
- 10 × 2-position housings
- 20 × female contacts

Important: select the **2-position housing visibly in the product dropdown**. Do not infer the exact suffix from the family code.

### If no suitable crimper is owned

Do not buy an expensive dedicated crimper just for five endstop plugs.

LaskaKit `LA150090`:
- 40 × pre-crimped 2-pin F/F cables
- 70 cm
- ~€6.10–6.12
- currently in stock

Source:
- https://www.laskakit.cz/en/propojovaci-kabely-f-f-40ks-2pin-samice-samice--70cm/

Cut five short board-side pigtails and solder/splice them to the long `LA150151A` runs.

It is overkill in quantity but still cheaper and less annoying than buying a precision DuPont crimper solely for this project; the extras are reusable maker stock.

## Switch-side termination

Default: **solder directly to COM + NC**.

Procedure:
- conductor 1 -> COM
- conductor 2 -> NC
- individual heatshrink over each terminal
- strain-relieve cable near the switch so gantry motion does not flex the solder joint

V1 explicitly allows soldering these switches. This avoids another purchase and avoids using generic automotive mini-spades whose wire-size range often does not suit 26 AWG well.

Sources:
- https://www.v1e.com/products/limit-switch-endstop
- https://www.v1e.com/products/endstop-plug

## 24 V PSU output cable

Endstop cable is **not** the PSU cable.

For `HDR-60-24 -> Jackpot3`, add around 1 m of LaskaKit UL2464 20 AWG / 0.52 mm² tinned-copper multicore cable.

Current LaskaKit family:
- `LA150187A` / `B` / `C` / `D`
- 20 AWG / 0.52 mm²
- selectable core count including **2 cores**
- 2-core OD ~4.8 mm
- current price from about €0.99–1.00/m

Source:
- https://www.laskakit.cz/en/ul2464-20awg-liyy-0-52-mm2-nestineny-vicezilovy-kabel--cerny/

The indexed page does not reliably expose which suffix maps to which core count, so **select 2 cores in the product UI instead of guessing a suffix**.

Use ferrules at the screw-terminal ends if an appropriate ferrule crimper is already available; otherwise follow the terminal manufacturer's accepted stripped-wire practice. Keep mains wiring physically separate from this low-voltage wiring.

## Final wiring purchase additions

Add to the existing LaskaKit cart:
- 10 m `LA150151A` endstop cable: ~€5.80
- 1 m 20 AWG UL2464 2-core variant: ~€1
- board-side connector option:
  - housings + `LA217002` sockets, roughly <€1 if a crimper exists, or
  - `LA150090` ~€6.1 if no crimper exists

Do not add:
- stepper extensions yet
- special switch-side spade terminals by default
- shielded audio cable
- CCA cable
- separate cable shipment

## Locked wiring rules

- motors: use native 1 m leads first
- endstops: exact `SS-3GL13PT`
- endstop logic: NC
- switch terminals: COM + NC
- endstop cable: 10 m `LA150151A`
- switch end: solder + heatshrink
- board end: 2-pin 2.54 mm female connector/pigtail
- PSU output: ~1 m 20 AWG 2-core LaskaKit UL2464

This closes the previously open cable-source question without adding a new vendor/order.