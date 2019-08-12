import string
from typing import Tuple

import pandas as pd
from sklearn.datasets import make_regression

from temples import log, outputs, settings

from .data import raw_features, raw_targets


@outputs(raw_features, raw_targets)
@log("Creating fake regression data")
def create_regression(
    n_samples=settings["make_regression"]["n_samples"]
) -> Tuple[pd.DataFrame, pd.Series]:
    X, y = make_regression(n_samples=n_samples, n_features=20, n_informative=5)
    features = pd.DataFrame(X, columns=list(string.ascii_lowercase[: X.shape[1]]))
    targets = pd.Series(y, name="target")
    return features, targets
