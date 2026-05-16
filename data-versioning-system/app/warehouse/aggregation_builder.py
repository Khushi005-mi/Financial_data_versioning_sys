def aggregation_building(db, dataset_id: int , aggregation_type: str):
    from app.database.models.snapshot import Snapshot
    from sqlalchemy import func

    if aggregation_type == "sum":
        return (
            db.query(func.sum(Snapshot.data ["amount"] as integer ))
            .filter(Snapshot.dataset_id == dataset_id)
            .scalar()
        )
    elif aggregation_type == "count":
        return (
            db.query(func.count(Snapshot.id))
            .filter(Snapshot.dataset_id == dataset_id)
            .scalar()
        )
    else:
        raise ValueError("Unsupported aggregation type")
    