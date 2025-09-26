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

def predict_match(team_1_rating: float, team_2_rating: float):
    if model is None:
        return {"prediction": "Model not loaded"}

    input_data = np.array([[team_1_rating, team_2_rating]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        return {"result": "Team 1 wins"}
    elif prediction == 2:
        return {"result": "Team 2 wins"}
    else:
        return {"result": "Draw"}