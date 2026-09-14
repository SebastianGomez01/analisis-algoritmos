# Laboratorio evaluativo 1 — Fundamentos, complejidad y recurrencias

**Nombre:** John Sebastian Gomez

## Cómo correr esto

Con el entorno virtual de la raíz del repo ya activado (ver Laboratorio 2):

```bash
source venv/Scripts/activate      # o venv/bin/activate en Linux/Mac
pip install -r requirements.txt
cd lab1-fundamentos-complejidad-recurrencias
python parte3_casos.py
python parte4_complejidad.py
```

El primer script deja las gráficas `parte3_comparaciones.png` y `parte3_tiempo.png` en `graficas/`, y el segundo deja `parte4_tiempo.png`. En consola también quedan impresos los números que se citan más abajo.

---

## Parte 1 — Analizar el algoritmo antes de comprar hardware

Que insertion sort lleve ocho años funcionando bien en Tamiza confirma que es **correcto**: para cualquier lote que reciba, en algún momento termina y entrega la lista ordenada por riesgo. Pero eso no dice nada sobre si es una buena elección para este problema, porque corrección y eficiencia son dos cosas distintas — la eficiencia mide cuánto tarda (o cuánta memoria gasta) en llegar a ese resultado correcto, y acá la restricción concreta que se está incumpliendo es la ventana de 4 horas. Un algoritmo puede ser 100% correcto y aun así no servir si tarda más de lo que el sistema puede esperar.

Por qué duplicar la velocidad del servidor no arregla el problema de raíz: insertion sort tiene un costo que crece con el cuadrado del número de registros. Si el volumen de datos se duplicó al pasar de unos pocos laboratorios a los 340 de todo el departamento, el tiempo de ordenamiento no se duplicó también, se multiplicó por cuatro. Un servidor el doble de rápido solo divide ese tiempo entre dos, así que en el mejor de los casos deja el proceso donde estaba antes de la ampliación — y en cuanto la Secretaría vuelva a ampliar la cobertura (que es literalmente el objetivo del programa), va a tocar comprar hardware otra vez. Es un parche que hay que repetir cada vez que crece el volumen, mientras que cambiar a un algoritmo de orden n log n resuelve esto de fondo, sin depender de comprar más máquina cada dos años.

Otro ejemplo, bien distinto: una empresa de mensajería que cada madrugada arma las rutas de reparto ordenando los pedidos del día por franja horaria de entrega prometida. Si la empresa opera con 5.000 pedidos diarios en una ciudad y decide expandirse a diez ciudades, el volumen puede llegar a 50.000 pedidos, y si el algoritmo que arma esas rutas también es de los que escalan cuadrático, el tiempo de cómputo no crece 10 veces, crece 100 veces. La restricción que se rompe ahí no es "el servidor es viejo", es que el algoritmo elegido no aguanta el volumen que la empresa necesita procesar todas las mañanas antes de que salgan los repartidores.

---

## Parte 2 — Responsabilidad ambiental y ética

**Ambiental.** El tiempo que tarda el proceso de ordenamiento se traduce directo en consumo eléctrico del servidor, y esto no es un gasto aislado: corre todas las madrugadas, sin descanso, mientras la plataforma siga en producción. Si cambiar de insertion sort a un algoritmo más rápido ahorra, digamos, 20 minutos de cómputo por noche, ese ahorro se repite 365 veces al año y se acumula durante todos los años que Tamiza siga corriendo. Mantener un algoritmo ineficiente en un proceso que se repite todos los días no es un descuido menor, es una decisión que tiene un costo energético que se paga una y otra vez, indefinidamente.

**Ética.** Encuentro al menos dos perjuicios concretos, con alguien identificable detrás de cada uno:

1. El **operador del centro de llamadas**, que en las madrugadas donde el proceso no termina a tiempo probablemente tiene que trabajar con una lista incompleta o reprocesar algo a mano bajo presión, cargando con un problema que no generó él sino el software que le entregan.
2. El **equipo de desarrollo/soporte** de la plataforma, que es quien va a tener que explicar por qué la lista quedó incompleta cuando eso ya pasó tres veces, aunque la causa real sea una decisión de diseño de hace ocho años que nadie revisó a tiempo — el costo de la reputación técnica cae sobre quien mantiene el sistema hoy, no sobre quien lo escribió originalmente.

Y hay una tensión de fondo que vale la pena nombrar: el orden en que queda la lista decide, en la práctica, a quién se llama primero. Si el ordenamiento falla o queda incompleto, no es un error neutro como perder una fila en un reporte cualquiera — significa que alguien con más riesgo cardiovascular puede quedar más abajo en la fila que alguien con menos riesgo. Eso obliga a que el criterio de "funciona la mayoría de las veces" no sea suficiente acá: el ordenamiento tiene que ser exacto siempre, porque el orden de la lista es, de hecho, quién recibe la llamada primero.

---
