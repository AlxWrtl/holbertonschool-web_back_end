#!/usr/bin/env python3
"""A simple Python module to calculate the sum of mixed type lists.

This module provides a function to sum up a list containing both integers and
floating point numbers, returning the total as a float.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculate the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and/or floats.

    Returns:
        float: The sum of the elements in the list converted to float.
    """
    return float(sum(mxd_lst))
