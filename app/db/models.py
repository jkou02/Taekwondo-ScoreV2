from sqlalchemy import Table, Column, String, DateTime, MetaData, JSON
import uuid

metadata = MetaData()

events = Table(
    "events",
    metadata,
    Column("id", String, primary_key=True, default=lambda: str(uuid.uuid4())),
    Column("judge_id", String),
    Column("match_id", String),
    Column("event_type", String),
    Column("timestamp", DateTime)
)

validated_events = Table(
    "validated_events",
    metadata,
    Column("id", String, primary_key=True, default=lambda: str(uuid.uuid4())),
    Column("match_id", String),
    Column("event_type", String),
    Column("judges", JSON),  # lista de juez_id que coincidieron
    Column("validated_at", DateTime)
)