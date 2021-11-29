from aoc import AOC
import functools

aoc = AOC(year=2020, day=6)
data = aoc.load()

# Part 1

aoc.p1(
    sum(
        [
            len(functools.reduce(lambda a, b: set(a) | set(b), group.splitlines()))
            for group in data.contents().split("\n\n")
        ]
    )
)

# Part 2

aoc.p2(
    sum(
        [
            len(functools.reduce(lambda a, b: set(a) & set(b), group.splitlines()))
            for group in data.contents().split("\n\n")
        ]
    )
)
