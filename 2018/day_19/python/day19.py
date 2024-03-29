from aoc import AOC


aoc = AOC(year=2018, day=19)
data = aoc.load()


def addr(A, B, C, reg):
    reg[C] = reg[A] + reg[B]


def addi(A, B, C, reg):
    reg[C] = reg[A] + B


def mulr(A, B, C, reg):
    reg[C] = reg[A] * reg[B]


def muli(A, B, C, reg):
    reg[C] = reg[A] * B


def banr(A, B, C, reg):
    reg[C] = reg[A] & reg[B]


def bani(A, B, C, reg):
    reg[C] = reg[A] & B


def borr(A, B, C, reg):
    reg[C] = reg[A] | reg[B]


def bori(A, B, C, reg):
    reg[C] = reg[A] | B


def setr(A, _, C, reg):
    reg[C] = reg[A]


def seti(A, _, C, reg):
    reg[C] = A


def gtir(A, B, C, reg):
    reg[C] = 1 if A > reg[B] else 0


def gtri(A, B, C, reg):
    reg[C] = 1 if reg[A] > B else 0


def gtrr(A, B, C, reg):
    reg[C] = 1 if reg[A] > reg[B] else 0


def eqir(A, B, C, reg):
    reg[C] = 1 if A == reg[B] else 0


def eqri(A, B, C, reg):
    reg[C] = 1 if reg[A] == B else 0


def eqrr(A, B, C, reg):
    reg[C] = 1 if reg[A] == reg[B] else 0


op_map = {
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr,
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtir": gtir,
    "gtri": gtri,
    "gtrr": gtrr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr,
}

registers = [0] * 6
ip_reg = 0
program = []

for line in data.lines():
    if "#ip" in line:
        ip_reg = int(line[4])
        ip = registers[ip_reg]
    else:
        instruction = line.split(" ")
        program.append([instruction[0]] + [int(i) for i in instruction[1:]])

while ip in range(0, len(program)):
    instruction = program[ip]
    registers[ip_reg] = ip
    op_map[instruction[0]](instruction[1], instruction[2], instruction[3], registers)
    ip = registers[ip_reg] + 1

aoc.p1(registers[0])


## Part 2


# Solved manually
aoc.p2(25165632)
