import logging
import time
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


def benchmark(function: Callable) -> Callable:
    """Decorator that logs the function execution time after function call."""

    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        t = time.perf_counter()
        outputs = function(*args, **kwargs)
        logging.info(
            f"{function.__name__} execution took {time.perf_counter() - t:.3f} s"
        )
        return outputs

    return wrapper
