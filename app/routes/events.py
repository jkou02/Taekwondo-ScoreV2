from fastapi import APIRouter
from app.models.event_models import EventIn

router = APIRouter()

@router.post("/events")
async def receive_event(event: EventIn):
    print("✅ Evento recibido:", event)
    return {
        "message": "Evento recibido correctamente",
        "event": event
    }
