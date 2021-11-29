from genericpath import exists
from os import path
from typing import Optional
import json

from aoc_util.challenge import Challenge
from aoc_util.language import Language

_cache_file = ".aoc_cache"


class Session:
    token: str
    language: Language
    challenge: Challenge
    save: bool

    def __init__(
        self,
        token: Optional[str],
        language: Optional[Language],
        year: Optional[int],
        day: Optional[int],
        save: bool,
    ):
        self.token = token
        self.language = language
        self.challenge = Challenge(year, day)
        self.save = save

        if path.exists(_cache_file):
            with open(_cache_file) as f:
                cache = json.load(f)
                self.token = token if token else cache["token"]
                self.language = language if language else Language(cache["language"])
                self.challenge = Challenge(
                    year if year else cache["year"], day if day else cache["day"]
                )

        self.validate(require_token=False)
        self._cache()

    def session_with_day(self, day: int):
        return Session(
            token=self.token,
            language=self.language,
            year=self.challenge.year,
            day=day,
            save=self.save,
        )

    @property
    def working_directory(self):
        return path.join(self.challenge.working_directory, self.language.value)

    @property
    def compilation_directory(self):
        if self.language == Language.PYTHON:
            return path.join(".", "util", "python")
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

    def _cache(self):
        values = {
            "token": self.token,
            "language": self.language.value,
            "year": self.challenge.year,
            "day": self.challenge.day,
        }

        with open(_cache_file, "w") as f:
            json.dump(values, f)
