from __future__ import annotations
from aoc import AOC
from typing import List, Optional, Tuple

aoc = AOC(year=2021, day=22)
data = aoc.load()


class Cuboid:
    def __init__(self, xr: Tuple[int, int], yr: Tuple[int, int], zr: Tuple[int, int]):
        self.xr = xr
        self.yr = yr
        self.zr = zr

    @classmethod
    @property
    def P1(cls) -> Cuboid:
        return Cuboid((-50, 50), (-50, 50), (-50, 50))

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
            xr = (min(self.xr), min(other.xr) - 1)
            yr = (max(min(self.yr), min(other.yr)), min(max(self.yr), max(other.yr)))
            bits.append(Cuboid(xr, yr, self.zr))
        if max(self.xr) > max(other.xr):
            xr = (max(other.xr) + 1, max(self.xr))
            yr = (max(min(self.yr), min(other.yr)), min(max(self.yr), max(other.yr)))
            bits.append(Cuboid(xr, yr, self.zr))
        if min(self.yr) < min(other.yr):
            yr = (min(self.yr), min(other.yr) - 1)
            bits.append(Cuboid(self.xr, yr, self.zr))
        if max(self.yr) > max(other.yr):
            yr = (max(other.yr) + 1, max(self.yr))
            bits.append(Cuboid(self.xr, yr, self.zr))
        if min(self.zr) < min(other.zr):
            xr = (max(min(self.xr), min(other.xr)), min(max(self.xr), max(other.xr)))
            yr = (max(min(self.yr), min(other.yr)), min(max(self.yr), max(other.yr)))
            zr = (min(self.zr), min(other.zr) - 1)
            bits.append(Cuboid(xr, yr, zr))
        if max(self.zr) > max(other.zr):
            xr = (max(min(self.xr), min(other.xr)), min(max(self.xr), max(other.xr)))
            yr = (
                max(min(self.yr), min(other.yr)),
                min(max(self.yr), max(other.yr)),
            )
            zr = (max(other.zr) + 1, max(self.zr))
            bits.append(Cuboid(xr, yr, zr))
        return [b for b in bits if b.area > 0]

    @property
    def area(self) -> int:
        return (
            abs(self.xr[1] - self.xr[0] + 1)
            * abs(self.yr[1] - self.yr[0] + 1)
            * abs(self.zr[1] - self.zr[0] + 1)
        )


def count_on(within: Optional[Cuboid]) -> int:
    cuboids: List[Cuboid] = []
    steps = data.parse(
        r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)"
    )

    for toggle, x1, x2, y1, y2, z1, z2 in steps:
        new_cuboid = Cuboid((x1, x2), (y1, y2), (z1, z2))

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
