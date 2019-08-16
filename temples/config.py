import os
from pathlib import Path
from typing import Any, Dict

import toml

if "TEMPLES_CONFIG" not in os.environ:
    raise KeyError(
        "You must set the environment variable TEMPLES_CONFIG to use this package"
    )
_base_temples_path = Path(os.environ["TEMPLES_CONFIG"])


def get_absolute_path(relative_path: str) -> Path:
    """Returns the full path for a path relative to the TEMPLES_CONFIG directory.

    Parameters
    ----------
    relative_path : str
    """
    return _base_temples_path / relative_path


class Configuration(object):
    """
    Loads a TOML configuration file and stores its content.

    Temples configuration files must be located in the directory given by the
    TEMPLES_CONFIG environment variable.

    Parameters
    ----------
    name : str
        name of the .toml file to load

    Attributes
    ----------
    _path : str
        path to the TOML configuration file
    _dict : Dict
        content of the configuration as a dictionary

    Usage
    -----
    Once the Configuration instance created, its content can be accessed as with
    a dictionary:
    >>> conf = Configuration("env")  # loads the env.toml file
    >>> conf()  # returns full content
    >>> conf["key"]
    >>> conf["section"]["variable"]
    """

    def __init__(self, name: str) -> None:
        self._path = get_absolute_path(name + ".toml")
        self._dict = self.load()

    def load(self) -> Dict:
        if self._path.exists():
            return dict(toml.load(self._path))
        return {}

    def __call__(self) -> Dict:
        return self._dict

    def __getitem__(self, key: str) -> Any:
        return self._dict[key]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} instance loaded from file {self._path}"


# define global configurations
env = Configuration("env")
settings = Configuration("settings")
