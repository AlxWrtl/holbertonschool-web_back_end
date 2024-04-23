#!/usr/bin/env python3
from typing import Union, Tuple
"""A simple Python module to transform key-value pairs.

This module provides a function to transform a key and a numeric value by
squaring the value and ensuring it is of type float, then returning them
as a tuple.
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert a key and a numerical value to a key-value tuple with
    value squared.

    Args:
        k (str): The key.
        v (Union[int, float]): The value to be squared and converted to float.

    Returns:
        Tuple[str, float]: A tuple containing the key and the squared
        float value.
    """
    return (k, float(v ** 2))
