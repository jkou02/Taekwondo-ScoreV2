from fastapi import APIRouter
from app.models.event_models import EventIn
from app.db.database import database
from app.db.models import events
from app.services.validation import verificar_evento
import uuid

router = APIRouter()

@router.post("/events")
async def receive_event(event: EventIn):
    # Guardar el evento recibido
    query = events.insert().values(
        id=str(uuid.uuid4()),
        judge_id=event.judge_id,
        match_id=event.match_id,
        event_type=event.event_type,
        timestamp=event.timestamp
    )
    await database.execute(query)

    # Verificar si coincide con otros jueces
    validado, jueces = await verificar_evento(event)

    return {
        "message": "Evento registrado",
        "validado": validado,
        "jueces_confirmantes": jueces if validado else []
    }
