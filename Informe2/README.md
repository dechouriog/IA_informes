# Informe #X - Support Vector Regression (SVR)

## 1) Descripción del dataset

**Fuente:** Kaggle – House Price Prediction Dataset.  

**Formato:** CSV.  

**Número de registros:** 2000  

**Número de variables:** 10 (incluyendo la variable objetivo).  

### Variables

- **Id:** Identificador único de la vivienda. (irrelevante para la predicción)  
- **Area:** Área de la vivienda en pies cuadrados.  
- **Bedrooms:** Número de habitaciones.  
- **Bathrooms:** Número de baños.  
- **Floors:** Número de pisos.  
- **YearBuilt:** Año de construcción.  
- **Location:** Ubicación de la casa (ej. Downtown, Suburban).  
- **Condition:** Estado de la vivienda (Excellent, Good, Fair).  
- **Garage:** Indica si tiene garaje (Yes / No).  
- **Price:** Variable objetivo (target) → precio de la vivienda en dólares.  

El dataset se encontraba bien estructurado, sin valores nulos ni duplicados, con un target definido, lo que facilita su uso para tareas de aprendizaje supervisado.

---

## 2) Preprocesamiento realizado

### a) Limpieza de datos faltantes
- Se verificó la existencia de valores nulos.  
- Se eliminaron las filas con datos faltantes usando `dropna()`.  
- La columna **Id** fue eliminada por no aportar valor predictivo.  

### b) Codificación de variables categóricas
- Las variables categóricas (**Location**, **Condition**, **Garage**) fueron convertidas a variables numéricas mediante **One-Hot Encoding**.  
- Se usó `drop_first=True` para evitar multicolinealidad.  

### c) Escalado/normalización
- Se aplicó **MinMaxScaler** a las variables numéricas:  
  - *Area, Bedrooms, Bathrooms, Floors, YearBuilt*  
- Esto es importante porque **SVR se basa en distancias** y es sensible a la escala de las variables.  

### d) División en train/test
- Se dividió el dataset en:  
  - **80% entrenamiento** (X_train, y_train)  
  - **20% prueba** (X_test, y_test)  
- Se utilizó `train_test_split` con `random_state=42` para reproducibilidad.  

---

## 3) Entrenamiento del modelo

Se utilizó un **Support Vector Regressor (SVR)** de `scikit-learn` con los siguientes parámetros:  

- **kernel = "rbf"** → permite capturar relaciones no lineales.  
- **C = 100** → controla la penalización del error.  
- **gamma = 0.1** → define la influencia de cada punto de soporte.  
- **epsilon = 0.1** → margen de tolerancia al error.  

El modelo se entrenó con el conjunto de entrenamiento y posteriormente se evaluó con el conjunto de prueba.  

---

## 4) Evaluación de resultados

### a) Métricas de rendimiento
Se calcularon las siguientes métricas:  

- **MSE (Mean Squared Error):** mide el error cuadrático medio de las predicciones.  
- **R² (Coeficiente de determinación):** indica qué proporción de la variabilidad del precio es explicada por el modelo.  
- **MAE (Mean Absolute Error):** mide el error absoluto promedio de las predicciones.  

### b) Curvas o visualizaciones
Se realizaron dos gráficas principales:  

1. **Valores reales vs valores predichos:**  
   Permite comparar visualmente el desempeño del modelo.  
   Idealmente, los puntos deberían alinearse a la diagonal (predicción perfecta).  

2. **Distribución de errores:**  
   Histograma que muestra la dispersión de los errores de predicción.  

---

## 5) Análisis comparativo

Como se pudo apreciar por los valores de MSE y R^2, el modelo SVR no contó con un buen desempeño para este dataset, pues no está especializado para este tipo de predicciones, siendo casi tan efectivo a no tener modelo en general. En comparación a los demás modelos, este no contó con un buen desempeño, y considerando la posible carga que puede representar en cuanto a recursos no vale la pena hacer uso del mismo para este dataset en específico.

---

## 6) Conclusiones

- El modelo SVR logró capturar relaciones no lineales en los datos gracias al kernel RBF.  
- La normalización de las variables fue clave para que el modelo funcionara, pero no necesariamente garantizó éxito predictivo.  
- Aunque los resultados fueron bastante alejados a perfectos, SVR es una técnica "interesante" para datasets de tamaño pequeño a mediano, pero muy costosa para aquellos que cuenten con una mayor cantidad de filas.  
