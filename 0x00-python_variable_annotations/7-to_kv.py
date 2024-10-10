#!/usr/bin/env python3
""" Moudule """
from typing import Union, List, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """ Function """
    return (k, v ** 2)
