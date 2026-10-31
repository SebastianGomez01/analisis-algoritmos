"""Mediciones del laboratorio 3: lista enlazada contra tabla hash."""

import gc
import pathlib
import random
import statistics
import time

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

CARPETA = pathlib.Path(__file__).resolve().parent
SEMILLA = 1990
TAMANOS = [200, 800, 3000, 6000, 12000, 24000, 48000, 96000]
BUSQUEDAS_A = 200
N_FIJO = 30000
ALFAS = [0.25, 0.5, 1, 3, 6, 10]
BUSQUEDAS_B = 20000
REPETICIONES = 5


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def siguiente_primo(desde: int) -> int:
    """Busca el primer numero primo mayor o igual a un valor.

    Args:
        desde: valor a partir del cual se busca.

    Returns:
        El primo mas pequeno que es mayor o igual a desde.
    """
    candidato = max(desde, 2)
    while True:
        divisor = 2
        es_primo = True
        while divisor * divisor <= candidato:
            if candidato % divisor == 0:
                es_primo = False
                break
            divisor += 1
        if es_primo:
            return candidato
        candidato += 1


def crear_guias(n: int) -> list[int]:
    """Crea n guias distintas de diez digitos con semilla fija.

    Args:
        n: cantidad de guias.

    Returns:
        Lista de n enteros distintos entre 10**9 y 10**10 - 1.
    """
    azar = random.Random(SEMILLA * 100 + n)
    return azar.sample(range(10**9, 10**10), n)


def cargar(guias: list[int], casillas: int) -> tuple[ListaEnlazada, TablaHash]:
    """Carga una lista y una tabla con las mismas guias.

    Args:
        guias: guias a insertar.
        casillas: numero de casillas de la tabla.

    Returns:
        La lista y la tabla ya cargadas.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(casillas)
    for guia in guias:
        estado = "en reparto" if guia % 3 == 0 else "en bodega"
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla


def comprobar_igualdad(lista: ListaEnlazada, tabla: TablaHash, guias: list[int]) -> None:
    """Verifica que lista y tabla den el mismo estado en una muestra.

    Args:
        lista: lista cargada con las guias.
        tabla: tabla cargada con las mismas guias.
        guias: guias existentes de las que se toma la muestra.
    """
    muestra = random.Random(SEMILLA).sample(guias, min(300, len(guias)))
    for guia in muestra:
        assert lista.buscar(guia) is not None
        assert lista.buscar(guia) == tabla.buscar(guia)


def tiempo_por_busqueda(estructura: ListaEnlazada | TablaHash, guias: list[int]) -> float:
    """Calcula el tiempo promedio de una busqueda en una estructura.

    Hace una pasada de calentamiento y despues varias repeticiones; la
    medicion se hace con el recolector de basura apagado.

    Args:
        estructura: lista o tabla donde se busca.
        guias: guias que se buscan en cada repeticion.

    Returns:
        Promedio del tiempo por busqueda, en segundos.
    """
    for guia in guias:
        estructura.buscar(guia)

    gc.disable()
    tiempos = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        for guia in guias:
            estructura.buscar(guia)
        tiempos.append((time.perf_counter() - inicio) / len(guias))
    gc.enable()
    return statistics.mean(tiempos)


def experimento_a() -> tuple[list[float], list[float]]:
    """Compara lista y tabla (alfa cercano a 2) para cada n de TAMANOS.

    Returns:
        Los tiempos por busqueda de la lista y de la tabla, en segundos.
    """
    de_lista = []
    de_tabla = []
    for n in TAMANOS:
        guias = crear_guias(n)
        casillas = siguiente_primo(n // 2)
        lista, tabla = cargar(guias, casillas)
        comprobar_igualdad(lista, tabla, guias)

        inexistentes = generar_guias_inexistentes(set(guias), BUSQUEDAS_A)
        de_lista.append(tiempo_por_busqueda(lista, inexistentes))
        de_tabla.append(tiempo_por_busqueda(tabla, inexistentes))
        print(
            f"n={n}, m={casillas}: lista={de_lista[-1] * 1e6:.3f} us, "
            f"tabla={de_tabla[-1] * 1e6:.3f} us"
        )
    return de_lista, de_tabla


def experimento_b() -> list[float]:
    """Mide la tabla con N_FIJO guias y distintos valores de alfa.

    Returns:
        El tiempo por busqueda, en segundos, para cada alfa de ALFAS.
    """
    guias = crear_guias(N_FIJO)
    inexistentes = generar_guias_inexistentes(set(guias), BUSQUEDAS_B)
    tiempos = []
    for alfa in ALFAS:
        casillas = siguiente_primo(round(N_FIJO / alfa))
        _, tabla = cargar(guias, casillas)
        tiempos.append(tiempo_por_busqueda(tabla, inexistentes))
        print(f"alfa={tabla.factor_carga():.2f}, m={casillas}: {tiempos[-1] * 1e6:.3f} us")
    return tiempos


def graficar_a(de_lista: list[float], de_tabla: list[float]) -> None:
    """Guarda graficas/lista_vs_tabla.png con escala lineal y logaritmica.

    Args:
        de_lista: tiempos de la lista, uno por tamano de TAMANOS.
        de_tabla: tiempos de la tabla, uno por tamano de TAMANOS.
    """
    figura, ejes = plt.subplots(1, 2, figsize=(11, 4.5))
    for eje, escala in zip(ejes, ("lineal", "logaritmica")):
        eje.plot(TAMANOS, [t * 1e6 for t in de_lista], marker="o", label="Lista enlazada")
        eje.plot(TAMANOS, [t * 1e6 for t in de_tabla], marker="s", label="Tabla hash")
        eje.set_title(f"Guia inexistente: lista vs tabla (escala {escala})")
        eje.set_xlabel("Numero de guias (n)")
        eje.set_ylabel("Tiempo por busqueda (microsegundos)")
        eje.legend()
    ejes[1].set_xscale("log")
    ejes[1].set_yscale("log")
    figura.tight_layout()
    figura.savefig(CARPETA / "graficas" / "lista_vs_tabla.png")
    plt.close(figura)


def graficar_b(tiempos: list[float]) -> None:
    """Guarda graficas/tiempo_vs_alfa.png.

    Args:
        tiempos: tiempos por busqueda, uno por valor de ALFAS.
    """
    plt.figure()
    plt.plot(ALFAS, [t * 1e6 for t in tiempos], marker="o", label=f"Tabla hash (n = {N_FIJO})")
    plt.title("Tiempo de busqueda segun el factor de carga")
    plt.xlabel("Factor de carga (alfa = n / m)")
    plt.ylabel("Tiempo por busqueda (microsegundos)")
    plt.legend()
    plt.savefig(CARPETA / "graficas" / "tiempo_vs_alfa.png")
    plt.close()


def main() -> None:
    """Corre los dos experimentos, imprime los tiempos y guarda las graficas."""
    print("Experimento A: lista contra tabla")
    de_lista, de_tabla = experimento_a()
    graficar_a(de_lista, de_tabla)

    print("Experimento B: factor de carga")
    graficar_b(experimento_b())


if __name__ == "__main__":
    main()
