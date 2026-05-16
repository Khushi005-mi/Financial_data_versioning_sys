import pandas as pd
from abc import ABC, abstractmethod


class BaseParser(ABC):

    @abstractmethod
    def parse(self, file_path: str) -> pd.DataFrame:
        pass
    