from aoc import AOC, Position
from heapq import heappush, heappop

aoc = AOC(year=2021, day=15)
data = aoc.load()


def least_risk_path(grid):
    Position.set_limits(range(len(grid[0])), range(len(grid)))

    start = Position(0, 0)
    end = Position(len(grid[0]) - 1, len(grid) - 1)

    q = [(0, start)]
    visited = set([start])
    while q:
        risk, pos = heappop(q)

        if pos == end:
            return risk

        for adj in pos.adjacent(diagonal=False):
            if adj not in visited:
                new_risk = risk + grid[adj.y][adj.x]
                visited.add(adj)
                heappush(q, (new_risk, adj))


base_grid = data.digits_by_line()
aoc.p1(least_risk_path(base_grid))

full_grid = [
    [0 for _ in range(len(base_grid[0]) * 5)] for _ in range(len(base_grid) * 5)
]

# Generate first row for full_grid
for y, row in enumerate(base_grid):
    for i in range(5):
        for x, value in enumerate(row):
            full_grid[y][x + i * len(row)] = (value + i - 1) % 9 + 1

# Copy first X rows to rest of full_grid
for i in range(5):
    for y, row in enumerate(full_grid[: len(base_grid)]):
        for x, value in enumerate(row):
            full_grid[y + i * len(base_grid)][x] = (value + i - 1) % 9 + 1

aoc.p2(least_risk_path(full_grid))
