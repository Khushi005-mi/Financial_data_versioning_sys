# Step 1 — Imports
from sqlalchemy.orm import Session
from models.dataset.py import Dataset
from datetime import datetime
# Step 2 — Create Dataset Registry Class
class DatasetRegistry:
    def __init__(self, db: Session):
        self.db = db
# Step 3 — Duplicate dataset detection (CRITICAL)
def duplicate_detection(self, source_name: str, file_name: str, checksum: str) -> bool:
    return (self.db.query(Dataset)
            .filter(checksum= checksum)
            .first()
            is not None
            )
        
# Step 4 — Create dataset record:
def create_dataset_record(self, source_name: str, file_name: str, checksum: str) -> Dataset:
    if self.dataset_exists(source_name, file_name, checksum):
        raise ValueError("Dataset already exists with the same checksum.")
    Dataset = Dataset(
        source_name = source_name,
        file_name = file_name,
        checksum = checksum,
        uploaded_at = datetime.utcnow()
        original_file_name = file_name
    )
    self.db.add(Dataset)
    self.db.commit()
    self.db.refresh(Dataset)

    return Dataset
# Step 5 — Fetch latest dataset by source
def fetch_latest_dataset_by_source(self, source_name: str) -> Dataset:
    return(self.db.query(Dataset))
.filter(Dataset.source_name == source_name
                    .order_by(Dataset.uploaded_at.desc)
                    .first()
                    )
return Dataset
    
# Step 6 — Fetch dataset by ID
def fetch_dataset_by_id(self, dataset_id: int) -> Dataset:
    return self.db.query(Dataset).filter(Dataset.id == dataset_id).first()
