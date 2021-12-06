from typing import List
from util.intcode.operations.op import Op
from util.intcode.state import State


class Read(Op):
    OPCODE = 3

    def __init__(self, mode: List[int]):
        super().__init__(
            opcode=Read.OPCODE, mode=mode, params_count=1, write_params=[0]
        )

    def apply(self, state: State):
        [dest] = self.params(state)
        state.program[dest] = state.next_input
        super().apply(state)
