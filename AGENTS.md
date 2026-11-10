# AGENTS.md

This file provides guidance to Codex (claude.ai/code) when working with code in this repository.

## What this repo is

Dokumentation och CAD för ett fysiskt bygge: en **LowRider V4** CNC-fräs (arbetsyta 650 × 1250 mm, Jackpot3, KATSU 101750, Ø30×1,5 mm rör). Repot är källa till sanning för bygget. Det finns inget allmänt applikationsbygge eller lintkommando; CAD-exporterna har egna kontroller och arbetsflöden. Ny text skrivs på **svenska**, kort och sakligt. PrintNC/IndyMill är inte alternativ.

## Canonical-file hierarchy

Top-level files supersede `research/` on any conflict. Each top-level file owns one kind of fact — update the owner rather than duplicating information elsewhere:

- `DECISIONS.md` — locked decisions (D001…); newer ones supersede older only when stated explicitly.
- `BOM.md` — what the build needs and what is already owned/bought.
- `PROCUREMENT.md` — the *only* order matrix for remaining purchases.
- `COSTS.md` — the *only* ledger; actual charged SEK amounts.
- `CHECKLIST.md` — next work in physical order.
- `AUDIT.md` — mechanical/electrical/physical gates; no volatile prices. `AUDIT_2026-09-29.md` is the dated review.
- `SOURCING.md` — dated sourcing evidence/links; must not become an alternative BOM.
- `TABLE.md`, `CABLE_ROUTING.md` — table/deck and cable layers (cable cut lengths are intentionally empty until measured physically).
- `CALIBRATION.md` — calibration protocol + the only measurement log; `machine/` holds `config.yaml` backups pulled from the controller (`http://192.168.50.184/config.yaml`).
- `BUILD_LOG.md` — history only; old choices may live here but are not current state.
- `README.md` — current-status summary and work order; it repeats headline facts (geometry, costs, order status), so keep it in sync when those change.

## Aktuell status kontra historik

Läs `README.md` och `CHECKLIST.md` först. Maskinen är byggd och har fräst; gamla obockade monteringskort är inte dagens återstående byggplan. `docs/arkiv/`, daterad research och äldre loggrader är historik, inte aktuella krav.

För sensorenheten äger `machine/delar/sensorer/README.md` aktuellt CAD-spår och listan över printdelar; `KOPPLING_CORE_V0.md` äger planerad koppling. Senaste arbetsmodellen är `sidotorn.py`. Befintligt `core-build123d.yml` kontrollerar äldre `core_enhet.py`; dess gröna status får inte tillskrivas sidotornet. D020 tar bort armbrytarna, D021 väljer signalpinnar och `CALIBRATION.md` dokumenterar det godkända servoomfånget. Återöppna inte detta som obesvarat utan motsägande ny evidens.

Probmodellen korrigerades 2026-11-10 till **CR Touch Auto Leveling Kit**, nu tillgängligt enligt användaren. `sidotorn.py` är anpassad via `crtouch.py` och en källangiven tredjeparts-STEP. Ny hylsa, kontaktutrymme och provplatta finns; fysisk passning och inkoppling är ännu inte verifierade. Läs `research/2026-11-10-crtouch-anpassning.md` och CAD-underlaget. Återanvänd inte gamla BLTouch-exporter eller beställ en BLTouch av gammal vana.

Fysisk arbetsstatus hålls i `CHECKLIST.md`, mottagning i `PROCUREMENT.md` och mätningar i `CALIBRATION.md`. Journalen i `cnc` äger historik och mjukvarudokumenten programmets funktion; de ska hänvisa till aktuell fysisk status. Skilj ritad, digitalt kontrollerad, printberedd, printad, provpassad och fysiskt verifierad.

Inför printberedning: läs erfarenhetsvärdet för printade hål i `CALIBRATION.md` (2026-11-10). Beakta redan inritad spelmån så att korrigering inte dubbleras; använd inte generell skalning av hela delen som hålkorrigering.

Geometry numbers (tubes 816/816/1505, strut input 819, `front_wing_size=10.8`, GT2 999/1705/1705, minimum table 941 × 1563) appear in several files; change them everywhere or nowhere.

## Work orders (three synced representations)

`WORK_ORDERS.md` (human-readable LR-00…LR-xx one-hour cards with dependencies), `docs/work-orders.json` (same cards as data), and `docs/index.html` (published GitHub Pages site, single large file with inline script, shows the cards with original images) must stay consistent. The site's checkbox state is local to the browser and is **not** SSOT. Status is never assumed: everything is "ej verifierat" until the user reports `klar | delvis | blockerad` with measurements/photos; only then update `WORK_ORDERS.md`, `CHECKLIST.md`, and `BUILD_LOG.md`. Respect ordering gates (e.g. LR-16 before LR-15 and belt tensioning; LR-22 approved before motor tests).

## Assembly guide

`docs/MONTERING_SV.md` is the extended Swedish assembly guide for the actual LR4 + Jackpot3 configuration. It supplements V1E's original images and does not override `DECISIONS.md` or `CHECKLIST.md`.

## Research convention

New research goes in `research/` as a dated Markdown file `YYYY-MM-DD-topic.md` with YAML front matter (`research_date`, `scope`, `status`, `decision_state`, `price_basis`, `region`, `sources_checked`, `supersedes`) — see `research/README.md`. Don't reopen broad component research without a concrete price, stock, compatibility, or integration problem.

## Conventions

- Purchase/receipt facts come from the user's reports; distinguish "ordered", "paid", and "received", and don't mark physical checks done without the user's report.
- Git history uses short prefixed messages (`docs:`, `SSOT:`, `dust extraction:`).
