# Informe: Predicción de Precios de Casas con Aprendizaje Automático

## 1. Descripción del dataset
El dataset utilizado corresponde a un conjunto de **2000 registros** con información de viviendas.  
- **Variables**: 10 en total.  
  - `Id`: identificador único de la vivienda.  
  - `Area`: área en pies cuadrados.  
  - `Bedrooms`: número de habitaciones.  
  - `Bathrooms`: número de baños.  
  - `Floors`: número de pisos.  
  - `YearBuilt`: año de construcción.  
  - `Location`: ubicación de la vivienda.  
  - `Condition`: estado de la vivienda.  
  - `Garage`: indicador de si posee garaje.  
  - `Price`: **variable objetivo**, precio de la vivienda.  

**Objetivo del problema**: Construir un modelo predictivo que estime el precio de una vivienda a partir de sus características.

---

## 2. Preprocesamiento realizado

### a. Limpieza de datos faltantes
El dataset no presentaba valores nulos, por lo que no se realizaron imputaciones.

### b. Codificación de variables categóricas
Las variables `Location`, `Condition` y `Garage` fueron codificadas mediante **One-Hot Encoding**, generando variables binarias para representar cada categoría.

### c. Escalado/normalización
Las variables numéricas (`Area`, `Bedrooms`, `Bathrooms`, `Floors`, `YearBuilt`) fueron escaladas mediante **StandardScaler** para mejorar la estabilidad del entrenamiento de los modelos.

### d. División en train/test
El dataset fue dividido en:  
- **80% entrenamiento**  
- **20% prueba**  

---

## 3. Entrenamiento de los tres modelos

Se entrenaron tres enfoques diferentes para comparar su desempeño:

1. **Regresión Lineal**  
   - Parámetros: implementación estándar de `sklearn.linear_model.LinearRegression`.

2. **Random Forest Regressor**  
   - Parámetros principales: `n_estimators=100`, `max_depth=None`.  
   - Librería: `sklearn.ensemble.RandomForestRegressor`.

3. **Red Neuronal Artificial (ANN)**  
   - Implementada en TensorFlow/Keras.  
   - Arquitectura:
     - Capa densa de 128 neuronas, activación `ReLU`.  
     - Capa densa de 64 neuronas, activación `ReLU`.  
     - Capa densa de 32 neuronas, activación `ReLU`.  
     - Capa de salida de 1 neurona (regresión).  
   - Optimizador: `Adam`.  
   - Función de pérdida: `MSE`.  
   - Entrenamiento: 50 epochs, batch size de 32, validación del 20% del conjunto de entrenamiento.  

---

## 4. Evaluación de resultados

### a. Métricas de rendimiento
Se utilizaron las siguientes métricas para evaluar el desempeño de cada modelo:  
- **MAE (Mean Absolute Error)**  
- **MSE (Mean Squared Error)**  
- **R² (Coeficiente de determinación)**  

| Modelo                  | MAE        | MSE        | R²     |
|--------------------------|------------|------------|--------|
| Regresión Lineal         | ...        | ...        | ...    |
| Random Forest Regressor  | ...        | ...        | ...    |
| Red Neuronal             | ...        | ...        | ...    |

*(Los valores deben completarse con los resultados obtenidos en la ejecución).*

### b. Curvas o visualizaciones
Para la red neuronal se graficaron las curvas de **entrenamiento y validación** de `loss` y `MAE` por época, lo que permitió observar la convergencia del modelo.

---

## 5. Análisis comparativo

- **Regresión Lineal**: Modelo sencillo, rápido de entrenar, pero con limitaciones para capturar relaciones no lineales en los datos.  
- **Random Forest Regressor**: Buen desempeño en datasets tabulares, maneja no linealidad y categorías, pero puede ser más costoso computacionalmente.  
- **Red Neuronal Artificial**: Flexible y capaz de aprender representaciones complejas, aunque requiere más tiempo de entrenamiento y ajuste de hiperparámetros.  

---

## 6. Conclusiones

- El análisis comparativo permitió evidenciar que cada modelo tiene ventajas y limitaciones según el contexto.  
- Para este dataset, el modelo con mejor rendimiento fue **[indicar el modelo ganador]**, considerando el equilibrio entre error y capacidad de generalización.  
- Se concluye que el uso de técnicas de normalización y codificación de variables categóricas fue esencial para mejorar el desempeño de los modelos.  
- El proyecto permitió comprender el proceso completo de **preprocesamiento, entrenamiento y evaluación de modelos de machine learning aplicados a un problema de regresión**.  

---
