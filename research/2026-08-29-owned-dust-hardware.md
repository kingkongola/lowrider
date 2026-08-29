---
research_date: 2026-08-29
scope: already-owned dust/air-handling hardware relevant to LR4
status: recommendation-ready
decision_state: do not buy a new shop-vac; identify existing DeWalt model, then optimize hose/cyclone around it; investigate old FTX only as secondary air handling
price_basis: already owned; no purchase cost should be assigned to build
region: Sweden
sources_checked:
  - user-provided inventory
  - current LR4 dust-system architecture research
supersedes: any plan to research/buy a new shop-vac before checking the existing DeWalt
---

# Already-owned dust/air hardware

## DeWalt wet/dry vacuum

User already owns a **DeWalt grovdammsugare / shop-vac bought from Jula for about 2,500 SEK**.

Exact model is not yet known.

### Procurement consequence

**Do not buy or research a replacement shop-vac yet.**

The LR4 dust architecture already favours a high-static-pressure wet/dry vacuum behind a cyclone, so an existing mid-range DeWalt unit is likely to be in exactly the right product class.

Before buying hose/adapters/cyclone:
1. identify exact model number from rating plate
2. record nominal hose/port diameter
3. record power and, if published, airflow/vacuum pressure
4. check current filter/bag condition
5. determine whether the tool-socket/auto-start feature exists and is useful

Then build adapters around the actual machine rather than buying a new vacuum.

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

This inventory may remove one of the largest expected dust-system purchases entirely.

Likely remaining dust costs become mostly:
- cyclone separator + rigid bucket/container
- correct flexible 2.5-inch-class moving hose / adapters
- hose support/boom
- dust-shoe brush/material
- antistatic grounding
- simple wipeable curtain/enclosure

The old FTX may additionally eliminate the need to buy a separate ambient air cleaner or enclosure exhaust fan if its condition and airflow are suitable.
