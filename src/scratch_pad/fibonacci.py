"""Fibonacci"""

import logging
import time
from collections.abc import Callable

_logger = logging.getLogger(__name__)


def time_function(function: Callable[[int], int], iterations: int) -> None:
    """Time function

    Args:
        function (Callable[[int], int]): function to call
        iterations (int): number of iterations

    """
    start_time: float = time.perf_counter()
    result: int = function(iterations)
    end_time: float = time.perf_counter()

    _logger.info("%s%s=%s", function.__name__, iterations, result)
    _logger.info("Total time: %ss", f"{end_time - start_time:.4f}")


def fibonacci_recursive(n: int) -> int:
    """Recursive Fibonacci implementation

    Args:
        n (int): number of iterations

    Returns:
        int: fibonacci number

    """
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci(n: int) -> int:
    """Summation implementation of Fibonacci

    Args:
        n (int): number of iterations

    Returns:
        int: fibonacci number

    """
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


if __name__ == "__main__":
    time_function(fibonacci, 500_000)
    # time_function(fibonacci_recursive, 35)  # noqa: ERA001
