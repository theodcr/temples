import logging
from pathlib import Path
from typing import List

from .config import get_absolute_path


class Data(object):
    """
    Defines a Data object: a wrapper around a given data stored on disk.
    Actual data is not loaded on instanciation.

    Parameters
    ----------
    path : str
        path to data, can be a file or a directory depending on how the data is loaded
    relative_to_config : bool = False
        set to True if `path` is relative to the TEMPLES_CONFIG directory

    Attributes
    ----------
    path : str
        path to the actual data on disk
    _data : Any
        actual loaded data

    Usage
    -----
    This class should be used to define classes specific to the application.
    For example:
    >>> class RawCSVData(Data):
    >>>     def __init__(self):
    >>>         super().__init__(path="../examples.csv", relative_to_config=True)
    >>>
    >>>     def load(self):
    >>>         self._data = pd.read_csv(self.path)
    >>>         return self._data
    >>>
    >>>     def write(self) -> None:
    >>>         super().write()
    >>>         self._data.to_csv(self.path)
    """

    def __init__(self, path: str, relative_to_config: bool = False) -> None:
        if relative_to_config:
            self.path = get_absolute_path(path)
        else:
            self.path = Path(path)
        self._data = None

    def load(self) -> None:
        raise NotImplementedError

    def write(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Writing {self.__class__.__name__} at {self.path.absolute()}")

    def exists(self) -> bool:
        return self.path.exists()


def output(*list_of_data: List[Data]):
    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            outputs = function(*args, **kwargs)
            for data, output in zip(list_of_data, outputs):
                data._data = output
                data.write()

        return wrapper

    return actual_decorator
