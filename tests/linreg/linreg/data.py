import pandas as pd

from temples import Data, PickleData, env


class CSVData(Data):
    """Generic class to define data contained in CSV files."""

    def __init__(self, path: str) -> None:
        super().__init__(path=path, relative_to_config=True)

    def _load(self) -> pd.DataFrame:
        return pd.read_csv(self.path)

    def _write(self) -> None:
        self._data.to_csv(self.path, header=True)


class TrainedModel(PickleData):
    def __init__(self) -> None:
        super().__init__(path=env["trained_model"], relative_to_config=True)


raw_data = CSVData(env["raw_data"])
clean_features = CSVData(env["features"])
clean_targets = CSVData(env["targets"])
trained_model = TrainedModel()
