"""Validacion experimental de la parte 4: insertion sort contra merge sort.

Se mide sobre el escenario A (aleatorio) porque es el mas parecido a lo
que llega por el portal web de los laboratorios, sin ningun orden previo.
"""

import pathlib
import statistics
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

CARPETA = pathlib.Path(__file__).resolve().parent
TAMANOS = [128, 256, 512, 1024, 2048, 4096, 8192]
REPETICIONES = 3


def medir_tiempo_promedio(funcion_ordenar, tamano: int) -> float:
    tiempos = []
    for _ in range(REPETICIONES):
        lote = generar_aleatorio(tamano)
        inicio = time.perf_counter()
        funcion_ordenar(lote)
        tiempos.append(time.perf_counter() - inicio)
    return statistics.mean(tiempos)


def main() -> None:
    tiempos_insertion = []
    tiempos_merge = []

    for tamano in TAMANOS:
        t_insertion = medir_tiempo_promedio(insertion_sort, tamano)
        t_merge = medir_tiempo_promedio(merge_sort, tamano)
        tiempos_insertion.append(t_insertion)
        tiempos_merge.append(t_merge)
        print(f"n={tamano}: insertion_sort={t_insertion:.6f} s, merge_sort={t_merge:.6f} s")

    plt.figure()
    plt.plot(TAMANOS, tiempos_insertion, marker="o", label="insertion sort")
    plt.plot(TAMANOS, tiempos_merge, marker="o", label="merge sort")
    plt.title("Tiempo de ejecucion vs tamano del lote (escenario A)")
    plt.xlabel("Tamano del lote (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.savefig(CARPETA / "graficas" / "parte4_tiempo.png")
    plt.close()


if __name__ == "__main__":
    main()
