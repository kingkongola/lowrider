# Research metadata convention

All new procurement/design research should be saved as a dated Markdown file with YAML front matter.

Required metadata:

```yaml
---
research_date: YYYY-MM-DD
scope: short description
status: exploring | recommendation-ready | locked | superseded
decision_state: short statement
price_basis: observed web prices; re-check at checkout
region: Sweden / EU unless otherwise stated
sources_checked:
  - source/category
supersedes: null or prior research file
---
```

Guidelines:
- Separate **verified specification**, **observed price/stock**, **inference**, and **decision**.
- Prices and stock are observations, not permanent facts. Always record the date and re-check before purchase.
- If a newer research file changes a recommendation, set `supersedes` and mark the older conclusion as stale/superseded when practical.
- Prefer exact manufacturer part numbers / retailer SKUs for variant-sensitive parts.
- Optimize delivered cart total, not isolated line-item price.
