from util.intcode.operations.op import Op
from util.intcode.state import State


class LessThan(Op):
    OPCODE = 7
    DEBUG = False

    def __init__(self, mode):
        super().__init__(
            opcode=LessThan.OPCODE, mode=mode, params_count=3, write_params=[2]
        )

    def apply(self, state: State):
        [op1, op2, dest] = self.params(state)
        state.program[dest] = 1 if op1 < op2 else 0
        super().apply(state)
