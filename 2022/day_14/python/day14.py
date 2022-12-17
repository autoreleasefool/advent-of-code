from aoc import AOC, Position
from itertools import product

aoc = AOC(year=2022, day=14)
data = aoc.load()

def build_cave():
    cave = {}
    for path in data.lines():
        prev_point = None
        for point in path.split(' -> '):
            x, y = [int(p) for p in point.split(',')]
            for xx, yy in product(
                range(min(x, prev_point[0]), max(x, prev_point[0]) + 1) if prev_point else [],
                range(min(y, prev_point[1]), max(y, prev_point[1]) + 1) if prev_point else []
            ):
                cave[(xx, yy)] = '#'
            prev_point = (x, y)
    return cave

def simulate(part):
    cave = build_cave()
    max_y = max(y for _, y in cave) + 2

    if part == 2:
        for x in range(-10000, 10000):
            cave[(x, max_y)] = '#'

    sand = Position(500, 0)
    while (500, 0) not in cave:
        if (sand.y == max_y):
            break

        if sand.south().tuple not in cave:
            sand.move_south()
        elif sand.southwest().tuple not in cave:
            sand.move_southwest()
        elif sand.southeast().tuple not in cave:
            sand.move_southeast()
        else:
            cave[sand.tuple] = 'o'
            sand = Position(500, 0)

    return cave

part_1_cave = simulate(1)
aoc.p1(sum(1 for x, y in part_1_cave if part_1_cave[(x, y)] == 'o'))

part_2_cave = simulate(2)
aoc.p2(sum(1 for x, y in part_2_cave if part_2_cave[(x, y)] == 'o'))
