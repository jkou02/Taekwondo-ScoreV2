from fastapi import FastAPI
from app.routes import events
from app.db.database import database
from app.db.models import metadata
from sqlalchemy import create_engine
from contextlib import asynccontextmanager

# Crear la base de datos al inicio (solo para SQLite)
engine = create_engine("sqlite:///./events.db")
metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🔌 Conectando a la base de datos...")
    await database.connect()
    yield
    print("🔌 Desconectando de la base de datos...")
    await database.disconnect()

app = FastAPI(
    title="Combate API",
    description="API para recibir señales de jueces desde la app móvil",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(events.router)
