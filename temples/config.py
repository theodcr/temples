import os
from pathlib import Path
from typing import Any, Dict

import toml


class Configuration(object):
    def __init__(self, name: str) -> None:
        self._path = Path(os.environ["TEMPLE_CONFIG"]) / (name + ".toml")
        self._dict = self.load()

    def load(self) -> Dict:
        if self._path.exists():
            return dict(toml.load(self._path))
        return {}

    def __call__(self) -> Dict:
        return self._dict

    def __getitem__(self, key) -> Any:
        return self._dict[key]


# define global configurations
env = Configuration("env")
settings = Configuration("settings")
