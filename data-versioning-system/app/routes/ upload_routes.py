from fastapi import APIRouter, File, UploadFile
from app.services.ingestion.file_storage import save_upload_file

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Endpoint to handle file uploads.
    """
    try:
        metadata = await save_upload_file(file, source="upload")
        return {"message": "File uploaded successfully", "metadata": metadata}
    except Exception as e:
        return {"message": "Failed to upload file", "error": str(e)}
