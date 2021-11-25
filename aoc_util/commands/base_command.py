from abc import ABC, abstractmethod

from aoc_util.challenge import Challenge


class BaseCommand(ABC):
    @abstractmethod
    def run(challenge: Challenge):
        pass
