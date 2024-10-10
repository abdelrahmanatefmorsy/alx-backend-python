#!/usr/bin/env python3
""" Moudule """
from typing import Callable, Iterator, Union, Optional, List


def sum_list(input_list: List[float]) -> float:
    """ Function """
    sum = 0

    for i in input_list:
        sum += i
    return sum
