import aoc
import re

data = aoc.load(year=2015, day=2)

## Part 1

# Initialize to 0 feet of wrapping paper
total_square_feet = 0

# For each line in the input
for line in data.lines():

    # Get the integers in each line
    sides = re.split(r"\D", line)
    sides = [int(i) for i in sides[:3]]

    # Get the surface area of each side and add to total
    first_side = sides[0] * sides[1]
    second_side = sides[1] * sides[2]
    third_side = sides[0] * sides[2]
    total_square_feet += 2 * (first_side + second_side + third_side)

    # Find shortest side and add to total
    if first_side < second_side:
        if first_side < third_side:
            total_square_feet += first_side
        else:
            total_square_feet += third_side
    else:
        if third_side < second_side:
            total_square_feet += third_side
        else:
            total_square_feet += second_side

p1_solution = total_square_feet
print(p1_solution)

## Part 2

# Initialize to 0 feet of ribbon
total_length = 0

# For each line in the input
for line in data.lines():

    # Get the integers in each line
    sides = re.split(r"\D", line)
    sides = [int(i) for i in sides[:3]]

    # Start by calculating the volume of the gift
    total_length += sides[0] * sides[1] * sides[2]

    # Find 2 smallest sides and add their perimeter to the total
    if sides[0] < sides[1]:
        if sides[2] < sides[1]:
            total_length += 2 * (sides[0] + sides[2])
        else:
            total_length += 2 * (sides[0] + sides[1])
    else:
        if sides[2] < sides[0]:
            total_length += 2 * (sides[1] + sides[2])
        else:
            total_length += 2 * (sides[0] + sides[1])

p2_solution = total_length
print(p2_solution)
