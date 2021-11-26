import aoc
import re

data = aoc.load(year=2015, day=19)

## Part 1

# Initialize the dictionary of available replacements, and the combinations made
replacements = {}
input_molecule = None
combinations = {}

# FOr each line in the input
for line in data.lines():
    # If the line does not contain '=>', then it is the initial molecule
    if not "=>" in line and len(line) > 1:
        input_molecule = list(line)
    # Otherwise, the line represents a replacement. Add it to the available replacements
    elif "=>" in line:
        replacement = re.search(r"(\w+) => (\w+)", line)
        if replacement.group(1) in replacements:
            replacements[replacement.group(1)].append(replacement.group(2))
        else:
            replacements[replacement.group(1)] = [replacement.group(2)]

# For each character in the initial molecule
for i, _ in enumerate(input_molecule):
    # If the character can be replaced, add the replacement to the list of combinations made
    if input_molecule[i] in replacements:
        for replacement in replacements[input_molecule[i]]:
            new_combination = (
                "".join(input_molecule[:i])
                + replacement
                + "".join(input_molecule[i + 1 :])
            )
            combinations[new_combination] = 1
    # If 2 characters in a row can be replaced, add their replacement as well
    # The longest replacement is only 2 chars, so we only need to do this for up to 2
    substring_len_2 = "".join(input_molecule[i : i + 2])
    if substring_len_2 in replacements:
        for replacement in replacements[substring_len_2]:
            new_combination = (
                "".join(input_molecule[:i])
                + replacement
                + "".join(input_molecule[i + 2 :])
            )
            combinations[new_combination] = 1

p1_solution = len(combinations)
print(p1_solution)

## Part 2

# Initialize the dictionary of available replacements, and the combinations made
replacements = {}
target_molecule = None
combinations = {}

# For each line in the input
for line in data.lines():
    # If the line does not contain '=>', then it is the initial molecule
    if not "=>" in line and len(line) > 1:
        target_molecule = line.rstrip().lstrip()

    # Otherwise, the line represents a replacement. Add it to the available replacements
    elif "=>" in line:
        replacement = re.search(r"(\w+) => (\w+)", line)
        if replacement.group(2) in replacements:
            replacements[replacement.group(2)].append(replacement.group(1))
        else:
            replacements[replacement.group(2)] = [replacement.group(1)]

min_steps = -1
max_steps = 0
potential = [(target_molecule, 0)]
while potential:
    molecule, steps = potential.pop()
    if min_steps != -1 and steps > min_steps:
        continue

    for key in replacements:
        for loc in re.finditer(key, molecule):
            for rep in replacements[key]:

                # Get the new molecule made from the replacement
                replaced = (
                    molecule[0 : loc.start()] + rep + molecule[loc.start() + len(key) :]
                )

                # Ensure a combination is not used more than once
                if replaced in combinations:
                    continue
                combinations[replaced] = True

                if replaced == "e":
                    print("Reached 'e' in", steps + 1, "steps.")
                    if steps + 1 < min_steps or min_steps == -1:
                        min_steps = steps + 1
                else:
                    potential.append((replaced, steps + 1))

p2_solution = min_steps
print(p2_solution)
