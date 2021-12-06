from util.intcode.operations.op import Op
from util.intcode.state import State


class JumpIfFalse(Op):
    OPCODE = 6
    DEBUG = False

    def __init__(self, mode):
        super().__init__(opcode=JumpIfFalse.OPCODE, mode=mode, params_count=2)

    def apply(self, state: State):
        [comparator, dest] = self.params(state)
        if comparator == 0:
            state.pointer = dest
        else:
            super().apply(state)
