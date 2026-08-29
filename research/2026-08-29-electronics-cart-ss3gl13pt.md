---
research_date: 2026-08-29
scope: earlier electronics cart optimization after correcting LR4 endstop to SS-3GL13PT
status: superseded
decision_state: superseded by final HDR-60-24 + SS-3GL13PT + LaskaKit wiring order strategy
price_basis: historical observations from 2026-08-29; do not use for purchase without the superseding file
region: Sweden / EU
sources_checked:
  - V1 Engineering Jackpot3 documentation and forum wiring threads
  - DigiKey Sweden
  - Farnell Sweden
  - RS Sweden
  - Mouser Europe
supersedes: research/2026-08-29-electronics-cart.md
superseded_by: research/2026-08-29-final-psu-endstop-wiring-cart.md
---

# Superseded electronics-cart research

This file captured the intermediate comparison between `LRS-100-24`, `GST60A24-P1J`, exact Omron `SS-3GL13PT`, distributor freight thresholds and endstop-terminal options.

Its cart decision is stale.

Use instead:
- `research/2026-08-29-final-psu-endstop-wiring-cart.md`

The superseding research locks the current recommendation to:
- Mean Well **HDR-60-24** from DigiKey
- **10 × Omron SS-3GL13PT** from the same DigiKey order (5 installed + 5 cheap spares)
- endstop and short 24 V cable added to the already-needed LaskaKit order
- soldered COM + NC switch termination by default
- no separate cable order and no PSU added to the StepperOnline motor order

Historical details remain available in Git history if needed.