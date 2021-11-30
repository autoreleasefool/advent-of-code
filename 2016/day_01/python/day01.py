from aoc import AOC


aoc = AOC(year=2016, day=1)
data = aoc.load()


## Part 1

# Initial position and direction
pos = (0, 0)
direction = "N"


def turn(facing, towards):
    # Returns the new direction after turning towards the left or right
    if towards == "R":
        if facing == "N":
            return "E"
        if facing == "E":
            return "S"
        if facing == "S":
            return "W"
        if facing == "W":
            return "N"
    else:
        if facing == "N":
            return "W"
        if facing == "W":
            return "S"
        if facing == "S":
            return "E"
        if facing == "E":
            return "N"
    return facing


def move(start, cardinal, distance):
    # Returns the new position after moving a distance from the current position in the provided direction
    if cardinal == "N":
        return (start[0], start[1] + distance)
    if cardinal == "E":
        return (start[0] + distance, start[1])
    if cardinal == "S":
        return (start[0], start[1] - distance)
    if cardinal == "W":
        return (start[0] - distance, start[1])
    return start


# For each instruction provided in the input
for instruction in data.contents().split(", "):
    # Move in the provided direction
    direction = turn(direction, instruction[0])
    pos = move(pos, direction, int(instruction[1:]))


aoc.p1(abs(pos[0]) + abs(pos[1]))

## Part 2

# Initial position and direction
pos = (0, 0)
direction = "N"

# Track which positions were visited
visited = {}
visited_twice_first = None


def turn(facing, towards):
    # Returns the new direction after turning towards the left or right
    if towards == "R":
        if facing == "N":
            return "E"
        if facing == "E":
            return "S"
        if facing == "S":
            return "W"
        if facing == "W":
            return "N"
    else:
        if facing == "N":
            return "W"
        if facing == "W":
            return "S"
        if facing == "S":
            return "E"
        if facing == "E":
            return "N"
    return facing


def move(start, cardinal, dist):
    # Returns the new position after moving a distance from the current position in the provided direction
    if cardinal == "N":
        return (start[0], start[1] + dist)
    if cardinal == "E":
        return (start[0] + dist, start[1])
    if cardinal == "S":
        return (start[0], start[1] - dist)
    if cardinal == "W":
        return (start[0] - dist, start[1])
    return start


# For each instruction provided in the input
for instruction in data.contents().split(", "):

    # Turn towards the provided direction
    direction = turn(direction, instruction[0])

    # Move one space at a time so that all positions are recorded and when one is visited twice, break
    distance = int(instruction[1:])
    while distance > 0:
        pos = move(pos, direction, 1)
        distance -= 1
        if pos in visited:
            if visited_twice_first is None:
                visited_twice_first = pos
        visited[pos] = True


aoc.p2(abs(visited_twice_first[0]) + abs(visited_twice_first[1]))
