# Discurso — Presentación MIT LiftLab 2026

> Storytelling para acompañar la presentación de 16 slides.
> Las indicaciones entre corchetes son escénicas. Cada slide está marcado.
> Duración total: ~14–16 min sin contar Q&A.

> **Arco narrativo:**
> 1. Crisis → 2. Modelo simple (falla) → 3. Expansión con datasets → 4. Encuesta propia → 5. Plan centrado en personas → 6. Monte Carlo → 7. Validación experta

---

## SLIDE 1 — Título

**Fernanda:**

> Buenas tardes. Somos Fernanda, Alexis y Carlos.
>
> Esta es la historia de un proyecto que empezó mal — con un modelo estadístico básico que no servía — y de cómo, al darnos cuenta, lo expandimos con datos oficiales, salimos a hablar con cien personas reales, y construimos un plan centrado en ellas.
>
> Empieza con una voz que no es la nuestra.

---

## SLIDE 2 — VIDEO: Tendera

**Antes:**

> Cuando hablamos de obesidad infantil, normalmente hablamos de cifras. Hoy queremos empezar diferente. Esta es Doña [Nombre], dueña de una tiendita aquí en San Luis Potosí. Le pedimos que nos contara qué ve detrás del mostrador todos los días.

**[REPRODUCIR VIDEO — 45–60 s]**

**Después:**

> Doña [Nombre] no es el problema. Es testigo del problema. Y los datos confirman lo que ella ve.

---

## SLIDE 3 — Dashboard: La Crisis

**Fernanda:**

> México tiene una de las crisis de obesidad infantil más severas del mundo. No es opinión: tres de cada diez niños de cinco a once años viven con sobrepeso u obesidad. Cuatro de cada diez adolescentes.
>
> Y la tendencia empeora. Mientras tanto, 1.1 millones de tienditas son el primer punto de acceso a comida en comunidades vulnerables, y la escuela, que antes tenía hasta cinco horas semanales de educación física, hoy tiene dos.
>
> El sistema ya nombró el problema — *Vida Saludable* en la Nueva Escuela Mexicana. Pero un eje articulador sin horas ni capacitación es una buena intención sin músculo. Ahí entró nuestro proyecto.

---

## SLIDE 4 — Primer Intento: Regresión Lineal Simple (falló)

**Carlos:**

> Aquí empezó el proyecto, y aquí casi fracasa.
>
> Hipótesis inicial: si las tienditas son el primer punto de acceso a comida ultraprocesada, debe haber una correlación visible entre su densidad y la obesidad infantil. Probamos con la regresión más simple posible: una variable, 32 estados.
>
> Los números fueron **malos**. R² de 0.064 — el modelo explicaba el 6% de la varianza. El coeficiente era negativo, lo opuesto a lo que esperábamos, y ni siquiera era significativo: p de 0.16.
>
> En una propuesta seria, ese resultado pide tres reacciones. Primero, honestidad: **el modelo es básico y no sirve solo**. Segundo, expansión: traer más variables, controlar por factores estructurales. Tercero, complementariedad: si los datos estatales no muestran causas — solo geografía — hay que ir a hablar con las personas.
>
> Y eso es lo que hicimos a continuación.

---

## SLIDE 5 — La Expansión: 6 Datasets + Regresión Controlada + Random Forest

**Carlos:**

> Si el modelo simple falla, no se abandona el proyecto — se expande.
>
> Trajimos seis datasets oficiales: **INEGI DENUE** para tienditas, **ENSANUT Continua** para obesidad y comportamiento, **ENIGH** para gasto en alimentos, **CONAPO** para marginación, **Anuarios de Morbilidad** para diabetes en menores, y el **Plan SEP 2022** para contexto curricular.
>
> Ocurrieron dos cosas, ambas valiosas.
>
> **Primero: la regresión controlada.** Al añadir marginación y urbanización, el R² subió de 0.064 a 0.634 — diez veces más varianza explicada. Y el coeficiente de densidad de tienditas SE INVIRTIÓ: pasó de negativo a positivo, ahora con p<0.001. ¿Por qué? Porque los estados con más tienditas son los más pobres y rurales — Guerrero, Oaxaca, Chiapas — que paradójicamente tienen menor obesidad. La pobreza enmascaraba el efecto. Una vez que controlamos por eso, las tienditas sí correlacionan con obesidad.
>
> **Segundo: el Random Forest sobre las 8 variables.** Y aquí está el hallazgo más útil: el predictor más importante no son las tienditas. Es el cumplimiento de actividad física, con una correlación de menos 0.91 con la obesidad adolescente. Las tienditas quedaron últimas con importancia de 0.004.
>
> Eso reorientó toda la propuesta. No se trata de regular comercios. Se trata de mover la variable más modificable: **la actividad física en los adolescentes**.

---

