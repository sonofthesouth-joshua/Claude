"""AgenticOS Starter Kit — cockpit dashboard.

One screen to control the whole system: run any skill or routine, create and
tune routines (plain-language schedules, one-click automation), read the run
log, and see the latest health report.

Run from the vault root:
    streamlit run "000 OS/dashboard/app.py"
"""

from __future__ import annotations

import re
import shutil
import subprocess
from datetime import date, datetime, time as dtime, timedelta
from pathlib import Path

import streamlit as st

VAULT = Path(__file__).resolve().parents[2]
SKILLS_DIR = VAULT / "000 OS" / "skills"
ROUTINES_DIR = VAULT / "000 OS" / "routines"
REPORTS_DIR = VAULT / "000 OS" / "reports"
AGENT_LOG_DIR = REPORTS_DIR / "agent-runs"
RUNS_DIR = VAULT / "210 Runs"

ENVELOPE_KEYS = ("max_budget_usd", "max_duration_sec", "sends_external")
CRON_TAG = "# agenticos:"
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
WEEKDAY_CRON = [1, 2, 3, 4, 5, 6, 0]  # cron day-of-week for the list above
FREQS = ["Every day", "Weekdays", "Once a week", "Every hour"]


# ---------- schedules: humans pick times, cron stays under the hood -------

def build_cron(freq: str, t: dtime, weekday: str) -> str:
    if freq == "Every hour":
        return f"{t.minute} * * * *"
    if freq == "Weekdays":
        return f"{t.minute} {t.hour} * * 1-5"
    if freq == "Once a week":
        return f"{t.minute} {t.hour} * * {WEEKDAY_CRON[WEEKDAYS.index(weekday)]}"
    return f"{t.minute} {t.hour} * * *"


def parse_cron(cron: str) -> dict | None:
    parts = cron.split()
    if len(parts) != 5 or parts[2] != "*" or parts[3] != "*":
        return None
    m, h, _, _, dow = parts
    if not m.isdigit():
        return None
    minute = int(m)
    if h == "*":
        return {"freq": "Every hour", "time": dtime(9, minute), "weekday": "Monday"}
    if not h.isdigit():
        return None
    t = dtime(int(h), minute)
    if dow == "*":
        return {"freq": "Every day", "time": t, "weekday": "Monday"}
    if dow == "1-5":
        return {"freq": "Weekdays", "time": t, "weekday": "Monday"}
    if dow.isdigit() and int(dow) in WEEKDAY_CRON:
        return {"freq": "Once a week", "time": t, "weekday": WEEKDAYS[WEEKDAY_CRON.index(int(dow))]}
    return None


def humanize_cron(cron: str) -> str:
    p = parse_cron(cron)
    if p is None:
        return cron  # hand-written cron — show as-is
    hhmm = p["time"].strftime("%H:%M")
    if p["freq"] == "Every hour":
        return f"Hourly at :{p['time'].minute:02d}"
    if p["freq"] == "Weekdays":
        return f"Weekdays · {hhmm}"
    if p["freq"] == "Once a week":
        return f"{p['weekday']}s · {hhmm}"
    return f"Daily · {hhmm}"


# ---------- vault readers -------------------------------------------------

