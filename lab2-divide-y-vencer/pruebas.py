"""Pruebas de la fuerza bruta y del divide y venceras."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def suma_divide_y_venceras(valores: list[float]) -> float:
    """Devuelve la suma que calcula subarreglo_maximo sobre toda la lista."""
    return subarreglo_maximo(valores, 0, len(valores) - 1)[2]


# la serie de ocho dias del enunciado
serie = [-3, 5, -2, 8, -6, 3, 9, -4]
assert subarreglo_fuerza_bruta(serie)[2] == 17
assert suma_divide_y_venceras(serie) == 17

# series de un solo elemento
for unico in ([5], [-1], [0]):
    assert subarreglo_fuerza_bruta(unico)[2] == unico[0]
    assert suma_divide_y_venceras(unico) == unico[0]

# todo negativo: se queda con el valor menos malo
negativos = [-7, -4, -9, -1, -6]
assert subarreglo_fuerza_bruta(negativos)[2] == -1
assert suma_divide_y_venceras(negativos) == -1

# todo positivo: la racha es la serie completa
positivos = [2, 9, 4, 1, 6, 3]
assert subarreglo_fuerza_bruta(positivos) == (0, 5, 25)
assert subarreglo_maximo(positivos, 0, 5) == (0, 5, 25)

# el mejor tramo cruza el punto medio (indice 3) y queda en los indices 2 a 4
cruzado = [2, -9, 4, 6, 5, -8, 1]
assert subarreglo_fuerza_bruta(cruzado) == (2, 4, 15)
assert subarreglo_maximo(cruzado, 0, 6) == (2, 4, 15)

# ninguna funcion toca la lista original
original = list(serie)
subarreglo_fuerza_bruta(serie)
subarreglo_maximo(serie, 0, len(serie) - 1)
assert serie == original

# listas aleatorias: las dos soluciones tienen que dar la misma suma
random.seed(1234)
for _ in range(40):
    largo = random.randint(1, 80)
    lista = [random.randint(-100, 100) for _ in range(largo)]
    assert subarreglo_fuerza_bruta(lista)[2] == suma_divide_y_venceras(lista), lista

print("Todas las pruebas pasaron")
