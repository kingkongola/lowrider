---
research_date: 2026-08-29
last_updated_at: 2026-08-29
scope: final Pareto machine mains switch / NVR / emergency-stop choice for LR4
status: recommendation-ready
confidence: high-on-device-class-medium-on-final-seller
machine_target: LowRider V4 ~650×1250, VEVOR 0700C 800 W, HDR-60-24 controller PSU, existing DeWalt shop-vac
region: Sweden / EU
price_basis: current EU listings observed 2026-08-29; Sweden freight must be checked before order
sources_checked:
  - KEDU KJD12 manufacturer/order-option datasheet
  - Kahlhorn KEDU KJD12 technical sheet
  - Sinolec genuine KEDU KJD12/230V listing
  - Optimum/German KEDU KJD12 listings
  - Güde Denmark KJD12 listings
  - Italian KEDU safety-switch distributor
  - Swedish marketplace references used only as price comparison
supersedes:
  - earlier idea that a KJD17 remote-trip switch plus separate contactor/mushroom is the default Pareto architecture
---

# Final NVR / emergency-stop direction

## Decision

Use a **genuine KEDU KJD12, 230 V, 16 A, 4-pin/2-pole NVR machine switch with the yellow/red emergency-stop cover/button** as the baseline machine mains switch.

This is dramatically simpler than building an industrial contactor/control circuit while still providing the two practical behaviours we actually need:
- **no-volt release / restart prevention** after mains loss
- a large, easy-to-hit stop actuator that removes mains power through the two-pole switch

This is a hobby/workshop CNC machine-power solution. Do not describe it as a safety-PLC / PLd / Category-3 safety system.

## Exact electrical class

KEDU KJD12 manufacturer/reference data supports:
- 230 V / 50 Hz coil variant
- 2-pole N/O switching
- 16 A AC-1 at 230 V
- 10 A AC-3 at 230 V on the Kahlhorn reference
- IP54 front
- 6.3×0.8 mm Faston terminals
- no-voltage release
- optional emergency-stop button/cover in the KEDU order system

Sources:
- https://www.kahlhorn.com/print_product_info/english/kjd12.pdf
- https://www.stathisnet.gr/image/SpecsUpload/016325.pdf

Sinolec's genuine KEDU `KJD12/230V` is specifically described as:
- DPST
- 16(12) A / 250 V
- 220–250 V AC
- red/green actuators plus red emergency-stop button under yellow top
- IP54
- TUV / VDE / CE / UL approvals

Source:
- https://sinolec.co.uk/gb/nvr-no-volt-release-kedu-switches/1212072-kjd12230v-nvr-emergency-safety-stop-switch-230v-16a.html

## Load margin for our machine

Core machine loads are modest:
- VEVOR router: ~800 W
- HDR-60-24: 60 W maximum DC output class, much less than 1 A mains-side

Even if the existing ~1050 W DeWalt vacuum is later placed on the same machine-level switched supply, combined nominal power is around 1.9 kW, roughly 8–9 A at 230 V before transients.

That is still within the KJD12's 16 A resistive / 10 A AC-3 reference class. Final wiring/fusing should of course respect the actual outlet/cable ratings.

## Current EU purchase references

### Best exact German reference

Optimum / Stürmer spare part:
- code **`ST0380001`** / manufacturer reference `0380001`
- KEDU KJD12
- 230 V
- 16 A
- IP54
- 4-pole terminal arrangement / 2 switched poles
- **includes yellow cover with emergency-stop button**
- current observed item price **€28.86 incl VAT**

Source:
- https://drehen-fraesen-bohren.de/stuermer-maschinen-optimum-aircraft-metallkraft/ersatzteile/elektrobauteile/ohne-unterwarengruppe/schalter-230v-kedu-kjd12-16a-ip54-4pol

Other German exact references:
- Optimum/Bach `0380001`: ~€39.09, also explicitly includes Not-Aus cover
- ManoMano Germany genuine KEDU/Güde variants around ~€18–45 depending seller/variant

