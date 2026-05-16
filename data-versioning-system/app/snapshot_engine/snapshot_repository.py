def snapshot_repository(db, dataset_id: int):
    from app.database.models.snapshot import Snapshot
    return db.query(Snapshot).filter(Snapshot.dataset_id == dataset_id).all()
