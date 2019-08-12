from typing import Tuple

import pandas as pd

from temples import benchmark, inputs, log, outputs

from .data import clean_features, clean_targets, raw_data


@inputs(raw_data=raw_data)
@outputs(clean_features, clean_targets)
@log("Cleaning data")
@benchmark
def clean(raw_data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """Cleans raw data and split it in features and targets.

    Returns
    -------
    pd.DataFrame of features and targets:
        feature names are lowercase letters, targets are in the column "target"
    """
    features = raw_data.drop("target", axis=1)
    targets = raw_data["target"]
    return features, targets


if __name__ == "__main__":
    clean()
