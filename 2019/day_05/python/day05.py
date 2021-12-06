from aoc import AOC
from util.intcode.computer import IntcodeComputer

aoc = AOC(year=2019, day=5)
data = aoc.load()

# Part 1

computer = IntcodeComputer(data)
computer.state.add_input(1)
computer.run()
aoc.p1(computer.state.outputs[-1])

# Part 2

computer = IntcodeComputer(data)
computer.state.add_input(5)
computer.run()
aoc.p1(computer.state.outputs[-1])
