from aoc import AOC, prod
from functools import reduce
import operator

aoc = AOC(year=2023, day=2)
data = aoc.load()

cubes_in_bag = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def parse_game(s: str):
    max_cubes = { "red": 0, "green": 0, "blue": 0 }
    id, all_rounds = s.split(":")
    for round in all_rounds.split(";"):
        for cubes in round.strip().split(","):
            amount, color = cubes.strip().split(" ")[:2]
            if int(amount) > max_cubes[color]:
                max_cubes[color] = int(amount)

    return int(id[5:]), max_cubes

possible_games = 0

for line in data.lines():
    game_id, cubes = parse_game(line)
    is_possible = True
    for color in cubes:
        if cubes[color] > cubes_in_bag[color]:
            is_possible = False

    if is_possible:
        possible_games += game_id

aoc.p1(possible_games)

powers = 0

def power(cubes):
    return prod(cubes[c] for c in cubes)

for line in data.lines():
    game_id, cubes = parse_game(line)
    powers += power(cubes)

aoc.p2(powers)
