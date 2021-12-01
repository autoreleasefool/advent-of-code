from aoc import AOC, Drop, Numbers

aoc = AOC(year=2020, day=22)
data = aoc.load()

hands = data.chunk(
    [
        Drop(1),
        Numbers(),
        Drop(2),
        Numbers(),
    ]
)

first_hand = hands[0][:]
second_hand = hands[1][:]


def calculate_score(hand):
    return sum([(i + 1) * h for i, h in enumerate(reversed(hand))])


# Part 1


def play_round():
    p1 = first_hand.pop(0)
    p2 = second_hand.pop(0)

    if p1 > p2:
        first_hand.append(p1)
        first_hand.append(p2)
    else:
        second_hand.append(p2)
        second_hand.append(p1)


while first_hand and second_hand:
    play_round()

aoc.p1(calculate_score(first_hand if first_hand else second_hand))

# Part 2

first_hand = hands[0][:]
second_hand = hands[1][:]


def play_game(first_hand, second_hand):
    previous_deck_orders = set()
    while first_hand and second_hand:
        tuple_first = tuple(first_hand)
        tuple_second = tuple(second_hand)
        if (tuple_first, tuple_second) in previous_deck_orders:
            return 1
        previous_deck_orders.add((tuple_first, tuple_second))

        p1 = first_hand.pop(0)
        p2 = second_hand.pop(0)

        if len(first_hand) >= p1 and len(second_hand) >= p2:
            winner = play_game(first_hand[:p1], second_hand[:p2])
        else:
            winner = 1 if p1 > p2 else 2

        if winner == 1:
            first_hand.append(p1)
            first_hand.append(p2)
        else:
            second_hand.append(p2)
            second_hand.append(p1)

    return 1 if first_hand else 2


while first_hand and second_hand:
    play_game(first_hand, second_hand)

aoc.p2(calculate_score(first_hand if first_hand else second_hand))
