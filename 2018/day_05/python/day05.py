from aoc import AOC


aoc = AOC(year=2018, day=5)
data = aoc.load()


## Part 1


puzzle = data.contents()


def next_index(after, removed):
    n = after + 1
    while n in removed:
        n += 1
    return n


def prev_index(before, removed):
    p = before - 1
    while p in removed:
        p -= 1
    if p < 0:
        p = next_index(p, removed)
    return p


cur_index = 0
removed_elements = set()
lower_puzzle = puzzle.lower()
while cur_index < len(puzzle) - 1:
    compare_index = next_index(cur_index, removed_elements)
    if compare_index >= len(puzzle):
        break

    if (
        lower_puzzle[cur_index] == lower_puzzle[compare_index]
        and puzzle[cur_index] != puzzle[compare_index]
    ):
        removed_elements.add(cur_index)
        removed_elements.add(compare_index)
        cur_index = prev_index(cur_index, removed_elements)
        continue

    cur_index = next_index(cur_index, removed_elements)

aoc.p1(len(puzzle) - len(removed_elements))


## Part 2


def next_index(after, removed):
    n = after + 1
    while n in removed:
        n += 1
    return n


def prev_index(before, removed):
    prev = before - 1
    while prev in removed:
        prev -= 1
    if prev < 0:
        prev = next_index(prev, removed)
    return prev


original_puzzle = data.contents()

available_units = set()
for unit in original_puzzle.lower():
    available_units.add(unit)

smallest_size = len(original_puzzle)
for unit in available_units:
    puzzle = original_puzzle
    lower_puzzle = puzzle.lower()
    removed_elements = set()

    unit_upper = unit.upper()
    for index, p in enumerate(puzzle):
        if p in (unit, unit_upper):
            removed_elements.add(index)

    cur_index = next_index(-1, removed_elements)

    while cur_index < len(puzzle) - 1:
        compare_index = next_index(cur_index, removed_elements)
        if compare_index >= len(puzzle):
            break

        if (
            lower_puzzle[cur_index] == lower_puzzle[compare_index]
            and puzzle[cur_index] != puzzle[compare_index]
        ):
            removed_elements.add(cur_index)
            removed_elements.add(compare_index)
            cur_index = prev_index(cur_index, removed_elements)
            continue

        cur_index = next_index(cur_index, removed_elements)

    puzzle_size = len(puzzle) - len(removed_elements)
    if puzzle_size < smallest_size:
        smallest_size = puzzle_size

aoc.p2(smallest_size)
