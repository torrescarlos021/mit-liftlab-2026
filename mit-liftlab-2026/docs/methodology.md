# Methodology

This document details the methodology of the five analytical phases described in the [README](../README.md). It is the canonical technical reference for the project and the paper.

---

## 1. Conceptual Framework

The project tests the following causal chain through empirical work:

```
Nanostore proliferation  ──┐
                           ├──▶  Unhealthy food access for minors  ──▶  Childhood overweight/obesity
Time-scarce households   ──┤                                                   │
                           │                                                   │
Survey: lack of time   ───┘                                                    ▼
                                                                Long-term metabolic risk
                                                                           ▲
                                                                           │
       Educational intervention  ──▶  Behaviour change  ──▶  ΔBMI  ────────┘
       (PE + Vida Saludable)
```

The intervention does not attempt to alter the structural factor (lack of time) but rather to equip students with the knowledge and skills to navigate it.

---

## 2. Phase 1 — Linear Regression on Nanostore and Health Data

### 2.1 Research question
> *Does state-level nanostore density correlate with childhood overweight + obesity prevalence after controlling for marginalization?*

### 2.2 Variables

| Variable | Type | Source | Description |
|----------|------|--------|-------------|
| `obesity_prev_5_11` | Dependent | ENSANUT 2020–2024 (state-level) | % of children 5–11 with overweight + obesity |
| `obesity_prev_12_19` | Dependent | ENSANUT 2020–2024 (state-level) | % of adolescents 12–19 with overweight + obesity |
| `nanostore_density` | Independent | INEGI DENUE 2024 | Nanostores per 1,000 inhabitants |
| `marginalization_index` | Control | CONAPO 2020 | Standardized index (−2 ≈ very low, +2 ≈ very high) |
| `urbanization_pct` | Control | INEGI 2020 | % population in localities of 15,000+ inhabitants |

### 2.3 Model

```
y_i = β₀ + β₁ · nanostore_density_i
        + β₂ · marginalization_index_i
        + β₃ · urbanization_pct_i
        + ε_i
```

estimated by ordinary least squares (OLS), with `i` indexing the 32 federal entities.

### 2.4 Diagnostics

Reported in `docs/phase1_results.md`:

- R², adjusted R²
- Per-coefficient p-values and 95 % CIs
- Variance Inflation Factor (VIF) for multicollinearity
- Breusch–Pagan test for heteroskedasticity
- Cook's distance for influential observations
- Residual normality (Shapiro–Wilk)

### 2.5 Honest reporting

We report **all coefficients**, including those that lose significance under control variables, and we discuss them rather than suppressing them. Phase 1 is **descriptive**, not causal — we do not claim that nanostores *cause* obesity, only that an association exists that justifies further investigation.

---

## 3. Phase 2 — Extended Dataset Integration

### 3.1 Goal

Refine the Phase-1 model by adding behavioural and intake variables, and identify the strongest correlates of state-level obesity.

### 3.2 Additional variables

| Variable | Source | Justification |
|----------|--------|---------------|
| `pa_compliance_minors` | ENSANUT PA module 2023 | % minors meeting WHO ≥60 min/day PA recommendation |
| `fruits_veg_daily` | ENSANUT food module 2023 | Mean daily F&V portions |
| `sugary_drink_weekly` | ENSANUT food module 2023 | Mean weekly sugar-sweetened beverage consumption |
| `processed_food_spend_pct` | ENIGH 2022 | Share of food spending on processed foods |
| `t2dm_minors_incidence` | Anuarios de Morbilidad | Incidence of type-2 diabetes in minors per 100k |

### 3.3 Procedure

1. Merge state-level data on the `state_id` key.
2. Fit a hierarchy of nested models (M1: baseline → M2: + behaviour → M3: + spending → M4: + morbidity).
3. Report each model's R², AIC, BIC, and likelihood-ratio test against the previous nested model.
4. Apply stepwise regression with AIC criterion for variable selection.
5. Report the final model with all diagnostics.

### 3.4 Interpretation

The phase identifies the strongest *modifiable* predictor of state-level childhood obesity, which directly informs the design of Phase 4.

---

## 4. Phase 3 — Primary Survey Analysis

### 4.1 Sample

- **Size:** 104 valid responses
- **Region:** San Luis Potosí, Mexico
- **Collection period:** December 2025 – January 2026
- **Mode:** Online (Microsoft Forms), distributed via WhatsApp and direct contact
- **Composition:** Students (~55 %), office workers, teachers, industry, homemakers, commerce; ages from <18 to >50; ~30 % are parents.

### 4.2 Instrument

Two-track questionnaire with branching by parental status:

- **Track A (non-parents):** focus on personal habits, barriers, willingness to change.
- **Track B (parents):** focus on children's habits, parental concern, household decision-making.

### 4.3 Analysis

Implemented in `src/ml/phase3_survey_analysis.py`. Steps:

1. **Cleaning.** Strip whitespace, normalize encodings, drop empty rows.
2. **Demographic stratification.** Age groups, parental status, occupation.
3. **Frequency analysis.** Multi-select fields split on `;` and counted.
4. **Cross-tabulation.** Key bivariates (parental status × concern; occupation × time-to-cook; age × processed food frequency).
5. **Sentiment toward solutions.** Frequency count of preferred interventions.
6. **Triangulation with phases 1 & 2.** Does the survey's identification of "lack of time" align with state-level predictors?

