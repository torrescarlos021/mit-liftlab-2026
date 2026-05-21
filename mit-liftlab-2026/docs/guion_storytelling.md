# Guión de Presentación — MIT LiftLab 2026
## "De las Tienditas a las Aulas"
### Storytelling en Cuatro Actos

> **Equipo:** Fernanda Ita (F) · Alexis Marcos (A) · Carlos Torres (C)
> **Tiempo estimado:** 18–22 minutos
> **Formato:** Storytelling conversacional — no leer el texto, usarlo como guía narrativa

---

## INSTRUCCIONES DE USO

- Las líneas marcadas `[F]`, `[C]`, `[A]` indican quién habla.
- Los `[corchetes]` son instrucciones de escena, no se dicen en voz alta.
- Las cifras clave están en **negrita** — asegúrate de pronunciarlas con pausa antes y después.
- El tono es el de alguien contando *su historia real*, no recitando datos. Usa "nosotros", "encontramos", "nos sorprendió".

---

## SLIDE 1 — TÍTULO
**[F] abre, de pie, sin mirar la pantalla:**

> "MIT nos lanzó una pregunta: ¿qué impide que la gente compre productos saludables en las tienditas de México? Hoy les traemos nuestra respuesta. Pero antes de la respuesta, les vamos a contar el camino. Porque el camino incluye un modelo que no funcionó — y ese fracaso fue justo lo que nos llevó a la respuesta correcta."

*[Pausa de 2 segundos. Voltear hacia la pantalla solo al pasar a la siguiente slide.]*

---

## SLIDE 2 — EL DATASET
**[C] toma la palabra:**

> "El MIT nos dio acceso a un dataset de campo como pocas veces ves en un proyecto universitario: **3,040 registros reales** levantados en nanostores de toda la república. Compradores entrevistados en el momento de la compra. Tenderos. Repartidores de última milla."

> "Cuatro lentes distintos del mismo sistema: **221 tienditas, 1,135 compradores, 236 tenderos, 1,448 entregas de distribución**."

*[Señalar cada número mientras aparece.]*

> "Y además de ese dataset, nosotros mismos salimos a campo en San Luis Potosí con nuestra propia encuesta de **104 respuestas**. Por qué hicimos eso lo explica Alexis más adelante."

> "Esta no es la historia de 'usamos datos y encontramos la respuesta'. Es la historia de *cómo los datos nos sorprendieron dos veces*."

---

## SLIDE 3 — ACTO 01: LA REGRESIÓN QUE NO FUNCIONÓ
**[C] continúa — tono honesto, casi confesional:**

> "Empezamos como empieza cualquier analista. Con una regresión lineal."

> "La lógica era simple: si conocemos la demografía del comprador, su presupuesto mensual, con qué frecuencia va a la tiendita — deberíamos poder predecir cuánto gasta. Y de ahí razonar sobre su consumo saludable."

*[Señalar la gráfica de R² por fold.]*

> "El resultado: un **R² promedio de 0.032**. Cero punto cero tres dos. El modelo no explica prácticamente nada."

*[Pausa deliberada.]*

> "Ahora bien — esto no fue un fracaso de esfuerzo. Fue el **primer hallazgo real**: el comportamiento de compra en las tienditas *no es una función lineal simple de quién eres*. Algo más estructural está pasando. Y eso fue lo que nos empujó al Acto 2."

---

## SLIDE 4 — ACTO 02: EL INSERT REAL (STATS)
**[C] continúa:**

> "Cambiamos la pregunta. En vez de *'¿cuánto gasta esta persona?'*, preguntamos: ¿qué se compra realmente? ¿Puede el ML predecir quién compra sano? ¿Y cómo se ve el sistema completo?"

> "Los números que aparecen aquí son los que más nos detuvieron cuando los vimos por primera vez."

*[Señalar el strip de estadísticas, una por una, con pausa entre cada una.]*

> "**60.8%** de los compradores lleva al menos un producto no saludable en su canasta."

> "**50.3%** — la mitad exacta — lleva *solo* productos no saludables. Nada sano."

> "Y apenas **23.7%** lleva algo saludable."

> "Eso en el lado del comprador. Del lado de la distribución: **66% de las entregas de última milla no ofrecieron ni un producto saludable a la tienda**."

> "El problema no empieza en el mostrador. Empieza en lo que llega al changarro."

---

## SLIDE 5 — EL CORAZÓN DEL HALLAZGO
**[C] — este es el momento más importante de la presentación. Hablar despacio:**

> "Pero la cifra que realmente cambia el diagnóstico está aquí."

