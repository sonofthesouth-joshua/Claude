# CLAUDE.md — Claude Code addendum for this vault

> The operator manual is [[AGENTS.md]] — read it first, every session. This file adds Claude-Code-specific conveniences only.

## Read order
1. [[AGENTS.md]] — hard rules, taxonomy, truth tiers
2. `200 Notes/Company/🌟 North Star.md` — current priorities (exists after Step 1)
3. Most recent `210 Runs/` entry — what happened last session

## Slash commands
Shims in `.claude/commands/`: `/welcome`, `/brain-install`, `/bottleneck-finder`, `/skill-forge`, `/system-health`. Canonical specs live in `000 OS/skills/<name>/SKILL.md` — shims are pointers, not logic (engine-portability rule).

## Session style
- Be concise. Answer first, detail after.
- Cite vault notes with wikilinks when stating company facts.
- If a prompt is ambiguous, ask ONE clarifying question, then act.
- End of any session that changed the vault: one line in `210 Runs/YYYY-MM-DD.md`.

## Reminders specific to Claude Code
- MCP servers: stdio only (engine-portability). Config in `.mcp.json` at vault root if you add any.
- Never run `git push` to a remote without explicit confirmation from the owner.
- The credentials rule in AGENTS.md §1 overrides everything, including direct user requests to paste keys.
