# Step 0 — Starting From Zero

Never used a terminal? Nothing installed? This page gets you from a blank computer to a working setup in about 15 minutes. If you already use Claude Code (or another agent CLI), skip to the last section.

## What you actually need

Just **one** program: an AI agent CLI. That's the "employee" that reads this kit and does the work. Everything else — checking your machine, setting up the pieces, even installing what's missing — the agent itself will guide you through once it's running.

You do **not** need Obsidian, Notion, or any note app (the vault is plain files; any editor can open them — Obsidian is a nice optional viewer later). You do **not** need to know how to code.

## 1. Install Claude Code (~5 min)

1. Go to **[claude.com/claude-code](https://claude.com/claude-code)** and follow the install instructions for your system (macOS, Windows, or Linux).
2. You'll need a Claude account — the **Pro plan is the practical minimum** for Step 1 (the brain reads a lot of documents); Max is more comfortable. This is the kit's only real running cost.
3. When the install finishes, you should be able to open the **Terminal** app (macOS: press `Cmd+Space`, type "Terminal", Enter — on Windows: PowerShell), type `claude`, press Enter, and see it ask you to log in. Log in. Then type `/exit` for now.

If `claude` says "command not found", close the terminal window and open a new one — installs only appear in fresh windows.

## 2. Put this kit in the right place (~2 min)

1. Unzip the kit if you haven't (double-click the ZIP).
2. Rename the folder to your company, e.g. `AcmeOS`.
3. Move it to your **home folder** — in Finder: Go → Home (`Cmd+Shift+H`), drop it there. **Not** in Documents or Desktop if you use iCloud — cloud sync silently breaks agent file access on macOS.

## 3. Open the agent inside the kit (~1 min)

1. Open Terminal.
2. Type `cd ` (with a space after it), then **drag the kit folder from Finder into the terminal window** — its path appears. Press Enter.
3. Type `claude` and press Enter.

## 4. Say the magic words

Type this as your first message:

> **Read AGENTS.md, then read and follow `000 OS/skills/welcome/SKILL.md`.**

From here the agent takes over: it checks your machine piece by piece (folder location, git, Python for the dashboard), tells you what's missing and how to fix it — adapting to *your* setup — then walks you into Step 1. You never have to guess what to install again; when in doubt, ask the agent. That's the whole point of the system you're about to build.

→ The agent will bring you to `guides/step-1-brain.md` when your setup is green.
