# Guión — Versión Español · 15 minutos
## "De las Tienditas a las Aulas" · MIT LiftLab 2026

> **Equipo:** Fernanda Ita [F] · Alexis Marcos [A] · Carlos Torres [C]
> **Objetivo:** máximo 15 minutos + preguntas
> **Tono:** conversacional, honesto, contar la historia real

---

## SLIDE 1 — TÍTULO · 40 seg · [F]

> "MIT nos lanzó una pregunta: ¿qué impide que la gente compre productos saludables en las tienditas de México?
>
> Esta es nuestra respuesta en cuatro actos. Y empezamos por el fracaso — porque ese fracaso fue lo que nos llevó a la respuesta correcta."

---

## SLIDE 2 — EL DATASET · 1 min · [C]

> "El MIT nos dio acceso a 3,040 registros de campo reales: compradores entrevistados en el momento de la compra, tenderos, repartidores de última milla.
>
> Además de eso, nosotros salimos a campo con nuestra propia encuesta — 104 respuestas en San Luis Potosí.
>
> Esta no es la historia de 'usamos datos y encontramos la respuesta'. Es la historia de cómo los datos nos sorprendieron dos veces."

---

## SLIDE 3 — ACTO 01: LA REGRESIÓN · 1:30 min · [C]

> "Empezamos donde empieza cualquier analista: con una regresión lineal. Si conocemos la demografía y el presupuesto del comprador, deberíamos poder predecir su comportamiento de compra.
>
> El resultado: R² de **0.032**. El modelo no explica prácticamente nada.
>
> Pero eso no fue un error — fue nuestro **primer hallazgo real**: el comportamiento de compra en las tienditas no depende de quién eres. Algo más estructural está pasando. Y eso fue lo que nos llevó al Acto 2."

---

## SLIDE 4 — ACTO 02: LOS NÚMEROS · 1:30 min · [C]

> "Cambiamos la pregunta. En vez de cuánto gasta alguien, preguntamos qué se compra y cómo se ve el sistema completo.
>
> Cuatro números que detienen:
>
> **60.8%** lleva al menos un producto no saludable.
>
> **50.3%** — la mitad exacta — lleva *solo* productos no saludables. Nada sano.
>
> Solo **23.7%** lleva algo saludable.
>
> Y **66%** de las entregas de última milla ni siquiera ofrecieron productos sanos a la tienda. El problema no empieza en el mostrador — empieza en lo que llega al changarro."

---

## SLIDE 5 — EL CORAZÓN DEL HALLAZGO · 2 min · [C]

> "Pero el número que realmente cambia el diagnóstico está aquí.
>
> **85%** sabe que lo que compra le hace daño. **63%** dice que compraría más sano si pudiera. **65%** pide más opciones.
>
> Pero solo el **24%** realmente compra algo sano."

*[Pausa de 2 segundos.]*

> "Eso es una brecha de **39 puntos** entre lo que la gente quiere hacer y lo que hace.
>
> Aplicamos además un Random Forest — inteligencia artificial más avanzada — para ver si podíamos predecir quién compra sano. AUC de **0.55**. Apenas mejor que lanzar una moneda.
>
> La conclusión: la compra saludable no depende de quién eres. El problema es estructural — precio, disponibilidad, lo que llega a la tienda."

---

## SLIDE 6 — ACTO 03: NUESTRA ENCUESTA · 1:30 min · [A]

> "Para validar, salimos a campo con una muestra independiente: 104 encuestas en San Luis Potosí.
>
> La razón más citada para no cocinar: falta de tiempo por el trabajo.
>
> Y cuando preguntamos qué soluciones querían..."

*[Pausa.]*

> "Los propios encuestados nombraron la educación nutricional entre las tres primeras.
>
> **80 de 94 dijeron que sí cambiarían sus hábitos** con más tiempo o recursos.
>
> El dataset del MIT y nuestra encuesta de campo — dos fuentes completamente independientes — nos dieron exactamente la misma respuesta."

---

## SLIDE 7 — EL PUENTE · 1 min · [F]

> "Nuestros datos son de adultos. Nuestra intervención apunta a adolescentes. Somos honestos con ese salto.
>
> El puente es este: si la gente ya sabe y ya quiere, pero el sistema no le da las condiciones, entonces la palanca de mayor impacto es **formar a los compradores del futuro**.
>
> ¿Por qué secundaria? Porque a los 12–15 años ya manejan dinero propio, visitan tienditas solos, y los hábitos que se forman ahí se consolidan para toda la vida.
>
> No regulamos las tienditas. Educamos a quienes las visitarán toda su vida."

