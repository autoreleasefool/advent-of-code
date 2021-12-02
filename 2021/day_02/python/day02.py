from aoc import AOC

aoc = AOC(year=2021, day=2)
data = aoc.load()

# Part 1

x, y = 0, 0
for c, i in data.parse_lines(r"(\w+) (\d+)"):
  if c == "forward":
    x += int(i)
  if c == "down":
    y += int(i)
  if c == "up":
    y -= int(i)

aoc.p1(x * y)

# Part 2

x, y, aim = 0, 0, 0
for c, i in data.parse_lines(r"(\w+) (\d+)"):
  if c == "forward":
    x += int(i)
    y += aim * int(i)
  if c == "down":
    aim += int(i)
  if c == "up":
    aim -= int(i)

aoc.p2(x * y)
