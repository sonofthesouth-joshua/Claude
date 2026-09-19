# AGENTS.md — Operator manual for this vault

> Engine-neutral manual. ANY agent working in this vault (Claude Code today, another LLM runtime tomorrow) reads this first, every session. Engine-specific notes live in CLAUDE.md.

## What this vault is

The AI business brain of the company that owns it, built with the AgenticOS Starter Kit (Sempra Systems). It holds company knowledge as plain markdown in the numbered taxonomy below, plus the skills that operate on it.

## Taxonomy (don't rename top-level folders — the numbers matter)

- `000 OS/` — system core: skills, routines, dashboard, install staging, health reports. Not company content.
- `100 Periodics/` — daily/weekly notes, created through use.
- `150 Clients/` — one folder per customer of this company.
- `200 Notes/` — the knowledge base. `Company/` holds the **brain core** (profile, org, offer & pricing, clients overview, tool stack, KPIs, glossary, voice & tone, 🌟 North Star) — distilled, owner-verified, highest-trust tier. `Archive-Imported/` is the unclassified holding pen. `Inbox/` is where new facts wait for weekly processing.
- `210 Runs/` — run log: every agent session appends one line to `210 Runs/YYYY-MM-DD.md` (time, what ran, outcome). The dashboard and the Step-5 health check read this file — never skip it.
- `999 Archive/` — nothing is ever hard-deleted; superseded *files* move here with a date prefix. Superseded *facts* stay in place with a `superseded-by:` frontmatter pointer.

## Hard rules for any agent in this vault

1. **Credentials** live ONLY in `200 Notes/Admin/Credentials/api-keys.env` (gitignored). Never accept a credential pasted into chat — refuse, and tell the human to rotate it. Never log, echo, or commit credential values.
2. **Provenance:** ingested notes carry a source header; distilled claims cite sources. When answering questions, cite the note(s) used; say "not in my sources" rather than guessing.
3. **Truth tiers:** owner-verified rulings > owner-stated seed facts > corpus documents > `Archive-Imported/`. A note marked `superseded-by:` is history, not current truth.
4. **Source originals are read-only.** Never modify, move, or delete anything in the company's Drive or source folders during ingestion. The vault copy is yours; the original is sacred.
5. **Nothing sends externally on its own.** No email, message, payment, or post leaves this system without a human confirming it. Routines declare `sends_external: false` or `drafts_only` unless the owner explicitly rules otherwise (see `000 OS/routines/README.md`).
6. **Write the run log.** One line per session in `210 Runs/`.

## Skills in this vault

| Skill | Step | Purpose |
|---|---|---|
| `welcome` | 0 | First-run machine check + orientation — run before anything else |
| `brain-install` | 1 | Ingest the company corpus, distill the brain core |
| `bottleneck-finder` | 2 | Interview + brain → ranked Friction Map of automation candidates |
| `skill-forge` | 3 | Observe a real workflow → forge a working, tested agent |
| `system-health` | 5 | Read the run log → health report + improvement list in the dashboard |

Canonical specs: `000 OS/skills/<name>/SKILL.md`. Routines (scheduled skills) live in `000 OS/routines/` — format in that folder's README.

## Weekly habit

The owner drops new facts and corrections into `200 Notes/Inbox/` during the week. Once a week: say **"process the brain inbox"** — the agent proposes promotions into the brain core, the human approves or rejects each, approved items get applied with an attribution footer, processed items get archived. This keeps the brain current between health checks.
