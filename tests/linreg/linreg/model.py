import pandas as pd
from sklearn.linear_model import Ridge

from temples import benchmark, inputs, log, outputs, settings

from .data import clean_features, clean_targets, trained_model


@inputs(features=clean_features, targets=clean_targets)
@outputs(trained_model)
@log("Training linear regression model")
@benchmark
def train_linear_regression(
    features: pd.DataFrame, targets: pd.Series, alpha=settings["ridge"]["alpha"]
) -> Ridge:
    """Trains a ridge regression model on given data, returns the model."""
    model = Ridge(alpha)
    model.fit(features, targets)
    return model


if __name__ == "__main__":
    train_linear_regression()
