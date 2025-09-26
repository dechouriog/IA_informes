import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow import keras

# Cargar dataset
df = pd.read_csv("House Price Prediction Dataset.csv")

# Preprocesamiento
df = df.drop(columns=["Id"])  # no aporta información

# Separar X (features) y y (target)
X = df.drop(columns=["Price"])
y = df["Price"]

# One-hot encoding para variables categóricas
X = pd.get_dummies(X, columns=["Location", "Condition", "Garage"], drop_first=True)

# Normalización
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Separar train/test
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# red neuronal
model = keras.Sequential([
    keras.layers.Dense(128, activation="relu", input_shape=(X_train.shape[1],)),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(32, activation="relu"),
    keras.layers.Dense(1)  # salida para regresión
])

model.compile(optimizer="adam", loss="mse", metrics=["mae", "mse"])

# 5. Entrenamiento
history = model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=50,
    batch_size=32,
    verbose=1
)

# 6. Evaluación
loss, mae, mse = model.evaluate(X_test, y_test, verbose=0)
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")

# 7. Predicción de ejemplo
y_pred = model.predict(X_test[:5])
print("Predicciones:", y_pred.flatten())
print("Valores reales:", y_test.iloc[:5].values)
