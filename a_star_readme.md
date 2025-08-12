# Análisis y aplicación del algoritmo A* en el problema de rutas en Rumanía

## 1. Análisis del problema
El problema consiste en encontrar la ruta de menos costosa entre dos ciudades dentro de un grafo que está representando el mapa de Rumanía.  

Para esto tenemos la siguiente estructura para poder modelar el sistema:
- **Nodos:** Son las ciudades, com lo son Arad, Sibiu o Bucharest.
- **Aristas:** Estas son las conexiones directas entre ciudades relacionadas.
- **Pesos:** En este caso representan la "distancia real" entre dos ciudades conectadas.

**Objetivo:**  
Lo que queremos hacer es poder encontrar la ruta más corta desde Arad hasta Bucharest, haciendo lo posible para minimizar la suma total de distancias recorridas.

Este problema se clasifica como búsqueda de caminos en grafos con costos asociados, que se puede reoslver haciendo uso de algoritmos best firs search o A*.

---

## 2. Aplicación del algoritmo A*
El algoritmo A\* usa dos valores para decidir a qué nodo se mueve en cada paso:

- **g(n):** Este es el costo que hay desde el nodo inicial hasta el nodo `n`, que es el nodo que se está "visitando"
- **h(n):** Es la heurística del costo desde `n` hasta el destino.  

La función de evaluación es:

\[
f(n) = g(n) + h(n)
\]

El proceso en el código:
1. La **frontera** se maneja como **cola de prioridad** usando `heapq`.
2. En cada iteración:
   - Se extrae el nodo con menor `f(n)`.
   - Se expande para generar nodos hijos (`expand`).
   - Se calcula su nuevo `g(n)` y `f(n)`.
   - Se añade a la frontera si es mejor que cualquier camino previo a ese nodo.
3. La búsqueda se detiene al alcanzar la meta.

---

## 3. Por qué la ruta encontrada es óptima
La optimalidad de A\* se puede asegurar si la heurística cumple:

* Nunca sobreestima el costo real hasta la meta.  
> En este caso, la distancia en línea recta entre dos ciudades siempre es menor o igual que la distancia real por carretera.

* Para dos nodos `n` y `n'` se asegure que la estimación desde `n` no es mayor que ir a `n'` más la estimación desde `n'` (f(n) = g(n) + h(n)).

Como la heurística cumple con esto, haciendo uso de A\* se puede garantizar que la primera vez que se alcanza la meta, se ha encontrado la ruta más corta posible.

---

## 4. Resultado encontrado
El algoritmo A\* da como resultado la siguiente ruta:
Solution path: ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']