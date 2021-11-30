from aoc import AOC


aoc = AOC(year=2018, day=10)
data = aoc.load()


## Part 1


points = {}
for l in data.numbers_by_line():
    x, y, xx, yy = l
    points[(x, y)] = [(xx, yy)]

xs = [x[0] for x in points.keys()]
ys = [x[0] for x in points.keys()]
left, width = min(xs), max(xs)
top, height = min(ys), max(ys)


def print_lights(lights):
    pass
    # pxs = [x[0] for x in lights.keys()]
    # pys = [x[0] for x in lights.keys()]
    # pleft, pwidth = min(pxs), max(pxs)
    # ptop, pheight = min(pys), max(pys)
    # for py in range(ptop, pheight + 1):
    #     for px in range(pleft, pwidth + 1):
    #         if (px, py) in lights:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()
    # print(seconds)


should_print = False
count = 10
seconds = 0
while True:
    if should_print:
        print_lights(points)
    updated_points = {}
    for point in points:
        x, y = point
        for velocity in points[point]:
            xx, yy = velocity
            new_point = (x + xx, y + yy)
            if new_point in updated_points:
                updated_points[new_point].append((xx, yy))
            else:
                updated_points[new_point] = [(xx, yy)]
    points = updated_points
    seconds += 1

    count -= 1
    if count == 0:
        count = 10
        ys = [x[0] for x in points.keys()]
        top, height = min(ys), max(ys)
        did_print = should_print
        should_print = abs(top - height) < 100
        if not should_print and did_print != should_print:
            break


aoc.p1("CRXKEZPZ")


## Part 2


points = {}
for l in data.numbers_by_line():
    x, y, xx, yy = l
    points[(x, y)] = [(xx, yy)]

xs = [x[0] for x in points.keys()]
ys = [x[0] for x in points.keys()]
left, width = min(xs), max(xs)
top, height = min(ys), max(ys)


def print_lights(lights):
    pass
    # pxs = [x[0] for x in lights.keys()]
    # pys = [x[0] for x in lights.keys()]
    # pleft, pwidth = min(pxs), max(pxs)
    # ptop, pheight = min(pys), max(pys)
    # for py in range(ptop, pheight + 1):
    #     for px in range(pleft, pwidth + 1):
    #         if (px, py) in lights:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()
    # print(seconds)


should_print = False
count = 10
seconds = 0
while True:
    if should_print:
        print_lights(points)
    updated_points = {}
    for point in points:
        x, y = point
        for velocity in points[point]:
            xx, yy = velocity
            new_point = (x + xx, y + yy)
            if new_point in updated_points:
                updated_points[new_point].append((xx, yy))
            else:
                updated_points[new_point] = [(xx, yy)]
    points = updated_points
    seconds += 1

    count -= 1
    if count == 0:
        count = 10
        ys = [x[0] for x in points.keys()]
        top, height = min(ys), max(ys)
        did_print = should_print
        should_print = abs(top - height) < 100
        if not should_print and did_print != should_print:
            break


aoc.p2(10081)
