from aoc import AOC

aoc = AOC(year=2021, day=4)
data = aoc.load()
# data._contents = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7"""


series = data.numbers_by_line()

bingo_cards = []
next_card = []
for n in series[2:]:
  if not n:
    bingo_cards.append(next_card)
    next_card = []
    continue

  next_card.append(n)

bingo_cards.append(next_card)
# aoc.d(bingo_cards)

draws = data.numbers_by_line()[0]

def bingo(b):
  cols = [[b[r][c] for r in range(5)] for c in range(5)]
  for row in b:
    if row == [None] * 5:
      return True
  for col in cols:
    if col == [None] * 5:
      return True

  return False

binged = None
binged_board = None
for d in draws:
  # print("drawing", d)
  if binged:
    break

  for b in bingo_cards:
    for r in range(5):
      for c in range(5):
        if b[r][c] == d:
          b[r][c] = None

    if bingo(b):
      binged = d
      binged_board = b
      break

# print(binged)

unmarked = sum(binged_board[r][c] if binged_board[r][c] else 0 for r in range(5) for c in range(5))
aoc.p1(unmarked * binged)
# unmarked = sum(b[r][c] if b[r][c] else 0 for b in bingo_cards for r in range(5) for c in range(5))


from aoc import AOC

aoc = AOC(year=2021, day=4)
data = aoc.load()
# data._contents = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7"""


series = data.numbers_by_line()

bingo_cards = []
next_card = []
for n in series[2:]:
  if not n:
    bingo_cards.append(next_card)
    next_card = []
    continue

  next_card.append(n)

bingo_cards.append(next_card)
# aoc.d(bingo_cards)

draws = data.numbers_by_line()[0]

def bingo(b):
  cols = [[b[r][c] for r in range(5)] for c in range(5)]
  for row in b:
    if row == [None] * 5:
      return True
  for col in cols:
    if col == [None] * 5:
      return True

  return False

binged = None
binged_board = None
solved = {}
next_binger = False
for d in draws:
  if binged:
    break

  for i, b in enumerate(bingo_cards):
    for r in range(5):
      for c in range(5):
        if b[r][c] == d:
          b[r][c] = None

    if bingo(b):
      if next_binger and i not in solved:
        binged_board = b
        binged = d

      solved[i] = True

      if len(solved) == len(bingo_cards) - 1:
        next_binger = True


# print(binged)

unmarked = sum(binged_board[r][c] if binged_board[r][c] else 0 for r in range(5) for c in range(5))
aoc.p2(unmarked * binged)
# unmarked = sum(b[r][c] if b[r][c] else 0 for b in bingo_cards for r in range(5) for c in range(5))

# aoc.p1(unmarked * binged)
# unmarked = 0
# for b in bingo_cards:
#   for r in range(5):
#     for c in range(5):
#       unmarked += b[r][c] if b[r][c] else 0
# aoc.p1(unmarked * binged)
