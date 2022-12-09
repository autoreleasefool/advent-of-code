from aoc import AOC, Position, manhattan
from copy import copy

aoc = AOC(year=2022, day=9)
data = aoc.load()

def move_head(dir, head):
    match dir:
        case 'L':
            head.x -= 1
        case 'R':
            head.x += 1
        case 'U':
            head.y -= 1
        case 'D':
            head.y += 1

def move_tail(head, tail):
    if tail not in head.adjacent(include_self=True):
        if head.x == tail.x:
            tail.y += (head.y - tail.y) // abs(head.y - tail.y)
        elif head.y == tail.y:
            tail.x += (head.x - tail.x) // abs(head.x - tail.x)
        elif head.x == tail.x + 2:
            tail.x += 1
            tail.y += 1 if head.y > tail.y else -1
        elif head.x == tail.x - 2:
            tail.x -= 1
            tail.y += 1 if head.y > tail.y else -1
        elif head.y == tail.y - 2:
            tail.y -= 1
            tail.x += 1 if head.x > tail.x else -1
        elif head.y == tail.y + 2:
            tail.y += 1
            tail.x += 1 if head.x > tail.x else -1

for part, lengths in enumerate([2, 10]):
    rope = [Position(0, 0) for _ in range(lengths)]
    tail_positions = set([tuple(rope[-1])])

    for movement in data.lines():
        dir, dist = movement.split(' ')
        for _ in range(int(dist)):
            move_head(dir, rope[0])
            for n in range(len(rope) - 1):
                move_tail(rope[n], rope[n + 1])
            tail_positions.add(tuple(rope[-1]))

    if part == 0:
        aoc.p1(len(tail_positions))
    elif part == 1:
        aoc.p2(len(tail_positions))
