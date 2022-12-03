from aoc import AOC, chunk

aoc = AOC(year=2022, day=3)
data = aoc.load()

priority = 0
for sack in data.lines():
    comp1, comp2 = sack[:len(sack) // 2], sack[len(sack) // 2:]
    item = [x for x in comp1 if x in comp2][0]
    priority += ord(item) - ord('a') + 1 if item.islower() else ord(item) - ord('A') + 27
aoc.p1(priority)

priority = 0
for group in chunk(3, data.lines()):
    for item in group[2]:
        if item in group[0] and item in group[1]:
            priority += ord(item) - ord('a') + 1 if item.islower() else ord(item) - ord('A') + 27
            break
aoc.p2(priority)
