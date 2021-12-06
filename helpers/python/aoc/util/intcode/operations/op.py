from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Set
from util.intcode.state import State


class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1


class Op(ABC):
    DEBUG = False
    opcode: int
    mode: List[int]
    params_count: int
    write_params: Set[int]

    def __init__(
        self,
        opcode: int,
        mode: List[int],
        params_count: int,
        write_params: Set[int] = None,
    ):
        self.opcode = opcode
        self.mode = mode + ([0] * (params_count - len(mode)))
        self.params_count = params_count
        self.write_params = write_params if write_params else set()
        if Op.DEBUG:
            print(f"Creating op {opcode} with {self.mode}")

    @abstractmethod
    def apply(self, state: State):
        state.pointer += self.params_count + 1

    def params(self, state: State):
        return [
            state.program[p]
            if self.mode[i] == ParameterMode.POSITION.value
            and i not in self.write_params
            else p
            for i, p in enumerate(
                [
                    state.program[state.pointer + i]
                    for i in range(1, self.params_count + 1)
                ]
            )
        ]
