import pandas as pd
from sklearn.linear_model import Ridge

from temples import inputs

from .data import raw_features, raw_targets


@inputs(features=raw_features, targets=raw_targets)
def train_linear_regression(features: pd.DataFrame, targets: pd.DataFrame) -> Ridge:
    model = Ridge()
    model.fit(features, targets)
    return model
