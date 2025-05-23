from fastapi import APIRouter, HTTPException
from typing import List
from app.models.Models import VentaDTO, CompraDTO
from app.services.VentaServices import registrar_venta_service, registrar_compra_service

router = APIRouter()

@router.post("/registrarVentas", response_model=VentaDTO)
async def registrar_venta(venta: VentaDTO):
    try:        
        ventaRegistrada = await registrar_venta_service(venta)
        return ventaRegistrada
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/registrarCompras", response_model=CompraDTO)
async def registrar_compras(compra: CompraDTO):
    try:        
        compraRegistrada = await registrar_compra_service(compra)
        return compraRegistrada
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))