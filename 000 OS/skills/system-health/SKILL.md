---
name: system-health
description: Read the run log + routines + skills, write a health report the dashboard displays — status summary, what broke, what to improve next. Step 5 of the 5-step install (DIY edition).
---

# system-health (DIY)

The lite Self-Maintenance Engine: a periodic check that keeps your AgenticOS improving instead of rotting. It reads what actually happened (the run log), compares it against what's supposed to happen (the routines), and writes a report the dashboard renders — summary, problems, and concrete improvements.

Run it **weekly** (by hand, or as your first scheduled routine once you trust it).

**Hard rules:**
1. **Read-only against everything except the report.** The health check observes and recommends; it changes nothing else. Fixes are separate, human-approved actions.
2. **Specific over generic.** Every improvement names the file/routine/skill it refers to and the exact change proposed. "Improve reliability" is banned; "raise `max_duration_sec` on morning-brief from 600 to 900 — it hit the timeout twice this week" is the standard.
3. **Honest about silence.** No runs logged is a finding, not a clean bill. A routine that never fires is a problem to surface, not to skip.

## Steps

1. **Gather (read-only):**
   - `210 Runs/` — last 30 days of run lines (parse date, time, name, outcome).
   - `000 OS/routines/*.md` — frontmatter: name, schedule, enabled, safety envelope.
   - `000 OS/skills/*/SKILL.md` — the skill inventory.
   - `200 Notes/Inbox/` — count of unprocessed items (the weekly brain habit).
   - `000 OS/reports/cron.log` (if present) — scheduled-run errors land here; a dead routine's cause is usually in this file.
   - The previous report in `000 OS/reports/` (to track whether last week's recommendations happened).

2. **Analyze:**
   - **Run summary:** total runs this week vs last, successes / errors / skips per skill+routine.
   - **Failures:** any line containing an error/failed/timeout marker → group by cause, note recurrence.
   - **Dead routines:** `enabled: true` but no matching run lines in the period → misconfigured scheduler or broken invocation.
   - **Safety-envelope gaps:** routines missing `max_budget_usd` / `max_duration_sec` / `sends_external`.
   - **Unused skills:** skills with zero invocations in 30 days — candidates to improve, schedule, or archive.
   - **Brain hygiene:** unprocessed Inbox count; days since the last `Company/` core-doc correction (a brain nobody corrects is drifting).
   - **Last report follow-through:** which of the previous recommendations happened (visible in runs/files), which are still open.

3. **Report — write `000 OS/reports/health-YYYY-MM-DD.md`:**

```markdown
---
date: YYYY-MM-DD
period: last 7 days (trends vs prior 30)
status: green | yellow | red
---
# System Health — YYYY-MM-DD

## Summary
One paragraph: overall state, the single most important thing to fix this week.

## The numbers
| Metric | This week | Trend |
|---|---|---|
| Runs / successes / errors | … | … |
| Active routines (firing / enabled) | … | … |
| Skills used / total | … | … |
| Inbox items waiting | … | … |

## Problems found
- ❗ <problem> — <evidence: file/line> — <proposed fix>

## Improvements proposed
1. <specific change, file named> — <why, evidence>
2. …

## Carried from last report
- <recommendation> — done / still open
```

   `status`: red = a routine is failing or an envelope is missing; yellow = dead routines, growing inbox, or no runs at all; green = everything firing and clean.

4. **Wrap:** append a run line to `210 Runs/` (`system-health · status=<color> · problems=<n>`). The dashboard picks the report up automatically. Do NOT apply any fix in the same session unless the human explicitly asks — recommendations first, changes on approval.

## Acceptance test

- [ ] Report exists in `000 OS/reports/` with status, numbers, problems (with evidence), and specific improvements
- [ ] Every enabled-but-silent routine and every envelope gap is surfaced
- [ ] Previous report's recommendations tracked
- [ ] Run line written; nothing else modified

**Grow from here:** `guides/grow-your-system.md` — creating new skills and routines, and keeping them healthy over time.
