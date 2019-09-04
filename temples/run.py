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
    """Decorator that logs the function execution time after function call.

    When chaining decorators, the benchmark decorator should be placed last
    so that only the undecorated code is benchmarked.
    """

    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        t = time.perf_counter()
        outputs = function(*args, **kwargs)
        logging.info(
            f"{function.__name__} execution took {time.perf_counter() - t:.3f} s"
        )
        return outputs

    return wrapper


def main_runner(*functions: Callable) -> Callable:
    """Returns a main function that calls given functions in order

    Progression is logged.
    """

    def wrapper() -> None:
        n_steps = len(functions)
        t = time.perf_counter()
        for i, function in enumerate(functions, 1):
            logging.info(f"Step #{i}/{n_steps}")
            function()
        logging.info(f"Global execution took {time.perf_counter() - t:.3f} s")

    return wrapper
