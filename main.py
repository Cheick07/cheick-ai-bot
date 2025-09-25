from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Cheick AI Bot")
app.include_router(router)
