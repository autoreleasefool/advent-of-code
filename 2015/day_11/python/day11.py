from aoc import AOC


aoc = AOC(year=2015, day=11)

## Part 1

# The original password
PUZZLE_INPUT = ["v", "z", "b", "x", "k", "g", "h", "b"]


def three_straight_letters(password):
    # Checks for a row of 3 letters in the password
    for i in range(len(password) - 3):
        for j in range(2):
            if not ord(password[i + j]) + 1 == ord(password[i + j + 1]):
                break
            if j == 1:
                return True
    return False


def has_double_doubles(password):
    # Checks for 2 different sets of doubles in the password
    double_count = 0
    last_double = None
    for i in range(len(password) - 1):
        if password[i] != last_double and password[i] == password[i + 1]:
            double_count += 1
            if double_count == 2:
                return True
            last_double = password[i]
    return False


def increment_by_one(position, password):
    # Move the letter at position up by 1
    # If the letter is 'z', make it 'a' and increment the previous letter
    # Skip the letters 'i', 'o' and 'l'
    if password[position] == "z":
        password[position] = "a"
        increment_by_one(position - 1, password)
    else:
        password[position] = chr(ord(password[position]) + 1)
        if password[position] in {"i", "o", "l"}:
            password[position] = chr(ord(password[position]) + 1)
    return password


def increment_all_until_valid(password):
    # Skips any letters in the entire string which are 'i', 'o', or 'l'
    for i, letter in enumerate(password):
        if letter in {"i", "o", "l"}:
            increment_by_one(i)
            for j in range(i + 1, len(password)):
                password[j] = "a"
    return password


# Increment until the password is valid
password = increment_by_one(7, PUZZLE_INPUT)
password = increment_all_until_valid(password)
while not has_double_doubles(password) or not three_straight_letters(password):
    password = increment_by_one(7, password)

aoc.p1("".join(password))

## Part 2

# The original password
PUZZLE_INPUT = ["v", "z", "b", "x", "k", "g", "h", "b"]


def three_straight_letters(password):
    # Checks for a row of 3 letters in the password
    for i in range(len(password) - 3):
        for j in range(2):
            if not ord(password[i + j]) + 1 == ord(password[i + j + 1]):
                break
            if j == 1:
                return True

    return False


def has_double_doubles(password):
    # Checks for 2 different sets of doubles in the password
    double_count = 0
    last_double = None
    for i in range(len(password) - 1):
        if password[i] != last_double and password[i] == password[i + 1]:
            double_count += 1
            if double_count == 2:
                return True
            last_double = password[i]
    return False


def increment_by_one(position, password):
    # Move the letter at position up by 1
    # If the letter is 'z', make it 'a' and increment the previous letter
    # Skip the letters 'i', 'o' and 'l'
    if password[position] == "z":
        password[position] = "a"
        increment_by_one(position - 1, password)
    else:
        password[position] = chr(ord(password[position]) + 1)
        if password[position] in {"i", "o", "l"}:
            password[position] = chr(ord(password[position]) + 1)
    return password


def increment_all_until_valid(password):
    # Skips any letters in the entire string which are 'i', 'o', or 'l'
    for i, letter in enumerate(password):
        if letter in {"i", "o", "l"}:
            increment_by_one(i)
            for j in range(i + 1, len(password)):
                password[j] = "a"
    return password


# Increment until the password is valid
password = increment_by_one(7, PUZZLE_INPUT)
password = increment_all_until_valid(password)
while not has_double_doubles(password) or not three_straight_letters(password):
    password = increment_by_one(7, password)

# Increment until the password is valid
password = increment_by_one(7, password)
password = increment_all_until_valid(password)
while not has_double_doubles(password) or not three_straight_letters(password):
    password = increment_by_one(7, password)

aoc.p1("".join(password))
