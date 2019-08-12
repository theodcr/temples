import logging
import pickle
from abc import ABC, abstractmethod
from functools import wraps
from pathlib import Path
from typing import Any, Callable

from .config import get_absolute_path


class Data(ABC):
    """
    Defines a Data object: a wrapper around a given data stored on disk.
    Actual data is not loaded on instantiation.

    This is an abstract base class, this class should be used to define Data classes
    specific to the application.
    Methods `load` and `write` must be overridden, it is also advised to override
    the `__init__` method. See PickleData class for an example.

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

    Methods
    -------
    load : loads the data stored on disk at self.path to attribute self._data
    write : writes content of attribute self._data to disk at self.path
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


class PickleData(Data):
    """Wrapper around data stored in pickle format on disk."""

    def load(self) -> Any:
        super().load()
        with open(self.path, "rb") as f:
            self._data = pickle.load(f)
        return self._data

    def write(self) -> None:
        super().write()
        with open(self.path, "wb") as f:
            pickle.dump(self._data, f)


def inputs(**dict_of_data: Data) -> Callable:
    """
    Returns a decorator that maps the inputs of the decorated function
    to Data objects. Before decorated function call, the inputs are loaded from disk
    using their load method.

    Parameters
    ----------
    **dict_of_data : Dict[str, Data]
        dict of Data instances mapped to inputs of the decorated function

    Returns
    -------
    Decorator that maps the inputs of a function to the Data instances and
    loads them from disk before function call.
    """

    def decorator(function: Callable) -> Callable:
        @wraps(function)
        def new_func(*args: Any, **kwargs: Any) -> Any:
            inputs = {keyword: data.load() for keyword, data in dict_of_data.items()}
            return function(*args, **inputs, **kwargs)

        return new_func

    return decorator


def outputs(*list_of_data: Data) -> Callable:
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

    def decorator(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            outputs = function(*args, **kwargs)
            for data, output in zip(list_of_data, outputs):
                data._data = output
                data.write()
            return outputs

        return wrapper

    return decorator
