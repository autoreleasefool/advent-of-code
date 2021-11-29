from aoc import AOC

aoc = AOC(year=2020, day=2)
data = aoc.load()


class Password:
    def __init__(self, groups):
        self.range = range(int(groups[0]), int(groups[1]) + 1)
        self.letter = groups[2]
        self.value = groups[3]

    def is_valid_legacy(self):
        return self.value.count(self.letter) in self.range

    def is_valid(self):
        return (self.value[min(self.range) - 1] == self.letter) ^ (
            self.value[max(self.range) - 1] == self.letter
        )


pass_regex = r"(\d+)-(\d+) (\w): (.+)"
aoc.p1(len([p for p in data.parse_lines(pass_regex, Password) if p.is_valid_legacy()]))
aoc.p2(len([p for p in data.parse_lines(pass_regex, Password) if p.is_valid()]))
