### Maze Solver con A\*

Este proyecto consiste en resolver un laberinto usando el algoritmo de A\* (A estrella). El objetivo es encontrar el camino mas corto desde un punto de inicio "S" hasta un punto de salida "E", considerando posibles obstaculos como muros y diferentes tipos de terreno.

## Descripcion del problema

El laberinto esta representado como una matriz donde:

"#" representa un muro (no se puede pasar)

S es el punto de inicio

E es la meta o salida

" " (espacio en blanco) es un camino valido

"x" es un terreno inestable que cuesta mas cruzar

El objetivo es encontrar el camino mas corto desde S hasta E, considerando que los movimientos pueden tener diferentes costos. Por ejemplo, moverse hacia la izquierda o derecha cuesta 2, mientras que moverse hacia arriba o abajo cuesta 1.

## Algoritmo utilizado: A\*

Se uso el algoritmo A\* porque es eficiente y garantiza encontrar el camino de menor costo siempre que la heurística sea admisible. En este caso se uso la distancia Manhattan como heurística, ya que solo se permite moverse en 4 direcciones (arriba, abajo, izquierda, derecha).

# Como funciona A\* (resumen de estudiante):

Empieza desde el nodo inicial.

Explora los caminos posibles, elgiendo primero los que parecen mas prometedores segun el costo real + una estimacion (heurística).

Guarda la accion tomada en cada paso y el costo acumulado.

Cuando llega a la meta, reconstruye el camino usando los nodos padres.

## Modificaciones realizadas

Se agrego el registro de las acciones tomadas (ej. 'UP', 'RIGHT') para cada paso del camino.

Se implemento un sistema de costos diferente para las direcciones:

Movimientos horizontales (LEFT, RIGHT) cuestan 2.(esto como prueba para la primera pregunta del informe por lo general todos los movimientos valen 1)

Movimientos verticales (UP, DOWN) cuestan 1.

Se muestra el costo total real del camino, no solo la cantidad de pasos.

## Respuestas a preguntas importantes

# ¿Siempre encuentra el camino mas corto?

Sí, porque se usa una heurística admisible (distancia Manhattan) y los costos son positivos. A\* esta diseñado para encontrar el camino mas barato bajo esas condiciones.

# ¿Para que sirve la heurística?

Sirve para estimar cuanto falta para llegar a la meta. A\* combina esa estimacion con el costo real que ya llevas acumulado para decidir que camino probar primero.

# ¿Que pasa si cambio los costos?

El algoritmo tomara rutas diferentes si conviene evitar caminos mas caros. Por ejemplo, si moverse a la derecha cuesta 2, puede preferir dar una vuelta mas larga pero mas barata.

# Ejemplo de salida

Total cost: 14
Path to exit: [(None, (1, 1)), ('DOWN', (2, 1)), ('RIGHT', (2, 2)), ('RIGHT', (2, 3)), ('DOWN', (3, 3)), ('RIGHT', (3, 4)), ('RIGHT', (3, 5)), ('UP', (2, 5)), ('UP', (1, 5)), ('RIGHT', (1, 6))]

# ¿Que pasa si hay multiples salidas?

Si el laberinto tiene varias salidas posibles (por ejemplo varias E), el algoritmo tal como esta ahora solo busca una salida específica (la que se define como end = (fila, columna) en el código).

-Por lo cual si hay otras salidas incluso si estan a un solo paso las obviara pasando de largo de estas buscando solamente la salida que se le marca.

-Una posible solucion es que en vez de definir la salida manualmente, hacer un algoritmo para recorrer la matriz en busca de "E" y marcarlas como salidas de esta manera se tendrian en cuenta todas.

# ¿Que limitaciones tiene el algoritmo?

-Una limitacion que veo es y recalco el tema de las "E" pues el algoritmo solo sabe buscar desde un inicio marcado hasta una salida marcada provocando que no siempre se halle la salida mas rapida ya que A\* no busca la meta mas cercana solamente la ya definida.
