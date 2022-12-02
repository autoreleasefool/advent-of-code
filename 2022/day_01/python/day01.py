from aoc import AOC, Regex

aoc = AOC(year=2022, day=1)
data = aoc.load()

# Part 1

elves = []
calories = []
for item in data.numbers_by_line():
    if not item:
        elves.append(sum(calories))
        calories = []
        continue
    calories.append(item[0])
elves.append(sum(calories))

aoc.p1(max(elves))

# Part 2

top_elves = []
for _ in range(3):
    top_elves.append(max(elves))
    elves.remove(top_elves[-1])

aoc.p2(sum(top_elves))
