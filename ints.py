# Generation and identification of integer sequences. There are mainly two
# kinds of functions here:
# 1. `get_foo_ints` returns a foo integer sequence.
# 2. `is_bar_ints` returns a true or false.
import random
from functools import wraps

__all__ = [
    "get_const_diff_ints",
    "is_const_diff_ints",
    "get_const_ratio_ints",
    "is_const_ratio_ints",
    "get_fibonacci_ints",
    "is_fibonacci_ints",
    "get_random_ints",
]


def is_ints(ints):
    """Check the basic integer sequence things.

    These basic checks are a little tedious and verbose, so we've chosen to
    focus these checks here.
    """
    try:
        # A single integer would not be seen as an integer sequence.
        if len(ints) < 2:
            return False
        # Note that a boolean is also a instance of `int`.
        if not all(isinstance(obj, int) for obj in ints):
            return False
    except (TypeError, ValueError):
        return False


def is_ints_checked(is_some_ints_func):
    """Decorator for performing `is_ints` before `is_some_ints_func`."""

    @wraps(is_some_ints_func)
    def wrapper(ints):
        if is_ints(ints) is False:
            return False
        return is_some_ints_func(ints)

    return wrapper


def get_const_diff_ints(ints, length):
    """f(n) = an + b"""
    first = ints[0]
    diff = ints[1] - ints[0]
    return [first + diff * n for n in range(length)]


@is_ints_checked
def is_const_diff_ints(ints):
    _ints = get_const_diff_ints(ints, length=len(ints))
    return _ints == ints


def get_const_ratio_ints(ints, length):
    """f(n) = a(b^n)"""
    first = ints[0]
    ratio = int(ints[1] / ints[0])
    return [first * (ratio ** n) for n in range(length)]


@is_ints_checked
def is_const_ratio_ints(ints):
    if 0 in ints:
        return False
    _ints = get_const_ratio_ints(ints, length=len(ints))
    return _ints == ints


def get_fibonacci_ints(ints, length):
    """f(n) = f(n-1) + f(n-2)"""
    first = ints[0]
    second = ints[1]
    if length == 1:
        return [first]
    if length == 2:
        return [first, second]
    ints = get_fibonacci_ints(ints, length=length - 1)
    ints.append(ints[-1] + ints[-2])
    return ints


@is_ints_checked
def is_fibonacci_ints(ints):
    _ints = get_fibonacci_ints(ints, length=len(ints))
    return _ints == ints


def get_parabolic_ints(ints, length):
    """f(n) = an^2 + bn + c"""
    a, b, c = cal_parabolic_coefficients(ints)
    return [a * (n ** 2) + b * n + c for n in range(length)]


def cal_parabolic_coefficients(ints):
    """Calculate the coefficients of a integer sequence

    Let n be 0, 1 and 2. We get:
    c = first
    a + b + c = second
    4a + 2b + c = third
    """
    if len(ints) < 3:
        msg = "To calculate, length of `ints` must be three or more."
        raise ValueError(msg)
    first, second, third = ints[0], ints[1], ints[2]
    a = first / 2 - second + third / 2
    b = -3 / 2 * first + 2 * second - third / 2
    c = first
    return int(a), int(b), int(c)


@is_ints_checked
def is_parabolic_ints(ints):
    if len(ints) < 3:
        # Connot tell
        return False
    a, b, c = cal_parabolic_coefficients(ints)
    _ints = get_parabolic_ints(ints, length=len(ints))
    return _ints == ints


def get_random_ints(minimum, maximum, length):
    return [random.randint(minimum, maximum) for _ in range(length)]
