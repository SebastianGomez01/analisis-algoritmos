# Retroalimentación — Laboratorio evaluativo 02: Dividir y vencer

**Estudiante:** John Sebastian Gomez Gonzalez · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `6763799`

Excelente trabajo: un laboratorio completo, ordenado y respaldado con sus propios datos.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 20 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 25 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **100 / 100** |
| **Nota (0–5)** | **5.00** |

## 1. Corrección conceptual (20 / 20)
**Lo que hizo bien:**
- Identifica que divide y vencerás empieza a ganar entre n = 20 y n = 80, con los tiempos medidos, y aclara que la causa es una hipótesis y no algo probado.
- Compara con el máximo de un arreglo: explica que combinar cuesta solo una comparación, que la recurrencia da `Θ(n)` y que por eso dividir no mejora nada.
- Recomienda divide y vencerás y estima 1.000.000 de registros (horas contra cerca de un segundo), declarando que es una estimación y sin usar una regla de tres lineal.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` explicando de dónde sale cada término, incluido el costo del caso cruzado.
- Resuelve con el método maestro verificando que se cumple la condición del caso 2.
- Justifica el `Θ(n²)` de la fuerza bruta contando las pasadas, `n(n+1)/2`.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en la serie de ocho días, con un elemento, todo negativo, todo positivo y en un caso cruzado.
- `subarreglo_maximo` resuelve los tres casos por sí misma, sin llamar a la fuerza bruta, y ninguna función cambia la lista recibida.
- Las pruebas incluyen 40 listas aleatorias y comparan sumas, no índices.
- El código sigue PEP 8 y tiene *type hints* y *docstrings* en cada función.

## 4. Calidad del análisis de las gráficas (25 / 25)
**Lo que hizo bien:**
- La gráfica tiene ambas curvas en los mismos ejes, título, ejes rotulados y leyenda, con ocho tamaños y una versión en escala logarítmica muy útil.
- Calcula el factor al duplicar n de 3200 a 6400 (cerca de 3,94 y 2,04) y lo compara con lo que predicen `Θ(n²)` y `Θ(n log n)`.
- Lo que dice del informe coincide con lo que se ve en la gráfica publicada.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta `lab2-divide-y-vencer/` tiene exactamente los archivos pedidos y la gráfica se ve incrustada con ruta correcta.
- Hay enlaces al código al inicio de cada parte, instrucciones para reproducir y seis commits descriptivos.
- Entregó en la rama `main`, antes de la fecha límite.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos dan la misma suma en todos los tamaños y la medición genera la gráfica sin errores.

## Para el próximo laboratorio
- Siga midiendo con varias repeticiones y semilla fija, como hizo aquí.
- Conserve el hábito de declarar como hipótesis lo que no probó.
- Mantenga commits pequeños y con mensajes claros.
- Si puede, pruebe también con series mucho más grandes para confirmar sus estimaciones.
