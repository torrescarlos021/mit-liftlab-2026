"""
Phase 1 — Linear Regression on Nanostore and Health Data
========================================================
MIT LiftLab 2026 — From Nanostores to Classrooms

This script answers the question:
    Does state-level nanostore density correlate with childhood
    overweight + obesity prevalence after controlling for marginalization
    and urbanization?

It fits two nested OLS models per dependent variable (5–11 yr and 12–19 yr)
and reports full diagnostics: coefficients, R², VIF, Breusch–Pagan, residual
normality, and Cook's distance for influential observations.

Inputs:
    src/data/state_data.csv

Outputs:
    results/phase1_summary.txt        — text summary
    results/phase1_coefficients.csv   — coefficient table
    results/phase1_diagnostics.csv    — diagnostic statistics
    results/phase1_residuals.png      — residual plots
    results/phase1_scatter.png        — scatter with fit line

Usage:
    python src/ml/phase1_regression.py

Author: Carlos Torres / MIT LiftLab 2026
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_breuschpagan
from scipy import stats

# ──────────────────────────────────────────────────────────────────────────
# Paths
# ──────────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "src" / "data" / "state_data.csv"
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True, parents=True)

# Plot style
sns.set_style("whitegrid")
plt.rcParams.update({"figure.dpi": 110, "savefig.dpi": 140, "font.size": 10})


# ──────────────────────────────────────────────────────────────────────────
# Utilities
# ──────────────────────────────────────────────────────────────────────────
def vif(df: pd.DataFrame) -> pd.DataFrame:
    """Variance Inflation Factor for each column in df (already includes const)."""
    return pd.DataFrame(
        {
            "variable": df.columns,
            "VIF": [variance_inflation_factor(df.values, i) for i in range(df.shape[1])],
        }
    )


def diagnostics(model) -> dict:
    """Return a dict of post-fit diagnostic statistics."""
    res = model.resid
    fitted = model.fittedvalues

    bp_stat, bp_p, _, _ = het_breuschpagan(res, model.model.exog)
    sw_stat, sw_p = stats.shapiro(res)
    influence = model.get_influence()
    cooks_d = influence.cooks_distance[0]

    return {
        "R²": model.rsquared,
        "R²_adj": model.rsquared_adj,
        "F-stat": model.fvalue,
        "F p-value": model.f_pvalue,
        "AIC": model.aic,
        "BIC": model.bic,
        "Breusch–Pagan stat": bp_stat,
        "Breusch–Pagan p": bp_p,
        "Shapiro–Wilk stat": sw_stat,
        "Shapiro–Wilk p": sw_p,
        "max Cook's D": cooks_d.max(),
        "n influential (Cook's > 4/n)": int((cooks_d > 4 / len(cooks_d)).sum()),
    }


def fit_ols(df: pd.DataFrame, y: str, X_cols: list[str]):
    """Fit a single OLS model with constant. Returns the fitted model."""
    X = sm.add_constant(df[X_cols])
    y_vec = df[y]
    return sm.OLS(y_vec, X).fit()


def plot_residuals(model, title: str, path: Path):
    """4-panel residual diagnostic plot."""
    res = model.resid
    fitted = model.fittedvalues
    sqrt_std_res = np.sqrt(np.abs((res - res.mean()) / res.std()))

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle(title, fontsize=12, fontweight="bold")

    # 1. Residual vs fitted
    axes[0, 0].scatter(fitted, res, alpha=0.7, edgecolors="k")
    axes[0, 0].axhline(0, color="red", linestyle="--", linewidth=1)
    axes[0, 0].set_xlabel("Fitted values")
    axes[0, 0].set_ylabel("Residuals")
    axes[0, 0].set_title("Residuals vs Fitted")

    # 2. Q-Q plot
    sm.qqplot(res, line="45", fit=True, ax=axes[0, 1])
    axes[0, 1].set_title("Normal Q–Q")

    # 3. Scale-location
    axes[1, 0].scatter(fitted, sqrt_std_res, alpha=0.7, edgecolors="k")
    axes[1, 0].set_xlabel("Fitted values")
    axes[1, 0].set_ylabel(r"$\sqrt{|standardized residuals|}$")
    axes[1, 0].set_title("Scale–Location")

    # 4. Cook's distance
    influence = model.get_influence()
    cooks = influence.cooks_distance[0]
    threshold = 4 / len(cooks)
    axes[1, 1].stem(range(len(cooks)), cooks, basefmt=" ")
    axes[1, 1].axhline(threshold, color="red", linestyle="--", linewidth=1,
                       label=f"4/n = {threshold:.3f}")
    axes[1, 1].set_xlabel("Observation index")
    axes[1, 1].set_ylabel("Cook's D")
    axes[1, 1].set_title("Influence (Cook's distance)")
    axes[1, 1].legend()

    plt.tight_layout()
    plt.savefig(path, bbox_inches="tight")
    plt.close()


def plot_scatter(df: pd.DataFrame, x: str, y: str, path: Path,
                 xlabel: str, ylabel: str, title: str):
    """Scatter with annotated state codes and OLS fit line."""
    fig, ax = plt.subplots(figsize=(9, 6))

    slope, intercept, r_val, p_val, _ = stats.linregress(df[x], df[y])
    xs = np.linspace(df[x].min(), df[x].max(), 100)
    ys = intercept + slope * xs

    ax.scatter(df[x], df[y], s=60, alpha=0.75, edgecolors="k", color="#0066cc")
    ax.plot(xs, ys, color="#cc3333", linewidth=2,
            label=f"OLS fit: y = {intercept:.2f} + {slope:.3f}x  |  R² = {r_val**2:.3f}, p = {p_val:.3f}")

    for _, row in df.iterrows():
        ax.annotate(row["state_name"][:6], (row[x], row[y]),
                    fontsize=7, alpha=0.7, xytext=(3, 3),
                    textcoords="offset points")

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(loc="best")
    plt.tight_layout()
    plt.savefig(path, bbox_inches="tight")
    plt.close()


# ──────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────
def main():
    if not DATA.exists():
        sys.exit(f"ERROR: data file not found at {DATA}")

    df = pd.read_csv(DATA)
    print(f"\n=== Phase 1 — Linear Regression ===")
    print(f"Loaded {len(df)} state-level observations from {DATA.name}\n")
    print(df[["state_name", "nanostore_density", "marginalization_index",
              "obesity_prev_5_11", "obesity_prev_12_19"]].describe().round(2))

    # ──────────────────────────────────────────────────────────────
    # Build two models per dependent variable: M1 simple, M2 controlled
    # ──────────────────────────────────────────────────────────────
    dep_vars = {
        "obesity_prev_5_11": "Children 5–11 (overweight + obesity %)",
        "obesity_prev_12_19": "Adolescents 12–19 (overweight + obesity %)",
    }

    all_diag = []
    all_coef = []

    for y, y_label in dep_vars.items():
        print(f"\n──── Dependent variable: {y_label} ────")

        # M1: simple bivariate
        m1 = fit_ols(df, y, ["nanostore_density"])
        # M2: full controlled
        m2 = fit_ols(df, y, ["nanostore_density", "marginalization_index",
                             "urbanization_pct"])

        for name, m in [("M1_simple", m1), ("M2_controlled", m2)]:
            d = diagnostics(m)
            d["model"] = f"{y}::{name}"
            all_diag.append(d)

            coef_df = pd.DataFrame({
                "model": f"{y}::{name}",
                "term": m.params.index,
                "coef": m.params.values,
                "std_err": m.bse.values,
                "t": m.tvalues.values,
                "p_value": m.pvalues.values,
                "ci_low": m.conf_int()[0].values,
                "ci_high": m.conf_int()[1].values,
            })
            all_coef.append(coef_df)

            print(f"\n--- {name} ---")
            print(m.summary())

        # VIF for the full model
        X2 = sm.add_constant(df[["nanostore_density", "marginalization_index",
                                  "urbanization_pct"]])
        vif_df = vif(X2)
        print(f"\nVIF for {y} (M2):")
        print(vif_df.to_string(index=False))

        # Plots
        plot_residuals(m2,
                       f"Residual diagnostics — M2 controlled — {y_label}",
                       OUT / f"phase1_residuals_{y}.png")
        plot_scatter(df, "nanostore_density", y,
                     OUT / f"phase1_scatter_{y}.png",
                     xlabel="Nanostore density (per 1,000 inhab.)",
                     ylabel=y_label,
                     title=f"State-level: nanostore density vs {y_label}")

    # ──────────────────────────────────────────────────────────────
    # Persist results
    # ──────────────────────────────────────────────────────────────
    pd.concat(all_coef, ignore_index=True).round(4).to_csv(
        OUT / "phase1_coefficients.csv", index=False)
    pd.DataFrame(all_diag).round(4).to_csv(
        OUT / "phase1_diagnostics.csv", index=False)

    # Human-readable summary
    with open(OUT / "phase1_summary.txt", "w") as f:
        f.write("PHASE 1 — LINEAR REGRESSION SUMMARY\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Observations: {len(df)} Mexican federal entities\n")
        f.write(f"Predictors:   nanostore_density, marginalization_index, urbanization_pct\n\n")
        for d in all_diag:
            f.write(f"Model {d['model']}\n")
            f.write(f"  R²        = {d['R²']:.4f}    R²_adj = {d['R²_adj']:.4f}\n")
            f.write(f"  F p-value = {d['F p-value']:.4g}\n")
            f.write(f"  AIC       = {d['AIC']:.2f}   BIC    = {d['BIC']:.2f}\n")
            f.write(f"  Breusch–Pagan p = {d['Breusch–Pagan p']:.4g}\n")
            f.write(f"  Shapiro–Wilk p  = {d['Shapiro–Wilk p']:.4g}\n")
            cooks_key = "n influential (Cook's > 4/n)"
            f.write(f"  influential obs = {d[cooks_key]}\n\n")

    print("\n\n=== Phase 1 complete ===")
    print(f"Results written to:  {OUT}")
    for fn in sorted(OUT.glob("phase1_*")):
        print(f"  - {fn.name}")


if __name__ == "__main__":
    main()
