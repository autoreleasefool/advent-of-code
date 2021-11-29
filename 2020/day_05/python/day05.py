from aoc import AOC

aoc = AOC(year=2020, day=5)
data = aoc.load()

# Part 1


def bin_search(commands, lower, upper):
    for idx, dir in enumerate(commands):
        mid = (lower + upper) // 2
        if dir == "F" or dir == "L":
            upper = mid
        elif dir == "B" or dir == "R":
            lower = mid + 1
    return [lower, upper]


def seat_id(boarding_pass):
    lower, upper = bin_search(boarding_pass[:7], 0, 127)
    row = lower if boarding_pass[6] == "B" else upper

    lower, upper = bin_search(boarding_pass[7:], 0, 7)
    col = lower if boarding_pass[-1] == "R" else upper

    return row * 8 + col


seats = [seat_id(p) for p in data.lines()]

aoc.p1(max(seats))

# Part 2
seats = set(seats)
aoc.p2(next(sid for sid in seats if (sid + 1) not in seats) + 1)
