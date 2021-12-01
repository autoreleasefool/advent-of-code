from enum import Enum
from util.position import Position


class Direction(Enum):
    N = (0, -1)
    E = (1, 0)
    S = (0, 1)
    W = (-1, 0)

    @property
    def position(self):
        return Position(self.value[0], self.value[1])
