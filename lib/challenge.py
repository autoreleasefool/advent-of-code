from dataclasses import dataclass
from os import path


@dataclass
class Challenge:
    year: int
    day: int

    @property
    def url(self) -> str:
        return f"https://adventofcode.com/{self.year}/day/{self.day}"

    @property
    def input_url(self) -> str:
        return f"{self.url}/input"

    @property
    def submit_url(self) -> str:
        return f"{self.url}/answer"

    def working_directory(self, base_directory: str) -> str:
        return path.join(base_directory, str(self.year), f"day_{self.day_with_padding}")

    def input_file(self, base_directory: str) -> str:
        return path.join(self.working_directory(base_directory), "input.txt")

    def output_file(self, base_directory: str) -> str:
        return path.join(self.working_directory(base_directory), "output.txt")

    def log_file(self, base_directory: str) -> str:
        return path.join(self.working_directory(base_directory), ".log")

    @property
    def day_with_padding(self) -> str:
        return str(self.day) if self.day >= 10 else f"0{self.day}"

    def validate(self):
        if not self.year:
            raise ValueError("year is not available")
        if not self.day:
            raise ValueError("day is not available")

    def __repr__(self):
        return f"challenge({self.year}, {self.day})"
