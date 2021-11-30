from aoc import AOC


aoc = AOC(year=2018, day=23)
data = aoc.load()


## Part 1

nanobots = [((vals[0], vals[1], vals[2]), vals[3]) for vals in data.numbers_by_line()]
nanobots.sort(key=lambda tup: tup[1], reverse=True)
strongest = nanobots[0]


def manhattan(first, second):
    return (
        abs(first[0][0] - second[0][0])
        + abs(first[0][1] - second[0][1])
        + abs(first[0][2] - second[0][2])
    )


in_range = sum([1 if manhattan(x, strongest) <= strongest[1] else 0 for x in nanobots])

aoc.p1(in_range)
