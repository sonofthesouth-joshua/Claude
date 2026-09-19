---
candidate: C-01 (Friction Map)
kills: F-01, F-02
date: 2026-09-19
mode: EXAMPLE — spec-derived, not observed. SMM is pre-launch; there is no real run to watch yet.
---

# Observed workflow — Revenue Leak Audit Assistant

**Substitution note:** skill-forge's Phase 1 normally means watching a real run. There isn't one yet — no prospect has been audited. Instead this was assembled entirely from the brain's own specification of the audit ([[Revenue Audit Model]], [[Revenue Leak Audit Engine]], [[Sales Scripts and Objection Handling]], [[Lead Scoring Model]]), which is detailed enough to forge from directly. **The first real run should replace this file's assumptions with what actually happens.**

## Trigger
Joshua is on a call or message thread with a prospect and wants to run the Revenue Leak Audit live, or wants to prep before a scheduled discovery call.

## Steps
1. Collect the 12 required inputs (ask one at a time if the prospect is live on a call; ask all at once if prepping from notes):
   monthly marketing spend, monthly lead volume, phone-lead %, missed-call %, average closed-job value, gross margin %, current close rate, first-response-time band, % receiving 3+ follow-up attempts, % of open estimates receiving follow-up, open estimates per month, Google rating.
2. Apply the formulas from [[Revenue Audit Model]] exactly:
   - Phone leads = monthly leads × phone-lead %
   - Missed phone leads = phone leads × missed-call %
   - Illustrative missed-call revenue at risk = missed phone leads × close rate × avg job value
   - Follow-up gap leads = monthly leads × (1 − % receiving 3+ attempts)
   - Illustrative follow-up revenue at risk = follow-up gap leads × close rate × avg job value × a **configurable, conservative** recovery factor (default 30% unless Joshua overrides)
   - Stale estimate value at risk = open estimates × avg job value × a **configurable** close/recovery factor (default 20%)
   - Gross profit at risk = modeled revenue at risk × gross margin %
   - Annualized at risk = monthly modeled at risk × 12
3. Rank leak categories (missed calls, slow response, insufficient follow-up, stale estimates, weak reviews, poor pipeline visibility) by modeled impact — no causation claims.
4. Score the lead using [[Lead Scoring Model]]'s point table (revenue band, marketing spend, lead volume, missed-call rate, response time, follow-up gap, open estimates, decision-maker access, timeline, budget).
5. Generate 5–10 tailored discovery questions from [[Sales Scripts and Objection Handling]]'s Core Diagnostic Questions, adapted to whichever leak categories scored highest.
6. Produce a call-prep brief: company snapshot, top 2–3 leaks with numbers, lead score, recommended discovery questions, suggested CTA (30-minute strategy call).
7. Persist the raw inputs, formulas version, outputs, and timestamp — since there's no CRM/database yet, write a dated record to `000 OS/reports/revenue-leak-audits/`.

## Decision points
- Which recovery-factor defaults to use (30% follow-up, 20% stale-estimate) — Joshua can override per-run; the skill must never silently treat these as fixed truths.
- Whether a data point is missing — the skill asks, never assumes a plausible-sounding number.

## Inputs / outputs
- **In:** the 12 audit inputs (numbers/percentages, prospect-supplied or Joshua's best estimate, labeled which).
- **Out:** ranked leak table (monthly + annualized, gross-profit-at-risk), lead score, 5–10 discovery questions, call-prep brief, a persisted record file.

## Frequency
Ad hoc — whenever there's a live prospect. No fixed schedule; not proposed as a Step-4 routine (see SKILL.md — no `sends_external`, no automation trigger, just an on-demand skill).

## Open questions (interview stand-in — answer on first real use)
- **Exceptions:** what happens when a prospect can't answer some inputs (e.g. doesn't track missed-call %)? → default: mark that leak category `UNVERIFIED` in the output rather than guessing a number.
- **Quality bar:** a good output is one Joshua could read straight into a call without editing. First real run will confirm.
- **Judgment calls that stay human:** which leak to lead with in conversation, any pricing/scope talk, whether to run the audit at all with a given prospect.
- **Failure handling:** if formulas produce a negative or nonsensical value (e.g. missed-call % > 100%), flag it and ask for correction rather than showing a broken number.
