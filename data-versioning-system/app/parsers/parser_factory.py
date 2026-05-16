import pandas as pd
from abc import ABC, abstractmethod

def get_parser(file_name: str) -> ABC:
    if file_name.endswith(".csv"):
        from .csv_parser import csvParser
        return csvParser()
    if file_name.endswith(".xlxs"):
        from .excel_parser import excelParser
        return csvParser()