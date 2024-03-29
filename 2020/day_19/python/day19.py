from aoc import AOC, Regex, Drop, String
import re
from functools import lru_cache

aoc = AOC(year=2020, day=19)
data = aoc.load()


chunks = data.chunk(
    [
        Regex(r"^(\d.*)$"),
        Drop(1),
        String(),
    ]
)

rules = {
    int(m[0][: m[0].find(":")]): [
        s[1] if '"' in s else [int(x) for x in s.split(" ")]
        for s in m[0][m[0].find(" ") + 1 :].split(" | ")
    ]
    for m in chunks[0]
}

"""
Given input:
0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"

`rules` will be:
{
    0: [[1, 2]],
    1: ['a'],
    2: [[1, 3], [3, 1]],
    3: ['b']
}
"""

# Part 1


def resolve_rule(r):
    @lru_cache
    def resolver(r):
        if type(rules[r][0]) is str:
            return rules[r][0]
        else:
            return (
                "("
                + "|".join(["".join([resolver(y) for y in x]) for x in rules[r]])
                + ")"
            )

    return "^" + resolver(r) + "$"


rule_zero = resolve_rule(0)
aoc.p1(len([1 for x in chunks[1] if re.match(rule_zero, x)]))

# Part 2

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]


def resolve_infinite_rule(r):
    @lru_cache
    def manual_resolution(r):
        if r == 8:
            return "(" + resolver(42) + ")" + "+"
        elif r == 11:
            return (
                "("
                + "|".join([resolver(42) * i + resolver(31) * i for i in range(1, 5)])
                + ")"
            )
        return ""

    @lru_cache
    def resolver(r):
        if type(rules[r][0]) is str:
            return rules[r][0]
        else:
            return (
                "("
                + "|".join(
                    [
                        "".join(
                            [
                                manual_resolution(y) if y in [8, 11] else resolver(y)
                                for y in x
                            ]
                        )
                        for x in rules[r]
                    ]
                )
                + ")"
            )

    return "^" + resolver(r) + "$"


rule_zero = resolve_infinite_rule(0)
aoc.p2(len([1 for x in chunks[1] if re.match(rule_zero, x)]))
