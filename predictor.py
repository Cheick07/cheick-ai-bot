import pickle
import numpy as np

# Chargement du modèle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_match(team_1_rating: float, team_2_rating: float) -> str:
    """
    Prédit le résultat d'un match entre deux équipes selon leurs ratings.
    Retourne 'Team 1 wins', 'Team 2 wins' ou 'Draw'.
    """
    features = np.array([[team_1_rating, team_2_rating]])
    prediction = model.predict(features)[0]

    if prediction == 1:
        return "Team 1 wins"
    elif prediction == 2:
        return "Team 2 wins"
    else:
        return "Draw"
