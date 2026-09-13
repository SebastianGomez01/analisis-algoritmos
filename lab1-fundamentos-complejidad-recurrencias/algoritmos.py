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