*[Señalar el callout oscuro.]*

> "**85%** de los compradores sabe que lo que consume diariamente le hace daño. **63%** dice que compraría más sano si pudiera. **65%** pide más opciones saludables disponibles."

*[Pausa.]*

> "Pero solo el **24%** realmente compra algo sano."

> "Eso es una brecha de **39.1 puntos porcentuales** entre lo que la gente *dice que querría hacer* y lo que *realmente hace*."

> "La barrera más citada: perciben que lo saludable es más caro."

> "Y cuando aplicamos un **Random Forest** para ver si podíamos predecir quién compra sano a partir de sus características — género, edad, frecuencia de visita — el modelo dio un **AUC de 0.55**. Apenas mejor que lanzar una moneda."

> "Ese resultado también es un hallazgo: la compra saludable no se predice por quién eres. El problema no está en las personas — está en las condiciones que las rodean. Es estructural."

---

## SLIDE 6 — ACTO 03: NUESTRA ENCUESTA
**[A] toma la palabra — tono de campo, cercano:**

> "Un solo dataset, por grande que sea, es un solo lente. Así que nosotros salimos a campo."

> "En diciembre de 2025 y enero de 2026 levantamos **104 encuestas en San Luis Potosí** — una muestra completamente independiente del dataset del MIT. No anclar con los datos que ya teníamos era el punto."

> "La pregunta principal que más nos importaba: ¿por qué no cocinas con frecuencia?"

> "Respuesta más citada: **'No tengo tiempo por el trabajo'**."

> "¿Y qué soluciones pedían? Las tres más votadas fueron: acceso a alimentos sanos y económicos, menos horas de trabajo..."

*[Pausa dramática antes de la tercera.]*

> "...y **programas de educación sobre nutrición**."

> "Los propios encuestados *nombraron la intervención que nosotros íbamos a diseñar*."

> "Y más: **80 de 94 dijeron que sí cambiarían sus hábitos** si tuvieran más tiempo o más recursos."

> "Esto es clave: la gente no es resistente al cambio. Solo necesita condiciones."

> "Y cuando esto convergió con lo que el dataset nacional del MIT nos decía, nos dio la confianza para diseñar el Acto 4."

---

## SLIDE 7 — EL PUENTE LÓGICO
**[F] retoma:**

> "Antes de la solución, tenemos que ser honestos sobre algo."

> "Nuestros datos son de **adultos**. El gasto, las actitudes, la brecha intención-acción — todo medido en personas que hoy ya van a las tienditas."

> "Nuestra intervención apunta a **adolescentes**. Hay un salto generacional ahí, y no lo vamos a esconder."

> "El puente es este: el ecosistema actual empuja el consumo no saludable, y la gente no logra cerrar la brecha entre lo que sabe y lo que hace. Si ese es el problema — entonces la palanca de mayor impacto a largo plazo es *formar a los compradores del futuro*. Los adolescentes de hoy llegan al mostrador dentro de 3 o 4 años."

> "¿Por qué secundaria específicamente? Porque la prevalencia de obesidad en adolescentes de **12 a 15 años ya es del 40.1%** — más alta que en niños menores. Porque ya manejan dinero propio y visitan tienditas solos. Y porque los hábitos que se forman en esa edad se consolidan hacia la adultez."

> "No vamos a regular las tienditas. Vamos a educar a quienes las visitarán toda su vida."

---

## SLIDE 8 — ACTO 04: LA SOLUCIÓN
**[F] continúa:**

> "La propuesta es reforzar la materia de **Educación Física** y el eje articulador **Vida Saludable** de la Nueva Escuela Mexicana — que ya existe en el currículo, pero hoy no tiene el contenido ni el tiempo suficientes para lo que los datos nos piden."

> "Cuatro componentes:"

*[Señalar cada uno en el slide.]*

> "**A**: Una hora extra de EF por semana — no para sumar ejercicio genérico, sino para *alfabetizar en estilo de vida activo*: leer etiquetas, planear un snack sano con un presupuesto real, entender las decisiones que están tomando."

> "**B**: Un módulo de entorno crítico cada dos semanas. Los estudiantes salen a auditar las tienditas *alrededor de su propia escuela*. Cuentan productos, documentan precios sano vs no sano, presentan sus hallazgos. La escuela se convierte en laboratorio."

> "**C**: Capacitación docente. Un paquete asincrónico de 8 horas más un taller opcional. Sin docentes preparados, nada de esto llega al aula."

> "**D**: Un puente familiar. Una actividad mensual — una conversación guiada, una receta económica — pensada para no sumar carga a familias que ya declararon que su problema principal es el tiempo."

