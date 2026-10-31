# Laboratorio evaluativo 3 — Estructuras de datos

**Nombre completo:** John Sebastian Gomez Gonzalez

## Cómo correr esto

Con el entorno virtual de la raíz del repo activado (ver Laboratorio 2 del curso):

```bash
source venv/Scripts/activate      # o venv/bin/activate en Linux/Mac
pip install -r requirements.txt
cd lab3-estructuras-datos
python pruebas.py                 # si todo está bien imprime "Todas las pruebas pasaron"
python medicion.py                # imprime los tiempos y guarda las dos gráficas en graficas/
```

---

## Parte 1 — Implementar y verificar

Código: [`estructuras.py`](estructuras.py) con `Nodo`, `ListaEnlazada` y `TablaHash`, y [`pruebas.py`](pruebas.py) con las verificaciones.

`ListaEnlazada.buscar` avanza nodo por nodo con un `while`, sin recursión, y `TablaHash` guarda una `ListaEnlazada` en cada casilla. No usé `dict`, `set` ni `hash()` dentro de las estructuras. Las pruebas con `assert` cubren:

- Búsquedas exitosas e infructuosas en la lista y en la tabla (con `m = 11`), usando las cuatro guías de la serie de ejemplo del enunciado.
- La colisión forzada con `m = 7`: las guías 10, 24 y 17 dan la casilla 3, se insertan las tres y se encuentran después, la lista de esa casilla tiene longitud 3, y la guía 31, que también cae en la casilla 3 pero no está guardada, devuelve `None`.
- `factor_carga()` igual a `3 / 7` después de esas tres inserciones, y 0 en una tabla vacía.
- Lista y tabla vacías.
- 25 colecciones aleatorias (de 1 a 400 guías y de 1 a 80 casillas, con semilla fija) donde la lista y la tabla devuelven el mismo estado para todas las guías existentes y `None` para guías inexistentes.

---

## Parte 2 — Medir y graficar

Código: [`medicion.py`](medicion.py).

Las guías son enteros distintos de diez dígitos generados con semilla fija, y en cada n la lista y la tabla se cargan con las mismas guías. Solo se cronometran las búsquedas (con `time.perf_counter()`), no la construcción ni la generación de datos. Cada medición hace una pasada de calentamiento sin medir y luego 5 repeticiones con el recolector de basura apagado, y uso el promedio del tiempo por búsqueda. Antes de medir, el script verifica que la lista y la tabla den el mismo estado en una muestra de 300 guías existentes.

**Experimento A** (200 búsquedas de guías inexistentes por cada n, tabla con `m` primo cercano a n / 2, o sea α ≈ 2). La gráfica tiene dos paneles con los mismos datos, en escala lineal y en escala logarítmica, porque en la lineal la tabla queda pegada al eje.

![Lista enlazada frente a tabla hash](graficas/lista_vs_tabla.png)

| n (guías) | m de la tabla | Lista (µs por búsqueda) | Tabla (µs por búsqueda) |
|---|---|---|---|
| 200 | 101 | 5,348 | 0,137 |
| 800 | 401 | 21,300 | 0,145 |
| 3000 | 1511 | 82,839 | 0,145 |
| 6000 | 3001 | 163,857 | 0,150 |
| 12000 | 6007 | 332,336 | 0,144 |
| 24000 | 12007 | 675,454 | 0,165 |
| 48000 | 24001 | 1490,327 | 0,135 |
| 96000 | 48017 | 3285,091 | 0,160 |

**Experimento B** (n = 30000 guías fijas, 20000 búsquedas de guías inexistentes por medición): cambio `m` para variar α.

![Tiempo de búsqueda según el factor de carga](graficas/tiempo_vs_alfa.png)

| α | m | Tabla (µs por búsqueda) |
|---|---|---|
| 0,25 | 120011 | 0,218 |
| 0,5 | 60013 | 0,205 |
| 1 | 30011 | 0,199 |
| 3 | 10007 | 0,291 |
| 6 | 5003 | 0,519 |
| 10 | 3001 | 0,702 |

---

## Parte 3 — Análisis

