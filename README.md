# 🏪 De las tienditas a las aulas

<div align="center">

![MIT LiftLab](https://img.shields.io/badge/MIT-LiftLab%202026-red?style=for-the-badge)
![Tec de Monterrey](https://img.shields.io/badge/Tec%20de%20Monterrey-Campus%20SLP-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=for-the-badge&logo=python)

**¿Qué factores impiden la compra de productos saludables en las nanostores de México?**

*Una investigación en cuatro actos — del dato crudo a la solución.*

</div>

---

## 📖 La historia en cuatro actos

Este proyecto no empezó con una respuesta. Empezó con una pregunta del MIT LiftLab — *¿qué hace que la gente no compre productos saludables en las tienditas?* — y un dataset nacional de más de 3,000 registros de campo. Lo que sigue es el camino real que recorrimos: incluyendo el modelo que **no** funcionó, porque ese fracaso fue justo lo que nos llevó a la respuesta correcta.

> **Acto 1** → Intentamos lo obvio (regresión lineal). No funcionó.
> **Acto 2** → Cambiamos de pregunta y usamos ML. Encontramos el insight real.
> **Acto 3** → Salimos a campo con nuestra propia encuesta. Confirmamos la causa.
> **Acto 4** → Diseñamos la solución y proyectamos su impacto con Monte Carlo.

---

## 🎬 Acto 1 — La regresión que no funcionó

**Lo que intentamos.** Como cualquier analista, empezamos con una regresión lineal. La intuición: si conocemos la demografía y el presupuesto de un comprador, deberíamos poder predecir cuánto gasta — y de ahí razonar sobre su consumo saludable.

**Lo que pasó.**

```
Regresión lineal → predecir gasto del comprador (total_spent)
R² promedio (validación cruzada 5-fold) = 0.032
```

Un R² de **0.03** significa que el modelo no explica prácticamente nada. La demografía y el presupuesto **no** predicen el comportamiento de compra de forma lineal.

**Por qué importa.** Esto no fue un fracaso de esfuerzo — fue el primer hallazgo real: *el comportamiento del comprador en las nanostores no es una función lineal simple de quién eres*. Algo más estructural está pasando. Ese descubrimiento nos empujó al Acto 2.

> 📄 Código: [`src/act1_linear_regression.py`](src/act1_linear_regression.py)

---

## 🎬 Acto 2 — El ML y el insight real

**Cambiamos la pregunta.** En vez de *"¿cuánto gasta esta persona?"*, preguntamos:
1. ¿Qué se compra realmente en las nanostores?
2. ¿Puede el ML predecir quién compra saludable? (y si no, ¿por qué no?)
3. ¿Cómo se ve el sistema completo — compradores, tenderos, cadena de suministro?

**Insight 1 — Los productos no saludables dominan el changarro.**

| Métrica | Valor |
|---------|-------|
| Compradores que llevan ≥1 producto no saludable | **60.8 %** |
| Compradores que llevan **solo** no saludable (nada sano) | **50.3 %** |
| Compradores que llevan ≥1 producto saludable | 23.7 % |

Las bebidas azucaradas y los snacks salados encabezan la lista; frutas y verduras quedan al fondo.

**Insight 2 — La paradoja intención–acción.** Aquí está el corazón del proyecto:

| Los compradores… | % |
|------------------|---|
| **Saben** que lo no saludable les hace daño | 85.3 % |
| **Dirían** que comprarían más saludable | 62.8 % |
| **Quieren** más opciones saludables disponibles | 64.6 % |
| **Perciben** lo saludable como más caro | **65.8 %** |
| Pero realmente **compraron** algo saludable | 23.7 % |

La gente **no es ignorante y no es desinteresada**. Sabe, querría y pide opciones — pero compra lo no saludable. La barrera dominante que declaran es la **percepción de precio**.

**Insight 3 — Ni el ML predice bien la compra saludable.**

```
Random Forest → predecir compra saludable
ROC-AUC ≈ 0.55  (apenas mejor que el azar)
```

Esto *también* es un hallazgo: la compra saludable **no** se explica por *quién* es el comprador. Está condicionada por factores estructurales (precio, disponibilidad), no por rasgos individuales.

**Insight 4 — La cadena de suministro empuja lo no saludable.**

| En la última milla… | % |
|----------------------|---|
| Entregas que **NO** ofrecieron productos saludables a la tienda | **66 %** |

El problema no empieza en el mostrador — empieza en lo que llega al changarro.

**Síntesis.** La barrera a la compra saludable en las nanostores mexicanas es **estructural y conductual, no informativa**. Por eso una intervención **educativa orientada al futuro** — que construya los hábitos y la conciencia de precio de la próxima generación de compradores — es el punto de palanca que probamos en el Acto 4.

> 📄 Código: [`src/act2_ml_insights.py`](src/act2_ml_insights.py) · Insights: [`results/act2_insights.md`](results/act2_insights.md)

---

## 🎬 Acto 3 — Nuestra propia encuesta (triangulación)

Un dataset es un solo lente. Para validar, levantamos **nuestra propia encuesta**: 104 respuestas en San Luis Potosí (dic 2025 – ene 2026), una muestra independiente.

**Convergió con el Acto 2:**

- La causa raíz vuelve a ser **estructural**: *"No tengo tiempo debido al trabajo"* es la razón más citada para no cocinar.
- Las **3 soluciones más pedidas** por los propios encuestados:
  1. Mayor acceso a alimentos saludables y económicos
  2. Menos horas de trabajo
  3. **Programas de educación sobre nutrición** ← la intervención que diseñamos
- **80 de 94** dirían que sí cambiarían sus hábitos con más tiempo o recursos.
- De los padres encuestados, la gran mayoría está *"muy"* o *"algo preocupada"* por la dieta de sus hijos.

La población **nombra ella misma** la educación nutricional como solución. Esa convergencia entre el dataset nacional del MIT y nuestra encuesta de campo es lo que nos dio la confianza para diseñar el Acto 4.

> 📄 Código: [`src/act3_own_survey.py`](src/act3_own_survey.py) · Resumen: [`results/act3_summary.md`](results/act3_summary.md)

---

## 🎬 Acto 4 — La solución + simulación Monte Carlo

**La lógica del puente.** Los datos son de consumo adulto. Pero si el problema es la brecha entre lo que la gente *sabe/quiere* y lo que *hace*, la palanca de mayor impacto a largo plazo es **formar a los compradores del futuro**: los adolescentes de hoy.

**La propuesta.** Reforzar la materia de **Educación Física** y el eje articulador **Vida Saludable** de la Nueva Escuela Mexicana (Plan 2022) en secundaria (12–15 años). No es una materia nueva — es reforzar lo que el currículo ya nombra pero no equipa. Cuatro componentes: hora extra de EF con *alfabetización de estilo de vida activo*, módulo de auditoría del entorno (las propias tienditas alrededor de la escuela), capacitación docente, y puente familiar.

> 📄 Propuesta completa: [`docs/curricular_proposal.md`](docs/curricular_proposal.md)

**La proyección.** Simulamos el impacto sobre el IMC de una cohorte de 1,000 estudiantes, 5,000 corridas por escenario, con tamaños de efecto tomados de meta-análisis publicados (Silveira 2013, Cochrane, Brown 2020, Hodder 2021).

| Escenario | Obesidad año 5 | vs. sin intervención |
|-----------|----------------|----------------------|
| Sin intervención (baseline) | 31.9 % | — |
| Conservador | 29.8 % | −2.1 pp |
| **Central** | **26.2 %** | **−5.7 pp** |
| Optimista | 22.7 % | −9.2 pp |
| Robustez nula (Hodder 2021) | 32.0 % | ≈ 0 |

**Honestidad epistémica.** Incluimos explícitamente el escenario de **resultado nulo** a largo plazo, junto con los positivos. No hacer esto sería seleccionar datos a conveniencia — y un evaluador del MIT lo detectaría.

> 📄 Código: [`src/act4_montecarlo_intervention.py`](src/act4_montecarlo_intervention.py) · Resultados: [`results/act4_summary.md`](results/act4_summary.md)

---

## 📁 Estructura del repositorio

```
mit-liftlab-nanostores/
├── README.md                        ← este documento (hilo narrativo)
├── data/
│   ├── nanostore_clean_v2.csv       ← censo de tienditas (MIT, n=221)
│   ├── shopper_clean_v2.csv         ← compradores (MIT, n=1,135)
│   ├── shopkeeper_clean_v2.csv      ← tenderos (MIT, n=236)
│   ├── lastmile_clean_v2.csv        ← entregas / cadena de suministro (MIT, n=1,448)
│   ├── own_survey_104.csv           ← nuestra encuesta propia (n=104)
│   └── literature_parameters.json   ← parámetros del Monte Carlo
├── src/
│   ├── act1_linear_regression.py    ← Acto 1: la regresión que no salió
│   ├── act2_ml_insights.py          ← Acto 2: ML + los 4 insights
│   ├── act3_own_survey.py           ← Acto 3: encuesta propia
│   └── act4_montecarlo_intervention.py ← Acto 4: simulación de impacto
├── docs/
│   ├── methodology.md               ← metodología técnica
│   ├── curricular_proposal.md       ← propuesta de intervención
│   ├── findings.md                  ← resumen ejecutivo de hallazgos
│   └── references.bib               ← bibliografía
├── web/
│   └── index.html                   ← dashboard interactivo del proyecto
├── results/                         ← gráficas y tablas (se generan al correr)
├── requirements.txt
└── LICENSE
```

---

## 🚀 Cómo reproducirlo

```bash
pip install -r requirements.txt

python src/act1_linear_regression.py        # Acto 1 — la regresión falla (R²=0.03)
python src/act2_ml_insights.py              # Acto 2 — insights + gráficas
python src/act3_own_survey.py               # Acto 3 — encuesta propia
python src/act4_montecarlo_intervention.py  # Acto 4 — Monte Carlo

# Dashboard: abrir web/index.html en el navegador
```

Todos los resultados (gráficas, tablas, resúmenes) se escriben en `results/`.

---

## 📚 Datos y fuentes

| Dataset | Origen | Registros |
|---------|--------|-----------|
| nanostore / shopper / shopkeeper / lastmile | MIT LiftLab 2026 (estudio nacional, ~13 campus) | 3,040 |
| Encuesta propia | Equipo, San Luis Potosí | 104 |
| Tamaños de efecto (Monte Carlo) | Meta-análisis publicados | ver `docs/references.bib` |
| Contexto epidemiológico | ENSANUT Continua 2020–2024 (INSP) | — |

---

## 👥 Equipo

**Fernanda Ita** · investigación educativa y marco curricular
**Alexis Marcos** · trabajo de campo y encuesta propia
**Carlos Torres** · modelado cuantitativo y plataforma

Tecnológico de Monterrey · Campus San Luis Potosí · Ingeniería en Mecatrónica
**MIT LiftLab — Competencia Nacional 2026**

---

## 📄 Licencia

MIT License — ver [LICENSE](LICENSE).

<div align="center">

*Del dato crudo a la solución — investigación basada en evidencia para la salud alimentaria en México.*

</div>
