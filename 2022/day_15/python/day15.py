import re


def parse(data):
    rex = re.compile(r"^.+x=([-0-9]+), y=([-0-9]+).+x=([-0-9]+), y=([-0-9]+)$")

    for line in data.strip().split("\n"):
        sx, sy, bx, by = rex.match(line).groups()
        yield (int(sx), int(sy)), (int(bx), int(by))


def solve(input):
    input = list(input)
    return (
        part1(input, 2_000_000),
        part2(input, 4_000_000),
    )


def part1(input, y):
    segments = []
    ocupado = set()

    for sensor, beacon in input:
        radius = manhatten(sensor, beacon)
        sx, sy = sensor
        bx, by = beacon

        overlap = radius - abs(sy - y)
        if overlap >= 0:
            segments = append_segment(
                segments, (sx - overlap, sx + overlap, y)
            )

        if by == y:
            ocupado.add(bx)
        if sy == y:
            ocupado.add(sx)

    return sum(1 + end - start for start, end, _ in segments) - len(ocupado)


def part2(input, bound):
    # Let u = x + y and v = x - y, let's rotate into that coordinate system
    # This changes the manhatten distance to the L-infinity distance (cool!)
    input = [(rotate(*s), rotate(*b)) for s, b in input]

    # Now all the diamons are squares - lets start with the left-most square
    # and build a "wave-front" which should proceed across the grid covering
    # everything until we hit our beacon point.
    # For each new square the left-most edge must be the largest possible
    # left-most edge
    input = sorted(input, key=lambda pair: pair[0][0] - linf(*pair))

    # The big (x, y) grid we're checking is a (u, v) diamond with
    # 0 <= u + v <= 2 * bound, 0 <= u - v <= 2 * bound
    segments = [(0, 0, -1)]

    for sensor, beacon in input:
        radius = linf(sensor, beacon)
        # Check no points are to the right of the wave and left of this square
        # First build the left-hand edge of this square as a segment
        u_outer = sensor[0] - radius - 1
        to_cover = (
            max(sensor[1] - radius, -u_outer, u_outer - 2 * bound),
            min(sensor[1] + radius + 1, u_outer, 2 * bound - u_outer),
            u_outer,
        )
        if to_cover[0] < to_cover[1]:
            # Try and append the segment to the wave: this should have no
            # effect, the left-hand edge should be fully behind the frontier!
            new_segments = append_segment(segments, to_cover)
            if new_segments != segments:
                for segment in new_segments:
                    if segment not in segments:
                        return result(u_outer, segment[0])

        # Now we need to update the segments
        u_upper = sensor[0] + radius
        v_lower = sensor[1] - radius
        v_upper = sensor[1] + radius
        segments = append_segment(segments, (v_lower, v_upper, u_upper))


