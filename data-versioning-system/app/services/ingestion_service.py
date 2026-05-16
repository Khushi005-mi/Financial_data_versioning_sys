from app.parsers.csv_parser import parse_csv
from app.parsers.excel_parser import parse_excel
from app.services.versioning_service import run_versioning

def ingest_data(file_path: str, dataset_id: int, db):
      if file_path.endswith(".csv"):
        df = parse_csv(file_path)

      elif file_path.endswith(".xlsx"):
        df = parse_excel(file_path)

      else:
        raise Exception("Unsupported file type")

    # Send parsed data to versioning stage
      run_versioning(dataset_id, df)