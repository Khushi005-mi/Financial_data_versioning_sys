def apply_inserts(db, table_name, rows):
    """
    Insert new records into warehouse table.
    """
    for row in rows:
        db.execute(
            f"""
            INSERT INTO {table_name} (row_hash, data)
            VALUES (:row_hash, :data)
            """,
            {"row_hash": row["row_hash"], "data": row}
        )
def apply_updates(db, table_name, rows):
    """
    Update existing warehouse records.
    """
    for row in rows:
        db.execute(
            f"""
            UPDATE {table_name}
            SET data = :data
            WHERE row_hash = :row_hash
            """,
            {"row_hash": row["row_hash"], "data": row}
        )
def sync_warehouse(db, dataset_id, events):
    """
    Apply diff events to warehouse tables.
    """
    inserts = events["inserts"]
    updates = events["updates"]
    deletes = events["deletes"]

    table_name = "transactions"  # for MVP we start with one table

    apply_inserts(db, table_name, inserts)
    apply_updates(db, table_name, updates)
    apply_deletes(db, table_name, deletes)

    db.commit()