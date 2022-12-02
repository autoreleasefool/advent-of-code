from aoc import AOC

aoc = AOC(year=2022, day=2)
data = aoc.load()

playing_rock = 1
playing_paper = 2
playing_scissors = 3

winning = 6
drawing = 3
losing = 0

score = 0
for line in data.lines():
    opponent, player = line.split()
    match line.split():
        case ['A', 'X']: score += playing_rock + drawing
        case ['A', 'Y']: score += playing_paper + winning
        case ['A', 'Z']: score += playing_scissors + losing
        case ['B', 'X']: score += playing_rock + losing
        case ['B', 'Y']: score += playing_paper + drawing
        case ['B', 'Z']: score += playing_scissors + winning
        case ['C', 'X']: score += playing_rock + winning
        case ['C', 'Y']: score += playing_paper + losing
        case ['C', 'Z']: score += playing_scissors + drawing

aoc.p1(score)

score = 0
for line in data.lines():
    opponent, player = line.split()
    match line.split():
        case ['A', 'X']: score += playing_scissors + losing
        case ['A', 'Y']: score += playing_rock + drawing
        case ['A', 'Z']: score += playing_paper + winning
        case ['B', 'X']: score += playing_rock + losing
        case ['B', 'Y']: score += playing_paper + drawing
        case ['B', 'Z']: score += playing_scissors + winning
        case ['C', 'X']: score += playing_paper + losing
        case ['C', 'Y']: score += playing_scissors + drawing
        case ['C', 'Z']: score += playing_rock + winning

aoc.p2(score)
