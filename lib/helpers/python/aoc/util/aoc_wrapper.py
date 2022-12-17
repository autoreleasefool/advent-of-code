from datetime import datetime
from typing import Optional
from util.data.data import Data
import sys


class AOC:
    token: Optional[str] = None
    is_submitting: bool = False

    input_file: Optional[str] = None
    log_file: Optional[str] = None

    skip_real_input: bool = False
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
        contents = None
        if AOC.input_file:
            with open(AOC.input_file) as f:
                contents = f.read()

        if not contents:
            raise Exception(f"Failed to load input data ({AOC.input_file})")

        return Data(
            contents,
            force_skip_test=AOC.force_skip_test,
            on_test_input_set=AOC.on_test_input_set,
        )

    def d(self, s):
        print(s)
        sys.stdout.flush()

    def log(self, s):
        if AOC.log_file:
            with open(AOC.log_file, "a") as f:
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
