from pydantic import BaseModel

class DatasetResponse(BaseModel):
    id: str
    file_name: str
    status: str

    class Config:
        orm_mode = True
        