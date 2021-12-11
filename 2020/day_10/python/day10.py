from aoc import AOC
from functools import lru_cache


aoc = AOC(year=2020, day=10)
data = aoc.load()


# Part 1

joltages = sorted([jolt for jolt in data.numbers()])
joltages = [0] + joltages + [max(joltages) + 3]
differences = [i - joltages[idx] for idx, i in enumerate(joltages[1:])]

aoc.p1(differences.count(1) * differences.count(3))

# Part 2

adjacencies = {
    i: [(i + j + 1) for j in range(3) if (i + j + 1) in joltages] for i in joltages
}
joltages = sorted(joltages)


@lru_cache
def count_trees(root):
    if root == joltages[-1]:
        return 1
    return sum([count_trees(adj) for adj in adjacencies[root]])


aoc.p2(count_trees(0))
