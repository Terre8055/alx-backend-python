#!/usr/bin/env python3
"""Module to return complex types"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return the tup[le of two params"""
    return (k, v*v)