def append_segment(segments, segment):
    # The heart of our solution. Take a bunch of disjoint line segments
    # with heights - and a new segment. Produce a new family of disjoint
    # line segments with the highest possible heights, example:
    #            ____                       ____
    #    ____  ~~~~       ===>      ____  ~~
    # ___    ___                 ___    __
    # where the squigly line is the new segment.
    # Probably there is a neater algorithm to do this!
    to_process = [segment]
    new_segments = segments

    while to_process:
        segments, new_segments = new_segments, []

        vl, vu, u = segment = to_process.pop()
        for k, other in enumerate(segments):
            other_vl, other_vu, other_u = other
            # We completely cover the other segment
            if vl <= other_vl and vu >= other_vu:
                if u >= other_u:
                    continue  # no need for this segment
                else:
                    # The middle chunk is covered by the old segment
                    new_segments.extend(segments[k:])
                    if vl <= other_vl - 1:
                        to_process.append((vl, other_vl - 1, u))
                    if other_vu + 1 <= vu:
                        to_process.append((other_vu + 1, vu, u))
                    break

            # Other segment completely covers us
            elif other_vl <= vl and other_vu >= vu:
                if u >= other_u:
                    if other_vl <= vl - 1:
                        to_process.append((other_vl, vl - 1, other_u))
                    if vu + 1 <= other_vu:
                        to_process.append((vu + 1, other_vu, other_u))
                    continue  # TODO: could append and break here
                else:
                    new_segments.extend(segments[k:])
                    break

            elif vl <= other_vl and vu >= other_vl:
                if u >= other_u:
                    if vu + 1 <= other_vu:
                        to_process.append((vu + 1, other_vu, other_u))
                    continue
                else:
                    new_segments.extend(segments[k:])
                    if vl <= other_vl - 1:
                        to_process.append((vl, other_vl - 1, u))
                    break

            elif vl <= other_vu and vu >= other_vu:
                if u >= other_u:
                    if other_vl <= vl - 1:
                        to_process.append((other_vl, vl - 1, other_u))
                    continue
                else:
                    new_segments.extend(segments[k:])
                    if other_vu + 1 <= vu:
                        to_process.append((other_vu + 1, vu, u))
                    break
            else:
                new_segments.append(other)  # doesn't overlap

        else:
            new_segments.append(segment)

    return sorted(new_segments)


