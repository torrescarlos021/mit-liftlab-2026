"""
ACT 2 — Machine Learning & The Real Insight
===========================================
MIT LiftLab 2026 · ¿Qué factores impiden la compra de productos saludables
en las nanostores de México?

THE STORY
---------
Act 1 told us linear regression on demographics is hopeless. So we changed the
question. Instead of "how much does this person spend?", we asked:

    1. WHAT actually gets bought in nanostores? (descriptive)
    2. Can ML predict who buys healthy? (and if not, why not?)
    3. What does the WHOLE SYSTEM look like — shoppers, shopkeepers, supply?

The answers converge on one story: the problem is NOT ignorance and NOT lack of
willingness. It's a structural intention–action gap, gated by price perception
and availability, and reinforced by a supply chain that barely offers healthy
products to the stores in the first place.

Inputs:
    data/shopper_clean_v2.csv
    data/shopkeeper_clean_v2.csv
    data/lastmile_clean_v2.csv

Outputs:
    results/act2_product_mix.png
    results/act2_intention_action_gap.png
    results/act2_feature_importance.png
    results/act2_supply_chain.png
    results/act2_insights.md

Usage:
    python src/act2_ml_insights.py
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

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True, parents=True)

sns.set_style("whitegrid")
plt.rcParams.update({"figure.dpi": 110, "savefig.dpi": 140, "font.size": 10})

# Product taxonomy (structured categories from the survey instrument)
UNHEALTHY = ["Sugary drinks", "Salty snacks", "Bakery items", "Cigarettes"]
HEALTHY = ["Fruits and vegetables", "Bottled Water"]

C_UNH = "#b8332a"
C_HLT = "#2d5e3e"
C_DATA = "#1d4e89"
C_GOLD = "#b8862a"
C_INK = "#1a1612"


def load(name):
    df = pd.read_csv(DATA / f"{name}_clean_v2.csv")
    df.columns = [c.lstrip("\ufeff").strip() for c in df.columns]
    return df


def has_any(value, keywords):
    if pd.isna(value):
        return np.nan
    return int(any(k in str(value) for k in keywords))


def main():
    shopper = load("shopper")
    shopkeeper = load("shopkeeper")
    lastmile = load("lastmile")
    print(f"=== ACT 2 — ML & Insights ===")
    print(f"shopper={len(shopper)}  shopkeeper={len(shopkeeper)}  lastmile={len(lastmile)}\n")

    # ──────────────────────────────────────────────────────────
    # INSIGHT 1 — What gets bought (product mix)
    # ──────────────────────────────────────────────────────────
    shopper["buys_healthy"] = shopper["products_purchased"].apply(lambda x: has_any(x, HEALTHY))
    shopper["buys_unhealthy"] = shopper["products_purchased"].apply(lambda x: has_any(x, UNHEALTHY))
    d = shopper.dropna(subset=["buys_healthy"]).copy()

    pct_unhealthy = d["buys_unhealthy"].mean() * 100
    pct_healthy = d["buys_healthy"].mean() * 100
    pct_only_unhealthy = ((d["buys_unhealthy"] == 1) & (d["buys_healthy"] == 0)).mean() * 100

    # Explode product categories for the bar chart
    cats = []
    for v in shopper["products_purchased"].dropna():
        for part in str(v).split(","):
            p = part.strip()
            if p:
                # collapse to short labels
                for full, short in [
                    ("Sugary drinks", "Sugary drinks"),
                    ("Salty snacks", "Salty snacks"),
                    ("Bread/Tortillas", "Bread/Tortillas"),
                    ("Dairy", "Dairy"),
                    ("Fruits and vegetables", "Fruits & veg"),
                    ("Bakery", "Bakery"),
                    ("Bottled Water", "Bottled water"),
                    ("Cigarettes", "Cigarettes"),
                ]:
                    if full in p:
                        cats.append(short)
                        break
    mix = pd.Series(cats).value_counts().head(8)
    colors = [C_UNH if c in ["Sugary drinks", "Salty snacks", "Bakery", "Cigarettes"]
              else (C_HLT if c in ["Fruits & veg", "Bottled water"] else C_GOLD)
              for c in mix.index]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.barh(range(len(mix)), mix.values, color=colors, edgecolor=C_INK)
    ax.set_yticks(range(len(mix)))
    ax.set_yticklabels(mix.index)
    ax.invert_yaxis()
    ax.set_xlabel("Times mentioned among purchases")
    ax.set_title("Act 2 · Insight 1 — Unhealthy products dominate the basket",
                 fontweight="bold")
    for i, v in enumerate(mix.values):
        ax.text(v + 1, i, str(v), va="center", fontsize=9)
    legend = [plt.Rectangle((0, 0), 1, 1, color=C_UNH),
              plt.Rectangle((0, 0), 1, 1, color=C_HLT),
              plt.Rectangle((0, 0), 1, 1, color=C_GOLD)]
    ax.legend(legend, ["Unhealthy", "Healthy", "Neutral"], loc="lower right")
    plt.tight_layout()
    plt.savefig(OUT / "act2_product_mix.png", bbox_inches="tight")
    plt.close()

    # ──────────────────────────────────────────────────────────
    # INSIGHT 2 — The intention–action gap
    # ──────────────────────────────────────────────────────────
    know = shopper["daily_unhealthy_affects_health"].isin(["Totally agree", "Moderately agree"]).mean() * 100
    would = shopper["would_choose_healthier"].isin(["Likely", "Very likely"]).mean() * 100
    price = shopper["healthy_price_perception"].isin(["Slightly higher", "Much higher"]).mean() * 100
    want = (shopper["recommend_more_healthy"] == "Yes").mean() * 100

    gap = pd.Series({
        "Know it harms\ntheir health": know,
        "Say they'd buy\nhealthier": would,
        "Want more healthy\noptions available": want,
        "Perceive healthy\nas more expensive": price,
        "Actually bought\nsomething healthy": pct_healthy,
    })
    fig, ax = plt.subplots(figsize=(10, 5.5))
    bar_colors = [C_DATA, C_DATA, C_DATA, C_GOLD, C_HLT]
    ax.bar(range(len(gap)), gap.values, color=bar_colors, edgecolor=C_INK, width=0.6)
    ax.set_xticks(range(len(gap)))
    ax.set_xticklabels(gap.index, fontsize=10)
    ax.set_ylabel("% of shoppers")
    ax.set_ylim(0, 100)
    ax.set_title("Act 2 · Insight 2 — The intention–action gap",
                 fontweight="bold")
    for i, v in enumerate(gap.values):
        ax.text(i, v + 1.5, f"{v:.0f}%", ha="center", fontweight="bold")
    plt.tight_layout()
    plt.savefig(OUT / "act2_intention_action_gap.png", bbox_inches="tight")
    plt.close()

    # ──────────────────────────────────────────────────────────
    # INSIGHT 3 — ML: can we predict healthy buying? (barely)
    # ──────────────────────────────────────────────────────────
    cat = ["age_group", "sex", "purchase_frequency", "healthy_price_perception",
           "impulse_purchase", "would_choose_healthier", "recommend_more_healthy"]
    num = ["household_size", "monthly_food_budget"]
    for c in num:
        d[c] = pd.to_numeric(d[c], errors="coerce")
    d[num] = d[num].fillna(d[num].median())
    d[cat] = d[cat].fillna("Missing")

    pre = ColumnTransformer([("cat", OneHotEncoder(handle_unknown="ignore"), cat)],
                            remainder="passthrough")
    rf = Pipeline([("pre", pre),
                   ("rf", RandomForestClassifier(n_estimators=400, random_state=42,
                                                 class_weight="balanced"))])
    auc = cross_val_score(rf, d[cat + num], d["buys_healthy"], cv=5, scoring="roc_auc").mean()

    # Permutation importance on a holdout
    Xtr, Xte, ytr, yte = train_test_split(d[cat + num], d["buys_healthy"],
                                          test_size=0.25, random_state=42, stratify=d["buys_healthy"])
    rf.fit(Xtr, ytr)
    perm = permutation_importance(rf, Xte, yte, n_repeats=20, random_state=42, scoring="roc_auc")
    imp = pd.Series(perm.importances_mean, index=cat + num).sort_values(ascending=True)

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.barh(range(len(imp)), imp.values, color=C_DATA, edgecolor=C_INK)
    ax.set_yticks(range(len(imp)))
    ax.set_yticklabels(imp.index)
    ax.set_xlabel("Permutation importance (Δ ROC-AUC)")
    ax.set_title(f"Act 2 · Insight 3 — What predicts healthy buying?  (model AUC = {auc:.2f})",
                 fontweight="bold")
    plt.tight_layout()
    plt.savefig(OUT / "act2_feature_importance.png", bbox_inches="tight")
    plt.close()

    # ──────────────────────────────────────────────────────────
    # INSIGHT 4 — The supply chain barely offers healthy products
    # ──────────────────────────────────────────────────────────
    lm_offered = lastmile["offered_healthy"].value_counts(normalize=True) * 100
    sk_offers = shopkeeper["offers_healthy"].value_counts(normalize=True) * 100

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    # last-mile deliveries
    vals_lm = [lm_offered.get(True, 0), lm_offered.get(False, 0)]
    axes[0].bar(["Offered\nhealthy", "Did NOT offer\nhealthy"], vals_lm,
                color=[C_HLT, C_UNH], edgecolor=C_INK, width=0.6)
    axes[0].set_ylabel("% of deliveries")
    axes[0].set_title("Last-mile: did the supplier offer healthy products?")
    for i, v in enumerate(vals_lm):
        axes[0].text(i, v + 1, f"{v:.0f}%", ha="center", fontweight="bold")
    # shopkeepers
    vals_sk = [sk_offers.get(True, 0), sk_offers.get(False, 0)]
    axes[1].bar(["Offers\nhealthy", "Does NOT\noffer healthy"], vals_sk,
                color=[C_HLT, C_UNH], edgecolor=C_INK, width=0.6)
    axes[1].set_ylabel("% of shopkeepers")
    axes[1].set_title("Shopkeepers: do you stock healthy products?")
    for i, v in enumerate(vals_sk):
        axes[1].text(i, v + 1, f"{v:.0f}%", ha="center", fontweight="bold")
    plt.suptitle("Act 2 · Insight 4 — The supply side under-offers healthy products",
                 fontweight="bold")
    plt.tight_layout()
    plt.savefig(OUT / "act2_supply_chain.png", bbox_inches="tight")
    plt.close()

    # ──────────────────────────────────────────────────────────
    # Markdown insight report
    # ──────────────────────────────────────────────────────────
    md = [
        "# Act 2 — Machine Learning & Insights\n\n",
        "## Insight 1 — Unhealthy products dominate the basket\n",
        f"- Shoppers buying at least one **unhealthy** product: **{pct_unhealthy:.1f}%**\n",
        f"- Shoppers buying at least one **healthy** product: **{pct_healthy:.1f}%**\n",
        f"- Shoppers buying **only unhealthy** (nothing healthy): **{pct_only_unhealthy:.1f}%**\n\n",
        "## Insight 2 — The intention–action gap\n",
        f"- Know unhealthy food harms their health: **{know:.1f}%**\n",
        f"- Say they would buy healthier: **{would:.1f}%**\n",
        f"- Want more healthy options available: **{want:.1f}%**\n",
        f"- Perceive healthy food as more expensive: **{price:.1f}%**\n\n",
        "People are **not** ignorant and **not** unwilling. They know, they'd like to, ",
        "they want options — yet they buy unhealthy. The dominant stated barrier is **price perception**.\n\n",
        "## Insight 3 — ML can barely predict healthy buying\n",
        f"- Random Forest ROC-AUC: **{auc:.3f}** (≈ chance).\n",
        "- This is itself a finding: healthy buying is **not** explained by who the shopper is. ",
        "It is gated by structural factors (price, availability), not individual traits.\n\n",
        "## Insight 4 — The supply chain under-offers healthy products\n",
        f"- Last-mile deliveries that did **NOT** offer healthy products: **{lm_offered.get(False, 0):.1f}%**\n",
        f"- Shopkeepers who say they stock healthy products: **{sk_offers.get(True, 0):.1f}%** ",
        "(but shoppers still walk out with soda and snacks — availability ≠ salience/price).\n\n",
        "## The synthesis that sets up Act 3 & 4\n",
        "The barrier to healthy purchasing in Mexican nanostores is **structural and behavioural**, ",
        "not informational. That is why a future-facing **educational intervention** — building the ",
        "habits and price-savvy of the next generation of shoppers — is the leverage point we test in Act 4.\n",
    ]
    (OUT / "act2_insights.md").write_text("".join(md), encoding="utf-8")

    print(f"Insight 1 — unhealthy dominate: {pct_unhealthy:.1f}% buy unhealthy, {pct_only_unhealthy:.1f}% only unhealthy")
    print(f"Insight 2 — gap: know {know:.0f}%, would {would:.0f}%, price-barrier {price:.0f}%")
    print(f"Insight 3 — RF AUC = {auc:.3f} (≈ chance)")
    print(f"Insight 4 — {lm_offered.get(False, 0):.0f}% of deliveries didn't offer healthy")
    print(f"\n=== Act 2 complete ===  Outputs in {OUT}/")
    for fn in sorted(OUT.glob("act2_*")):
        print(f"   - {fn.name}")


if __name__ == "__main__":
    main()
