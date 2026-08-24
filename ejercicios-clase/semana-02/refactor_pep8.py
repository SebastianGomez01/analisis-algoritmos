"""Ejemplo de cálculo de promedio con convenciones PEP 8."""


def calcular_promedio(numeros: list[int]) -> float:
    """Calcula el promedio de una lista de números enteros.

    Args:
        numeros: Lista de valores enteros para promediar.

    Returns:
        El promedio de los valores recibidos.
    """
    suma = 0

    for numero in numeros:
        suma += numero

    return suma / len(numeros)


def main() -> None:
    """Ejecuta el ejemplo con la lista definida para el ejercicio."""
    numeros_ejemplo = [1, 2, 3, 4, 5]
    print(calcular_promedio(numeros_ejemplo))


if __name__ == "__main__":
    main()