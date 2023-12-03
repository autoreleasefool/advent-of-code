from aoc import AOC, numbers, positions_around

aoc = AOC(year=2023, day=3)
print, p1, p2 = aoc.d, aoc.p1, aoc.p2
data = aoc.load()

grid = data.lines()

def is_valid_position(x, y):
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def part_number(y, nrange):
    return int("".join(grid[y][nrange[0]:nrange[1] + 1]))

def is_part(y, nrange):
    for x in range(nrange[0], nrange[1] + 1):
        for xx, yy in positions_around(x, y):
            if is_valid_position(xx, yy) and grid[yy][xx] not in numbers and grid[yy][xx] != '.':
                return True
    return False

def identify_gear(y, nrange, stars):
    for x in range(nrange[0], nrange[1] + 1):
        for xx, yy in positions_around(x, y):
            if is_valid_position(xx, yy) and grid[yy][xx] == '*':
                if (yy, xx) not in stars:
                    stars[(yy, xx)] = []
                if (y, nrange) not in stars[(yy, xx)]:
                    stars[(yy, xx)].append((y, nrange))

# Part 1

valid_parts = 0

for y, row in enumerate(grid):
    nrange = None
    for x, p in enumerate(row + '.'):
        if p in numbers:
            nrange = (x, x) if nrange is None else (nrange[0], x)
        elif nrange is not None:
            valid_parts += part_number(y, nrange) if is_part(y, nrange) else 0
            nrange = None

aoc.p1(valid_parts)

# Part 2

stars = {}
for y, row in enumerate(grid):
    nrange = None
    for x, p in enumerate(row + '.'):
        if p in numbers:
            nrange = (x, x) if nrange is None else (nrange[0], x)
        elif nrange is not None:
            identify_gear(y, nrange, stars)
            nrange = None

ratios = 0

for star in stars:
    if len(stars[star]) == 2:
        pn1 = part_number(stars[star][0][0], stars[star][0][1])
        pn2 = part_number(stars[star][1][0], stars[star][1][1])
        ratios += pn1 * pn2

p2(ratios)