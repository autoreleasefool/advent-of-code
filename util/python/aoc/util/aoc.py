from .data import Data
from os import path
from typing import Optional
import requests
import sys


_SCRIPT_PATH = path.dirname(path.realpath(__file__))


class AOC:
    _session: Optional[str] = None

    def __init__(self, year: int, day: int):
        self.year = year
        self.day = day

    def load(self):
        if not path.exists(self._input_file):
            self._fetch(self._input_file)

        contents = None
        with open(self._input_file) as f:
            contents = f.read()

        if not contents:
            raise Exception(f"Failed to load input data ({self._input_file})")

        return Data(contents)

    def d(self, s):
        print(s)
        sys.stdout.flush()

    def p1(self, solution):
        self.d(solution)

    def p2(self, solution):
        self.d(solution)

    def _fetch(self, input_file):
        cookies = {"session": AOC._session}
        r = requests.get(
            f"https://adventofcode.com/{self.year}/day/{self.day}/input",
            cookies=cookies,
        )

        with open(input_file, "w") as f:
            f.write(r.text)

    @property
    def _input_file(self):
        return path.join(
            _SCRIPT_PATH,
            "..",
            "..",
            "..",
            "..",
            str(self.year),
            f"day_{self.day}" if self.day >= 10 else f"day_0{self.day}",
            "input.txt",
        )
