from aoc import AOC, Position

aoc = AOC(year=2021, day=17)
data = aoc.load()


def step(position, velocity):
    position.x += velocity.x
    position.y += velocity.y
    velocity.x -= (velocity.x // abs(velocity.x)) if velocity.x != 0 else 0
    velocity.y -= 1


def overshot(position):
    return position.y < min(target_y) or position.x > max(target_x)


def in_target_range(position):
    return position.x in target_x and position.y in target_y


[minX, maxX, minY, maxY] = data.nums()
target_x = range(minX, maxX + 1)
target_y = range(minY, maxY + 1)

total_max_height = 0
total_valid_velocities = 0

for dx in range(max(target_x) + 1):
    for dy in range(min(target_y) - 1, 200):
        position = Position(0, 0)
        velocity = Position(dx, dy)
        max_height = 0

        while not overshot(position) and not in_target_range(position):
            step(position, velocity)
            max_height = max(position.y, max_height)
            if velocity.x == 0 and position.x < min(target_x):
                break

        if in_target_range(position):
            total_max_height = max(total_max_height, max_height)
            total_valid_velocities += 1

aoc.p1(total_max_height)
aoc.p2(total_valid_velocities)
