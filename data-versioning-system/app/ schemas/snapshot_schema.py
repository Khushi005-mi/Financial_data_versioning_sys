# app/schemas/snapshot.py
from pydantic import BaseModel
from datetime import datetime

class SnapshotResponse(BaseModel):
    id: int
    dataset_id: int
    version: int
    created_at: datetime

    class Config:
        from_attributes = True