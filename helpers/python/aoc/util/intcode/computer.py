from collections import defaultdict
from aoc import AOC
from util.intcode.state import State
from util.intcode.operations import Add, Halt, Multiply, Op


class IntcodeComputer:
    def __init__(self, aoc: AOC):
        self.state = State(program=defaultdict(int))
        for i, n in enumerate(aoc.load().nums()):
            self.state.program[i] = n

    def run(self):
        while not self.is_halted:
            self.run_next()

    def run_next(self):
        self.op.apply(self.state)

    @property
    def is_halted(self) -> bool:
        return self.op.opcode == Halt.OPCODE

    @property
    def output(self) -> int:
        return self.state.output

    @property
    def op(self) -> Op:
        if self.instruction == Add.OPCODE:
            return Add()
        elif self.instruction == Multiply.OPCODE:
            return Multiply()
        elif self.instruction == Halt.OPCODE:
            return Halt()

        raise LookupError(f"{self.instruction} is not a valid instruction")

    @property
    def instruction(self) -> int:
        return self.state.instruction
