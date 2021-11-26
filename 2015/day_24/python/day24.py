import aoc
from operator import mul
from functools import reduce

data = aoc.load(year=2015, day=24)

## Part 1

total_weight = 0
weights = []

for line in data.lines():
    w = int(line)
    total_weight += w
    weights.append(w)

# Get the weights from heaviest to lightest
weights.sort(reverse=True)

# Goal is to get 3 groups of exactly this weight
target_weight = total_weight // 3

minimum_presents = -1
quantum_entanglement = -1
potential_first_bags = []


def bag_it(ws, add_to_compilation, compilation, bag):
    current_weight = sum(bag)
    if current_weight == target_weight:
        if add_to_compilation:
            compilation.append(bag)
        return True
    if current_weight > target_weight:
        return False

    bagged = False
    for i, weight in enumerate(ws):
        remaining = ws[i + 1 :]
        bagged = (
            bag_it(remaining, add_to_compilation, compilation, bag + [weight]) or bagged
        )
        if not add_to_compilation and bagged:
            return True
    return bagged


bag_it(weights, True, potential_first_bags, [])
for first_bag in potential_first_bags:
    if minimum_presents != -1 and minimum_presents < len(first_bag):
        continue

    bag_entanglement = reduce(mul, first_bag)
    if quantum_entanglement != -1 and bag_entanglement > quantum_entanglement:
        continue

    b = first_bag[:]
    remaining_weights = weights[:]
    while b:
        remaining_weights.remove(b.pop())
    if bag_it(remaining_weights, False, None, []):
        minimum_presents = len(first_bag)
        quantum_entanglement = bag_entanglement

p1_solution = quantum_entanglement
print(p1_solution)

## Part 2

total_weight = 0
weights = []

for line in data.lines():
    w = int(line)
    total_weight += w
    weights.append(w)

# Get the weights from heaviest to lightest
weights.sort(reverse=True)

# Goal is to get 4 groups of exactly this weight
target_weight = total_weight // 4

minimum_presents = -1
quantum_entanglement = -1
potential_first_bags = []


def bag_it(ws, add_to_compilation, compilation, bag):
    current_weight = sum(bag)
    if current_weight == target_weight:
        if add_to_compilation:
            compilation.append(bag)
        return True
    if current_weight > target_weight:
        return False

    bagged = False
    for i, weight in enumerate(ws):
        remaining = ws[i + 1 :]
        bagged = (
            bag_it(remaining, add_to_compilation, compilation, bag + [weight]) or bagged
        )
        if not add_to_compilation and bagged:
            return True
    return bagged


bag_it(weights, True, potential_first_bags, [])
for first_bag in potential_first_bags:
    if minimum_presents != -1 and minimum_presents < len(first_bag):
        continue

    bag_entanglement = reduce(mul, first_bag)
    if quantum_entanglement != -1 and bag_entanglement > quantum_entanglement:
        continue

    potential_second_bags = []
    b = first_bag[:]
    remaining_weights = weights[:]
    while b:
        remaining_weights.remove(b.pop())

    bag_it(remaining_weights, True, potential_second_bags, [])
    for second_bag in potential_second_bags:
        bag_again = second_bag[:]
        remaining_weights_again = remaining_weights[:]
        while bag_again:
            remaining_weights_again.remove(bag_again.pop())
        if bag_it(remaining_weights, False, None, []):
            minimum_presents = len(first_bag)
            quantum_entanglement = bag_entanglement

p2_solution = quantum_entanglement
print(p2_solution)
