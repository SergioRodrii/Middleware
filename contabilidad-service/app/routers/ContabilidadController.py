from fastapi import APIRouter, HTTPException
from app.models.Models import FacturaVenta, FacturaCompra
from app.services.ContabilidadServices import generar_factura_service, recibir_factura_service

router = APIRouter()

@router.post("/generarFactura", response_model=FacturaVenta)
def generar_factura(factura: FacturaVenta):
    try:
        facturaGenerada = generar_factura_service(factura)
        return facturaGenerada
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/recibirFactura", response_model=FacturaCompra)
def recibir_factura(factura: FacturaCompra):
    try:
        compraRegistrada = recibir_factura_service(factura)
        return compraRegistrada
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))