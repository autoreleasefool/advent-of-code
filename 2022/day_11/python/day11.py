from aoc import AOC, parse_number_line, chinese_remainder, chunk
from dataclasses import dataclass, field
from typing import List

aoc = AOC(year=2022, day=11)
data = aoc.load()

@dataclass
class TestCase:
    value: int
    if_true: int
    if_false: int

@dataclass
class Monkey:
    items: List[int]
    operation: str
    test: TestCase
    inspections: int = 0

def get_monkeys():
    monkeys = []
    for monkey in chunk(7, data.lines()):
        monkeys.append(
            Monkey(
                items=parse_number_line(monkey[1]),
                operation=monkey[2].split(' = ')[1],
                test=TestCase(
                    value=parse_number_line(monkey[3])[0],
                    if_true=parse_number_line(monkey[4])[0],
                    if_false=parse_number_line(monkey[5])[0]
                )
            )
        )
    return monkeys

def perform_round(part: int):
    divisors = [m.test.value for m in monkeys]

    for monkey in monkeys:
        while monkey.items:
            item = monkey.items.pop(0)
            item = eval(monkey.operation.replace('old', str(item)))
            monkey.inspections += 1

            if part == 1:
                item //= 3
            elif part == 2:
                item = chinese_remainder(divisors, [item % d for d in divisors])

            dest = monkey.test.if_true if item % monkey.test.value == 0 else monkey.test.if_false
            monkeys[dest].items.append(item)

def monkey_business():
    m = sorted(monkeys, key=lambda m: m.inspections)
    return m[-1].inspections * m[-2].inspections

monkeys = get_monkeys()
for _ in range(20):
    perform_round(part=1)
aoc.p1(monkey_business())

monkeys = get_monkeys()
for _ in range(10000):
    perform_round(part=2)
aoc.p2(monkey_business())
