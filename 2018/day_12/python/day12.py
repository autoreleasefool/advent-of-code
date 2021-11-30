from aoc import AOC


aoc = AOC(year=2018, day=12)
data = aoc.load()


## Part 1

start_state = None
transformations = {}

for index, line in enumerate(data.lines()):
    line = line.strip()
    if index == 0:
        start_state = [1 if x == "#" else 0 for x in line]
    elif not line:
        continue
    else:
        state = tuple([1 if x == "#" else 0 for x in line[:5]])
        transformations[state] = 1 if line[9] == "#" else 0

start_index = 4
state = [0, 0, 0, 0] + start_state
for i in range(20):
    if sum(state[:5]) > 0:
        state = [0, 0, 0, 0] + state
        start_index += 4
    if sum(state[-6:]) > 0:
        state.append(0)
        state.append(0)
        state.append(0)
        state.append(0)

    next_state = state[:]
    for index, pot in enumerate(state):
        pot_state = tuple(state[index - 2 : index + 3])
        if pot_state in transformations:
            next_state[index] = transformations[pot_state]
        else:
            next_state[index] = 0
    state = next_state

total = 0
for index, pot in enumerate(state):
    total += (index - start_index) if pot == 1 else 0
aoc.p1(total)


## Part 2


start_state = None
transformations = {}

for index, line in enumerate(data.lines()):
    line = line.strip()
    if index == 0:
        start_state = [1 if x == "#" else 0 for x in line]
    elif not line:
        continue
    else:
        state = tuple([1 if x == "#" else 0 for x in line[:5]])
        transformations[state] = 1 if line[9] == "#" else 0

start_index = 4
state = [0, 0, 0, 0] + start_state
last_total = 0
for i in range(501):
    if sum(state[:5]) > 0:
        state = [0, 0, 0, 0] + state
        start_index += 4
    if sum(state[-6:]) > 0:
        state.append(0)
        state.append(0)
        state.append(0)
        state.append(0)

    total = 0
    for index, pot in enumerate(state):
        total += (index - start_index) if pot == 1 else 0
    if i == 500:
        diff = total - last_total
        final_sum = total + (50000000000 - 500) * diff
        aoc.p2(final_sum)

    last_total = total

    next_state = state[:]
    for index, pot in enumerate(state):
        pot_state = tuple(state[index - 2 : index + 3])
        if pot_state in transformations:
            next_state[index] = transformations[pot_state]
        else:
            next_state[index] = 0
    state = next_state
