import aoc
from collections import namedtuple

data = aoc.load(year=2015, day=3)

## Part 1

# Tuple to use as dictionary key
Location = namedtuple("Location", ["x", "y"])

# Start dictionary with Santa's starting location
presents_delivered = {Location(0, 0): 1}

# Initialize Santa's starting location
current_x = 0
current_y = 0

# For each character in input
for c in data.contents():

    # Move Santa based on the character
    if c == "<":
        current_x -= 1
    elif c == ">":
        current_x += 1
    elif c == "^":
        current_y += 1
    elif c == "v":
        current_y -= 1

    # Check if the location is in the dictionary yet, if not, added it
    loc = Location(current_x, current_y)
    if loc in presents_delivered:
        presents_delivered[loc] += 1
    else:
        presents_delivered[loc] = 1

# Total number of houses visited is total number of entries in the dictionary
p1_solution = len(presents_delivered)
print(p1_solution)

## Part 2

# Start dictionary with Santa's starting location
presents_delivered = {Location(0, 0): 1}

# Initialize Santa and robot's starting location
current_x = [0, 0]
current_y = [0, 0]
santas_turn = True

# For each character in the input
for c in data.contents():

    # Swapping turns
    offset = 0
    if not santas_turn:
        offset = 1
    santas_turn = not santas_turn

    # Move current person based on the character
    if c == "<":
        current_x[offset] -= 1
    elif c == ">":
        current_x[offset] += 1
    elif c == "^":
        current_y[offset] += 1
    elif c == "v":
        current_y[offset] -= 1

    # Check if the location is in the dictionary yet, if not, added it
    loc = Location(current_x[offset], current_y[offset])
    if loc in presents_delivered:
        presents_delivered[loc] += 1
    else:
        presents_delivered[loc] = 1

p2_solution = len(presents_delivered)
print(p2_solution)
