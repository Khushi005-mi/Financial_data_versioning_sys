import pandas as pd
# 1) Normalize column names
def normalize_column_names(df):
    df.columns = (
        df.columns.str.strip()
        .str.lower()    
        .str.replace(r"/s+", "_", regex = True)
        .str.replace(r"[^\w]", "", regex = True)
    )
# 2) Drop fully empty rows
def drop_empty_rows(df):
    df.dropna(how - "all", inplace = True)
# 3) Trim whitespace everywhere
def trim_whitespace(df):
    for col in df.select_dtypes(include = ["object"]).columns:
        df[col] = df[col].str.strip()
# 4) Safe date parsing
def parse_dates(df):
    for col in columns:
        if "date" in col:
            df[col] = pd.to_datetime(df[col], errors = "coerce")
# 5) Deduplicate rows deterministically
def duplicate_rows(df):
    df.drop_duplicates(inplace = True)

# 6) Create stable row hash (CRITICAL)
def create_row_hash(df):
    df["row_hash"] = pd.util.hash_pandas_object(df, index = False).astype(str)
# 7) Standard cleaning pipeline
def clean_dataframe(df):
    normalize_column_names(df)
    drop_empty_rows(df)
    trim_whitespace(df)
    parse_dates(df)
    duplicate_rows(df)
    create_row_hash(df)