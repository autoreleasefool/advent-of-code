from aoc import AOC


aoc = AOC(year=2018, day=1)
data = aoc.load()


freq = 0
for line in data.lines():
    freq += int(line)

aoc.p1(freq)


## Part 2

freq = 0
freq_set = {0: True}
repeated_freq = None
while repeated_freq is None:
    for line in data.lines():
        freq += int(line)
        if freq in freq_set:
            repeated_freq = freq
            break
        freq_set[freq] = True

aoc.p2(repeated_freq)
