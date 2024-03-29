from aoc import AOC


aoc = AOC(year=2015, day=17)


## Part 1

# Initialize and sort the puzzle input
PUZZLE_INPUT = [
    33,
    14,
    18,
    20,
    45,
    35,
    16,
    35,
    1,
    13,
    18,
    13,
    50,
    44,
    48,
    6,
    24,
    41,
    30,
    42,
]
container_sizes = PUZZLE_INPUT
container_sizes.sort(reverse=True)

# Total amount of eggnog to store
target_eggnog = 150


def get_arrangements(containers_total, remaining_containers):
    # Gets the number of arrangements of containers to store the eggnog
    # containers_total is the total amount of the containers used so far
    # remaining_containers is the unused containers
    arrangements = 0

    # If there are no more containers, then the target amount won't be met
    if len(remaining_containers) == 0:
        return 0

    # Iterate over each of the remaining containers
    for i in range(len(remaining_containers) - 1, -1, -1):
        # If the target eggnog amount is met, then add the arrangement to the total
        if containers_total + remaining_containers[i] == target_eggnog:
            arrangements += 1
        # If the total is too large, then only larger containers are remaining
        elif containers_total + remaining_containers[i] > target_eggnog:
            break
        # If the total is too small, keep iterating over the remaining containers
        elif i > 0:
            arrangements += get_arrangements(
                containers_total + remaining_containers[i], remaining_containers[:i]
            )

    # Return the total number of arrangements made from this iteration
    return arrangements


# Gets the number of total container arrangements
total_arrangements = get_arrangements(0, PUZZLE_INPUT)

aoc.p1(total_arrangements)

## Part 2

# Initialize and sort the puzzle input
PUZZLE_INPUT = [
    33,
    14,
    18,
    20,
    45,
    35,
    16,
    35,
    1,
    13,
    18,
    13,
    50,
    44,
    48,
    6,
    24,
    41,
    30,
    42,
]
container_sizes = PUZZLE_INPUT
container_sizes.sort(reverse=True)

# Total amount of eggnog to store
target_eggnog = 150
minimum_containers = -1
minimum_arrangements = -1


def get_arrangements(containers_used, remaining_containers):
    # Gets the number of arrangements of containers to store the eggnog
    # containers_total is the total amount of the containers used so far
    # remaining_containers is the unused containers
    global minimum_containers
    global minimum_arrangements

    # If there are no more containers, then the target amount won't be met
    if len(remaining_containers) == 0:
        return

    # Get the total size of all the containers
    containers_total = sum(containers_used)

    # Iterate over each of the remaining containers
    for i in range(len(remaining_containers) - 1, -1, -1):
        # If the target eggnog amount is met, then check if the number of containers is the minimum
        if containers_total + remaining_containers[i] == target_eggnog:
            if (
                minimum_containers == -1
                or len(containers_used) + 1 < minimum_containers
            ):
                minimum_containers = len(containers_used) + 1
                minimum_arrangements = 1
            elif len(containers_used) + 1 == minimum_containers:
                minimum_arrangements += 1
        # If the total is too large, then only larger containers are remaining
        elif containers_total + remaining_containers[i] > target_eggnog:
            break
        # If the total is too small, keep iterating over the remaining containers
        elif i > 0:
            updated_containers_used = containers_used[:]
            updated_containers_used.append(remaining_containers[i])
            get_arrangements(updated_containers_used, remaining_containers[:i])


# Gets the number of total container arrangements
get_arrangements([], PUZZLE_INPUT)

aoc.p2(minimum_arrangements)
