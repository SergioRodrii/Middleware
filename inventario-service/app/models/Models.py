from pydantic import BaseModel
from typing import List

class Producto(BaseModel):
    id: int
    nombreProducto: str
    precio: float
    cantidad: int

class ActualizarProductoDTO(BaseModel):
    id: int
    cantidad: int
