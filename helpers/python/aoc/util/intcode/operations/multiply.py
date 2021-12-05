from util.intcode.operations.op import Op
from util.intcode.state import State


class Multiply(Op):
    OPCODE = 2

    def __init__(self):
        super().__init__(opcode=Multiply.OPCODE, params_count=3)

    def apply(self, state: State):
        [op1, op2, dest] = self.params(state)
        state.program[dest] = state.program[op1] * state.program[op2]
        super().apply(state)
