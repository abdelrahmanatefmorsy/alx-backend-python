#!/usr/bin/env python3
""" Moudule """
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function1
    """
    def f(n: float) -> float:
        """ Function2 """
        return float(n * multiplier)

    return f
