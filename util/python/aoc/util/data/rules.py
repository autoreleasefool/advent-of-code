from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Tuple
from util.data.regex import parse_number_line, parse_regex
import math


class Rule(ABC):
    count: int
    returns_chunks: bool

    @abstractmethod
    def apply(self, line: str) -> Tuple[Any, bool]:
        pass


@dataclass
class Drop(Rule):
    count: int = math.inf
    returns_chunks = False

    def apply(self, line: str):
        return (None, True)


@dataclass
class Numbers(Rule):
    count: int = math.inf
    returns_chunks = True

    def apply(self, line: str):
        numbers = parse_number_line(line)
        if not numbers:
            return (None, False)
        return (numbers if len(numbers) > 1 else numbers[0], True)


@dataclass
class Regex(Rule):
    regex: str
    count: int = math.inf
    returns_chunks = True

    def apply(self, line: str):
        parsed = parse_regex(self.regex, line)
        return (parsed, parsed is not None)


@dataclass
class String(Rule):
    count: int = math.inf
    returns_chunks = True

    def apply(self, line: str):
        return (line, True)
