#!/usr/bin/env python3
"""Module to return complex types"""
from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Method to return iterable"""
    return [(i, len(i)) for i in lst]
