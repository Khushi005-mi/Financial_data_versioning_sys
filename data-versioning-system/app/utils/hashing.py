import hashlib

def sha256_hash(text: str) -> str:
    """
    Core hashing primitive used across the entire system.
    Converts any string into a deterministic SHA256 hash.
    """
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def hash_row_dict(row: dict) -> str:
    """
    Create deterministic hash of a row dictionary.
    Sorting keys is CRITICAL to ensure stability.
    """
    # sort keys to make order deterministic
    items = sorted(row.items())
    
    # convert to string representation
    row_string = "|".join(f"{k}={v}" for k, v in items)
    
    return sha256_hash(row_string)
import pandas as pd

def hash_dataset(df: pd.DataFrame) -> str:
    """
    Create a single deterministic hash representing the entire dataset.
    This becomes the DATASET VERSION ID.
    """
    if "row_hash" not in df.columns:
        raise ValueError("DataFrame must contain 'row_hash' column before hashing")

    # sort hashes to make order independent
    sorted_hashes = sorted(df["row_hash"].tolist())
    
    # combine into single string
    dataset_string = "|".join(sorted_hashes)
    
    return sha256_hash(dataset_string)
def hash_file_bytes(file_bytes: bytes) -> str:
    """
    Hash raw uploaded file.
    Useful for deduplication before processing.
    """
    return hashlib.sha256(file_bytes).hexdigest()