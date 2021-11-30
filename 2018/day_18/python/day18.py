from aoc import AOC
import copy


aoc = AOC(year=2018, day=18)
data = aoc.load()


## Part 1


ground = set()
trees = set()
lumber = set()

width = 50
height = 50

lines = data.lines()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == ".":
            ground.add((x, y))
        elif c == "#":
            lumber.add((x, y))
        elif c == "|":
            trees.add((x, y))

current_state = {"ground": ground, "trees": trees, "lumber": lumber}


def neighbors(cell):
    n = []
    for xx in range(-1, 2):
        for yy in range(-1, 2):
            if xx == 0 and yy == 0:
                continue
            n.append((cell[0] - xx, cell[1] - yy))
    return n


def total_resources(state):
    total_lumber = 0
    total_trees = 0
    for state_y in range(height):
        for state_x in range(width):
            cell = (state_x, state_y)
            if cell in state["trees"]:
                total_trees += 1
            elif cell in state["lumber"]:
                total_lumber += 1
    return total_lumber * total_trees


minutes_passed = 0
while minutes_passed < 10:
    next_state = copy.deepcopy(current_state)
    for x in range(width):
        for y in range(height):
            current_cell = (x, y)
            ns = neighbors(current_cell)
            if current_cell in current_state["ground"]:
                surrounding_trees = sum(
                    [1 if n in current_state["trees"] else 0 for n in ns]
                )
                if surrounding_trees >= 3:
                    next_state["ground"].remove(current_cell)
                    next_state["trees"].add(current_cell)
            elif current_cell in current_state["trees"]:
                surrounding_lumber = sum(
                    [1 if n in current_state["lumber"] else 0 for n in ns]
                )
                if surrounding_lumber >= 3:
                    next_state["trees"].remove(current_cell)
                    next_state["lumber"].add(current_cell)
            elif current_cell in current_state["lumber"]:
                surrounding_lumber = sum(
                    [1 if n in current_state["lumber"] else 0 for n in ns]
                )
                surrounding_trees = sum(
                    [1 if n in current_state["trees"] else 0 for n in ns]
                )
                if surrounding_lumber == 0 or surrounding_trees == 0:
                    next_state["lumber"].remove(current_cell)
                    next_state["ground"].add(current_cell)

    current_state = next_state
    minutes_passed += 1

aoc.p1(total_resources(current_state))


## Part 2


ground = set()
trees = set()
lumber = set()

width = 50
height = 50

lines = data.lines()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == ".":
            ground.add((x, y))
        elif c == "#":
            lumber.add((x, y))
        elif c == "|":
            trees.add((x, y))

current_state = {"ground": ground, "trees": trees, "lumber": lumber}


def neighbors(cell):
    n = []
    for xx in range(-1, 2):
        for yy in range(-1, 2):
            if xx == 0 and yy == 0:
                continue
            n.append((cell[0] - xx, cell[1] - yy))
    return n


def total_resources(state):
    total_lumber = 0
    total_trees = 0
    for state_y in range(height):
        for state_x in range(width):
            cell = (state_x, state_y)
            if cell in state["trees"]:
                total_trees += 1
            elif cell in state["lumber"]:
                total_lumber += 1
    return total_lumber * total_trees


goal = 1000000000
minutes_passed = 0
total_resources_seen = {}
last_distance = -1
states_remaining = -1
repeated_states = {}
while minutes_passed < goal and states_remaining != 0:
    next_state = copy.deepcopy(current_state)
    for x in range(width):
        for y in range(height):
            current_cell = (x, y)
            ns = neighbors(current_cell)
            if current_cell in current_state["ground"]:
                surrounding_trees = sum(
                    [1 if n in current_state["trees"] else 0 for n in ns]
                )
                if surrounding_trees >= 3:
                    next_state["ground"].remove(current_cell)
                    next_state["trees"].add(current_cell)
            elif current_cell in current_state["trees"]:
                surrounding_lumber = sum(
                    [1 if n in current_state["lumber"] else 0 for n in ns]
                )
                if surrounding_lumber >= 3:
                    next_state["trees"].remove(current_cell)
                    next_state["lumber"].add(current_cell)
            elif current_cell in current_state["lumber"]:
                surrounding_lumber = sum(
                    [1 if n in current_state["lumber"] else 0 for n in ns]
                )
                surrounding_trees = sum(
                    [1 if n in current_state["trees"] else 0 for n in ns]
                )
                if surrounding_lumber == 0 or surrounding_trees == 0:
                    next_state["lumber"].remove(current_cell)
                    next_state["ground"].add(current_cell)

    current_state = next_state
    minutes_passed += 1

    resources = total_resources(current_state)
    if states_remaining < 0:
        if resources in total_resources_seen:
            distance = minutes_passed - total_resources_seen[resources]
            if distance == last_distance:
                states_remaining = distance
            last_distance = distance
        total_resources_seen[resources] = minutes_passed
    else:
        states_remaining -= 1
        repeated_states[minutes_passed] = resources

for x in repeated_states:
    if (goal - x) % distance == 0:
        aoc.p2(repeated_states[x])
