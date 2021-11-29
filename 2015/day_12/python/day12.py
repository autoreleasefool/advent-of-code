from aoc import AOC
import re

aoc = AOC(year=2015, day=12)
data = aoc.load()

## Part 1

# Find all of the digits in the document
results = re.findall(r"-?\d+", data.contents())

# Add all of the values together
total = 0
for value in results:
    total += int(value)

aoc.p1(total)

## Part 2


def get_sum(obj):
    # Recursively gets the sum of an object in the JSON document
    obj_total = 0

    # If the object is a list, get the subtotal of each item
    if isinstance(obj, list):
        for it in obj:
            obj_total += get_sum(it)

    # If the object is a dictionary, get the subtotal of each item
    # or return 0 if any item has a value of 'red'
    elif isinstance(obj, dict):
        for it in obj:
            if obj[it] == "red":
                return 0
            obj_total += get_sum(obj[it])

    # If the object is a primitive
    else:
        # If the value is red, return 0
        if obj == "red":
            return 0

        # Otherwise, try to add the item to the sum or add nothing if its not an integer
        try:
            obj_total += int(obj)
        except ValueError:
            obj_total += 0
            # do nothing
    return obj_total


# For each item in the JSON document, add its subtotal to the total
total = 0
puzzle_input = data.json()
for item in puzzle_input:
    total += get_sum(puzzle_input[item])

aoc.p2(total)
