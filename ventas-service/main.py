from fastapi import FastAPI
from app.routers import VentasController

app = FastAPI()

# Registrar routers
app.include_router(VentasController.router, prefix="/ventas", tags=["Ventas"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
