#!/usr/bin/env python3
"""A simple Python module for creating multiplier functions.

This module provides a function that generates and returns another function,
which multiplies its input by a pre-defined multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies its input by a given multiplier.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        Callable[[float], float]: A function that multiplies a given number by
        the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """Multiply a given float by a fixed multiplier.

        Args:
            value (float): The number to be multiplied.

        Returns:
            float: The product of the value and the multiplier.
        """
        return value * multiplier

    return multiplier_function
