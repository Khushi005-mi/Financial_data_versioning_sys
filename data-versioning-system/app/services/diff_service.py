from app.database.models.snapshot import Snapshot

def difference_services(db, dataset_id: int, timestamp1: str, timestamp2: str):
    snapshot1 = db.query(Snapshot).filter(
        Snapshot.dataset_id == dataset_id,
        Snapshot.created_at <= timestamp1
    ).order_by(Snapshot.created_at.desc()).first()

    snapshot2 = db.query(Snapshot).filter(
        Snapshot.dataset_id == dataset_id,
        Snapshot.created_at <= timestamp2
    ).order_by(Snapshot.created_at.desc()).first()

    if not snapshot1 or not snapshot2:
        return {"error": "One or both snapshots not found for the given timestamps."}

    # Assuming data is stored as JSON and we want to compare them
    data1 = snapshot1.data
    data2 = snapshot2.data

    # Simple difference calculation (this can be more complex based on the data structure)
    added = {k: v for k, v in data2.items() if k not in data1}
    removed = {k: v for k, v in data1.items() if k not in data2}
    modified = {k: {"old": data1[k], "new": data2[k]} for k in data1 if k in data2 and data1[k] != data2[k]}

    return {
        "added": added,
        "removed": removed,
        "modified": modified
    }