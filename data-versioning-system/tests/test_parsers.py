import pandas as pd
from app.parsers.file_parser import parse_file_to_dataframe
from pathlib import Path
def create_test_files():
    Path("tests/data").mkdir(exist_ok=True)

    df = pd.DataFrame([
        {"Txn ID": 1, "Amount": 100, "Category": "Food"},
        {"Txn ID": 2, "Amount": 250, "Category": "Travel"},
    ])

    df.to_csv("tests/data/sample.csv", index=False)
    df.to_excel("tests/data/sample.xlsx", index=False)
    def test_parse_csv():
    create_test_files()

    df = parse_file_to_dataframe("tests/data/sample.csv")

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert "txn_id" in df.columns
    assert "amount" in df.columns
    def test_parse_excel():
     df = parse_file_to_dataframe("tests/data/sample.xlsx")

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert "category" in df.columns
def test_unsupported_file():
    try:
        parse_file_to_dataframe("tests/data/sample.txt")
    except ValueError as e:
        assert "Unsupported file format" in str(e)

        
