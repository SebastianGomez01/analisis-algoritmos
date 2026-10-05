# Retroalimentación — Laboratorio evaluativo 01: fundamentos, complejidad y recurrencias

**Estudiante:** John Sebastian Gomez · **Laboratorio:** Fundamentos, complejidad y recurrencias (caso Tamiza)
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `ef84012`

Muy buen trabajo: el código funciona y el informe está bien armado.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 25 |
| Calidad de la explicación teórica | 22 / 25 |
| Corrección de la implementación | 16 / 20 |
| Calidad del análisis de las gráficas | 16 / 20 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **83 / 100** |
| **Nota (0–5)** | **4.15** |

## 1. Corrección conceptual (19 / 25)
**Lo que hizo bien:**
- Distingue bien corrección de eficiencia y nombra la restricción incumplida: la ventana de 4 horas.
- Explica con claridad por qué un servidor el doble de rápido solo divide el tiempo entre dos y no cambia el crecimiento cuadrático.
- Su segundo ejemplo (rutas de reparto, de 5.000 a 50.000 pedidos) tiene datos y una restricción concreta.
- Conecta el ahorro de minutos por noche con el consumo de energía acumulado durante años.
- La tensión de que el orden de la lista decide a quién se llama primero está bien explicada.

**Lo que puede mejorar:**
- En los perjuicios éticos nombra al operador del centro de llamadas y al equipo de desarrollo, pero el más importante, el paciente que recibe la llamada tarde, no aparece como persona afectada ni como quien asume el costo del error.
- El segundo perjuicio (la reputación del equipo técnico) es débil frente al riesgo para la salud de una persona.

## 2. Calidad de la explicación teórica (22 / 25)
**Lo que hizo bien:**
- Define los tres casos indicando sobre qué entradas se toma el máximo, el mínimo y el promedio, y justifica usar el peor caso por la ventana estricta.
- Escribió la predicción antes de medir y la contrastó después.
- Resuelve la recurrencia de merge sort con el método maestro: identifica `a`, `b` y `f(n)` y verifica la condición del caso 2.
- La tabla línea por línea de insertion sort y la tabla de complejidades están completas.

**Lo que puede mejorar:**
- Explique con más detalle de dónde sale cada término de la recurrencia (por qué `2T(n/2)` y por qué el costo de mezclar es lineal).
- En el caso promedio faltó justificar un poco más el valor `n(n−1)/4`.

## 3. Corrección de la implementación (16 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista recibida, cuentan solo comparaciones entre elementos y no usan `sorted()` ni `list.sort()`.
- Su `merge_sort` tiene su propia mezcla recursiva.
- Los generadores producen lotes del tamaño pedido, sin repetidos y con semilla reproducible.
- El código cumple el estilo PEP 8.

**Lo que puede mejorar:**
- Varias funciones no tienen docstring: las de graficar en `parte3_casos.py`, `medir_tiempo_promedio` y las funciones `main`.
- Algunas funciones no tienen todos los *type hints* (por ejemplo `medir_escenario`, `graficar_*` y `medir_tiempo_promedio`).

## 4. Calidad del análisis de las gráficas (16 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes rotulados y leyenda, y muestran las curvas en los mismos ejes.
- Identifica con datos el peor caso (C), el mejor (B) y el intermedio (A), y verifica el conteo con 8.128 comparaciones para n=128.
- Concluye que merge sort es mejor describiendo lo que hace cada curva, y lo relaciona con lo calculado en 4.1.
- Declara que la estimación de 5,5 horas para insertion sort es una extrapolación.

**Lo que puede mejorar:**
- Los ejes no indican unidades claras en el tamaño (diga "registros"). Además, la curva de B queda pegada al eje; una escala logarítmica la haría visible.
- Para merge sort dice solo "unos pocos segundos"; calcule el número con el crecimiento `n log n`, como hizo con insertion sort.
- Al responder sobre el servidor, cite explícitamente la gráfica de la Parte 4.
- La explicación de por qué merge sort ya gana en n=128 es una suposición; esa conclusión depende del ruido de las mediciones pequeñas.
- Dice que insertion sort "no garantiza" estabilidad, pero tal como está escrito, con `<` estricto, sí es estable. Revise ese punto.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas acordada y los archivos tienen los nombres exactos.
- El informe sigue el orden pedido, incluye sus instrucciones de reproducción, las gráficas se ven con ruta relativa y cada parte enlaza su código.
- Hay siete commits del laboratorio con mensajes descriptivos.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien listas aleatorias y casos pequeños, y los dos scripts corren sin errores y regeneran las gráficas en pocos segundos.

## Para el próximo laboratorio
- Incluya siempre al afectado directo (aquí, el paciente) cuando se pida identificar perjuicios y quién asume el costo.
- Ponga docstring y *type hints* en todas las funciones, también en las auxiliares y en `main`.
- Cuando estime tiempos, calcule un número para cada algoritmo, no solo para uno.
- Use unidades en los ejes y pruebe una escala logarítmica cuando una curva se aplaste contra el eje.
- Verifique las afirmaciones teóricas, como la estabilidad, contra su propio código.