**1. Costo teórico.** Para una guía que no existe, la lista tiene que pasar por todos los nodos antes de poder concluir que no está, así que hace n comparaciones: Θ(n). En la tabla, `guia % m` se calcula en un paso y después solo se revisa la lista de esa casilla, que en promedio tiene n/m = α nodos; por eso el costo esperado es Θ(1 + α). Esto se sostiene si la función hash reparte las guías de manera uniforme (hash uniforme simple): cada guía cae en cualquier casilla con la misma probabilidad e independiente de las demás. Si todas cayeran en la misma casilla, la tabla sería una sola lista de n nodos y buscar volvería a costar Θ(n), exactamente como en la lista original.

**2. Lo medido contra lo esperado.** Al pasar de n = 12000 a n = 24000 la lista se multiplicó por 675,5 / 332,3 ≈ 2,03, como predice Θ(n); la tabla pasó de 0,144 a 0,165 µs, un factor de 1,15 que atribuyo a ruido, porque en toda la tabla los valores se mueven entre 0,135 y 0,165 µs y no crecen con n, como predice Θ(1). Entre 48000 y 96000 la lista creció 2,20 veces (algo más de 2) y la tabla 1,19, otra vez sin tendencia. En la gráfica de α, el tiempo es casi plano hasta α = 1 (0,20 a 0,22 µs) y después sube: 0,291 µs con α = 3, 0,519 con α = 6 y 0,702 con α = 10. De α = 3 a 6 se multiplicó por 1,78 y Θ(1 + α) predice 1,75; de α = 10 contra α = 1 medí 3,5 veces y la fórmula predice 5,5. La diferencia viene de que hay un costo fijo (la llamada y el hash) que no depende de α; la dirección y el orden de magnitud coinciden con Θ(1 + α), aunque no la proporción exacta.

**3. Colisiones.** Una colisión ocurre cuando dos guías distintas dan la misma casilla. Sucede aunque sobren casillas porque hay 10¹⁰ guías posibles para un número de casillas mucho menor, y basta que dos de las guías guardadas coincidan; esto pasa antes de que la tabla esté llena. Con m = 7, las guías 10, 24 y 17 dan casilla 3. Con encadenamiento, las tres quedan en la lista de la casilla 3 y la búsqueda recorre esa lista: es simple y admite α mayor que 1, pero cada nodo gasta memoria en el puntero y las cadenas largas hacen más lenta la búsqueda. Con direccionamiento abierto no hay listas: la 10 se queda en la casilla 3, la 24 prueba la 4 y la 17 la 5. Ahorra la memoria de los punteros y recorre posiciones contiguas, pero α no puede superar 1, las casillas ocupadas seguidas forman rachas y borrar obliga a dejar una marca (lápida).

**4. Tabla hash o árbol de búsqueda.** Para "guías entre X y Y" la tabla no sirve: la función hash mezcla las guías y no conserva el orden, entonces las guías vecinas quedan en casillas lejanas y habría que revisar todas las casillas. Un BST mantiene las guías ordenadas: baja hasta X en Θ(h) y recorre en orden hasta Y, con costo Θ(h + k) para k resultados. Si las 400.000 guías llegan ya ordenadas, cada una se cuelga a la derecha de la anterior y el árbol es una lista: h ≈ 400.000. Insertar la guía número i cuesta unas i comparaciones, así que el total es la suma de 1 hasta 400.000, cerca de 8·10¹⁰. En un árbol equilibrado, h ≈ log₂400000 ≈ 18,6 y el total es del orden de 400.000 · 18,6 ≈ 7,4·10⁶, unas 10.000 veces menos.

**5. Concepto para la jefa de operaciones.** Recomiendo una tabla hash para el call center (consulta puntual) y un árbol de búsqueda balanceado (AVL o rojo-negro) para el monitoreo por rango, a cambio de mantener las guías en dos estructuras. **Lo siguiente es una estimación, no una medición.** La lista crece en forma lineal; con n = 96000 medí 3285 µs, y 5.000.000 es 52 veces más, así que una búsqueda de guía inexistente tardaría unos 3285 · 52 ≈ 171.000 µs, cerca de 0,17 s, o algo más si la memoria penaliza. La tabla, si `m` crece junto con n para mantener α cercano a 2, seguiría en Θ(1 + α) ≈ Θ(1): del orden de 0,15 µs, posiblemente algo más por la memoria. La diferencia sería de más de un millón de veces.
