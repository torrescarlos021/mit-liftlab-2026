# Explicación de los slides de datos — Para Carlos (Charly)
## "De las Tienditas a las Aulas" · MIT LiftLab 2026

> Versión simple, sin tecnicismos. Para que lo puedas explicar con tus propias palabras.
> **ACTUALIZADO para el formato de 5 minutos** — slide numbers corresponden a la nueva presentación.

---

## VERSIÓN 5 MINUTOS — Lo que Carlos explica y cuándo

| Slide | Qué explica Carlos | Tiempo |
|-------|-------------------|--------|
| Slide 2 | R² = 0.032 + AUC = 0.55 | 45 seg |
| Slide 3 | Los 4 números + brecha de 39 pts | 45 seg |
| Slide 6 | Monte Carlo simplificado | 45 seg |

---

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

## SLIDE 6 (versión 5 min) — Monte Carlo SIMPLIFICADO
### ¿Qué muestra ahora la gráfica? (VERSIÓN NUEVA — más fácil)

En la versión anterior había 5 líneas en el tiempo. **Ahora son 3 barras simples** que muestran el resultado al año 5. Mucho más fácil de leer de un vistazo.

**Las 3 barras que ves:**

| Barra | Color | Valor | Qué significa |
|-------|-------|-------|---------------|
| Sin intervención | Rojo | **36.4%** | Si no hacemos nada, la obesidad sube (era 31.9% al inicio) |
| Resultado nulo | Gris | **32.0%** | Si la intervención no funciona, se mantiene estable |
| Con intervención (central) | Verde | **26.2%** | Si funciona según la literatura, baja 5.7 puntos |

**El mensaje visual es inmediato:** la barra verde es claramente más corta. No necesitas explicar matemáticas — la diferencia se ve sola.

**¿Qué es Monte Carlo en una oración?**
Corremos la simulación 5,000 veces con pequeñas variaciones al azar, para ver no solo *qué podría pasar* sino *qué tan probable* es cada resultado. Como lanzar una moneda 5,000 veces en vez de calcularla matemáticamente.

**¿De dónde vienen los números?**
De meta-análisis publicados — estudios que juntan los resultados de docenas de experimentos reales en otros países. No inventamos los efectos; los tomamos de la mejor evidencia disponible (Cochrane, Silveira 2013, Brown 2020).

**¿Por qué incluimos el escenario nulo?**
Porque sería deshonesto no incluirlo. Algunos estudios muestran que las intervenciones escolares no tienen efecto duradero a largo plazo. Lo incluimos para que nadie pueda decir que solo mostramos los resultados buenos. Eso, en el MIT, suma puntos.

**Cómo lo dices en 45 segundos:**
> *"Corrimos Monte Carlo: 5,000 simulaciones, 1,000 estudiantes, 5 años.*
> *Sin intervención, la obesidad sube al 36.4%. Solo por la tendencia natural.*
> *Con nuestra intervención, el escenario central la baja al 26.2% — menos 5.7 puntos.*
> *Y este de aquí es el escenario nulo — donde no funciona. Lo incluimos porque la honestidad es parte de nuestro método."*

---

## SLIDE 6 — Panel de honestidad epistémica (mismo slide que Monte Carlo)

El lado derecho del slide muestra tres columnas. No tienes que leerlas — solo señalarlas y decir:

> *"A la derecha separamos lo que sabemos con datos reales, lo que asumimos de la literatura, y lo que todavía no sabemos. En el MIT no buscan proyectos perfectos. Buscan proyectos honestos."*

---

## RESUMEN ACTUALIZADO: Las 5 frases que Charly debe dominar (versión 5 min)

1. **"R² de 0.032 — el modelo no explica casi nada. Ese fracaso fue el primer hallazgo."** *(Slide 2)*
2. **"El Random Forest dio AUC 0.55 — casi igual que el azar. La barrera no es de las personas, es del sistema."** *(Slide 2)*
3. **"85% sabe, 63% querría, solo 24% compra. Brecha de 39 puntos."** *(Slide 3)*
4. **"Monte Carlo, 5,000 corridas: sin intervención 36.4%, con intervención 26.2%. Menos 5.7 puntos."** *(Slide 6)*
5. **"Incluimos el resultado nulo intencionalmente. La honestidad no es opcional."** *(Slide 6)*
