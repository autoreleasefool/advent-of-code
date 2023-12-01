from aoc import AOC
import math

aoc = AOC(year=2023, day=1)
data = aoc.load()

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def digit(s):
    return digits.index(s) + 1 if s in digits else s

# part 1

numeric_calibration_values = []
for numbers in data.digits_by_line():
    if not numbers: continue
    numeric_calibration_values.append(numbers[0] * 10 + numbers[-1])

aoc.p1(sum(numeric_calibration_values))

# part 2

calibration_values = []
for line in data.lines():
    first = (-1, math.inf)
    last = (-1, -1)

    for d in digits:
        i = digit(d)
        from_start, from_end = line.find(d), line.rfind(d)
        if from_start >= 0:
            if from_start < first[1]: first = (i, from_start)
            if from_end > last[1]: last = (i, from_end)

        from_start, from_end = line.find(str(i)), line.rfind(str(i))
        if from_start >= 0:
            if from_start < first[1]: first = (i, from_start)
            if from_end > last[1]: last = (i, from_end)
    calibration_values.append(first[0] * 10 + last[0])

aoc.p2(sum(calibration_values))