Sources:
- https://www.bachgmbh.de/Schalter-230V-KEDU-KJD12-16A-IP54-4POL-0380001
- https://www.manomano.de/p/kedu-kjd12-magnetschalter-4pin-startstop-250v-16a-mit-not-aus-funktion-druckknopfschalter-62632844

### Denmark

Güde Denmark sells genuine KEDU KJD12 variants for **205 DKK** and shows stock on current pages.

However KJD12 has several panel/button variants. A Denmark listing is only valid if the chosen version visibly includes the emergency-stop actuator/cover we want.

Sources:
- https://www.guede.dk/kontakt-onoff-kjd12-p-2439.html?language=en
- https://www.guede.dk/startstop-switch-kedu-kjd12-design-p-2420.html?language=en

## Why not the Swedish Fyndiq/Fruugo generics

Current Swedish marketplace pages show KJD12/KJD12-14 products around ~214–338 SEK plus small freight, but manufacturer identity and exact emergency-stop mechanics are often unclear/unbranded.

For a mains safety switch, saving perhaps 50–100 SEK is not worth losing provenance.

Use those only as a price reference, not the default purchase source.

## Why not KJD17 + separate contactor anymore

A KJD17 remote-trip input is useful for industrial interlocks, but it created unnecessary design questions about:
- how remote trip is wired
- whether the mushroom only drops a coil
- whether a contactor is then needed for robust upstream isolation
- extra enclosure, terminals and mains wiring

The genuine KJD12 integrated machine-switch form already provides the practical stop + NVR behaviour for this small machine with far fewer components.

If the project later needs door interlocks, safety relays, automatic spindle control or industrial safety categories, revisit the architecture then.

## Enclosure / wiring architecture

Do not leave mains terminals exposed.

Preferred simple arrangement:

`wall plug -> KJD12 -> switched machine distribution -> router + HDR-60-24 (and optionally vacuum)`

Implementation:
- mount KJD12 in a small robust insulated or earthed enclosure/front panel
- strain relief on mains entry/exit
- use correctly rated flexible cable and insulated 6.3 mm female Faston terminals or equivalent approved terminations
- protective earth bypasses the switch and remains continuous to all Class-I loads/enclosures
- switch both live and neutral through the two KJD12 poles where the actual wiring diagram/terminal markings specify the DPST arrangement
- do not rely on wire colours; follow terminal numbering/data sheet

The KJD12 does **not** provide overload/short-circuit protection. House circuit protection and any machine-specific fuse/breaker remain separate functions.

## Possible DeWalt simplification to investigate later

The existing DeWalt has an automatic tool socket. If its exact tool-socket rating is sufficient for the 800 W VEVOR, a clean topology may be:

`KJD12 machine supply -> DeWalt + HDR-60-24`

and

`VEVOR router -> DeWalt auto-start tool socket`

Then one KJD12 stop could remove power from controller, vacuum and router while the DeWalt handles vacuum auto-start.

Do **not** lock this topology until the DXV30SAPTA tool-socket maximum load and auto-start behaviour are verified from its manual.

## Buy threshold

For a **genuine branded KEDU KJD12 with emergency-stop cover**, accept roughly:
- **<=400 SEK delivered:** excellent, buy
- **400–500 SEK delivered:** still reasonable if seller is reputable and exact variant is clear
- **>500 SEK delivered:** re-compare EU sellers / complete station options

Do not spend ~900+ SEK on a prebuilt industrial station unless the simple KJD12 enclosure genuinely becomes awkward.

## Remaining pre-order check

Only one checkout task remains:
1. check whether exact Optimum `ST0380001` or another genuine KEDU KJD12/230V/16A/Not-Aus variant ships to Sweden
2. record final delivered price
3. if <=400–500 SEK, buy
4. otherwise compare the Denmark genuine KEDU route

No further contactor/safety-relay research is warranted for the baseline build unless this sourcing fails.