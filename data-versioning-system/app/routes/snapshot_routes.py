from fastapi import APIRouter, File, UploadFile
from app.services.ingestion.file_storage import save_upload_file

router = APIRouter()

@router.post("/upload")
async def snapshot_file(file: UploadFile = File(...)):
    """
    Endpoint to handle file snapshots.
    """
    try:
        snapshot_file = await save_file_snapshot(file, source="upload")
        return {"message": "File snapped successfully", "snapshot_file":snapshot_file}
    except Exception as e:
        return {"message": "Failed to take snap of file", "error": str(e)}
