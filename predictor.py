import xgboost as xgb
import numpy as np
import os

model = None

try:
    model = xgb.XGBClassifier()
    model.load_model("model.json")
    print("✅ Modèle chargé avec succès")
except Exception as e:
    print(f"[ERREUR] Chargement du modèle : {e}")
    model = None

def predict_match(team_1_rating, team_2_rating):
    if model is None:
        return {"result": "Model not loaded"}

    try:
        input_data = np.array([[team_1_rating, team_2_rating]])
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]

        result_label = (
            "Team 1 wins" if prediction == 1 else
            "Team 2 wins" if prediction == 2 else
            "Draw"
        )

        return {
            "result": result_label,
            "probabilities": {
                "Team 1": round(probabilities[1] * 100, 2),
                "Team 2": round(probabilities[2] * 100, 2),
                "Draw": round(probabilities[0] * 100, 2)
            }
        }

    except Exception as e:
        print(f"[ERREUR] Prédiction échouée : {e}")
        return {"result": "Erreur de prédiction"}
