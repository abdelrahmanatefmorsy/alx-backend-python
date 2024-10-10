#!/usr/bin/env python3
""" Moudule """
from typing import Union, List


def to_kv(k: str, v: Union[float, int]) -> tuple:
    """ Function """
    return (k, v ** 2)
