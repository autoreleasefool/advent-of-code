from typing import List
from util.intcode.operations.op import Op
from util.intcode.state import State


class Halt(Op):
    OPCODE = 99
    DEBUG = False

    def __init__(self, _):
        super().__init__(opcode=Halt.OPCODE, mode=[], params_count=0)

    def apply(self, _):
        pass
