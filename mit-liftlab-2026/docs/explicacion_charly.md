# Explicación de los slides de datos — Para Carlos (Charly)
## "De las Tienditas a las Aulas" · MIT LiftLab 2026

> Versión simple, sin tecnicismos. Para que lo puedas explicar con tus propias palabras.

---

## SLIDE 3 — La regresión que no funcionó
### ¿Qué dice la gráfica?

Hay 5 barras, una por cada "prueba" que le hicimos al modelo. El modelo era una **regresión lineal** — básicamente una línea recta que intenta adivinar cuánto gasta una persona según quién es.

**Lo que ves:** todas las barras están cerquísimas de cero. Una incluso es negativa (está por debajo del piso).

**Qué significa R² = 0.032:**
Imagina que R² es un porcentaje de cuánto "entiende" el modelo. Un 100% significaría que adivina perfecto. Un 0% significa que no sabe nada — igual que lanzar un dado. Nuestro modelo obtuvo **3.2%**. Básicamente no sirve.

**¿Por qué eso es interesante y no solo un fracaso?**
Porque nos dice algo importante: *el comportamiento de compra en las tienditas no depende de quién eres* — de tu edad, tu género, tu presupuesto. Hay algo más grande que eso. Y eso nos llevó a buscar qué era.

**Cómo lo dices en la presentación:**
> *"El modelo que usamos normalmente no funcionó. Y eso, curiosamente, fue nuestra primera respuesta: el problema no es individual."*

---

## SLIDE 4 — Los cuatro números del Acto 2
### ¿Qué dicen los números?

Los cuatro números grandes son estadísticas de los **1,135 compradores** que el MIT entrevistó en tienditas reales.

| Número | Qué significa en palabras simples |
|--------|-----------------------------------|
| **60.8%** | De cada 10 personas que entran a una tiendita, 6 se llevan algo no saludable (refresco, papitas, etc.) |
| **50.3%** | De esas 10 personas, 5 se llevan **solo** cosas no saludables. Nada sano en absoluto. |
| **23.7%** | Solo 2 de cada 10 se llevan algo saludable (fruta, agua) |
| **66%** | De cada 3 repartidores que llegaron a surtir una tienda, 2 ni siquiera ofrecieron productos saludables |

**La imagen que ayuda:**
Imagina que ves a 10 personas entrar y salir de una tiendita. 5 de ellas salen solo con papitas y refrescos. Solo 2 salen con algo sano. Y la mitad de los camiones que surten la tienda ni siquiera traen opciones sanas para vender.

**Las dos gráficas de abajo:**
- La de la izquierda (barras horizontales) muestra qué productos se compran más. Las barras rojas son lo no saludable, las verdes lo saludable. Las rojas ganan por mucho.
- La de la derecha muestra la "paradoja": la gente sabe, querría, y pide opciones sanas — pero no las compra. Esa brecha de 39 puntos es la clave de todo el proyecto.

---

## SLIDE 5 — El corazón del hallazgo (la caja negra)
### ¿Por qué hay una caja negra enorme?

Porque ese es **el hallazgo más importante** de todo el proyecto y queremos que se vea así.

**¿Qué dice?**
- **85%** sabe que lo que compra le hace daño
- **63%** dice que compraría más sano si pudiera
- **65%** quiere que haya más opciones sanas disponibles
- Pero solo el **24%** realmente compra algo sano

La brecha entre el 63% y el 24% es de **39 puntos porcentuales**. Eso es lo que llamamos la "paradoja intención-acción": la gente no es ignorante ni floja. Sabe y quiere. Pero algo se lo impide.

**¿Qué es el Random Forest y por qué AUC = 0.55 es relevante?**

Un **Random Forest** es un modelo de inteligencia artificial más avanzado que una regresión. Le preguntamos: *¿puedes predecir quién va a comprar algo sano, basándote en las características de esa persona?*

**AUC = 0.55** significa: el modelo acierta el 55% de las veces. Un modelo perfecto sería 100%. Un modelo inútil que adivina al azar sería 50%.

