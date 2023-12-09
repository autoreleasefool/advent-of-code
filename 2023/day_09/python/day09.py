from aoc import AOC, sliding_window

aoc = AOC(year=2023, day=9)
print, p1, p2 = aoc.d, aoc.p1, aoc.p2
data = aoc.load()

extrapolated1 = 0
extrapolated2 = 0

for line in data.numbers_by_line():
    seq = line
    seqs = [seq]
    while any(seqs[-1]):
        seqs.append(list(y - x for x, y in sliding_window(seqs[-1], 2)))

    index = len(seqs) - 1
    seqs[index].append(0)
    seqs[index].insert(0, 0)
    index -= 1

    while index >= 0:
        seqs[index].append(seqs[index][-1] + seqs[index + 1][-1])
        seqs[index].insert(0, seqs[index][0] - seqs[index + 1][0])
        index -= 1

    extrapolated1 += seqs[0][-1]
    extrapolated2 += seqs[0][0]

p1(extrapolated1)
p2(extrapolated2)
