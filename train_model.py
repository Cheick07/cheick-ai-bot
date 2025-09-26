import xgboost as xgb
import numpy as np

# === Étape 1 : Données d'entraînement ===
# Chaque ligne représente : [team_1_rating, team_2_rating]
X = np.array([
    [85.0, 78.5],
    [70.0, 80.0],
    [90.0, 60.0],
    [65.0, 65.0],
    [88.0, 75.0],
    [72.0, 85.0],
    [80.0, 80.0]
])

# Labels : 1 = Team 1 wins, 2 = Team 2 wins, 0 = Draw
y = np.array([1, 2, 1, 0, 1, 2, 0])

# === Étape 2 : Entraînement du modèle ===
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric="mlogloss")
model.fit(X, y)

# === Étape 3 : Sauvegarde du modèle ===
model.save_model("model.json")
print("✅ Modèle entraîné et sauvegardé dans model.json")