from aoc import AOC


aoc = AOC(year=2015, day=1)
data = aoc.load()

## Part 1

current_floor = sum(1 if c == "(" else -1 for c in data.contents())
aoc.p1(current_floor)

## Part 2

current_floor = 0
for i, c in enumerate(data.contents()):
    current_floor += 1 if c == "(" else -1
    if current_floor == -1:
        aoc.p2(i + 1)
        break
