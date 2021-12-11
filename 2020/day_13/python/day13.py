from aoc import AOC, chinese_remainder
import itertools
import re

aoc = AOC(year=2020, day=13)
contents = aoc.load().lines()

# Part 1


start_time = int(contents[0])
buses = [int(v) for v in re.findall(r"\d+", contents[1])]

for i in itertools.count(start_time):
    departing_bus = next((bid for bid in buses if (start_time + i) % bid == 0), False)
    if departing_bus:
        aoc.p1(departing_bus * i)
        break

# Part 2

buses = [int(b) if b != "x" else b for b in contents[1].split(",")]

n = [bid for bid in buses if bid != "x"]
a = [0] + [bid - (idx + 1) for idx, bid in enumerate(buses[1:]) if bid != "x"]

aoc.p2(chinese_remainder(n, a))
