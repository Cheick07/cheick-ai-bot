# === API FastAPI avec route /predict ===
from fastapi import FastAPI
from pydantic import BaseModel
from predictor import predict_match
from fastapi.middleware.cors import CORSMiddleware

# Initialisation de l'app FastAPI
app = FastAPI()

# Autoriser toutes les origines (utile pour frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Définition du modèle d'entrée
class MatchInput(BaseModel):
    team_1_rating: float
    team_2_rating: float

# Route POST /predict
@app.post("/predict")
def predict(input: MatchInput):
    return predict_match(input.team_1_rating, input.team_2_rating)
