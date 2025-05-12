import json
import httpx
#from typing import List
from app.models.Models import VentaDTO, CompraDTO


async def registrar_venta_service(venta: VentaDTO):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://gateway:8080/contabilidad/generarFactura",
            json=venta.dict()
        )

        print("Status:", response.status_code)
        print("Contenido:", response.text)

        if response.status_code != 200:
            raise RuntimeError("Error al registrar la venta")
        return response.json()

async def registrar_compra_service(compra: CompraDTO):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://gateway:8080/contabilidad/recibirFactura",
            json=compra.dict()
        )
        if response.status_code != 200:
            raise RuntimeError("Error al registrar la compra")
        return response.json()
