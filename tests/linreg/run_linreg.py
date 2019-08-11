import os

from temples import env, settings

if __name__ == "__main__":
    print(os.environ["TEMPLE_CONFIG"])
    print(env())
    print(settings())