## SLIDE 6 — ¿Por qué hicimos nuestra propia encuesta?

**Alexis:**

> Cuando los modelos cuantitativos terminaron de hablar, nos dimos cuenta de algo importante: nos habían dado el QUÉ y el CUÁNTO, pero no el POR QUÉ.
>
> Sabíamos que la actividad física es el predictor más fuerte. Sabíamos que los estados más urbanos tienen más obesidad. Sabíamos que las tienditas, controlando otras variables, sí correlacionan.
>
> Pero **no sabíamos qué decide una madre o un padre cuando llega a casa a las 8 de la noche y tiene que dar de cenar.** No sabíamos qué compran los hijos cuando reciben dinero. No sabíamos si la barrera principal es el tiempo, el dinero, la educación o la voluntad.
>
> Por eso diseñamos nuestra propia encuesta. Aplicada en San Luis Potosí, con población real, no agregados estatales. Estructurada en dos pistas — padres y no padres — para no perder ningún ángulo.
>
> Esto no es complementario al análisis. Es el corazón del análisis.

---

## SLIDE 7 — Resultados de la Encuesta

**Alexis:**

> Cien personas. San Luis Potosí. Diciembre y enero.
>
> La barra más alta de la izquierda no necesita explicación: **38 personas**, la respuesta más frecuente con amplio margen, dicen que no cocinan porque **no tienen tiempo por el trabajo**. Más que las que dicen que no les gusta cocinar.
>
> Ese dato es estructural. La gente no es ignorante, no es perezosa, no le falta motivación. Le falta tiempo. Físicamente.
>
> Ahora la derecha: cuando preguntamos qué soluciones quieren, las dos respuestas más pedidas fueron **acceso a alimentos saludables** y **educación nutricional**. La gente nos estaba diciendo, sin que se lo preguntáramos directamente, qué intervención están dispuestos a recibir.
>
> Y los números de abajo: **79% de los padres están preocupados** por la alimentación de sus hijos. **80 de 98 personas dicen que cambiarían sus hábitos** con más tiempo o recursos. 27 piden explícitamente programas de educación nutricional.
>
> La motivación no es el problema. La estructura sí. Y la población misma nombra la solución.

---

## SLIDE 8 — El Momento de Claridad

**[PAUSA — bajar el ritmo]**

> Una frase. Dicha por 38 personas que no se conocen entre sí: *"No tengo tiempo debido al trabajo."*
>
> Si el tiempo es estructural, no podemos cambiar a los adultos de hoy. Pero sí podemos equipar a los adolescentes de mañana.
>
> Los modelos cuantitativos lo confirman: el predictor más fuerte de obesidad adolescente es la actividad física, con correlación de −0.91. La encuesta lo confirma desde el otro lado: la gente pide educación nutricional explícitamente.
>
> **Cuantitativo y cualitativo apuntan al mismo lugar. El plan ya estaba en los datos. Solo había que construirlo.**

---

## SLIDE 9 — El Plan, centrado en personas

**Fernanda:**

> Aquí está el plan. Lo importante es que cada componente está anclado en un hallazgo concreto, no en una opinión.
>
> **A — EF 2h→3h:** La tercera hora no es deporte adicional. Es alfabetización aplicada. Leer una etiqueta de un producto real de la tiendita, diseñar un snack saludable con 20 pesos, mapear el entorno alimentario. Responde directamente al predictor número uno del Random Forest: la actividad física.
>
> **B — Auditoría de tienditas:** Bisemanales. Es ciencia ciudadana, y produce un dataset geolocal que México hoy no tiene. Responde a las tienditas como nodo obesogénico identificado por la regresión controlada.
>
> **C — Capa estructural:** Nudges en el punto de venta con tienderos voluntarios. Responde directamente a lo que la encuesta dijo: la decisión de compra se toma en segundos, no en la clase del martes.
>
> **D — Capacitación docente:** Pedagogía de autonomía, no cátedra. La fidelidad se mide.
>
> **E — Puente familiar:** Una invitación mensual — nunca tarea. Respeta el hallazgo número uno de la encuesta: la barrera principal es el tiempo.
>
> Doce mil pesos por escuela al año. Escalado a 35 mil secundarias: 420 millones. **Menos del 0.1% del presupuesto federal de educación. Sin necesidad de reforma legislativa.**

---

## SLIDE 10 — Monte Carlo: probamos el plan antes de proponerlo

**Carlos:**

