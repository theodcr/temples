import pandas as pd

from temples import Data, env


class RawCSVData(Data):
    """Base class to define raw data contained in CSV files in the "raw_data" directory.
    """

    def __init__(self, name: str) -> None:
        super().__init__(path=env["raw_data"] + name + ".csv", relative_to_config=True)

    def load(self) -> pd.DataFrame:
        self._data = pd.read_csv(self.path)
        return self._data

    def write(self) -> None:
        self._data.to_csv(self.path)


raw_features = RawCSVData("features")
raw_targets = RawCSVData("targets")
