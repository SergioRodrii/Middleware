from pydantic import BaseModel
from typing import List

# Definición de la clase Producto
class Producto(BaseModel):
    id: int
    nombreProducto: str
    precio: float
    cantidad: int

# Definición de la clase DTO para actualizar producto
class ActualizarProductoDTO(BaseModel):
    id: int
    cantidad: int
