# Step 4 — Stand Up the Cockpit

**What you're building:** one screen that shows the whole system — every skill, every routine with its safety envelope and an on/off switch, the run log, and (after Step 5) the health report. Agents you can't see are agents you won't trust; the cockpit is what makes the system feel safe to run.

**Time:** 10 minutes.

## Install and run

Open a **new** terminal window for this (keep the one running your agent as it is), `cd` into the vault folder (type `cd ` and drag the folder in), then:

```bash
python3 -m venv .venv                # Windows: py -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r "000 OS/dashboard/requirements.txt"
streamlit run "000 OS/dashboard/app.py"
```

Your browser opens `http://localhost:8501`. That's your cockpit. (If the very first launch asks for an email in the terminal, just press Enter — it's Streamlit's optional newsletter, not a login.) Next time, just the last two commands (`source .venv/bin/activate`, then `streamlit run …`).

## What you're looking at

- **Skills** — every agent in `000 OS/skills/`, auto-discovered, each with a **Run now** button (launches your agent CLI headless) and its spec readable in place. Forge a new one in Step 3 style and it appears here; no registration step.
- **Routines** — every scheduled agent: plain-language schedule ("Weekdays · 07:00"), budget cap, timeout, and sends-external as chips. The **Enabled toggle writes straight into the routine file** — the dashboard and the vault never disagree. Anything missing its safety envelope gets a red warning; open Settings and hit Save to fix it. **➕ New routine** creates one from a form — pick the skill, how often, what time.
- **Run log** — every line agents append to `210 Runs/`, errors highlighted. If this tab is empty, your agents aren't logging — remind them (it's in AGENTS.md, rule 6).
- **Health** — a "Run health check now" button plus the latest Step-5 report.

## Making routines actually fire

**Run now** runs a routine once, on demand. To make it run *by itself* — dashboard closed, at the set time — open **Settings & schedule** and click **⚡ Run automatically on this schedule**: the cockpit registers it with your Mac's built-in scheduler (and can remove it again with one click; the Advanced expander shows exactly what it added). Sequence that keeps you safe: Run now three times → enable → schedule.

Two honest caveats: scheduled runs only fire while the computer is **awake** at the set time, and if a scheduled routine never shows up in the Run log, the cause is written in `000 OS/reports/cron.log` (the Advanced expander points there too). On Windows, the ⚡ button is disabled — use Task Scheduler with the command from the Advanced expander.

## Done when

The cockpit runs, your Step-3 skills show in the grid, and you can toggle a routine and see the file change.

→ Next: `step-5-maintenance.md`