> "Costo estimado: **9,500 pesos por escuela por año**. Escalado a las 35,000 secundarias del país, eso es **330 millones de pesos anuales — menos del 0.05% del presupuesto federal educativo**."

---

## SLIDE 9 — MONTE CARLO
**[C] retoma:**

> "Antes de diseñar la solución, Carlos modeló su impacto. ¿Por qué Monte Carlo y no un modelo predictivo más 'sofisticado'?"

> "Porque no tenemos datos longitudinales de intervención en México. Y pretender que los tenemos sería deshonesto. Lo que sí tenemos son **cinco meta-análisis publicados** con tamaños de efecto y intervalos de confianza. El Monte Carlo con parámetros de literatura es la opción rigurosa: cada input tiene cita, cada output reporta incertidumbre."

> "**1,000 estudiantes simulados. 5,000 corridas por escenario.**"

*[Señalar la gráfica y la tabla.]*

> "Sin intervención, la obesidad en la cohorte sube de **31.9% a más de 36%** a cinco años — solo por el crecimiento natural del IMC."

> "En el **escenario central** — usando el efecto publicado de la Cochrane para actividad física combinada con nutrición — la cohorte termina en **26.2%. Una reducción de 5.7 puntos porcentuales**."

> "El optimista llega a 22.7%. El conservador a 29.8%."

> "Y aquí, el escenario de **resultado nulo** — basado en Hodder 2021, que encontró que las intervenciones escolares a largo plazo a veces no tienen efecto duradero. Lo incluimos porque si lo escondiéramos, un evaluador del MIT lo buscaría. Y tendría razón."

> "La simulación no es una predicción. Es una proyección honesta de lo que la literatura nos dice que es posible."

---

## SLIDE 10 — HONESTIDAD EPISTÉMICA
**[C] brevemente:**

> "En el MIT aprecian el rigor intelectual. Por eso hemos organizado explícitamente lo que sabemos, lo que asumimos, y lo que no sabemos."

*[Señalar las tres columnas — verde, dorado, rojo.]*

> "Lo que sabemos: la barrera es estructural, confirmada en dos datasets independientes. Los modelos lineales y el ML fallan igual — no es un problema individual. 66% de la distribución no llega con opciones sanas."

> "Lo que asumimos: que los efectos de la literatura son trasladables a México, que la adherencia docente será del 80%, que una hora extra a la semana es la dosis mínima efectiva."

> "Lo que no sabemos: si los efectos se mantienen más de 5 años, cómo escala a 35,000 escuelas, qué pasa con la fidelidad docente real."

> "La honestidad sobre las limitaciones no debilita la propuesta. La hace creíble."

---

## SLIDE 11 — EXPERTOS
**[A] cierra esta sección:**

> "Para no quedarnos solo con nuestros propios datos, llevamos la propuesta a **cinco expertos** con perspectivas radicalmente distintas: dos investigadores del Tec de Monterrey, el director de una secundaria técnica en Matehuala, un docente de EF que es practicante fitness, y un estudiante de educación que conoce tanto la teoría como la vida de un adolescente de hoy."

> "Cada uno fue entrevistado de forma independiente, con las mismas 8 preguntas core, más preguntas específicas a su perfil. Sus respuestas se codificaron buscando convergencia y divergencia."

*[Reproducir los videos uno por uno, con breve introducción de cada uno.]*

---

## SLIDE 12 — CIERRE
**[F] cierra, de pie, mirando a la audiencia:**

> "La pregunta del MIT fue: ¿qué impide la compra saludable en las nanostores?"

*[Pausa.]*

> "La respuesta no es lo que la mayoría esperaba. No es ignorancia. No es falta de voluntad. Es que el **sistema está diseñado para empujar lo no saludable** — desde la cadena de distribución hasta el mostrador — y la gente no tiene las condiciones para actuar sobre lo que ya sabe y ya quiere."

> "La solución más efectiva a largo plazo no está en regular las tienditas. Está en las aulas."

> "Formando a los compradores del futuro. Dándoles las herramientas para cerrar esa brecha de **39 puntos** entre lo que saben y lo que hacen, antes de que lleguen al mostrador por primera vez con dinero en el bolsillo."

*[Pausa final.]*

> "Muchas gracias."

---

## NOTAS DE TIEMPO ESTIMADO

