from aoc import AOC
from functools import cache
from itertools import product

aoc = AOC(year=2021, day=21)
data = aoc.load()

# Part 1


class Die:
    def __init__(self):
        self.last_roll = 0
        self.roll_count = 0

    def roll(self):
        self.roll_count += 1
        self.last_roll = (self.last_roll % 100) + 1
        return self.last_roll


scores = [0, 0]
positions = [l[1] for l in data.numbers_by_line()]
current_player = 0
die = Die()
while max(scores) < 1000:
    roll = sum([die.roll() for _ in range(3)])
    positions[current_player] += roll
    while positions[current_player] > 10:
        positions[current_player] -= 10
    scores[current_player] += positions[current_player]
    current_player = (current_player + 1) % 2

aoc.p1(min(scores) * die.roll_count)

# Part 2


@cache
def possibilities(scores, positions, current_player):
    if scores[0] >= 21:
        return (1, 0)
    if scores[1] >= 21:
        return (0, 1)

    p1_wins = p2_wins = 0
    for r1, r2, r3 in product(range(1, 4), range(1, 4), range(1, 4)):
        new_position = (positions[current_player] + sum([r1, r2, r3])) % 10
        next_positions = (
            (new_position, positions[1])
            if current_player == 0
            else (positions[0], new_position)
        )

        new_score = scores[current_player] + new_position + 1
        next_score = (
            (new_score, scores[1]) if current_player == 0 else (scores[0], new_score)
        )

        p1, p2 = possibilities(next_score, next_positions, (current_player + 1) % 2)
        p1_wins += p1
        p2_wins += p2
    return (p1_wins, p2_wins)


positions = tuple([l[1] - 1 for l in data.numbers_by_line()])
scores = (0, 0)

aoc.p2(max(possibilities(scores, positions, 0)))
