import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv("matches.csv")
X = df[['home_rank', 'away_rank', 'odds_home', 'odds_draw', 'odds_away']]
y = df['result']  # 1 = home win, 0 = draw, -1 = away win

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = xgb.XGBClassifier()
model.fit(X_train, y_train)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
