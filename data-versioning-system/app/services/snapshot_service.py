# app/services/snapshot_service.py

from app.snapshot_engine.snapshot_builder import build_snapshot


def rebuild_snapshot(dataset_id: int, df):
    build_snapshot(dataset_id, df)