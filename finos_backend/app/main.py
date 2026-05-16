from fastapi import FastAPI
from app.core.database import engine, Base
from app.api.routes_datasets import router as dataset_router

app = FastAPI(title="FinOS")

# create tables automatically (for now)
Base.metadata.create_all(bind=engine)

app.include_router(dataset_router)