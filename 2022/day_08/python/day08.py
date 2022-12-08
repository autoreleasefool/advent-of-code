from aoc import AOC, griditer
from math import prod

aoc = AOC(year=2022, day=8)
data = aoc.load()

height_map = data.digits_by_line()
visible = [[False for _ in row] for row in height_map]

# check left to right / right to left
for row in range(len(height_map)):
    tallest = [0, 0]
    width = len(height_map[row])

    for col in range(width):
        if row == 0 or col == 0 or row == len(height_map) - 1 or col == width - 1:
            visible[row][col] = True

        if height_map[row][col] > tallest[0]:
            visible[row][col] = True
            tallest[0] = height_map[row][col]

        if height_map[row][width - col - 1] > tallest[1]:
            visible[row][width - col - 1] = True
            tallest[1] = height_map[row][width - col - 1]

# check top to bottom / bottom to top
for col in range(len(height_map[0])):
    tallest = [0, 0]
    height = len(height_map)

    for row in range(height):
        if height_map[row][col] > tallest[0]:
            visible[row][col] = True
            tallest[0] = height_map[row][col]

        if height_map[height - row - 1][col] > tallest[1]:
            visible[height - row - 1][col] = True
            tallest[1] = height_map[height - row - 1][col]

aoc.p1(sum(1 for x, y in griditer(visible) if visible[y][x]))

scenic_score = [[0 for _ in row] for row in height_map]

for col, row in griditer(height_map):
    scores = []
    tree = height_map[row][col]

    height = len(height_map)
    width = len(height_map[row])

    # travel up
    for y in range(row - 1, -1, -1):
        if height_map[y][col] >= tree:
            scores.append(row - y)
            break
    if len(scores) == 0: scores.append(row)

    # travel left
    for x in range(col - 1, -1, -1):
        if height_map[row][x] >= tree:
            scores.append(col - x)
            break
    if len(scores) == 1: scores.append(col)

    # travel right
    for x in range(col + 1, width):
        if height_map[row][x] >= tree:
            scores.append(x - col)
            break
    if len(scores) == 2: scores.append(width - (col + 1))

    # travel down
    for y in range(row + 1, height):
        if height_map[y][col] >= tree:
            scores.append(y - row)
            break
    if len(scores) == 3: scores.append(height - (row + 1))

    scenic_score[row][col] = prod(scores)

aoc.p2(max(scenic_score[x][y] for x, y in griditer(scenic_score)))
