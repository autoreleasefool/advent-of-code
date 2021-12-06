from util.intcode.operations.op import Op
from util.intcode.state import State


class Equals(Op):
    OPCODE = 8
    DEBUG = False

    def __init__(self, mode):
        super().__init__(
            opcode=Equals.OPCODE, mode=mode, params_count=3, write_params=[2]
        )

    def apply(self, state: State):
        [op1, op2, dest] = self.params(state)
        state.program[dest] = 1 if op1 == op2 else 0
        super().apply(state)
