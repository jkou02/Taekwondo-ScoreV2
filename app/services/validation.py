from app.db.database import database
from app.db.models import events, validated_events
from sqlalchemy import and_, select
from datetime import timedelta, datetime
import uuid

MARGIN_MS = 300  # margen de coincidencia ±300ms

async def verificar_evento(evento):
    """Verifica si hay coincidencias con otros jueces"""
    margen_inferior = evento.timestamp - timedelta(milliseconds=MARGIN_MS)
    margen_superior = evento.timestamp + timedelta(milliseconds=MARGIN_MS)

    # Buscar eventos del mismo tipo, mismo match, dentro del margen
    query = select(events).where(
        and_(
            events.c.match_id == evento.match_id,
            events.c.event_type == evento.event_type,
            events.c.timestamp >= margen_inferior,
            events.c.timestamp <= margen_superior,
            events.c.judge_id != evento.judge_id  # otros jueces
        )
    )
    resultados = await database.fetch_all(query)

    if len(resultados) >= 1:  # al menos otro juez coincide
        judge_ids = list(set([evento.judge_id] + [r["judge_id"] for r in resultados]))

        # Insertar evento validado
        insert_query = validated_events.insert().values(
            id=str(uuid.uuid4()),
            match_id=evento.match_id,
            event_type=evento.event_type,
            judges=judge_ids,
            validated_at=datetime.utcnow()
        )
        await database.execute(insert_query)
        return True, judge_ids

    return False, []
