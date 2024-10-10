#!/usr/bin/env python3
""" Moudule """
from typing import Callable, Iterator, Union, Optional, List


def sum_mixed_list(mxd_lst: List[float,int]) -> float:
    """ Function """
    sum = 0

    for i in mxd_lst:
        sum += i
    return sum
