from collections import defaultdict
from enum import Enum
from aoc import AOC


class Ops(Enum):
    ADD = 1
    MULTIPLY = 2
    HALT = 99


class IntcodeComputer:
    def __init__(self, aoc: AOC):
        self.aoc = aoc
        self.pointer = 0
        self.program = defaultdict(int)
        for i, n in enumerate(aoc.load().nums()):
            self.program[i] = n

    def run(self):
        while not self.is_halted:
            self.run_operation()

    def run_operation(self):
        ins = self.program[self.pointer]
        if ins == Ops.ADD.value:
            self._add()
        elif ins == Ops.MULTIPLY.value:
            self._mult()

    def _add(self):
        first_param = self.program[self.pointer + 1]
        second_param = self.program[self.pointer + 2]
        store = self.program[self.pointer + 3]
        self.program[store] = self.program[first_param] + self.program[second_param]
        self.pointer += 4

    def _mult(self):
        first_param = self.program[self.pointer + 1]
        second_param = self.program[self.pointer + 2]
        store = self.program[self.pointer + 3]
        self.program[store] = self.program[first_param] * self.program[second_param]
        self.pointer += 4

    @property
    def is_halted(self) -> bool:
        return self.program[self.pointer] == Ops.HALT.value

    @property
    def output(self) -> int:
        return self.program[0]
