from fastapi import FastAPI
from app.routers import VentasController

app = FastAPI()

# Registrar routers
app.include_router(VentasController.router, tags=["Ventas"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