| Slide | Quién | Tiempo |
|-------|-------|--------|
| 1 — Título | F | 45 seg |
| 2 — Dataset | C | 1:30 min |
| 3 — Acto 01 | C | 1:30 min |
| 4 — Stats | C | 1:30 min |
| 5 — Callout (corazón) | C | 2:00 min |
| 6 — Acto 03 | A | 2:00 min |
| 7 — Puente | F | 1:30 min |
| 8 — Propuesta | F | 2:30 min |
| 9 — Monte Carlo | C | 2:00 min |
| 10 — Honestidad | C | 1:00 min |
| 11 — Expertos | A | ~3:00 min (incl. videos) |
| 12 — Cierre | F | 1:00 min |
| **Total** | | **~20 min** |

---

## FRASES CLAVE QUE DEBEN MEMORIZAR

Estas 5 frases son el núcleo emocional de la presentación. Si nada más se recuerda, que sea esto:

1. **"R² de 0.032 no es un error — es el primer hallazgo real."** (Carlos, Slide 3)
2. **"85% sabe, 63% querría, pero solo 24% compra. Brecha de 39 puntos."** (Carlos, Slide 5)
3. **"Los propios encuestados nombraron la intervención que íbamos a diseñar."** (Alexis, Slide 6)
4. **"No vamos a regular las tienditas. Vamos a educar a quienes las visitarán toda su vida."** (Fernanda, Slide 7)
5. **"La honestidad sobre las limitaciones no debilita la propuesta — la hace creíble."** (Carlos, Slide 10)

---

---

# Presentation Script — MIT LiftLab 2026
## "From Nanostores to Classrooms"
### Four-Act Storytelling Script (English)

> **Team:** Fernanda Ita (F) · Alexis Marcos (A) · Carlos Torres (C)
> **Estimated time:** 18–22 minutes

---

## SLIDE 1 — TITLE
**[F] opens, standing, without looking at the screen:**

> "MIT gave us a question: what keeps people from buying healthy products in Mexico's nanostores? Today we bring you our answer. But before the answer, we're going to tell you the path. Because that path includes a model that failed — and that failure was exactly what led us to the right answer."

---

## SLIDE 2 — THE DATASET
**[C]:**

> "MIT gave us access to a field dataset you rarely see in an undergraduate project: **3,040 real records** collected at nanostores across the country. Shoppers interviewed at the moment of purchase. Store owners. Last-mile delivery workers."

> "Four different lenses on the same system: **221 nanostores, 1,135 shoppers, 236 shopkeepers, 1,448 last-mile deliveries**."

> "And on top of that, we ran our own field survey in San Luis Potosí — **104 responses**. Why we did that, Alexis will explain."

> "This is not the story of 'we used data and found the answer.' It's the story of *how the data surprised us twice*."

---

## SLIDE 3 — ACT 01: THE REGRESSION THAT FAILED
**[C] — honest, almost confessional tone:**

> "We started where every analyst starts. With a linear regression."

> "The logic was simple: if we know a shopper's demographics and budget, we should be able to predict how much they spend — and from there reason about healthy purchasing."

> "The result: a mean **R² of 0.032**. The model explains almost nothing."

*[Deliberate pause.]*

> "This wasn't a failure of effort. It was the **first real finding**: shopper behavior in nanostores is not a simple linear function of who you are. Something more structural is going on. And that's what pushed us to Act 2."

---

## SLIDE 4 — ACT 02: THE REAL INSIGHT (STATS)
**[C]:**

> "We changed the question. Instead of *'how much does this person spend?'*, we asked: what actually gets bought? Can ML predict who buys healthy? And how does the whole system look?"

> "**60.8%** of shoppers pick up at least one unhealthy item."

> "**50.3%** — exactly half — pick up *only* unhealthy products. Nothing healthy at all."

> "And just **23.7%** pick up anything healthy."

> "On the supply side: **66% of last-mile deliveries offered no healthy products to the store**."

> "The problem doesn't start at the counter. It starts with what arrives at the store."

---

## SLIDE 5 — THE HEART OF THE FINDING
**[C] — speak slowly, this is the presentation's pivotal moment:**

> "But the number that truly changes the diagnosis is here."

> "**85%** of shoppers know that what they buy daily is bad for them. **63%** say they would buy healthier if they could. **65%** want more healthy options available."

*[Pause.]*

> "But only **24%** actually buy anything healthy."

> "That's a gap of **39.1 percentage points** between what people *say they want to do* and what they *actually do*."

> "The most cited barrier: they perceive healthy options as more expensive."

> "And when we applied a **Random Forest** to predict who buys healthy from personal characteristics — the model gave an **AUC of 0.55**. Barely better than a coin flip."

> "That result is also a finding: healthy purchasing is not predicted by who you are. The problem is not the people — it's the conditions around them. It's structural."

---

