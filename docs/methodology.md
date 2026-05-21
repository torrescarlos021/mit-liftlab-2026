# Metodología

Documento técnico de los cuatro actos del proyecto. Referencia canónica para la presentación y el reporte.

---

## Marco general

La pregunta del MIT LiftLab es: *¿qué factores impiden la compra de productos saludables en las nanostores de México?* Nuestro abordaje es secuencial y honesto: cada acto pone a prueba el supuesto sobre el que descansa el anterior.

```
Acto 1 (regresión)  →  "no es lineal-individual"
        ↓
Acto 2 (ML + sistema)  →  "es estructural: precio, disponibilidad, brecha intención-acción"
        ↓
Acto 3 (encuesta propia)  →  "se confirma en muestra independiente; piden educación"
        ↓
Acto 4 (intervención + Monte Carlo)  →  "educar a los compradores del futuro"
```

---

## Acto 1 — Regresión lineal

**Objetivo.** Establecer un punto de partida cuantitativo: ¿puede un modelo lineal predecir el gasto del comprador a partir de variables observables?

**Datos.** `shopper_clean_v2.csv` (n = 1,135).

**Variable objetivo.** `total_spent_numeric` (gasto por visita, MXN).

**Predictores.** `age_group`, `sex`, `purchase_frequency` (categóricas, one-hot) + `household_size`, `monthly_food_budget`, `purchase_freq_monthly` (numéricas).

**Modelo.** OLS / regresión lineal con validación cruzada de 5 folds.

**Resultado.** R² promedio ≈ 0.032. El modelo no explica el comportamiento.

**Diagnósticos.** Se reporta R² por fold, R² de test, mapa de correlaciones y gráfica predicho-vs-real. Se incluye el resumen OLS de `statsmodels` con coeficientes y p-valores.

**Interpretación honesta.** Un R² cercano a cero no es un error: es evidencia de que el fenómeno no es lineal-individual. Esto motiva el cambio de enfoque del Acto 2.

---

## Acto 2 — Machine Learning e insights

**Objetivo.** Caracterizar el sistema en lugar de predecir al individuo.

**Datos.** `shopper`, `shopkeeper`, `lastmile`.

**Taxonomía de productos.** Categorías estructuradas del instrumento:
- No saludables: Sugary drinks, Salty snacks, Bakery items, Cigarettes.
- Saludables: Fruits and vegetables, Bottled Water.
- Neutrales: Bread/Tortillas, Dairy.

Se usa la columna estructurada `products_purchased` (no el texto libre `healthy_products_bought`, que está demasiado ruidoso para ser confiable).

**Insight 1 — Mezcla de productos.** Frecuencia de cada categoría comprada; % que compra no saludable / saludable / solo no saludable.

**Insight 2 — Brecha intención-acción.** Tabulación de cuatro actitudes (`daily_unhealthy_affects_health`, `would_choose_healthier`, `recommend_more_healthy`, `healthy_price_perception`) contra la compra real.

**Insight 3 — Clasificación.** Random Forest (400 árboles, `class_weight='balanced'`) para predecir compra saludable, evaluado con ROC-AUC en validación cruzada de 5 folds. Importancia de variables por permutación sobre un holdout estratificado.

**Insight 4 — Cadena de suministro.** Proporción de entregas de última milla (`offered_healthy`) y de tenderos (`offers_healthy`) que ofrecen / surten productos saludables.

**Hallazgo central.** La barrera es estructural y conductual, no informativa. Ni la regresión (Acto 1) ni el RF (AUC ≈ 0.55) predicen la compra por rasgos individuales.

---

## Acto 3 — Encuesta propia

**Objetivo.** Triangular el hallazgo del Acto 2 con una muestra independiente.

**Datos.** `own_survey_104.csv` (n = 104; San Luis Potosí; dic 2025 – ene 2026; delimitador `;`).

**Análisis.** Limpieza y normalización de texto; conteo de frecuencias (incluyendo multi-respuesta separada por `;`/`,`); cruces clave (estatus parental × preocupación); identificación de soluciones más solicitadas.

**Limitaciones.** Muestra no probabilística, regional, autoreportada. Es un instrumento de *triangulación* y *generación de hipótesis*, no representativo a nivel nacional. Se declara explícitamente.

**Convergencia.** Causa estructural (tiempo/costo), alta disposición al cambio, y demanda explícita de educación nutricional — coherente con el Acto 2.

---

## Acto 4 — Intervención y Monte Carlo

**Objetivo.** Proyectar el impacto de la intervención educativa sobre el IMC de una cohorte de adolescentes a 1, 3 y 5 años.

**Por qué Monte Carlo y no "deep ML".** No tenemos datos longitudinales de intervención en México. La simulación Monte Carlo con parámetros de meta-análisis publicados es la opción honesta: cada input tiene cita, cada output reporta incertidumbre.

**Arquitectura.**
1. Cohorte de 1,000 estudiantes con IMC inicial ~ Normal(μ, σ) de ENSANUT.
2. Para cada una de 5,000 corridas por escenario: se muestrea un tamaño de efecto de Normal(μ, σ), con σ derivada del IC95% (σ = (LS − LI)/3.92).
3. Se proyecta el IMC año a año = IMC + crecimiento_anual + efecto·adherencia·dosis.
4. Se calcula prevalencia de sobrepeso/obesidad a los años 1, 3, 5.

**Tamaños de efecto.**

| Componente | μ (kg/m²) | IC 95% | Fuente |
|---|---|---|---|
| Educación nutricional | −0.33 | (−0.55, −0.11) | Silveira 2013 |
| Actividad física sola | −0.13 | (−0.22, −0.04) | Cochrane |
| AF + nutrición combinada | −0.17 | (−0.29, −0.06) | Cochrane |
| Salud en adolescentes (BMI-z) | −0.06 | (−0.10, −0.03) | Brown 2020 |
| Resultado nulo a largo plazo | 0.00 | (−0.05, 0.04) | Hodder 2021 |

**Escenarios.** baseline, central, optimista (cota baja del IC = mayor reducción), conservador (cota alta = menor reducción), robustez nula.

**Análisis de sensibilidad.** Barrido sobre adherencia (50–100 %) y dosis (0.5–3 h/semana) en el escenario central.

**Disclaimer.** Es una *proyección*, no una *predicción*. Cualquier despliegue requiere validación piloto.

---

## Reproducibilidad

- Código abierto bajo licencia MIT.
- Semilla fija (`seed = 42`) en el Monte Carlo.
- Cada acto es un script independiente que escribe a `results/`.
- Dependencias fijadas en `requirements.txt`.

## Consideraciones éticas

- Los datos del MIT y la encuesta propia están anonimizados.
- No se entrevistó a menores; la intervención es *propuesta* y requeriría revisión ética antes de cualquier piloto.
- Los datasets se usan conforme a los términos del MIT LiftLab.
