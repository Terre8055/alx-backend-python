#!/usr/bin/env python3
"""Module to return sum of list of a int as float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return float of list"""
    init_fig: float = 0
    for i in mxd_lst:
        init_fig += i
    return init_fig


print(sum_mixed_list.__annotations__)