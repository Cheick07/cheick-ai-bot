import xgboost as xgb
import numpy as np

# === Données d'entraînement ===
# Format : [team_1_rating, team_2_rating, team_1_rank, team_2_rank, team_1_odds, team_2_odds]
X = np.array([
    [85.0, 78.5, 5, 12, 2.1, 3.4],
    [70.0, 80.0, 15, 8, 3.8, 2.5],
    [90.0, 60.0, 2, 20, 1.9, 4.5],
    [65.0, 65.0, 10, 10, 3.0, 3.0],
    [88.0, 75.0, 4, 13, 2.2, 3.6],
    [72.0, 85.0, 14, 6, 3.5, 2.1],
    [80.0, 80.0, 9, 9, 2.9, 2.9]
])

# Labels : 1 = Team 1 wins, 2 = Team 2 wins, 0 = Draw
y = np.array([1, 2, 1, 0, 1, 2, 0])

# === Entraînement du modèle ===
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric="mlogloss")
model.fit(X, y)

# === Sauvegarde ===
model.save_model("model.json")
print("✅ Modèle enrichi sauvegardé dans model.json")