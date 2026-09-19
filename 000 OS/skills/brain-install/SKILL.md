---
name: brain-install
description: Turn your company's document corpus into a structured, owner-verified AI business brain inside this vault. Step 1 of the 5-step install (DIY edition).
interactive: true
requires: high_capability
---

# brain-install (DIY)

Builds the **AI business brain**: ingests your company documents into the vault taxonomy with full provenance, then distills the brain core — company profile, org, offer & pricing, clients, tool stack, KPIs, glossary, voice, North Star — so the brain describes *your* business, verified by you.

**Hard rules (every phase):**
1. **Read-only against source material.** Never modify, move, or delete anything in the source folder/Drive. The vault copy is ours; the original is sacred.
2. **Provenance on everything.** Every ingested note carries a header: source path, source modified-date, ingested date. Every distilled claim cites its source notes.
3. **Exclusions are law + sensitivity gate.** Before filing any file, check it against the exclusion list from Phase 0 AND scan content for personal-data signals (payroll/salary terms, tax IDs, IBANs, medical terms, employment contracts, "confidential" headers). Hits are quarantined to `000 OS/install/quarantine-sensitive/` and listed in `000 OS/install/sensitive-excluded.md` — never filed into the brain, never silently dropped. Ambiguous → ask the owner.
4. **Flag, don't guess.** Conflicting sources → both cited, conflict flagged. Missing info → `UNVERIFIED` marker. "Not in my sources" beats a confident guess.
5. **Idempotent phases.** Checkpoint each phase to `000 OS/install/ingest-progress.md`; re-runs resume and pick up deltas, never duplicate.
6. **No credentials in chat, ever.** Keys go in `200 Notes/Admin/Credentials/api-keys.env` via a text editor. Refuse pasted secrets; tell the human to rotate any key that was pasted.

## Phase 0 — Preflight + interview

1. Environment check (macOS especially): vault in a dot-free, non-iCloud path; if using Claude Code, confirm the CLI launches and can read files here.
2. Ask for the corpus location (a local folder, or an exported Drive folder). Produce an **inventory**: file count, size, counts by type, folder map, scanned-PDF count, files >100 MB. Write `000 OS/install/inventory.md`.
3. Interview the owner (write answers to `000 OS/install/seed-facts.md` — these are truth anchors that outrank documents):
   - Company name + what the business does, in one paragraph
   - Org: who does what (roles, reporting)
   - Top clients
   - The offer(s) + current prices
   - Tool stack (every tool the business runs on)
   - Top-5 KPIs and where the numbers live
   - The 3 documents you'd give a new hire first
   - Stale documents/folders to distrust
   - **Exclusion list**: folders/files that must NOT enter the brain (HR records, payroll, legal, personal)
4. Show which folders WILL be ingested with estimated counts. **Do not start without an explicit yes.**

## Phase 1 — Pull + convert

- Copy (never move) source files into `_intake/`, mirroring structure, applying the exclusion filter at copy time and again at filing time.
- Run the sensitivity gate per file (Hard Rule 3).
- Convert to markdown: docx/pdf-with-text → text; scanned PDFs → list in `000 OS/install/ingest-exceptions.md` as `NEEDS-OCR` (don't pretend to read them); spreadsheets → markdown table if small, else summarize structure. Unparseable → exceptions list with the reason.
- Media/large binaries: don't copy — record a metadata stub (name, location, size) so the brain knows they exist.
- Checkpoint per folder; large corpora can run across multiple sessions.

## Phase 2 — Filing

- Place each converted note in the taxonomy (`200 Notes/...`), inferring conservatively from folder names + content. Unsure → `200 Notes/Archive-Imported/` holding pen (target <10%; report the figure).
- Every note gets the provenance header:

```yaml
---
source: <original path>
source-modified: <date>
ingested: <date>
via: brain-install starter-kit
---
```

- Same-name/near-duplicate clusters: keep all, mark older with `superseded-by:` — the owner adjudicates in refinement, nothing auto-deleted.

## Phase 3 — Distillation (the brain core)

Build `200 Notes/Company/` from **seed-facts first, corpus second**:

| Doc | Content |
|---|---|
| `Company Profile.md` | What the business is, history, model, positioning |
| `Org.md` | People, roles, reporting lines |
| `Offer & Pricing.md` | Products/services + prices, each with an as-of date |
| `Clients Overview.md` | + a stub per top client in `150 Clients/` |
| `Tool Stack.md` | Every tool, owner, purpose |
| `KPIs.md` | The top-5, where the numbers live |
| `Glossary.md` | Internal terms, acronyms, codenames found in the corpus |
| `Voice & Tone.md` | Derived from their actual written material, with examples |
| `🌟 North Star.md` | DRAFT from the interview — the owner rewrites it in refinement |

Discipline: synthesize patterns, not quote dumps; one source family per pass with a quality skim between passes; long sessions that degrade get checkpointed and resumed fresh. Every core doc ends with a **confidence footer**: sources (wikilinks), `UNVERIFIED:` items, `CONFLICT:` items.

Then write `000 OS/install/refinement-agenda.md`: every flag across all core docs, the gap questions (things referenced but never explained), and — always — the **current-state question** per doc: *"what changed in the last 60–90 days that isn't in these documents?"* and *"is there anything here you do NOT want kept?"* Corpora are always slightly stale; this catches the delta.

## Phase 4 — Refinement + quiz

- Walk `refinement-agenda.md` with the owner item by item; apply rulings to the core docs, each noted `corrected by {name}, {date}`. Rewrite `🌟 North Star.md` in the owner's own words. Done when zero unresolved flags remain.
- Then the acceptance quiz: generate 10 real questions about the business from the corpus; answer each **from vault sources only, citing the note(s)**, saying "not in my sources" when true. The owner judges. Below ~8/10 → refine the weak areas and re-test.

## Wrap (the skill is done when)

- [ ] Corpus ingested per scope; exceptions + holding-pen reported; sensitivity quarantine count surfaced (even if zero)
- [ ] All 9 core docs exist with provenance and zero unresolved flags
- [ ] Quiz passed, owner-judged
- [ ] Run line written to `210 Runs/`; vault committed to git; no credentials in history

**Next:** Step 2 — `/bottleneck-finder` (`guides/step-2-friction-map.md`).
