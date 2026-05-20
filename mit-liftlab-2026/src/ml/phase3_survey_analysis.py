"""
Phase 3 — Primary Survey Analysis (n = 104)
===========================================
MIT LiftLab 2026 — From Nanostores to Classrooms

This script re-analyzes the eating-habits survey to test five claims that
underpin our intervention design:

    H1  Lack of time is the dominant barrier reported.
    H2  Parents are concerned about their children's diet.
    H3  Children given money buy ultraprocessed items predominantly.
    H4  The population itself names "nutrition education" and "more access
        to healthy food" as top desired solutions.
    H5  Willingness to change is high — the limiting factor is structural.

Inputs:
    src/data/survey_responses.csv   (CSV with ';' delimiter)

Outputs:
    results/phase3_summary.md          — human-readable findings
    results/phase3_frequencies.csv     — frequency tables per question
    results/phase3_charts/             — bar charts per finding

Usage:
    python src/ml/phase3_survey_analysis.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from collections import Counter

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

# ──────────────────────────────────────────────────────────────────────────
# Paths
# ──────────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "src" / "data" / "survey_responses.csv"
OUT = ROOT / "results"
CHARTS = OUT / "phase3_charts"
OUT.mkdir(exist_ok=True, parents=True)
CHARTS.mkdir(exist_ok=True, parents=True)

sns.set_style("whitegrid")
plt.rcParams.update({"figure.dpi": 110, "savefig.dpi": 140, "font.size": 10})


# ──────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────
def clean_str(x):
    """Strip whitespace, normalize whitespace, return None for empties."""
    if pd.isna(x):
        return None
    s = re.sub(r"\s+", " ", str(x)).strip()
    return s if s else None


def split_multi(value: str | None, separators=(";", "·", ",")):
    """Split a multi-select cell into individual options."""
    if not value:
        return []
    # The Forms export usually uses ';' inside a single cell for multi-select
    pattern = "|".join(re.escape(s) for s in separators)
    parts = re.split(pattern, value)
    return [p.strip() for p in parts if p and p.strip()]


def count_freq(series: pd.Series, multi=False, top=None) -> pd.Series:
    """Frequency count for a single column. If multi=True, split each cell."""
    if multi:
        all_vals = []
        for v in series.dropna():
            all_vals.extend(split_multi(v))
        counts = pd.Series(Counter(all_vals)).sort_values(ascending=False)
    else:
        counts = series.dropna().apply(clean_str).value_counts()
    if top:
        counts = counts.head(top)
    return counts


def bar_chart(counts: pd.Series, title: str, xlabel: str, path: Path,
              palette="viridis", top=10):
    """Horizontal bar chart for a frequency series."""
    counts = counts.head(top)
    fig, ax = plt.subplots(figsize=(10, max(3, 0.5 * len(counts) + 1)))

    colors = sns.color_palette(palette, n_colors=len(counts))
    bars = ax.barh(range(len(counts)), counts.values, color=colors, edgecolor="white")
    ax.set_yticks(range(len(counts)))
    ax.set_yticklabels([str(i)[:55] for i in counts.index])
    ax.invert_yaxis()
    ax.set_xlabel(xlabel)
    ax.set_title(title, fontweight="bold")

    # value labels
    for bar, val in zip(bars, counts.values):
        ax.text(val + 0.3, bar.get_y() + bar.get_height() / 2,
                f"{int(val)}", va="center", fontsize=9)

    plt.tight_layout()
    plt.savefig(path, bbox_inches="tight")
    plt.close()


# ──────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────
def main():
    if not DATA.exists():
        sys.exit(f"ERROR: data file not found at {DATA}")

    df = pd.read_csv(DATA, sep=";", encoding="utf-8")
    df.columns = [c.strip() for c in df.columns]
    n = len(df)

    print(f"\n=== Phase 3 — Survey Analysis ===")
    print(f"Loaded {n} responses from {DATA.name}\n")

    # ──────────────────────────────────────────────────────────────
    # Quick descriptors
    # ──────────────────────────────────────────────────────────────
    print("Age distribution:")
    age_counts = count_freq(df["Edad"])
    print(age_counts.to_string())

    print("\nOccupation distribution:")
    occ_col = [c for c in df.columns if "trabajo" in c.lower()][0]
    occ_counts = count_freq(df[occ_col])
    print(occ_counts.head(10).to_string())

    print("\nParental status distribution:")
    parent_col = [c for c in df.columns if "padre" in c.lower()
                  and "soltero" not in c.lower()][0]
    parent_counts = count_freq(df[parent_col])
    print(parent_counts.to_string())

    bar_chart(age_counts, "Age distribution of respondents",
              "Count", CHARTS / "00_age_distribution.png", palette="crest")
    bar_chart(occ_counts, "Occupation distribution",
              "Count", CHARTS / "01_occupation.png", palette="mako")

    # ──────────────────────────────────────────────────────────────
    # H1 — Lack of time is the dominant barrier
    # ──────────────────────────────────────────────────────────────
    print("\n──── H1: Why don't you cook? ────")
    why_cols = [c for c in df.columns if "Por que no cocinas" in c
                or "Por qué no cocinas" in c]
    why_all = pd.concat([df[c] for c in why_cols], ignore_index=True)
    why_counts = count_freq(why_all, multi=True)
    print(why_counts.head(15).to_string())
    bar_chart(why_counts, "Reasons not to cook frequently (all respondents)",
              "Count", CHARTS / "02_why_not_cook.png", palette="rocket")

    # ──────────────────────────────────────────────────────────────
    # H2 — Parental concern
    # ──────────────────────────────────────────────────────────────
    print("\n──── H2: Parental concern level ────")
    concern_col = [c for c in df.columns if "preocupado" in c.lower()
                   and "hijos" in c.lower()]
    if concern_col:
        concern = count_freq(df[concern_col[0]])
        print(concern.to_string())
        bar_chart(concern, "Parental concern about child diet",
                  "Count (parents only)", CHARTS / "03_parental_concern.png",
                  palette="flare")

    # ──────────────────────────────────────────────────────────────
    # H3 — What do kids buy with parental money?
    # ──────────────────────────────────────────────────────────────
    print("\n──── H3: What do children buy with parental money? ────")
    buy_col = [c for c in df.columns if ("tipo de alimentos suelen comprar" in c)]
    if buy_col:
        buy_freq = count_freq(df[buy_col[0]], multi=True)
        print(buy_freq.head(10).to_string())
        bar_chart(buy_freq, "Items children buy with parental money",
                  "Count", CHARTS / "04_children_purchases.png", palette="rocket_r")

    # ──────────────────────────────────────────────────────────────
    # H4 — Top requested solutions (key result)
    # ──────────────────────────────────────────────────────────────
    print("\n──── H4: Most-requested solutions ────")
    sol_cols = [c for c in df.columns
                if "soluciones" in c.lower() and "podrían ayudar" in c.lower()]
    sol_all = pd.concat([df[c] for c in sol_cols], ignore_index=True)
    sol_freq = count_freq(sol_all, multi=True)
    print(sol_freq.head(10).to_string())
    bar_chart(sol_freq, "Solutions requested by respondents",
              "Count (all)", CHARTS / "05_requested_solutions.png", palette="crest")

    # ──────────────────────────────────────────────────────────────
    # H5 — Willingness to change
    # ──────────────────────────────────────────────────────────────
    print("\n──── H5: Willingness to change habits ────")
    will_cols = [c for c in df.columns
                 if "cambiar tus hábitos" in c or "cambiar tus habitos" in c]
    will_all = pd.concat([df[c] for c in will_cols], ignore_index=True)
    will_freq = count_freq(will_all)
    print(will_freq.to_string())
    bar_chart(will_freq, "Willingness to change habits with more time/resources",
              "Count", CHARTS / "06_willingness.png", palette="viridis")

    # ──────────────────────────────────────────────────────────────
    # Cross-tab: parental status × concern
    # ──────────────────────────────────────────────────────────────
    print("\n──── Cross-tab: parental status × concern ────")
    if concern_col:
        ct = pd.crosstab(df[parent_col].apply(clean_str),
                         df[concern_col[0]].apply(clean_str),
                         margins=True, margins_name="Total")
        print(ct.to_string())
        ct.to_csv(OUT / "phase3_crosstab_parent_concern.csv")

    # ──────────────────────────────────────────────────────────────
    # Persist frequency tables
    # ──────────────────────────────────────────────────────────────
    freq_tables = {
        "age": age_counts,
        "occupation": occ_counts,
        "parental_status": parent_counts,
        "why_not_cook": why_counts,
        "children_buy": (buy_freq if buy_col else pd.Series(dtype=int)),
        "requested_solutions": sol_freq,
        "willingness": will_freq,
    }
    rows = []
    for k, v in freq_tables.items():
        for label, count in v.items():
            rows.append({"question": k, "answer": label, "count": int(count)})
    pd.DataFrame(rows).to_csv(OUT / "phase3_frequencies.csv", index=False)

    # ──────────────────────────────────────────────────────────────
    # Markdown summary
    # ──────────────────────────────────────────────────────────────
    md = []
    md.append("# Phase 3 — Survey Analysis Summary\n")
    md.append(f"**N = {n} responses**  ·  Region: San Luis Potosí  ·  ")
    md.append("Dec 2025 – Jan 2026\n\n")

    md.append("## H1 — Why respondents don't cook frequently\n")
    md.append("| Reason | Count |\n|---|---|\n")
    for k, v in why_counts.head(10).items():
        md.append(f"| {k} | {int(v)} |\n")

    if concern_col:
        md.append("\n## H2 — Parental concern about child diet\n")
        md.append("| Level of concern | Count |\n|---|---|\n")
        for k, v in concern.items():
            md.append(f"| {k} | {int(v)} |\n")

    if buy_col:
        md.append("\n## H3 — What children buy with parental money\n")
        md.append("| Purchase | Count |\n|---|---|\n")
        for k, v in buy_freq.head(10).items():
            md.append(f"| {k} | {int(v)} |\n")

    md.append("\n## H4 — Requested solutions (key result)\n")
    md.append("| Solution | Count |\n|---|---|\n")
    for k, v in sol_freq.head(10).items():
        md.append(f"| {k} | {int(v)} |\n")

    md.append("\n## H5 — Willingness to change habits\n")
    md.append("| Answer | Count |\n|---|---|\n")
    for k, v in will_freq.items():
        md.append(f"| {k} | {int(v)} |\n")

    md.append("\n---\n")
    md.append("Charts in `results/phase3_charts/`. Frequency CSV in ")
    md.append("`results/phase3_frequencies.csv`.\n")

    (OUT / "phase3_summary.md").write_text("".join(md), encoding="utf-8")

    print("\n\n=== Phase 3 complete ===")
    print(f"Results written to:  {OUT}")
    for fn in sorted(OUT.glob("phase3_*")):
        print(f"  - {fn.name}")
    print(f"Charts saved in:     {CHARTS}")


if __name__ == "__main__":
    main()
