import pickle
from typing import Any

import pandas as pd

from temples import Data, env


class RawCSVData(Data):
    """Base class to define raw data contained in CSV files in the "raw_data" directory.
    """

    def __init__(self, name: str) -> None:
        super().__init__(path=env["raw_data"] + name + ".csv", relative_to_config=True)

    def load(self) -> pd.DataFrame:
        super().load()
        self._data = pd.read_csv(self.path)
        return self._data

    def write(self) -> None:
        super().write()
        self._data.to_csv(self.path, header=True)


class TrainedModel(Data):
    def __init__(self) -> None:
        super().__init__(path=env["trained_model"], relative_to_config=True)

    def load(self) -> Any:
        super().load()
        with open(self.path, "rb") as f:
            self._data = pickle.load(f)
        return self._data

    def write(self) -> None:
        super().write()
        with open(self.path, "wb") as f:
            pickle.dump(self._data, f)


raw_features = RawCSVData("features")
raw_targets = RawCSVData("targets")
trained_model = TrainedModel()
