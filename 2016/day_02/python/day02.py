from aoc import AOC


aoc = AOC(year=2016, day=2)
data = aoc.load()


## Part 1

# Keypad layout
layout = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Initial position (number 5)
start = (1, 1)
code = []

for line in data.lines():
    for char in line:
        if char == "L":
            start = (start[0], max(start[1] - 1, 0))
        if char == "U":
            start = (max(start[0] - 1, 0), start[1])
        if char == "R":
            start = (start[0], min(start[1] + 1, 2))
        if char == "D":
            start = (min(start[0] + 1, 2), start[1])

    code.append(layout[start[0]][start[1]])

aoc.p1("".join([str(c) for c in code]))

## Part 2

# Keypad layout
layout = [
    [-1, -1, 1, -1, -1],
    [-1, 2, 3, 4, -1],
    [5, 6, 7, 8, 9],
    [-1, "A", "B", "C", -1],
    [-1, -1, "D", -1, -1],
]

# Initial position (number 5)
start = (2, 0)
code = []

keypad_height = len(layout)
keypad_width = len(layout[0])


def is_valid(y, x):
    # Returns true if a position is valid on the keypad
    return (
        x in range(0, keypad_width)
        and y in range(0, keypad_height)
        and layout[y][x] != -1
    )


for line in data.lines():
    for char in line:
        if char == "L" and is_valid(start[0], start[1] - 1):
            start = (start[0], start[1] - 1)
        if char == "U" and is_valid(start[0] - 1, start[1]):
            start = (start[0] - 1, start[1])
        if char == "R" and is_valid(start[0], start[1] + 1):
            start = (start[0], start[1] + 1)
        if char == "D" and is_valid(start[0] + 1, start[1]):
            start = (start[0] + 1, start[1])

    code.append(layout[start[0]][start[1]])

aoc.p2("".join([str(c) for c in code]))