def manhatten(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def linf(x, y):
    return max(abs(x[0] - y[0]), abs(x[1] - y[1]))


def rotate(x, y):
    return x + y, x - y


def unrotate(u, v):
    return (u + v) // 2, (u - v) // 2


def result(u, v):
    x, y = unrotate(u, v)
    return 4_000_000 * x + y

from aoc import AOC, manhattan
aoc = AOC(year=2022, day=15)
data = aoc.load()
aoc.d(solve(parse(data.contents())))

# from itertools import product

# aoc = AOC(year=2022, day=15)
# data = aoc.load()
# # data.test="""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# # Sensor at x=9, y=16: closest beacon is at x=10, y=16
# # Sensor at x=13, y=2: closest beacon is at x=15, y=3
# # Sensor at x=12, y=14: closest beacon is at x=10, y=16
# # Sensor at x=10, y=20: closest beacon is at x=10, y=16
# # Sensor at x=14, y=17: closest beacon is at x=10, y=16
# # Sensor at x=8, y=7: closest beacon is at x=2, y=10
# # Sensor at x=2, y=0: closest beacon is at x=2, y=10
# # Sensor at x=0, y=11: closest beacon is at x=2, y=10
# # Sensor at x=20, y=14: closest beacon is at x=25, y=17
# # Sensor at x=17, y=20: closest beacon is at x=21, y=22
# # Sensor at x=16, y=7: closest beacon is at x=15, y=3
# # Sensor at x=14, y=3: closest beacon is at x=15, y=3
# # Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

# # beacons = set()
# # unreachable = set()
# # poi_row = 2000000
# # for sx, sy, bx, by in data.numbers_by_line():
# #     beacons.add((bx, by))
# #     distance = manhattan((sx, sy), (bx, by))
# #     for dx in range(0, distance):
# #         failed_to_reach = True
# #         if manhattan((sx, sy), (sx + dx, poi_row)) <= distance:
# #             failed_to_reach = False
# #             unreachable.add((sx + dx, poi_row))
# #         if manhattan((sx, sy), (sx - dx, poi_row)) <= distance:
# #             failed_to_reach = False
# #             unreachable.add((sx - dx, poi_row))
# #         if failed_to_reach:
# #             break
# # aoc.p1(len(unreachable - beacons))

# # sensors = []
# # beacons = set()
# # for sx, sy, bx, by in data.numbers_by_line():
# #     sensors.append((sx, sy, manhattan((sx, sy), (bx, by))))
# #     beacons.add((bx, by))

# # for x, y in product(range(0, 4000000 + 1), range(0, 4000000 + 1)):
# #     if (x, y) in beacons:
# #         continue
# #     if all(manhattan((sx, sy), (x, y)) > dist for sx, sy, dist in sensors):
# #         aoc.p2(x * 4000000 + y)

# sensors = []
# beacons = set()
# for sx, sy, bx, by in data.numbers_by_line():
#     sensors.append((sx, sy, manhattan((sx, sy), (bx, by))))
#     beacons.add((bx, by))

# beacon_range = range(0, 4000000 + 1)

# for sx, sy, dist in sensors:
#     aoc.d((sx, sy))
#     dx = -dist - 1
#     dy = 0
#     while dx < 0:
#         if (sx + dx) in beacon_range and (sy + dy) in beacon_range:
#             if all(manhattan((ssx, ssy), (sx + dx, sy + dy)) > ddist for ssx, ssy, ddist in sensors):
#                 aoc.p2((sx + dx) * 4000000 + (sy + dy))
#                 break
#         dx += 1
#         dy -= 1
#     while dy < 0:
#         if (sx + dx) in beacon_range and (sy + dy) in beacon_range:
#             if all(manhattan((ssx, ssy), (sx + dx, sy + dy)) > ddist for ssx, ssy, ddist in sensors):
#                 aoc.p2((sx + dx) * 4000000 + (sy + dy))
#                 break
#         dx += 1
#         dy += 1
#     while dx > 0:
#         if (sx + dx) in beacon_range and (sy + dy) in beacon_range:
#             if all(manhattan((ssx, ssy), (sx + dx, sy + dy)) > ddist for ssx, ssy, ddist in sensors):
#                 aoc.p2((sx + dx) * 4000000 + (sy + dy))
#                 break
#         dx -= 1
#         dy += 1
#     while dy > 0:
#         if (sx + dx) in beacon_range and (sy + dy) in beacon_range:
#             if all(manhattan((ssx, ssy), (sx + dx, sy + dy)) > ddist for ssx, ssy, ddist in sensors):
#                 aoc.p2((sx + dx) * 4000000 + (sy + dy))
#                 break
#         dx -= 1
#         dy -= 1

# # for sx, sy, bx, by in data.numbers_by_line():


# # sensors = []
# # beacons = set()
# # for sx, sy, bx, by in data.numbers_by_line():
# #     sensors.append((sx, sy, manhattan((sx, sy), (bx, by))))
# #     beacons.add((bx, by))

# # for x, y in product(range(0, 4000000 + 1), range(0, 4000000 + 1)):
# #     if (x, y) in beacons:
# #         continue
# #     if all(manhattan((sx, sy), (x, y)) > dist for sx, sy, dist in sensors):
# #         aoc.p2(x * 4000000 + y)

#     # if all((x, y) not in)
#     # for sx, sy, dist in sensors:
#     #     if (x, y) not in beacons and all()
#     #     if (x, y) not in beacons and manhattan((sx, sy), (x, y)) > dist:


# # beacons = set()
# # unreachable = set()
# # for sx, sy, bx, by in data.numbers_by_line():
# #     beacons.add((bx, by))
# #     distance = manhattan((sx, sy), (bx, by))
# #     for dx, dy in product(range(0, distance), range(0, distance)):
# #         failed_to_reach = True
# #         if manhattan((sx, sy), (sx + dx, sy)) <= distance:
# #             failed_to_reach = False
# #             unreachable.add((sx + dx, sy))
# #         if manhattan((sx, sy), (sx - dx, sy)) <= distance:
# #             failed_to_reach = False
# #             unreachable.add((sx - dx, sy))
# #         if manhattan((sx, sy), (sx + dx, sy)) <= distance:
# #             failed_to_reach = False
# #             unreachable.add((sx + dx, sy))
# #         if manhattan((sx, sy), (sx - dx, sy)) <= distance:
# #             failed_to_reach = False
# #             unreachable.add((sx - dx, sy))

# #         if failed_to_reach:
# #             break
# # aoc.p1(len(unreachable - beacons))

# # range
# # for x, y in product(range(0, 4000000 + 1))