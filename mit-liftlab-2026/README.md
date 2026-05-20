# 🏪➡️🏫 From Nanostores to Classrooms

<div align="center">

![MIT LiftLab](https://img.shields.io/badge/MIT-LiftLab%202026-red?style=for-the-badge)
![Tec de Monterrey](https://img.shields.io/badge/Tec%20de%20Monterrey-Campus%20SLP-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A Data-Driven Proposal to Strengthen Physical Education and *Vida Saludable* in Mexican Basic Education**

[Methodology](./docs/methodology.md) · [Validation Protocol](./docs/validation_protocol.md) · [Curricular Proposal](./docs/curricular_proposal.md) · [ML Model](./src/ml)

</div>

---

## 📋 Table of Contents

- [Executive Summary](#-executive-summary)
- [The Problem](#-the-problem)
- [Analytical Pipeline](#-analytical-pipeline)
  - [Phase 1: Linear Regression on Nanostore & Health Data](#phase-1--linear-regression-on-nanostore--health-data)
  - [Phase 2: Extended Dataset Integration](#phase-2--extended-dataset-integration)
  - [Phase 3: Primary Survey Analysis](#phase-3--primary-survey-analysis-104-responses)
  - [Phase 4: Educational Intervention Design](#phase-4--educational-intervention-design)
  - [Phase 5: ML-Based Impact Simulation](#phase-5--ml-based-impact-simulation-1-3-5-years)
- [Expert Validation](#-expert-validation)
- [Data Sources](#-data-sources)
- [Installation](#-installation)
- [References](#-references)
- [Team](#-team)

---

## 🎯 Executive Summary

Mexico has one of the world's most severe childhood obesity crises. According to **ENSANUT Continua 2020–2024**, **36.6 % of school-age children (5–11 years)** and **40.1 % of adolescents (12–19 years)** live with overweight or obesity [1]. The SEP reports that **5.7 million children aged 5–11 and 10.4 million adolescents aged 12–19** are obese, and that **7 out of 10 schoolchildren and 5 out of 10 adolescents perform no physical activity at all** [2].

Mexico's **1.1 million nanostores** — the country's primary food access point in vulnerable communities — sell predominantly ultraprocessed, sugar-rich, and nutritionally poor products. This project does **not** propose to regulate nanostores. Instead, it asks a more tractable question:

> **If structural conditions force families to depend on these stores, how do we equip the next generation to make better decisions within that environment?**

Through a five-phase analytical pipeline — combining open public data, a primary survey (n = 104), expert validation, and Monte-Carlo health-impact simulation — we propose a concrete reinforcement of the **Physical Education** subject and the **Vida Saludable** articulating axis of the **Nueva Escuela Mexicana (NEM)** curriculum.

### 🏆 MIT LiftLab National Competition 2026
> Tecnológico de Monterrey, Campus San Luis Potosí

---

## 🚨 The Problem

### Childhood obesity in Mexico (ENSANUT Continua 2020–2024)

| Group | Overweight + Obesity | Source |
|-------|----------------------|--------|
| Children 0–4 years | 6.7 % | ENSANUT 2023 [3] |
| School-age children (5–11) | **36.6 %** | ENSANUT 2020–2024 [1] |
| Adolescents (12–19) | **40.1 %** | ENSANUT 2020–2024 [1] |
| Adults | ~70 % | ENSANUT 2023 [3] |
| Diabetes prevalence (adults) | ~18 % | ENSANUT 2023 [3] |

Between 2006 and 2020–2022, obesity prevalence in male schoolchildren rose by **5.8 percentage points** [4]. The trajectory is worsening, not improving.

### Why nanostores are part of the story

| Indicator | Value | Source |
|-----------|-------|--------|
| Total nanostores in Mexico | 1,100,824 | INEGI DENUE 2024 |
| Share of food retail | 31 % | Data México |
| Children/adolescents not meeting daily physical activity | 53 % | ENSANUT 2023 [5] |

### Why the school is the right intervention point

| Indicator | Value | Source |
|-----------|-------|--------|
| Current PE hours (preschool & primary) | **1 h / week** | SEP — Plan 2022 [6] |
| Current PE hours (secondary) | **2 h / week** | SEP — Plan 2022 [6] |
| Historical PE hours (pre-2010 reforms) | up to 5 h / week | Observatorio Tec [7] |
| *Vida Saludable* status | Articulating axis (not a standalone subject) | NEM / Plan 2022 [8] |

The system already names health as a curricular priority, but in practice the time, training, and content allocated are insufficient to counter the obesity trend. **Our intervention sits inside this gap.**

---

## 🔬 Analytical Pipeline

Our work follows a five-phase pipeline. Each phase builds on the previous one and feeds the next.

```
┌───────────────────────────────────────────────────────────────────────┐
│                                                                       │
│  Phase 1            Phase 2             Phase 3                       │
│  ┌──────────┐      ┌──────────┐       ┌──────────┐                    │
│  │ Linear   │ ───▶ │ Extended │  ───▶ │ Primary  │                    │
│  │Regression│      │ Datasets │       │  Survey  │                    │
│  └──────────┘      └──────────┘       └──────────┘                    │
│       │                                     │                         │
│       ▼                                     ▼                         │
│  ┌─────────────────────────────────────────────────┐                  │
│  │   Root-cause diagnosis: structural time scarcity │                  │
│  └─────────────────────────────────────────────────┘                  │
│                       │                                               │
│                       ▼                                               │
│              Phase 4               Phase 5                            │
│           ┌──────────────┐      ┌──────────────┐                      │
│           │  Curricular  │ ───▶ │  ML Impact   │                      │
│           │ Intervention │      │  Simulation  │                      │
│           └──────────────┘      └──────────────┘                      │
│                       │                                               │
│                       ▼                                               │
│              Expert Validation (n = 5)                                │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘
```

---

### Phase 1 — Linear Regression on Nanostore & Health Data

**Goal.** Establish a quantitative baseline relationship between nanostore density and population health outcomes at the state level.

**Method.** OLS linear regression with the model:

```
Obesity_prevalence(state) = β₀ + β₁ · nanostore_density(state) + β₂ · marginalization_index(state) + ε
```

**Data.**
- **Independent variable 1:** nanostores per 1,000 inhabitants, by state (INEGI DENUE 2024).
- **Independent variable 2:** marginalization index by state (CONAPO 2020).
- **Dependent variable:** child + adolescent overweight/obesity prevalence by state (ENSANUT 2020–2024 state-level estimates [9]).

**Why a regression first?**
A simple, defensible model establishes whether nanostore density correlates with obesity prevalence after controlling for socioeconomic conditions. This is the academically honest entry point — before any complex simulation, we must show the basic statistical relationship exists.

**Diagnostics reported.** R², adjusted R², p-values per coefficient, residual plots, VIF for multicollinearity, Breusch–Pagan for heteroskedasticity.

> See `src/ml/phase1_regression.py` for full implementation and `docs/phase1_results.md` for diagnostics.

---

### Phase 2 — Extended Dataset Integration

**Goal.** Enrich the Phase-1 model with behavioral and nutritional intake variables to refine the picture.

**Datasets added.**

| Dataset | Source | Variables added |
|---------|--------|-----------------|
| ENSANUT physical activity module | INSP 2023 | % minors meeting WHO PA recommendation, by state |
| ENSANUT food consumption module | INSP 2023 | Daily F&V portions; weekly sugary-drink intake |
| ENIGH 2022 | INEGI | Household spending on processed vs fresh food, by income decile |
| Anuarios de Morbilidad | Secretaría de Salud | Incidence of type-2 diabetes in minors |

**Result.** The extended model raises explanatory power and surfaces the strongest predictor of state-level obesity in minors — guiding which variables matter most for intervention design.

> **Note on honest reporting.** Some predictors in the literature lose significance once others are controlled. We report all coefficients, including non-significant ones, to avoid p-hacking.

---

### Phase 3 — Primary Survey Analysis (104 responses)

**Goal.** Test the structural hypothesis (lack of time as a root cause) and surface the population's own preferred solutions.

**Sample.** 104 respondents, San Luis Potosí region, collected December 2025 – January 2026. Mix of students, parents, office workers, teachers, industry workers, homemakers, and commerce workers; age ranges from <18 to >50.

**Key findings (full analysis in `src/ml/phase3_survey_analysis.py`).**

| Finding | What the data shows | Implication |
|---------|---------------------|-------------|
| **Lack of time is the dominant barrier** | *"No tengo tiempo debido al trabajo"* is the most common answer to "Why don't you cook?" | Structural — cannot be solved by Claude or the consumer alone |
| **Parents are concerned** | Most parents answer *"Muy preocupado"* or *"Algo preocupado"* about the impact of poor diet on their children | Latent demand for solutions exists |
| **Children buy processed food** | When parents give children money, the most common purchases are chips, sweet snacks, and sugary drinks | The nanostore-to-child pipeline is real and measurable |
| **Population requests education** | *"Programas de educación sobre nutrición"* is among the two most-requested solutions, alongside *"Mayor acceso a alimentos saludables y económicos"* | **The intervention we propose is the one the population itself names** |
| **High willingness to change** | Majority responds *"Sí"* to "Would you change your habits with more time/resources?" | Receptiveness is not the limiting factor |

**This phase justifies pivoting the project from nanostore regulation to educational reinforcement.** The population does not need permission, it needs tools.

---

### Phase 4 — Educational Intervention Design

**Goal.** Design a concrete, implementable reinforcement to the existing Physical Education subject and *Vida Saludable* articulating axis, focused on **lower-secondary** education (ages 12–15).

**Why secondary, not primary?**
- Adolescents (12–19) show **higher overweight + obesity prevalence (40.1 %)** than school-age children (36.6 %) [1].
- Secondary students have higher discretionary spending in nanostores.
- They retain habits into adulthood — interventions at this stage shape long-term trajectories [10].

**Why complement, not replace?**
Mexico already has the *Vida Saludable* articulating axis in the NEM (Plan 2022) [8] and an established PE subject. Proposing a new subject is politically and operationally unrealistic in a 3-week timeframe. **Reinforcement is faster, cheaper, and uses existing infrastructure.**

**Proposed components (detailed in `docs/curricular_proposal.md`).**

| Component | Description | Time per week |
|-----------|-------------|---------------|
| **PE expansion** | From 2 h to 3 h, with one session explicitly devoted to *active lifestyle literacy* (reading nutrition labels, planning a healthy snack on a real budget, mapping food options around the school) | +1 h |
| **Critical-environment module** | Embedded in *Vida Saludable*: students audit the nanostores around their own school, classify products, present findings | 30 min, biweekly |
| **Teacher training package** | Short asynchronous CPD course for PE and Civic Education teachers, anchored in evidence-based pedagogy | One-off, 8 h |
| **Parent-facing component** | Monthly take-home activity connecting school content to family meal decisions | — |

**Theoretical anchors.** Health Belief Model, Social Cognitive Theory, evidence from the Cochrane reviews on school-based interventions (see References).

---

### Phase 5 — ML-Based Impact Simulation (1, 3, 5 years)

**Goal.** Provide quantitative, defensible projections of the intervention's effect on student BMI and overweight prevalence over 1, 3, and 5-year horizons.

**Why Monte Carlo, not "deep" ML.**
A neural network trained on this problem would require longitudinal Mexican intervention data we don't have. **Monte Carlo simulation with parameters drawn from published meta-analyses** is the academically honest choice: every input has a citation, every output reports uncertainty.

**Model architecture.**

```
INPUTS                                  PROCESS                          OUTPUTS
┌─────────────────────────┐           ┌────────────────────┐         ┌─────────────────────┐
│ Baseline BMI distribution│           │  Monte Carlo       │         │ ΔBMI at 1, 3, 5 yr  │
│  (ENSANUT, state-level) │           │  Simulation         │         │ Overweight prevalence│
│                          │   ───▶   │  N = 5,000 runs    │  ───▶   │ Risk-cohort shifts   │
│ Effect-size distributions│           │  per scenario      │         │ Confidence bands     │
│  (meta-analyses, Cochrane)│           │                    │         │  (5th – 95th %ile)   │
│                          │           │  Sensitivity      │         │                      │
│ Intervention parameters  │           │   analysis        │         │                      │
└─────────────────────────┘           └────────────────────┘         └─────────────────────┘
```

**Effect-size parameters drawn from published meta-analyses.**

| Component | Effect on BMI | 95 % CI | Source |
|-----------|---------------|---------|--------|
| Nutrition education alone (RCTs) | **−0.33 kg/m²** | (−0.55, −0.11) | Silveira et al., 2013 [11] |
| Physical activity alone | −0.13 kg/m² | (−0.22, −0.04) | Cochrane systematic review [12] |
| PA + nutrition combined | **−0.17 kg/m²** | (−0.29, −0.06) | Cochrane [12] |
| Health education in adolescents (10–19) — BMI z-score | −0.06 | (−0.10, −0.03) | Meta-analysis 2020 [13] |

**Honest reporting of limitations.** A 2021 meta-analysis of *long-term* PA + nutrition interventions in children 6–12 found **no significant pooled effect** (SMD ≈ 0.00) [14]. We include this null result explicitly in our scenario set — failing to do so would be cherry-picking.

**Scenarios simulated.**

| Scenario | Description |
|----------|-------------|
| Baseline | No intervention — extrapolated obesity trend |
| Optimistic | All effect sizes drawn from the upper bound of published 95 % CIs |
| Central | All effect sizes drawn from published point estimates |
| Conservative | Effect sizes drawn from null/lower-bound studies |
| Sensitivity | Parameter sweeps over adherence, dose, follow-up duration |

> See `src/ml/phase5_health_simulation.py` for implementation. Outputs are exported as CSV with confidence bands and rendered as charts in the web dashboard.

---

## 🧪 Expert Validation

The intervention proposal is validated through five semi-structured interviews. Validators were selected to triangulate **research perspective**, **school leadership**, **classroom practice**, and **student voice**.

| # | Validator | Role | Perspective |
|---|-----------|------|-------------|
| 1 | Dr. José Manuel Olais Govea | Researcher, Tec de Monterrey Campus SLP | Educational research |
| 2 | Dr. Leopoldo Zúñiga Silva | Researcher, Tec de Monterrey Campus SLP | Educational research |
| 3 | Director, Secundaria Técnica 78 (Matehuala, SLP) | School principal | Institutional implementation |
| 4 | Secondary-school teacher with active fitness practice | Classroom practitioner | Day-to-day feasibility |
| 5 | Undergraduate Education student with fitness background | Emerging educator + youth voice | Implementation realism |

**Protocol.** All five interviewees answer a standardized core of 6–8 questions, plus 2–3 role-specific questions. Responses are coded for convergence, divergence, and unexpected concerns. Full protocol, codebook, and reporting template in `docs/validation_protocol.md`.

---

## 📁 Data Sources

| Dataset | Source | Records | Phase used |
|---------|--------|---------|------------|
| **DENUE 2024** | INEGI | 1,100,824 nanostores | 1, 2 |
| **ENSANUT Continua 2020–2024** | INSP | National | 1, 2, 5 |
| **ENIGH 2022** | INEGI | National | 2 |
| **CONAPO 2020** | CONAPO | 2,469 municipalities | 1, 2 |
| **Anuarios de Morbilidad** | Secretaría de Salud | Annual | 2 |
| **SEP Plan de Estudios 2022** | SEP | Curricular | 4 |
| **Eating Habits Survey (own)** | Team — SLP, Dec 2025 | 104 responses | 3 |
| **Expert interviews (own)** | Team — May–June 2026 | 5 interviews | 4 |

---

## 🚀 Installation

### Prerequisites

- Python 3.10+
- Git

### Quick Start

```bash
# Clone repository
git clone https://github.com/healthy-nanostore/mit-liftlab-2026.git
cd mit-liftlab-2026

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Phase 1: Linear regression
python src/ml/phase1_regression.py

# Phase 3: Survey analysis
python src/ml/phase3_survey_analysis.py src/data/survey_responses.csv

# Phase 5: Health impact Monte Carlo
python src/ml/phase5_health_simulation.py --scenarios all --years 5 --runs 5000
```

---

## 📚 References

[1] Shamah-Levy T. et al. *Prevalencia nacional y estatal de sobrepeso y obesidad en escolares y adolescentes en México y factores asociados.* Salud Pública de México, 2025. https://saludpublica.mx/index.php/spm/article/view/17311

[2] Secretaría de Educación Pública. *Lineamientos y acciones de Vida Saludable en las escuelas*, 2025. https://educacionmediasuperior.sep.gob.mx

[3] ENSANUT Continua 2023. Instituto Nacional de Salud Pública.

[4] Shamah-Levy T. et al. *Prevalencias de sobrepeso y obesidad en población escolar y adolescente de México. Ensanut Continua 2020–2022.* Salud Pública de México, 65 (Suppl 1), 2023. https://pubmed.ncbi.nlm.nih.gov/38060970/

[5] Mexico Social. *Obesidad infantil en México: Un análisis de la ENSANUT Continua 2023*, 2024.

[6] SEP. *Plan de Estudio para la Educación Preescolar, Primaria y Secundaria 2022.*

[7] Observatorio del Instituto para el Futuro de la Educación, Tec de Monterrey. *La SEP retomará enfoque en educación física*, 2019.

[8] Nueva Escuela Mexicana — Eje articulador *Vida Saludable*. https://nuevaescuelamexicana.sep.gob.mx

[9] Instituto Nacional de Salud Pública. *ENSANUT Continua — Reportes estatales 2020–2024.*

[10] Singh AS et al. *Tracking of childhood overweight into adulthood: a systematic review of the literature.* Obesity Reviews, 2008.

[11] Silveira JAC et al. *The effect of participation in school-based nutrition education interventions on body mass index: a meta-analysis of randomized controlled community trials.* Preventive Medicine, 2013. https://pubmed.ncbi.nlm.nih.gov/23370048/

[12] Cochrane systematic review. *Systematic review and meta-analysis of school-based interventions to reduce body mass index.* https://www.ncbi.nlm.nih.gov/books/NBK114253/

[13] Brown EC et al. *A systematic review and meta-analysis of school-based interventions with health education to reduce body mass index in adolescents aged 10 to 19 years.* BMC Public Health, 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7784329/

[14] *Long-Term Dietary and Physical Activity Interventions in the School Setting and Their Effects on BMI in Children Aged 6–12: Meta-Analysis of RCTs.* 2021. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8066711/

---

## 👥 Team

<table>
<tr>
<td align="center">
<b>Fernanda Ita</b><br>
<sub>Literature & Educational Research</sub><br>
<sub>Systematic review · Curricular framework · Interview coding</sub>
</td>
<td align="center">
<b>Alexis Marcos</b><br>
<sub>Field Research & Validation</sub><br>
<sub>Survey design · Expert interviews · Qualitative synthesis</sub>
</td>
<td align="center">
<b>Carlos Torres</b><br>
<sub>Quantitative Modeling & Platform</sub><br>
<sub>Regression · Monte Carlo · Web dashboard</sub>
</td>
</tr>
</table>

**Institution:** Tecnológico de Monterrey, Campus San Luis Potosí
**Program:** Mechatronics Engineering — 4th semester
**Course:** MIT LiftLab — National Competition 2026

---

## 📄 License

MIT License — see [LICENSE](LICENSE).

---

<div align="center">

**From data to classrooms — evidence-based interventions for Mexican childhood health.**

MIT LiftLab National Competition 2026

</div>
