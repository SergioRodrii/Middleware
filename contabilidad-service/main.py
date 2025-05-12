from fastapi import FastAPI
from app.routers import ContabilidadController

app = FastAPI()

app.include_router(ContabilidadController.router, prefix="/contabilidad", tags=["Contabilidad"])

app.get("/health")
def health_check():
    return {"status": "ok"}