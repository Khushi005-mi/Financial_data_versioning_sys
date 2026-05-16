import pandas as pd
from pathlib import Path

# core modules
from app.parsers.file_parser import parse_file_to_dataframe
from app.normalization.standardizer import standardize_dataframe
from app.diff_engine.diff_service import diff_datasets
from app.event_store.event_service import generate_events


def create_version_files():
    Path("tests/data").mkdir(exist_ok=True)

    # Version 1 dataset
    df_v1 = pd.DataFrame([
        {"Txn ID": 1, "Amount": 100, "Category": "Food"},
        {"Txn ID": 2, "Amount": 200, "Category": "Travel"},
        {"Txn ID": 3, "Amount": 300, "Category": "Bills"},
    ])

    # Version 2 dataset (simulate real change)
    df_v2 = pd.DataFrame([
        {"Txn ID": 1, "Amount": 100, "Category": "Food"},     # unchanged
        {"Txn ID": 2, "Amount": 250, "Category": "Travel"},   # updated
        {"Txn ID": 4, "Amount": 500, "Category": "Shopping"}, # new row
    ])

    df_v1.to_csv("tests/data/v1.csv", index=False)
    df_v2.to_csv("tests/data/v2.csv", index=False)


def test_full_pipeline():
    create_version_files()

    # STEP 1 — Parse files
    df1 = parse_file_to_dataframe("tests/data/v1.csv")
    df2 = parse_file_to_dataframe("tests/data/v2.csv")

    assert len(df1) == 3
    assert len(df2) == 3

    # STEP 2 — Normalize
    df1 = standardize_dataframe(df1)
    df2 = standardize_dataframe(df2)

    # STEP 3 — Diff detection
    diff_result = diff_datasets(df1, df2, primary_key="txn_id")

    assert "new_rows" in diff_result
    assert "deleted_rows" in diff_result
    assert "updated_rows" in diff_result

    # We expect:
    # 1 new row (txn_id 4)
    # 1 updated row (txn_id 2)
    # 1 deleted row (txn_id 3)

    assert len(diff_result["new_rows"]) == 1
    assert len(diff_result["updated_rows"]) == 1
    assert len(diff_result["deleted_rows"]) == 1

    # STEP 4 — Generate events
    events = generate_events(diff_result, dataset_id="test_dataset")

    assert len(events) == 3
    event_types = {e["event_type"] for e in events}

    assert "INSERT" in event_types
    assert "UPDATE" in event_types
    assert "DELETE" in event_types