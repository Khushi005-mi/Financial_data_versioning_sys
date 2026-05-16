from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database.base import Base

class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)
    source_name = Column(String, nullable=False)  # bank / excel / tally
    file_name = Column(String, nullable=False)
    checksum = Column(String, nullable=False)     # detect duplicates
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())