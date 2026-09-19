---
source: _intake/Shadow_Marketing_Media_Operating_System_V3/SMM_Operating_System_V3.xlsx
source-modified: unknown (uploaded via chat; original filesystem modified-date not preserved by the upload)
ingested: 2026-09-19
via: brain-install starter-kit
---

## Automation Logic

| Automation | Trigger | Conditions | Actions | Stop Conditions | Owner | KPI |
| --- | --- | --- | --- | --- | --- | --- |
| New Lead Speed-to-Lead | New lead created | Valid phone/email; not duplicate | Assign owner; immediate SMS/email; task/call notification; start follow-up sequence | Reply; booked; disqualified; opt-out | Sales | Median response time |
| Missed Call Recovery | Inbound call missed | Known or new lead | Immediate text-back; create/update contact; notify owner; task | Conversation started; booked; opt-out | Sales | Missed-call recovery rate |
| Audit Submitted | Revenue Leak Audit submitted | Required fields complete | Store audit; score; create opportunity; email report; prompt booking; alert sales | Booked; disqualified | Sales | Audit-to-booking rate |
| Chat Qualified | Chat captures contact + intent | Qualification threshold met | Create lead; attach transcript; score; offer audit/booking; alert owner | Booked; human takeover; opt-out | Sales | Chat-to-lead rate |
| Appointment Booked | 30-min call booked | Within approved calendar | Confirmation; reminders; prep brief; pipeline update | Completed; cancelled | Sales | Show rate |
| No Show | Meeting status no-show | No reschedule already booked | Recovery SMS/email; task; reschedule link | Rescheduled; opt-out | Sales | No-show recovery rate |
| Proposal Sent | Proposal sent | Qualified opportunity | Follow-up cadence; reminders; pipeline update | Signed; declined; expired | Closer | Proposal close rate |
| Closed Won | Agreement + payment confirmed | Payment cleared | Create client; onboarding form; access checklist; project; deployment SLA | Onboarding complete | Client Success | Time-to-launch |
| Review Request | Approved customer milestone | Client-defined success event | Send review request; reminder; log result | Review received; opt-out | Client Success | Review request conversion |
| Reactivation | Lead/customer inactive threshold | Eligible; no open opportunity | Segmented reactivation sequence; create task on reply | Reply; booked; opt-out | Sales | Reactivation rate |
