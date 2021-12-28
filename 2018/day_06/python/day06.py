from aoc import AOC, manhattan


aoc = AOC(year=2018, day=6)
data = aoc.load()


## Part 1


coords = [tuple(t) for t in data.numbers_by_line()]

width = max([x for x, _ in coords])
height = max([y for _, y in coords])
left = min([x for x, _ in coords])
top = min([y for _, y in coords])

region_sizes = dict(zip(coords, [0] * len(coords)))

for region_center in region_sizes:
    x, y = region_center
    if x == left or x == width or y == top or y == height:
        region_sizes[region_center] = -1


def find_closest(coord):
    min_dist = max(width, height)
    current_closest = None
    for center in region_sizes:
        dist = manhattan(coord, center)
        if dist < min_dist:
            current_closest = center
            min_dist = dist
        elif dist == min_dist:
            current_closest = None
    return current_closest


for x in range(left, width + 1):
    for y in range(top, height + 1):
        closest = find_closest((x, y))
        if closest is not None and region_sizes[closest] >= 0:
            region_sizes[closest] += 1

aoc.p1(max(region_sizes.values()))


## Part 2


coords = [tuple(t) for t in data.numbers_by_line()]

width = max([x for x, _ in coords])
height = max([y for _, y in coords])
left = min([x for x, _ in coords])
top = min([y for _, y in coords])

last_region_size = -1
valid_region_size = 0

max_valid_dist = 10000


def coord_is_valid(coord):
    total = 0
    for other_coord in coords:
        total += manhattan(coord, other_coord)
    return total < max_valid_dist


for x in range(0, width + 1):
    for y in range(0, height + 1):
        if coord_is_valid((x, y)):
            valid_region_size += 1

xx = width + 1
yy = height + 1
while last_region_size != valid_region_size:
    last_region_size = valid_region_size
    for y in range(yy + 1):
        if coord_is_valid((xx, y)):
            valid_region_size += 1
    for x in range(xx + 1):
        if coord_is_valid((x, yy)):
            valid_region_size += 1

aoc.p2(valid_region_size)
