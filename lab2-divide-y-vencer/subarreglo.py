"""Subarreglo maximo: fuerza bruta y divide y venceras."""


def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias (i, j).

    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    n = len(valores)
    mejor = (0, 0, valores[0])

    for inicio in range(n):
        acumulado = 0
        for fin in range(inicio, n):
            acumulado += valores[fin]
            if acumulado > mejor[2]:
                mejor = (inicio, fin, acumulado)

    return mejor
