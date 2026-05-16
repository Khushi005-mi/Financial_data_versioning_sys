from sqlalchemy import Column, String, DateTime, JSON, Enum
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.database.base import Base
from app.diff_engine.diff_models import ChangeType

class financialevent(Base):
    __tablename__ = "financial_events"

    id = Column(UUID(as_uuid=True), primary_key=True, default= uuid.uuid4)
    event_type = Column(Enum(ChangeType), nullable=False)
    timestamp = Column(DateTime, default= datetime.utcnow)
    data = Column(JSON, nullable=False)
    change_type = Column(String, nullable= False)
    row_data = Column(JSON, nullable=False)