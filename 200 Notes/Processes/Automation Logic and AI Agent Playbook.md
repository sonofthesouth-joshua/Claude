---
source: _intake/Shadow_Marketing_Media_Operating_System_V3/01_Automation_Logic_and_AI_Agents.docx
source-modified: unknown (uploaded via chat; original filesystem modified-date not preserved by the upload)
ingested: 2026-09-19
via: brain-install starter-kit
---

SHADOW MARKETING MEDIA
AUTOMATION LOGIC & AI AGENT PLAYBOOK
Triggers, actions, guardrails, handoffs, and escalation logic

## Operating Principle

Automation exists to shorten response time, enforce follow-up, protect pipeline visibility, and remove repetitive work. AI may qualify, answer approved questions, book, summarize, and route. It must not invent prices, guarantees, legal terms, client results, or unsupported capabilities.

## Core Automations

- New lead: deduplicate → create/update contact → assign owner → immediate response → create opportunity → task/notification → follow-up cadence.
- Missed call: instant text-back → contact record → owner notification → recovery sequence → stop when conversation, booking, disqualification, or opt-out occurs.
- Revenue Leak Audit: store inputs → calculate modeled leakage → lead score → opportunity → report → booking CTA → sales alert → call-prep brief.
- Chat: capture identity and intent → answer from approved knowledge → qualify → route to audit or 30-minute call → save transcript → human escalation when needed.
- Booking: confirmation → reminders → sales prep brief → pipeline update → no-show recovery if required.
- Proposal: send → follow-up cadence → task reminders → stop on signed, declined, or expired.
- Closed won: payment confirmation → onboarding → access checklist → deployment project → 3–7 day target clock.
- Review/reactivation: trigger only at approved lifecycle milestones and respect opt-outs.

## AI Agent Roles


### Website Concierge

Answers FAQs, captures contact data, recommends audit/booking, and escalates unsupported questions.

### Revenue Audit Analyst

Explains audit outputs as estimates, identifies highest modeled leaks, and produces discovery questions.

### Sales Prep Agent

Summarizes company, audit, interactions, objections, and recommended discovery path before a call.

### Client Success Agent

Summarizes KPIs, dependencies, risks, and next actions without inventing attribution.

### Internal Operations Agent

Surfaces overdue tasks, broken integrations, launch blockers, and accounts at risk.

## Escalation Rules

- Human takeover for pricing exceptions, contract/legal questions, complaints, billing disputes, custom integrations, compliance concerns, or claims outside the approved knowledge base.
- Stop automated outreach on explicit opt-out or when the contact is marked disqualified.
- Do not let parallel automations send duplicate SMS/email sequences.
- Log every material AI action to the contact/account timeline.
