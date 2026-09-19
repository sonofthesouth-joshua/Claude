# Growing Your System — skills, routines, and keeping them healthy

You've run the five steps. This is the operating manual for everything after: how to keep adding agents and how to keep them trustworthy. Ten minutes now, then keep it as a reference.

## The mental model

- **Skill** = one self-contained capability, written as markdown instructions an agent can follow (`000 OS/skills/<name>/SKILL.md`). Your SOPs, made runnable.
- **Routine** = a skill on a schedule with a safety envelope (`000 OS/routines/<name>.md`). Your org chart of recurring work, made autonomous.
- **The brain** feeds both — a skill that knows your voice, clients, and tools writes like your business, not like a generic bot.

New capability? Write a skill. Should it recur? Wrap it in a routine. Never put logic in the routine — routines *reference* skills.

## Creating a new skill (the honest shortcut: reuse the forge)

For any new recurring task, run Step 3 again:

> Read and follow `000 OS/skills/skill-forge/SKILL.md` for a new candidate: <describe the task>. Here's a recording of me doing it once: <path>.

Record yourself doing the task, answer the 3–4 edge-case questions, watch the dry-run, correct it once. That loop — observe, interview, forge, test — is how every good agent gets built; resist the urge to just prompt one into existence. Skills born from real runs survive contact with reality; skills born from imagination don't.

Quality bar for any SKILL.md (the forge enforces this shape):
- Purpose, trigger, inputs
- Ordered steps with decision rules
- **What stays human** — written explicitly
- Exceptions and failure handling
- An acceptance test ("this skill is done when…")

## Creating a routine

1. The skill exists and has run cleanly by hand at least three times.
2. Copy the template from `000 OS/routines/README.md`. Declare the full safety envelope: `max_budget_usd`, `max_duration_sec`, `sends_external: false` (or `drafts_only`).
3. Run it by hand ("run the <name> routine") three times. Then enable in the cockpit, then schedule (cron/launchd calling your agent CLI headless).
4. Watch its first week in the run log.

**The sends-external line is sacred.** Drafts by default, forever. Flip `sends_external: true` only for a routine you'd bet a client relationship on, and only after weeks of clean drafts.

## The maintenance rhythm

| Cadence | Ritual |
|---|---|
| Every session | Agents append one line to `210 Runs/` — no exceptions; it's the system's memory |
| Weekly | `system-health` run + process `200 Notes/Inbox/` into the brain (10 min) |
| Monthly | Read the health trend: prune skills nobody used, fix or retire dead routines, and ask "what changed in the business that the brain doesn't know yet?" |
| Quarterly | Re-run the Bottleneck Finder. Your #1 friction moved — the map should too |

Two failure smells to act on immediately: a routine that errors twice the same way (fix or disable, never let it grind), and a brain answer that's confidently out of date (drop the correction in the Inbox, this week).

## When you outgrow DIY

Signals: you want routines running unattended on a machine that isn't your laptop; agents that touch email/CRM/invoicing with real supervision; more than ~10 agents; or you simply stopped having evenings for this. That's the line where we usually come in — the done-with-you install is these same five steps, plus the infrastructure, supervision layer, and accountability to have it live in three weeks: [semprasystems.com](https://semprasystems.com).

Until then: keep forging. The compound effect is real — every skill makes the next one easier, and the brain makes them all smarter.
