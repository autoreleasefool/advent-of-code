from aoc import AOC, filter_none
from math import floor, ceil
import json

aoc = AOC(year=2021, day=18)
data = aoc.load()

snailfish = [json.loads(line) for line in data.lines()]


def increment_first_in(root, by_increment):
    # Search for the first value to right by traversing left side of the tree, then increment it
    if isinstance(root, int):
        return root + by_increment
    else:
        left, right = root
        return [increment_first_in(left, by_increment), right]


def increment_last_in(root, by_increment):
    # Search for the first value to left by traversing right side of the tree, then increment it
    if isinstance(root, int):
        return root + by_increment
    else:
        left, right = root
        return [left, increment_last_in(right, by_increment)]


def exploded(root, depth=0):
    # Returns true if the node (or a subnode) exploded, value to add to the first value to the left,
    # the current node, and the value to add to the first value to the right

    left, right = root
    if depth >= 4 and isinstance(left, int) and isinstance(right, int):
        # When at a depth >= 4, explode
        return True, left, 0, right

    # Check for explosions in subnodes, bubble up exploded values to add to previous and next values
    if isinstance(left, list):
        did_explode, add_left, reduced_left, add_right = exploded(left, depth + 1)
        if did_explode:
            return (
                did_explode,
                add_left,
                [reduced_left, increment_first_in(right, add_right)],
                0,
            )
    if isinstance(right, list):
        did_explode, add_left, reduced_right, add_right = exploded(right, depth + 1)
        if did_explode:
            return (
                did_explode,
                0,
                [increment_last_in(left, add_left), reduced_right],
                add_right,
            )

    return False, 0, [left, right], 0


def split(root):
    # Splits a node. Returns true if the node (or a subnode) split, and the value of the node

    left, right = root
    # Check the leftmost node for a split first
    if isinstance(left, int):
        if left >= 10:
            return True, [[floor(left / 2), ceil(left / 2)], right]
    if isinstance(left, list):
        did_split, split_left = split(left)
        if did_split:
            return did_split, [split_left, right]

    # Check right nodes for a split after
    if isinstance(right, int):
        if right >= 10:
            return True, [left, [floor(right / 2), ceil(right / 2)]]
    if isinstance(right, list):
        did_split, split_right = split(right)
        if did_split:
            return did_split, [left, split_right]

    return False, [left, right]


def add(first, second):
    snailfish = [first, second]
    while True:
        # Try exploding first, and if it explodes
        did_explode, _, snailfish, _ = exploded(snailfish, 0)
        if did_explode:
            continue

        # If no explosion, try splitting
        did_split, snailfish = split(snailfish)
        if did_split:
            continue

        # If the number neither splits nor explodes, we're done
        if not did_explode and not did_split:
            break
    return snailfish


def magnitude(root):
    # If a node is a list, recursively get its magnitude, otherwise use the value as the magnitude
    left, right = root
    if isinstance(left, list):
        left_magnitude = magnitude(left)
    else:
        left_magnitude = left

    if isinstance(right, list):
        right_magnitude = magnitude(right)
    else:
        right_magnitude = right

    # Calculate root's magnitude and return
    return left_magnitude * 3 + right_magnitude * 2


while len(snailfish) > 1:
    # Add snailfish numbers one by one
    first, second = snailfish[0:2]
    snailfish = [add(first, second)] + snailfish[2:]

aoc.p1(magnitude(snailfish[0]))

# Part 2

max_mag = 0
snailfish = [json.loads(line) for line in data.lines()]
for first in snailfish:
    for second in snailfish:
        if first == second:
            continue

        # Brute force compare magnitudes of all snailfish numbers
        sf1 = add(first, second)
        sf2 = add(second, first)
        max_mag = max([max_mag, magnitude(sf1), magnitude(sf2)])

aoc.p2(max_mag)
