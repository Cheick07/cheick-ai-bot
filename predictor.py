import pickle
import numpy as np

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_match(data):
    X = np.array([[data['home_rank'], data['away_rank'],
                   data['odds_home'], data['odds_draw'], data['odds_away']]])
    pred = model.predict_proba(X)[0]
    return {
        "home_win": round(pred[2], 3),
        "draw": round(pred[1], 3),
        "away_win": round(pred[0], 3)
    }
