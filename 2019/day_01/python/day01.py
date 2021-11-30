from aoc import AOC


aoc = AOC(year=2019, day=1)
data = aoc.load()

aoc.p1(sum([mass // 3 - 2 for mass in data.numbers()]))


def fuel_for_module(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + fuel_for_module(fuel)


aoc.p2(sum([fuel_for_module(mass) for mass in data.numbers()]))
