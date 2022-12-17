from aoc import AOC, manhattan, merge_ranges
from typing import Set, Tuple, List

aoc = AOC(year=2022, day=15)
data = aoc.load()

beacons: Set[Tuple[int, int]] = set()
unreachable: List[range] = []
poi_row = 2000000
for sx, sy, bx, by in data.numbers_by_line():
    beacons.add((bx, by))
    distance_to_poi = manhattan((sx, sy), (sx, poi_row))
    distance_to_beacon = manhattan((sx, sy), (bx, by))

    if distance_to_beacon < distance_to_poi:
        continue

    unreachable.append(range(sx - (distance_to_beacon - distance_to_poi), sx + (distance_to_beacon - distance_to_poi)))

unreachable = merge_ranges(unreachable)
aoc.p1(sum(len(r) for r in unreachable) - sum(1 for b in beacons if any(b in r for r in unreachable)))

sensors: List[Tuple[int, int]] = []
beacons: Set[Tuple[int, int]] = set()
for sx, sy, bx, by in data.numbers_by_line():
    sensors.append((sx, sy, manhattan((sx, sy), (bx, by))))
    beacons.add((bx, by))

beacon_range = range(0, 4000000 + 1)

def find_beacon():
    for sx, sy, dist in sensors:
        dx = -dist - 1
        dy = 0
        while dx < 0:
            if (sx + dx) in beacon_range and (sy + dy) in beacon_range:
                if all(manhattan((ssx, ssy), (sx + dx, sy + dy)) > ddist for ssx, ssy, ddist in sensors):
                    aoc.p2((sx + dx) * 4000000 + (sy + dy))
                    return
            dx += 1
            dy -= 1
        while dy < 0:
            if (sx + dx) in beacon_range and (sy + dy) in beacon_range:
                if all(manhattan((ssx, ssy), (sx + dx, sy + dy)) > ddist for ssx, ssy, ddist in sensors):
                    aoc.p2((sx + dx) * 4000000 + (sy + dy))
                    return
            dx += 1
            dy += 1
        while dx > 0:
            if (sx + dx) in beacon_range and (sy + dy) in beacon_range:
                if all(manhattan((ssx, ssy), (sx + dx, sy + dy)) > ddist for ssx, ssy, ddist in sensors):
                    aoc.p2((sx + dx) * 4000000 + (sy + dy))
                    return
            dx -= 1
            dy += 1
        while dy > 0:
            if (sx + dx) in beacon_range and (sy + dy) in beacon_range:
                if all(manhattan((ssx, ssy), (sx + dx, sy + dy)) > ddist for ssx, ssy, ddist in sensors):
                    aoc.p2((sx + dx) * 4000000 + (sy + dy))
                    return
            dx -= 1
            dy -= 1

find_beacon()
