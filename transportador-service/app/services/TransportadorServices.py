import json
from typing import List
from app.models.Models import Servicio
import os

DB_PATH = "resources/facturas_transporte.json"

def cargar_servicios() -> List[Servicio]:
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, "r") as file:
        try:
            data = json.load(file)
            return [Servicio(**item) for item in data]
        except json.JSONDecodeError:
            return []

def guardar_servicio(servicio: Servicio):
    servicios = cargar_servicios()
    servicios.append(servicio)
    with open(DB_PATH, "w") as file:
        json.dump([s.dict() for s in servicios], file, indent=4)
