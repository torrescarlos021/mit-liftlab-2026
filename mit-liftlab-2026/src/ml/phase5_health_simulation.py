"""
Phase 5 — Monte-Carlo Health-Impact Simulation
==============================================
MIT LiftLab 2026 — From Nanostores to Classrooms

Projects the effect of the proposed school-based intervention on a simulated
cohort of N students over 1, 3, and 5 years, drawing effect-size parameters
from published meta-analyses.

Key design choices and disclaimers:

  * Effect sizes are sampled from Normal(μ, σ) with σ derived from each
    meta-analysis's 95 % CI.  This is a standard convention for Monte-Carlo
    over published estimates, NOT a claim about the true distribution.

  * Five scenarios are run: baseline, central, optimistic, conservative, and
    null_robustness.  The null robustness scenario uses the long-term
    null result (Hodder 2021) and is reported alongside the positive ones
    to avoid cherry-picking.

  * This is a PROJECTION, not a PREDICTION.  Any deployment would require
    pilot validation with real students.

Inputs:
    src/data/literature_parameters.json

Outputs:
    results/phase5_runs.csv             — all run-level outputs
    results/phase5_summary.csv          — per-scenario means + 5–95 % CIs
    results/phase5_trajectories.png     — BMI trajectory chart with bands
    results/phase5_prevalence.png       — overweight + obesity prevalence
    results/phase5_sensitivity.png      — adherence × dose heat-map
    results/phase5_summary.md           — human-readable findings

Usage:
    python src/ml/phase5_health_simulation.py
    python src/ml/phase5_health_simulation.py --runs 1000   # fewer runs for testing
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

# ──────────────────────────────────────────────────────────────────────────
# Paths
# ──────────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[2]
PARAMS = ROOT / "src" / "data" / "literature_parameters.json"
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True, parents=True)

sns.set_style("whitegrid")
plt.rcParams.update({"figure.dpi": 110, "savefig.dpi": 140, "font.size": 10})


# ──────────────────────────────────────────────────────────────────────────
# Model components
# ──────────────────────────────────────────────────────────────────────────
def init_cohort(n: int, mean_bmi: float, sd_bmi: float, rng) -> np.ndarray:
    """Initialize a cohort of n students with BMI ~ Normal(mean, sd)."""
    return rng.normal(mean_bmi, sd_bmi, size=n)


def annual_growth(n: int, mean_growth: float, sd_growth: float, rng) -> np.ndarray:
    """Random per-student annual BMI change without intervention."""
    return rng.normal(mean_growth, sd_growth, size=n)


def effect_for_scenario(scenario: str, params: dict, rng) -> float:
    """
    Sample an effect size (kg/m² applied to annual BMI growth) given scenario.

    Uses the PA + nutrition combined effect (closest to our proposal).
    """
    effects = params["intervention_effects"]

    if scenario == "baseline":
        return 0.0

    if scenario == "null_robustness":
        e = effects["long_term_null_robustness"]
        return float(rng.normal(e["mean_bmi_change_kg_m2"], e["sigma_bmi_change"]))

    e = effects["physical_activity_plus_nutrition"]
    mu, sigma = e["mean_bmi_change_kg_m2"], e["sigma_bmi_change"]

    if scenario == "central":
        return float(rng.normal(mu, sigma))
    if scenario == "optimistic":
        # Best-case for health = LARGEST reduction = lower bound of CI (most negative)
        return float(rng.normal(e["ci_lower"], sigma / 2))
    if scenario == "conservative":
        # Worst-case for health (still benefits) = SMALLEST reduction = upper bound of CI
        return float(rng.normal(e["ci_upper"], sigma / 2))
    raise ValueError(f"Unknown scenario: {scenario}")


def prevalence(bmi_vec: np.ndarray, threshold: float) -> float:
    """% of cohort at or above an overweight/obesity threshold."""
    return 100.0 * (bmi_vec >= threshold).mean()


# ──────────────────────────────────────────────────────────────────────────
# Main simulation loop
# ──────────────────────────────────────────────────────────────────────────
def run_scenario(scenario: str, params: dict, n_runs: int,
                 adherence: float, dose: float, rng) -> pd.DataFrame:
    """
    Run `n_runs` Monte-Carlo replicates of `scenario`.
    Returns one row per (run, horizon).
    """
    cfg = params["simulation_settings"]
    base = params["baseline_population"]
    horizons = cfg["horizons_years"]
    cohort_size = cfg["cohort_size"]
    overweight_thr = base["overweight_threshold_age_12"]
    obesity_thr = base["obesity_threshold_age_12"]

    rows = []

    for r in range(n_runs):
        # Initial cohort
        bmi = init_cohort(cohort_size, base["mean_bmi_age_12"],
                          base["sd_bmi_age_12"], rng)
        baseline_overweight = prevalence(bmi, overweight_thr)
        baseline_obesity = prevalence(bmi, obesity_thr)

        # Draw effect for this run (intervention effect scales with adherence × dose)
        eff_full = effect_for_scenario(scenario, params, rng)
        effective_eff = eff_full * adherence * dose

        # Project year by year
        current = bmi.copy()
        max_h = max(horizons)
        traj_means = []
        traj_overweight = []
        traj_obesity = []

        for year in range(1, max_h + 1):
            growth = annual_growth(cohort_size,
                                   base["annual_bmi_growth_no_intervention_mean"],
                                   base["annual_bmi_growth_no_intervention_sd"], rng)
            current = current + growth + effective_eff
            traj_means.append(current.mean())
            traj_overweight.append(prevalence(current, overweight_thr))
            traj_obesity.append(prevalence(current, obesity_thr))

        for h in horizons:
            rows.append({
                "scenario": scenario,
                "run": r,
                "adherence": adherence,
                "dose": dose,
                "horizon_yr": h,
                "effect_drawn": eff_full,
                "effective_effect": effective_eff,
                "baseline_mean_bmi": bmi.mean(),
                "horizon_mean_bmi": traj_means[h - 1],
                "delta_bmi": traj_means[h - 1] - bmi.mean(),
                "baseline_overweight_pct": baseline_overweight,
                "horizon_overweight_pct": traj_overweight[h - 1],
                "baseline_obesity_pct": baseline_obesity,
                "horizon_obesity_pct": traj_obesity[h - 1],
            })

    return pd.DataFrame(rows)


# ──────────────────────────────────────────────────────────────────────────
# Output / charts
# ──────────────────────────────────────────────────────────────────────────
def summarize(all_runs: pd.DataFrame) -> pd.DataFrame:
    """Per-scenario × horizon summary with mean and 5–95 % bands."""
    g = (all_runs[(all_runs["adherence"] == 0.80) & (all_runs["dose"] == 1.0)]
         .groupby(["scenario", "horizon_yr"]))
    return g.agg(
        mean_delta_bmi=("delta_bmi", "mean"),
        p5_delta_bmi=("delta_bmi", lambda x: np.percentile(x, 5)),
        p95_delta_bmi=("delta_bmi", lambda x: np.percentile(x, 95)),
        mean_overweight_pct=("horizon_overweight_pct", "mean"),
        p5_overweight=("horizon_overweight_pct", lambda x: np.percentile(x, 5)),
        p95_overweight=("horizon_overweight_pct", lambda x: np.percentile(x, 95)),
        mean_obesity_pct=("horizon_obesity_pct", "mean"),
        p5_obesity=("horizon_obesity_pct", lambda x: np.percentile(x, 5)),
        p95_obesity=("horizon_obesity_pct", lambda x: np.percentile(x, 95)),
    ).round(3).reset_index()


def plot_trajectories(summary: pd.DataFrame, path: Path):
    """Per-scenario mean ΔBMI with 5–95 % bands."""
    fig, ax = plt.subplots(figsize=(10, 6))
    palette = {
        "baseline": "#888888",
        "central": "#0066cc",
        "optimistic": "#26a269",
        "conservative": "#cc7700",
        "null_robustness": "#cc3333",
    }
    for sc in summary["scenario"].unique():
        sub = summary[summary["scenario"] == sc].sort_values("horizon_yr")
        ax.plot(sub["horizon_yr"], sub["mean_delta_bmi"],
                marker="o", linewidth=2.2, label=sc, color=palette.get(sc, "k"))
        ax.fill_between(sub["horizon_yr"],
                        sub["p5_delta_bmi"], sub["p95_delta_bmi"],
                        alpha=0.15, color=palette.get(sc, "k"))

    ax.axhline(0, color="black", linewidth=0.7, linestyle=":")
    ax.set_xlabel("Years from intervention start")
    ax.set_ylabel("Mean ΔBMI (kg/m²) vs cohort baseline")
    ax.set_title("Projected BMI change by scenario (5–95 % uncertainty bands)",
                 fontweight="bold")
    ax.legend(loc="best")
    plt.tight_layout()
    plt.savefig(path, bbox_inches="tight")
    plt.close()


def plot_prevalence(summary: pd.DataFrame, path: Path):
    """Side-by-side bar chart of horizon overweight + obesity prevalence."""
    horizons = sorted(summary["horizon_yr"].unique())
    scenarios = summary["scenario"].unique()

    fig, axes = plt.subplots(1, len(horizons), figsize=(13, 5), sharey=True)
    if len(horizons) == 1:
        axes = [axes]

    for ax, h in zip(axes, horizons):
        sub = summary[summary["horizon_yr"] == h].sort_values("scenario")
        x = np.arange(len(sub))
        ax.bar(x, sub["mean_overweight_pct"], color="#0066cc", alpha=0.85,
               label="Overweight+ %")
        ax.bar(x, sub["mean_obesity_pct"], color="#cc3333", alpha=0.85,
               label="Obesity %")
        ax.set_xticks(x)
        ax.set_xticklabels(sub["scenario"], rotation=30, ha="right")
        ax.set_title(f"Year {h}")
        ax.set_ylabel("Prevalence in cohort (%)")
        ax.legend(loc="best", fontsize=8)

    plt.suptitle("Projected overweight + obesity prevalence by scenario",
                 fontweight="bold")
    plt.tight_layout()
    plt.savefig(path, bbox_inches="tight")
    plt.close()


def plot_sensitivity(all_runs: pd.DataFrame, path: Path, horizon=3):
    """Heat-map: ΔBMI as function of adherence × dose, central scenario."""
    sub = all_runs[
        (all_runs["scenario"] == "central") &
        (all_runs["horizon_yr"] == horizon)
    ]
    if sub.empty:
        return
    pivot = sub.groupby(["adherence", "dose"])["delta_bmi"].mean().unstack()

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(pivot, annot=True, fmt=".3f", cmap="RdBu_r", center=0,
                cbar_kws={"label": "Mean ΔBMI (kg/m²)"}, ax=ax)
    ax.set_xlabel("Dose (additional intervention hours/week, scaled)")
    ax.set_ylabel("Adherence rate")
    ax.set_title(f"Sensitivity at year {horizon} — central scenario",
                 fontweight="bold")
    plt.tight_layout()
    plt.savefig(path, bbox_inches="tight")
    plt.close()


# ──────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────
def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--runs", type=int, default=None,
                   help="Override number of runs per scenario (default: from params)")
    p.add_argument("--seed", type=int, default=None,
                   help="Override random seed (default: from params)")
    return p.parse_args()


def main():
    args = parse_args()
    if not PARAMS.exists():
        sys.exit(f"ERROR: parameters file not found at {PARAMS}")

    with open(PARAMS, encoding="utf-8") as f:
        params = json.load(f)

    cfg = params["simulation_settings"]
    n_runs = args.runs or cfg["n_runs_per_scenario"]
    seed = args.seed or cfg["random_seed"]
    rng = np.random.default_rng(seed)

    print("=== Phase 5 — Monte-Carlo Health-Impact Simulation ===")
    print(f"Cohort size: {cfg['cohort_size']}    Runs per scenario: {n_runs}")
    print(f"Seed: {seed}    Horizons: {cfg['horizons_years']}\n")

    scenarios = params["scenarios"]
    all_runs = []

    # Primary: each scenario at default adherence/dose
    for sc in scenarios:
        print(f"  Running scenario: {sc} ...")
        df_sc = run_scenario(sc, params, n_runs,
                             cfg["default_adherence_rate"],
                             cfg["default_intervention_dose_hours_per_week"],
                             rng)
        all_runs.append(df_sc)

    # Sensitivity sweep on central scenario only
    sweeps = params["sensitivity_sweeps"]
    print("\n  Sensitivity sweep on 'central' scenario (adherence × dose) ...")
    for adh in sweeps["adherence_rates"]:
        for dose in sweeps["dose_hours"]:
            if adh == cfg["default_adherence_rate"] and dose == cfg["default_intervention_dose_hours_per_week"]:
                continue  # already covered above
            df_sw = run_scenario("central", params, max(500, n_runs // 10),
                                 adh, dose, rng)
            all_runs.append(df_sw)

    all_runs = pd.concat(all_runs, ignore_index=True)
    all_runs.to_csv(OUT / "phase5_runs.csv", index=False)
    print(f"\n  Saved {len(all_runs):,} run-level rows to phase5_runs.csv")

    summary = summarize(all_runs)
    summary.to_csv(OUT / "phase5_summary.csv", index=False)
    print("\nSummary by scenario × horizon:")
    print(summary.to_string(index=False))

    # Charts
    plot_trajectories(summary, OUT / "phase5_trajectories.png")
    plot_prevalence(summary, OUT / "phase5_prevalence.png")
    plot_sensitivity(all_runs, OUT / "phase5_sensitivity.png", horizon=3)

    # Markdown summary
    md = ["# Phase 5 — Monte-Carlo Health-Impact Simulation\n\n",
          f"**Cohort:** {cfg['cohort_size']} simulated students.  "
          f"**Runs/scenario:** {n_runs}.  **Seed:** {seed}.\n\n",
          "## Scenario summary\n\n",
          "| Scenario | Horizon (yr) | Mean ΔBMI | 5–95 % | Mean overweight+ % | Mean obesity % |\n",
          "|---|---|---|---|---|---|\n"]
    for _, r in summary.iterrows():
        md.append(
            f"| {r['scenario']} | {r['horizon_yr']} | "
            f"{r['mean_delta_bmi']:+.3f} | "
            f"[{r['p5_delta_bmi']:+.3f}, {r['p95_delta_bmi']:+.3f}] | "
            f"{r['mean_overweight_pct']:.2f} | "
            f"{r['mean_obesity_pct']:.2f} |\n"
        )
    md.append("\n## Notes\n")
    md.append("- The `null_robustness` row uses the long-term null result\n")
    md.append("  (Hodder 2021) and is included to test robustness rather than\n")
    md.append("  to claim it as our prediction.\n")
    md.append("- All effect sizes drawn from published meta-analyses;\n")
    md.append("  see `src/data/literature_parameters.json` for sources.\n")
    md.append("- Charts in `results/phase5_*.png`.\n")
    (OUT / "phase5_summary.md").write_text("".join(md), encoding="utf-8")

    print("\n=== Phase 5 complete ===")
    print(f"Outputs in {OUT}/:")
    for fn in sorted(OUT.glob("phase5_*")):
        print(f"  - {fn.name}")


if __name__ == "__main__":
    main()
