from fastapi import APIRouter, HTTPException
from typing import List
from app.services.ProductosServices import cargar_inventario, actualizar_cantidad_producto, cargar_requerimientos
from app.models.Models import Producto, ActualizarProductoDTO

router = APIRouter()

# Endpoint para cargar los productos del inventario
@router.get("/cargarProductos", response_model=List[Producto])
def cargar_productos():
    try:
        return cargar_inventario()
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para actualizar el inventario
@router.put("/actualizarInventario/{numero}", response_model=List[Producto])
def actualizar_inventario(productos_actualizar: List[ActualizarProductoDTO], numero: int):
    try:
        return actualizar_cantidad_producto(productos_actualizar, numero)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para cargar los requerimientos de productos
@router.get("/cargarRequerimientosProductos", response_model=List[Producto])
def cargar_requerimientos_productos():
    try:
        return cargar_requerimientos()
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))