---
name: welcome
description: First-run setup and orientation — check the machine, fix what's missing (with permission), orient the owner, and hand off to Step 1. Run this before anything else in the kit.
interactive: true
---

# welcome

The kit's front door. The human running you may have **never used a terminal before** — they followed `guides/step-0-setup.md`, installed an agent CLI, and typed one sentence. From here, everything is your job: check their machine, adapt to what you find, fix gaps one at a time, and get them confidently to Step 1.

**Hard rules:**
1. **One thing at a time, plain language.** No jargon without a one-line explanation. Never dump a list of ten problems — check, report, fix, next.
2. **Never install or change anything without saying what and why, and getting a yes.**
3. **Adapt to their system** (macOS / Windows / Linux) — detect it, give instructions for *their* OS only.
4. **No credentials in chat, ever** (AGENTS.md rule 1). Nothing in this setup needs a key; refuse any pasted secret.
5. **Idempotent.** Safe to re-run anytime; write findings to `000 OS/install/setup-status.md` and update it on re-runs.

## Phase 1 — Hello + the map (1 minute)

Greet them briefly. Explain in three sentences what this kit builds: a business brain (Step 1), a ranked automation map (Step 2), their first working agents (Step 3), a dashboard to control it all (Step 4), and a health check that keeps it improving (Step 5). Tell them this session is just a machine check — 5 minutes, nothing scary.

## Phase 2 — Machine check (one item at a time, fix as you go)

Run each check yourself (shell commands), explain the result in one line, and fix problems before moving on:

1. **Where are we?** `pwd` — the vault must be in a plain local path. Red flags: a path containing `Documents`, `Desktop`, `Mobile Documents`, `OneDrive`, `Dropbox`, `Google Drive` (cloud sync breaks agent file access), or a **dot in the username's home segment** (e.g. `/Users/f.a./…` — breaks some CLI file readers). If misplaced: explain the problem, then give them the exact recovery ritual — **type `/exit` to close this session, move the folder in Finder/Explorer to the home folder, open a fresh terminal, `cd` into the folder's new location (type `cd ` and drag the folder in), run the agent again, and re-run this welcome skill** (it's safe to re-run; it picks up where it left off). Never try to move the folder yourself while running from inside it.
2. **Can I write?** Create and delete a scratch file in the vault. If blocked (macOS permission popup): tell them to click Allow, retry.
3. **Git present?** `git --version`. Missing on macOS → it will offer the Command Line Tools popup; tell them to accept and wait (~5 min), then retry. Missing on Windows/Linux → guide the standard install for their OS. Then check `git config user.name` and `user.email` — on a fresh machine they're unset and commits fail. If unset, ask for their name and email (explain: it's just the label on the vault's history, stays on this computer, any email works) and set them. Then: if the vault isn't a repo yet, `git init` + first commit ("Day zero") — explain in one line why (time machine for their brain; nothing leaves the computer).
4. **Python 3.10+?** `python3 --version`. Only needed for the Step-4 dashboard — if missing, note it in the status file and say we'll fix it when we reach Step 4 (macOS: comes with the git tools above; Windows: python.org installer, tick "Add to PATH"). Don't block setup on it.
5. **The run log works.** Append the first line to `210 Runs/{today}.md`: `- HH:MM welcome (manual) · setup check started`. Explain: every agent session logs one line here — it's the system's memory, and the dashboard reads it.

Write results to `000 OS/install/setup-status.md`: each check, its state (OK / fixed / deferred), and the date. Re-runs update in place.

## Phase 3 — Orientation (2 minutes)

- **Their pace:** Step 1 needs 2–4 hours of agent time but only ~30 min of theirs, and it checkpoints — stopping anytime is safe.
- **One question:** "Do you have a folder (or Drive export) with your company documents — offers, processes, client docs?" If yes → they're ready for Step 1 now. If no → their only homework: gather that folder (point them to the "Before you start" list in `guides/step-1-brain.md`), come back, and say "start Step 1".
- **Optional, not required:** Obsidian (free) is a pleasant way to *read* the vault — mention it once, don't push it.
- **How to come back:** open Terminal → `cd` into this folder → `claude`. Any time. Suggest they keep the terminal command written down somewhere.

## Phase 4 — Hand off

- Update `setup-status.md` to its final state; append the run-log line (`setup complete · N checks OK, M fixed, K deferred`).
- If their corpus is ready and they're willing: offer to start Step 1 right now — "Read and follow `000 OS/skills/brain-install/SKILL.md`" — and carry straight on.
- If not: close with the exact sentence to type next time ("Read and follow `000 OS/skills/brain-install/SKILL.md`. My documents are at <folder>."), and where the guides live.

## Acceptance test (the skill is done when)

- [ ] Location, write access, and git are green (or explicitly fixed); Python state recorded (OK or deferred to Step 4)
- [ ] Vault is a git repo with at least one commit
- [ ] `000 OS/install/setup-status.md` exists and is current; run-log lines written
- [ ] The human knows exactly what to do next, in one sentence
