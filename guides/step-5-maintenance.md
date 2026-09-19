# Step 5 — Turn On Self-Maintenance

**What you're building:** the habit (and eventually the routine) that stops your system from rotting. Every AI setup decays — tools change, goals shift, routines silently stop firing. Static systems die in a quarter; maintained systems compound. This step is the difference.

**Time:** 5 minutes to run; weekly thereafter.

## Run it

> Read and follow `000 OS/skills/system-health/SKILL.md`.

The agent reads the run log, the routines, the skills, and your brain inbox, and writes a health report into `000 OS/reports/`. Open the **Health tab** in your cockpit — the report is there: a status light, the week's numbers, problems with evidence, and specific proposed improvements ("raise the timeout on X — it died twice", "routine Y is enabled but never fired — the scheduler isn't calling it").

It only *recommends*. You approve fixes; the agent applies them in a follow-up session. That approval loop is deliberate — it keeps you the operator, not the bystander.

## Make it weekly

For the first two weeks, run it by hand (the cockpit's "Run health check now" button, or say "run system-health"). Once the report is boringly accurate, make it your first scheduled routine — the kit ships one ready: `000 OS/routines/weekly-health.md` (Mondays 08:00, disabled). Run it by hand three times, then in the cockpit: enable it and hit **⚡ Run automatically on this schedule**.

Pair it with the **weekly inbox habit** from AGENTS.md: during the week, drop new facts and corrections into `200 Notes/Inbox/`; once a week, "process the brain inbox." Ten minutes. The health report will nag you if the inbox piles up — that's it doing its job.

## Done when

A health report exists, renders in the cockpit, and you've acted on (or consciously parked) its first recommendations. From here the system maintains its own momentum — which is the whole point.

→ Final read: `grow-your-system.md` — how to keep building.
