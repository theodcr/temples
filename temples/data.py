from pathlib import Path
from typing import List

from .config import get_absolute_path


class Data(object):
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
