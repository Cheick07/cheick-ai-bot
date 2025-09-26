from fastapi import APIRouter
from pydantic import BaseModel
from predictor import predict_match

router = APIRouter()

class MatchInput(BaseModel):
    team_1_rating: float
    team_2_rating: float

@router.post("/predict")
def predict(input: MatchInput):
    result = predict_match(input.team_1_rating, input.team_2_rating)
    return {"prediction": result}
