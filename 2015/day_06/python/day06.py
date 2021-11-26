import aoc
import re

data = aoc.load(year=2015, day=6)

## Part 2

# Initialize all lights to off in 1000x1000 matrix
value_to_set = 0
lights_on = 0
light_matrix = [[0 for i in range(1000)] for j in range(1000)]

# Regular expression to find values of coordinates
coordinates_regex = re.compile(r"\d+")

# For every line in the input
for line in data.lines():

    # Set lights to on, off, or toggle them
    if "on" in line:
        value_to_set = 1
    elif "off" in line:
        value_to_set = 0
    else:
        value_to_set = "toggle"

    # Getting coordinates of lights to be adjusted
    lights_to_change = re.findall(coordinates_regex, line)
    lights_to_change = [int(i) for i in lights_to_change[:4]]

    # For each light in the range, adjust its value
    for x in range(lights_to_change[0], lights_to_change[2] + 1):
        for y in range(lights_to_change[1], lights_to_change[3] + 1):
            if value_to_set == "toggle":
                if light_matrix[x][y] == 0:
                    light_matrix[x][y] = 1
                else:
                    light_matrix[x][y] = 0
            else:
                light_matrix[x][y] = value_to_set

# Count the lights that remain on
for x in range(1000):
    for y in range(1000):
        if light_matrix[x][y] == 1:
            lights_on += 1

p1_solution = lights_on
print(p1_solution)

## Part 2

# Initialize all lights to off in 1000x1000 matrix
value_to_offset = 0
total_brightness = 0
light_matrix = [[0 for i in range(1000)] for j in range(1000)]

# Regular expression to find values of coordinates
coordinates_regex = re.compile(r"\d+")

# For every line in the input
for line in data.lines():

    # Set lights to on, off, or toggle them
    if "on" in line:
        value_to_offset = 1
    elif "off" in line:
        value_to_offset = -1
    else:
        value_to_offset = 2

    # Getting coordinates of lights to be adjusted
    lights_to_change = re.findall(coordinates_regex, line)
    lights_to_change = [int(i) for i in lights_to_change[:4]]

    # For each light in the range, adjust its value
    for x in range(lights_to_change[0], lights_to_change[2] + 1):
        for y in range(lights_to_change[1], lights_to_change[3] + 1):
            light_matrix[x][y] = max(light_matrix[x][y] + value_to_offset, 0)

# Count the lights that remain on
for x in range(1000):
    for y in range(1000):
        total_brightness += light_matrix[x][y]

p2_solution = total_brightness
print(p2_solution)
