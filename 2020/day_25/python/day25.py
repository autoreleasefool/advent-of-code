from aoc import AOC


aoc = AOC(year=2020, day=25)
data = aoc.load()

public_keys = [int(d) for d in data.lines()]
subs = [7, 7]
loop_sizes = []


def transform(sub, loop_size):
    value = 1
    for _ in range(loop_size):
        value = single_transform(value, sub)
    return value


def single_transform(value, sub):
    value = value * sub
    return value % 20201227


for sub, key in zip(subs, public_keys):
    value = 1
    loops = 0
    while value != key:
        value = single_transform(value, sub)
        loops += 1
    loop_sizes.append(loops)

aoc.p1(transform(public_keys[0], loop_sizes[1]))
