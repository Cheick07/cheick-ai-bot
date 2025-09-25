from fastapi import APIRouter
from model.predictor import predict_match

router = APIRouter()

@router.post("/predict")
def get_prediction(data: dict):
    return predict_match(data)
