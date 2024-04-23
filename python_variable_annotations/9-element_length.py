#!/usr/bin/env python3
from typing import Iterable, List, Tuple, Sequence
"""A simple Python module to calculate the lengths of sequences within
an iterable.

This module provides a function that takes an iterable of sequences and returns
a list of tuples. Each tuple contains a sequence from the iterable and
its length.
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each sequence in an iterable and return
    a list of tuples.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each consisting of a
        sequence and its length.
    """
    return [(i, len(i)) for i in lst]
