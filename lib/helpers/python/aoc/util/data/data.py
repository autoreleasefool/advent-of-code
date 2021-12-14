import json
import re
from types import FunctionType
from typing import Any, List
from util.data.regex import parse_number_line, parse_regex
from util.data.rules import Rule


class Data:
    def __init__(
        self, contents: str, force_skip_test: bool, on_test_input_set: FunctionType
    ):
        self._contents = contents
        self._original_contents = contents
        self.force_skip_test = force_skip_test
        self.on_test_input_set = on_test_input_set

    # Raw string contents
    def contents(self) -> str:
        return self._contents[:]

    # List of lines in the file
    def lines(self) -> List[str]:
        return self._contents.splitlines()

    # Length of the first line
    @property
    def line_length(self):
        return len(self.lines()[0])

    @property
    def test(self):
        return self._contents if self._contents != self._original_contents else None

    @test.setter
    def test(self, value):
        self.on_test_input_set()
        if self.force_skip_test:
            return
        self._contents = value

    # List of numbers in the file, when they are separated 1 number per line
    def numbers(self) -> List[int]:
        return [int(re.search(r"-?\d+", line).group(0)) for line in self.lines()]

    def digits_by_line(self) -> List[List[int]]:
        return [[int(x) for x in l] for l in self.lines()]

    def nums(self) -> List[int]:
        return [int(x) for x in re.findall(r"-?\d+", self.contents())]

    # List of numbers in the file, with multiple numbers per line
    def numbers_by_line(self) -> List[List[int]]:
        return [parse_number_line(line) for line in self.lines()]

    # JSON contents
    def json(self) -> Any:
        return json.loads(self._contents)

    # Parse as a table. `data` should be a list of 'w' or 'd'
    # 'd' columns are parsed as integers, 'w' columns are strings
    # `sep` can be provided to split the columns on a different value
    def table(self, data, sep=","):
        return [
            [
                int(col[1]) if col[0] == "d" else col[1]
                for col in zip(data, line.split(sep))
            ]
            for line in self.lines()
        ]

    # List of lines in the file, parsed by a regex.
    # The groups from the regex match are passed to `container`, which returns a list by default
    # But could be an initializer or namedtuple, etc.
    # SEE 2020/day_02
    def parse_lines(self, regex, container=list, intify=True):
        return [parse_regex(regex, line, container, intify) for line in self.lines()]

    def parse(self, regex, container=list, intify=True):
        return self.parse_lines(regex, container, intify)

    # Define with Rules how multiple chunks of the content will be parsed. A Rule will be used until a line
    # fails to parse, or the max count is reached
    # SEE 2020/day_16
    def chunk(self, rules: List[Rule]):
        lines = self.lines()

        chunks = []
        current_chunk = []
        rule = rules.pop(0)
        line = lines.pop(0)

        while line is not None and rule is not None:
            chunk, applied = rule.apply(line)
            rule.count -= 1

            if chunk:
                current_chunk.append(chunk)

            if rule.count == 0 or not applied:
                if rule.returns_chunks:
                    chunks.append(current_chunk)

                current_chunk = []
                rule = rules.pop(0) if rules else None

            if applied:
                line = lines.pop(0) if lines else None

        if rule and rule.returns_chunks:
            chunks.append(current_chunk)

        return chunks
