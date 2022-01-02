from itertools import product
from typing import Dict, Iterable, List, Optional, Set, Tuple
from aoc import AOC, manhattan, flatten
from dataclasses import dataclass

aoc = AOC(year=2021, day=19)
data = aoc.load()


@dataclass
class ScannerPosition:
    absolute_offset: Tuple[int, int, int]
    offset: Tuple[int, int, int]
    rotation: Tuple[int, int, int]
    direction: int
    base: int

    def __iter__(self):
        return iter(
            (
                self.absolute_offset,
                self.offset,
                self.rotation,
                self.direction,
                self.base,
            )
        )


scanners: Dict[int, List[Tuple[int, int, int]]] = {}
scanner_id: int = None
for readings in data.numbers_by_line():
    if len(readings) == 1:
        scanner_id = readings[0]
        scanners[scanner_id] = []
        continue
    elif len(readings) == 3:
        scanners[scanner_id].append(tuple(readings))


def sub(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return tuple(map(lambda i, j: i - j, a, b))


def add(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return tuple(map(lambda i, j: i + j, a, b))


def mult(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return tuple(map(lambda i, j: i * j, a, b))


def facing(beacon: Tuple[int, int, int], i: int) -> Tuple[int, int, int]:
    x, y, z = beacon
    if i == 0:
        return (x, y, z)
    if i == 1:
        return (x, z, y)
    if i == 2:
        return (y, x, z)
    if i == 3:
        return (y, z, x)
    if i == 4:
        return (z, x, y)
    if i == 5:
        return (z, y, x)


rotations = list(product((1, -1), (1, -1), (1, -1)))
positions: Dict[int, ScannerPosition] = {}
positions[0] = ScannerPosition(
    absolute_offset=(0, 0, 0), offset=(0, 0, 0), rotation=(1, 1, 1), direction=0, base=0
)


def find_overlap(
    base: Set[Tuple[int, int, int]], beacons: List[Tuple[int, int, int]]
) -> Optional[Tuple[int, int, int]]:
    for ref_idx, reference in enumerate(base):
        if len(base) - ref_idx < 12:
            continue

        for idx, beacon in enumerate(beacons):
            if len(beacons) - idx < 12:
                break

            offset = sub(reference, beacon)
            matched_beacons = sum(1 for b in beacons if add(b, offset) in base)

            if matched_beacons >= 12:
                return offset


def find_position(
    base_ids: Iterable[int], scanner_id: int, beacons: List[Tuple[int, int, int]]
):
    for base_id in base_ids:
        if scanner_id == base_id:
            # Can't compare the same scanners
            continue

        base = scanners[base_id]
        checked_beacons = set()

        for rotation in rotations:
            for direction in range(6):
                first_beacon = mult(facing(beacons[0], direction), rotation)
                if first_beacon in checked_beacons:
                    continue
                checked_beacons.add(first_beacon)

                comparable_beacons = [
                    mult(facing(b, direction), rotation) for b in beacons
                ]
                offset = find_overlap(set(base), comparable_beacons)
                if offset:
                    return base_id, offset, rotation, direction


def offset_relative_to_zero(
    position: Tuple[int, int, int], base: int
) -> Tuple[int, int, int]:
    relative_offset, _, relative_rotation, relative_direction, base = positions[base]
    position = mult(facing(position, relative_direction), relative_rotation)
    while base != 0:
        _, _, relative_rotation, _, base = positions[base]
        position = mult(position, relative_rotation)
    return add(position, relative_offset)


def position_relative_to_zero(
    position: Tuple[int, int, int], base: int
) -> Tuple[int, int, int]:
    _, relative_offset, relative_rotation, relative_direction, base = positions[base]
    position = add(
        mult(facing(position, relative_direction), relative_rotation), relative_offset
    )
    while base != 0:
        _, relative_offset, relative_rotation, relative_direction, base = positions[
            base
        ]
        position = add(
            mult(facing(position, relative_direction), relative_rotation),
            relative_offset,
        )
    return position


prior_comparisons: Set[Tuple[int, int]] = set()
while len(positions) < len(scanners):
    for scanner_id, beacons in scanners.items():
        if scanner_id in positions:
            continue

        # Saving some work by not checking against scanners that have been checked in the past
        base_ids = [
            id for id in positions.keys() if (scanner_id, id) not in prior_comparisons
        ]
        prior_comparisons.update([(scanner_id, id) for id in base_ids])
        position = find_position(base_ids, scanner_id, beacons)

        if position is None:
            continue

        base_id, offset, rotation, direction = position
        if base_id == 0:
            positions[scanner_id] = ScannerPosition(
                offset, offset, rotation, direction, base_id
            )
        else:
            positions[scanner_id] = ScannerPosition(
                offset_relative_to_zero(offset, base_id),
                offset,
                rotation,
                direction,
                base_id,
            )

# Part 1
beacons = set(
    flatten(
        [position_relative_to_zero(b, id) for b in scanners[id]] for id in positions
    )
)
aoc.p1(len(beacons))

# Part 2

maximum_distance = 0
for ida in positions:
    for idb in positions:
        position_a = position_relative_to_zero(
            positions[ida].offset, positions[ida].base
        )
        position_b = position_relative_to_zero(
            positions[idb].offset, positions[idb].base
        )
        maximum_distance = max(maximum_distance, manhattan(position_a, position_b))
aoc.p2(maximum_distance)
