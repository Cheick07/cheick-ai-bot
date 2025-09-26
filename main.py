from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Cheick AI Bot")
app.include_router(router)
from fastapi import FastAPI
from api import router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de Cheick"}

app.include_router(router)