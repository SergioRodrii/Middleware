from pydantic import BaseModel

class Servicio(BaseModel):
    id: int
    nombre: str
    apellido: str
    dni: int
    telefono: int
    direccion: str
    precio: float