"""Medicion de tiempos del subarreglo maximo: fuerza bruta contra divide y venceras."""

import pathlib
import random
import statistics
import time
from collections.abc import Callable
from typing import Any

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

CARPETA = pathlib.Path(__file__).resolve().parent
TAMANOS = [20, 80, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 5
SEMILLA = 1990


def generar_serie(n: int) -> list[int]:
    """Genera una serie de n variaciones de caja entre -100 y 100.

    Args:
        n: cantidad de dias de la serie.

    Returns:
        Lista de n enteros. Para un mismo n la serie siempre es la misma.
    """
    rng = random.Random(SEMILLA * 1000 + n)
    return [rng.randint(-100, 100) for _ in range(n)]


def tiempo_promedio(funcion: Callable[..., Any], *argumentos: Any) -> float:
    """Corre la funcion varias veces y promedia lo que tarda cada corrida.

    Args:
        funcion: funcion que se quiere medir.
        *argumentos: argumentos con los que se llama a la funcion.

    Returns:
        Tiempo promedio por corrida, en segundos.
    """
    tiempos = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        funcion(*argumentos)
        tiempos.append(time.perf_counter() - inicio)
    return statistics.mean(tiempos)


def graficar(tiempos_fb: list[float], tiempos_dc: list[float]) -> None:
    """Guarda graficas/tiempo_vs_n.png con escala lineal y logaritmica.

    Args:
        tiempos_fb: tiempos de la fuerza bruta, uno por tamano de TAMANOS.
        tiempos_dc: tiempos del divide y venceras, uno por tamano de TAMANOS.
    """
    figura, ejes = plt.subplots(1, 2, figsize=(11, 4.5))

    for eje, titulo in zip(ejes, ("Escala lineal", "Escala logaritmica")):
        eje.plot(TAMANOS, tiempos_fb, marker="o", label="Fuerza bruta")
        eje.plot(TAMANOS, tiempos_dc, marker="s", label="Divide y venceras")
        eje.set_title(f"Subarreglo maximo: tiempo vs tamano ({titulo.lower()})")
        eje.set_xlabel("Tamano de la serie (n, dias)")
        eje.set_ylabel("Tiempo de ejecucion (segundos)")
        eje.legend()

    ejes[1].set_xscale("log")
    ejes[1].set_yscale("log")

    figura.tight_layout()
    figura.savefig(CARPETA / "graficas" / "tiempo_vs_n.png")
    plt.close(figura)


def main() -> None:
    """Mide los dos algoritmos en cada tamano, imprime y grafica los tiempos."""
    tiempos_fb = []
    tiempos_dc = []

    for n in TAMANOS:
        serie = generar_serie(n)

        suma_fb = subarreglo_fuerza_bruta(serie)[2]
        suma_dc = subarreglo_maximo(serie, 0, n - 1)[2]
        assert suma_fb == suma_dc, f"las sumas no coinciden con n={n}"

        tiempos_fb.append(tiempo_promedio(subarreglo_fuerza_bruta, serie))
        tiempos_dc.append(tiempo_promedio(subarreglo_maximo, serie, 0, n - 1))
        print(f"n={n}: fuerza bruta={tiempos_fb[-1]:.6f} s, "
              f"divide y venceras={tiempos_dc[-1]:.6f} s")

    graficar(tiempos_fb, tiempos_dc)


if __name__ == "__main__":
    main()
