from fastapi import FastAPI
from app.routes import events

app = FastAPI(
    title="Combate API",
    description="API para recibir señales de jueces desde la app móvil",
    version="1.0.0"
)

app.include_router(events.router)