### 4.4 Limitations

- Non-probabilistic sample.
- Self-reported behaviour subject to social desirability bias.
- Regional sample (SLP); national generalization requires caution.

The survey is **hypothesis-generating** and **triangulation-supporting**, not population-representative. We make this explicit in the paper.

---

## 5. Phase 4 — Educational Intervention Design

See `docs/curricular_proposal.md` for the full proposal. Methodologically, the design follows:

### 5.1 Theoretical anchors

- **Health Belief Model** (Rosenstock, 1974) — perceived susceptibility/severity/benefits drive behaviour change.
- **Social Cognitive Theory** (Bandura, 1986) — observational learning, self-efficacy, environmental influence.
- **Self-Determination Theory** (Deci & Ryan, 1985) — intrinsic motivation through autonomy, competence, relatedness.

### 5.2 Evidence base

The proposal draws on:

- Cochrane systematic reviews of school-based interventions to reduce BMI.
- WHO recommendations on school nutrition and physical activity.
- Comparative international programs (e.g., Daily Mile in the UK; CHIRP in Chile).
- Local context from the Nueva Escuela Mexicana (NEM) Plan 2022 and the *Vida Saludable* articulating axis.

### 5.3 Implementation pathway

The proposal explicitly maps each component to existing SEP curriculum slots, teacher training programs, and budget categories, to keep the intervention politically and operationally realistic.

---

## 6. Phase 5 — Monte-Carlo Health Impact Simulation

### 6.1 Architecture

A cohort-based Monte-Carlo simulation projects BMI trajectories under different intervention scenarios.

```
Step 0: Initialize cohort of N = 1,000 simulated students
        with BMI drawn from ENSANUT-derived distribution for 12-year-olds.

Step 1: For each simulation run r ∈ {1, …, R = 5,000}:
        a) Draw intervention effect size e_r from a Normal(μ, σ) distribution
           parameterized by the meta-analysis point estimate and CI.
        b) Project each student's BMI year by year:
              BMI_{i,t+1} = BMI_{i,t} + age_growth_t + intervention_effect_{r,t}
        c) Compute overweight + obesity prevalence at years 1, 3, 5.

Step 2: Aggregate across runs to compute:
        - Mean ΔBMI at years 1, 3, 5.
        - 5th-95th percentile bands.
        - Probability of meeting WHO targets (>5 % relative reduction).
```

### 6.2 Effect-size sources

| Component | μ (kg/m²) | σ (kg/m²) | Source |
|-----------|-----------|-----------|--------|
| Nutrition education (Silveira 2013) | −0.33 | 0.11 | [11] |
| PA alone (Cochrane) | −0.13 | 0.046 | [12] |
| PA + nutrition combined (Cochrane) | −0.17 | 0.058 | [12] |
| Adolescent health-ed BMI-z (Brown 2020) | −0.06 | 0.018 | [13] |
| Long-term null result (2021 MA) | 0.00 | 0.023 | [14] |

σ is derived from the published 95 % CI assuming Normal distribution (σ = (UB − LB) / 3.92).

### 6.3 Scenarios

| Scenario | Description |
|----------|-------------|
| `baseline` | No intervention — apply background BMI growth only |
| `central` | Effect sizes at published point estimates |
| `optimistic` | Effect sizes at upper bound of 95 % CI |
| `conservative` | Effect sizes at lower bound (closer to null) |
| `null_robustness` | Force long-term null effect to test robustness |

### 6.4 Sensitivity analysis

We sweep over:

- **Adherence rate** (50 % – 100 %): not every student fully participates.
- **Dose** (1 h, 2 h, 3 h extra per week): does more help linearly?
- **Follow-up duration** (1, 3, 5 years).

### 6.5 Outputs

- CSV of all run-level outcomes (`results/phase5_runs.csv`).
- Summary table with point estimates and CIs by scenario.
- Plots: BMI trajectory bands, prevalence at each horizon, sensitivity heatmaps.

### 6.6 Disclaimers

The simulation is **not a prediction**. It is an evidence-based projection given current literature. Real-world deployment requires pilot validation. We state this explicitly in every output.

---

## 7. Expert Validation Methodology

See `docs/validation_protocol.md` for the full protocol. Qualitative methodology summary:

- **Sample:** 5 experts, purposive sampling.
- **Instrument:** Semi-structured interview, 6–8 core questions + 2–3 role-specific.
- **Recording:** With consent, audio + notes.
- **Analysis:** Thematic coding (open → axial), looking for convergence, divergence, unexpected concerns.
- **Reporting:** Each expert quoted (with consent) or paraphrased anonymously.

---

## 8. Ethical Considerations

- Survey respondents gave informed consent; data is anonymized.
- Expert interviewees will sign a consent form before recording.
- No minors are interviewed in the present study; the intervention is *proposed* and would require IRB / ethics review before any pilot.
- All public datasets (DENUE, ENSANUT, ENIGH, CONAPO) are open and used per their license.

---

## 9. Reproducibility

- All code is open-source under MIT license.
- Random seeds are fixed (`seed = 42`) for the Monte Carlo.
- Each phase has its own script and writes outputs to `results/` for inspection.
- Dependencies pinned in `requirements.txt`.
