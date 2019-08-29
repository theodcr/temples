import string

import numpy as np
import pandas as pd

from temples import Data, PandasDataFrame, PickleData

from .config import env


class CSVData(Data):
    """Generic class to define data contained in CSV files."""

    def _load(self) -> pd.DataFrame:
        return pd.read_csv(self.path)

    def _write(self) -> None:
        self._data.to_csv(self.path, header=True)


class Features(CSVData, PandasDataFrame):
    """Specific class for features dataframe, containing its schema."""

    def __init__(self):
        super().__init__(path=env["features"], relative_to_config=True)
        self.schema = {key: np.dtype("float") for key in string.ascii_lowercase[:20]}


class TrainedModel(PickleData):
    def __init__(self) -> None:
        super().__init__(path=env["trained_model"], relative_to_config=True)


raw_data = CSVData(env["raw_data"], relative_to_config=True)
clean_features = Features()
clean_targets = CSVData(env["targets"], relative_to_config=True)
trained_model = TrainedModel()
