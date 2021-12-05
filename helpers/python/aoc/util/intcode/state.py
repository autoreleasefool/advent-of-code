from collections import defaultdict
from typing import DefaultDict
from aoc import AOC
from util.intcode.mode import Mode


class State:
    def __init__(
        self,
        program: DefaultDict[int, int],
        pointer: int = 0,
        mode: Mode = Mode.POSITION,
    ):
        self.program = program
        self.pointer = pointer
        self.mode = mode

    @property
    def output(self):
        return self.program[0]

    @property
    def instruction(self):
        return self.program[self.pointer]
