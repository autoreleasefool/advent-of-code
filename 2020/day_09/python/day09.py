from aoc import AOC
import itertools

aoc = AOC(year=2020, day=9)
series = aoc.load().numbers()

# Part 1

aoc.p1(
    next(
        s
        for i, s in enumerate(series[25:])
        if not any(sum(c) == s for c in itertools.combinations(series[i : i + 25], 2))
    )
)

# Part 2

window = []
for s in series:
    window.append(s)
    while sum(window) > aoc.p1_solution:
        window.pop(0)
    if sum(window) == aoc.p1_solution:
        break

aoc.p2(min(window) + max(window))
