import string

import pandas as pd
from sklearn.datasets import make_regression

from temples import output, settings

from .data import raw_features, raw_targets


def create_regression(
    n_samples=settings["make_regression"]["n_samples"]
) -> pd.DataFrame:
    X, y = make_regression(n_samples=n_samples, n_features=20, n_informative=5)
    features = pd.DataFrame(X, columns=list(string.ascii_lowercase[: X.shape[1]]))
    targets = pd.Series(y, name="target")
    return features, targets


@output(raw_features, raw_targets)
def main():
    return create_regression()