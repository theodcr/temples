import pandas as pd

from temples import Data, PickleData, env


class RawCSVData(Data):
    """Base class to define raw data contained in CSV files in the "raw_data" directory.
    """

    def __init__(self, name: str) -> None:
        super().__init__(path=env["raw_data"] + name + ".csv", relative_to_config=True)

    def _load(self) -> pd.DataFrame:
        return pd.read_csv(self.path)

    def _write(self) -> None:
        self._data.to_csv(self.path, header=True)


class TrainedModel(PickleData):
    def __init__(self) -> None:
        super().__init__(path=env["trained_model"], relative_to_config=True)


raw_features = RawCSVData("features")
raw_targets = RawCSVData("targets")
trained_model = TrainedModel()
