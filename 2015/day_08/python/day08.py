import aoc
import re

data = aoc.load(year=2015, day=8)

## Part 1

# Regex to find special character sequences
special_regex = re.compile(r"(\\\"|\\x..|\\\\)")

# Initialize counts
total_characters_code = 0
total_characters_memory = 0

# For each line in the input
for line in data.lines():
    # Remove whitespace from ends of input
    line = line.strip()

    # Get the total number of raw characters
    total_characters_code += len(line)
    total_characters_memory += len(line) - 2

    # Get all instances of special characters and subtract their length from in memory
    special_characters = re.findall(special_regex, line)
    for result in special_characters:
        # Subtract one less than length to account for character the sequence actually represents
        total_characters_memory -= len(result) - 1

p1_solution = total_characters_code - total_characters_memory
print(p1_solution)

## Part 2

# Regex to find special character sequences
special_regex = re.compile(r"(\"|\\)")

# Initialize counts
total_characters_code = 0
total_characters_memory = 0

# For each line in the input
for line in data.lines():
    # Remove whitespace from ends of input
    line = line.strip()

    # Get the total number of raw characters
    total_characters_code += len(line)
    total_characters_memory += len(line) + 2

    # Get all instances of special characters and subtract their length from in memory
    special_characters = re.findall(special_regex, line)
    for result in special_characters:
        # Subtract one less than length to account for character the sequence actually represents
        total_characters_memory += 1

p2_solution = total_characters_memory - total_characters_code
print(p2_solution)
