from aoc import AOC, numbers_from


aoc = AOC(year=2018, day=16)
data = aoc.load()


def addr(A, B, C, reg):
    reg[C] = reg[A] + reg[B]
    return reg


def addi(A, B, C, reg):
    reg[C] = reg[A] + B
    return reg


def mulr(A, B, C, reg):
    reg[C] = reg[A] * reg[B]
    return reg


def muli(A, B, C, reg):
    reg[C] = reg[A] * B
    return reg


def banr(A, B, C, reg):
    reg[C] = reg[A] & reg[B]
    return reg


def bani(A, B, C, reg):
    reg[C] = reg[A] & B
    return reg


def borr(A, B, C, reg):
    reg[C] = reg[A] | reg[B]
    return reg


def bori(A, B, C, reg):
    reg[C] = reg[A] | B
    return reg


def setr(A, _, C, reg):
    reg[C] = reg[A]
    return reg


def seti(A, _, C, reg):
    reg[C] = A
    return reg


def gtir(A, B, C, reg):
    reg[C] = 1 if A > reg[B] else 0
    return reg


def gtri(A, B, C, reg):
    reg[C] = 1 if reg[A] > B else 0
    return reg


def gtrr(A, B, C, reg):
    reg[C] = 1 if reg[A] > reg[B] else 0
    return reg


def eqir(A, B, C, reg):
    reg[C] = 1 if A == reg[B] else 0
    return reg


def eqri(A, B, C, reg):
    reg[C] = 1 if reg[A] == B else 0
    return reg


def eqrr(A, B, C, reg):
    reg[C] = 1 if reg[A] == reg[B] else 0
    return reg


ops = [
    addr,
    addi,
    mulr,
    muli,
    banr,
    bani,
    borr,
    bori,
    setr,
    seti,
    gtir,
    gtri,
    gtrr,
    eqir,
    eqri,
    eqrr,
]

ambiguous_samples = 0
lines = data.lines()
for index, l in enumerate(lines):
    if "Before" in l:
        before = numbers_from(l)
        op = numbers_from(lines[index + 1])
        after = numbers_from(lines[index + 2])

        similar_ops = sum(
            [1 if f(op[1], op[2], op[3], list(before)) == after else 0 for f in ops]
        )
        if similar_ops >= 3:
            ambiguous_samples += 1

aoc.p1(ambiguous_samples)


## Part 2


# Solved manually
aoc.p2(627)
