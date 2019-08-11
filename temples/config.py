import os
from pathlib import Path
from typing import Any, Dict

import toml

_base_temples_path = Path(os.environ["TEMPLES_CONFIG"])


def get_absolute_path(path: str) -> Path:
    return _base_temples_path / path


class Configuration(object):
    def __init__(self, name: str) -> None:
        self._path = get_absolute_path(name + ".toml")
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
