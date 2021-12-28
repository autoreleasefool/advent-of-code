from aoc import AOC
from heapq import heappop, heappush
from itertools import count, product
from typing import Dict, List, Optional, Tuple

aoc = AOC(year=2021, day=23)
data = aoc.load()


def manhattan(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return sum(map(lambda i, j: abs(i - j), a, b))


def rooms_for_value(v: str) -> List[Tuple[int, int]]:
    if v == "A":
        return sorted(list(filter(lambda r: r[0] == 3, rooms)))
    elif v == "B":
        return sorted(list(filter(lambda r: r[0] == 5, rooms)))
    elif v == "C":
        return sorted(list(filter(lambda r: r[0] == 7, rooms)))
    elif v == "D":
        return sorted(list(filter(lambda r: r[0] == 9, rooms)))


def value_for_room(r: Tuple[int, int]) -> str:
    if r[0] == 3:
        return "A"
    elif r[0] == 5:
        return "B"
    elif r[0] == 7:
        return "C"
    elif r[0] == 9:
        return "D"


def movement_cost(v: str, dist: int) -> int:
    if v == "A":
        return dist
    elif v == "B":
        return dist * 10
    elif v == "C":
        return dist * 100
    elif v == "D":
        return dist * 1000


def is_blocked_above(r: Tuple[int, int], d: Dict[Tuple[int, int], str]):
    return any(d[(r[0], y)] != "." for y in range(2, r[1]))


def can_move_between(
    start: Tuple[int, int], dest: Tuple[int, int], d: Dict[Tuple[int, int], str]
):
    xr = range(min(start[0], dest[0]) + 1, max(start[0], dest[0]))
    return all((x, 1) not in halls or d[(x, 1)] == "." for x in xr)


def lowest_available_room(
    value: str, d: Dict[Tuple[int, int], str]
) -> Optional[Tuple[int, int]]:
    rooms = rooms_for_value(value)
    lowest_room = None
    for r in rooms:
        if d[r] == ".":
            lowest_room = r
        elif d[r] != value:
            return None

    return lowest_room


def misplaced(d: Dict[Tuple[int, int], str]) -> List[Tuple[Tuple[int, int], str]]:
    misplaced = []
    for v in ["A", "B", "C", "D"]:
        has_incorrect_value_below = False
        for r in reversed(rooms_for_value(v)):
            if d[r] == ".":
                continue

            if has_incorrect_value_below:
                misplaced.append((r, d[r]))
            elif d[r] != v:
                has_incorrect_value_below = True
                misplaced.append((r, d[r]))
    for h in halls:
        if d[h] != ".":
            misplaced.append((h, d[h]))

    return tuple(sorted(misplaced))


def possible_moves(
    r: Tuple[int, int], d: Dict[Tuple[int, int], str]
) -> List[Tuple[Tuple[int, int], Tuple[int, int], int]]:
    if is_blocked_above(r, d):
        return []

    movements = []
    if r in halls:
        dest = lowest_available_room(d[r], d)
        if dest is not None and r[0] != dest[0] and can_move_between(r, dest, d):
            movements.append((r, dest, manhattan(r, dest)))
    else:
        movements += [
            (r, h, manhattan(r, h))
            for h in halls
            if d[h] == "." and can_move_between(r, h, d)
        ]

    return movements


def solve(diagram):
    cnt = count()
    diagrams = [(0, next(cnt), diagram)]
    visited = {}
    prev = {}
    while diagrams:
        cost, _, diagram = heappop(diagrams)

        mp = misplaced(diagram)
        if not mp:
            return cost

        if mp in visited:
            continue
        visited[mp] = cost

        for room, _ in mp:
            for start, end, spaces_moved in possible_moves(room, diagram):
                updated_diagram = {k: v for k, v in diagram.items()}
                updated_diagram[start], updated_diagram[end] = (
                    updated_diagram[end],
                    updated_diagram[start],
                )
                updated_cost = cost + movement_cost(updated_diagram[end], spaces_moved)
                updated_mp = misplaced(updated_diagram)
                prev[(updated_mp, updated_cost)] = (mp, diagram, cost)
                heappush(diagrams, (updated_cost, next(cnt), updated_diagram))


# Part 1

halls = set([(1, 1), (2, 1), (10, 1), (11, 1)] + [(x, 1) for x in range(4, 9, 2)])
rooms = set([(x, y) for x, y in product(range(3, 10, 2), range(2, 4))])

initial_diagram = data.lines()
diagram = {(x, y): initial_diagram[y][x] for x, y in rooms | halls}

aoc.p1(solve(diagram))

# Part 2

rooms = set([(x, y) for x, y in product(range(3, 10, 2), range(2, 6))])

initial_diagram = (
    initial_diagram[:3] + ["###D#C#B#A###", "###D#B#A#C###"] + initial_diagram[3:]
)
diagram = {(x, y): initial_diagram[y][x] for x, y in rooms | halls}

aoc.p2(solve(diagram))
