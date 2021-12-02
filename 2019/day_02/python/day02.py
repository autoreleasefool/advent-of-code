from aoc import AOC, IntcodeComputer

aoc = AOC(year=2019, day=2)

computer = IntcodeComputer(aoc)
computer.program[1] = 12
computer.program[2] = 2
computer.run()

aoc.p1(computer.program[0])


def find_noun_and_verb():
    for noun in range(100):
        for verb in range(100):
            computer = IntcodeComputer(aoc)
            computer.program[1] = noun
            computer.program[2] = verb
            computer.run()
            if computer.output == 19690720:
                return noun, verb


noun, verb = find_noun_and_verb()
aoc.p2(100 * noun + verb)
