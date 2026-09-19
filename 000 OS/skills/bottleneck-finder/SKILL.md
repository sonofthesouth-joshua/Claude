---
name: bottleneck-finder
description: Interview + the Step-1 brain → a ranked, owner-readable Friction Map of AI/automation candidates by ROI. Step 2 of the 5-step install (DIY edition).
interactive: true
requires: high_capability
---

# bottleneck-finder (DIY)

Produces the **Friction Map**: a ranked list of automation candidates scored by ROI — readable by a CFO, actionable by Step 3. You don't guess what to automate; the business tells you.

**Hard rules (every phase):**
1. **Read-only.** Query the brain, never mutate it. The Friction Map is a recommendation, not a change.
2. **Consent + privacy.** Any observation of how time is spent is transparent and opt-in. No covert monitoring, no reading private messages. Anything that would feel like spying is out of scope.
3. **Every ROI number cites its source** — a brain KPI, an owner-stated figure, or an explicit `ASSUMPTION` written down. An honest range beats a false point estimate.
4. **Flag, don't guess.** Missing data → `UNVERIFIED`. Conflicts (owner says X, documents say Y) → surface both; the owner rules.
5. **Idempotent.** Checkpoint to `000 OS/install/bottleneck-progress.md`; resume across sessions. On resume, recite the loaded state back and get a confirm before continuing.
6. **Don't drift into Step 3.** This step ranks; it does not build. It ends at "here is the build queue."

## Inputs

- A completed Step 1: `200 Notes/Company/` core docs exist and the brain answers a smoke question ("what does this company do, top clients, tool stack?") from sources. Missing → stop; Step 1 is the prerequisite.
- A loaded hourly cost per role, owner-stated — or derive a defensible placeholder from `Org.md` and mark it `ASSUMPTION`.

## Phase 0 — Preflight

1. Verify the brain (smoke query above). Load the baseline: Org, Tool Stack, processes, KPIs. Write it to the checkpoint file.
2. Confirm hourly cost figures (or mark `ASSUMPTION`).

## Phase 1 — Friction interview

Walk the business function by function (enumerate from `Org.md`: sales, delivery/ops, finance, marketing, support, admin). Capture **frictions, not solutions**.

**Opening question (always first):** *"Do you already have an impression of what you'd want to automate?"* Everything named is tagged `owner_requested` — and every owner-requested item **always appears in the final list**, whatever the data says. The data speaks alongside their wishes, not instead of them.

Per function:
- What recurring tasks eat the most time? (task, who, frequency, minutes each, tools touched)
- Where do things wait, get re-keyed, or bounce between tools/people?
- What breaks or gets dropped when you're busy?
- What do you personally hate doing / keep meaning to fix?

**Structural probes (always run — the best finds are usually here, not in the owner's list):**
- Walk `Org.md` person by person: "what does {name} actually do all day?"
- Single-point-of-failure hunt: "what breaks if {person} is sick for two weeks?"
- Habit hunt: "what do you do simply because it's always been done that way?"

**Time estimates: propose, don't ask cold.** Using the brain's knowledge of roles, propose an estimate per friction and have the owner confirm or correct. Generous but realistic.

Pre-fill from the brain — never ask what the brain already knows; confirm it instead. Each friction gets an id (`F-01…`), description, function, people, frequency, time estimate, and origin tag (`owner_requested` / `friction_detected` / both). Write `000 OS/install/friction-log.md`.

*(Optional, for measured data instead of estimates: have one team member keep a 3–4 day time log of the top candidate task — a two-minute end-of-day note. Skip it by default; estimates are usually enough.)*

## Phase 2 — Candidate synthesis + ROI scoring

Cluster related frictions into **automation candidates**: what an AI skill/routine would do, which tools it touches, what stays human. Score each — every number cites its source:

| Dimension | How |
|---|---|
| **Annual value** | (hrs saved/wk × people × 52 × loaded hourly cost) + quantified quality/risk upside |
| **Build effort** | S ≈ 1–2 days · M ≈ 3–8 days · L ≈ 8+ days (integration count, data availability, edge cases) |
| **Payback** | months until value covers the build: (effort in days × 8 × loaded hourly cost) ÷ monthly value |
| **Risk** | low/med/high — failure blast radius, data sensitivity, human-in-loop need |
| **Leverage** | 0–3: does it unblock a North-Star bottleneck or compound across the business? |

ROI score = annual value, discounted for effort and risk, multiplied by leverage. **Show the math per candidate** — inputs visible, auditable. Tie-break by payback, then lowest risk. Tag each candidate's confidence (High/Med/Low).

## Phase 3 — The Friction Map (deliverable)

Write `200 Notes/Company/Friction Map.md`:

- **Top line:** the #1 candidate, its annual value, payback, and the one-sentence "why this first."
- **Ranked table:** rank · candidate · function · annual value (range) · effort · payback · risk · confidence · origin tag.
- **Per-candidate card** for the top 5: the friction it kills, the proposed skill, the ROI math with sources, what stays human.
- **The contrarian callout** (when present): where the data disagrees with what you planned to automate — stated plainly, with evidence. This is the moment the map earns its keep.
- **Build queue:** the 2–3 candidates Step 3 should forge first, and why.
- Confidence footer: sources, `UNVERIFIED`, `CONFLICT`, `ASSUMPTION` register.

## Phase 4 — Owner sign-off

Walk the map with the owner: validate the ranking, resolve every flag (each ruling stamped `confirmed by {name}, {date}`), lock the cost figures, pick the build queue. Re-rank if rulings move the math.

## Acceptance test (the skill is done when)

- [ ] Every function in `Org.md` interviewed; opening wishlist question + structural probes run
- [ ] Every owner-requested item present in the final list with its origin tag
- [ ] Every ROI number sourced or tagged `ASSUMPTION`
- [ ] `Friction Map.md` exists with a signed-off build queue; zero unresolved flags
- [ ] Run line in `210 Runs/`

**Next:** Step 3 — `/skill-forge` on the build queue (`guides/step-3-skill-forge.md`).
