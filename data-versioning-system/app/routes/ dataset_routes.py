
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_datasets():
    return {"message": "Dataset listing endpoint (coming next)"}
