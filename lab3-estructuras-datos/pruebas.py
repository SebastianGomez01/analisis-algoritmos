"""Pruebas de la lista enlazada y de la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash

SERIE = [
    (1000000010, "en bodega"),
    (1000000024, "en reparto"),
    (1000000017, "en bodega"),
    (1000000005, "entregado"),
]

# busquedas exitosas e infructuosas con la serie de ejemplo
lista = ListaEnlazada()
tabla = TablaHash(11)
for guia, estado in SERIE:
    lista.insertar(guia, estado)
    tabla.insertar(guia, estado)

for guia, estado in SERIE:
    assert lista.buscar(guia) == estado
    assert tabla.buscar(guia) == estado
assert lista.buscar(1000000999) is None
assert tabla.buscar(1000000999) is None
assert lista.tamano == tabla.tamano == 4

# colision forzada: con m = 7 las guias 10, 24 y 17 van a la casilla 3
colision = TablaHash(7)
for guia in (10, 24, 17):
    assert colision.hash(guia) == 3
    colision.insertar(guia, "en bodega")

assert colision.casillas[3].tamano == 3
assert colision.buscar(10) == "en bodega"
assert colision.buscar(24) == "en bodega"
assert colision.buscar(17) == "en bodega"
assert colision.buscar(31) is None  # tambien cae en la casilla 3 pero no esta
assert colision.factor_carga() == 3 / 7

# estructuras vacias
assert ListaEnlazada().buscar(1) is None
assert TablaHash(3).buscar(1) is None
assert TablaHash(3).factor_carga() == 0

# colecciones aleatorias: la lista y la tabla tienen que coincidir siempre
azar = random.Random(2025)
estados = ["en bodega", "en reparto", "entregado"]
for _ in range(25):
    cantidad = azar.randint(1, 400)
    casillas = azar.randint(1, 80)
    guias = azar.sample(range(10**9, 10**10), cantidad)

    una_lista = ListaEnlazada()
    una_tabla = TablaHash(casillas)
    for guia in guias:
        estado = azar.choice(estados)
        una_lista.insertar(guia, estado)
        una_tabla.insertar(guia, estado)

    for guia in guias:
        assert una_lista.buscar(guia) == una_tabla.buscar(guia)
        assert una_tabla.buscar(guia) is not None

    existentes = set(guias)
    for _ in range(40):
        otra = azar.randint(10**9, 10**10 - 1)
        if otra not in existentes:
            assert una_lista.buscar(otra) is None
            assert una_tabla.buscar(otra) is None

print("Todas las pruebas pasaron")
