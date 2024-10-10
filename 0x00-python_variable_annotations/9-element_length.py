#!/usr/bin/env python3
""" Moudule """
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Function """
    return [(i, len(i)) for i in lst]
