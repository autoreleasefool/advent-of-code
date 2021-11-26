import aoc

data = aoc.load(year=2015, day=1)

## Part 1

# Initialize to floor 0
current_floor = 0

# For each character in input
for c in data.contents():

    # Move up or down one floor based on character
    if c == "(":
        current_floor += 1
    elif c == ")":
        current_floor -= 1


p1_solution = current_floor
print(p1_solution)

## Part 2

# Initialize to floor 0, start at first position
current_floor = 0
position = 1

# For each character in input
for c in data.contents():
    # Move up or down one floor based on input
    if c == "(":
        current_floor += 1
    elif c == ")":
        current_floor -= 1

    # When the basement is first reached, print out solution and exit
    if current_floor == -1:
        break
    position += 1

p2_solution = position
print(p2_solution)
