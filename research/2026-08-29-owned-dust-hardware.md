---
research_date: 2026-08-29
scope: already-owned dust/air-handling hardware relevant to LR4
status: recommendation-ready
decision_state: do not buy a new shop-vac; existing DeWalt is very likely DXV30SAPTA and is already suitable class; verify rating plate before locking model-specific adapters; investigate old FTX only as secondary air handling
price_basis: already owned; no purchase cost should be assigned to build
region: Sweden
sources_checked:
  - user-provided screenshot showing DeWalt DXV30SAPTA 30 L / 1050 W
  - Jula current DXV30SAPTA product page
  - DXV30SAPTA manual/specification
  - current LR4 dust-system architecture research
supersedes: previous guess that the owned vacuum was DXV38SPTA
---

# Already-owned dust/air hardware

## DeWalt wet/dry vacuum

User already owns a **DeWalt grovdammsugare / shop-vac bought from Jula**.

### Very likely model: `DXV30SAPTA`

User supplied a screenshot of the Jula listing and said this is probably the machine:
- DeWalt `DXV30SAPTA`
- 30 L stainless tank
- 1050 W
- 230 V tool socket with automatic start/stop
- blow function
- current Jula listing price observed 2026-08-29: **1,999 SEK**

Official/manual specifications:
- power: **1050 W**
- seal pressure: **15 kPa**
- airflow: **37.8 L/s = 2268 L/min**
- tank: **30 L stainless steel**
- hose: **48 mm × 2.1 m**
- power cable: 3.05 m

Sources:
- https://www.jula.se/catalog/hem-och-hushall/stad-och-kladvard/dammsugare/grovdammsugare/grovdammsugare-015478/
- https://www.bauhaus.se/media/pdf/1163387A.pdf

**Confidence: very high but still not serial/rating-plate confirmed.** Do not order a proprietary replacement filter or hard adapter solely from this identification until the label is checked.

### Suitability for LR4

This is already a strong match for the planned CNC dust system:
- 15 kPa static pressure is appropriate shop-vac territory for a small router dust shoe
- 37.8 L/s airflow is substantial for a 48 mm hose
- native **48 mm × 2.1 m hose** is especially interesting because 48–50 mm hose sizes have precedent in V1E dust-shoe designs
- automatic tool socket may be useful, though final NVR/machine-power architecture must determine how router/vacuum auto-start is integrated

Therefore **no new vacuum purchase is justified**.

### Procurement consequence

New default is even more aggressive about reuse:
1. confirm model/rating plate when convenient
2. measure actual hose cuff OD/ID with calipers
3. first test the existing **48 mm × 2.1 m hose as the moving LR4 hose**
4. print the dust-shoe/cyclone adapters around the real hose dimensions
5. only buy a separate 2.5-inch hose if the DeWalt hose proves too short, too stiff, too heavy or measurably restrictive in real use

This supersedes the earlier assumption that the DeWalt hose should only be used on the stationary cyclone→vacuum side.

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

This inventory removes the expected vacuum purchase entirely and may also remove the need to purchase a moving hose.

Likely remaining dust costs become mostly:
- printed cyclone
- separate rigid collection can
- printed adapters
- hose support/boom
- dust-shoe brush/material
- antistatic grounding
- simple wipeable curtain/enclosure

The old FTX may additionally eliminate the need to buy a separate ambient air cleaner or enclosure exhaust fan if its condition and airflow are suitable.
