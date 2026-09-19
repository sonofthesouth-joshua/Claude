---
source: _intake/Shadow_Marketing_Media_Operating_System_V3/02_Revenue_Leak_Audit_Engine.docx
source-modified: unknown (uploaded via chat; original filesystem modified-date not preserved by the upload)
ingested: 2026-09-19
via: brain-install starter-kit
---

SHADOW MARKETING MEDIA
REVENUE LEAK AUDIT ENGINE
Diagnostic model, scoring framework, outputs, and sales handoff

## Purpose

The audit turns operational friction into a measurable sales conversation. It is a diagnostic model, not a promise of recoverable revenue.

## Required Inputs

- Monthly marketing spend
- Monthly lead volume
- Phone-lead percentage
- Missed-call percentage
- Average closed-job value
- Gross margin percentage
- Current close rate
- First-response-time band
- Percentage receiving 3+ follow-up attempts
- Percentage of open estimates receiving follow-up
- Open estimates per month
- Google rating

## Model Logic

- Phone leads = monthly leads × phone-lead percentage.
- Missed phone leads = phone leads × missed-call percentage.
- Illustrative missed-call revenue at risk = missed phone leads × current close rate × average job value.
- Follow-up gap = monthly leads × the share not receiving 3+ attempts. Apply a configurable conservative recovery factor before assigning modeled revenue.
- Stale estimate value at risk = open estimates × average job value × configurable recovery/close factor.
- Gross profit at risk = modeled revenue at risk × supplied gross margin.
- Annualized modeled risk = monthly modeled risk × 12.

## Output Rules

- Show monthly and annualized modeled values separately.
- Show assumptions next to outputs.
- Rank leak categories by modeled impact without claiming causation.
- Generate 5–10 tailored discovery questions.
- CTA: schedule a 30-minute strategy call.
- Persist raw inputs, formulas/version, output, timestamp, source, and contact record.

## Lead Scoring

Use fit + pain + authority + urgency. Strong signals include $500K–$20M+ revenue, existing marketing spend, meaningful lead volume, measurable response/follow-up gaps, decision-maker involvement, and a 30-day implementation horizon. Keep thresholds configurable.
