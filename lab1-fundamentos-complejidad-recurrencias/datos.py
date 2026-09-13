"""Generadores de los tres escenarios de entrada del caso Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros a generar.
        semilla: semilla del generador aleatorio, para poder repetir el
            mismo lote en distintas corridas.

    Returns:
        Lista de n valores de riesgo distintos, en orden aleatorio.
    """
    rng = random.Random(semilla)
    return rng.sample(range(1, n + 1), n)


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros a generar.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n valores de riesgo, ordenada de mayor a menor salvo
        el ultimo 2%, que queda revuelto.
    """
    rng = random.Random(semilla)
    ordenado = list(range(n, 0, -1))  # de mayor a menor riesgo

    cantidad_al_final = max(1, round(n * 0.02))
    parte_ordenada = ordenado[:-cantidad_al_final]
    parte_desordenada = ordenado[-cantidad_al_final:]
    rng.shuffle(parte_desordenada)

    return parte_ordenada + parte_desordenada


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros a generar.

    Returns:
        Lista de n valores de riesgo en orden ascendente, es decir,
        al reves del orden que necesita Tamiza.
    """
    return list(range(1, n + 1))
