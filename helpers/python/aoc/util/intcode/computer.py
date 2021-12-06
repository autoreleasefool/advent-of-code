from collections import defaultdict
from util.functions import digits
from util.data.data import Data
from util.intcode.state import State
from util.intcode.operations import (
    Add,
    Halt,
    Multiply,
    Op,
    Read,
    Write,
    JumpIfTrue,
    JumpIfFalse,
    LessThan,
    Equals,
)


POSSIBLE_OPS = [
    Add,
    Halt,
    Multiply,
    Read,
    Write,
    JumpIfTrue,
    JumpIfFalse,
    LessThan,
    Equals,
]


class IntcodeComputer:
    def __init__(self, data: Data, debug=False):
        self.state = State(program=defaultdict(int))
        self.debug = debug
        for i, n in enumerate(data.nums()):
            self.state.program[i] = n

        for op in POSSIBLE_OPS:
            op.DEBUG = debug
        Op.DEBUG = debug

    def run(self):
        while not self.is_halted:
            self.run_next()

    def run_next(self):
        self.op.apply(self.state)
        if self.debug:
            print(self.state.program)

    @property
    def is_halted(self) -> bool:
        return self.state.instruction[0] == Halt.OPCODE

    @property
    def output(self) -> int:
        return self.state.output

    @property
    def op(self) -> Op:
        opcode, mode = self.state.instruction
        for op in POSSIBLE_OPS:
            if opcode == op.OPCODE:
                return op(mode)

        raise LookupError(f"{opcode} is not a valid instruction")
