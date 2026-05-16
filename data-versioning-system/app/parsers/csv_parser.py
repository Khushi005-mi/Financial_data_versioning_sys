import pandas as pd
from abc import ABC, abstractmethod


class csvParser(ABC):

    @abstractmethod
    def parse(self, file_path: str) -> pd.DataFrame:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.stripe()
        df.dropna(inplace=True)
        return df