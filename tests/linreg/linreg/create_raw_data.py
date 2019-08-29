import string

import pandas as pd
from sklearn.datasets import make_regression

from temples import benchmark, log, outputs

from .config import settings
from .data import raw_data


@outputs(raw_data)
@log("Creating fake regression data")
@benchmark
def create_regression(
    n_samples=settings["make_regression"]["n_samples"]
) -> pd.DataFrame:
    """Creates a fake regression dataset with 20 features

    Parameters
    ----------
    n_samples : int
        number of samples to generate

    Returns
    -------
    pd.DataFrame of features and targets:
        feature names are lowercase letters, targets are in the column "target"
    """
    X, y = make_regression(n_samples=n_samples, n_features=20, n_informative=5)
    features = pd.DataFrame(X, columns=list(string.ascii_lowercase[: X.shape[1]]))
    targets = pd.Series(y, name="target")
    data = features.join(targets)
    return data


if __name__ == "__main__":
    create_regression()
