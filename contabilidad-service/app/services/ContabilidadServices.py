import json
import os
import httpx
from app.models.Models import FacturaVenta, FacturaCompra

FACTURA_CLIENTE_FILE = "resources/facturas_clientes.json"
FACTURA_PROVEEDOR_FILE = "resources/facturas_proveedores.json"

async def generar_factura_service(factura: FacturaVenta) -> FacturaVenta:
    
    total = sum(p.precio * p.cantidad for p in factura.productos)
    factura.total = total

    
    facturas_existentes = []
    if os.path.exists(FACTURA_CLIENTE_FILE):
        with open(FACTURA_CLIENTE_FILE, "r", encoding="utf-8") as f:
            try:
                facturas_existentes = json.load(f)
            except json.JSONDecodeError:
                facturas_existentes = []

    
    facturas_existentes.append(factura.dict())
    with open(FACTURA_CLIENTE_FILE, "w", encoding="utf-8") as f:
        json.dump(facturas_existentes, f, indent=4, ensure_ascii=False)

   
    productos_actualizar = [
        {"id": p.id, "cantidad": p.cantidad} for p in factura.productos
    ]

    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"http://gateway:8080/inventario/actualizarInventario/2",
            json=productos_actualizar
        )
        if response.status_code != 200:
            raise RuntimeError("Error al actualizar inventario desde Contabilidad")

    return factura



async def recibir_factura_service(factura: FacturaCompra) -> FacturaCompra:
    
    total = sum(p.precio * p.cantidad for p in factura.productos)
    factura.total = total

    
    facturas_existentes = []
    if os.path.exists(FACTURA_PROVEEDOR_FILE):
        with open(FACTURA_PROVEEDOR_FILE, "r", encoding="utf-8") as f:
            try:
                facturas_existentes = json.load(f)
            except json.JSONDecodeError:
                facturas_existentes = []

    
    facturas_existentes.append(factura.dict())

    with open(FACTURA_PROVEEDOR_FILE, "w", encoding="utf-8") as f:
        json.dump(facturas_existentes, f, indent=4, ensure_ascii=False)

    
    productos_actualizar = [
        {"id": p.id, "cantidad": p.cantidad} for p in factura.productos
    ]

    
    async with httpx.AsyncClient() as client:
        response = await client.put(
            "http://gateway:8080/inventario/actualizarInventario/1", 
            json=productos_actualizar
        )
        if response.status_code != 200:
            raise RuntimeError("Error al actualizar el inventario")

    return factura