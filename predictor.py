import xgboost as xgb
import numpy as np
import os

model = None

try:
    if os.path.exists("model.json"):
        model = xgb.XGBClassifier()
        model.load_model("model.json")
        print("✅ Modèle chargé avec succès")
    else:
        print("❌ model.json introuvable")
except Exception as e:
    print(f"[ERREUR] Chargement du modèle : {e}")
    model = None

def predict_match(team_1_rating, team_2_rating, team_1_rank, team_2_rank, team_1_odds, team_2_odds):
    if model is None:
        return {"result": "Model not loaded"}

    input_data = np.array([[team_1_rating, team_2_rating, team_1_rank, team_2_rank, team_1_odds, team_2_odds]])
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]

    return {
        "result": "Team 1 wins" if prediction == 1 else "Team 2 wins" if prediction == 2 else "Draw",
        "probabilities": {
            "Team 1": round(probabilities[1] * 100, 2),
            "Team 2": round(probabilities[2] * 100, 2),
            "Draw": round(probabilities[0] * 100, 2)
        }
    }