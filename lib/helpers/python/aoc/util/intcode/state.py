from typing import DefaultDict, List, Tuple
from aoc import AOC
from util.functions import digits
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
        self.inputs = []
        self.outputs = []

    @property
    def output(self):
        return self.program[0]

    @property
    def next_input(self):
        return self.inputs.pop(0)

    def add_input(self, input):
        self.inputs.append(input)

    def add_output(self, output):
        self.outputs.append(output)

    @property
    def instruction(self) -> Tuple[int, List[int]]:
        instruction = digits(self.program[self.pointer])
        if len(instruction) == 1:
            opcode = instruction[0]
            mode = []
        else:
            opcode = instruction[-2] * 10 + instruction[-1]
            mode = [] if len(instruction) == 2 else instruction[-3::-1]

        return opcode, mode
