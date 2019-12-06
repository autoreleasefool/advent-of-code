#!/usr/bin/env python3

import re
import os
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
FILENAME = '{}/../input.txt'.format(SCRIPT_PATH)

# Read the challenge input
with open(FILENAME, 'r') as input_file:
    PUZZLE_INPUT = input_file.readlines()


# The target properties of the real aunt
aunt_properties = [3, 7, 2, 3, 0, 0, 5, 3, 2, 1]

# Regexes to find the properties of each aunt remembered
aunt_regexes = [r'children: (\d+)', r'cats: (\d+)', r'samoyeds: (\d+)', r'pomeranians: (\d+)', r'akitas: (\d+)',
                r'vizslas: (\d+)', r'goldfish: (\d+)', r'trees: (\d+)', r'cars: (\d+)', r'perfumes: (\d+)']

# The list of aunts so far
aunts = []

# For each aunt in the input
for line in PUZZLE_INPUT:
    # Start with -1 for all the values
    aunt = [-1 for i in range(10)]

    # For each property, check if it was remembered about the aunt and, if so, update the list
    for i, _ in enumerate(aunt_regexes):
        match = re.search(aunt_regexes[i], line)
        if match:
            aunt[i] = int(match.group(1))

    # Add the new aunt to the list so far
    aunts.append(aunt)

# Loop through all the aunts and find the one who matches all the properties
# When they are found, print out their number
for aunt, _ in enumerate(aunts):
    the_real_aunt = True
    for i, _ in enumerate(aunts[aunt]):
        if aunts[aunt][i] != aunt_properties[i] and aunts[aunt][i] != -1:
            the_real_aunt = False
            break
    if the_real_aunt:
        print('The aunt who sent the gift was Aunt Sue #', aunt + 1)
