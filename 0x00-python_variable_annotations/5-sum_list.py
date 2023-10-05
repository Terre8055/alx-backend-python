#!/usr/bin/env python3
"""Module to return sum of list of a float"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return float of list"""
    init_fig: float = 0
    for i in input_list:
        init_fig += i
    return init_fig
