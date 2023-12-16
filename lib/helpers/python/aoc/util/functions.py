import re
from itertools import product
from typing import Any, Iterable, List, Tuple


def transpose(l):
    return list(map(list, zip(*l)))


def chunk(count, l):
    return [l[i : i + count] for i in range(0, len(l), count)]


def flatten(l):
    return [item for sublist in l for item in sublist]


def find_all(s, f):
    return [m.start() for m in re.finditer(s, f)]


def filter_none(l):
    return [x for x in l if x is not None]


def sliding_window(iterable, size):
    return [iterable[i - (size - 1) : i + 1] for i in range(size - 1, len(iterable))]


def mins(iterable, count):
    return sorted(iterable)[:count]


def maxes(iterable, count):
    return sorted(iterable)[-count:]


def digits(number: int) -> List[int]:
    return [int(c) for c in str(number)]


def manhattan(a: Iterable[int], b: Iterable[int]) -> int:
    return sum(map(lambda i, j: abs(i - j), a, b))


def griditer(l: List[List[Any]]) -> List[Tuple[int, int]]:
    return product(range(len(l[0])), range(len(l)))


def stringifygrid(l: List[List[Any]]):
    return "\n".join(["".join(str(item) for item in row) for row in l])


def print_grid(l: List[List[Any]]):
    print(stringifygrid(l))
