from pydantic import BaseModel
from typing import List
from app.models import Producto

class VentaDTO(BaseModel):
    id: int
    nombre: str
    apellido: str
    dni: str
    telefono: str
    direccion: str
    productos: List[Producto]  

class CompraDTO(BaseModel):
    id: int
    nombre: str
    apellido: str
    dni: str
    telefono: str
    productos: List[Producto]

class Producto(BaseModel):
    id: int
    nombreProducto: str
    precio: float
    cantidad: int