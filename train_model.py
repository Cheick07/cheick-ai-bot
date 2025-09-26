import pandas as pd
import xgboost as xgb
import pickle

# Données fictives
data = {
    'home_rank': [5, 10, 3],
    'away_rank': [20, 15, 8],
    'odds_home': [1.8, 2.1, 1.5],
    'odds_draw': [3.2, 3.0, 3.5],
    'odds_away': [4.5, 3.8, 5.0],
    'result': [1, 0, -1]  # 1 = home win, 0 = draw, -1 = away win
}

df = pd.DataFrame(data)

# Remapper les classes : -1 → 0, 0 → 1, 1 → 2
df['result'] = df['result'].map({-1: 0, 0: 1, 1: 2})

X = df[['home_rank', 'away_rank', 'odds_home', 'odds_draw', 'odds_away']]
y = df['result']

model = xgb.XGBClassifier()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Modèle entraîné et sauvegardé dans model.pkl")
import pandas as pd
import xgboost as xgb
import pickle

# Données fictives
data = {
    'home_rank': [5, 10, 3],
    'away_rank': [20, 15, 8],
    'odds_home': [1.8, 2.1, 1.5],
    'odds_draw': [3.2, 3.0, 3.5],
    'odds_away': [4.5, 3.8, 5.0],
    'result': [1, 0, -1]  # 1 = home win, 0 = draw, -1 = away win
}

df = pd.DataFrame(data)

# Remapper les classes : -1 → 0, 0 → 1, 1 → 2
df['result'] = df['result'].map({-1: 0, 0: 1, 1: 2})

X = df[['home_rank', 'away_rank', 'odds_home', 'odds_draw', 'odds_away']]
y = df['result']

model = xgb.XGBClassifier()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Modèle entraîné et sauvegardé dans model.pkl")