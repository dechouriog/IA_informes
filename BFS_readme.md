# Comparación entre BFS e IDS

### 1. ¿Cómo exploran el espacio de estados?
- **BFS (Breadth-First Search):** explora primero todos los nodos de un nivel antes de pasar al siguiente.  
- **IDS (Iterative Deepening Search):** explora con profundidad limitada y repite la búsqueda aumentando el límite poco a poco.

---

### 2. ¿Qué algoritmo encuentra antes la solución?
- **BFS:** encuentra la solución más rápidamente porque sigue los niveles de manera ordenada.  
- **IDS:** puede tardar más porque repite varias veces las exploraciones al aumentar la profundidad.

---

### 3. ¿Qué pasa con la memoria que usan?
- **BFS:** consume mucha memoria, ya que guarda todos los nodos de cada nivel.  
- **IDS:** usa muy poca memoria, solo necesita almacenar el camino actual.

---

### 4. ¿Y en términos de tiempo?
- **BFS:** es más eficiente en tiempo si la solución está cerca de la raíz.  
- **IDS:** es menos eficiente en tiempo porque repite caminos al aumentar la profundidad.

---

### 5. Entonces, ¿cuál es mejor?
- Si la memoria no es un problema y quieres rapidez → **BFS**.  
- Si la memoria es limitada y puedes tolerar más tiempo → **IDS**.

### Comparación de BFS e IDS

| Criterio       | BFS                          | IDS                          | Observación |
|----------------|-----------------------------|-----------------------------|--------------|
| **Tiempo**     | 8.25 × 10⁻⁵ s               | 4.34 × 10⁻⁵ s               | IDS fue ligeramente más rápido |
| **Memoria actual** | 856 bytes                 | 1000 bytes                  | IDS consumió un poco más |
| **Memoria pico**   | 4656 bytes                | 4656 bytes                  | Ambos alcanzaron el mismo pico |

**Conclusión:** En este caso particular, IDS tuvo un tiempo de ejecución menor, aunque utilizó ligeramente más memoria actual que BFS. No obstante, en escenarios más grandes y complejos se espera que BFS consuma más memoria mientras que IDS incremente su tiempo de ejecución debido a la repetición de búsquedas en cada nivel.
