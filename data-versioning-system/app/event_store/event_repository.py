# app/event_store/repository.py

from sqlalchemy.orm import Session
from .models import FinancialEvent


def insert_events(db: Session, events: list[FinancialEvent]):
    db.add_all(events)
    db.commit()