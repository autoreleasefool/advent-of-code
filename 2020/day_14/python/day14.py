from aoc import AOC
import re


aoc = AOC(year=2020, day=14)
data = aoc.load()

# Part 1

mask = "X" * 36
memory = {}
for line in data.lines():
    if line[:4] == "mask":
        mask = line[7:]
        continue

    mem, val = [int(x) for x in re.search(r"mem\[(\d+)\] = (\d+)", line).groups()]
    memory[mem] = int(
        "".join([m if m != "X" else b for b, m in zip(format(val, "036b"), mask)]),
        base=2,
    )

aoc.p1(sum(memory.values()))

# Part 2


def replace_x(mem):
    x = mem.find("X")
    if x < 0:
        return [mem]
    return replace_x(mem.replace("X", "0", 1)) + replace_x(mem.replace("X", "1", 1))


mask = "X" * 36
memory = {}
for line in data.lines():
    if line[:4] == "mask":
        mask = line[7:]
        continue

    mem, val = [int(x) for x in re.search(r"mem\[(\d+)\] = (\d+)", line).groups()]

    mem = "".join(
        [
            m if m == "X" else b if m == "0" else "1"
            for b, m in zip(format(mem, "036b"), mask)
        ]
    )

    for m in replace_x(mem):
        memory[int(m, base=2)] = val

aoc.p2(sum(memory.values()))
