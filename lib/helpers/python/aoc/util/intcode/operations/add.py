from util.intcode.operations.op import Op
from util.intcode.state import State


class Add(Op):
    OPCODE = 1
    DEBUG = False

    def __init__(self, mode):
        super().__init__(opcode=Add.OPCODE, mode=mode, params_count=3, write_params=[2])

    def apply(self, state: State):
        [op1, op2, dest] = self.params(state)
        state.program[dest] = op1 + op2
        super().apply(state)
