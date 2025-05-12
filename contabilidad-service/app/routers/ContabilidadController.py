from fastapi import APIRouter, HTTPException
from app.models.Models import FacturaVenta, FacturaCompra
from app.services.ContabilidadServices import generar_factura_service, recibir_factura_service

router = APIRouter()

@router.post("/generarFactura", response_model=FacturaVenta)
async def generar_factura(factura: FacturaVenta):
    try:
        facturaGenerada = await generar_factura_service(factura)
        return facturaGenerada
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/recibirFactura", response_model=FacturaCompra)
async def recibir_factura(factura: FacturaCompra):
    try:
        compraRegistrada = await recibir_factura_service(factura)
        return compraRegistrada
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))