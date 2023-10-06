#!/usr/bin/env python3
"""Module to return complex types"""
from typing import Callable, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: The generated function.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
