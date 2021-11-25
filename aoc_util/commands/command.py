from abc import abstractmethod, ABC
from enum import Enum

from aoc_util.challenge import Challenge
from aoc_util.commands.create import Create
from aoc_util.commands.fetch import Fetch
from aoc_util.commands.open import Open
from aoc_util.session import Session


class Command(Enum):
  CREATE = 'create'
  FETCH = 'fetch'
  OPEN = 'open'
  RUN = 'run'
  TEST = 'test'

  def run(self, session: Session):
    match self:
      case Command.CREATE:
        Create().run(session)
      case Command.FETCH:
        Fetch().run(session)
      case Command.OPEN:
        Open().run(session)
      # case Command.RUN:
      #   Run().run(session)
      # case Command.TEST:
      #   Test().run(session)