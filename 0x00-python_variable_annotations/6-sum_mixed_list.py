#!/usr/bin/env python3
"""Module to return sum of list of a int as float"""
from typing import List


def sum_mixed_list(mxd_lst: List[int]) -> float:
    """Return float of list"""
    init_fig: float = 0
    for i in mxd_lst:
        init_fig += i
    return init_fig
