from aoc import AOC, Position
from typing import Dict, List
from math import inf

aoc = AOC(year=2022, day=12)
data = aoc.load()

def build_map(part: int):
    starting_points: List[Position] = []
    ending_point: Position = None
    heightmap: Dict[Position, int] = {}

    for y, row in enumerate(data.lines()):
        for x, c in enumerate(row):
            if c == 'S' or (part == 2 and c == 'a'):
                heightmap[Position(x, y)] = ord('a')
                starting_points.append(Position(x, y))
            elif c == 'E':
                heightmap[Position(x, y)] = ord('z')
                ending_point = Position(x, y)
            else:
                heightmap[Position(x, y)] = ord(c)

    Position.set_limits(range(max(heightmap, key=lambda p: p.x).x + 1), range(max(heightmap, key=lambda p: p.y).y + 1))
    return starting_points, ending_point, heightmap

def explore(start: Position, target: Position, heightmap: Dict[Position, int]):
    to_visit: List[Position] = [start]
    distance = { start: 0 }

    while to_visit:
        position = to_visit.pop(0)

        if position == target:
            return distance[position]

        for neighbor in position.adjacent(diagonal=False):
            if neighbor in distance:
                continue

            if heightmap[neighbor] <= heightmap[position] + 1:
                distance[neighbor] = distance[position] + 1
                to_visit.append(neighbor)

    # End is unreachable
    return inf

starting_points, ending_point, heightmap = build_map(1)
aoc.p1(explore(starting_points[0], ending_point, heightmap))

starting_points, ending_point, heightmap = build_map(2)
aoc.p2(min(explore(start, ending_point, heightmap) for start in starting_points))
