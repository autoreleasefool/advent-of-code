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

    def __init__(
        self,
        token: Optional[str],
        language: Optional[Language],
        year: Optional[int],
        day: Optional[int],
    ):
        self.token = token
        self.language = language
        self.challenge = Challenge(year, day)

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

    @property
    def working_directory(self):
        return path.join(self.challenge.working_directory, self.language.value)

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
