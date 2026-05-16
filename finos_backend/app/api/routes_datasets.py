import shutil
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.dataset import Dataset

router = APIRouter(prefix="/datasets", tags=["Datasets"])

UPLOAD_DIR = "uploads/"

@router.post("/upload")
def upload_dataset(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # 1) Save file locally
    file_path = UPLOAD_DIR + file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 2) Create DB row
    dataset = Dataset(
        file_name=file.filename,
        source="manual_upload",
        status="uploaded"
    )

    db.add(dataset)
    db.commit()
    db.refresh(dataset)

    return {
        "message": "File uploaded successfully",
        "dataset_id": dataset.id
    }