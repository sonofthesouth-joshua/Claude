# Step 3 — Forge Your First Agents

**What you're building:** working agents for the top of your build queue. Not SOP documents — runnable skills your agent CLI executes, forged by watching how the work actually happens.

**Time:** per candidate — one recorded run of the process (10–30 min), a 10-minute interview, then the agent forges and tests. Expect an afternoon for your first, faster after.

## Before you start

- Steps 1 and 2 done, build queue signed.
- For each candidate: pick the **process owner** (maybe you) and plan to do the task **once for real while narrating it to the agent in the chat** ("now I copy this into the sheet…"). The agent reads along, asks as you go, and captures the workflow. Imperfect is fine; real beats polished.

## Run it

> Read and follow `000 OS/skills/skill-forge/SKILL.md`. Start with the first candidate in the build queue. The recording is at `<path>`.

The flow per candidate:

1. **Observe** — the agent studies the recording + the artifacts the process produces and writes down the workflow it saw.
2. **Interview** — it asks you the 3–4 things observation can't show: the exceptions, the quality bar, what must stay human, what to do when it breaks. These edge cases are the difference between a demo and an agent you trust.
3. **Forge** — it writes the skill (and a routine file if the task recurs on a schedule).
4. **Test** — dry-run on real or realistic data, sandboxed. Then *you watch it do the work once* and correct it like you'd correct a new hire on day one.

## The safety rule that matters

Any routine the forge creates ships **disabled** and declares its safety envelope: max budget per run, max duration, and `sends_external: false` — nothing emails, posts, or pays anyone on its own. If you ever want an agent to send externally, that's an explicit line you change yourself, eyes open. Keep drafts-first as your default; it's how we run client systems too.

## Done when

Your first 2–3 agents pass their dry-runs and you've watched each one work. They'll appear in the dashboard automatically in Step 4.

→ Next: `step-4-dashboard.md`
