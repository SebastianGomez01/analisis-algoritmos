# Laboratorio evaluativo 2 — Dividir y vencer

**Nombre completo:** John Sebastian Gomez Gonzalez

## Cómo correr esto

Con el entorno virtual de la raíz del repo activado (ver Laboratorio 2 del curso):

```bash
source venv/Scripts/activate      # o venv/bin/activate en Linux/Mac
pip install -r requirements.txt
cd lab2-divide-y-vencer
python pruebas.py                 # si todo está bien imprime "Todas las pruebas pasaron"
python medicion.py                # imprime los tiempos y guarda graficas/tiempo_vs_n.png
```

---

## Parte 1 — Implementar y verificar

Código: [`subarreglo.py`](subarreglo.py) con las tres funciones y [`pruebas.py`](pruebas.py) con las verificaciones.

En las pruebas comparo siempre la **suma** y no los índices, porque si hay dos tramos empatados cualquiera de los dos es válido. Lo que verifico es:

- La serie de ocho días del enunciado (`[-3, 5, -2, 8, -6, 3, 9, -4]`), que tiene que dar 17 en las dos funciones.
- Series de un solo elemento: uno positivo, uno negativo y un cero.
- Una serie con todo negativo, donde gana el valor menos malo.
- Una serie con todo positivo, donde el tramo es la serie completa.
- Un caso donde el mejor tramo cruza el punto medio: `[2, -9, 4, 6, 5, -8, 1]`, con tramo de los índices 2 a 4 y suma 15. Con este caso se prueba `suma_cruzada`, porque el mejor tramo no está entero en ninguna de las dos mitades.
- Que las dos funciones no modifican la lista que reciben.
- 40 listas aleatorias de entre 1 y 80 elementos (semilla fija) en las que la fuerza bruta y el divide y vencerás tienen que dar la misma suma.

---

## Parte 2 — Medir y graficar

Código: [`medicion.py`](medicion.py).

Medí ocho tamaños: 20, 80, 200, 400, 800, 1600, 3200 y 6400 días. Las series son de enteros entre -100 y 100 con semilla fija, y para cada tamaño las dos funciones reciben exactamente la misma lista. Antes de medir, el script verifica que las dos den la misma suma. Cada medición se repite 5 veces con `time.perf_counter()`, se cronometra solo la llamada al algoritmo (no la generación de datos) y en la gráfica y en la tabla uso el promedio.

La gráfica tiene dos paneles con los mismos datos: a la izquierda en escala lineal y a la derecha en escala logarítmica en ambos ejes. Agregué la logarítmica porque en la lineal la curva de divide y vencerás queda pegada al eje y no se ven los tamaños pequeños.

![Tiempo de ejecución contra tamaño de la serie](graficas/tiempo_vs_n.png)

Valores medidos (promedio de 5 corridas):

| n (días) | Fuerza bruta (s) | Divide y vencerás (s) |
|---|---|---|
| 20 | 0,000007 | 0,000011 |
| 80 | 0,000086 | 0,000043 |
| 200 | 0,000539 | 0,000150 |
| 400 | 0,002263 | 0,000256 |
| 800 | 0,009875 | 0,000552 |
| 1600 | 0,041021 | 0,001135 |
| 3200 | 0,165651 | 0,002424 |
| 6400 | 0,652660 | 0,004933 |