## SLIDE 6 — ACT 03: OUR OWN SURVEY
**[A] — field tone, close and direct:**

> "A single dataset, however large, is a single lens. So we went to the field."

> "In December 2025 and January 2026 we collected **104 surveys in San Luis Potosí** — a completely independent sample. The point was *not* to anchor on the MIT data we already had."

> "The top reason people gave for not cooking at home: **'I don't have time because of work.'**"

> "And what solutions did they ask for? The top three: access to affordable healthy food, fewer working hours..."

*[Dramatic pause.]*

> "...and **nutrition education programs**."

> "Our own respondents *named the exact intervention we were going to design*."

> "And **80 out of 94 said they would change their habits** if they had more time or resources."

> "This is key: people are not resistant to change. They just need the conditions."

---

## SLIDE 7 — THE LOGICAL BRIDGE
**[F]:**

> "Before the solution, we have to be honest about something."

> "Our data is about **adults**. Every measurement — spending, attitudes, the intention-action gap — was made on people who already visit nanostores today."

> "Our intervention targets **adolescents**. There is a generational leap there, and we are not going to hide it."

> "The bridge is this: the current ecosystem pushes unhealthy consumption, and people can't close the gap between what they know and what they do. If that's the problem — then the highest-leverage long-term solution is to *form the next generation of shoppers* before they reach the counter."

> "Why secondary school specifically? Because obesity prevalence in **12 to 15 year-olds is already 40.1%** — higher than in younger children. Because they already handle their own money and visit nanostores independently. And because the habits formed at that age consolidate into adult life."

> "We are not going to regulate the nanostores. We are going to educate those who will visit them for the rest of their lives."

---

## SLIDE 8 — ACT 04: THE SOLUTION
**[F]:**

> "The proposal is to strengthen **Physical Education** and the **Healthy Living** axis of Mexico's National Curriculum — which already exists, but today doesn't have enough content or time for what the data is asking of it."

> "Four components: an extra hour of PE focused on active lifestyle literacy; a bi-weekly critical environment module where students audit the nanostores around their own school; teacher training; and a family bridge activity that respects the time constraints our data showed are real."

> "Estimated cost: **9,500 pesos per school per year. Scaled to Mexico's 35,000 secondary schools, that's 330 million pesos — less than 0.05% of the federal education budget.**"

---

## SLIDE 9 — MONTE CARLO
**[C]:**

> "Why Monte Carlo and not a more 'sophisticated' predictive model? Because we don't have longitudinal intervention data from Mexico. And pretending we do would be dishonest. What we do have are **five published meta-analyses** with effect sizes and confidence intervals. The Monte Carlo is the rigorous choice: every input has a citation, every output reports uncertainty."

> "**1,000 simulated students. 5,000 runs per scenario.**"

> "In the **central scenario** — using the Cochrane-published effect for combined PA and nutrition — the cohort ends at **26.2%. A reduction of 5.7 percentage points** versus no intervention."

> "And here, the **null-result scenario** — based on Hodder 2021. We include it because if we hid it, an MIT evaluator would look for it. And they would be right to."

> "This simulation is not a prediction. It's an honest projection of what the literature says is possible."

---

## SLIDE 10 — EPISTEMIC HONESTY
**[C]:**

> "We've organized explicitly what we know, what we assume, and what we don't know. The honesty about limitations doesn't weaken the proposal — it makes it credible."

---

## SLIDE 11 — EXPERT VALIDATION
**[A]:**

> "We brought the proposal to **five independent experts**: two education researchers, a secondary school principal, a PE teacher, and an education student. Each interviewed independently. Their responses coded for convergence and divergence."

*[Play videos.]*

---

## SLIDE 12 — CLOSE
**[F] closes, facing the audience:**

> "MIT's question was: what stops healthy purchasing in nanostores?"

*[Pause.]*

> "The answer is not what most people expect. It's not ignorance. It's not lack of willpower. The **system is structured to push unhealthy choices** — from the supply chain to the counter — and people don't have the conditions to act on what they already know and already want."

> "The most effective long-term solution is not in the nanostores."

> "It's in the classrooms."

*[Final pause.]*

> "Thank you."

---

## KEY PHRASES TO MEMORIZE (English)

1. **"R² of 0.032 is not a mistake — it's the first real finding."**
2. **"85% know, 63% would, but only 24% do. A gap of 39 points."**
3. **"Our own respondents named the exact intervention we were going to design."**
4. **"We're not regulating the nanostores. We're educating those who will visit them for life."**
5. **"Honesty about limitations doesn't weaken the proposal — it makes it credible."**
