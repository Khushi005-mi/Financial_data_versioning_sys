import pandas as pd
from app.snapshot_engine.snapshot_service import rebuild_snapshot


def create_sample_events():
    # Simulated event log (what event_store would produce)
    return [
        {
            "event_type": "INSERT",
            "primary_key": 1,
            "data": {"txn_id": 1, "amount": 100, "category": "Food"},
        },
        {
            "event_type": "INSERT",
            "primary_key": 2,
            "data": {"txn_id": 2, "amount": 200, "category": "Travel"},
        },
        {
            "event_type": "UPDATE",
            "primary_key": 2,
            "data": {"txn_id": 2, "amount": 250, "category": "Travel"},
        },
        {
            "event_type": "DELETE",
            "primary_key": 1,
            "data": None,
        },
        {
            "event_type": "INSERT",
            "primary_key": 3,
            "data": {"txn_id": 3, "amount": 500, "category": "Shopping"},
        },
    ]


def test_snapshot_rebuild():
    events = create_sample_events()

    snapshot_df = rebuild_snapshot(events)

    # Convert to dict for easier assertions
    records = snapshot_df.to_dict(orient="records")

    # Expected final state:
    # txn_id 1 -> deleted
    # txn_id 2 -> updated to 250
    # txn_id 3 -> inserted

    assert len(records) == 2

    txn_ids = {r["txn_id"] for r in records}
    assert txn_ids == {2, 3}

    # Verify update applied
    for r in records:
        if r["txn_id"] == 2:
            assert r["amount"] == 250