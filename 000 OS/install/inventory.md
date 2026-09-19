---
date: 2026-09-19
phase: 0 — preflight
---

# Corpus inventory

**Source:** files attached to chat by the owner (no external Drive/folder — the corpus is the 5 uploads below, one of which is a package .zip).

## Files received (5 uploads → 11 unique source files after dedupe)

| # | File | Type | Size | Note |
|---|---|---|---|---|
| 1 | `Shadow_Marketing_Media_Master_Business_OS.docx` | docx | 51,719 B | Uploaded twice, byte-identical (md5 `b0caae7f…`) — counted once |
| 2 | `SMM_Operating_Data_Model.xlsx` | xlsx, 6 sheets | 10,365 B | Offers, Services, CRM Pipeline, KPIs, Migration Fields, SOP Index |
| 3 | `Shadow_Marketing_Media_Operating_System_V3.zip` | zip package | 226,330 B | Unpacks to the 8 rows below |
| 3a | ↳ `01_Automation_Logic_and_AI_Agents.docx` | docx | 38,708 B | |
| 3b | ↳ `02_Revenue_Leak_Audit_Engine.docx` | docx | 38,327 B | |
| 3c | ↳ `03_Sales_Scripts_and_Objection_Handling.docx` | docx | 38,542 B | |
| 3d | ↳ `04_Client_Delivery_Checklists.docx` | docx | 38,164 B | |
| 3e | ↳ `05_Roles_Comp_and_Management.docx` | docx | 38,155 B | |
| 3f | ↳ `06_Proposal_and_Reporting_Templates.docx` | docx | 38,132 B | |
| 3g | ↳ `README.txt` | txt | 713 B | Import-order note for this package |
| 3h | ↳ `SMM_AI_Operating_Knowledge.json` | json | 1,173 B | Structured summary — also uploaded standalone as `SMM_Operating_System_V3.xlsx`'s sibling; byte-identical to upload #4 (md5 `518a4f39…`), counted once |
| 4 | `SMM_Operating_System_V3.xlsx` | xlsx, 7 sheets | 10,625 B | Duplicate of 3's copy — filed once, from the zip package |

## Counts by type
- docx: 7 (1 master + 6 playbooks)
- xlsx: 2 (Operating Data Model, Operating System V3)
- json: 1
- txt: 1 (README)
- **Total unique files to file: 11**

## Other checks
- Scanned/image-only PDFs: 0 (no PDFs in this corpus)
- Files >100 MB: 0 (largest is the 226 KB zip)
- Sensitivity-gate scan (payroll/salary, SSN/tax ID, IBAN, medical, "confidential" headers, employment-contract language): **0 hits** across all 11 files — nothing quarantined
- Folder map: flat — no subfolder structure to infer taxonomy from; filing will rely on content

## Scope
All 11 files are business-operations content (company profile, offers/pricing, sales process, automation logic, roles/comp, reporting templates, data-model spec). Nothing resembling HR, payroll, or personal records was found, so no exclusion list is needed from a content-scan standpoint — **owner confirmation still required** (see seed-facts.md and the chat message) before Phase 1 starts, per Hard Rule 3.
