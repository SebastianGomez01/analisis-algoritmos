"""Algoritmos de ordenamiento del laboratorio evaluativo 1.

Los dos algoritmos ordenan de mayor a menor indice de riesgo, que es
el orden que necesita Tamiza para armar la lista de llamadas, y cuentan
solamente las comparaciones hechas entre elementos de la lista.
"""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    resultado = list(datos)
    comparaciones = 0

    for indice in range(1, len(resultado)):
        valor = resultado[indice]
        posicion = indice

        while posicion > 0:
            comparaciones += 1
            if resultado[posicion - 1] < valor:
                resultado[posicion] = resultado[posicion - 1]
                posicion -= 1
            else:
                break

        resultado[posicion] = valor

    return resultado, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    if len(datos) <= 1:
        return list(datos), 0

    mitad = len(datos) // 2
    mitad_izq, comparaciones_izq = merge_sort(datos[:mitad])
    mitad_der, comparaciones_der = merge_sort(datos[mitad:])
    combinada, comparaciones_combinar = _combinar(mitad_izq, mitad_der)

    return combinada, comparaciones_izq + comparaciones_der + comparaciones_combinar


def _combinar(mitad_izq: list[int], mitad_der: list[int]) -> tuple[list[int], int]:
    """Une dos listas ya ordenadas de mayor a menor en una sola."""
    combinada = []
    comparaciones = 0
    i = 0
    j = 0

    while i < len(mitad_izq) and j < len(mitad_der):
        comparaciones += 1
        if mitad_izq[i] >= mitad_der[j]:
            combinada.append(mitad_izq[i])
            i += 1
        else:
            combinada.append(mitad_der[j])
            j += 1

    combinada.extend(mitad_izq[i:])
    combinada.extend(mitad_der[j:])
    return combinada, comparaciones
