from aoc import AOC
import re
from functools import lru_cache

aoc = AOC(year=2020, day=7)
data = aoc.load()

# Part 1

rules = {
    rule[0]: {b[2:]: int(b[0]) for b in re.split(r" bags?[,.] ?", rule[1]) if b}
    if not "no " in rule[1]
    else {}
    for rule in data.parse_lines(r"(.*) bags contain (.*)")
}


@lru_cache
def find_bags(root):
    if root == "shiny gold":
        return True
    return any([find_bags(adj) for adj in rules[root]])


aoc.p1(sum(1 for b in rules if find_bags(b)) - 1)  # Subtract 1 for 'shiny gold'

# Part 2


@lru_cache
def count_bags_within(root):
    if root not in rules or not rules[root]:
        return 0
    return sum((count_bags_within(b) + 1) * rules[root][b] for b in rules[root])


aoc.p2(count_bags_within("shiny gold"))
