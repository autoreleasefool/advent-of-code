from aoc import AOC

aoc = AOC(year=2015, day=25)

# Challenge input
target_row = 3010
target_col = 3019
starting_value = 20151125

# Calculate which code is required
target_code = (target_col * (target_col + 1)) // 2

row_counter = 1
while row_counter < target_row:
    target_code += target_col - 1 + row_counter
    row_counter += 1

target_code -= 1

code = starting_value
while target_code > 0:
    code = code * 252533
    code = code % 33554393
    target_code -= 1

aoc.p1(code)
