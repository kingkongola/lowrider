---
research_date: 2026-08-29
last_updated_at: 2026-08-29
scope: DeWalt DXV30SAPTA 230 V tool socket, auto-start behavior, maximum connected tool load, and integration with LR4 router/NVR
status: recommendation-ready
confidence: high
machine_target: LowRider V4 with VEVOR 0700C 800 W
region: Sweden / EU
sources_checked:
  - Jula DXV30SAPTA product page
  - DXV30SAPTA original/manual copies from Bauhaus/ManualsLib
  - DXV30SAPTA Finnish manual distributed by jem & fix
supersedes: earlier unresolved assumption that DXV30SAPTA tool-socket maximum load was unknown
---

# DeWalt DXV30SAPTA tool socket

## Verified model behavior

Jula's current `DXV30SAPTA` listing confirms:
- built-in **230 V tool outlet**
- automatic start/stop function
- 1050 W vacuum motor
- 30 L tank
- 48 mm × 2.1 m hose

Source:
- https://www.jula.se/catalog/hem-och-hushall/stad-och-kladvard/dammsugare/grovdammsugare/grovdammsugare-015478/

The original manual confirms that in automatic/tool mode the vacuum starts and stops from a power tool connected to the vacuum's socket, and the vacuum continues for approximately **15 seconds** after the tool is switched off.

Sources:
- https://www.bauhaus.se/media/pdf/1163387A.pdf
- https://www.manualslib.com/manual/3147173/Dewalt-Dxv30sapta.html?page=22

## Maximum connected tool power — resolved

A DXV30SAPTA manual distributed by jem & fix explicitly lists:

- **maximum power for connected electric tool: 2450 W**

Source:
- https://media.jemogfix.dk/prod-mediafiles/dk/pdf/1140_9077574_001.pdf

This resolves the previous missing `PA` value in other manual copies, which state only that the connected tool must not exceed the socket's maximum connected load.

## VEVOR compatibility margin

Chosen router:
- VEVOR 0700C
- 800 W rated power

Tool socket maximum:
- 2450 W

Nominal margin:
- 2450 - 800 = **1650 W**
- router uses only about **33%** of the published maximum tool-socket rating

Therefore the 800 W router is comfortably inside the DXV30SAPTA tool-socket rating.

## Recommended operating topology

This enables a very clean baseline:

`wall -> KJD12 NVR/emergency stop -> machine distribution`

with two branches after KJD12:

1. `-> HDR-60-24 -> Jackpot3`
2. `-> DeWalt DXV30SAPTA`

and:

`VEVOR 0700C -> DeWalt 230 V auto-start tool socket`

Behavior:
- press machine START: controller PSU and DeWalt receive mains
- DeWalt remains in tool/auto mode
- when router is switched/energized, DeWalt automatically starts extraction
- when router stops, DeWalt runs on ~15 seconds
- hitting KJD12 emergency stop removes upstream mains from controller, DeWalt and therefore the router socket
- after a mains outage, KJD12 no-volt release prevents the whole machine supply from automatically restoring until restarted

## Current draw sanity check

Approximate nominal machine load while cutting:
- DeWalt: 1050 W
- router: 800 W
- HDR-60-24 input: roughly <=70 W class at full DC output
- total: around **1.9 kW**, roughly **8.3 A at 230 V** nominal

This is inside the referenced KJD12 10 A AC-3 / 16 A AC-1 class, but starting currents are higher than nominal. The final machine distribution, cable, connectors and upstream circuit protection must be rated appropriately and the actual KJD12 datasheet/terminal diagram must be followed.

## Important distinctions

The DeWalt auto-start socket is a convenience/control function, not a replacement for the machine-level NVR/emergency stop.

Do not use the vacuum's auto-start as the only emergency shutdown mechanism.

Likewise, the KJD12 is a pragmatic workshop NVR/emergency-stop machine switch, not a certified safety-relay/PLd system.

## Practical commissioning test

Before production use:
1. confirm physical vacuum label says `DXV30SAPTA`
2. inspect tool socket/label for any local rating marking that differs from the 2450 W manual
3. plug the 800 W router into the tool socket
4. put DeWalt in automatic/tool mode
5. test router start -> vacuum start
6. test router stop -> ~15 s vacuum run-on
7. test KJD12 stop -> both router and vacuum lose mains immediately, controller loses 24 V
8. restore wall power without pressing KJD12 start -> machine must remain de-energized

If the actual unit's socket label gives a lower limit than the 2450 W manual, the physical label wins.

## Decision

**Use the DXV30SAPTA tool socket for the VEVOR 0700C.**

No separate router-trigger relay or smart vacuum switch is needed for the baseline build.