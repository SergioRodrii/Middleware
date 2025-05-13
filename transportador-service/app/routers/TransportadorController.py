from fastapi import APIRouter, HTTPException
from app.models.Models import Servicio
from app.services.TransportadorServices import guardar_servicio

router = APIRouter()

@router.post("/odenarTransporte", response_model= Servicio)
async def ordenar_transporte_service(servicio: Servicio):
    try:
        await guardar_servicio(servicio)
        return {"message": "Su pedido se esta preparando para ser enviado a su destino."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))