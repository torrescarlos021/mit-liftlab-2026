"""
ACT 4 — The Intervention & Monte-Carlo Projection
=================================================
MIT LiftLab 2026 · ¿Qué factores impiden la compra de productos saludables
en las nanostores de México?

THE STORY
---------
Acts 1-3 converged: the barrier to healthy purchasing is structural and
behavioural (price perception, availability, time), reinforced by the supply
chain — and crucially, NOT a lack of knowledge or willingness. People already
know and already want; what's missing are the habits and skills to act on it
inside a constrained environment.

So our intervention is future-facing: strengthen Physical Education and the
"Vida Saludable" articulating axis in lower-secondary education, to build the
price-savvy, label-literate habits of the NEXT generation of nanostore shoppers.

This script projects the intervention's impact on student BMI over 1, 3, and 5
years with a Monte-Carlo simulation, drawing effect sizes from published
meta-analyses. It reports a null-robustness scenario alongside the positive
ones — honesty over hype.

Inputs:
    data/literature_parameters.json

Outputs:
    results/act4_summary.csv
    results/act4_summary.md
    results/act4_trajectories.png
    results/act4_prevalence.png
    results/act4_sensitivity.png

Usage:
    python src/act4_montecarlo_intervention.py
    python src/act4_montecarlo_intervention.py --runs 1000
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
PARAMS = ROOT / "data" / "literature_parameters.json"
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True, parents=True)

sns.set_style("whitegrid")
plt.rcParams.update({"figure.dpi": 110, "savefig.dpi": 140, "font.size": 10})


def init_cohort(n, mean, sd, rng):
    return rng.normal(mean, sd, size=n)


def effect_for_scenario(scenario, params, rng):
    e = params["intervention_effects"]
    if scenario == "baseline":
        return 0.0
    if scenario == "null_robustness":
        x = e["long_term_null_robustness"]
        return float(rng.normal(x["mean_bmi_change_kg_m2"], x["sigma_bmi_change"]))
    pn = e["physical_activity_plus_nutrition"]
    mu, sigma = pn["mean_bmi_change_kg_m2"], pn["sigma_bmi_change"]
    if scenario == "central":
        return float(rng.normal(mu, sigma))
    if scenario == "optimistic":      # best for health = largest reduction = lower CI bound
        return float(rng.normal(pn["ci_lower"], sigma / 2))
    if scenario == "conservative":    # smallest reduction = upper CI bound
        return float(rng.normal(pn["ci_upper"], sigma / 2))
    raise ValueError(scenario)


def prevalence(bmi, thr):
    return 100.0 * (bmi >= thr).mean()


def run_scenario(scenario, params, n_runs, adherence, dose, rng):
    cfg = params["simulation_settings"]; base = params["baseline_population"]
    horizons = cfg["horizons_years"]; N = cfg["cohort_size"]
    ow_thr = base["overweight_threshold_age_12"]; ob_thr = base["obesity_threshold_age_12"]
    rows = []
    max_h = max(horizons)
    for r in range(n_runs):
        bmi = init_cohort(N, base["mean_bmi_age_12"], base["sd_bmi_age_12"], rng)
        b_ow, b_ob = prevalence(bmi, ow_thr), prevalence(bmi, ob_thr)
        eff = effect_for_scenario(scenario, params, rng) * adherence * dose
        cur = bmi.copy(); tm = []; tow = []; tob = []
        for _ in range(1, max_h + 1):
            g = rng.normal(base["annual_bmi_growth_no_intervention_mean"],
                           base["annual_bmi_growth_no_intervention_sd"], size=N)
            cur = cur + g + eff
            tm.append(cur.mean()); tow.append(prevalence(cur, ow_thr)); tob.append(prevalence(cur, ob_thr))
        for h in horizons:
            rows.append({"scenario": scenario, "run": r, "adherence": adherence, "dose": dose,
                         "horizon_yr": h, "delta_bmi": tm[h-1] - bmi.mean(),
                         "overweight_pct": tow[h-1], "obesity_pct": tob[h-1],
                         "baseline_obesity_pct": b_ob})
    return pd.DataFrame(rows)


def summarize(runs):
    cfg_a, cfg_d = 0.80, 1.0
    g = runs[(runs.adherence == cfg_a) & (runs.dose == cfg_d)].groupby(["scenario", "horizon_yr"])
    return g.agg(
        mean_delta_bmi=("delta_bmi", "mean"),
        p5=("delta_bmi", lambda x: np.percentile(x, 5)),
        p95=("delta_bmi", lambda x: np.percentile(x, 95)),
        mean_overweight=("overweight_pct", "mean"),
        mean_obesity=("obesity_pct", "mean"),
    ).round(3).reset_index()


def plot_traj(summary, path):
    pal = {"baseline": "#8a7d6e", "central": "#1d4e89", "optimistic": "#2d5e3e",
           "conservative": "#b8862a", "null_robustness": "#b8332a"}
    fig, ax = plt.subplots(figsize=(10, 6))
    for sc in summary.scenario.unique():
        s = summary[summary.scenario == sc].sort_values("horizon_yr")
        ax.plot(s.horizon_yr, s.mean_delta_bmi, marker="o", lw=2.4, label=sc, color=pal.get(sc, "k"))
        ax.fill_between(s.horizon_yr, s.p5, s.p95, alpha=0.13, color=pal.get(sc, "k"))
    ax.axhline(0, color="black", lw=0.7, ls=":")
    ax.set_xlabel("Years from intervention start"); ax.set_ylabel("Mean ΔBMI (kg/m²)")
    ax.set_title("Act 4 — Projected BMI change by scenario (5–95% bands)", fontweight="bold")
    ax.legend(); plt.tight_layout(); plt.savefig(path, bbox_inches="tight"); plt.close()


def plot_prev(summary, path):
    hs = sorted(summary.horizon_yr.unique())
    fig, axes = plt.subplots(1, len(hs), figsize=(13, 5), sharey=True)
    if len(hs) == 1: axes = [axes]
    for ax, h in zip(axes, hs):
        s = summary[summary.horizon_yr == h].sort_values("scenario")
        x = np.arange(len(s))
        ax.bar(x, s.mean_overweight, color="#1d4e89", alpha=0.85, label="Overweight+ %")
        ax.bar(x, s.mean_obesity, color="#b8332a", alpha=0.9, label="Obesity %")
        ax.set_xticks(x); ax.set_xticklabels(s.scenario, rotation=30, ha="right")
        ax.set_title(f"Year {h}"); ax.set_ylabel("Cohort prevalence (%)"); ax.legend(fontsize=8)
    plt.suptitle("Act 4 — Projected overweight + obesity prevalence", fontweight="bold")
    plt.tight_layout(); plt.savefig(path, bbox_inches="tight"); plt.close()


def plot_sens(runs, path, horizon=3):
    sub = runs[(runs.scenario == "central") & (runs.horizon_yr == horizon)]
    if sub.empty: return
    piv = sub.groupby(["adherence", "dose"]).delta_bmi.mean().unstack()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(piv, annot=True, fmt=".3f", cmap="RdBu_r", center=0,
                cbar_kws={"label": "Mean ΔBMI (kg/m²)"}, ax=ax)
    ax.set_xlabel("Dose (extra hours/week, scaled)"); ax.set_ylabel("Adherence rate")
    ax.set_title(f"Act 4 — Sensitivity at year {horizon} (central scenario)", fontweight="bold")
    plt.tight_layout(); plt.savefig(path, bbox_inches="tight"); plt.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=None)
    ap.add_argument("--seed", type=int, default=None)
    args = ap.parse_args()
    if not PARAMS.exists():
        sys.exit(f"ERROR: missing {PARAMS}")
    params = json.load(open(PARAMS, encoding="utf-8"))
    cfg = params["simulation_settings"]
    n_runs = args.runs or cfg["n_runs_per_scenario"]
    seed = args.seed or cfg["random_seed"]
    rng = np.random.default_rng(seed)

    print(f"=== ACT 4 — Monte-Carlo Intervention ===")
    print(f"Cohort {cfg['cohort_size']}  runs/scenario {n_runs}  seed {seed}\n")

    all_runs = []
    for sc in params["scenarios"]:
        print(f"  scenario: {sc}")
        all_runs.append(run_scenario(sc, params, n_runs,
                                     cfg["default_adherence_rate"],
                                     cfg["default_intervention_dose_hours_per_week"], rng))
    sw = params["sensitivity_sweeps"]
    print("  sensitivity sweep (central)...")
    for a in sw["adherence_rates"]:
        for d in sw["dose_hours"]:
            if a == cfg["default_adherence_rate"] and d == cfg["default_intervention_dose_hours_per_week"]:
                continue
            all_runs.append(run_scenario("central", params, max(500, n_runs // 10), a, d, rng))
    runs = pd.concat(all_runs, ignore_index=True)

    summary = summarize(runs)
    summary.to_csv(OUT / "act4_summary.csv", index=False)
    print("\n" + summary.to_string(index=False))

    plot_traj(summary, OUT / "act4_trajectories.png")
    plot_prev(summary, OUT / "act4_prevalence.png")
    plot_sens(runs, OUT / "act4_sensitivity.png", horizon=3)

    md = [f"# Act 4 — Intervention & Monte-Carlo Projection\n\n",
          f"Cohort {cfg['cohort_size']}, {n_runs} runs/scenario, seed {seed}.\n\n",
          "| Scenario | Year | Mean ΔBMI | 5–95% | Overweight+ % | Obesity % |\n|---|---|---|---|---|---|\n"]
    for _, r in summary.iterrows():
        md.append(f"| {r.scenario} | {int(r.horizon_yr)} | {r.mean_delta_bmi:+.3f} | "
                  f"[{r.p5:+.3f}, {r.p95:+.3f}] | {r.mean_overweight:.1f} | {r.mean_obesity:.1f} |\n")
    md += ["\n**Honesty note.** The `null_robustness` scenario (Hodder 2021) is reported alongside ",
           "the positive ones. The intervention is future-facing: it targets the intention–action ",
           "gap (39.1 pp) measured in Acts 2–3, by building habits in the next generation of shoppers.\n"]
    (OUT / "act4_summary.md").write_text("".join(md), encoding="utf-8")

    print(f"\n=== Act 4 complete ===  Outputs in {OUT}/")
    for fn in sorted(OUT.glob("act4_*")):
        print(f"   - {fn.name}")


if __name__ == "__main__":
    main()
