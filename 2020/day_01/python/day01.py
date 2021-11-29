from aoc import AOC
import math
from itertools import chain

aoc = AOC(year=2020, day=1)
data = aoc.load()

# Part 1

expenses = set(data.numbers())
product = math.prod([e for e in expenses if (2020 - e) in expenses])
aoc.p1(product)

# Part 2

product = math.prod(
    set(chain(*[[e for e in expenses if (2020 - f - e) in expenses] for f in expenses]))
)
aoc.p2(product)
