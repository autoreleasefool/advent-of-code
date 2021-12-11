from datetime import datetime
from os import path
from typing import Optional
from util.data.data import Data
import requests
import sys


_SCRIPT_PATH = path.dirname(path.realpath(__file__))


class AOC:
    session: Optional[str] = None
    is_submitting: bool = False

    contains_test_input: bool = False
    force_skip_test: bool = False

    @classmethod
    def on_test_input_set(cls):
        AOC.contains_test_input = True

    def __init__(self, year: int, day: int):
        self.year = year
        self.day = day
        self.p1_solution = None
        self.p2_solution = None

    def load(self):
        if not path.exists(self._input_file):
            self._fetch(self._input_file)

        contents = None
        with open(self._input_file) as f:
            contents = f.read()

        if not contents:
            raise Exception(f"Failed to load input data ({self._input_file})")

        return Data(
            contents,
            force_skip_test=AOC.force_skip_test,
            on_test_input_set=AOC.on_test_input_set,
        )

    def d(self, s):
        print(s)
        sys.stdout.flush()

    def log(self, s):
        with open(self._log_file, "a") as f:
            f.write(f"{datetime.now()}: {s}\n")

    def p1(self, solution):
        self.p1_solution = solution
        if AOC.is_submitting:
            self.d(f"p1={solution}")
        else:
            self.d(solution)
        self.log(solution)

    def p2(self, solution):
        self.p2_solution = solution
        if AOC.is_submitting:
            self.d(f"p2={solution}")
        else:
            self.d(solution)
        self.log(solution)

    def _fetch(self, input_file):
        cookies = {"session": AOC.session}
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
            "..",
            str(self.year),
            f"day_{self.day}" if self.day >= 10 else f"day_0{self.day}",
            "input.txt",
        )

    @property
    def _log_file(self):
        return path.join(
            _SCRIPT_PATH,
            "..",
            "..",
            "..",
            "..",
            "..",
            str(self.year),
            f"day_{self.day}" if self.day >= 10 else f"day_0{self.day}",
            ".log",
        )
