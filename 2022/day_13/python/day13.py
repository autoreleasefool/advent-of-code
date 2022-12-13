from aoc import AOC, chunk
from functools import cmp_to_key
from math import prod

aoc = AOC(year=2022, day=13)
data = aoc.load()

def compare_packets(left, right):
    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            result = compare_packets(l, r)
            if result < 0:
                return -1
            elif result > 0:
                return 1
        if len(left) < len(right):
            return -1
        elif len(right) < len(left):
            return 1
        else:
            return 0
    elif isinstance(left, int) and isinstance(right, int):
        return left - right
    elif isinstance(left, list):
        return compare_packets(left, [right])
    else:
        return compare_packets([left], right)

indices = []
for n, ch in enumerate(chunk(3, data.lines())):
    left, right = eval(ch[0]), eval(ch[1])
    if compare_packets(left, right) < 0:
        indices.append(n + 1)
aoc.p1(sum(indices))

packets = [eval(d) for d in data.lines() if d] + [[[2]], [[6]]]
packets = sorted(packets, key=cmp_to_key(compare_packets))
dividers = [n + 1 for n, p in enumerate(packets) if p == [[2]] or p == [[6]]]
aoc.p2(prod(dividers))
