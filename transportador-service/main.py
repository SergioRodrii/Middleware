from fastapi import FastAPI
from app.routers import TransportadorController

app = FastAPI()

app.include_router(TransportadorController.router , tags=["Transportador"])

@app.get("/health")
def health_check():
    return {"status": "ok"}