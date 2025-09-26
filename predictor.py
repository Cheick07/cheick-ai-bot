import pickle
import numpy as np
import xgboost as xgb

try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    print(f"Erreur lors du chargement du modèle : {e}")
    model = None

def predict_match(team_1_rating: float, team_2_rating: float) -> str:
    if model is None:
        return "Model not loaded"

    try:
        features = np.array([[team_1_rating, team_2_rating]])
        prediction = model.predict(features)[0]

        if prediction == 1:
            return "Team 1 wins"
        elif prediction == 2:
            return "Team 2 wins"
        else:
            return "Draw"
    except Exception as e:
        print(f"Erreur pendant la prédiction : {e}")
        return "Prediction failed"
