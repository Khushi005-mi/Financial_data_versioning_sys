# app/services/warehouse_service.py

from sqlalchemy.orm import Session
from app.database.models.snapshot import Snapshot
from app.database.models.event import Event
from app.database.session import get_db
from sqlalchemy import func
def get_latest_snapshot(db: Session, dataset_id: int):
    return (
        db.query(Snapshot)
        .filter(Snapshot.dataset_id == dataset_id)
        .all()
    )

def get_event_history(db: Session, dataset_id: int):
    return (
        db.query(Event)
        .filter(Event.dataset_id == dataset_id)
        .order_by(Event.created_at.desc())
        .all()
    )
# 4) Time-travel query (key feature)
def time_travel_query(db: Session, dataset_id: int, timestamp:str):
    return (
        db.query(Snapshot)
        .filter(Snapshot.dataset_id == dataset_id)
        .filter(Snapshot.created_at <= timestamp)
        .order_by(Snapshot.created_at.desc())
        .first()
    )
# 5) Financial aggregation example
def Financial_aggregation(db: Session, dataset_id = int):
    return(
        db.query(func.sum(Snapshot.data["amount"].as_integer()))
        .filter(Snapshot.dataset_id == dataset_id)
        .scalar(Snapshot.dataset("amount"),("transactions"))
    )
# 6) Count records
def count_records(db: Session, dataset_id: int):
    return (
        db.query(func.count(Snapshot.id))
        .filter(Snapshot.dataset_id == dataset_id)
        .scalar()
    )

