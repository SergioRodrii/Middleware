import json
from typing import List
from app.models.Models import Producto, ActualizarProductoDTO

INVENTARIO_PATH = "resources/inventario.json"
REQUERIMIENTOS_PATH = "resources/requerimientos.json"

def cargar_inventario() -> List[Producto]:
    try:
        with open(INVENTARIO_PATH, "r") as file:
            inventario = json.load(file)
            return [Producto(**producto) for producto in inventario]
    except Exception as e:
        raise RuntimeError("Error leyendo inventario.json") from e


def actualizar_cantidad_producto(productos_actualizar: List[ActualizarProductoDTO], numero: int) -> List[Producto]:
    try:
        inventario = cargar_inventario()

        for actualizacion in productos_actualizar:
            for p in inventario:
                if p.id == actualizacion.id:
                    if numero == 1:  
                        nueva_cantidad = p.cantidad + actualizacion.cantidad
                        p.cantidad = max(nueva_cantidad, 0)
                    else:  
                        nueva_cantidad = p.cantidad - actualizacion.cantidad
                        p.cantidad = max(nueva_cantidad, 0)
                    break

        # Guardar los cambios en el archivo JSON
        with open(INVENTARIO_PATH, "w") as file:
            json.dump([prod.dict() for prod in inventario], file, indent=4)

        return inventario
    except Exception as e:
        raise RuntimeError("Error actualizando inventario.json") from e


def cargar_requerimientos() -> List[Producto]:
    try:
        with open(REQUERIMIENTOS_PATH, "r") as file:
            requerimientos = json.load(file)
            return [Producto(**producto) for producto in requerimientos]
    except Exception as e:
        raise RuntimeError("Error leyendo requerimientos.json") from e