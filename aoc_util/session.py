from os import path
from typing import Any, List, Optional
import json

from aoc_util.challenge import Challenge
from aoc_util.commands.command import Command
from aoc_util.language import Language


_cache_file = ".aoc_cache"


class Session:
    command: Command
    command_args: Any

    token: Optional[str]
    language: Optional[Language]
    challenge: Optional[Challenge]

    def __init__(self, command: Command, command_args: Any):
        self.command = command
        self.command_args = command_args
        self.token = None
        self.language = None
        self.challenge = None

        if path.exists(_cache_file):
            with open(_cache_file) as f:
                cache = json.load(f)
                self.token = cache["token"]
                self.language = Language(cache["language"])
                self.challenge = Challenge(cache["year"], cache["day"])

        self.validate(require_token=False)

    @property
    def working_directory(self):
        return path.join(self.challenge.working_directory, self.language.value)

    @property
    def compilation_directory(self):
        if self.language == Language.PYTHON:
            return path.join(".", "helpers", "python")
        elif self.language == Language.RUST:
            return self.working_directory
        elif self.language == Language.SWIFT:
            return self.working_directory
        elif self.language == Language.RUBY:
            return None
        elif self.language == Language.HASKELL:
            return None

    @property
    def root_file(self):
        return path.join(
            self.working_directory,
            self.language.src_prefix if self.language.src_prefix else "",
            f"day{self.challenge.day_with_padding}{self.language.file_extension}",
        )

    @property
    def compiled_file(self):
        extension = self.language.compiled_extension
        if not extension:
            return None

        return path.join(
            path.dirname(path.realpath(__file__)),
            "..",
            str(self.challenge.year),
            f"day_{self.challenge.day_with_padding}",
            self.language.value,
            f"day{self.challenge.day_with_padding}{self.language.compiled_extension}",
        )

    def validate(self, require_token: bool = False):
        if require_token and not self.token:
            raise ValueError("token is not available")
        if not self.language:
            raise ValueError("language is not available")
        self.challenge.validate()

    def cache(self):
        values = {
            "token": self.token,
            "language": self.language.value,
            "year": self.challenge.year,
            "day": self.challenge.day,
        }

        with open(_cache_file, "w") as f:
            json.dump(values, f)
