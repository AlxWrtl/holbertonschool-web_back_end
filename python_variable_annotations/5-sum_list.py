#!/usr/bin/env python3
"""A simple Python module to calculate the sum of a list of numbers.

This module provides a function to sum up all the floating point numbers in a
given list and return the total.
"""


def sum_list(input_list: list[float]) -> float:
    """Calculate the sum of a list of floating point numbers.

    Args:
        input_list (list[float]): A list of floating point numbers.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(input_list)
