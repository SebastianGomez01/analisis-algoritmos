"""Experimento de la parte 3: mejor, peor y caso promedio de insertion sort.

Antes de correr esto, mi prediccion es que el escenario C (orden inverso)
va a ser el peor caso, porque es justo el orden contrario al que arma
insertion_sort, y que el B (casi ordenado) va a ser el mejor porque casi
todo ya esta en su lugar. Abajo queda el numero real para comparar contra
esta prediccion.
"""

import pathlib
import statistics
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

CARPETA = pathlib.Path(__file__).resolve().parent
TAMANOS = [128, 256, 512, 1024, 2048, 4096, 8192]
REPETICIONES = 3

ESCENARIOS = {
    "A - aleatorio": generar_aleatorio,
    "B - casi ordenado": generar_casi_ordenado,
    "C - orden inverso": generar_inverso,
}


def medir_escenario(generador, tamano: int) -> tuple[float, int]:
    """Corre insertion_sort varias veces sobre un lote y promedia el tiempo.

    El numero de comparaciones no cambia entre repeticiones porque el
    generador siempre produce el mismo lote para el mismo tamano.
    """
    tiempos = []
    comparaciones = 0
    for _ in range(REPETICIONES):
        lote = generador(tamano)
        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(lote)
        tiempos.append(time.perf_counter() - inicio)
    return statistics.mean(tiempos), comparaciones


def graficar_comparaciones(resultados: dict) -> None:
    plt.figure()
    for nombre, valores in resultados.items():
        plt.plot(TAMANOS, valores["comparaciones"], marker="o", label=nombre)
    plt.title("Insertion sort: comparaciones segun el escenario de entrada")
    plt.xlabel("Tamano del lote (n)")
    plt.ylabel("Numero de comparaciones")
    plt.legend()
    plt.savefig(CARPETA / "graficas" / "parte3_comparaciones.png")
    plt.close()


def graficar_tiempos(resultados: dict) -> None:
    plt.figure()
    for nombre, valores in resultados.items():
        plt.plot(TAMANOS, valores["tiempos"], marker="o", label=nombre)
    plt.title("Insertion sort: tiempo de ejecucion segun el escenario de entrada")
    plt.xlabel("Tamano del lote (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.savefig(CARPETA / "graficas" / "parte3_tiempo.png")
    plt.close()


def main() -> None:
    resultados = {nombre: {"tiempos": [], "comparaciones": []} for nombre in ESCENARIOS}

    for nombre, generador in ESCENARIOS.items():
        for tamano in TAMANOS:
            tiempo, comparaciones = medir_escenario(generador, tamano)
            resultados[nombre]["tiempos"].append(tiempo)
            resultados[nombre]["comparaciones"].append(comparaciones)
            print(f"{nombre}, n={tamano}: {comparaciones} comparaciones, {tiempo:.6f} s")

    graficar_comparaciones(resultados)
    graficar_tiempos(resultados)


if __name__ == "__main__":
    main()
