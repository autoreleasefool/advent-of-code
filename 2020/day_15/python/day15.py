from aoc import AOC

aoc = AOC(year=2020, day=15)
series = aoc.load().numbers_by_line()[0]

seen = {}
n = 0

for idx, x in enumerate(series[:-1]):
    seen[x] = idx

last = series[-1]
n = len(series)

while n < 30_000_000:
    if last in seen:
        next = n - 1 - seen[last]
    else:
        next = 0
    seen[last] = n - 1
    last = next
    n += 1

    if n == 2020:
        aoc.p1(last)

aoc.p2(last)
