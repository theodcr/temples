import logging
from functools import wraps
from typing import Any, Callable


def log(message: str) -> Callable:
    """Returns a decorator to log info a message before function call.

    Parameters
    ----------
    message : str
        message to log before function call
    """

    def decorator(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> None:
            logging.info(message)
            return function(*args, **kwargs)

        return wrapper

    return decorator
