import json
import httpx
#from typing import List
from app.models.Models import VentaDTO, CompraDTO


async def registrar_venta(venta: VentaDTO):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://gateway:8000/contabilidad/generarFactura/",
            json=venta
        )
        if response.status_code != 200:
            raise RuntimeError("Error al registrar la venta")
        return response.json()

async def registrar_compra(compra: CompraDTO):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://gateway:8000/contabilidad/recibirFactura/",
            json=compra
        )
        if response.status_code != 200:
            raise RuntimeError("Error al registrar la compra")
        return response.json()