Tener 55% es casi lo mismo que adivinar a ciegas. Lo que eso nos dice: **no importa quién seas — joven, grande, hombre, mujer, con presupuesto alto o bajo — la probabilidad de que compres sano es casi la misma para todos.** No es un rasgo de la persona. Es una barrera del sistema.

**Cómo lo dices:**
> *"Usamos también inteligencia artificial. Y tampoco sirvió para predecir quién compra sano. No porque el modelo sea malo — sino porque la barrera no está en las personas. Está en lo que les rodea: precios, disponibilidad, lo que llega a la tienda."*

---

## SLIDE 9 — Monte Carlo (la proyección)
### ¿Qué es una simulación Monte Carlo?

Imagina que lanzas una moneda 5,000 veces para estimar cuántas veces cae cara. No lo calculas una vez — lo repites miles de veces para ver el rango de resultados posibles. Eso es, básicamente, Monte Carlo.

Nosotros lo usamos para proyectar qué le pasaría al IMC (índice de masa corporal) de 1,000 estudiantes si aplicamos la intervención, durante 5 años. Y lo repetimos **5,000 veces por escenario** para ver el rango de lo que podría pasar.

**¿Por qué no usamos solo datos reales de México?**
Porque no existen. No hay un estudio de 5 años en secundarias mexicanas con este tipo de intervención. Lo que sí existen son **meta-análisis** — estudios que compilan los resultados de docenas de experimentos en otros países. Usamos esos números como punto de partida.

**¿Qué muestra la gráfica?**
Cinco líneas que van del año 0 al año 5:

- **Línea gris punteada (Sin intervención):** si no hacemos nada, la obesidad en la cohorte sube de 31.9% a 36.4%. Solo por el crecimiento natural.
- **Línea gris clara punteada (Resultado nulo):** si la intervención no funciona en absoluto (basado en un estudio pesimista de 2021), se queda estable alrededor de 32%.
- **Línea dorada (Conservador):** si funciona poco, baja a 29.8%.
- **Línea verde oscuro (Central):** con el efecto promedio de la literatura publicada, baja a **26.2%**. Una reducción de 5.7 puntos porcentuales.
- **Línea azul (Optimista):** si funciona bien, baja a 22.7%.

**La tabla de la derecha** resume esos mismos números para que sean fáciles de comparar.

**¿Por qué incluimos el escenario nulo?**
Porque sería deshonesto no incluirlo. La evidencia dice que a largo plazo algunas intervenciones escolares no tienen efecto duradero. Lo incluimos para que nadie pueda decir que solo mostramos los resultados buenos.

**Cómo lo dices:**
> *"Corrimos 5,000 simulaciones. El escenario más probable nos da una reducción de 5.7 puntos en la prevalencia de obesidad a 5 años. Y les mostramos también el escenario donde no funciona — porque la honestidad es parte de nuestro método."*

---

## SLIDE 10 — Las tres columnas (lo que sabemos / asumimos / no sabemos)
### ¿Para qué sirve este slide?

Para demostrar madurez intelectual. Los jueces del MIT saben que cualquier proyecto tiene limitaciones. Si las escondes, desconfían. Si las declaras abiertamente, les das más credibilidad a tus resultados.

**Lo que sabemos** (verde): cosas que medimos directamente con datos reales.
**Lo que asumimos** (dorado): cosas que tomamos de la literatura pero que no medimos nosotros.
**Lo que no sabemos** (rojo): preguntas abiertas que necesitarían un piloto real para responder.

**Cómo lo dices:**
> *"En el MIT no buscan proyectos perfectos. Buscan proyectos honestos. Por eso separamos explícitamente lo que sabemos, lo que asumimos, y lo que todavía no sabemos."*

---

## RESUMEN: Las 5 frases que Charly debe dominar

1. **"R² de 0.032 — el modelo no explica casi nada. Ese fracaso fue el primer hallazgo."**
2. **"El Random Forest dio AUC 0.55 — casi igual que el azar. Lo que nos dice que el problema no es de las personas."**
3. **"85% sabe, 63% querría, 24% compra. Brecha de 39 puntos."**
4. **"Monte Carlo, 5,000 corridas: escenario central da −5.7 pp en obesidad a 5 años."**
5. **"Incluimos el resultado nulo intencionalmente. La honestidad no es opcional."**
