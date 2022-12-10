from aoc import AOC, stringifygrid
from dataclasses import dataclass, field
from typing import List

aoc = AOC(year=2022, day=10)
data = aoc.load()

@dataclass
class State:
    register: int = 1
    cycle: int = 1
    strengths: List[int] = field(default_factory=list)
    read_points: List[int] = field(default_factory=lambda: [20, 60, 100, 140, 180, 220])
    crt: List[List[int]] = field(default_factory=lambda: [['.' for _ in range(40)] for _ in range(6)])

    def advance_crt(self):
        coord = ((self.cycle - 1) % 40, (self.cycle - 1) // 40)
        if self.register - 1 <= coord[0] <= self.register + 1 and self.cycle <= 240:
            self.crt[coord[1]][coord[0]] = '#'

    def advance_cycle(self):
        self.cycle += 1

        if self.cycle in self.read_points:
            self.strengths.append(self.cycle * self.register)


state = State()
for cmd in data.lines():
    cmd = cmd.split(' ')
    match cmd[0]:
        case 'noop':
            state.advance_crt()
            state.advance_cycle()
        case 'addx':
            state.advance_crt()
            state.advance_cycle()
            state.advance_crt()
            state.register += int(cmd[1])
            state.advance_cycle()

aoc.p1(sum(state.strengths))
aoc.p2(stringifygrid(state.crt))
