#!/usr/bin/env python3
""" Moudule """
from typing import  Union, List


def sum_mixed_list(mxd_lst: List[Union[int,float]]) -> float:
    """ Function """
    sum = 0

    for i in mxd_lst:
        sum += i
    return sum
