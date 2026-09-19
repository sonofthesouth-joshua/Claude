---
name: weekly-health
description: Weekly system health check — the kit's example routine (Step 5 makes it your first scheduled one)
skill: 000 OS/skills/system-health/SKILL.md
schedule: "0 8 * * 1"
enabled: false
max_budget_usd: 0.50
max_duration_sec: 600
sends_external: false
---

Run the skill at `000 OS/skills/system-health/SKILL.md` with these standing instructions:
- Produce this week's health report and keep it specific (name files and routines).
- Append the outcome to `210 Runs/YYYY-MM-DD.md`.
