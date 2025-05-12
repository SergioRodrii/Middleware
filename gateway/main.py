# gateway/main.py
from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import httpx

app = FastAPI()

# Mapeo de prefijos de ruta a la URL de cada micro‑servicio
SERVICE_MAP = {
    "/tienda":      "http://tienda-service:8081",
    "/inventario":  "http://inventario-service:8082",
    "/ventas":      "http://ventas-service:8083",
    "/contabilidad":"http://contabilidad-service:8084",
    "/proveedores": "http://proveedores-service:8085",
    "/transportador":"http://transportador-service:8086",
}

class ProxyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        
        for prefix, upstream in SERVICE_MAP.items():
            if path.startswith(prefix):
                
                suffix = path[len(prefix):] or "/"
                target_url = f"{upstream}{suffix}"
                
                async with httpx.AsyncClient() as client:
                    proxied = await client.request(
                        request.method,
                        target_url,
                        params=request.query_params,
                        headers=request.headers.raw,
                        content=await request.body()
                    )
                
                return Response(
                    content=proxied.content,
                    status_code=proxied.status_code,
                    headers=proxied.headers
                )
        
        return await call_next(request)


app.add_middleware(ProxyMiddleware)


@app.get("/health")
async def health():
    return {"status": "gateway up"}
