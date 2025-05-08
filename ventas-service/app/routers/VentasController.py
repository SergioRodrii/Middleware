from fastapi import APIRouter, HTTPException
from typing import List
from app.models.Models import Producto

router = APIRouter()

@router.post("/registrarVenta", response_model=List[Producto])
def registrar_venta(productos: List[Producto]):
    try:        
        return 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))