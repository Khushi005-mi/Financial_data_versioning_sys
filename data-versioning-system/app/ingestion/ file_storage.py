# 1) Generate safe file paths
# create /uploads/{source}/{date}/ folders
# generate unique filenames using UUID
# prevent path traversal attacks
from pathlib import Path

UPLOAD_DIR = Path("uploads")

import uuid
from datetime import datetime
from pathlib import Path
import re
from app.config.storage_config import UPLOAD_DIR


def sanitize_filename(filename: str) -> str:
    # remove path separators and unsafe characters
    filename = filename.replace("\\", "").replace("/", "") 
    filename = re.sub(r"[^a-zA-Z0-9_.-]", "_", filename)
    return filename.lower()

def create_directory(source: str) -> Path:
    today = datetime.utcnow().strftime("%Y-%m-%d")
    directory = UPLOAD_DIR / source / today
    directory.mkdir(parents= True, exist_ok= True)
    return directory

def generate_unique_filename(filename: str) -> str:
    unique_id = uuid.uuid4().hex
    sanitize_filename = sanitize_filename(filename)  
    return f"{unique_id}_{sanitize_filename}"

def generate_safe_file_path(source:str , filename: str):
    directory = create_directory(source)
    unique_filename = generate_unique_filename(filename)
    return directory / unique_filename


# 2) Save uploaded file
def save_uploaded_file(upload_file, destination: Path):
    with destination.open("wb") as buffer:
        for chunk in upload_file.file:
            buffer.write(chunk)
# Receive FastAPI UploadFile and persist to disk.
import hashlib
from fastapi import UploadFile
from pathlib import Path
from app.utils.storage import generate_safe_file_path  # if in same file, ignore
async def save_upload_file(file: UploadFile, source: str) -> dict:
    """
    Saves uploaded file to disk and returns metadata.
    """

    file_path: Path = generate_safe_file_path(source, file.filename)

    size = 0
    sha256 = hashlib.sha256()

    with open(file_path, "wb") as buffer:
        while chunk := await file.read(CHUNK_SIZE):
            size += len(chunk)
            sha256.update(chunk)
            buffer.write(chunk)

    await file.close()

    return {
        "file_path": str(file_path),
        "file_size": size,
        "checksum": sha256.hexdigest(),
        "original_filename": file.filename,
    }
# Must handle:

# chunk writing (large files)
# async safe writing
# file size limits (future)

# 3) Generate checksum (VERY IMPORTANT)
def generate_checksum(file_path: Path) -> str:
    sha256 = hashlib.sha256()
    with file_path.open("rb") as f:
        while_chunk = f.read(8192):
        sha256.update(chunk)
    return sha256.hexdigest()

# 4) Return storage metadata
def get_file_metadata(file_path: Path , original_filename: str) -> dict:
    return {
        "file_path": str(file_path),
        "file_size": file_path.stat().st_size,
        "checksum": generate_checksum(file_path),
        "original_filename": original_filename,
    }

# 5) Abstract storage backend (future proofing)
def save_file_to_storage(file_path: Path, destination: str):
    # For now, we just save to local disk
    # In future, this can be extended to save to S3, GCS, etc.
    pass
