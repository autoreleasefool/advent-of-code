from aoc import AOC


aoc = AOC(year=2018, day=3)
data = aoc.load()


claimed = {}
overlapping_coords = 0

for line in data.lines():
    comp = line.split()

    left = int(comp[2][: comp[2].index(",")])
    top = int(comp[2][comp[2].index(",") + 1 : -1])
    width = int(comp[3][: comp[3].index("x") :])
    height = int(comp[3][comp[3].index("x") + 1 :])

    for x in range(width):
        for y in range(height):
            spot = (left + x, top + y)
            if spot in claimed and not claimed[spot]:
                overlapping_coords += 1
                claimed[spot] = True
            elif spot not in claimed:
                claimed[spot] = False

aoc.p1(overlapping_coords)


## Part 2


claimed = {}

for line in data.lines():
    comp = line.split()

    left = int(comp[2][: comp[2].index(",")])
    top = int(comp[2][comp[2].index(",") + 1 : -1])
    width = int(comp[3][: comp[3].index("x") :])
    height = int(comp[3][comp[3].index("x") + 1 :])

    for x in range(width):
        for y in range(height):
            spot = (left + x, top + y)
            if spot in claimed:
                claimed[spot] += 1
            else:
                claimed[spot] = 1

for line in data.lines():
    comp = line.split()

    claim_id = comp[0][1:]
    left = int(comp[2][: comp[2].index(",")])
    top = int(comp[2][comp[2].index(",") + 1 : -1])
    width = int(comp[3][: comp[3].index("x") :])
    height = int(comp[3][comp[3].index("x") + 1 :])

    valid = True
    for x in range(width):
        for y in range(height):
            spot = (left + x, top + y)
            if claimed[spot] > 1:
                valid = False
    if valid:
        aoc.p2(claim_id)
        break
