from fastapi import FastAPI
from app.routers import ProductosControllers

app = FastAPI()

app.include_router(ProductosControllers.router, tags=["Productos"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
