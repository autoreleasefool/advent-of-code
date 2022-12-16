from aoc import AOC

aoc = AOC(year=2022, day=14)
data = aoc.load()
data.test = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

cave = {}
# max_y = 0
for path in data.lines():
    prev_point = None
    for point in path.split(' -> '):
        # aoc.d(point)
        x, y = point.split(',')
        x, y = int(x), int(y)
        if prev_point:
            if x == prev_point[0]:
                for yy in range(min(y, prev_point[1]), max(y, prev_point[1]) + 1):
                    cave[(x, yy)] = '#'
            elif y == prev_point[1]:
                for xx in range(min(x, prev_point[0]), max(x, prev_point[0]) + 1):
                    cave[(xx, y)] = '#'
                    # max_y = max(max_y, y)
        prev_point = (x, y)
max_y = max(y for _, y in cave) + 1
for x in range(-10000, 10000):
    cave[(x, max_y + 1)] = '#'

# aoc.d(cave)
# aoc.d(max_y)

sand = (500, 0)
while (500, 0) not in cave:
    if (sand[0], sand[1] + 1) not in cave:
        sand = (sand[0], sand[1] + 1)
    # elif (sand[0] - 1, sand[1]) not in cave and (sand[0] - 1, sand[1] + 1) not in cave:
    elif (sand[0] - 1, sand[1] + 1) not in cave:
        sand = (sand[0] - 1, sand[1] + 1)
    # elif (sand[0] + 1, sand[1]) not in cave and (sand[0] + 1, sand[1] + 1) not in cave:
    elif (sand[0] + 1, sand[1] + 1) not in cave:
        sand = (sand[0] + 1, sand[1] + 1)
    else:
        cave[sand] = 'o'
        sand = (500, 0)


# aoc.d(cave)
# print_dict_grid(cave)
aoc.p1(sum(1 for x, y in cave if cave[(x, y)] == 'o'))