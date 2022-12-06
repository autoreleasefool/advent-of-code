from aoc import AOC, sliding_window

aoc = AOC(year=2022, day=6)
data = aoc.load()

series = sliding_window(data.lines()[0], 4)
for n, s in enumerate(series):
    if len(set(s)) == 4:
        aoc.p1(n + 4)
        break

series = sliding_window(data.lines()[0], 14)
for n, s in enumerate(series):
    if len(set(s)) == 14:
        aoc.p2(n + 14)
        break
