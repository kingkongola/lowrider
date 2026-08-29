---
research_date: 2026-08-29
scope: already-owned dust/air-handling hardware relevant to LR4
status: recommendation-ready
decision_state: do not buy a new shop-vac; existing DeWalt is likely DXV38SPTA and is already suitable class; verify label before locking adapters; investigate old FTX only as secondary air handling
price_basis: already owned; no purchase cost should be assigned to build
region: Sweden
sources_checked:
  - user-provided inventory
  - Jula current DeWalt vacuum listings
  - DeWalt DXV38SPTA published/manual specifications
  - current LR4 dust-system architecture research
supersedes: any plan to research/buy a new shop-vac before checking the existing DeWalt
---

# Already-owned dust/air hardware

## DeWalt wet/dry vacuum

User already owns a **DeWalt grovdammsugare / shop-vac bought from Jula for about 2,500 SEK**.

### Likely model: `DXV38SPTA`

Current Jula listing is an unusually close match to the user's description:
- DeWalt `DXV38SPTA`
- current Jula price **2,499 SEK**
- 38 L tank
- 1250 W
- 230 V tool socket with automatic start/stop
- 48 mm × 2.1 m hose
- airflow **2550 L/min = 42.5 L/s**
- published seal pressure **17 kPa**
- washable cartridge filter, nominal 5 µm / 95 % on Jula page

Sources:
- https://www.jula.se/catalog/hem-och-hushall/stad-och-kladvard/dammsugare/grovdammsugare/grovdammsugare-030849/
- DXV38SPTA manual/spec references

**Confidence: high but not confirmed.** A historical Jula purchase around 2,500 SEK could still be another DeWalt model. Confirm the rating plate before ordering model-specific adapters/filters.

### Suitability for LR4 if confirmed

This is already a strong match for the planned CNC dust system:
- 17 kPa static pressure is shop-vac territory and well suited to a small dust shoe
- 42.5 L/s is ample source-capture airflow for this class when hose losses are controlled
- 48 mm native hose is close enough to the LR4 2.5-inch dust-shoe class that a short printed/tapered adapter is straightforward
- automatic tool socket may be useful, though final machine-power/NVR architecture must be checked before relying on it

Therefore **no new vacuum purchase is justified**.

### Procurement consequence

Before buying hose/adapters/cyclone:
1. confirm exact model number from rating plate
2. confirm actual existing hose/port dimensions
3. inspect cartridge filter/bag condition
4. decide whether the 48 mm DeWalt hose is used only from cyclone→vacuum while a lighter 2.5-inch moving hose is used from LR4→cyclone

The last arrangement is currently preferred because it keeps the moving hose flexible while preserving the DeWalt's native connection on the stationary side.

## Old FTX ventilation unit

User also has an **older FTX heat-recovery ventilation unit lying unused**. Exact make/model, fan capacity and filter format are unknown.

This is potentially valuable, but it should not be treated as the primary CNC chip extractor.

### Good possible uses

After model identification, investigate it for one of these secondary roles:

1. **negative-pressure enclosure extraction**
   - pull a modest continuous airflow from the CNC curtain/enclosure
   - primary dust shoe/shop-vac still captures chips at source
   - FTX/ventilation side handles the fine airborne leakage that escapes source capture

2. **garage ambient air cleaner / recirculator**
   - if the fan/filter section can be used conveniently with a large disposable prefilter/fine filter
   - useful after MDF/XPS/wood cutting to reduce residual airborne dust

3. **purge/exhaust after dirty jobs**
   - move enclosure/garage air outdoors for a short period after cutting

### Uses to avoid

Do **not** route raw router chips/XPS debris directly into the FTX heat exchanger/fans.

Reason:
- domestic ventilation units are not chip collectors
- coarse dust will foul the heat exchanger and fan impellers quickly
- their filters are designed for ventilation air, not for the dust loading produced at a CNC cutter

The correct hierarchy remains:

`dust shoe -> cyclone -> DeWalt shop-vac`

with FTX, if useful, operating only as a **secondary airborne-dust / enclosure-air system**.

### What to record from the FTX label

Before designing around it:
- manufacturer + exact model
- rated supply/extract airflow, ideally m³/h
- fan power
- duct connection diameter
- filter classes/sizes
- whether fans can be controlled independently
- whether bypassing/removing the heat exchanger is practical
- physical size and noise

## Current dust-system cost impact

This inventory removes the expected vacuum purchase entirely.

Likely remaining dust costs become mostly:
- cyclone separator + rigid bucket/container
- correct flexible 2.5-inch-class moving hose / adapters
- hose support/boom
- dust-shoe brush/material
- antistatic grounding
- simple wipeable curtain/enclosure

The old FTX may additionally eliminate the need to buy a separate ambient air cleaner or enclosure exhaust fan if its condition and airflow are suitable.
