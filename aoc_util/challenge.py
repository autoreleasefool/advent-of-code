from dataclasses import dataclass
from os import path


@dataclass
class Challenge:
    year: int
    day: int

    @property
    def url(self):
        return f"https://adventofcode.com/{self.year}/day/{self.day}"

    @property
    def input_url(self):
        return f"{self.url}/input"

    @property
    def working_directory(self):
        return path.join(".", str(self.year), f"day_{self.day_with_padding}")

    @property
    def input_file(self):
        return path.join(self.working_directory, "input.txt")

    @property
    def output_file(self):
        return path.join(self.working_directory, "output.txt")

    @property
    def day_with_padding(self):
        return str(self.day) if self.day >= 10 else f"0{self.day}"

    def validate(self):
        if not self.year:
            raise ValueError("year is not available")
        if not self.day:
            raise ValueError("day is not available")

    def __repr__(self):
        return f"challenge({self.year}, {self.day})"
