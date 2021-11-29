from aoc import AOC
import re

aoc = AOC(year=2015, day=5)
data = aoc.load()

## Part 1

# Create regex to match the rules
# 1. Contains at least one pair of two letters that appears twice (non-overlapping)
# 2. At least one letter that repeats, with one letter between them
nicestring_regex = re.compile(
    r"^(?=\w*(\w)\w\1\w*)(\w*(\w\w)\w*\3\w*)$", flags=re.MULTILINE
)
total_nicestrings = len(re.findall(nicestring_regex, data.contents()))

# Print the total number of nice strings
aoc.p1(total_nicestrings)

## Part 2

# Create regex to match the rules
# 1. Contains at least 3 values
# 2. At least one letter that appears twice in a row
# 3. Does not contain 'ab', 'cd', 'pq', or 'xy'
nicestring_regex = re.compile(
    r"^(?=\w*(\w)\1)(?!\w*(ab|cd|pq|xy))((\w*[aeiou]\w*){3,})$", flags=re.MULTILINE
)
total_nicestrings = len(re.findall(nicestring_regex, data.contents()))

# Print the total number of nice strings
aoc.p2(total_nicestrings)
