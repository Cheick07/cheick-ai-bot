import xgboost as xgb
import numpy as np

# === Données d'entraînement avec 6 features ===
X = np.array([
    [85.0, 78.5, 5, 12, 2.1, 3.4],
    [70.0, 80.0, 15, 8, 3.8, 2.5],
    [90.0, 60.0, 2, 18, 1.9, 4.2],
    [65.0, 85.0, 20, 5, 4.5, 2.0],
    [88.0, 82.0, 3, 6, 2.2, 2.8]
])

y = np.array([1, 2, 1, 2, 0])  # 1 = Team 1 wins, 2 = Team 2 wins, 0 = Draw

model = xgb.XGBClassifier()
model.fit(X, y)

# === Sauvegarde du modèle ===
model.save_model("model.json")
print("✅ Modèle enrichi sauvegardé dans model.json")