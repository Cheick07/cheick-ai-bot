import xgboost as xgb
import numpy as np

# Chargement du modèle
try:
    model = xgb.XGBClassifier()
    model.load_model("model.json")
except Exception as e:
    print(f"[ERREUR] Chargement du modèle : {e}")
    model = None

# Fonction de prédiction
def predict_match(team_1_rating: float, team_2_rating: float) -> str:
    if model is None:
        return "Model not loaded"

    try:
        features = np.array([[team_1_rating, team_2_rating]])
        prediction = model.predict(features)
        result = prediction[0]

        if result == 1:
            return "Team 1 wins"
        elif result == 2:
            return "Team 2 wins"
        else:
            return "Draw"
    except Exception as e:
        print(f"[ERREUR] Prédiction : {e}")
        return "Prediction failed"
