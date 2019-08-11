import string

import pandas as pd
from sklearn.datasets import make_regression

from temples import settings


def create_regression(
    n_samples=settings["make_regression"]["n_samples"]
) -> pd.DataFrame:
    X, y = make_regression(n_samples=n_samples, n_features=20, n_informative=5)
    features = pd.DataFrame(X, columns=list(string.ascii_lowercase[: X.shape[1]]))
    targets = pd.Series(y, name="target")
    return features, targets
