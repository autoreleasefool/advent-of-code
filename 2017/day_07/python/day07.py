from aoc import AOC


aoc = AOC(year=2017, day=7)
data = aoc.load()


## Part 1


class Program:
    def __init__(self, params):
        components = params.split()
        self.name = components[0]
        self.weight = int(components[1][1:-1])
        self.heldPrograms = []

        if len(components) > 2:
            self.heldPrograms = [
                name if name[-1] != "," else name[0:-1] for name in components[3:]
            ]


programMap = {}
for line in data.lines():
    program = Program(line)
    programMap[program.name] = program

subPrograms = {
    program
    for programName in programMap
    for program in programMap[programName].heldPrograms
}
baseProgram = "".join([x for x in programMap if x not in subPrograms])

aoc.p1(baseProgram)


## Part 2


class Program:
    def __init__(self, params):
        components = params.split()
        self.name = components[0]
        self.weight = int(components[1][1:-1])
        self.held_programs = []

        if len(components) > 2:
            self.held_programs = [
                name if name[-1] != "," else name[0:-1] for name in components[3:]
            ]

    def total_weight(self):
        weight = self.weight
        sub_program_weights = [
            program_map[name].total_weight() for name in self.held_programs
        ]
        if not sub_program_weights:
            return weight
        sub_weight = sum(sub_program_weights)
        return weight + sub_weight


program_map = {}
for line in data.lines():
    program = Program(line)
    program_map[program.name] = program

sub_programs = {
    program
    for program_name in program_map
    for program in program_map[program_name].held_programs
}
base_program_name = [x for x in program_map if x not in sub_programs][0]
base_program = program_map[base_program_name]
base_weight = base_program.total_weight()

aoc.p2(base_weight)
