from pydantic import BaseModel
from typing import List

class Producto(BaseModel):
    id: int
    nombreProducto: str
    precio: float
    cantidad: int

class FacturaVenta(BaseModel):
    id: int
    nombre: str
    apellido: str
    dni: int
    telefono: int
    direccion: str
    productos: List[Producto]  
    total: float = 0.0

class FacturaCompra(BaseModel):
    id: int
    nombreProveedor: str
    telefono: int
    productos: List[Producto]
    total: float = 0.0
