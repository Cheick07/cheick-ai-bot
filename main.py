from fastapi import FastAPI
from pydantic import BaseModel
from predictor import predict_match
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MatchInput(BaseModel):
    team_1_rating: float
    team_2_rating: float

@app.post("/predict")
def predict(input: MatchInput):
    return predict_match(input.team_1_rating, input.team_2_rating)
