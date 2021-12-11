import re
from itertools import product
from typing import List, Tuple


def transpose(l):
    return list(map(list, zip(*l)))


def chunk(count, l):
    return [l[i : i + count] for i in range(0, len(l), count)]


def flatten(l):
    return [item for sublist in l for item in sublist]


def find_all(s, f):
    return [m.start() for m in re.finditer(s, f)]


def sliding_window(iterable, size):
    return [iterable[i - (size - 1) : i + 1] for i in range(size - 1, len(iterable))]


def mins(iterable, count):
    return sorted(iterable)[:count]


def maxes(iterable, count):
    return sorted(iterable)[-count:]


def digits(number: int) -> List[int]:
    return [int(c) for c in str(number)]


def griditer(l: List[List[int]]) -> List[Tuple[int, int]]:
    return product(range(len(l[0])), range(len(l)))
