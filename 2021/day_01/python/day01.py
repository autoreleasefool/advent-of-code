from aoc import AOC


aoc = AOC(year=2021, day=1)
series = aoc.load().numbers()


# Part 1

increments = sum(1 for x in range(len(series) - 1) if series[x] < series[x + 1])
aoc.p1(increments)

# Part 2

increments = sum(
    1
    for x in range(3, len(series))
    if sum(series[x - 3 : x]) < sum(series[x - 2 : x + 1])
)
aoc.p2(increments)
