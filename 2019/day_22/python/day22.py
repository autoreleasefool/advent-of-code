from aoc import AOC, Deck
from dataclasses import dataclass


aoc = AOC(year=2019, day=22)
data = aoc.load()
deck = Deck(size=10007)


class Instruction:
    instruction: str
    value: int

    def __init__(self, groups):
        self.instruction = groups[0]
        self.value = int(groups[1]) if groups[1] != "stack" else None


for i in data.parse_lines(r"(.*?)(-?\d+|stack)", container=Instruction):
    if i.instruction[:3] == "cut":
        deck.cut(i.value)
    elif "increment" in i.instruction:
        deck.deal(i.value)
    else:
        deck.reverse()


aoc.p1(deck.position_of_card(2019))
