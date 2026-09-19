# Routines — scheduled skills

A **skill** is a capability you invoke. A **routine** is a skill on a schedule ("every morning, run X"). Routines live here, one markdown file each, and the dashboard reads this folder.

A routine **references** a skill — it never duplicates the skill's logic.

## Format

Easiest way: the dashboard's **➕ New routine** form writes this file for you. By hand, the format is (no comments on the frontmatter lines):

```markdown
---
name: morning-brief
description: One-line summary shown in the dashboard
skill: 000 OS/skills/<skill-name>/SKILL.md
schedule: "0 7 * * 1-5"
enabled: false
max_budget_usd: 1.00
max_duration_sec: 600
sends_external: false
---

Run the skill at `<skill path>` with the following standing instructions:
- <what this scheduled run should do, in plain language>
- Append the outcome to `210 Runs/YYYY-MM-DD.md`.
```

`schedule` is cron syntax, but you never need to write it — the dashboard's schedule picker does ("Weekdays · 07:00"). `enabled` is the dashboard toggle. `sends_external` is `false` | `drafts_only` | `true`.

## The safety envelope (non-negotiable)

Every routine MUST declare all three: `max_budget_usd`, `max_duration_sec`, `sends_external`. The dashboard flags any routine missing them, and every run instructs the agent to respect the declared limits and stop cleanly rather than exceed them. Honest note: in this starter kit the limits are a contract the agent follows and the weekly health check audits — not a hard kill-switch layer (that's part of the supervised production setup we install for clients). `sends_external` defaults to `false` — nothing emails, posts, pays, or messages anyone autonomously unless you explicitly set `true`, and even then prefer `drafts_only` (the agent prepares, you send).

## Scheduling

New routines ship `enabled: false`. The dashboard (Step 4) manages everything from there:

- **Run now** (dashboard button, or by hand in your agent: "run the morning-brief routine") — run it on demand until you trust it.
- **⚡ Run automatically** (dashboard → the routine's Settings & schedule) — one click registers it with your Mac's built-in scheduler so it fires at the set time without you; one click removes it. The Advanced expander shows the underlying crontab line for transparency.

Rule of thumb: run by hand three times → enable → schedule.

The Step-5 health check reads this folder and the run log, and will tell you which routines are misconfigured, failing, or never firing.
