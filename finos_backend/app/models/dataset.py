import uuid
from sqlalchemy import Column, String, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import Base

class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    file_name = Column(Text, nullable=False)
    upload_time = Column(TIMESTAMP, server_default=func.now())
    source = Column(Text)
    status = Column(Text, default="uploaded")