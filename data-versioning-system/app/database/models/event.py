from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.sql import func
from app.database.base import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)

    dataset_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)

    event_type = Column(String, nullable=False)
    # INSERT | UPDATE | DELETE

    entity_id = Column(String, nullable=False)
    # unique transaction id from source

    event_data = Column(JSON, nullable=False)
    # full transaction payload

    created_at = Column(DateTime(timezone=True), server_default=func.now())