import logging
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

from .config import get_absolute_path


class Data(ABC):
    """
    Defines a Data object: a wrapper around a given data stored on disk.
    Actual data is not loaded on instantiation.

    This is an abstract base class, this class should be used to define Data classes
    specific to the application.
    Methods `load` and `write` must be overridden, it is also advised to override
    the `__init__` method. See Usage section for an example.

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
    >>> class RawCSVData(Data):
    >>>     def __init__(self):
    >>>         super().__init__(path="../examples.csv", relative_to_config=True)
    >>>
    >>>     def load(self):
    >>>         super().load()
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

    @abstractmethod
    def load(self) -> None:
        logging.info(f"Loading {self.__class__.__name__} from {self.path.resolve()}")

    @abstractmethod
    def write(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Writing {self.__class__.__name__} at {self.path.resolve()}")

    def exists(self) -> bool:
        return self.path.exists()


def output(*list_of_data: List[Data]):
    """
    Returns a decorator that maps the outputs of the decorated function
    to Data objects. After decorated function call, the outputs are written to disk
    using their write method.

    Parameters
    ----------
    *list_of_data : List[Data]
        ordered list of Data instances, there must be as many instances as outputs
        of the decorated function

    Returns
    -------
    Decorator that maps the outputs of a function to the Data instances and
    writes them to disk after function call.
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            outputs = function(*args, **kwargs)
            for data, output in zip(list_of_data, outputs):
                data._data = output
                data.write()

        return wrapper

    return decorator
