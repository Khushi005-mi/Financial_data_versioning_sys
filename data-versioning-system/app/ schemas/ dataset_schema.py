# app/schemas/dataset.py
from pydantic import BaseModel
from datetime import datetime


# Incoming request when user registers dataset
class DatasetCreate(BaseModel):
    name: str
    source: str  # bank / tally / excel / payment_gateway


# API response after dataset created
class DatasetResponse(BaseModel):
    id: int
    name: str
    source: str
    created_at: datetime

    class Config:
        from_attributes = True