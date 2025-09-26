import xgboost as xgb
import numpy as np

# === Données d'entraînement avec 2 features ===
X = np.array([
    [85.0, 78.5],
    [70.0, 80.0],
    [90.0, 60.0],
    [65.0, 85.0],
    [88.0, 82.0]
])

y = np.array([1, 2, 1, 2, 0])  # 1 = Team 1 wins, 2 = Team 2 wins, 0 = Draw

model = xgb.XGBClassifier()
model.fit(X, y)

# === Sauvegarde du modèle ===
model.save_model("model.json")
print("✅ Modèle avec 2 features sauvegardé dans model.json")
