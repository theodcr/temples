import pandas as pd
from sklearn.linear_model import Ridge

from temples import inputs, outputs

from .data import raw_features, raw_targets, trained_model


@inputs(features=raw_features, targets=raw_targets)
@outputs(trained_model)
def train_linear_regression(features: pd.DataFrame, targets: pd.DataFrame) -> Ridge:
    model = Ridge()
    model.fit(features, targets)
    return model,
