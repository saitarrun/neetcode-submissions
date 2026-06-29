#!/usr/bin/env python3
"""Build streak data (public/data.json) and a README badge (assets/streak.svg)
from the repository's git history. Run from the repo root."""

import datetime
import json
import os
import re
import subprocess

PROBLEM_BASE = "Data Structures & Algorithms"

# --- colors (GitHub-style buckets) ---
FILL = {0: "#ffffff", 1: "#a8e0b8", 3: "#2da44e", 4: "#116329"}
EMPTY_STROKE = "#d0d7de"

CELL = 11
GAP = 3
STEP = CELL + GAP
PAD = 18
HEADER_H = 86
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def git_days():
    out = subprocess.check_output(
        ["git", "log", "--pretty=format:%ad%x09%s", "--date=short"], text=True)
    days = {}
    for line in out.splitlines():
        if "\t" not in line:
            continue
        date, subj = line.split("\t", 1)
        w = 0
        m = re.match(r"Bulk sync: (\d+) submissions", subj)
        if m:
            w = int(m.group(1))
        elif subj.startswith("Add:"):
            w = 1
        if w:
            days[date] = days.get(date, 0) + w
    return days


def to_date(s):
    y, m, d = map(int, s.split("-"))
    return datetime.date(y, m, d)


def level(c):
    if not c:
        return 0
    if c > 10:
        return 4
    if c >= 5:
        return 3
    return 1


def compute_stats(days):
    sd = sorted(days)
    total = sum(days.values())
    active = len(sd)

    longest = run = 0
    prev = None
    for s in sd:
        d = to_date(s)
        run = run + 1 if (prev and (d - prev).days == 1) else 1
        longest = max(longest, run)
        prev = d

    today = datetime.date.today()
    current = 0
    if sd:
        last = to_date(sd[-1])
        if (today - last).days <= 1:
            dayset = set(sd)
            cur = last
            while cur.isoformat() in dayset:
                current += 1
                cur -= datetime.timedelta(days=1)
    return total, active, longest, current


def count_problems():
    if not os.path.isdir(PROBLEM_BASE):
        return 0
    return sum(1 for n in os.listdir(PROBLEM_BASE)
               if os.path.isdir(os.path.join(PROBLEM_BASE, n)))


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_svg(days, problems, stats):
    total, active, longest, current = stats
    today = datetime.date.today()
    year = today.year
    jan1 = datetime.date(year, 1, 1)
    dec31 = datetime.date(year, 12, 31)
    grid_start = jan1 - datetime.timedelta(days=jan1.isoweekday() % 7)

    grid_top = HEADER_H + 14
    cells = []
    months = []
    col = 0
    d = grid_start
    while d <= dec31:
        for row in range(7):
            cur = d + datetime.timedelta(days=row)
            in_year = cur.year == year
            count = days.get(cur.isoformat(), 0) if in_year else 0
            lv = level(count)
            x = PAD + col * STEP
            y = grid_top + row * STEP
            opacity = "" if in_year else ' opacity="0.35"'
            stroke = f' stroke="{EMPTY_STROKE}"' if lv == 0 else ""
            cells.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" '
                f'fill="{FILL[lv]}"{stroke}{opacity}/>')
            if in_year and cur.day == 1:
                months.append((col, cur.month - 1))
        col += 1
        d += datetime.timedelta(days=7)

    width = PAD * 2 + col * STEP - GAP
    height = grid_top + 7 * STEP + 34

    month_labels = "".join(
        f'<text x="{PAD + c * STEP}" y="{HEADER_H + 6}" '
        f'class="mut" font-size="10">{MONTHS[m]}</text>'
        for c, m in months)

    # stat blocks
    stat_items = [("Current Streak", f"{current} days"),
                  ("Longest Streak", f"{longest} days"),
                  ("Problems Solved", str(problems)),
                  ("Active Days", f"{active} days")]
    col_w = (width - PAD * 2) / 4
    stats_svg = ""
    for i, (label, val) in enumerate(stat_items):
        x = PAD + i * col_w
        stats_svg += (
            f'<text x="{x:.0f}" y="62" class="num">{esc(val)}</text>'
            f'<text x="{x:.0f}" y="76" class="mut" font-size="10">{esc(label.upper())}</text>')

    swatch_start = width - PAD - (4 * STEP + 36)
    legend = (
        f'<text x="{swatch_start - 8}" y="{height - 12}" text-anchor="end" '
        f'class="mut" font-size="10">Less</text>')
    lx = swatch_start
    for lv in [0, 1, 3, 4]:
        stroke = f' stroke="{EMPTY_STROKE}"' if lv == 0 else ""
        legend += f'<rect x="{lx}" y="{height - 22}" width="{CELL}" height="{CELL}" rx="2" fill="{FILL[lv]}"{stroke}/>'
        lx += STEP
    legend += f'<text x="{lx + 4}" y="{height - 12}" class="mut" font-size="10">More</text>'

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif">
  <style>
    .mut {{ fill: #656d76; }}
    .num {{ fill: #1f2328; font-size: 20px; font-weight: 700; }}
    .title {{ fill: #1f2328; font-size: 18px; font-weight: 700; }}
  </style>
  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="10" fill="#ffffff" stroke="#d0d7de"/>
  <text x="{PAD}" y="30" class="title">Habit Streak</text>
  <text x="{width - PAD}" y="30" text-anchor="end" class="mut" font-size="14" font-weight="600">{year}</text>
  {stats_svg}
  {month_labels}
  {"".join(cells)}
  {legend}
</svg>
'''


def main():
    days = git_days()
    problems = count_problems()
    stats = compute_stats(days)

    os.makedirs("public", exist_ok=True)
    with open("public/data.json", "w") as f:
        json.dump({"days": days, "problemsSolved": problems}, f, indent=2)

    os.makedirs("assets", exist_ok=True)
    with open("assets/streak.svg", "w") as f:
        f.write(build_svg(days, problems, stats))

    print(f"days={len(days)} total={stats[0]} problems={problems} "
          f"longest={stats[2]} current={stats[3]}")


if __name__ == "__main__":
    main()
