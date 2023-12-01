from lib.challenge import Challenge
from lib.commands.command import Command
from lib.language.language_id import LanguageID
from os import path
from typing import Any, Optional
import json


_cache_file = ".aoc_cache"


class Session:
    command: Command
    command_args: Any

    token: Optional[str]
    language: Optional[LanguageID]
    challenge: Optional[Challenge]
    base_directory: str

    def __init__(self, command: Command, command_args: Any):
        self.command = command
        self.command_args = command_args
        self.token = None
        self.language = None
        self.challenge = None
        self.base_directory = path.realpath(".")

        if path.exists(_cache_file):
            with open(_cache_file) as f:
                cache = json.load(f)
                self.token = cache["token"]
                self.language = LanguageID(cache["language"])
                self.challenge = Challenge(cache["year"], cache["day"])
        else:
            self.language = LanguageID.PYTHON # default to Python
            self.challenge = Challenge(year=2015, day=1) # default to 2015, day 1

        self.validate(require_token=False)

    @property
    def working_directory(self) -> str:
        return path.join(
            self.challenge.working_directory(self.base_directory), self.language.value
        )

    @property
    def input_file(self) -> str:
        return self.challenge.input_file(self.base_directory)

    @property
    def output_file(self) -> str:
        return self.challenge.output_file(self.base_directory)

    @property
    def log_file(self) -> str:
        return self.challenge.log_file(self.base_directory)

    def validate(self, require_token: bool = False):
        if require_token and not self.token:
            raise ValueError("token is not available")
        if not self.language:
            raise ValueError("language is not available")
        self.challenge.validate()

    def __repr__(self):
        return f"AOC {self.challenge}, {self.language.value}"

    def cache(self):
        values = {
            "token": self.token,
            "language": self.language.value,
            "year": self.challenge.year,
            "day": self.challenge.day,
        }

        with open(_cache_file, "w") as f:
            json.dump(values, f)
