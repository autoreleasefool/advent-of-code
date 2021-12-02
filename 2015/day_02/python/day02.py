from math import prod
from aoc import AOC, mins

aoc = AOC(year=2015, day=2)
data = aoc.load()

## Part 1

total_square_feet = 0

for sides in data.numbers_by_line():
    first = sides[0] * sides[1]
    second = sides[1] * sides[2]
    third = sides[2] * sides[0]
    total_square_feet += 2 * (first + second + third) + min(first, second, third)

aoc.p1(total_square_feet)

## Part 2

# Initialize to 0 feet of ribbon
total_length = 0

for sides in data.numbers_by_line():
    total_length += sides[0] * sides[1] * sides[2] + (2 * sum(mins(sides, 2)))

aoc.p2(total_length)
