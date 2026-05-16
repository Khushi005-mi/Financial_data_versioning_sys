# app/schemas/event.py
from pydantic import BaseModel
from datetime import datetime


class EventResponse(BaseModel):
    id: int
    dataset_id: int
    event_type: str  # INSERT / UPDATE / DELETE
    record_id: str
    created_at: datetime
