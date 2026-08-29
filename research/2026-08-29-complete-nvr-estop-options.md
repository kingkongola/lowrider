---
researched_at: 2026-08-29
last_updated_at: 2026-08-29
scope: complete or near-complete 230 V NVR + emergency-stop options in EU/Europe
status: researched-not-ordered
confidence: high-on-kjd12-spec-medium-on-supplier
machine_target: LowRider V4 with VEVOR 0700C ~800 W router + 24 V Jackpot3 PSU
constraints:
  - user wants low cost but not unsafe/no-name junk
  - machine-level stop should remove router + controller power
  - prefer EU sourcing and low parcel count
  - dust-prone garage
sources_checked:
  - Klinger & Born / technikundmehr Germany
  - Kahlhorn Germany
  - KEDU KJD12 manufacturer/distributor documentation
  - Güde Denmark
  - Idealo Germany
  - Sinolec UK reference
  - Tripus Germany
  - Swedish marketplace comparison
observed_prices_are_time_sensitive: true
---

# Research: complete NVR + emergency-stop options

This is a deliberately small follow-up to `2026-08-29-machine-power-safety.md`.

Goal: find a credible machine switch that combines no-voltage release / no automatic restart with a physically obvious emergency stop, without building an unnecessarily expensive industrial control cabinet.

## Option A — KEDU KJD12: strongest Pareto candidate

The KEDU `KJD12` family is a real workshop-machine NVR switch used on drill presses, planers, saws, lathes and dust extractors.

### Electrical specification now strongly verified

Kahlhorn's KEDU `KJD12-10ZF` documentation states:
- 230 V / 50 Hz
- 2-pole, 2 normally-open main contacts
- NVR / zero-voltage release
- AC-1: **16 A at 230 V**
- AC-3: **10 A at 230 V**
- positively driven contacts
- 50,000 switching cycles
- IP54 front
- 6.3×0.8 mm Faston terminals
- IEC947-4-1 / EN60947 / DIN VDE 0630 part 102

KEDU's own KJD12 family drawing confirms the 230 V / 50 Hz coil option and an optional emergency-stop + waterproof cover accessory.

Sources:
- https://www.kahlhorn.com/print_product_info/english/kjd12.pdf
- https://www.stathisnet.gr/image/SpecsUpload/016325.pdf

Güde's current KJD12 spare-part pages independently show:
- 16(12) A / 250 V AC
- IP54
- NVR behavior
- warning that **KJD12 exists in several mechanical variants**, so exact panel/terminal geometry must be checked before ordering.

Source:
- https://www.guede.dk/kontakt-onoff-kjd12-p-2439.html?language=en

### German/EU price observations

Verified German listing from Klinger & Born / technikundmehr:
- KEDU KJD12
- 230 V / 50 Hz coil
- 2-pole
- 16(12) A
- up to 2.5 kW at 230 V AC-1
- IP54 front
- yellow/red NOT-AUS cover / stop flap
- undervoltage release according to IEC204-1 / EN60204 section 7.5
- observed price **€37.62 incl VAT + shipping**

Source:
- https://www.technikundmehr.com/einbauschalter-als-geraeteschalter-2-polig-not-aus-kedu-type-kjd12-230v-bis-2-5kw-16-12-a-schliesser-2-motorschalter-hauptschalter.html

Other market observations:
- Wolpart / Güde-branded KEDU KJD12: **€14.95–17.99** depending listing, 250 V / 16 A / IP54, 4-pin, emergency-stop function
- German Idealo observed Amazon Marketplace `KEDU KJD12-14` around **€20.99 incl VAT**, Prime-capable in Germany; Sweden delivery not confirmed
- Traub: **€36.89**, stock shown high, but Sweden shipping **€24.45 for 0–4 kg**, so poor as a one-item order
- Optimum/German machine-spares listing: around **€28.86**, emergency-stop cover included
- Swedish Fyndiq has a KJD12-14 listing around **338 SEK + 39 SEK shipping**, but seller/source provenance is less attractive and total is not cheaper than importing a known German machine-spares part

Sources:
- https://www.wolpart.com/KEDU-KJD12-Ein-Aus-Schalter-250V-16A-4Pin-Schalter-mit-Not-Aus-Funktion-fuer-Abrichthobel-uvm./55098-01025
- https://www.idealo.de/preisvergleich/Liste/123521455/kedu-kjd12.html
- https://www.shop-traub.de/470-000-31-kedu-einbauschalter.html
- https://www.shop-traub.de/versandkosten
- https://drehen-fraesen-bohren.de/stuermer-maschinen-optimum-aircraft-metallkraft/ersatzteile/elektrobauteile/ohne-unterwarengruppe/schalter-230v-kedu-kjd12-16a-ip54-4pol
- https://fyndiq.se/produkt/kjd12-14-inbyggd-enhetsbrytare-magnetbrytare-6-pin-230v-b525c3c70d9f43f4/

Independent UK reference from Sinolec gives additional product-validation evidence:
- DPST
- 16(12) A / 250 V
- NVR emergency-stop switch
- IP54
- distributor states CE, TÜV and UL approvals
- £17.94 incl UK VAT

