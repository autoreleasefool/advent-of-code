from aoc import AOC
import re

## Part 1

aoc = AOC(year=2015, day=10)

# Input from the site
puzzle_input = "1113122113"

# Apply the process 40 times
for i in range(40):
    puzzle_output = ""

    # Get character repeated at start, number of times its repeated and add to output
    while len(puzzle_input) > 0:
        digits = re.search(r"(\d)\1*", puzzle_input)
        puzzle_input = puzzle_input[len(digits.group(0)) :]
        puzzle_output = (
            puzzle_output + str(len(digits.group(0))) + str(digits.group(0)[:1])
        )

    # Update input to iterate
    puzzle_input = puzzle_output

aoc.p1(len(puzzle_input))

## Part 2

# Input from the site
puzzle_input = "1113122113"

# Apply the process 50 times
for i in range(50):
    puzzle_output = ""

    # Get character repeated at start, number of times its repeated and add to output
    while len(puzzle_input) > 0:
        digits = re.search(r"(\d)\1*", puzzle_input)
        puzzle_input = puzzle_input[len(digits.group(0)) :]
        puzzle_output = (
            puzzle_output + str(len(digits.group(0))) + str(digits.group(0)[:1])
        )

    # Update input to iterate
    puzzle_input = puzzle_output

aoc.p1(len(puzzle_input))
