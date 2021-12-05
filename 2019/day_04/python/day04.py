from aoc import AOC, chunk

aoc = AOC(year=2019, day=4)
password_range = range(256310, 732736 + 1)

# Part 1


def has_pair(p):
    return any(x == y for x, y in zip(p[:-1], p[1:]))


def never_decreases(p):
    return all(int(y) >= int(x) for x, y in zip(p[:-1], p[1:]))


def is_valid(p):
    return has_pair(str(p)) and never_decreases(str(p))


valid_passwords = sum(1 for p in password_range if is_valid(p))
aoc.p1(valid_passwords)

# Part 2


def has_pair(p):
    p = [None, None] + list(p) + [None, None]
    return any(
        x == y and x != w and y != z
        for w, x, y, z in zip(p[:-3], p[1:-2], p[2:-1], p[3:])
    )


valid_passwords = sum(1 for p in password_range if is_valid(p))
aoc.p2(valid_passwords)
