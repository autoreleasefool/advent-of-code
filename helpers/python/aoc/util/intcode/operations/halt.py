from util.intcode.operations.op import Op
from util.intcode.state import State


class Halt(Op):
    OPCODE = 99

    def __init__(self):
        super().__init__(opcode=Halt.OPCODE, params_count=0)

    def apply(self, state: State):
        pass
