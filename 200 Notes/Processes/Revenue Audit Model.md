---
source: _intake/Shadow_Marketing_Media_Operating_System_V3/SMM_Operating_System_V3.xlsx
source-modified: unknown (uploaded via chat; original filesystem modified-date not preserved by the upload)
ingested: 2026-09-19
via: brain-install starter-kit
---

## Revenue Audit Model

| Metric | Formula / Method | Guardrail |
| --- | --- | --- |
| Phone leads | Monthly leads × phone-lead % | Input-derived |
| Missed phone leads | Phone leads × missed-call % | Do not assume all are lost |
| Illustrative missed-call revenue at risk | Missed phone leads × close rate × avg job value | Label as modeled estimate |
| Follow-up gap leads | Monthly leads × max(0, 1 - % receiving 3+ attempts) | Proxy, not causal proof |
| Illustrative follow-up revenue at risk | Follow-up gap leads × close rate × avg job value × conservative recovery factor | Recovery factor configurable, never guaranteed |
| Stale estimate value at risk | Open estimates × avg job value × configurable close/recovery factor | Use client-specific factor when known |
| Gross profit at risk | Modeled revenue at risk × gross margin % | Separate revenue from gross profit |
| Annualized at risk | Monthly modeled at risk × 12 | Label annualized model |
