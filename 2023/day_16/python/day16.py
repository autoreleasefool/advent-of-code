from aoc import AOC, Position, map_grid_to_postions, Direction, flatten

aoc = AOC(year=2023, day=16)
print, p1, p2 = aoc.d, aoc.p1, aoc.p2
data = aoc.load()

grid = map_grid_to_postions(data.lines())
max_y = len(data.lines()) - 1
max_x = len(data.lines()[0]) - 1

def get_next_direction(current_direction: Direction, to: Position) -> list[Position]:
    if grid[to] == '.':
        return [current_direction]
    if grid[to] == '/':
        if current_direction == Direction.E: return [Direction.N]
        if current_direction == Direction.N: return [Direction.E]
        if current_direction == Direction.S: return [Direction.W]
        if current_direction == Direction.W: return [Direction.S]
    if grid[to] == '\\':
        if current_direction == Direction.E: return [Direction.S]
        if current_direction == Direction.N: return [Direction.W]
        if current_direction == Direction.S: return [Direction.E]
        if current_direction == Direction.W: return [Direction.N]
    if grid[to] == '|':
        if current_direction == Direction.E or current_direction == Direction.W: return [Direction.N, Direction.S]
        return [current_direction]
    if grid[to] == '-':
        if current_direction == Direction.N or current_direction == Direction.S: return [Direction.E, Direction.W]
        return [current_direction]

def is_invalid(position):
    return position.x < 0 or position.x > max_x or position.y < 0 or position.y > max_y


def find_max_energized(starts: list[tuple[Position, Direction]]):
    max_energized = 0
    for start in starts:
        currents = [start]
        energized = set()
        visited = set()

        while currents:
            current = currents.pop()
            if current in visited:
                continue
            visited.add(current)

            position, direction = current
            energized.add(position)

            next_position = position.move(direction)
            if is_invalid(next_position): continue
            next_directions = get_next_direction(direction, next_position)

            for next_direction in next_directions:
                currents.append((next_position, next_direction))

        if len(energized) > max_energized:
            max_energized = len(energized)

    return max_energized - 1

p1(find_max_energized([(Position(-1, 0), Direction.E)]))
p2(find_max_energized(flatten([
    [(Position(x, -1), Direction.S) for x in range(len(data.lines()[0]))],
    [(Position(x, len(data.lines())), Direction.N) for x in range(len(data.lines()[0]))],
    [(Position(-1, y), Direction.E) for y in range(len(data.lines()))],
    [(Position(len(data.lines()[0]), y), Direction.W) for y in range(len(data.lines()))],
])))
