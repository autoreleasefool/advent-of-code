from functools import reduce
import operator
import re

# Usage:
# n = [3, 5, 7]
# a = [2, 3, 2]
# chinese_remainder(n, a) == 23

# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def numbers_from(l):
    regex = r"-?\d+"
    return [int(match) for match in re.findall(regex, l)]

def prod(l) -> int:
    return reduce(operator.mul, l)