UK sourcing is not preferred because Sweden import/shipping economics are worse.

Source:
- https://sinolec.co.uk/gb/nvr-no-volt-release-kedu-switches/1212072-kjd12230v-nvr-emergency-safety-stop-switch-230v-16a.html

### Why KJD12 is interesting for this LowRider

The router is ~800 W, roughly ~3.5 A nominal at 230 V, and controller PSU is small. Even the more relevant AC-3 rating documented by Kahlhorn is 10 A, giving substantial current margin.

It solves two practical machine requirements:
- after outage, machine cannot restart automatically without pressing START
- yellow/red emergency-stop cover can be hit quickly

It is not the same architecture as a safety relay + dual-channel mushroom + contactors on an industrial production CNC, but it is a purpose-built, standards-referenced machine NVR switch rather than a random marketplace red button.

### Important variant rule

Do not buy merely by the string `KJD12`.

Required variant characteristics for our box:
- 230 V / 50 Hz NVR coil
- 2-pole / 4-main-terminal version suitable for switching line + neutral
- 16 A class
- emergency-stop yellow/red cover accessory installed
- mounting geometry known before cutting enclosure

Six-terminal `KJD12-14` variants may include extra circuitry/contact arrangements and are not automatically preferable.

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
- seller rates up to 16 A / 4.0 kW
- ON/OFF + dedicated NOT-AUS
- undervoltage release per IEC204-1 / EN60204 / VDE0113 section 7.5
- 2 m H07RN-F 3×1.5 mm mains cable + Schuko plug
- 1 m H07RN-F 3×1.5 mm machine cable
- IP54 insulated enclosure
- ~180×106×90 mm
- observed price **€93.44 incl VAT + shipping**

A Kahlhorn listing for the same K3000 family shows **€112.50 incl VAT** and describes contactor, undervoltage release and emergency stop.

Sources:
- https://www.technikundmehr.com/Geraete-Schalter-3003--4KW-230V--EIN-AUS--Not-Aus--Unterspannung--VDE-0113--Netzschalter.html
- https://www.kahlhorn.com/single-phase-motorstarter-230v-with-emergency-stop-button%3A%3A2554.html

### Assessment

This remains the quality/simplicity benchmark: ready-to-connect, enclosed, proper cable, NVR and emergency stop. But €93–113 before Sweden shipping is hard to justify for an ~800 W hobby router unless cheaper KJD12 integration becomes awkward.

Keep as fallback, not first choice.

## Option C — KJD17 + separate emergency stop / contactor

Previous research showed genuine E-Switch `KJD17-22413-112` around 168–170 SEK incl VAT from Farnell/DigiKey, with NVR and remote-trip capability.

A separate industrial emergency-stop device then needs either main contacts suitable for the machine load or a properly rated contactor/switching element.

This is electrically expandable but creates more parts, enclosure work and cost than KJD12.

**Assessment:** no longer Pareto default. Keep if we later want guard/interlock logic.

## Option D — Tripus modular industrial parts

Tripus Germany sells credible individual safety/control parts:
- enclosed emergency-stop station `301.173`: **€26.78 incl VAT**, IP65, red 40 mm mushroom, turn reset
- direct AC-15 rating at 230 V is **4.5 A**, so it should not automatically be used as a high-margin direct router power switch
- Tripus also sells 230 V contactors around €25 and complete machine-control housings

Source:
- https://tripus-shop.com/en/product/emergency-stop-with-push-button-in-enclosure/

Valid industrial DIY route, but worse component count/cost for this build.

## Current ranking

### 1 — KEDU KJD12, recommended Pareto direction

Why:
- purpose-built machine NVR
- documented AC-1 16 A / AC-3 10 A at 230 V
- positive-opening/positively driven contact documentation from Kahlhorn
- emergency-stop cover available/included in relevant variants
- standards-referenced workshop-machine part
- widely sold by German machine-spares vendors
- likely €15–38 before Sweden shipping
- much simpler than contactor + separate safety-control circuit

### 2 — K&B K3000 complete station, premium fallback

Ready-to-connect and best documented complete physical solution, but ~€93+.

### 3 — KJD17 + separate industrial emergency circuit

Technically expandable but poorer current cost/complexity fit.

## Procurement rule

Do **not** order KJD12 from a seller with €20–25 Sweden shipping only because the item itself is cheap.

Before purchase:
1. search Amazon.se/Amazon.de checkout for a genuine **KEDU KJD12, 230 V / 50 Hz, 16 A class, 4-main-terminal / 2-pole NVR with emergency-stop cover**
2. check if it can be bundled with enclosure, cable glands or other actually-needed machine electrical parts
3. target total for KJD12 + enclosure-related small parts: roughly **<=400–500 SEK delivered**

If complete KJD12 integration approaches ~700–900 SEK, reconsider the K&B ready-made €93 station.

## Decision state

- **Architecture direction promoted:** KEDU KJD12 in a small insulated machine-power box.
- **Exact electrical variant characteristics now defined.**
- **Supplier not locked.**
- **Do not buy yet** until Sweden-delivered source plus enclosure/output arrangement is priced.