def parse_frontmatter(path: Path) -> dict:
    meta: dict[str, str] = {}
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return meta
    m = re.match(r"\A---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return meta
    for line in m.group(1).splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            key, _, value = line.partition(":")
            value = value.split(" #")[0]  # tolerate inline comments from copied templates
            meta[key.strip()] = value.strip().strip("\"'")
    return meta


def body_without_frontmatter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return re.sub(r"\A---.*?---\s*", "", text, flags=re.S)


def load_skills() -> list[dict]:
    skills = []
    if SKILLS_DIR.is_dir():
        for spec in sorted(SKILLS_DIR.glob("*/SKILL.md")):
            meta = parse_frontmatter(spec)
            skills.append({
                "name": meta.get("name", spec.parent.name),
                "description": meta.get("description", ""),
                "interactive": meta.get("interactive", "false").lower() == "true",
                "path": spec.relative_to(VAULT),
                "file": spec,
            })
    return skills


def load_routines() -> list[dict]:
    routines = []
    if ROUTINES_DIR.is_dir():
        for spec in sorted(ROUTINES_DIR.glob("*.md")):
            if spec.name.upper().startswith("README"):
                continue
            meta = parse_frontmatter(spec)
            missing = [k for k in ENVELOPE_KEYS if k not in meta]
            routines.append({
                "name": meta.get("name", spec.stem),
                "description": meta.get("description", ""),
                "schedule": meta.get("schedule", "0 9 * * *"),
                "enabled": meta.get("enabled", "false").lower() == "true",
                "sends_external": meta.get("sends_external", "false"),
                "budget": meta.get("max_budget_usd", ""),
                "duration": meta.get("max_duration_sec", ""),
                "missing_envelope": missing,
                "file": spec,
            })
    return routines


def set_frontmatter_value(spec: Path, key: str, value: str) -> None:
    text = spec.read_text(encoding="utf-8")
    if re.search(rf"(?m)^{key}\s*:", text):
        new = re.sub(rf"(?m)^({key}\s*:).*$", rf"\1 {value}", text, count=1)
    else:
        parts = text.split("---", 2)
        new = f"---{parts[1]}{key}: {value}\n---{parts[2]}" if len(parts) >= 3 else text
    spec.write_text(new, encoding="utf-8")


def load_runs(days: int = 14) -> list[dict]:
    entries = []
    if not RUNS_DIR.is_dir():
        return entries
    cutoff = date.today() - timedelta(days=days)
    for f in sorted(RUNS_DIR.glob("*.md"), reverse=True):
        try:
            day = datetime.strptime(f.stem, "%Y-%m-%d").date()
        except ValueError:
            continue
        if day < cutoff:
            break
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line.startswith("- "):
                continue
            body = line[2:]
            bad = bool(re.search(r"error|failed|timeout|killed", body, re.I))
            entries.append({"day": day.isoformat(), "line": body, "error": bad})
    return entries


def latest_report() -> Path | None:
    if not REPORTS_DIR.is_dir():
        return None
    reports = sorted(REPORTS_DIR.glob("health-*.md"), reverse=True)
    return reports[0] if reports else None


# ---------- agent runner + scheduler --------------------------------------

def find_agent_cli() -> tuple[str, list[str]] | None:
    claude = shutil.which("claude") or next(
        (str(p) for p in [
            Path.home() / ".local/bin/claude",       # native installer default
            Path.home() / ".npm-global/bin/claude",  # npm prefix installs
            Path("/opt/homebrew/bin/claude"),
            Path("/usr/local/bin/claude"),
        ] if Path(p).exists()),
        None,
    )
    if claude:
        return "claude", [claude, "--permission-mode", "acceptEdits", "-p"]
    codex = shutil.which("codex")
    if codex:
        return "codex", [codex, "exec"]
    return None


def run_spec(spec_rel: str, label: str) -> str:
    cli = find_agent_cli()
    if cli is None:
        return "No agent CLI found — install Claude Code (`claude`) or Codex (`codex`) and restart the dashboard."
    engine, argv = cli
    prompt = (
        f'Read and follow "{spec_rel}" in this vault. '
        "Respect any max_budget_usd / max_duration_sec declared in the spec — stop cleanly rather than exceed them. "
        f"When finished, append a one-line outcome to 210 Runs/{date.today().isoformat()}.md."
    )
    AGENT_LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = AGENT_LOG_DIR / f"{label}-{datetime.now().strftime('%H%M%S')}.log"
    with open(log_path, "w", encoding="utf-8") as log:
        subprocess.Popen(argv + [prompt], cwd=VAULT, stdout=log, stderr=subprocess.STDOUT,
                         stdin=subprocess.DEVNULL, start_new_session=True)
    RUNS_DIR.mkdir(exist_ok=True)
    with open(RUNS_DIR / f"{date.today().isoformat()}.md", "a", encoding="utf-8") as f:
        f.write(f"- {datetime.now().strftime('%H:%M')} {label} (dashboard) · launched via {engine}\n")
    return (
        f"Launched with {engine} — the outcome will appear in the Run log when it finishes. "
        f"(Nothing after a few minutes? Check 000 OS/reports/agent-runs/{log_path.name} — "
        f"a logged-out CLI is the usual cause.)"
    )


CRONTAB_AVAILABLE = shutil.which("crontab") is not None


def scheduler_line(routine: dict) -> str | None:
    """The crontab entry for a routine. Uses the CLI's absolute path — cron's
    PATH is bare /usr/bin:/bin and never contains agent-CLI install locations."""
    cli = find_agent_cli()
    if cli is None:
        return None
    _, argv = cli
    rel = routine["file"].relative_to(VAULT)
    prompt = f'Read and follow "{rel}". Append the outcome to the run log.'
    invoke = " ".join([f'"{a}"' for a in argv] + [f"'{prompt}'"])
    env = 'export PATH="$HOME/.local/bin:$HOME/.npm-global/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin";'
    return f'{routine["schedule"]} {env} cd "{VAULT}" && {invoke} >> "{VAULT}/000 OS/reports/cron.log" 2>&1'


def crontab_text() -> str:
    try:
        out = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
        return out.stdout if out.returncode == 0 else ""
    except OSError:
        return ""


def is_scheduled(slug: str) -> bool:
    return f"{CRON_TAG}{slug}" in crontab_text()


def schedule_on(routine: dict) -> str:
    slug = routine["file"].stem
    line = scheduler_line(routine)
    if line is None:
        return "No agent CLI found — install Claude Code first, then schedule."
    lines = [l for l in crontab_text().splitlines() if f"{CRON_TAG}{slug}" not in l]
    lines.append(f"{line} {CRON_TAG}{slug}")
    try:
        subprocess.run(["crontab", "-"], input="\n".join(lines) + "\n", text=True, check=True)
        return f"Scheduled — this Mac will now run {routine['name']} {humanize_cron(routine['schedule']).lower()}, dashboard open or not."
    except (OSError, subprocess.CalledProcessError) as e:
        return f"Couldn't write the schedule ({e}). You can add it manually — see Advanced."


def schedule_off(slug: str, name: str) -> str:
    lines = [l for l in crontab_text().splitlines() if f"{CRON_TAG}{slug}" not in l]
    try:
        subprocess.run(["crontab", "-"], input="\n".join(lines) + ("\n" if lines else ""), text=True, check=True)
        return f"Removed — {name} no longer runs automatically."
    except (OSError, subprocess.CalledProcessError) as e:
        return f"Couldn't update the schedule ({e})."


# ---------- UI ------------------------------------------------------------

st.set_page_config(page_title="AgenticOS Cockpit", page_icon="🧠", layout="wide")

st.markdown(
    """<style>
@import url('https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap');

html, body, [class*="css"], .stApp, p, span, div { font-family: 'DM Sans', sans-serif; }
h1, h2, h3, [data-testid="stMetricValue"] { font-family: 'Archivo', sans-serif !important; }

.stApp { background: radial-gradient(ellipse 80% 50% at 50% -10%, rgba(124,58,237,.14), transparent 60%), #0D0F14; }
.block-container { padding-top: 2.4rem; max-width: 1200px; }

/* brand header */
.aos-brand { display:flex; align-items:center; gap:14px; margin-bottom:2px; }
.aos-logo { width:40px; height:40px; border-radius:12px; flex:0 0 40px;
  background: linear-gradient(135deg,#7C3AED,#D946EF);
  box-shadow: 0 8px 24px rgba(124,58,237,.45); display:flex; align-items:center; justify-content:center;
  color:#fff; font-family:'Archivo'; font-weight:900; font-size:20px; }
.aos-title { font-family:'Archivo'; font-weight:800; font-size:1.9rem; letter-spacing:-.02em; color:#F4F5F9; line-height:1.1; }
.aos-sub { color:#8A91A5; font-size:.82rem; margin-top:2px; }
.aos-sub code { color:#A78BFA; background:rgba(124,58,237,.10); padding:1px 7px; border-radius:6px; font-size:.78rem; }

/* metric tiles */
[data-testid="stMetric"] { background:#12151D; border:1px solid #232838; border-radius:16px; padding:14px 18px 10px; }
[data-testid="stMetricValue"] { color:#A78BFA !important; font-weight:800 !important; }
[data-testid="stMetricLabel"] p { color:#8A91A5 !important; font-size:.8rem !important; letter-spacing:.06em; text-transform:uppercase; font-weight:600 !important; }

/* tabs */
button[data-baseweb="tab"] p { font-size:.95rem !important; font-weight:600 !important; }
[data-testid="stTabs"] [data-baseweb="tab-highlight"] { background:#7C3AED; height:3px; border-radius:3px; }

/* bordered cards */
[data-testid="stVerticalBlockBorderWrapper"] { background:#12151D; border:1px solid #232838 !important; border-radius:16px !important; transition: border-color .2s; }
[data-testid="stVerticalBlockBorderWrapper"]:hover { border-color:#3A3F55 !important; }

/* chips */
.aos-chip { display:inline-block; background:rgba(124,58,237,.12); color:#C4B5FD;
  border:1px solid rgba(124,58,237,.35); border-radius:999px; padding:3px 12px;
  font-size:.78rem; font-weight:600; margin:0 6px 6px 0; white-space:nowrap; }
.aos-chip.dim { background:rgba(138,145,165,.10); color:#9AA1B5; border-color:rgba(138,145,165,.25); }
.aos-chip.live { background:rgba(16,185,129,.12); color:#6EE7B7; border-color:rgba(16,185,129,.35); }
.aos-warn { color:#F87171; font-weight:600; font-size:.85rem; }

/* buttons */
.stButton button, [data-testid="stFormSubmitButton"] button { border-radius: 10px; font-weight:600; }
.stButton button[kind="primary"] { background:linear-gradient(135deg,#7C3AED,#9333EA); border:none;
  box-shadow:0 6px 20px rgba(124,58,237,.35); }

/* expanders */
[data-testid="stExpander"] summary p { font-size:.85rem; font-weight:600; color:#9AA1B5; }
[data-testid="stExpander"] { border-radius: 12px; }

/* run log rows */
.aos-run { padding:9px 14px; border:1px solid #232838; border-radius:12px; margin-bottom:8px;
  background:#12151D; font-size:.9rem; color:#D7DAE4; }
.aos-run .d { color:#8A91A5; font-size:.78rem; margin-right:10px; font-variant-numeric:tabular-nums; }
.aos-run.err { border-color:rgba(248,113,113,.4); background:rgba(248,113,113,.05); }

/* health banner */
.aos-health { border-radius:14px; padding:14px 20px; margin-bottom:14px; font-weight:600; border:1px solid; }
.aos-health.green { background:rgba(16,185,129,.08); border-color:rgba(16,185,129,.35); color:#6EE7B7; }
.aos-health.yellow { background:rgba(245,158,11,.08); border-color:rgba(245,158,11,.35); color:#FCD34D; }
.aos-health.red { background:rgba(248,113,113,.08); border-color:rgba(248,113,113,.4); color:#FCA5A5; }
    </style>""",
    unsafe_allow_html=True,
)

skills = load_skills()
routines = load_routines()
runs = load_runs()
report = latest_report()

st.markdown(
    f"""<div class="aos-brand">
      <div class="aos-logo">A</div>
      <div><div class="aos-title">AgenticOS Cockpit</div>
      <div class="aos-sub">Vault <code>{VAULT.name}</code> · every agent, one screen</div></div>
    </div>""",
    unsafe_allow_html=True,
)
st.write("")

runs_week = [r for r in runs if r["day"] >= (date.today() - timedelta(days=7)).isoformat()]
errors_week = [r for r in runs_week if r["error"]]
c1, c2, c3, c4 = st.columns(4)
c1.metric("Skills", len(skills))
c2.metric("Routines on", f"{sum(r['enabled'] for r in routines)} / {len(routines)}")
c3.metric("Runs · 7d", len(runs_week))
c4.metric("Errors · 7d", len(errors_week))
st.write("")

tab_skills, tab_routines, tab_runs, tab_health = st.tabs(
    ["Skills", "Routines", "Run log", "Health"]
)

with tab_skills:
    if not skills:
        st.info("No skills yet — Step 3 (Skill Forge) adds them here automatically.")
    for row_start in range(0, len(skills), 3):
        cols = st.columns(3)
        for col, skill in zip(cols, skills[row_start:row_start + 3]):
            with col.container(border=True):
                st.markdown(f"**/{skill['name']}**")
                st.caption(skill["description"] or "No description in frontmatter.")
                if skill["interactive"]:
                    # interview-driven skills need a conversation — headless runs would stall
                    st.caption("Runs as a conversation — paste this in your agent chat:")
                    st.code(f'Read and follow "{skill["path"]}"', language=None)
                elif st.button("Run now", key=f"run-skill-{skill['name']}", type="primary"):
                    st.toast(run_spec(str(skill["path"]), skill["name"]))
                with st.expander("View spec"):
                    st.markdown(body_without_frontmatter(skill["file"]))

with tab_routines:
    st.caption(
        "A routine is a skill on a schedule. **Run now** runs it once, on demand. "
        "**Schedule** makes this Mac run it by itself at the set time — dashboard open or not."
    )
    if not routines:
        st.info("No routines yet — create your first one below.")
    for r in routines:
        slug = r["file"].stem
        scheduled = is_scheduled(slug)
        with st.container(border=True):
            left, mid, right = st.columns([3, 4, 1.6])
            with left:
                st.markdown(f"**{r['name']}**")
                st.caption(r["description"] or r["file"].name)
            with mid:
                chips = (
                    f"<span class='aos-chip'>{humanize_cron(r['schedule'])}</span>"
                    f"<span class='aos-chip dim'>≤ ${r['budget'] or '—'}/run</span>"
                    f"<span class='aos-chip dim'>≤ {r['duration'] or '—'}s</span>"
                    f"<span class='aos-chip dim'>sends: {r['sends_external']}</span>"
                )
                if scheduled:
                    chips += "<span class='aos-chip live'>⚡ runs automatically</span>"
                st.markdown(chips, unsafe_allow_html=True)
                if r["missing_envelope"]:
                    st.markdown(
                        f"<span class='aos-warn'>⚠ safety envelope incomplete — open Settings and Save to fix "
                        f"({', '.join(r['missing_envelope'])})</span>",
                        unsafe_allow_html=True,
                    )
            with right:
                toggled = st.toggle("Enabled", value=r["enabled"], key=f"tgl-{slug}")
                if toggled != r["enabled"]:
                    set_frontmatter_value(r["file"], "enabled", str(toggled).lower())
                    st.rerun()
                if st.button("Run now", key=f"run-rt-{slug}", type="primary"):
                    st.toast(run_spec(str(r["file"].relative_to(VAULT)), r["name"]))

            with st.expander("Settings & schedule"):
                parsed = parse_cron(r["schedule"]) or {"freq": "Every day", "time": dtime(9, 0), "weekday": "Monday"}
                with st.form(f"edit-{slug}"):
                    e1, e2, e3 = st.columns([1.4, 1, 1])
                    freq = e1.selectbox("How often", FREQS, index=FREQS.index(parsed["freq"]) if parsed["freq"] in FREQS else 0)
                    when = e2.time_input("At what time", value=parsed["time"])
                    weekday = e3.selectbox("Day", WEEKDAYS, index=WEEKDAYS.index(parsed["weekday"]))
                    e4, e5, e6 = st.columns(3)
                    budget = e4.text_input("Max cost per run (USD)", value=r["budget"] or "0.50")
                    duration = e5.text_input("Max duration (seconds)", value=r["duration"] or "600")
                    sends = e6.selectbox(
                        "Can it send externally?", ["false", "drafts_only", "true"],
                        index=["false", "drafts_only", "true"].index(r["sends_external"])
                        if r["sends_external"] in ("false", "drafts_only", "true") else 0,
                        help="false = never · drafts_only = prepares, you send · true = sends on its own (think twice)",
                    )
                    if st.form_submit_button("Save"):
                        set_frontmatter_value(r["file"], "schedule", f'"{build_cron(freq, when, weekday)}"')
                        set_frontmatter_value(r["file"], "max_budget_usd", budget)
                        set_frontmatter_value(r["file"], "max_duration_sec", duration)
                        set_frontmatter_value(r["file"], "sends_external", sends)
                        if is_scheduled(slug):  # keep the installed schedule in sync
                            r2 = dict(r, schedule=build_cron(freq, when, weekday))
                            schedule_on(r2)
                        st.rerun()

                st.divider()
                if scheduled:
                    st.markdown(f"⚡ **Runs automatically** — {humanize_cron(r['schedule'])}, even with the dashboard closed.")
                    if st.button("Stop running automatically", key=f"unsch-{slug}"):
                        st.toast(schedule_off(slug, r["name"]))
                        st.rerun()
                else:
                    st.markdown("Not scheduled yet — it only runs when you click **Run now**.")
                    blocked = bool(r["missing_envelope"]) or not CRONTAB_AVAILABLE
                    if st.button("⚡ Run automatically on this schedule", key=f"sch-{slug}", disabled=blocked):
                        st.toast(schedule_on(r))
                        st.rerun()
                    if r["missing_envelope"]:
                        st.caption("Complete the safety envelope above first (open Settings, hit Save).")
                    elif not CRONTAB_AVAILABLE:
                        st.caption(
                            "Automatic scheduling uses cron (macOS/Linux). On Windows, use Task Scheduler "
                            "with the command shown under Advanced."
                        )
                st.caption("Note: scheduled runs only fire while this computer is awake at the set time.")
                with st.expander("Advanced · what scheduling does under the hood"):
                    st.caption(
                        "Scheduling adds this line to your user crontab (the Mac's built-in task scheduler). "
                        "The button manages it for you; shown here for transparency. If a scheduled run never "
                        "reaches the Run log, read `000 OS/reports/cron.log` — errors land there:"
                    )
                    st.code(scheduler_line(r) or "Install an agent CLI (claude / codex) to generate this line.", language="bash")
                    st.code(r["file"].read_text(encoding="utf-8"), language="markdown")

    with st.expander("➕ New routine"):
        with st.form("new-routine", clear_on_submit=True):
            name = st.text_input("Name", placeholder="morning-brief")
            description = st.text_input("What it does (one line)")
            skill_names = [s["name"] for s in skills]
            skill_pick = st.selectbox("Skill it runs", skill_names) if skill_names else None
            f1, f2, f3 = st.columns([1.4, 1, 1])
            freq = f1.selectbox("How often", FREQS)
            when = f2.time_input("At what time", value=dtime(9, 0))
            weekday = f3.selectbox("Day", WEEKDAYS)
            n1, n2, n3 = st.columns(3)
            budget = n1.text_input("Max cost per run (USD)", value="0.50")
            duration = n2.text_input("Max duration (seconds)", value="600")
            sends = n3.selectbox("Can it send externally?", ["false", "drafts_only"])
            instructions = st.text_area(
                "Standing instructions for each run",
                value="Run the skill and append the outcome to the run log.",
            )
            if st.form_submit_button("Create routine"):
                slug = re.sub(r"[^a-z0-9-]", "-", (name or "").strip().lower()).strip("-")
                target = ROUTINES_DIR / f"{slug}.md"
                if not slug:
                    st.error("Give the routine a name.")
                elif target.exists():
                    st.error(f"`{target.name}` already exists.")
                elif not skill_pick:
                    st.error("No skills to schedule yet — forge one first (Step 3).")
                else:
                    skill_path = next(str(s["path"]) for s in skills if s["name"] == skill_pick)
                    target.write_text(
                        "---\n"
                        f"name: {slug}\n"
                        f"description: {description or slug}\n"
                        f"skill: {skill_path}\n"
                        f"schedule: \"{build_cron(freq, when, weekday)}\"\n"
                        "enabled: false\n"
                        f"max_budget_usd: {budget}\n"
                        f"max_duration_sec: {duration}\n"
                        f"sends_external: {sends}\n"
                        "---\n\n"
                        f"Run the skill at `{skill_path}` with these standing instructions:\n"
                        f"- {instructions}\n"
                        "- Append the outcome to `210 Runs/YYYY-MM-DD.md`.\n",
                        encoding="utf-8",
                    )
                    st.rerun()

with tab_runs:
    if not runs:
        st.info("No run lines yet — every agent session appends one to `210 Runs/`.")
    else:
        show_errors_only = st.checkbox("Errors only", value=False)
        for r in runs:
            if show_errors_only and not r["error"]:
                continue
            cls = "aos-run err" if r["error"] else "aos-run"
            icon = "🔴" if r["error"] else "🟢"
            st.markdown(
                f"<div class='{cls}'>{icon} <span class='d'>{r['day']}</span>{r['line']}</div>",
                unsafe_allow_html=True,
            )

with tab_health:
    if st.button("Run health check now", type="primary"):
        st.toast(run_spec("000 OS/skills/system-health/SKILL.md", "system-health"))
    if report is None:
        st.info("No health report yet — run the check above. The latest report renders here.")
    else:
        meta = parse_frontmatter(report)
        status = meta.get("status", "")
        labels = {"green": "All systems healthy", "yellow": "Needs attention", "red": "Something is broken"}
        if status in labels:
            st.markdown(
                f"<div class='aos-health {status}'>{labels[status]} · {report.stem.replace('health-', '')}</div>",
                unsafe_allow_html=True,
            )
        st.markdown(body_without_frontmatter(report))