---

## SLIDE 8 — ACTO 04: LA PROPUESTA · 1:30 min · [F]

> "Cuatro componentes, todos dentro de lo que el currículo de la Nueva Escuela Mexicana ya nombra — sin crear una materia nueva:
>
> **A** — Una hora extra de EF para alfabetización de estilo de vida activo: leer etiquetas, planear un snack sano con presupuesto real.
>
> **B** — Un módulo de auditoría: los estudiantes salen a mapear las tienditas alrededor de su propia escuela.
>
> **C** — Capacitación docente. Sin profesores preparados, nada funciona.
>
> **D** — Un puente familiar mensual que respeta el tiempo de familias que ya dijeron que su principal problema es el tiempo.
>
> Costo estimado: **9,500 pesos por escuela por año**. Escalado al país: menos del 0.05% del presupuesto educativo federal."

---

## SLIDE 9 — MONTE CARLO · 1:30 min · [C]

> "Para proyectar el impacto usamos una simulación Monte Carlo: 1,000 estudiantes, **5,000 corridas por escenario**, con tamaños de efecto de meta-análisis publicados.
>
> El escenario central — el más probable según la literatura — proyecta que la obesidad en la cohorte baja de **31.9% a 26.2% a 5 años**. Menos 5.7 puntos porcentuales.
>
> Y aquí el escenario de **resultado nulo**, donde la intervención no tiene efecto duradero. Lo incluimos intencionalmente — porque si lo escondiéramos, dejaríamos de ser honestos."

---

## SLIDE 10 — HONESTIDAD · 45 seg · [C]

> "Separamos explícitamente lo que sabemos, lo que asumimos, y lo que no sabemos todavía.
>
> La honestidad sobre las limitaciones no debilita la propuesta. La hace creíble."

---

## SLIDE 11 — EXPERTOS · 2 min (incluyendo videos) · [A]

> "Llevamos la propuesta a cinco expertos con perspectivas completamente distintas: investigadores del Tec, el director de una secundaria técnica en Matehuala, un docente de EF, y un estudiante de educación.
>
> Entrevistas independientes. Los mismos temas emergiendo sin que se coordinaran entre ellos."

*[Reproducir clips de video.]*

---

## SLIDE 12 — CIERRE · 45 seg · [F]

> "MIT preguntó: ¿qué impide la compra saludable en las tienditas?
>
> No es ignorancia. No es falta de voluntad. El sistema está diseñado para empujar lo no saludable — y la gente no tiene las condiciones para actuar sobre lo que ya sabe y ya quiere.
>
> La solución más efectiva a largo plazo no está en regular las tienditas."

*[Pausa.]*

> "Está en las aulas.
>
> Muchas gracias."

---

## CONTROL DE TIEMPO

| Slide | Quién | Tiempo | Acumulado |
|-------|-------|--------|-----------|
| 1 Título | F | 0:40 | 0:40 |
| 2 Dataset | C | 1:00 | 1:40 |
| 3 Acto 01 | C | 1:30 | 3:10 |
| 4 Acto 02 stats | C | 1:30 | 4:40 |
| 5 Corazón | C | 2:00 | 6:40 |
| 6 Acto 03 | A | 1:30 | 8:10 |
| 7 Puente | F | 1:00 | 9:10 |
| 8 Propuesta | F | 1:30 | 10:40 |
| 9 Monte Carlo | C | 1:30 | 12:10 |
| 10 Honestidad | C | 0:45 | 12:55 |
| 11 Expertos | A | 2:00 | 14:55 |
| 12 Cierre | F | 0:45 | **15:40** |

> Si van cortos de tiempo: comprimir slides 10 y 11 a 1 minuto combinado → llegan a **14:30**.

---

## LAS 5 FRASES QUE NO SE OLVIDAN

1. *"R² de 0.032 no es un fracaso — es el primer hallazgo."* **(Carlos)**
2. *"85% sabe, 63% querría, solo 24% compra. Brecha de 39 puntos."* **(Carlos)**
3. *"Los propios encuestados nombraron la intervención que íbamos a diseñar."* **(Alexis)**
4. *"No regulamos las tienditas. Educamos a quienes las visitarán toda su vida."* **(Fernanda)**
5. *"La honestidad sobre las limitaciones no debilita la propuesta — la hace creíble."* **(Carlos)**
