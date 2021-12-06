from typing import List
from util.intcode.operations.op import Op
from util.intcode.state import State


class Write(Op):
    OPCODE = 4

    def __init__(self, mode: List[int]):
        super().__init__(
            opcode=Write.OPCODE, mode=mode, params_count=1, write_params=[0]
        )

    def apply(self, state: State):
        [source] = self.params(state)
        state.add_output(state.program[source])
        super().apply(state)
