from pydantic import BaseModel, Field
from datetime import datetime

class EventIn(BaseModel):
    """
    - judge_id, str, ID del juez.
    - match_id, str, ID del combate en curso.
    - event_type, str, Tipo de punto.
    - timestamp, datetime, time del evento para comparar entre jueces.
    """
    
    judge_id: str = Field(..., example="judge_1")
    match_id: str = Field(..., example="match_abc")
    event_type: str = Field(
        ..., 
        example="kick_chest",
        description="Tipo de señal: kick_chest, kick_head, punch, spin_kick"
    )
    timestamp: datetime = Field(
        ..., 
        example="2025-06-25T21:32:00Z",
        description="Hora del evento en formato ISO 8601"
    )
    
    
