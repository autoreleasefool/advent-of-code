from __future__ import annotations
from aoc import AOC
from itertools import product
from typing import List, Optional, Tuple

aoc = AOC(year=2021, day=22)
data = aoc.load()


class Cuboid:
    def __init__(self, xr: range, yr: range, zr: range):
        self.xr = xr
        self.yr = yr
        self.zr = zr

    @classmethod
    @property
    def P1(cls) -> Cuboid:
        return Cuboid(range(-50, 51), range(-50, 51), range(-50, 51))

    def intersects(self, other: Cuboid) -> bool:
        return (
            max(self.xr) >= min(other.xr)
            and min(self.xr) <= max(other.xr)
            and max(self.yr) >= min(other.yr)
            and min(self.yr) <= max(other.yr)
            and max(self.zr) >= min(other.zr)
            and min(self.zr) <= max(other.zr)
        )

    def contains(self, other: Cuboid) -> bool:
        return (
            min(self.xr) <= min(other.xr)
            and max(self.xr) >= max(other.xr)
            and min(self.yr) <= min(other.yr)
            and max(self.yr) >= max(other.yr)
            and min(self.zr) <= min(other.zr)
            and max(self.zr) >= max(other.zr)
        )

    def split(self, other: Cuboid) -> List[Cuboid]:
        bits: List[Cuboid] = []
        if min(self.xr) < min(other.xr):
            xr = range(min(self.xr), min(other.xr))
            yr = range(
                max(min(self.yr), min(other.yr)), min(max(self.yr), max(other.yr)) + 1
            )
            bits.append(Cuboid(xr, yr, self.zr))
        if max(self.xr) > max(other.xr):
            xr = range(max(other.xr) + 1, max(self.xr) + 1)
            yr = range(
                max(min(self.yr), min(other.yr)), min(max(self.yr), max(other.yr)) + 1
            )
            bits.append(Cuboid(xr, yr, self.zr))
        if min(self.yr) < min(other.yr):
            yr = range(min(self.yr), min(other.yr))
            bits.append(Cuboid(self.xr, yr, self.zr))
        if max(self.yr) > max(other.yr):
            yr = range(max(other.yr) + 1, max(self.yr) + 1)
            bits.append(Cuboid(self.xr, yr, self.zr))
        if min(self.zr) < min(other.zr):
            xr = range(
                max(min(self.xr), min(other.xr)), min(max(self.xr), max(other.xr)) + 1
            )
            yr = range(
                max(min(self.yr), min(other.yr)), min(max(self.yr), max(other.yr)) + 1
            )
            zr = range(min(self.zr), min(other.zr))
            bits.append(Cuboid(xr, yr, zr))
        if max(self.zr) > max(other.zr):
            xr = range(
                max(min(self.xr), min(other.xr)), min(max(self.xr), max(other.xr)) + 1
            )
            ymin, ymax = (
                max(min(self.yr), min(other.yr)),
                min(max(self.yr), max(other.yr)) + 1,
            )
            yr = range(ymin, ymax)
            zr = range(max(other.zr) + 1, max(self.zr) + 1)
            bits.append(Cuboid(xr, yr, zr))
        return [b for b in bits if b.area > 0]

    @property
    def area(self) -> int:
        return len(self.xr) * len(self.yr) * len(self.zr)

    @property
    def bits(self) -> List[Tuple[int, int, int]]:
        return sorted(product(self.xr, self.yr, self.zr))

    def __repr__(self) -> str:
        return f"[({self.xr}, {self.yr}, {self.zr}), {self.source}, {self.area}]"


def count_on(within: Optional[Cuboid]) -> int:
    cuboids: List[Cuboid] = []
    steps = data.parse(
        r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)"
    )
    for toggle, x1, x2, y1, y2, z1, z2 in steps:
        new_cuboid = Cuboid(range(x1, x2 + 1), range(y1, y2 + 1), range(z1, z2 + 1))

        if within is not None and not within.contains(new_cuboid):
            continue

        next_cuboids = []
        for existing in cuboids:
            if existing.intersects(new_cuboid):
                next_cuboids += existing.split(new_cuboid)
            else:
                next_cuboids.append(existing)

        if toggle == "on":
            next_cuboids.append(new_cuboid)

        cuboids = next_cuboids
    return sum([c.area for c in cuboids])


aoc.p1(count_on(within=Cuboid.P1))
aoc.p2(count_on(within=None))
