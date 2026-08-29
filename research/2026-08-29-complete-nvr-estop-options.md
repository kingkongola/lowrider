---
researched_at: 2026-08-29
scope: complete or near-complete 230 V NVR + emergency-stop options in EU/Europe
status: researched-not-ordered
confidence: medium-high
machine_target: LowRider V4 with VEVOR 0700C ~800 W router + 24 V Jackpot3 PSU
constraints:
  - user wants low cost but not unsafe/no-name junk
  - machine-level stop should remove router + controller power
  - prefer EU sourcing and low parcel count
  - dust-prone garage
sources_checked:
  - Klinger & Born / technikundmehr Germany
  - Kahlhorn Germany
  - KEDU KJD12 German distributors
  - Idealo Germany
  - Sinolec UK reference
  - Tripus Germany
observed_prices_are_time_sensitive: true
---

# Research: complete NVR + emergency-stop options

This is a deliberately small follow-up to `2026-08-29-machine-power-safety.md`.

Goal: find a credible machine switch that combines no-voltage release / no automatic restart with a physically obvious emergency stop, without building an unnecessarily expensive industrial control cabinet.

## Option A — KEDU KJD12: strongest Pareto candidate

The KEDU `KJD12` family is a real workshop-machine NVR switch used on drill presses, planers, saws etc.

Verified German listing from Klinger & Born / technikundmehr:
- KEDU KJD12
- 230 V / 50 Hz coil
- 2-pole
- 16(12) A
- up to 2.5 kW at 230 V AC-1
- IP54 front
- yellow/red NOT-AUS cover / stop flap
- undervoltage release according to IEC204-1 / EN60204 section 7.5
- prevents automatic restart after voltage failure/recovery
- observed price **€37.62 incl VAT + shipping**

Source:
- https://www.technikundmehr.com/einbauschalter-als-geraeteschalter-2-polig-not-aus-kedu-type-kjd12-230v-bis-2-5kw-16-12-a-schliesser-2-motorschalter-hauptschalter.html

Other EU/German market observations:
- Wolpart / Güde-branded genuine KEDU KJD12: **€14.95–17.99** depending listing, 250 V / 16 A / IP54, 4-pin, emergency-stop function
- German Idealo observed an Amazon Marketplace `KEDU KJD12-14` at **€20.99 incl VAT**, Prime-capable in Germany, plus listed shipping from €3.99
- Traub: KEDU KJD12 with NVR + emergency-stop cover, **€36.89**, 406 units shown in stock; Swedish shipping however is expensive at **€24.45 for 0–4 kg**, making it a poor single-item source for us
- Optimum/German machine-spares listing: KJD12 around **€28.86**, emergency-stop cover included

Sources:
- https://www.wolpart.com/KEDU-KJD12-Ein-Aus-Schalter-250V-16A-4Pin-Schalter-mit-Not-Aus-Funktion-fuer-Abrichthobel-uvm./55098-01025
- https://www.idealo.de/preisvergleich/Liste/123521455/kedu-kjd12.html
- https://www.shop-traub.de/470-000-31-kedu-einbauschalter.html
- https://www.shop-traub.de/versandkosten
- https://drehen-fraesen-bohren.de/stuermer-maschinen-optimum-aircraft-metallkraft/ersatzteile/elektrobauteile/ohne-unterwarengruppe/schalter-230v-kedu-kjd12-16a-ip54-4pol

Independent UK reference from Sinolec gives stronger approval detail for KEDU KJD12/230V:
- DPST
- 16(12) A / 250 V
- NVR emergency-stop switch
- IP54
- CE, TÜV, UL / European approvals claimed by distributor
- £17.94 incl UK VAT

UK sourcing is not preferred because Sweden import/shipping economics are worse, but this is useful product-validation evidence.

Source:
- https://sinolec.co.uk/gb/nvr-no-volt-release-kedu-switches/1212072-kjd12230v-nvr-emergency-safety-stop-switch-230v-16a.html

### Why KJD12 is interesting for this LowRider

The router is ~800 W, only ~3.5 A nominal at 230 V, and controller PSU is small. The KJD12 16(12) A / 2.5 kW-class main contacts therefore have ample nominal load margin for switching the whole CNC supply path.

It also directly solves the two human-factor requirements:
- after outage, machine does not restart automatically
- a large yellow/red stop flap is easy to hit

It is not as industrially elaborate as a separate certified safety relay/contactors/mushroom system, but it is a purpose-built NVR/emergency machine switch rather than a random marketplace red button.

