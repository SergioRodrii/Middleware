from fastapi import APIRouter, HTTPException
from typing import List
from app.models.Models import VentaDTO, CompraDTO
from app.services.VentaServices import registrar_venta, registrar_compra

router = APIRouter()

@router.post("/registrarVenta", response_model=VentaDTO)
def registrar_venta(venta: VentaDTO):
    try:        
        factura = registrar_venta(venta)
        return factura
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/registrarCompras", response_model=CompraDTO)
def registrar_compras(compra: CompraDTO):
    try:        
        factura = registrar_compra(compra)
        return factura
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))