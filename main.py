from fastapi import FastAPI
from api import router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de Cheick"}

app.include_router(router)