### Integration cost

KJD12 is a panel/built-in switch, not a complete corded box. We still need:
- small insulated enclosure or panel
- cable strain reliefs
- grounded incoming cable / Schuko plug
- switched output arrangement to router + 24 V PSU

This is still likely far cheaper than a full industrial safety-control build.

## Option B — Klinger & Born K3000/1Ph-230/Not-Aus/P: premium complete benchmark

German `technikundmehr` / K&B unit:
- model `K3000/1Ph-230/Not-Aus/P`, product 3003
- 230 V
- rated up to 16 A / 4.0 kW on seller page
- ON/OFF + dedicated NOT-AUS
- undervoltage release per IEC204-1 / EN60204 / VDE0113 section 7.5
- 2 m H07RN-F 3×1.5 mm mains cable + Schuko plug
- 1 m H07RN-F 3×1.5 mm machine cable
- IP54 insulated enclosure
- ~180×106×90 mm
- observed price **€93.44 incl VAT + shipping**

A second Kahlhorn listing for the same type family shows **€112.50 incl VAT** and describes a 2-pole contactor, undervoltage release and emergency stop.

Sources:
- https://www.technikundmehr.com/Geraete-Schalter-3003--4KW-230V--EIN-AUS--Not-Aus--Unterspannung--VDE-0113--Netzschalter.html
- https://www.kahlhorn.com/single-phase-motorstarter-230v-with-emergency-stop-button%3A%3A2554.html

### Assessment

This is the quality/simplicity benchmark: ready-to-connect, enclosed, proper cable, NVR and emergency stop. But roughly €93–113 before Sweden shipping is hard to justify for an ~800 W hobby router unless cheaper KJD12 integration becomes awkward.

Keep as fallback, not first choice.

## Option C — KJD17 + separate emergency stop / contactor

Previous research showed a genuine E-Switch `KJD17-22413-112` around **168–170 SEK incl VAT** from Farnell/DigiKey, with NVR and remote-trip capability.

A separate industrial emergency-stop device then needs either:
- contacts rated to interrupt the actual machine load, or
- a properly rated contactor/switching element.

This is electrically elegant but creates more components, more enclosure work and usually a higher complete price than KJD12.

**Assessment:** no longer the Pareto default. Keep only if we later need remote interlocks/guards or a more industrial control architecture.

## Option D — Tripus modular industrial parts

Tripus Germany sells credible individual safety/control parts:
- enclosed emergency-stop station `301.173`: **€26.78 incl VAT**, IP65, red 40 mm mushroom, turn reset
- its direct AC-15 rating at 230 V is **4.5 A**, so it should not automatically be treated as a high-margin direct router power switch
- Tripus also sells 230 V contactors around €25 and many complete machine-control enclosures

Source:
- https://tripus-shop.com/en/product/emergency-stop-with-push-button-in-enclosure/

This provides a valid industrial DIY route but again adds component count and cost.

## Current ranking

### 1 — KEDU KJD12, recommended Pareto direction

Why:
- purpose-built machine NVR
- 16(12) A / 230–250 V class
- emergency-stop flap integrated
- proper manufacturer / workshop-machine application
- widely sold by German machine-spares vendors
- likely €15–38 before Sweden shipping
- much simpler than contactor + safety-control circuit

### 2 — K&B K3000 complete station, premium fallback

Why:
- ready-to-connect
- best documented complete physical solution
- proper emergency stop + NVR + cables + enclosure

Downside: ~€93+.

### 3 — KJD17 + separate industrial emergency circuit

Technically expandable but worse cost/complexity for current needs.

## Procurement rule

Do **not** order the KJD12 from a German seller with €20–25 Sweden shipping just because the item itself is €15.

Before purchase:
1. search Amazon.se/Amazon.de with Sweden delivery for **exact genuine KEDU KJD12 / KJD12-14 230 V 16 A NVR + emergency-stop cover**
2. check whether it can be bundled with any other machine-electrical items from a German/EU seller
3. target delivered price: roughly **<=400–500 SEK including enclosure-related small parts**

If the complete KJD12 solution approaches ~700–900 SEK delivered after enclosure/cables, reconsider the K&B ready-made €93 station because the convenience gap becomes small.

## Decision state

- **Architecture direction promoted:** KEDU KJD12 panel switch in a small insulated machine-power box.
- **Supplier not locked.**
- **Do not buy yet** until Sweden-delivered source and enclosure/output arrangement are priced.
