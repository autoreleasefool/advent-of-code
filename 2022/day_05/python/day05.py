from aoc import AOC, chunk, parse_number_line

aoc = AOC(year=2022, day=5)
data = aoc.load()

def parse_input():
    stacks = []
    for r, row in enumerate(data.lines()):
        if '[' not in row:
            continue
        boxes = chunk(4, row)
        for n, box in enumerate(boxes):
            if r == 0:
                stacks.append([])

            if box[1] != ' ':
                stacks[n].append(box[1])
    return [[x for x in stack[::-1]] for stack in stacks]

stacks = parse_input()
for command in data.lines():
    if not command.startswith('m'):
        continue

    command = parse_number_line(command)
    count = command[0]
    source = command[1] - 1
    dest = command[2] - 1

    moved = stacks[source][-count:]
    stacks[source] = stacks[source][:-count]
    stacks[dest] = stacks[dest] + moved[::-1]

aoc.p1("".join(x[-1] for x in stacks))

stacks = parse_input()
for command in data.lines():
    if not command.startswith('m'):
        continue

    command = parse_number_line(command)
    count = command[0]
    source = command[1] - 1
    dest = command[2] - 1

    moved = stacks[source][-count:]
    stacks[source] = stacks[source][:-count]
    stacks[dest] = stacks[dest] + moved

aoc.p2("".join(x[-1] for x in stacks))
