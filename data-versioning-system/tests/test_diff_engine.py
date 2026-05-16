# tests/test_diff_engine.py

import pandas as pd
from app.diff_engine.diff_engine import calculate_dataset_diff
old_data = pd.DataFrame([
    {"txn_id": 1, "amount": 100, "category": "Food"},
    {"txn_id": 2, "amount": 200, "category": "Travel"},
    {"txn_id": 3, "amount": 300, "category": "Bills"},
])
new_data = pd.DataFrame([
    {"txn_id": 1, "amount": 150, "category": "Food"},   # updated
    {"txn_id": 3, "amount": 300, "category": "Bills"},  # unchanged
    {"txn_id": 4, "amount": 500, "category": "Salary"}, # inserted
])
diff_result = calculate_dataset_diff(
    old_df=old_data,
    new_df=new_data,
    primary_key="txn_id"
)
print("\nINSERTED ROWS:")
print(diff_result["inserted"])

print("\nDELETED ROWS:")
print(diff_result["deleted"])

print("\nUPDATED ROWS:")
print(diff_result["updated"])
