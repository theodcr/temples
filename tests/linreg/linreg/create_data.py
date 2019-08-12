import string
from typing import Tuple

import pandas as pd
from sklearn.datasets import make_regression

from temples import benchmark, log, outputs, settings

from .data import raw_features, raw_targets


@outputs(raw_features, raw_targets)
@log("Creating fake regression data")
@benchmark
def create_regression(
    n_samples=settings["make_regression"]["n_samples"]
) -> Tuple[pd.DataFrame, pd.Series]:
    """Creates a fake regression dataset with 20 features

    Parameters
    ----------
    n_samples : int
        number of samples to generate

    Returns
    -------
    - pd.DataFrame of features, feature names are lowercase letters
    - pd.Series of targets, name is "target"
    """
    X, y = make_regression(n_samples=n_samples, n_features=20, n_informative=5)
    features = pd.DataFrame(X, columns=list(string.ascii_lowercase[: X.shape[1]]))
    targets = pd.Series(y, name="target")
    return features, targets


if __name__ == "__main__":
    create_regression()
