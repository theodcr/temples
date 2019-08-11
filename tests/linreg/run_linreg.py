import os

from linreg.data import RawData
from temples import env, settings

if __name__ == "__main__":
    print(os.environ["TEMPLES_CONFIG"])
    print(env())
    print(settings())
    raw_data = RawData()
    print(raw_data.path)
    print(raw_data.exists())
