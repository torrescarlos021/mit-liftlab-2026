"""
ACT 1 — The Regression That Didn't Work
=======================================
MIT LiftLab 2026 · ¿Qué factores impiden la compra de productos saludables
en las nanostores de México?

THE STORY
---------
We started where any analyst starts: with a linear regression. The intuition
was simple — if we know a shopper's demographics and budget, we should be able
to predict how much they spend, and from there reason about healthy purchasing.

It didn't work. The linear model explains almost nothing (R² ≈ 0.03). That is
not a failure of effort; it is the first real finding: shopper behaviour in
nanostores is NOT a simple linear function of who you are. Something more
structural is going on — which is exactly what pushed us to Act 2.

Inputs:
    data/shopper_clean_v2.csv

Outputs:
    results/act1_regression_summary.txt
    results/act1_correlations.png
    results/act1_predicted_vs_actual.png

Usage:
    python src/act1_linear_regression.py
"""
from __future__ import annotations
from pathlib import Path
import sys

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

import statsmodels.api as sm
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import r2_score

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "shopper_clean_v2.csv"
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True, parents=True)

sns.set_style("whitegrid")
plt.rcParams.update({"figure.dpi": 110, "savefig.dpi": 140, "font.size": 10})


def main():
    if not DATA.exists():
        sys.exit(f"ERROR: missing {DATA}")

    df = pd.read_csv(DATA)
    df.columns = [c.lstrip("\ufeff").strip() for c in df.columns]
    print(f"=== ACT 1 — Linear Regression ===")
    print(f"Loaded {len(df)} shopper records\n")

    # Target: total amount spent (continuous, the natural first target)
    target = "total_spent_numeric"
    cat = ["age_group", "sex", "purchase_frequency"]
    num = ["household_size", "monthly_food_budget", "purchase_freq_monthly"]

    d = df[[target] + cat + num].copy()
    for c in num:
        d[c] = pd.to_numeric(d[c], errors="coerce")
    d = d.dropna(subset=[target])
    d[num] = d[num].fillna(d[num].median())
    d[cat] = d[cat].fillna("Missing")
    print(f"Usable rows: {len(d)}")

    X, y = d[cat + num], d[target]

    pre = ColumnTransformer(
        [("cat", OneHotEncoder(handle_unknown="ignore"), cat)],
        remainder="passthrough",
    )
    pipe = Pipeline([("pre", pre), ("lr", LinearRegression())])

    # Cross-validated R²
    cv = cross_val_score(pipe, X, y, cv=5, scoring="r2")
    print(f"\nLinear regression → predict total_spent")
    print(f"  R² per fold: {np.round(cv, 3)}")
    print(f"  Mean CV R²:  {cv.mean():.3f}   <-- this is the point: it's basically noise")

    # Single split for the diagnostic plot
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    pipe.fit(Xtr, ytr)
    pred = pipe.predict(Xte)
    r2_test = r2_score(yte, pred)

    # Correlation heatmap of numeric features
    numeric = d[[target] + num].copy()
    fig, ax = plt.subplots(figsize=(7, 5.5))
    sns.heatmap(numeric.corr(), annot=True, fmt=".2f", cmap="RdBu_r", center=0,
                cbar_kws={"label": "Pearson r"}, ax=ax)
    ax.set_title("Act 1 — Weak linear correlations with spending", fontweight="bold")
    plt.tight_layout()
    plt.savefig(OUT / "act1_correlations.png", bbox_inches="tight")
    plt.close()

    # Predicted vs actual
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.scatter(yte, pred, alpha=0.4, edgecolors="k", color="#b8332a", s=40)
    lim = [min(yte.min(), pred.min()), max(yte.max(), pred.max())]
    ax.plot(lim, lim, "k--", linewidth=1, label="Perfect prediction")
    ax.set_xlabel("Actual spend (MXN)")
    ax.set_ylabel("Predicted spend (MXN)")
    ax.set_title(f"Act 1 — Linear model fails to predict spending\nTest R² = {r2_test:.3f}",
                 fontweight="bold")
    ax.legend()
    plt.tight_layout()
    plt.savefig(OUT / "act1_predicted_vs_actual.png", bbox_inches="tight")
    plt.close()

    # OLS summary for the report (statsmodels, with dummies)
    X_ols = pd.get_dummies(d[cat + num], columns=cat, drop_first=True).astype(float)
    X_ols = sm.add_constant(X_ols)
    model = sm.OLS(y.values, X_ols.values).fit()

    with open(OUT / "act1_regression_summary.txt", "w") as f:
        f.write("ACT 1 — LINEAR REGRESSION: THE MODEL THAT DIDN'T WORK\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Target: total_spent_numeric (MXN per visit)\n")
        f.write(f"Predictors: {cat + num}\n")
        f.write(f"Usable rows: {len(d)}\n\n")
        f.write(f"Cross-validated R² (5-fold): {cv.mean():.4f}\n")
        f.write(f"Test R²:                     {r2_test:.4f}\n\n")
        f.write("INTERPRETATION\n")
        f.write("-" * 60 + "\n")
        f.write("An R² this close to zero means demographics and budget do NOT\n")
        f.write("linearly explain how much a shopper spends — and by extension,\n")
        f.write("they don't explain WHAT shoppers buy either. The behaviour is\n")
        f.write("not individual-linear; it is structural. This is the finding\n")
        f.write("that motivated Act 2: stop predicting the person, start\n")
        f.write("characterizing the system.\n\n")
        f.write("OLS detail (statsmodels):\n")
        f.write(str(model.summary()))

    print(f"\n=== Act 1 complete ===")
    print(f"  Mean CV R² = {cv.mean():.3f}  →  the regression does not work (as expected)")
    print(f"  Outputs in {OUT}/")
    for fn in sorted(OUT.glob("act1_*")):
        print(f"   - {fn.name}")


if __name__ == "__main__":
    main()
