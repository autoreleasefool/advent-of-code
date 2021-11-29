from aoc import AOC

aoc = AOC(year=2015, day=20)

## Part 1

# Get a list of all the factors of x
def get_factors(x):
    factors = []

    # All values are divisible by 1
    factors.append(1)
    # Loop until at most the sqrt(x)
    for i in range(2, int(x ** (1.0 / 2.0)) + 1):
        # If the value divides x, add it and the other factor to the list
        if x % i == 0:
            factors.append(i)
            if x / i != i:
                factors.append(int(x / i))

    # All values are divisible by themselves (but 1 has already been added)
    if x > 1:
        factors.append(x)
    return factors


# Returns the first house that receives a number of presents of at least the target value
def find_minimum_house(target):
    i = 0
    while True:
        i += 1
        total = 0
        # For every factor, add the presents delivered to the total
        for factor in get_factors(i):
            total += factor * 10

        # If the total is greater that the target, return the value
        if total >= target:
            return i


# Get the house which receives at least the minimum
aoc.p1(find_minimum_house(34000000))

## Part 2

# The number of houses a certain elf has delivered to
number_of_houses_delivered = {}

# Get a list of all the factors of x
def get_factors(x):
    factors = []

    # All values are divisible by 1
    factors.append(1)
    # Loop until at most the sqrt(x)
    for i in range(2, int(x ** (1.0 / 2.0)) + 1):
        # If the value divides x, add it and the other factor to the list
        if x % i == 0:
            factors.append(i)
            if x / i != i:
                factors.append(int(x / i))

    # All values are divisible by themselves (but 1 has already been added)
    if x > 1:
        factors.append(x)
    return factors


# Returns the first house that receives a number of presents of at least the target value
def find_minimum_house(target):
    i = 0
    while True:
        i += 1
        total = 0

        # For every factor, add the presents delivered to the total
        for factor in get_factors(i):

            # Elves only deliver up to 50 houses
            if factor in number_of_houses_delivered:
                if number_of_houses_delivered[factor] < 50:
                    total += factor * 11
                number_of_houses_delivered[factor] += 1
            else:
                total += factor * 11
                number_of_houses_delivered[factor] = 1

        # If the total is greater that the target, return the value
        if total >= target:
            return i


# Get the house which receives at least the minimum
aoc.p2(find_minimum_house(34000000))
