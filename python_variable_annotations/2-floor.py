#!/usr/bin/env python3
import math
"""A simple Python module to perform the floor operation.

This module provides a function to find the largest integer less than or equal
to a given floating point number using the math library's floor function.
"""


def floor(n: float) -> int:
    """Return the largest integer less than or equal to a given float.

    Args:
        n (float): The floating point number to floor.

    Returns:
        int: The floor of n.
    """
    return math.floor(n)
