---
source: _intake/SMM_Operating_Data_Model.xlsx
source-modified: unknown (uploaded via chat; original filesystem modified-date not preserved by the upload)
ingested: 2026-09-19
via: brain-install starter-kit
---

## Migration Fields

| Object | Field | Type | Required | Notes |
| --- | --- | --- | --- | --- |
| Company | company_name | text | Yes | Canonical business name |
| Company | industry | text | Yes | Primary vertical |
| Contact | full_name | text | Yes | Primary person |
| Contact | email | email | Conditional | Store consent/source |
| Contact | phone | phone | Conditional | Store consent/source |
| Lead | lead_source | text | Yes | Original source |
| Lead | lead_score | number | No | Use approved scoring rules |
| Audit | monthly_marketing_spend | currency | No | Revenue Leak Audit input |
| Audit | monthly_lead_volume | number | No | Revenue Leak Audit input |
| Audit | missed_call_pct | percent | No | Revenue Leak Audit input |
| Audit | avg_job_value | currency | No | Revenue Leak Audit input |
| Audit | close_rate | percent | No | Revenue Leak Audit input |
| Opportunity | pipeline_stage | select | Yes | Use CRM Pipeline sheet |
| Opportunity | estimated_value | currency | No | Do not invent |
| Proposal | monthly_fee | currency | Yes | Approved quote |
| Proposal | term_months | number | Yes | 3/6/12 or custom |
| Client | start_date | date | Yes | Contract start |
| Client | package | text | Yes | Approved offer |
| Activity | activity_type | select | Yes | Page/form/chat/call/SMS/email/booking/meeting/proposal |
| KPI Snapshot | period_start | date | Yes | Reporting period |
| KPI Snapshot | period_end | date | Yes | Reporting period |
