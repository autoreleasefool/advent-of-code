from aoc import AOC


aoc = AOC(year=2015, day=1)
data = aoc.load()

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


aoc.p1(current_floor)

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

aoc.p2(position)
