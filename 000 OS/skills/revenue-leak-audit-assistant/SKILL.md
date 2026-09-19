---
name: revenue-leak-audit-assistant
description: Run SMM's Revenue Leak Audit conversationally with a live prospect or from discovery-call notes — compute modeled revenue-at-risk, rank leak categories, score the lead, and produce a call-prep brief. No web app or CRM required.
interactive: true
candidate: C-01 (Friction Map, 2026-09-19)
kills: F-01, F-02
status: beta — dry-run tested (formulas + lead score verified against a fictional example, see 000 OS/reports/revenue-leak-audits/), not yet used on a real prospect or watched by Joshua
---

# revenue-leak-audit-assistant

Turns the 12 Revenue Leak Audit inputs into the same diagnostic output the target web app would produce — modeled revenue-at-risk by leak category, a lead score, discovery questions, and a call-prep brief — entirely inside a conversation. Built because the web app (Next.js/Supabase/Resend) isn't configured yet (see [[Tool Stack]]), but the underlying model is fully specified and doesn't need it.

**Hard rules:**
1. **Never invent a number.** Every input comes from the prospect or from Joshua's explicit best-guess (labeled which). Missing input → ask, or mark that leak category `UNVERIFIED` in the output — never assume a plausible-sounding figure.
2. **Estimates, not promises.** Every dollar figure is labeled "modeled" or "illustrative." Never present revenue-at-risk as guaranteed or already-recovered revenue (per [[Revenue Leak Audit Engine]]'s output rules and the AI Knowledge Base Rules in [[Master Business OS]] §19).
3. **Configurable factors stay visible.** The follow-up recovery factor (default 30%) and stale-estimate recovery factor (default 20%) are assumptions, not facts — show them next to any number that uses them, and let Joshua override per-run.
4. **Nothing sends externally.** This skill produces a call-prep brief for Joshua to use himself. It never emails, texts, or messages the prospect. No `sends_external` capability — there's no routine here to declare one for.
5. **No credentials, no CRM writes.** There's no CRM yet; this skill only reads the brain and writes a local record file — never touches `200 Notes/Admin/Credentials/`.

## Trigger
Joshua invokes this before or during a conversation with a prospect — live on a call, or from notes taken after one.

## Inputs (ask for what's missing; accept "unknown" for any of them)
1. Monthly marketing spend
2. Monthly lead volume
3. Phone-lead percentage
4. Missed-call percentage
5. Average closed-job value
6. Gross margin percentage
7. Current close rate
8. First-response-time band
9. Percentage receiving 3+ follow-up attempts
10. Percentage of open estimates receiving follow-up
11. Open estimates per month
12. Google rating

## Steps
1. Collect the 12 inputs above (skip any the prospect can't answer — mark unknown, don't guess).
2. Compute, per [[Revenue Audit Model]]:
   - Phone leads = monthly leads × phone-lead %
   - Missed phone leads = phone leads × missed-call %
   - Illustrative missed-call revenue at risk = missed phone leads × close rate × avg job value
   - Follow-up gap leads = monthly leads × (1 − % receiving 3+ attempts)
   - Illustrative follow-up revenue at risk = follow-up gap leads × close rate × avg job value × recovery factor (default 30%, ask Joshua to confirm/override)
   - Stale estimate value at risk = open estimates × avg job value × recovery factor (default 20%, ask Joshua to confirm/override)
   - Gross profit at risk = modeled revenue at risk × gross margin %
   - Annualized at risk = monthly modeled at risk × 12
   - Any leak category with a missing input → show as `UNVERIFIED`, not zero.
3. Rank leak categories (missed calls, slow response, insufficient follow-up, stale estimates, weak reviews, poor pipeline visibility) by modeled monthly impact — descending, no causation language.
4. Score the lead using [[Lead Scoring Model]]'s point table. Four of its signals aren't among the 12 audit inputs — ask them separately, only for scoring: **annual revenue band**, **is a decision-maker engaged in this conversation**, **implementation timeline**, and **rough monthly budget expectation**. Skip any the prospect won't share yet; score only on what's answered and note which signals are `UNVERIFIED`. Show the running total and which signals drove it.
5. Generate 5–10 discovery questions from [[Sales Scripts and Objection Handling]]'s Core Diagnostic Questions, weighted toward the top-ranked leak categories.
6. Produce a call-prep brief: one-paragraph company snapshot, top 2–3 leaks with monthly + annualized numbers and their assumptions, lead score, the discovery questions, and a suggested close (schedule the 30-minute strategy call).
7. Write a dated record to `000 OS/reports/revenue-leak-audits/YYYY-MM-DD-<prospect-slug>.md`: raw inputs, formula version (this SKILL.md's date), outputs, timestamp. This is the audit's persistence layer until a real CRM exists.

## What stays human
Which leak to lead the conversation with. Any pricing, scope, or contract discussion. Whether to run the audit with a given prospect at all. Sending anything to the prospect — this skill only produces Joshua's own prep material.

## Exceptions
- Prospect can't answer an input → mark `UNVERIFIED`, compute what's computable from the rest, don't block the whole audit on one missing number.
- A computed value is negative or out of a sane range (e.g., a percentage input > 100) → flag it and ask for correction instead of showing a broken number.

## Acceptance test
- [ ] Given a full set of 12 realistic inputs, produces correct arithmetic for every formula in [[Revenue Audit Model]] (spot-checked by hand)
- [ ] Every dollar figure is labeled modeled/illustrative; recovery-factor assumptions are shown, not hidden
- [ ] Missing inputs produce `UNVERIFIED` leak categories, not fabricated numbers or silent zeros
- [ ] Lead score matches [[Lead Scoring Model]]'s point table for the same inputs, including the 4 scoring-only questions not in the core 12
- [ ] Output record is written to `000 OS/reports/revenue-leak-audits/`
- [ ] Nothing sends externally; nothing touches Admin/Credentials

## Failure handling
If a formula can't be computed (missing inputs, invalid values), say so plainly in the output next to that line rather than omitting it silently — Joshua should see exactly what's known vs. not.
