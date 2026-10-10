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


def suma_cruzada(
    valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado (inclusive).
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    # hacia la izquierda desde el medio
    acumulado = 0
    suma_izq = valores[medio]
    borde_izq = medio
    for i in range(medio, inicio - 1, -1):
        acumulado += valores[i]
        if acumulado > suma_izq:
            suma_izq = acumulado
            borde_izq = i

    # hacia la derecha desde medio + 1
    acumulado = 0
    suma_der = valores[medio + 1]
    borde_der = medio + 1
    for j in range(medio + 1, fin + 1):
        acumulado += valores[j]
        if acumulado > suma_der:
            suma_der = acumulado
            borde_der = j

    return borde_izq, borde_der, suma_izq + suma_der


def subarreglo_maximo(
    valores: list[float], inicio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y venceras.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar (inclusive).
        fin: indice final del rango a considerar (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2
    candidatos = [
        subarreglo_maximo(valores, inicio, medio),
        subarreglo_maximo(valores, medio + 1, fin),
        suma_cruzada(valores, inicio, medio, fin),
    ]

    mejor = candidatos[0]
    for candidato in candidatos[1:]:
        if candidato[2] > mejor[2]:
            mejor = candidato
    return mejor
