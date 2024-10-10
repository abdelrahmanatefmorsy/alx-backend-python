#!/usr/bin/env python3
""" Moudule """
from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Function """
    return (k, v ** 2)
