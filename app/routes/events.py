from fastapi import APIRouter
from app.models.event_models import EventIn
from app.db.database import database
from app.db.models import events
import uuid

router = APIRouter()

@router.post("/events")
async def receive_event(event: EventIn):
    query = events.insert().values(
        id=str(uuid.uuid4()),
        judge_id=event.judge_id,
        match_id=event.match_id,
        event_type=event.event_type,
        timestamp=event.timestamp
    )
    await database.execute(query)

    return {
        "message": "Evento registrado correctamente",
        "event": event
    }
