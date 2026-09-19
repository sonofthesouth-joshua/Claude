---
distilled: 2026-09-19
via: bottleneck-finder starter-kit
mode: EXAMPLE — pre-launch reframe, not owner-signed. See 000 OS/install/bottleneck-progress.md.
---

# Friction Map (example pass)

**This is a placeholder, not a signed build queue.** SMM has no live operations, team, or clients yet, so the normal friction interview (what eats your time today) has nothing real to interview. This map instead ranks the *target* operating system — already fully specified in the Step-1 brain — by which piece removes the most friction from reaching a first client. Re-run the real interview once there's a team, a client, or recurring work to observe.

## Top line
**C-01: Revenue Leak Audit Assistant** (conversational, no web app needed) — S-effort build, unblocks the flagship lead magnet immediately instead of waiting on Supabase/Resend/CRM-webhook configuration. Why this first: it's the one candidate that's fully specified in the brain, needs zero external tooling, and directly serves the current priority (get to a first client).

## Ranked table

| Rank | Candidate | Function | Annual value | Effort | Payback | Risk | Confidence | Origin |
|---|---|---|---|---|---|---|---|---|
| 1 | C-01 Revenue Leak Audit Assistant | Sales | `ASSUMPTION` ~$10–18K/yr equivalent (time + faster sales cycle) | S (1–2 days) | Immediate — no dollar cost to build, just agent time | Low | High | friction_detected |
| 2 | C-02 Proposal Drafter | Sales | `ASSUMPTION` ~$4–8K/yr equivalent | S (1–2 days) | Immediate | Low | Medium | friction_detected |
| 3 | C-03 Website Copy Drafter | Marketing | `UNVERIFIED` — blocked on domain/positioning decisions | M (3–8 days) | N/A until unblocked | Low | Low | friction_detected |
| 4 | C-04 Outbound Message Drafter | Marketing | `UNVERIFIED` — blocked on Seamless.AI/Apollo not connected | S (1–2 days) | N/A until unblocked | Low | Low | friction_detected |

*Dollar figures are `ASSUMPTION`-tagged, built on a $150/hr loaded-cost placeholder for Joshua's time (not owner-confirmed) and a guessed 2 prospects/week once outbound starts — they exist to rank candidates relative to each other, not as a real forecast. Treat as directionally useful, not a number to plan around.*

## Per-candidate cards

### C-01 — Revenue Leak Audit Assistant
**Kills:** F-01 (no working audit tool) + F-02 (no call-prep brief generator). **Proposed skill:** a conversational skill that asks for the 12 audit inputs (monthly spend, lead volume, missed-call %, etc. — see [[Revenue Audit Model]]), applies the exact formulas from that note, outputs ranked leak categories with monthly + annualized modeled values (always labeled as estimates, per [[Revenue Leak Audit Engine]]'s output rules), 5–10 tailored discovery questions, and a call-prep brief. **ROI math:** each manual pass (re-deriving formulas + discovery questions from memory) ≈ 2 hrs vs. ≈10 min with the skill → ~1.8 hrs saved/use × `ASSUMPTION` 2 uses/week × 52 × $150/hr ≈ $14K/yr, plus unquantified upside from a sharper, more consistent diagnostic on every call. **Stays human:** the actual sales conversation, any pricing/scope commitment, sending anything to a prospect.

### C-02 — Proposal Drafter
**Kills:** F-03. **Proposed skill:** takes discovery-call notes (situation, diagnosed leaks, recommended scope, term) and drafts a proposal following [[Proposal and Reporting Templates]]'s structure — client situation, evidence, recommended scope, deliverables/exclusions, 3-7 day deployment plan, KPIs, responsibilities, investment/term, change-control, acceptance. **ROI math:** `ASSUMPTION` ~1.5 hrs saved per proposal × 2–4 proposals/month once selling × $150/hr ≈ $4–8K/yr. **Stays human:** final price/term decision, all legal/contract language, sending to the prospect.

## The contrarian callout
The brain's own Master Business OS treats the Revenue Leak Audit as a *web app* (Next.js/Supabase/Resend) — the natural instinct is to prioritize building that. But the audit's actual value is the *model and the conversation it drives*, not the web form. A conversational version removes the same friction today, with zero infrastructure dependency, while the real web app waits on canonical-domain and production-config decisions that are still open (see `000 OS/install/refinement-agenda.md`). Build the reasoning first; wrap it in a web app later if volume justifies it.

## Build queue (proposed — not signed)
1. **C-01 Revenue Leak Audit Assistant** — highest leverage, zero dependency, directly serves "get to first client."
2. **C-02 Proposal Drafter** — same profile, ships right after.
3. **C-03, C-04 parked** — both genuinely blocked (domain/positioning; outbound tooling), not worth forging yet.

---
**Sources:** [[Revenue Leak Audit Engine]], [[Revenue Audit Model]], [[Sales Scripts and Objection Handling]], [[Proposal and Reporting Templates]], [[Master Business OS]], [[Tool Stack]]
**ASSUMPTION:** $150/hr loaded cost for Joshua's time; 2 prospects/week once outbound starts. Both need owner correction.
**UNVERIFIED:** C-03/C-04 dollar values (blocked candidates, not scored).
**CONFLICT:** none.
**Owner sign-off:** not done — this is an example pass per explicit request to bypass the full interview and keep moving. Confirm or correct before treating the build queue as final.
