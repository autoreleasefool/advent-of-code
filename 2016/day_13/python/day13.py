from aoc import AOC, Position

aoc = AOC(year=2016, day=13)
data = aoc.load()

favourite_number = data.numbers_by_line()[0][0]

start = Position(1, 1)
to_visit = [start]
distance_to_start = {start: 0}

def is_wall(p):
    value = (p.x * p.x) + (3 * p.x) + (2 * p.x * p.y) + p.y + (p.y * p.y)
    value += favourite_number
    return sum(int(x) for x in f'{value:b}' if x in ['0', '1']) % 2 == 1

while to_visit:
    position = to_visit.pop(0)
    if position == Position(31, 39):
        aoc.p1(distance_to_start[position])

    for adj in position.adjacent(diagonal=False):
        if adj.x < 0 or adj.y < 0:
            continue

        if adj in distance_to_start:
            if distance_to_start[position] + 1 >= distance_to_start[adj]:
                continue

        if not is_wall(adj):
            distance_to_start[adj] = distance_to_start[position] + 1
            to_visit.append(adj)

aoc.p2(sum(1 for x in distance_to_start if distance_to_start[x] <= 50))
