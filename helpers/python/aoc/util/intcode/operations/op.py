from abc import ABC, abstractmethod
from typing import DefaultDict
from util.intcode.state import State


class Op(ABC):
    opcode: int
    params_count: int

    def __init__(self, opcode: int, params_count: int):
        self.opcode = opcode
        self.params_count = params_count

    @abstractmethod
    def apply(self, state: State):
        state.pointer += self.params_count + 1

    def params(self, state: State):
        return [
            state.program[state.pointer + i] for i in range(1, self.params_count + 1)
        ]
