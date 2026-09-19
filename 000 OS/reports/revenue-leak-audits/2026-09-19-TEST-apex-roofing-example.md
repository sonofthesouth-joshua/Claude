---
type: TEST RUN — fictional example prospect, not a real audit
skill: revenue-leak-audit-assistant
skill-version: 2026-09-19
run-date: 2026-09-19
---

# Revenue Leak Audit — TEST (Apex Roofing, fictional)

**This is a dry-run acceptance test, not a real audit.** "Apex Roofing" is a made-up example used to verify the skill's arithmetic against [[Revenue Audit Model]] and [[Lead Scoring Model]] before shipping. Do not treat any figure here as a real prospect's numbers.

## Inputs (test data)
| Input | Value |
|---|---|
| Monthly marketing spend | $6,000 |
| Monthly lead volume | 80 |
| Phone-lead % | 70% |
| Missed-call % | 15% |
| Average closed-job value | $9,500 |
| Gross margin % | 35% |
| Current close rate | 25% |
| First-response-time band | 15–30 min |
| % receiving 3+ follow-up attempts | 40% |
| % of open estimates receiving follow-up | 50% |
| Open estimates per month | 12 |
| Google rating | 4.3 |

Recovery factors used: follow-up 30% (default), stale-estimate 20% (default) — both flagged to the test as adjustable, not fixed.

## Computed leak categories (ranked by monthly modeled impact)

| Rank | Leak | Monthly revenue at risk (modeled) | Monthly gross profit at risk | Annualized revenue at risk |
|---|---|---|---|---|
| 1 | Insufficient follow-up | $34,200 | $11,970 | $410,400 |
| 2 | Stale/unworked estimates | $22,800 | $7,980 | $273,600 |
| 3 | Missed calls | $19,950 | $6,982.50 | $239,400 |

**Arithmetic check (by hand, against [[Revenue Audit Model]]):**
- Phone leads = 80 × 0.70 = 56. Missed phone leads = 56 × 0.15 = 8.4. Missed-call revenue at risk = 8.4 × 0.25 × $9,500 = $19,950/mo. ✅.
- Follow-up gap leads = 80 × (1 − 0.40) = 48. Follow-up revenue at risk = 48 × 0.25 × $9,500 × 0.30 = $34,200/mo. ✅
- Stale estimate value at risk = 12 × $9,500 × 0.20 = $22,800/mo. ✅
- Gross profit at risk = revenue at risk × 35% margin, per category. ✅
- Annualized = monthly × 12. ✅

All labeled as modeled/illustrative, per output rule.

## Lead score
Two categories of signal: the 12 audit inputs above, plus 4 scoring-only questions the skill now asks separately (this test is what surfaced the need for them).

| Signal | Test answer | Points |
|---|---|---|
| Annual revenue $2M–$20M+ | $3M (test-assumed) | +20 |
| Marketing spend ≥ $5K/mo | $6,000 | +15 |
| 50+ leads/mo | 80 | +10 |
| Missed calls ≥ 10% | 15% | +10 |
| Response time > 15 min | 15–30 min band | +10 |
| Follow-up < 3 attempts | 60% don't get 3+ | +10 |
| Open estimates/opportunities present | 12 | +10 |
| Decision-maker engaged | yes (test-assumed) | +15 |
| Timeline ≤ 30 days | yes (test-assumed) | +10 |
| **Total** | | **120** |

Matches [[Lead Scoring Model]]'s point table for these inputs. ✅ Strong-fit signals dominate — consistent with the model's description of a strong lead.

## Call-prep brief (sample output)
> **Apex Roofing** — 80 leads/mo, $6K/mo ad spend, 4.3★ Google rating. Biggest leak: **follow-up gap** — 60% of leads never get 3+ contact attempts, an estimated $34.2K/mo in modeled revenue at risk (illustrative). Stale estimates close behind at $22.8K/mo modeled. Lead score: 120 (strong fit). Lead with follow-up-process questions, then stale-estimate ownership. Suggested close: 30-minute strategy call.

## Result
✅ Acceptance test passed — formulas correct, estimates labeled, lead score matches the model, missing-input handling not exercised in this run (all 16 inputs were supplied). Skill is ready to use on a real prospect; **not yet reviewed by Joshua** (Phase 4's "process owner watches it once" step is still open — do that on the first real prospect).
