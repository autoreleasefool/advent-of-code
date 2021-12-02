from aoc import AOC

aoc = AOC(year=2019, day=1)
data = aoc.load()

fuel = sum([mass // 3 - 2 for mass in data.numbers()])
aoc.p1(fuel)


def fuel_for_module(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + fuel_for_module(fuel)


aoc.p2(sum([fuel_for_module(mass) for mass in data.numbers()]))
