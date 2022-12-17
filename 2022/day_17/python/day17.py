from aoc import AOC, Position
from copy import copy, deepcopy

aoc = AOC(year=2022, day=17)
data = aoc.load()
jets = data.contents().strip()

rock_layouts = [
"""..####.""",

"""...#...
..###..
...#...""",

"""....#..
....#..
..###..""",

"""..#....
..#....
..#....
..#....""",

"""..##...
..##..."""
]

starting_positions = [
    [Position(2, 0), Position(3, 0), Position(4, 0), Position(5, 0)],
    [Position(3, 0), Position(2, 1), Position(3, 1), Position(4, 1), Position(3, 2)],
    [Position(4, 0), Position(4, 1), Position(2, 2), Position(3, 2), Position(4, 2)],
    [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
    [Position(2, 0), Position(3, 0), Position(2, 1), Position(3, 1)],
]

empty = list(".......")
starting_field = [list("#######")]

def push_rock(field, rock, direction):
    if direction == '>':
        moved = [p.east() for p in rock]
    else:
        moved = [p.west() for p in rock]

    can_move = all(0 <= m.x <= 6 and (field[m.y][m.x] == '.' or m in rock) for m in moved)

    if can_move:
        for r in rock: field[r.y][r.x] = '.'
        for m in moved: field[m.y][m.x] = '#'
        return moved
    else:
        return rock

def drop_rock(field, rock):
    dropped = [p.south() for p in rock]
    can_drop = all(field[m.y][m.x] == '.' or m in rock for m in dropped)

    if can_drop:
        for r in rock: field[r.y][r.x] = '.'
        for m in dropped: field[m.y][m.x] = '#'
        return True, dropped
    else:
        return False, rock

def height(field):
    return sum(1 for f in field if f != empty) - 1

def tick(field, current_rock, current_jet):
    next_rock = current_rock % len(rock_layouts)
    is_falling = True

    while field[0:3] != [empty, empty, empty]:
        field.insert(0, empty[:])

    field = [list(p) for p in rock_layouts[next_rock].split('\n')] + field
    rock_position = [copy(p) for p in starting_positions[next_rock]]

    while is_falling:
        rock_position = push_rock(field, rock_position, jets[current_jet % len(jets)])
        is_falling, rock_position = drop_rock(field, rock_position)
        current_jet += 1

    while field[0] == empty:
        field.pop(0)

    return field, current_jet

current_rock = 0
current_jet = 0
field = deepcopy(starting_field)
while current_rock < 2022:
    field, current_jet = tick(field, current_rock, current_jet)
    current_rock += 1
aoc.p1(height(field))

# Process:
# Starts repeating at height 82, after 52 rocks
# Increases in height by 53 every 35 rocks
# 1,000,000,000,000 - 52 rocks to go
# 999,999,999,948 rocks to go
# 999,999,999,948 % 35 == 33
# (999,999,999,915 / 35) * 53 with 33 rocks to go (increases by 40)
# Answer: 82 + (999,999,999,915 / 35) * 53 + 49
# Answer: 1514285714288

# Starts repeating at height 2933, after 1873 rocks
# Increases in height by 2,750 every 1,745 rocks
# 1,000,000,000,000 - 1873 rocks to go
# 999,999,998,127 rocks to go
# 999,999,998,127 % 1745 === 882
# (999,999,997,245 / 1745) * 2750 with 882 rocks to go (increases by 1,393)
# Answer: 2933 + (999,999,997,245 / 1745) * 2750 + 1393
# Answer: 1575931232076

previous_states = set()
height_at_first_repeat = None
height_at_last_repeat = None
rocks_fallen_at_first_repeat = None
rocks_fallen_at_last_repeat = None
rocks_left_to_fall = None
first_repeating_state = None
counting_repetitions = False
increment_per_repetition = None
rocks_per_repetition = 0
surplus_height = None

current_rock = 0
current_jet = 0
field = deepcopy(starting_field)
while True:
    field, current_jet = tick(field, current_rock, current_jet)

    if counting_repetitions:
        rocks_per_repetition += 1
    if rocks_per_repetition and height_at_last_repeat and (rocks_left_to_fall % rocks_per_repetition) == current_rock - rocks_fallen_at_last_repeat:
        surplus_height = height(field) - height_at_last_repeat
        break

    if len(field) > 10:
        state = (tuple(tuple(field[x]) for x in range(10)), current_rock % len(rock_layouts), current_jet % len(jets))
        if state not in previous_states:
            previous_states.add(state)
        elif not first_repeating_state:
            first_repeating_state = state
            height_at_first_repeat = height(field)
            rocks_fallen_at_first_repeat = current_rock
            rocks_left_to_fall = 1_000_000_000_000 - current_rock
            counting_repetitions = True
        elif state == first_repeating_state and not increment_per_repetition:
            height_at_last_repeat = height(field)
            rocks_fallen_at_last_repeat = current_rock - 1
            increment_per_repetition = height_at_last_repeat - height_at_first_repeat
            counting_repetitions = False

    current_rock += 1

aoc.p2(
    height_at_first_repeat +
    ((rocks_left_to_fall - (rocks_left_to_fall % rocks_per_repetition)) // rocks_per_repetition) * increment_per_repetition +
    surplus_height
)
