from typing import Dict, Set, Tuple
from aoc import AOC

aoc = AOC(year=2019, day=3)
data = aoc.load()

# Part 1


def follow_wire(path) -> Dict[Tuple[int, int], int]:
    x, y = 0, 0
    distance = 0
    board = {}
    for p in path:
        direction, count = p[0], int(p[1:])
        if direction == "R" or direction == "L":
            while count != 0:
                distance += 1
                x += 1 if direction == "R" else -1
                if (x, y) not in board:
                    board[(x, y)] = distance
                count -= 1
        else:
            while count != 0:
                distance += 1
                y += 1 if direction == "U" else -1
                if (x, y) not in board:
                    board[(x, y)] = distance
                count -= 1
    return board


boards = [follow_wire(l.split(",")) for l in data.lines()]
intersections = set(boards[0].keys()).intersection(set(boards[1].keys()))
distances = [abs(x) + abs(y) for x, y in intersections if (x, y) != (0, 0)]
aoc.d(min(distances))

# Part 2

boards = [follow_wire(l.split(",")) for l in data.lines()]
distances = [boards[0][(x, y)] + boards[1][(x, y)] for x, y in intersections]
aoc.d(min(distances))
