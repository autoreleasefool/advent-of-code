from aoc import AOC, flatten
import math


aoc = AOC(year=2020, day=16)
data = aoc.load()

chunks = data.parse_by_chunks(
    [
        {"type": "regex", "value": r"^(.*): (\d+)-(\d+) or (\d+)-(\d+)"},
        {"type": "drop", "count": 2},
        {"type": "numbers", "count": 1},
        {"type": "drop", "count": 2},
        {"type": "numbers"},
    ]
)

your_ticket = chunks[1][0]
tickets = chunks[2]
rules = {
    m[0]: [range(int(m[1]), int(m[2]) + 1), range(int(m[3]), int(m[4]) + 1)]
    for m in chunks[0]
}

# Part 1

all_rule_values = flatten(rules.values())


def is_valid_for_some_field(v):
    return any(v in x for x in all_rule_values)


aoc.p1(sum(sum(0 if is_valid_for_some_field(v) else v for v in t) for t in tickets))

# Part 2

tickets = [t for t in tickets if all(is_valid_for_some_field(v) for v in t)]
field_indices = {r: set(range(len(tickets[0]))) for r in rules.keys()}
confirmed_fields = set()

for t in tickets:
    for i, v in enumerate(t):
        for r in rules:
            if not any(v in x for x in rules[r]):
                field_indices[r].remove(i)

while True:
    nf = next(
        (
            f
            for f in field_indices
            if f not in confirmed_fields and len(field_indices[f]) == 1
        ),
        None,
    )
    if not nf:
        break

    idx, next_field = next(iter(field_indices[nf])), nf
    for f in field_indices:
        if f == next_field or idx not in field_indices[f]:
            continue
        field_indices[f].remove(idx)
    confirmed_fields.add(next_field)

aoc.p2(
    math.prod(
        [
            your_ticket[next(iter(field_indices[x]))]
            for x in field_indices
            if "departure " in x
        ]
    )
)
