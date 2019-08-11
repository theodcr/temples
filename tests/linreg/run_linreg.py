import os

from linreg.data import raw_features
from linreg.create_data import create_regression


if __name__ == "__main__":
    print(os.environ["TEMPLES_CONFIG"])
    print(raw_features.path)
    print(raw_features.exists())
    create_regression()