> Una propuesta sin proyección es una opinión. Aquí está la nuestra.
>
> Mil estudiantes simulados, 5,000 corridas por escenario, parámetros tomados de **meta-análisis publicados — no inventados**.
>
> Escenario central: la intervención ralentiza el crecimiento del IMC en **0.68 kg/m² a cinco años**. Aproximadamente seis puntos porcentuales menos de prevalencia de sobrepeso.
>
> Pero la pieza más importante está en el cuarto escenario. Dice cero. Es el escenario nulo de largo plazo: hay un meta-análisis del 2021 que encontró que intervenciones escolares de largo plazo en niños no mueven el IMC. **Lo incluimos.** Si no lo incluyéramos, deberían sospechar de nosotros.
>
> Y aún así, la propuesta sigue siendo defendible: los cambios en comportamiento de compra, en inventario de las tienditas, en la agencia crítica del estudiante — esos son medibles en semanas, no en años.

---

## TRANSICIÓN al bloque de validación

**Alexis:**

> Pero un equipo de tres estudiantes no puede juzgar su propia propuesta. Por eso la sometimos a cinco voces externas. Esto es lo que nos dijeron.

---

## SLIDE 11 — VIDEO: Dr. José Manuel Olais Govea

**Antes:**

> El primero: Dr. José Manuel Olais Govea, investigador del Tec Campus SLP. Le hicimos las ocho preguntas core del protocolo, más tres específicas para su rol.

**[VIDEO]**

**Después (una frase):**

> Del Dr. Olais retuvimos especialmente [su punto clave].

---

## SLIDE 12 — VIDEO: Dr. Leopoldo Zúñiga Silva

**Antes:**

> El segundo investigador, Dr. Leopoldo Zúñiga Silva, también del Tec SLP. Triangulamos para tener dos voces de la misma escuela teórica con énfasis distintos.

**[VIDEO]**

**Después (una frase):**

> Su aporte más fuerte: [tema central]. Reforzó nuestra decisión de [ajuste].

---

## SLIDE 13 — VIDEO: Director, Sec. Téc. 78

**Antes:**

> La validación académica no basta. Entrevistamos al director de la Sec. Téc. 78 de Matehuala — donde, si esto se pilotea, ocurriría primero.

**[VIDEO]**

**Después (una frase):**

> Aprendizaje operativo: [restricción levantada]. Por eso incluimos el fallback en el plan.

---

## SLIDE 14 — VIDEO: Docente de Secundaria

**Antes:**

> Cuarto: un docente de secundaria en activo, además practicante de fitness. Queríamos a alguien que viviera el aula todos los días y entendiera el lado físico de lo que proponemos.

**[VIDEO]**

**Después (una frase):**

> Lo que dijo y nosotros no habíamos visto: [punto inesperado]. Para eso sirve la validación.

---

## SLIDE 15 — VIDEO: Estudiante de Educación

**Antes:**

> La voz que más fácil se olvida: una estudiante de licenciatura en Educación con background deportivo. Nuestro puente entre quien está formándose para enseñar y quien fue alumno hace poco.

**[VIDEO]**

**Después (una frase):**

> Su frase: *"[cita]"*. Si los estudiantes no le ven sentido, ningún diseño funciona.

---

## SLIDE 16 — Cierre

**Fernanda:**

> Esta es una historia donde empezamos mal — con un modelo simple que no servía — y donde, en lugar de esconderlo, lo usamos como punto de partida.
>
> Trajimos seis datasets oficiales y subimos el R² de 0.064 a 0.634. Construimos un Random Forest que identificó la actividad física como el predictor número uno. Salimos a hablar con cien personas reales y entendimos que la barrera es el tiempo, no la voluntad. Diseñamos un plan centrado en personas. Lo probamos con Monte Carlo. Lo sometimos a cinco expertos.
>
> Lo que proponemos no es revolucionario. Es modesto, barato, alineado al NEM, y honesto sobre lo que no sabemos.
>
> Pero si funciona aunque sea a medias, le da a México algo que hoy le falta: una manera concreta, presupuestable, evaluable, de meter la salud infantil en el único lugar donde podemos alcanzarla a tiempo — el salón de clases.
>
> Gracias.

**[Abrir Q&A]**

---

## Cheatsheet de tiempos

| # | Slide | Quién | Duración |
|---|-------|-------|----------|
| 1 | Título | Fernanda | 0:40 |
| 2 | Video tendera | — | 1:00 |
| 3 | La crisis | Fernanda | 1:20 |
| 4 | Primer modelo (falló) | Carlos | 1:30 |
| 5 | La expansión | Carlos | 1:50 |
| 6 | ¿Por qué encuesta? | Alexis | 1:00 |
| 7 | Resultados encuesta | Alexis | 1:30 |
| 8 | Frase pivote | Quien narre | 0:45 |
| 9 | El plan | Fernanda | 1:45 |
| 10 | Monte Carlo | Carlos | 1:20 |
| 11–15 | 5 videos expertos | Alexis intros | ~6:30 |
| 16 | Cierre | Fernanda | 0:50 |
| **Total** | | | **~20 min** |

> Si necesitan recortar a 15 min, los videos de expertos son los más comprimibles (40–50 s cada uno).
