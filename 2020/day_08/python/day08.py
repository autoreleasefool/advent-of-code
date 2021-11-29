from aoc import AOC, Computer

aoc = AOC(year=2020, day=8)
data = aoc.load()

# Part 1

comp = Computer(data)


def run_until_finished(comp):
    seen = set()
    while comp.position not in seen and not comp.is_finished():
        seen.add(comp.position)
        comp.step()
    return comp.is_finished()


run_until_finished(comp)
aoc.p1(comp.accumulator)

# Part 2

for idx, ins in enumerate(comp.instructions()):
    modified_comp = Computer(data)
    if ins[0] == "jmp":
        modified_comp.replace(idx, "nop")
    elif ins[0] == "nop":
        modified_comp.replace(idx, "jmp")

    if run_until_finished(modified_comp):
        break

aoc.p2(modified_comp.accumulator)
