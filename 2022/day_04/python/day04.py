from aoc import AOC

aoc = AOC(year=2022, day=4)
data = aoc.load()

def get_range(elf):
    ends = elf.split('-')
    return range(int(ends[0]), int(ends[1]) + 1)

def intersect(r1, r2):
    return range(max(r1.start, r2. start), min(r1.stop, r2.stop)) or None

overlaps = 0
for elves in data.lines():
    elf1, elf2 = elves.split(',')
    elf1, elf2 = get_range(elf1), get_range(elf2)

    if intersect(elf1, elf2) == elf1 or intersect(elf1, elf2) == elf2:
        overlaps += 1
aoc.p1(overlaps)

overlaps = 0
for elves in data.lines():
    elf1, elf2 = elves.split(',')
    elf1, elf2 = get_range(elf1), get_range(elf2)

    if intersect(elf1, elf2):
        overlaps += 1
aoc.p2(overlaps)
