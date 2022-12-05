from aoc import AOC
from typing import Dict, List

aoc = AOC(year=2016, day=12)
data = aoc.load()

class Computer:

    reg: Dict[str, int]
    ins: List[str]
    pos: int

    def __init__(self, ins: List[str], ignition: bool=False) -> None:
        self.reg = { 'a': 0, 'b': 0, 'c': 1 if ignition else 0, 'd': 0 }
        self.ins = ins
        self.pos = 0

    def copy(self, x, y):
        self.reg[y] = self.reg[x] if x in self.reg else int(x)
        self.pos += 1

    def increase(self, x):
        self.reg[x] += 1
        self.pos += 1

    def decrease(self, x):
        self.reg[x] -= 1
        self.pos += 1

    def jump(self, x, y):
        x = self.reg[x] if x in self.reg else int(x)
        if x != 0:
            self.pos += int(y)
        else:
            self.pos += 1

    def run(self):
        while self.pos < len(self.ins):
            ins = self.ins[self.pos].split(' ')
            match ins[0]:
                case 'cpy':
                    self.copy(ins[1], ins[2])
                case 'inc':
                    self.increase(ins[1])
                case 'dec':
                    self.decrease(ins[1])
                case 'jnz':
                    self.jump(ins[1], ins[2])

computer = Computer(data.lines())
computer.run()
aoc.p1(computer.reg['a'])

computer = Computer(data.lines(), ignition=True)
computer.run()
aoc.p2(computer.reg['a'])
