from aoc import AOC
import re
from collections import defaultdict
from math import ceil

aoc = AOC(year=2019, day=14)
data = aoc.load()

reaction_regex = re.compile(r"(\d+) (\w+)")
result_regex = re.compile(r"=> (\d+) (\w+)")

reactions = {}
to_produce = [(1, "FUEL")]

leftover = defaultdict(int)
produced = defaultdict(int)
total_ore = 0

for line in data.lines():
    reaction = reaction_regex.findall(line)
    result = result_regex.search(line)
    reactions[result.group(2)] = (
        int(result.group(1)),
        [(int(r[0]), r[1]) for r in reaction[:-1]],
    )


while to_produce:
    amount_needed, chemical_needed = to_produce.pop()

    if leftover[chemical_needed] >= amount_needed:
        leftover[chemical_needed] -= amount_needed
        continue
    else:
        amount_needed -= leftover[chemical_needed]
        leftover[chemical_needed] = 0

    amount_produced, ingredients = reactions[chemical_needed]

    repetitions = (
        1 if amount_produced >= amount_needed else ceil(amount_needed / amount_produced)
    )
    amount_produced *= repetitions

    if amount_produced > amount_needed:
        leftover[chemical_needed] += amount_produced - amount_needed

    produced[chemical_needed] += amount_produced

    for requirement in ingredients:
        amount, chemical = requirement
        amount *= repetitions

        if chemical == "ORE":
            total_ore += amount
        else:
            to_produce.append((amount, chemical))

aoc.p1(total_ore)
